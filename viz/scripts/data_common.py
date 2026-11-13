import json
from pathlib import Path

try:
    from .normalize import canon, norm, slugify
except ImportError:
    from normalize import canon, norm, slugify


VIZ_ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = VIZ_ROOT / "data"
ROW_KINDS = (
    ("projects", "p", "project", "Project"),
    ("knowledge", "k", "knowledge", "Node"),
    ("robots", "r", "robot", "Name"),
    ("ecosystem", "o", "org", "Organization"),
)


def read_json(path, default=None):
    path = Path(path)
    if not path.exists():
        return {} if default is None else default
    return json.loads(path.read_text(encoding="utf-8"))


def parse_value(value):
    if value == "__YES__":
        return True
    if value == "__NO__":
        return False
    if isinstance(value, str) and value[:1] in ("[", "{"):
        try:
            return json.loads(value)
        except json.JSONDecodeError:
            pass
    return value


def rows_by_kind(rows_path=None):
    rows = read_json(rows_path or DATA_DIR / "rows.json")
    result = {}
    for key, _, _, _ in ROW_KINDS:
        result[key] = rows.get(key, [])
    return result


def assign_node_ids(rows):
    ids = {}
    names = {}
    for kind, prefix, _, _ in ROW_KINDS:
        used = set()
        ids[kind] = {}
        names[kind] = {}
        for row in rows.get(kind, []):
            name = row["name"]
            base = slugify(name)
            slug = base
            suffix = 2
            while slug in used:
                slug = f"{base}-{suffix}"
                suffix += 1
            used.add(slug)
            node_id = f"{prefix}:{slug}"
            ids[kind][name] = node_id
            names[kind][norm(canon(name))] = name
    return ids, names


def url_indexes(urls):
    by_name = {}
    by_url = {}
    for kind, values in urls.items():
        by_name[kind] = {norm(canon(name)): url for name, url in values.items()}
        for name, url in values.items():
            by_url[normalize_url(url)] = name
    return by_name, by_url


def normalize_url(url):
    return (url or "").rstrip("/").replace("/p/", "/").lower()


def place_for_org(fields, country=None):
    city = fields.get("City")
    region = fields.get("Region")
    if isinstance(city, list):
        city = ", ".join(str(part) for part in city)
    city = str(city or "").strip()
    region = str(region or "").strip()
    country = str(country or "").strip()
    if city.lower() in ("", "unknown", "n/a", "none"):
        if country:
            return country
        return region or "Europe"
    city = city.split("(", 1)[0].split("+", 1)[0].split("/", 1)[0].split(";", 1)[0].strip(" ,")
    if country:
        if norm(country) not in norm(city):
            return f"{city}, {country}"
        return city
    region_country = {
        "Paris": "France",
        "France": "France",
        "Europe": "",
        "US": "United States",
        "China": "China",
        "Japan": "Japan",
        "South Korea": "South Korea",
    }
    country = region_country.get(region, "")
    if country and norm(country) not in norm(city):
        return f"{city}, {country}"
    return city
