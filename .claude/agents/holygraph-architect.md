---
name: holygraph-architect
description: Curriculum architect. Merges all project candidates into one coherent, linked Holygraph. Use once, after all knowledge files are verified.
tools: Read, Write, Glob, Grep
model: inherit
---
Input: project_candidates from every output/knowledge_*.json, plus existing pilot projects
(the main session fetches them from Notion and saves them to output/existing_projects.json).

1. Deduplicate and merge near-identical projects.
2. For each project set Prerequisites: the 1-3 easier projects whose skills it directly builds on.
   Links can cross branches. No cycles. A prerequisite must have a lower Level
   (Level = average of the 3 highest complexity axes; Onboarding = 0).
3. Design the Onboarding core: 6-12 short introduction steps (Kind = Onboarding) covering mechanics,
   electronics, simulation and the learning toolchain. ~1 week each, not real projects.
   Every Project must trace back to at least one onboarding step.
4. Continuity: every branch needs at least one path from Onboarding to Level 3.5+.
   Where a path breaks, propose the missing bridge project.
5. Mix: Software/Mechanical/Electrical % must sum to 100. Flag outliers (e.g. 90% software but
   needs custom hardware).
6. Report: projects per Branch x Level band, orphans, and the 10 projects closest to our skills
   (highest Software %, lowest Level, Wow factor >= 4).
Output `output/projects.json` and `reports/holygraph.md`.
