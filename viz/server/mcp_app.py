from typing import Any

from mcp.server.fastmcp import FastMCP

from viz.server import tools


mcp = FastMCP(
    "maps",
    instructions="Explore the 42AI Robotics Lab research maps.",
    streamable_http_path="/",
)


@mcp.tool()
def overview() -> dict[str, Any]:
    return tools.overview()


@mcp.tool()
def search_nodes(
    query: str = "",
    type: str | None = None,
    branch: str | None = None,
    filters: dict[str, Any] | None = None,
    limit: int = 20,
) -> list[dict[str, Any]]:
    return tools.search_nodes(query, type, branch, filters, limit)


@mcp.tool()
def get_node(id_or_name: str) -> dict[str, Any]:
    return tools.get_node(id_or_name)


@mcp.tool()
def get_neighbors(id: str, depth: int = 1) -> list[dict[str, Any]]:
    return tools.get_neighbors(id, depth)


@mcp.tool()
def list_groups() -> list[dict[str, Any]]:
    return tools.list_groups()


@mcp.tool()
def create_group(
    name: str,
    description: str = "",
    node_ids: list[str] | None = None,
    color: str = "#e4572e",
) -> dict[str, Any]:
    return tools.create_group(name, description, node_ids, color)


@mcp.tool()
def add_to_group(group_id: str, node_ids: list[str]) -> dict[str, Any]:
    return tools.add_to_group(group_id, node_ids)


@mcp.tool()
def remove_from_group(group_id: str, node_ids: list[str]) -> dict[str, Any]:
    return tools.remove_from_group(group_id, node_ids)


@mcp.tool()
def rename_group(
    group_id: str,
    name: str | None = None,
    description: str | None = None,
) -> dict[str, Any]:
    return tools.rename_group(group_id, name, description)


@mcp.tool()
def delete_group(group_id: str) -> dict[str, Any]:
    return tools.delete_group(group_id)


@mcp.tool()
def focus_node(id: str) -> dict[str, Any]:
    return tools.focus_node(id)


@mcp.tool()
def highlight_nodes(ids: list[str]) -> dict[str, Any]:
    return tools.highlight_nodes(ids)


@mcp.tool()
def set_filters(view: str, filters: dict[str, Any]) -> dict[str, Any]:
    return tools.set_filters(view, filters)


@mcp.tool()
def show_group(group_id: str) -> dict[str, Any]:
    return tools.show_group(group_id)


@mcp.tool()
def switch_view(view: str) -> dict[str, Any]:
    return tools.switch_view(view)


mcp_http_app = mcp.streamable_http_app()
