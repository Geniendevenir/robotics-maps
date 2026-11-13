# Maps Visualizer backend

Build the canonical graph, geocodes, and image assets from the committed research and row data:

```bash
python viz/scripts/geocode.py
python viz/scripts/fetch_images.py
python viz/scripts/build_data.py
```

Install and run the local API, SSE, and MCP server:

```bash
python -m pip install -r viz/requirements.txt
python -m viz.server
```

The server listens on `127.0.0.1:8765`. It serves the built frontend from `viz/web/dist` when present. Groups are persisted in `viz/state/groups.json`.

## MCP clients

Claude Code can connect to the Streamable HTTP endpoint:

```bash
claude mcp add --transport http maps http://127.0.0.1:8765/mcp
```

For Claude Desktop, add a stdio server to its configuration:

```json
{
  "mcpServers": {
    "maps": {
      "command": "python",
      "args": ["-m", "viz.server.mcp_stdio"],
      "cwd": "/home/ubuntu/repos/robotics-maps"
    }
  }
}
```

In-app chat uses the Anthropic Messages API when `ANTHROPIC_API_KEY` is set, or the Claude Code CLI when `claude` is available on `PATH`. Set `VIZ_CHAT_MODEL` to choose the Anthropic model (defaults to `claude-sonnet-4-5`).

## Frontend

```bash
cd viz/web && npm install
npm run dev      # http://localhost:5173, proxies /api, /mcp and /img to :8765
npm run build    # writes viz/web/dist, then served by python -m viz.server at http://127.0.0.1:8765
```

Views: **Holygraph whiteboard** (projects, knowledge, robots/models, optional orgs; Branch = sector, Level = ring) and **World map** (455 organizations, clustered with logos; dashed border = approximate location). Click a node for its details panel; shift-drag to multi-select and group. The **Guide** tab is the chat; it can search, focus, filter, switch views and edit groups.
