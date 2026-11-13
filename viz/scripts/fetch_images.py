import base64
import concurrent.futures
import html
import json
import re
import shutil
import threading
import time
from io import BytesIO
from pathlib import Path
from urllib.parse import quote, unquote, urljoin, urlparse

import requests
from bs4 import BeautifulSoup
from PIL import Image

try:
    from .data_common import DATA_DIR, VIZ_ROOT, assign_node_ids, parse_value, read_json, rows_by_kind, url_indexes
    from .normalize import canon, norm, slugify
except ImportError:
    from data_common import DATA_DIR, VIZ_ROOT, assign_node_ids, parse_value, read_json, rows_by_kind, url_indexes
    from normalize import canon, norm, slugify


IMAGE_ROOT = VIZ_ROOT / "web" / "public" / "img"
USER_AGENT = "42ai-robotics-maps/0.1 (+https://42ai.fr)"
THREADS = 16
MIN_SIZE = 32
MAX_SIDE = 256
DOMAIN_INTERVAL = 0.2

_domain_lock = threading.Lock()
_domain_last_request = {}
_thread_local = threading.local()


def session():
    if not hasattr(_thread_local, "session"):
        client = requests.Session()
        client.headers.update({"User-Agent": USER_AGENT})
        _thread_local.session = client
    return _thread_local.session


def polite(url):
    domain = urlparse(url).netloc.lower()
    if not domain:
        return
    with _domain_lock:
        now = time.monotonic()
        delay = DOMAIN_INTERVAL - (now - _domain_last_request.get(domain, 0))
        if delay > 0:
            time.sleep(delay)
        _domain_last_request[domain] = time.monotonic()


def fetch(url, timeout=12):
    polite(url)
    response = session().get(url, timeout=timeout, allow_redirects=True)
    response.raise_for_status()
    return response.content, response.url, response.headers.get("content-type", "")


def cdp_html(url):
    try:
        import websocket
    except ImportError:
        return None

    target = None
    endpoint = f"http://localhost:29229/json/new?{quote(url, safe='')}"
    try:
        response = requests.put(endpoint, timeout=8)
        response.raise_for_status()
        target = response.json()
    except requests.RequestException:
        try:
            response = requests.get(endpoint, timeout=8)
            response.raise_for_status()
            target = response.json()
        except requests.RequestException:
            return None
    try:
        socket = websocket.create_connection(
            target["webSocketDebuggerUrl"], timeout=12, suppress_origin=True
        )
        socket.send(json.dumps({
            "id": 1,
            "method": "Runtime.evaluate",
            "params": {
                "expression": "document.documentElement ? document.documentElement.outerHTML : document.head.innerHTML",
                "returnByValue": True,
                "awaitPromise": True,
            },
        }))
        while True:
            message = json.loads(socket.recv())
            if message.get("id") == 1:
                return message.get("result", {}).get("result", {}).get("value")
    except Exception:
        return None
    finally:
        try:
            socket.close()
        except Exception:
            pass


def page_html(url):
    try:
        content, final_url, content_type = fetch(url)
        if "html" in content_type.lower() or b"<html" in content[:500].lower():
            return content.decode("utf-8", errors="replace"), final_url, "http"
    except requests.RequestException:
        pass
    markup = cdp_html(url)
    if markup:
        return markup, url, "chrome-cdp"
    return None, url, "unavailable"


def _attrs_text(element):
    attrs = []
    for key in ("src", "alt", "class", "id", "aria-label", "title"):
        value = element.get(key)
        if isinstance(value, list):
            value = " ".join(value)
        if value:
            attrs.append(str(value))
    return " ".join(attrs).lower()


def _logo_candidates(soup, page_url):
    scope = soup.find("header") or soup
    candidates = []
    for element in scope.find_all(["img", "svg"]):
        match = _attrs_text(element)
        if "logo" not in match:
            for parent in element.parents:
                if getattr(parent, "name", None) in ("a", "div", "header"):
                    if "logo" in _attrs_text(parent):
                        match = "logo"
                        break
        if "logo" not in match:
            continue
        if element.name == "img" and element.get("src"):
            candidates.append((urljoin(page_url, element["src"]), "header-logo"))
        elif element.name == "svg":
            candidates.append((str(element), "inline-svg-logo"))

    for link in soup.find_all("link", rel=lambda value: value and "apple-touch-icon" in value):
        if link.get("href"):
            candidates.append((urljoin(page_url, link["href"]), "apple-touch-icon"))
    for link in soup.find_all("link", rel=lambda value: value and "icon" in value):
        href = link.get("href")
        if not href:
            continue
        sizes = link.get("sizes", "").lower()
        is_svg = "svg" in (link.get("type", "") + href).lower()
        dimensions = [int(size) for size in re.findall(r"\d+", sizes)]
        if is_svg or max(dimensions, default=0) >= 64:
            candidates.append((urljoin(page_url, href), "site-icon"))
    return candidates


def _meta_image(soup):
    for selectors in (
        {"property": "og:image"},
        {"name": "twitter:image"},
        {"name": "twitter:image:src"},
    ):
        item = soup.find("meta", attrs=selectors)
        if item and item.get("content"):
            return html.unescape(item["content"])
    return None


def github_parts(url):
    match = re.search(r"(?:github\.com|githubusercontent\.com)/([^/\s?#]+)/([^/\s?#]+)", url, re.I)
    if not match:
        return None
    owner, repo = match.groups()
    repo = repo.removesuffix(".git")
    return owner, repo


def image_bytes(candidate):
    if candidate.startswith("<svg"):
        import cairosvg
        return cairosvg.svg2png(bytestring=candidate.encode("utf-8")), "image/png"
    if candidate.startswith("data:"):
        header, payload = candidate.split(",", 1)
        if ";base64" in header:
            data = base64.b64decode(payload)
        else:
            data = unquote(payload).encode("utf-8")
        content_type = header[5:].split(";", 1)[0]
        if "svg" in content_type:
            import cairosvg
            data = cairosvg.svg2png(bytestring=data)
            content_type = "image/png"
        return data, content_type
    payload, _, content_type = fetch(candidate)
    if "svg" in content_type.lower() or candidate.lower().split("?", 1)[0].endswith(".svg"):
        import cairosvg
        payload = cairosvg.svg2png(bytestring=payload)
        content_type = "image/png"
    return payload, content_type


def save_webp(payload, target):
    try:
        image = Image.open(BytesIO(payload))
        if getattr(image, "n_frames", 1) > 1:
            image.seek(0)
        image.load()
    except Exception:
        return False, "invalid-image"
    if image.width < MIN_SIZE or image.height < MIN_SIZE:
        return False, f"too-small:{image.width}x{image.height}"
    if image.mode not in ("RGB", "RGBA"):
        image = image.convert("RGBA" if "transparency" in image.info else "RGB")
    image.thumbnail((MAX_SIDE, MAX_SIDE), Image.Resampling.LANCZOS)
    image.save(target, "WEBP", quality=90, method=6)
    return True, None


def org_source_urls(row):
    fields = {key: parse_value(value) for key, value in row.get("props", {}).items()}
    candidates = []
    website = fields.get("Website")
    if isinstance(website, str) and website.startswith(("https://", "http://")):
        candidates.append(website)
    sources = fields.get("Sources", "")
    candidates.extend(re.findall(r"https?://[^\s;,\])}\"']+", str(sources)))
    return list(dict.fromkeys(candidates)), fields


def robot_source_urls(row):
    fields = {key: parse_value(value) for key, value in row.get("props", {}).items()}
    sources = fields.get("Sources", "")
    urls = re.findall(r"https?://[^\s;,\])}\"']+", str(sources))
    return list(dict.fromkeys(urls)), fields


def wikipedia_image(name):
    params = {
        "action": "query",
        "generator": "search",
        "gsrsearch": name,
        "gsrlimit": 1,
        "prop": "pageimages",
        "piprop": "original",
        "format": "json",
    }
    try:
        data, _, _ = fetch("https://en.wikipedia.org/w/api.php?" + requests.compat.urlencode(params))
        payload = json.loads(data)
    except Exception:
        return None
    pages = payload.get("query", {}).get("pages", {})
    if not pages:
        return None
    page = next(iter(pages.values()))
    requested = {token for token in re.findall(r"[a-z0-9]+", norm(name)) if len(token) > 2}
    title = {token for token in re.findall(r"[a-z0-9]+", norm(page.get("title", ""))) if len(token) > 2}
    if not requested or len(requested & title) / len(requested) < 0.8:
        return None
    return page.get("original", {}).get("source")


def _try_candidate(candidate, method, target):
    try:
        payload, _ = image_bytes(candidate)
        saved, error = save_webp(payload, target)
        if saved:
            return {"source": candidate if candidate.startswith("http") else "inline-svg", "method": method}
        return None, error
    except Exception as error:
        return None, str(error)


def fetch_org_image(item):
    row, node_id = item
    slug = node_id.split(":", 1)[1]
    target = IMAGE_ROOT / "orgs" / f"{slug}.webp"
    if target.exists():
        return node_id, f"/img/orgs/{target.name}", {"source": str(target), "method": "existing"}

    urls, fields = org_source_urls(row)
    errors = []
    for page_url in urls:
        markup, final_url, page_method = page_html(page_url)
        if not markup:
            errors.append(f"{page_url}: page unavailable")
            continue
        soup = BeautifulSoup(markup, "html.parser")
        for candidate, method in _logo_candidates(soup, final_url):
            result = _try_candidate(candidate, method, target)
            if isinstance(result, tuple):
                _, failure = result
                errors.append(f"{candidate}: {failure}")
                continue
            return node_id, f"/img/orgs/{target.name}", {
                "source": candidate if candidate.startswith("http") else page_url,
                "method": method if page_method == "http" else f"{method}+chrome-cdp",
            }

    domains = []
    for url in urls:
        host = urlparse(url).hostname
        if host:
            domains.append(host.removeprefix("www."))
    for domain in dict.fromkeys(domains):
        favicon = f"https://www.google.com/s2/favicons?domain={quote(domain)}&sz=256"
        result = _try_candidate(favicon, "google-favicon", target)
        if isinstance(result, tuple):
            errors.append(f"{favicon}: {result[1]}")
            continue
        return node_id, f"/img/orgs/{target.name}", {"source": favicon, "method": "google-favicon"}

    for url in urls:
        parts = github_parts(url)
        if parts:
            avatar = f"https://github.com/{parts[0]}.png?size=256"
            result = _try_candidate(avatar, "github-avatar", target)
            if not isinstance(result, tuple):
                return node_id, f"/img/orgs/{target.name}", {"source": avatar, "method": "github-avatar"}
            errors.append(f"{avatar}: {result[1]}")
    return node_id, None, {
        "source": urls[0] if urls else fields.get("Website"),
        "method": None,
        "failure": "; ".join(errors[-5:]) or "no website or usable source",
    }


def _site_image(url, target):
    markup, final_url, page_method = page_html(url)
    if not markup:
        return None, "page unavailable"
    soup = BeautifulSoup(markup, "html.parser")
    candidate = _meta_image(soup)
    if not candidate:
        return None, "no og:image or twitter:image"
    candidate = urljoin(final_url, candidate)
    result = _try_candidate(candidate, "social-image", target)
    if isinstance(result, tuple):
        return None, result[1]
    return {"source": candidate, "method": "social-image" if page_method == "http" else "social-image+chrome-cdp"}, None


def fetch_robot_image(item, org_ids, org_images):
    row, node_id = item
    slug = node_id.split(":", 1)[1]
    target = IMAGE_ROOT / "robots" / f"{slug}.webp"
    if target.exists():
        return node_id, f"/img/robots/{target.name}", {"source": str(target), "method": "existing"}
    urls, fields = robot_source_urls(row)
    errors = []

    is_github_relevant = fields.get("Kind") in ("Simulator/Tool", "AI model")
    if is_github_relevant:
        for url in urls:
            parts = github_parts(url)
            if not parts:
                continue
            owner, repo = parts
            opengraph = f"https://opengraph.githubassets.com/1/{owner}/{repo}"
            result = _try_candidate(opengraph, "github-opengraph", target)
            if not isinstance(result, tuple):
                return node_id, f"/img/robots/{target.name}", {"source": opengraph, "method": "github-opengraph"}
            errors.append(f"{opengraph}: {result[1]}")
            avatar = f"https://github.com/{owner}.png?size=256"
            result = _try_candidate(avatar, "github-avatar", target)
            if not isinstance(result, tuple):
                return node_id, f"/img/robots/{target.name}", {"source": avatar, "method": "github-avatar"}
            errors.append(f"{avatar}: {result[1]}")

    for url in urls[:5]:
        result, error = _site_image(url, target)
        if result:
            return node_id, f"/img/robots/{target.name}", result
        errors.append(f"{url}: {error}")

    wiki = wikipedia_image(row["name"])
    if wiki:
        result = _try_candidate(wiki, "wikipedia-pageimage", target)
        if not isinstance(result, tuple):
            return node_id, f"/img/robots/{target.name}", {"source": wiki, "method": "wikipedia-pageimage"}
        errors.append(f"{wiki}: {result[1]}")

    builders = row.get("rels", {}).get("Built by", [])
    builders = builders if isinstance(builders, list) else [builders]
    for builder in builders:
        org_id = org_ids.get(norm(canon(builder)))
        logo = org_images.get(org_id) if org_id else None
        if logo:
            org_path = IMAGE_ROOT / logo.removeprefix("/img/")
            if org_path.exists():
                shutil.copyfile(org_path, target)
                return node_id, f"/img/robots/{target.name}", {
                    "source": logo,
                    "method": "builder-logo",
                }
    return node_id, None, {
        "source": urls[0] if urls else None,
        "method": None,
        "failure": "; ".join(errors[-5:]) or "no usable source image or builder logo",
    }


def run():
    rows = rows_by_kind()
    ids, _ = assign_node_ids(rows)
    IMAGE_ROOT.joinpath("orgs").mkdir(parents=True, exist_ok=True)
    IMAGE_ROOT.joinpath("robots").mkdir(parents=True, exist_ok=True)

    urls = read_json(DATA_DIR / "notion_urls.json")
    by_name, _ = url_indexes(urls)
    org_ids = {}
    for row in rows["ecosystem"]:
        org_ids[norm(canon(row["name"]))] = ids["ecosystem"][row["name"]]

    org_items = [(row, ids["ecosystem"][row["name"]]) for row in rows["ecosystem"]]
    with concurrent.futures.ThreadPoolExecutor(max_workers=THREADS) as pool:
        org_results = list(pool.map(fetch_org_image, org_items))
    org_images = {node_id: path for node_id, path, _ in org_results if path}

    robot_items = [(row, ids["robots"][row["name"]]) for row in rows["robots"]]
    with concurrent.futures.ThreadPoolExecutor(max_workers=THREADS) as pool:
        robot_results = list(pool.map(lambda item: fetch_robot_image(item, org_ids, org_images), robot_items))

    image_map = {}
    report = {}
    for result in org_results + robot_results:
        node_id, path, details = result
        if path:
            image_map[node_id] = path
        report[node_id] = details

    (DATA_DIR / "images.json").write_text(json.dumps(image_map, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (DATA_DIR / "images_report.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    org_count = sum(path is not None for _, path, _ in org_results)
    robot_count = sum(path is not None for _, path, _ in robot_results)
    print(
        f"organization images: {org_count}/{len(org_results)} "
        f"({org_count / len(org_results):.1%}); robot/model images: {robot_count}/{len(robot_results)} "
        f"({robot_count / len(robot_results):.1%})"
    )


if __name__ == "__main__":
    run()
