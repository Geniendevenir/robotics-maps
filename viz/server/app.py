import mimetypes
from contextlib import asynccontextmanager

from fastapi import FastAPI, HTTPException
from fastapi.responses import StreamingResponse
from fastapi.staticfiles import StaticFiles

from viz.scripts.data_common import DATA_DIR, VIZ_ROOT, read_json
from viz.server import chat, tools
from viz.server.events import EventBroker
from viz.server.groups import GroupStore
from viz.server.mcp_app import mcp, mcp_http_app


broker = EventBroker()
groups = GroupStore()
tools.configure(
    groups,
    lambda command: broker.publish("ui", command),
    lambda current: broker.publish("groups", current),
)


@asynccontextmanager
async def lifespan(_app):
    async with mcp.session_manager.run():
        yield


app = FastAPI(title="42AI Robotics Maps API", lifespan=lifespan)


class MCPRootPath:
    def __init__(self, application):
        self.application = application

    async def __call__(self, scope, receive, send):
        if scope["type"] == "http" and scope["path"] in ("", "/mcp"):
            scope = {
                **scope,
                "path": "/",
                "raw_path": b"/",
                "root_path": scope.get("root_path", "") + "/mcp",
            }
        await self.application(scope, receive, send)


def _changed_groups():
    broker.publish("groups", groups.list())


def _group_or_404(group_id):
    try:
        return groups.get(group_id)
    except KeyError as error:
        raise HTTPException(status_code=404, detail="Group not found") from error


def _node_ids():
    graph = read_json(DATA_DIR / "graph.json", {"nodes": []})
    return {node["id"] for node in graph.get("nodes", [])}


@app.get("/api/data")
def get_data():
    path = DATA_DIR / "graph.json"
    if not path.exists():
        raise HTTPException(status_code=503, detail="Build viz/data/graph.json first")
    return read_json(path)


@app.get("/api/groups")
def get_groups():
    return groups.list()


@app.post("/api/groups/refresh")
def refresh_groups():
    current = groups.list()
    broker.publish("groups", current)
    return current


@app.post("/api/groups")
def create_group(payload: dict):
    name = payload.get("name")
    if not isinstance(name, str) or not name.strip():
        raise HTTPException(status_code=422, detail="name is required")
    node_ids = payload.get("node_ids", [])
    if not isinstance(node_ids, list) or not all(isinstance(value, str) for value in node_ids):
        raise HTTPException(status_code=422, detail="node_ids must be a list of strings")
    try:
        group = groups.create(
            name,
            payload.get("description", ""),
            payload.get("color", "#e4572e"),
            node_ids,
            payload.get("created_by", "user"),
        )
    except ValueError as error:
        raise HTTPException(status_code=422, detail=str(error)) from error
    _changed_groups()
    return group


@app.patch("/api/groups/{group_id}")
def update_group(group_id: str, payload: dict):
    _group_or_404(group_id)
    if "name" in payload and (not isinstance(payload["name"], str) or not payload["name"].strip()):
        raise HTTPException(status_code=422, detail="name cannot be empty")
    try:
        group = groups.update(
            group_id,
            name=payload.get("name"),
            description=payload.get("description"),
            color=payload.get("color"),
        )
    except ValueError as error:
        raise HTTPException(status_code=422, detail=str(error)) from error
    _changed_groups()
    return group


@app.post("/api/groups/{group_id}/add")
def add_to_group(group_id: str, payload: dict):
    _group_or_404(group_id)
    node_ids = payload.get("node_ids", [])
    if not isinstance(node_ids, list) or not all(isinstance(value, str) for value in node_ids):
        raise HTTPException(status_code=422, detail="node_ids must be a list of strings")
    group = groups.add_nodes(group_id, node_ids)
    _changed_groups()
    return group


@app.post("/api/groups/{group_id}/remove")
def remove_from_group(group_id: str, payload: dict):
    _group_or_404(group_id)
    node_ids = payload.get("node_ids", [])
    if not isinstance(node_ids, list) or not all(isinstance(value, str) for value in node_ids):
        raise HTTPException(status_code=422, detail="node_ids must be a list of strings")
    group = groups.remove_nodes(group_id, node_ids)
    _changed_groups()
    return group


@app.delete("/api/groups/{group_id}")
def delete_group(group_id: str):
    _group_or_404(group_id)
    groups.delete(group_id)
    _changed_groups()
    return {"ok": True}


@app.post("/api/ui")
def send_ui_command(payload: dict):
    action = payload.get("action")
    if action not in {"focus", "highlight", "set_filters", "show_group", "switch_view"}:
        raise HTTPException(status_code=422, detail="Unknown UiCommand action")
    if action == "focus":
        if payload.get("node_id") not in _node_ids():
            raise HTTPException(status_code=404, detail="Node not found")
    elif action == "highlight":
        node_ids = payload.get("node_ids")
        if not isinstance(node_ids, list) or not all(isinstance(value, str) for value in node_ids):
            raise HTTPException(status_code=422, detail="node_ids must be a list of strings")
    elif action in ("set_filters", "switch_view"):
        if payload.get("view") not in ("graph", "map"):
            raise HTTPException(status_code=422, detail="view must be graph or map")
        if action == "set_filters" and not isinstance(payload.get("filters"), dict):
            raise HTTPException(status_code=422, detail="filters must be an object")
    elif action == "show_group":
        _group_or_404(payload.get("group_id", ""))
    broker.publish("ui", payload)
    return {"ok": True}


@app.get("/api/events")
def events():
    def stream():
        subscriber = broker.subscribe()
        try:
            yield ": connected\n\n"
            while True:
                try:
                    event, data = subscriber.get(timeout=15)
                except Exception:
                    yield ": keep-alive\n\n"
                    continue
                yield f"event: {event}\ndata: {data}\n\n"
        finally:
            broker.unsubscribe(subscriber)

    return StreamingResponse(
        stream(),
        media_type="text/event-stream",
        headers={"Cache-Control": "no-cache", "X-Accel-Buffering": "no"},
    )


@app.get("/api/chat/status")
def chat_status():
    backend, model = chat.backend_info()
    return {"backend": backend, "model": model}


@app.post("/api/chat")
def chat_completion(payload: dict):
    messages = payload.get("messages")
    context = payload.get("context", {})
    if not isinstance(messages, list) or not messages:
        raise HTTPException(status_code=422, detail="messages must be a non-empty array")
    if not isinstance(context, dict):
        raise HTTPException(status_code=422, detail="context must be an object")
    if any(
        not isinstance(message, dict)
        or message.get("role") not in ("user", "assistant")
        or not isinstance(message.get("content"), str)
        for message in messages
    ):
        raise HTTPException(status_code=422, detail="messages require user/assistant roles and string content")
    return StreamingResponse(
        chat.stream_chat(messages, context),
        media_type="text/event-stream",
        headers={"Cache-Control": "no-cache", "X-Accel-Buffering": "no"},
    )


mcp_root = MCPRootPath(mcp_http_app)
app.add_route("/mcp", mcp_root, methods=["GET", "POST", "DELETE"])
app.mount("/mcp", mcp_http_app)
mimetypes.add_type("image/webp", ".webp")
img_dir = VIZ_ROOT / "web" / "public" / "img"
if img_dir.exists():
    app.mount("/img", StaticFiles(directory=img_dir), name="img")
web_dist = VIZ_ROOT / "web" / "dist"
if web_dist.exists():
    app.mount("/", StaticFiles(directory=web_dist, html=True), name="web")
