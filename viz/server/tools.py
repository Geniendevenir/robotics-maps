import json
from collections import Counter, defaultdict, deque
from pathlib import Path
from typing import Any

from viz.scripts.data_common import DATA_DIR, read_json
from viz.scripts.normalize import canon, norm


_groups = None
_ui_publisher = None
_groups_publisher = None
_graph_cache = None
_graph_mtime = None
MAIN_TEXT_FIELDS = (
    "What it is",
    "Description",
    "What they build",
    "Why it matters",
    "Key specs",
    "Deliverable",
    "Frontier state 2026",
)
SEARCH_TEXT_FIELDS = MAIN_TEXT_FIELDS + (
    "Prerequisites",
    "Key players",
    "Best resources",
    "Project ideas",
    "Sources",
    "Price / access",
    "Warm contact path",
)


def configure(group_store=None, ui_publisher=None, groups_publisher=None):
    global _groups, _ui_publisher, _groups_publisher
    if group_store is not None:
        _groups = group_store
    if ui_publisher is not None:
        _ui_publisher = ui_publisher
    if groups_publisher is not None:
        _groups_publisher = groups_publisher


def group_store():
    global _groups
    if _groups is None:
        from viz.server.groups import GroupStore
        _groups = GroupStore()
    return _groups


def _graph():
    global _graph_cache, _graph_mtime
    path = DATA_DIR / "graph.json"
    if not path.exists():
        return {"nodes": [], "edges": []}
    mtime = path.stat().st_mtime_ns
    if _graph_cache is None or mtime != _graph_mtime:
        _graph_cache = read_json(path)
        _graph_mtime = mtime
    return _graph_cache


def _as_values(value):
    if value is None:
        return []
    if isinstance(value, list):
        return value
    if isinstance(value, str) and value.startswith("["):
        try:
            decoded = json.loads(value)
            return decoded if isinstance(decoded, list) else [value]
        except json.JSONDecodeError:
            pass
    return [value]


def _text(value):
    if isinstance(value, list):
        return " ".join(str(item) for item in value)
    if value is None:
        return ""
    return str(value)


def _summary(node):
    fields = node.get("fields", {})
    one_line = next((_text(fields.get(key)) for key in MAIN_TEXT_FIELDS if fields.get(key)), "")
    return {
        "id": node["id"],
        "type": node["type"],
        "name": node["name"],
        "branch": node.get("branch"),
        "level": node.get("level"),
        "one_line": one_line[:280],
    }


def _matches_filter(node, filters):
    fields = node.get("fields", {})
    node_type = node.get("type")
    checks = (
        ("types", [node_type]),
        ("branches", [node.get("branch")]),
        ("project_kind", [fields.get("Kind")] if node_type == "project" else []),
        ("knowledge_level", [fields.get("Level")] if node_type == "knowledge" else []),
        ("robot_kind", [fields.get("Kind")] if node_type == "robot" else []),
        ("hardware_cost", [fields.get("Hardware cost"), fields.get("Starter hardware cost")]),
        ("org_type", [fields.get("Type")] if node_type == "org" else []),
        ("region", [fields.get("Region")] if node_type == "org" else []),
        ("value_chain", _as_values(fields.get("Value chain")) if node_type == "org" else []),
        ("sector", _as_values(fields.get("Sector")) if node_type == "org" else []),
        ("relationship", _as_values(fields.get("Relationship potential")) if node_type == "org" else []),
    )
    for filter_key, candidates in checks:
        wanted = filters.get(filter_key)
        if wanted:
            wanted_values = {str(value).casefold() for value in _as_values(wanted)}
            candidate_values = {str(value).casefold() for value in candidates if value is not None}
            if not (wanted_values & candidate_values):
                return False

    for key, compare in (("level_min", lambda a, b: a >= b), ("level_max", lambda a, b: a <= b)):
        constraint = filters.get(key)
        if constraint is not None:
            if node_type != "project" or node.get("level") is None or not compare(float(node["level"]), float(constraint)):
                return False

    if filters.get("open_source") is not None:
        value = fields.get("Open source")
        if isinstance(value, str):
            value = value.casefold() in ("true", "yes", "__yes__")
        if value is not filters["open_source"]:
            return False

    group_id = filters.get("group_id")
    if group_id:
        try:
            group = group_store().get(group_id)
        except KeyError:
            return False
        if node["id"] not in group["node_ids"]:
            return False
    return True


def _matches_query(node, query):
    if not query:
        return True
    fields = node.get("fields", {})
    searchable = " ".join(
        [node.get("name", "")] + [_text(fields.get(key)) for key in SEARCH_TEXT_FIELDS]
    )
    return query.casefold() in searchable.casefold()


def search_nodes(query=None, type=None, branch=None, filters=None, limit=20):
    """Search node names and descriptive fields, applying all supplied map filters."""
    filters = dict(filters or {})
    if type:
        filters["types"] = [type]
    if branch:
        filters["branches"] = [branch]
    query = (query or "").strip()
    filter_query = str(filters.pop("search", "") or "").strip()
    matches = [
        node for node in _graph().get("nodes", [])
        if _matches_query(node, query)
        and _matches_query(node, filter_query)
        and _matches_filter(node, filters)
    ]
    priority_query = query or filter_query
    matches.sort(key=lambda node: (0 if priority_query and priority_query.casefold() in node["name"].casefold() else 1, node["name"].casefold()))
    return [_summary(node) for node in matches[:max(0, min(int(limit), 100))]]


def _find_node(id_or_name):
    nodes = _graph().get("nodes", [])
    for node in nodes:
        if node["id"] == id_or_name:
            return node
    needle = norm(canon(id_or_name))
    for node in nodes:
        if norm(canon(node["name"])) == needle:
            return node
    raise ValueError(f"No map node named or identified by {id_or_name!r}")


def _node_lookup():
    return {node["id"]: node for node in _graph().get("nodes", [])}


def _neighbors(node):
    node_id = node["id"]
    edges = _graph().get("edges", [])
    lookup = _node_lookup()
    result = {key: {} for key in ("prerequisites", "unlocks", "knowledge", "robots", "orgs", "projects")}

    def add(category, target_id):
        target = lookup.get(target_id)
        if target:
            result[category][target_id] = {"id": target_id, "name": target["name"]}

    for edge in edges:
        source, target, kind = edge["source"], edge["target"], edge["kind"]
        if node["type"] == "project":
            if kind == "prerequisite":
                if target == node_id:
                    add("prerequisites", source)
                if source == node_id:
                    add("unlocks", target)
            elif source == node_id and kind == "project-knowledge":
                add("knowledge", target)
            elif source == node_id and kind == "project-robot":
                add("robots", target)
            elif source == node_id and kind == "project-org":
                add("orgs", target)
            elif kind.startswith("project-") and target == node_id and source != node_id:
                add("projects", source)
        elif node["type"] == "knowledge":
            if kind == "project-knowledge" and target == node_id:
                add("projects", source)
            elif kind == "robot-knowledge" and target == node_id:
                add("robots", source)
        elif node["type"] == "robot":
            if kind == "robot-knowledge" and source == node_id:
                add("knowledge", target)
            elif kind in ("robot-builder", "robot-user") and source == node_id:
                add("orgs", target)
            elif kind == "project-robot" and target == node_id:
                add("projects", source)
        elif node["type"] == "org":
            if kind.startswith("robot-") and target == node_id:
                add("robots", source)
            elif kind == "project-org" and target == node_id:
                add("projects", source)
    return {key: list(values.values()) for key, values in result.items()}


def get_node(id_or_name):
    node = _find_node(id_or_name)
    return {**node, "neighbors": _neighbors(node)}


def get_neighbors(id, depth=1):
    start = _find_node(id)
    lookup = _node_lookup()
    limit = max(1, min(int(depth), 5))
    seen = {start["id"]}
    pending = deque([(start["id"], 0)])
    results = []
    adjacency = defaultdict(set)
    for edge in _graph().get("edges", []):
        adjacency[edge["source"]].add(edge["target"])
        adjacency[edge["target"]].add(edge["source"])
    while pending:
        current, distance = pending.popleft()
        if distance >= limit:
            continue
        for neighbor_id in adjacency[current]:
            if neighbor_id in seen or neighbor_id not in lookup:
                continue
            seen.add(neighbor_id)
            next_distance = distance + 1
            results.append({**_summary(lookup[neighbor_id]), "distance": next_distance})
            pending.append((neighbor_id, next_distance))
    return results


def overview():
    nodes = _graph().get("nodes", [])
    counts_by_type = Counter(node.get("type") for node in nodes)
    counts_by_branch = Counter(node.get("branch") for node in nodes if node.get("branch"))
    counts_by_level = Counter(
        str(node.get("level")) for node in nodes if node.get("level") is not None
    )
    orgs = [node for node in nodes if node.get("type") == "org"]
    regions = Counter(str(node.get("fields", {}).get("Region", "unknown")) for node in orgs)
    org_types = Counter(str(node.get("fields", {}).get("Type", "unknown")) for node in orgs)
    return {
        "counts_by_type": dict(counts_by_type),
        "counts_by_branch": dict(counts_by_branch),
        "counts_by_level": dict(counts_by_level),
        "orgs_by_region": dict(regions),
        "orgs_by_type": dict(org_types),
        "groups": group_store().list(),
    }


def list_groups():
    return group_store().list()


def create_group(name, description="", node_ids=None, color="#e4572e"):
    group = group_store().create(name, description, color, node_ids, created_by="agent")
    _publish_groups()
    return group


def add_to_group(group_id, node_ids):
    group = group_store().add_nodes(group_id, node_ids)
    _publish_groups()
    return group


def remove_from_group(group_id, node_ids):
    group = group_store().remove_nodes(group_id, node_ids)
    _publish_groups()
    return group


def rename_group(group_id, name=None, description=None):
    group = group_store().update(group_id, name=name, description=description)
    _publish_groups()
    return group


def delete_group(group_id):
    group_store().delete(group_id)
    _publish_groups()
    return {"ok": True}


def _publish_groups():
    if _groups_publisher is not None:
        _groups_publisher(group_store().list())


def _send_ui(command):
    if _ui_publisher is None:
        return {"ok": True}
    _ui_publisher(command)
    return {"ok": True}


def focus_node(id):
    return _send_ui({"action": "focus", "node_id": _find_node(id)["id"]})


def highlight_nodes(ids):
    return _send_ui({"action": "highlight", "node_ids": [_find_node(value)["id"] for value in ids]})


def set_filters(view, filters):
    if view not in ("graph", "map") or not isinstance(filters, dict):
        raise ValueError("view must be graph or map and filters must be an object")
    return _send_ui({"action": "set_filters", "view": view, "filters": filters})


def show_group(group_id):
    group_store().get(group_id)
    return _send_ui({"action": "show_group", "group_id": group_id})


def switch_view(view):
    if view not in ("graph", "map"):
        raise ValueError("view must be graph or map")
    return _send_ui({"action": "switch_view", "view": view})
