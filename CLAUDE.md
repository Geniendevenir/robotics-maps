# 42AI Robotics Lab — Research Maps

## Context
42AI is École 42 Paris's AI association. We are launching a Robotics Lab: 15 students in 3 teams,
4-6 months, startup-style. Members are strong in software/AI, weak in mechanics and electronics.
Goals: reach startup-level robotics skills fast, ship impressive projects, and become known in the
French/European robotics ecosystem (events, hackathons, partners, sponsors, content).

Working hypothesis to test, not assume: our wedge is robot learning on low-cost hardware
(imitation learning, VLAs, sim-to-real, LeRobot/SO-101 stack).

This project fills four linked Notion databases with deep research. The final deliverable built
from them is a "Holygraph" (inspired by 42's Holygraph): projects as circles, Branch = sector,
Level = ring, Prerequisites = lines.

## Notion (access via the `notion` MCP server)
Hub page: 416f6c200e18816b9b46c28b8a56a030 ("Robotics Lab — Maps", private draft)

| Database | Data source ID (use for creating rows) |
|---|---|
| Knowledge Map | 3b023e17-b600-4f11-848a-11cdbcead7bc |
| Ecosystem Map | 66148973-c691-4717-8790-cfdf21e3a0dd |
| Robots & Models | e3aafb0d-9a5d-452b-92e8-54c18a45c1a7 |
| Projects (Holygraph) | 3eeadfc7-a1f7-44df-a0ed-601547ec217a |

Exact field names and allowed select options: see `schemas/notion-schema.md`. Before any sync,
fetch each data source live with the Notion MCP and trust Notion over that file if they differ.
The databases already contain pilot rows: never duplicate them, update them instead.

## Pipeline (always in this order)
1. Discovery: one `knowledge-researcher` subagent per knowledge branch and one
   `ecosystem-researcher` per ecosystem slice listed in `branches.yaml`. Run up to 4 in parallel.
   Each writes `output/<file>.json`.
2. Verification: one `verifier` subagent per output file -> `reports/verify_<file>.md` + cleaned JSON.
3. Coverage: one `coverage-critic` per output file -> `reports/gaps_<file>.md`.
   If a gaps report lists high-importance misses, re-run the researcher on those gaps only.
4. Holygraph: one `holygraph-architect` over ALL project candidates -> `output/projects.json`
   and `reports/holygraph.md`.
5. STOP. Summarize all reports for me and wait for my explicit approval.
6. Sync: `notion-syncer` pushes verified rows to Notion in this order:
   Ecosystem Map + Knowledge Map -> Robots & Models -> Projects (create all rows first,
   then set Prerequisites in a second pass).

## Research rules (apply to every subagent)
- Stay strictly inside the assigned branch or slice.
- Minimum 15 distinct sources per branch/slice; primary sources required (papers, official docs,
  company sites, funding announcements, conference programs, lab pages).
- Every row has at least one source URL that was actually opened.
- Write "unknown" rather than guess. Never invent organizations, papers, products or numbers.
- Saturation stop: keep searching until 3 consecutive queries return <10% new entries.
- Prefer 2024-2026 sources for anything about the current state. Today is late 2026.
- Hiring is out of scope: do not research jobs or hiring.
- Output JSON whose keys are exactly the Notion field names; relations are given as names
  (the syncer resolves them to page IDs).

## Conventions
- Writing for beginners: every explanation readable by a software student new to robotics.
- File names: snake_case slugs, e.g. `knowledge_robot_learning.json`, `ecosystem_paris_all.json`.
