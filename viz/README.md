# Maps Visualizer

A local web app to explore the maps: Holygraph whiteboard + world map + groups + Guide chat.

## Run it locally

Requires Python 3.10+ and Node 20+. Run these commands from the repository root:

```bash
python -m pip install -r viz/requirements.txt
cd viz/web && npm install && npm run build && cd ../..
python -m viz.server
```

Open <http://127.0.0.1:8765>. The graph data and images are committed, so a fresh clone does not need a data rebuild.

## Develop the frontend

Keep the server running, then start Vite from the repository root:

```bash
cd viz/web && npm run dev
```

Open <http://localhost:5173>. Vite proxies `/api`, `/mcp`, and `/img` to the server on port 8765.

## Using it

Views: **Holygraph whiteboard** (projects, knowledge, robots/models, optional orgs; Branch = sector, Level = ring) and **World map** (615 organizations, clustered with logos; dashed border = approximate location). Click a node for its details panel; shift-drag to multi-select and group. The **Guide** tab is the chat; it can search, focus, filter, switch views and edit groups.

## Groups

Groups are stored locally in `viz/state/groups.json`, which is git-ignored. On first run, groups start from the committed `viz/state/groups.seed.json`. To share an updated set of groups, copy your `groups.json` over the seed file and commit the seed.

```bash
cp viz/state/groups.json viz/state/groups.seed.json
```

## Guide chat (optional)

Chat works when `ANTHROPIC_API_KEY` is set (billed API usage) or when the `claude` CLI is on `PATH` and logged in. `VIZ_CHAT_MODEL` sets the Anthropic model; the default is `claude-sonnet-4-5`. Without either option, the maps and other features still work.

## Optional: control it from Claude (MCP)

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
      "cwd": "/path/to/robotics-maps"
    }
  }
}
```

The server must be running for browser-control tools to work.

## Rebuilding the data (only after changing research files)

Run from the repository root. Import each research file, then regenerate geocoding, images, and the graph:

```bash
python viz/scripts/import_research.py --country <Country> <file>
python viz/scripts/geocode.py
python viz/scripts/fetch_images.py
python viz/scripts/build_data.py
```

For the data format, REST endpoints, filters, and MCP contract, see [API.md](API.md).
