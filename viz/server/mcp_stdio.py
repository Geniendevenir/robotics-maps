from viz.server.mcp_app import mcp
from viz.server.groups import GroupStore
from viz.server import tools


tools.configure(GroupStore())
mcp.run(transport="stdio")
