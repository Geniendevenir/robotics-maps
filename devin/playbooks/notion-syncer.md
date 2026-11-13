# Playbook: notion-syncer

Read CLAUDE.md and schemas/notion-schema.md. Fetch each data source live first and use its exact
field names and options.

Order:
1. Ecosystem Map and Knowledge Map rows.
2. Robots & Models rows, resolving Built by / Used by / Knowledge nodes from names to page IDs.
   If a builder isn't in the Ecosystem Map, use "Builder (if not in map)".
3. Projects: create every row first, then a second pass to set Prerequisites, Knowledge nodes,
   Robots & models and Relevant orgs.

Rules:
- Query existing rows first and deduplicate by name (case-insensitive, ignore punctuation).
  Existing pilot rows get updated, never duplicated.
- Never write read-only fields (Level, Mix check, reverse relations like Unlocks/Builds).
- Batch page creation (many pages per call). Keep a log in `reports/sync_log.md`:
  created / updated / skipped with reasons.

## Devin-specific
- You run in your own VM. Work on main after the coordinator has merged all research branches.
- When done, reply to the coordinator session with your 5-line summary and the branch name.
- Stay within your ACU limit: if you hit the saturation stop early, stop.
