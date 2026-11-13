import json
from collections import Counter

import pytest
from fastapi.testclient import TestClient

from viz.server import app as server_app
from viz.server.groups import GroupStore
from viz.server import tools
from viz.server.mcp_app import mcp


@pytest.fixture
def client(tmp_path, monkeypatch):
    store = GroupStore(tmp_path / "groups.json")
    monkeypatch.setattr(server_app, "groups", store)
    tools.configure(store, lambda command: server_app.broker.publish("ui", command))
    test_client = TestClient(server_app.app)
    yield test_client
    test_client.close()


def test_api_data_counts(client):
    response = client.get("/api/data")
    assert response.status_code == 200
    graph = response.json()
    assert set(graph) == {"generated_at", "nodes", "edges"}
    counts = Counter(node["type"] for node in graph["nodes"])
    expected = {"project": 624, "knowledge": 231, "robot": 474, "org": 455}
    assert counts == expected, (
        f"Research dataset count mismatch: expected {expected}, got {dict(counts)}"
    )


def test_group_store_instances_reload_before_mutations(tmp_path):
    path = tmp_path / "groups.json"
    first = GroupStore(path)
    second = GroupStore(path)

    group_one = first.create("Group one")
    group_two = second.create("Group two")
    first.add_nodes(group_one["id"], ["p:one"])

    for store in (first, second):
        groups = {group["id"]: group for group in store.list()}
        assert groups[group_one["id"]]["node_ids"] == ["p:one"]
        assert groups[group_two["id"]]["name"] == "Group two"


def test_group_crud_and_persistence(client, tmp_path):
    created = client.post(
        "/api/groups",
        json={"name": "SO-101 starter path", "node_ids": ["p:first"], "created_by": "user"},
    )
    assert created.status_code == 200
    group = created.json()
    assert group["id"].startswith("g_")
    assert group["node_ids"] == ["p:first"]
    persisted = GroupStore(tmp_path / "groups.json").get(group["id"])
    assert persisted["name"] == group["name"]

    added = client.post(f"/api/groups/{group['id']}/add", json={"node_ids": ["r:so-101", "p:first"]})
    assert added.json()["node_ids"] == ["p:first", "r:so-101"]
    removed = client.post(f"/api/groups/{group['id']}/remove", json={"node_ids": ["p:first"]})
    assert removed.json()["node_ids"] == ["r:so-101"]
    updated = client.patch(f"/api/groups/{group['id']}", json={"name": "Starter"})
    assert updated.json()["name"] == "Starter"
    assert client.get("/api/groups").json() == [updated.json()]
    assert client.delete(f"/api/groups/{group['id']}").json() == {"ok": True}
    assert client.get("/api/groups").json() == []


def test_invalid_group_color_rejected_by_store_and_api(client):
    invalid = 'red;" onmouseover="x'
    with pytest.raises(ValueError, match="3- or 6-digit hex"):
        server_app.groups.create("Invalid", color=invalid)
    response = client.post("/api/groups", json={"name": "Invalid", "color": invalid})
    assert response.status_code == 422

    group = client.post("/api/groups", json={"name": "Valid"}).json()
    with pytest.raises(ValueError, match="3- or 6-digit hex"):
        server_app.groups.update(group["id"], color=invalid)
    response = client.patch(f"/api/groups/{group['id']}", json={"color": invalid})
    assert response.status_code == 422


def test_ui_broadcast_reaches_sse_subscriber(client):
    node_id = client.get("/api/data").json()["nodes"][0]["id"]
    subscriber = server_app.broker.subscribe()
    try:
        response = client.post("/api/ui", json={"action": "focus", "node_id": node_id})
        assert response.json() == {"ok": True}
        event, data = subscriber.get(timeout=1)
        assert event == "ui"
        assert json.loads(data) == {"action": "focus", "node_id": node_id}
    finally:
        server_app.broker.unsubscribe(subscriber)


def test_search_nodes_and_get_node():
    graph = json.loads((server_app.DATA_DIR / "graph.json").read_text(encoding="utf-8"))
    sample = graph["nodes"][0]
    matches = tools.search_nodes(query=sample["name"], limit=5)
    assert matches
    assert matches[0]["id"] == sample["id"]
    filtered = tools.search_nodes(filters={"search": sample["name"], "types": [sample["type"]]})
    assert any(node["id"] == sample["id"] for node in filtered)
    result = tools.get_node(sample["id"])
    assert result["id"] == sample["id"]
    assert set(result["neighbors"]) == {
        "prerequisites",
        "unlocks",
        "knowledge",
        "robots",
        "orgs",
        "projects",
    }


def test_fastmcp_instance_lists_contract_tools():
    registered = mcp._tool_manager.list_tools()
    names = {tool.name for tool in registered}
    assert {
        "overview",
        "search_nodes",
        "get_node",
        "get_neighbors",
        "list_groups",
        "create_group",
        "add_to_group",
        "remove_from_group",
        "rename_group",
        "delete_group",
        "focus_node",
        "highlight_nodes",
        "set_filters",
        "show_group",
        "switch_view",
    } <= names


def test_mcp_http_accepts_canonical_path():
    with TestClient(server_app.app, base_url="http://127.0.0.1:8765") as mcp_client:
        response = mcp_client.post(
            "/mcp",
            headers={"Accept": "application/json, text/event-stream"},
            json={
                "jsonrpc": "2.0",
                "id": 1,
                "method": "initialize",
                "params": {
                    "protocolVersion": "2025-06-18",
                    "capabilities": {},
                    "clientInfo": {"name": "test-client", "version": "1.0"},
                },
            },
        )
    assert response.status_code == 200
    assert "event: message" in response.text
