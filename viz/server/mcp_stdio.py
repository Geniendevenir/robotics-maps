from viz.server.mcp_app import mcp
from viz.server.groups import GroupStore
from viz.server import tools
from viz.server.stdio_publishers import make_publishers


ui_publisher, groups_publisher = make_publishers()
tools.configure(
    GroupStore(),
    ui_publisher=ui_publisher,
    groups_publisher=groups_publisher,
)
mcp.run(transport="stdio")
