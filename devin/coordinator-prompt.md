# Coordinator prompts (paste into a new Devin session on this repo)

## 1. Check
Read devin/knowledge.md and schemas/notion-schema.md. Using the Notion MCP, fetch the four data
sources listed there and confirm the schema matches. Report differences. Do nothing else.

## 2. Pilot
For each entry marked `pilot: true` in branches.yaml, start a managed Devin with the matching
playbook (knowledge-researcher or ecosystem-researcher), max 15 ACUs each. When all finish, start a
managed Devin with the verifier playbook on each branch, then the coverage-critic. Merge the
research branches into main, then summarize all reports and the ACU used per child. Stop.

## 3. Full run
Same as pilot for every remaining entry in branches.yaml, max 4 managed Devins at a time, ACU limit
per child = (pilot average x 1.5). Then fetch existing projects from Notion into
output/existing_projects.json and run the holygraph-architect playbook. Merge everything and stop
with a summary. Do not touch Notion.

## 4. Sync (only after I approve)
Run the notion-syncer playbook on main.
