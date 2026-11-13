import json
import time
from pathlib import Path
from urllib.parse import urlencode
from urllib.request import Request, urlopen

try:
    from .data_common import DATA_DIR, place_for_org, read_json, rows_by_kind
except ImportError:
    from data_common import DATA_DIR, place_for_org, read_json, rows_by_kind


USER_AGENT = "42ai-robotics-maps/0.1"
CENTROIDS = {
    "paris": (48.8566, 2.3522),
    "france": (46.2276, 2.2137),
    "europe": (50.8503, 4.3517),
    "united states": (39.8283, -98.5795),
    "us": (39.8283, -98.5795),
    "china": (35.8617, 104.1954),
    "japan": (36.2048, 138.2529),
    "south korea": (35.9078, 127.7669),
}


def approximate(place, region=None):
    for value in (region, place):
        if value:
            centroid = CENTROIDS.get(value.strip().lower())
            if centroid:
                return centroid
    return CENTROIDS["europe"]


def nominatim(place):
    query = urlencode({"q": place, "format": "jsonv2", "limit": 1})
    request = Request(
        f"https://nominatim.openstreetmap.org/search?{query}",
        headers={"User-Agent": USER_AGENT, "Accept": "application/json"},
    )
    with urlopen(request, timeout=20) as response:
        results = json.loads(response.read().decode("utf-8"))
    if not results:
        return None
    return {"lat": float(results[0]["lat"]), "lon": float(results[0]["lon"]), "approx": False}


def build_cache():
    rows = rows_by_kind()
    cache_path = DATA_DIR / "geocache.json"
    cache = read_json(cache_path)
    place_regions = {}
    for row in rows["ecosystem"]:
        fields = row.get("props", {})
        place = place_for_org(fields)
        place_regions.setdefault(place, str(fields.get("Region") or ""))
    places = set(place_regions)
    last_request = 0.0
    exact = 0
    approx = 0
    for place in sorted(places):
        existing = cache.get(place)
        if existing and "lat" in existing and "lon" in existing:
            if not existing.get("approx", False):
                exact += 1
            else:
                approx += 1
            continue
        is_region = place.strip().lower() in CENTROIDS
        coords = None
        if not is_region:
            delay = 1.0 - (time.monotonic() - last_request)
            if delay > 0:
                time.sleep(delay)
            last_request = time.monotonic()
            try:
                coords = nominatim(place)
            except Exception as error:
                print(f"geocode failed for {place!r}: {error}")
        if coords is None:
            lat, lon = approximate(place, place_regions.get(place))
            coords = {"lat": lat, "lon": lon, "approx": True}
            approx += 1
        else:
            exact += 1
        cache[place] = coords
        cache_path.write_text(json.dumps(cache, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return cache, exact, approx


def main():
    cache, exact, approx = build_cache()
    print(f"cached {len(cache)} places: {exact} exact, {approx} approximate")


if __name__ == "__main__":
    main()
