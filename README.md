# 42AI Robotics Lab — Research Maps (Claude Code project)

## Explore the maps in your browser

See [viz/README.md](viz/README.md) for the local Maps Visualizer guide. Quick start from the repository root (Python 3.10+ and Node 20+):

```bash
python -m pip install -r viz/requirements.txt
cd viz/web
npm install && npm run build
cd ../.. && python -m viz.server
```

Then open <http://127.0.0.1:8765>.

## Setup (once)
1. Install Claude Code: https://code.claude.com/docs/en/quickstart
2. Connect Notion:
   claude mcp add --transport http --scope user notion https://mcp.notion.com/mcp
   Then run `claude`, type `/mcp`, pick notion and log in with the account that owns
   the "Robotics Lab — Maps" page. Check with: claude mcp list
3. cd into this folder and run `claude`.

## Prompts to run, in order
1. Check:      "Read CLAUDE.md, then fetch the four Notion data sources and confirm the schema matches schemas/notion-schema.md."
2. Pilot:      "Run steps 1-3 of the pipeline only on entries marked pilot: true in branches.yaml. Then stop and summarize."
3. (Review output/ and reports/, adjust agents or schema if needed.)
4. Full run:   "Run steps 1-4 of the pipeline on all remaining entries, max 4 subagents in parallel. Stop at step 5."
5. Sync:       "I approve. Run step 6 with the notion-syncer."

## Running with Devin instead of Claude Code
See devin/: knowledge.md (add as a Devin Knowledge entry), playbooks/ (one Devin playbook each),
coordinator-prompt.md (prompts to paste into the coordinator session).
