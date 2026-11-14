# Maps Visualizer — data & API contract

Layout:
- `viz/scripts/build_data.py` — reads `output/*.json` + `viz/data/notion_urls.json` + `viz/data/geocache.json` + `viz/data/images.json`, writes `viz/data/graph.json`.
- `viz/scripts/geocode.py` — fills `viz/data/geocache.json` (place string -> {lat, lon}) via Nominatim, 1 req/s, cached.
- `viz/scripts/fetch_images.py` — downloads org logos + robot/model photos into `viz/web/public/img/{orgs,robots}/<slug>.webp` (max 256 px), writes `viz/data/images.json` (node id -> "/img/...").
- `viz/server/` — FastAPI app (`python -m viz.server`, port 8765): REST + SSE + MCP (`/mcp`, streamable HTTP) + chat. Also `python -m viz.server.mcp_stdio` for stdio MCP clients. Serves `viz/web/dist` at `/` when built.
- `viz/web/` — Vite + React + TypeScript frontend (dev on 5173, proxies `/api` and `/img` to 8765).
- `viz/state/groups.json` — persisted groups (gitignored).

## Node ids
`<prefix>:<slug>` with prefix `p` (project), `k` (knowledge node), `r` (robot/model), `o` (organization).
slug = lowercase, non-alphanumerics -> `-`, trimmed; on collision append `-2`, `-3`.
Names are deduplicated exactly like the Notion sync (same alias map / normalisation as `/home/ubuntu/sync/load.py` and `build_plan.py`), so there is one node per Notion row.

## graph.json
```json
{
  "generated_at": "ISO date",
  "nodes": [
    {
      "id": "p:pure-pursuit-in-nav2-simulation",
      "type": "project | knowledge | robot | org",
      "name": "Pure pursuit in Nav2 simulation",
      "branch": "Control",            // project Branch, knowledge Branch, null for robot/org
      "level": 1.67,                  // project: 0 for Onboarding else mean of 3 highest of Novelty/Autonomy/Hardware/Integration leading digits; knowledge: "Fundamental|Applied|Frontier"; else null
      "image": "/img/robots/so-101.webp",   // or null
      "notion_url": "https://app.notion.com/p/...", // or null
      "geo": {"lat": 48.85, "lon": 2.35, "place": "Paris", "approx": false},  // orgs only; approx=true when only Region was known (region centroid + small deterministic jitter)
      "fields": { /* every Notion scalar field of the row, exact Notion keys, relations removed */ }
    }
  ],
  "edges": [
    {"source": "p:a", "target": "p:b", "kind": "prerequisite"},       // a is prerequisite of b
    {"source": "p:x", "target": "k:y", "kind": "project-knowledge"},
    {"source": "p:x", "target": "r:y", "kind": "project-robot"},
    {"source": "p:x", "target": "o:y", "kind": "project-org"},
    {"source": "r:x", "target": "k:y", "kind": "robot-knowledge"},
    {"source": "r:x", "target": "o:y", "kind": "robot-builder"},
    {"source": "r:x", "target": "o:y", "kind": "robot-user"}
  ]
}
```
Include the 8 existing Notion-only Robot-learning knowledge nodes and Bleu_0.1 / Xiaomi-Robotics-0 / -1 (fields from `/home/ubuntu/sync/existing_rows_*.txt`).

## Group
```json
{"id": "g_ab12cd", "name": "SO-101 starter path", "description": "", "color": "#e4572e",
 "node_ids": ["p:...", "o:..."], "created_by": "user | agent", "created_at": "ISO", "updated_at": "ISO"}
```

## REST (all JSON)
- `GET  /api/data` -> graph.json
- `GET  /api/groups` -> `Group[]`
- `POST /api/groups` `{name, description?, color?, node_ids?, created_by?}` -> `Group`
- `PATCH /api/groups/{id}` `{name?, description?, color?}` -> `Group`
- `POST /api/groups/{id}/add` `{node_ids: []}` -> `Group`
- `POST /api/groups/{id}/remove` `{node_ids: []}` -> `Group`
- `DELETE /api/groups/{id}` -> `{ok: true}`
- `POST /api/ui` `UiCommand` -> `{ok: true}` (broadcast to all open browsers)
- `GET  /api/events` — SSE. Events: `event: groups` data `Group[]` (after any change); `event: ui` data `UiCommand`.
- `GET  /api/chat/status` -> `{"backend": "anthropic" | "claude-cli" | "none", "model": "..."}`
- `POST /api/chat` `{messages: [{role: "user"|"assistant", content: string}], context: {view: "graph"|"map", selected_node_id?: string, filters?: Filters, visible_node_ids_count?: number}}`
  -> `text/event-stream` of `data: {"type":"text","text":"..."}` | `{"type":"tool","name":"...","input":{...},"result_summary":"..."}` | `{"type":"error","message":"..."}` | `{"type":"done"}`.
  Tool calls run server-side with the same functions as MCP, so group/UI changes reach the browser through `/api/events`.

## UiCommand
```json
{"action": "focus", "node_id": "p:..."}                  // switch to the node's view, select it, open side panel, centre on it
{"action": "highlight", "node_ids": ["..."]}             // highlight these, dim others ([] clears)
{"action": "set_filters", "view": "graph"|"map", "filters": Filters}  // replaces filters for that view
{"action": "show_group", "group_id": "g_..."}           // filter the current view to that group's nodes
{"action": "switch_view", "view": "graph"|"map"}
```

## Filters
```json
{
  "search": "text",                 // substring on name + main text fields
  "types": ["project","knowledge","robot","org"],   // graph view only
  "branches": ["Control", ...],
  "level_min": 0, "level_max": 5,   // projects
  "project_kind": ["Onboarding","Project"],
  "knowledge_level": ["Fundamental","Applied","Frontier"],
  "robot_kind": ["Robot","AI model","Simulator/Tool"],
  "hardware_cost": ["€0 (sim only)", ...],
  "org_type": [...], "region": [...], "value_chain": [...], "sector": [...], "relationship": [...],
  "open_source": true | false | null,
  "group_id": "g_..." | null
}
```
Empty / missing key = no constraint.

## MCP / agent tools (identical for MCP and in-app chat)
- `overview()` — counts by type/branch/level, org counts by region/type, group list.
- `search_nodes(query?, type?, branch?, filters?, limit=20)` -> `[{id, type, name, branch, level, one_line}]`
- `get_node(id_or_name)` -> node + resolved neighbours `{prerequisites, unlocks, knowledge, robots, orgs, projects}` as `{id, name}`
- `get_neighbors(id, depth=1)`
- `list_groups()`, `create_group(name, description?, node_ids?, color?)`, `add_to_group(group_id, node_ids)`, `remove_from_group(group_id, node_ids)`, `rename_group(group_id, name?, description?)`, `delete_group(group_id)` — created_by = "agent"
- `focus_node(id)`, `highlight_nodes(ids)`, `set_filters(view, filters)`, `show_group(group_id)`, `switch_view(view)` -> broadcast UiCommand
Name lookups accept ids or case-/punctuation-insensitive names.
