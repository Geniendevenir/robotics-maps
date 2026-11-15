import json
import re
import statistics
from datetime import datetime, timezone

try:
    from .data_common import DATA_DIR, ROW_KINDS, assign_node_ids, parse_value, place_for_org, read_json, rows_by_kind, url_indexes
    from .normalize import canon, norm, resolve_name
except ImportError:
    from data_common import DATA_DIR, ROW_KINDS, assign_node_ids, parse_value, place_for_org, read_json, rows_by_kind, url_indexes
    from normalize import canon, norm, resolve_name


RELATION_FIELDS = {
    "projects": {"Prerequisites", "Knowledge nodes", "Robots & models", "Relevant orgs"},
    "robots": {"Built by", "Used by", "Knowledge nodes"},
    "knowledge": {"Projects", "Robots & models"},
    "ecosystem": {"Builds", "Uses", "Related projects"},
}


def project_level(fields):
    if fields.get("Kind") == "Onboarding":
        return 0
    scores = []
    for key in ("Novelty", "Autonomy", "Hardware", "Integration"):
        match = re.match(r"\s*(\d+)", str(fields.get(key, "")))
        if match:
            scores.append(int(match.group(1)))
    if not scores:
        return None
    return round(statistics.mean(sorted(scores, reverse=True)[:3]), 2)


def relation_targets(row, field):
    rels = row.get("rels", {})
    value = rels.get(field, [])
    return value if isinstance(value, list) else [value]


def jitter(node_id):
    import hashlib
    import math

    digest = hashlib.sha256(node_id.encode("utf-8")).digest()
    angle = int.from_bytes(digest[:4], "big") / 2**32 * math.tau
    radius = 0.01 + int.from_bytes(digest[4:8], "big") / 2**32 * 0.02
    return math.cos(angle) * radius, math.sin(angle) * radius


LESSONS_DIR = DATA_DIR.parents[1] / "output" / "lessons"


def load_learning(lessons_dir=LESSONS_DIR):
    lessons = {}
    guide = None
    for path in sorted(lessons_dir.glob("*.json")) if lessons_dir.exists() else []:
        payload = json.loads(path.read_text(encoding="utf-8"))
        if path.name == "guide.json":
            guide = payload
            continue
        for lesson in payload.get("lessons", []):
            lessons[lesson["node_id"]] = {
                "summary": lesson.get("summary", ""),
                "lesson_md": lesson.get("lesson_md", ""),
                "resources": lesson.get("resources", []),
            }
    return lessons, guide


def build_graph():
    rows = rows_by_kind()
    lessons, guide = load_learning()
    ids, _ = assign_node_ids(rows)
    notion_urls = read_json(DATA_DIR / "notion_urls.json")
    url_names, _ = url_indexes(notion_urls)
    geocache = read_json(DATA_DIR / "geocache.json")
    images = read_json(DATA_DIR / "images.json")

    canonical_names = {
        kind: [row["name"] for row in rows[kind]]
        for kind, _, _, _ in ROW_KINDS
    }

    nodes = []
    node_ids = {}
    for kind, prefix, node_type, _ in ROW_KINDS:
        for row in rows[kind]:
            name = row["name"]
            node_id = ids[kind][name]
            node_ids[(kind, norm(canon(name)))] = node_id
            fields = {
                field: parse_value(value)
                for field, value in row.get("props", {}).items()
                if field not in RELATION_FIELDS[kind]
            }
            if kind == "projects":
                level = project_level(fields)
            elif kind == "knowledge":
                level = fields.get("Level")
            else:
                level = None
            notion_url = row.get("existing_url") or url_names.get(kind, {}).get(norm(canon(name)))
            node = {
                "id": node_id,
                "type": node_type,
                "name": name,
                "branch": fields.get("Branch") if kind in ("projects", "knowledge") else None,
                "level": level,
                "image": images.get(node_id),
                "notion_url": notion_url,
                "fields": fields,
            }
            if node_id in lessons:
                node["lesson"] = lessons[node_id]
            if kind == "ecosystem":
                place = place_for_org(fields, row.get("country"))
                coords = geocache.get(place)
                if coords and "lat" in coords and "lon" in coords:
                    dlat, dlon = jitter(node_id)
                    node["geo"] = {
                        "lat": float(coords["lat"]) + dlat,
                        "lon": float(coords["lon"]) + dlon,
                        "place": place,
                        "approx": bool(coords.get("approx", False)),
                    }
                else:
                    node["geo"] = None
            nodes.append(node)

    edges = []
    dropped = 0

    def add_edge(source, target_kind, target_name, edge_kind):
        nonlocal dropped
        resolved = resolve_name(target_name, canonical_names[target_kind])
        target = node_ids.get((target_kind, norm(canon(resolved)))) if resolved else None
        if target is None:
            dropped += 1
            return
        edges.append({"source": source, "target": target, "kind": edge_kind})

    project_fields = (
        ("Prerequisites", "projects", "prerequisite", True),
        ("Knowledge nodes", "knowledge", "project-knowledge", False),
        ("Robots & models", "robots", "project-robot", False),
        ("Relevant orgs", "ecosystem", "project-org", False),
    )
    for row in rows["projects"]:
        project_id = ids["projects"][row["name"]]
        for field, target_kind, edge_kind, reverse in project_fields:
            for name in relation_targets(row, field):
                if reverse:
                    resolved = resolve_name(name, canonical_names[target_kind])
                    target_id = node_ids.get((target_kind, norm(canon(resolved)))) if resolved else None
                    if target_id:
                        edges.append({"source": target_id, "target": project_id, "kind": edge_kind})
                    else:
                        dropped += 1
                else:
                    add_edge(project_id, target_kind, name, edge_kind)

    robot_fields = (
        ("Built by", "ecosystem", "robot-builder"),
        ("Used by", "ecosystem", "robot-user"),
        ("Knowledge nodes", "knowledge", "robot-knowledge"),
    )
    for row in rows["robots"]:
        robot_id = ids["robots"][row["name"]]
        for field, target_kind, edge_kind in robot_fields:
            for name in relation_targets(row, field):
                add_edge(robot_id, target_kind, name, edge_kind)

    graph = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "nodes": nodes,
        "edges": edges,
    }
    if guide:
        graph["guide"] = guide
    return graph, dropped


def main():
    graph, dropped = build_graph()
    output = DATA_DIR / "graph.json"
    output.write_text(json.dumps(graph, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    counts = {}
    for node in graph["nodes"]:
        counts[node["type"]] = counts.get(node["type"], 0) + 1
    print(f"wrote {output}: {counts}; dropped edges: {dropped}")


if __name__ == "__main__":
    main()
