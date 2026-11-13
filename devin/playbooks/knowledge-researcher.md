# Playbook: knowledge-researcher

You map one robotics branch for the 42AI Robotics Lab. Read CLAUDE.md and schemas/notion-schema.md
first. Reader: a software/AI student with no mechanics or electronics background.

Steps:
1. Build the sub-taxonomy of the branch: 8-20 nodes tagged Fundamental, Applied or Frontier.
   Ground it in the Springer Handbook of Robotics, Modern Robotics (Lynch & Park), ICRA/RSS/CoRL
   session tracks and top university course syllabi.
2. Fill every Knowledge Map field for each node. "Accessibility for us" gets a one-line justification
   in the JSON (key `_accessibility_reason`, not synced).
3. For each node, list reference robots, AI models and simulators -> Robots & Models fields.
4. For each node, propose 3-6 candidates for Projects (Holygraph): Kind, Branch, the four complexity
   axes per the rubric, Deliverable, Duration, Hardware cost, Wow factor, Software/Mechanical/
   Electrical % (share of work hours, sum = 100), Knowledge nodes, Robots & models, References.
   Spread complexity widely so projects can chain from onboarding to frontier.
5. End with the 3 nodes with the best ratio (accessibility x visual impact x ecosystem relevance) / cost.

Follow the research rules in CLAUDE.md (15+ sources, saturation stop, "unknown" over guessing).
Output `output/knowledge_<branch_slug>.json` with keys: branch, nodes[], robots_models[],
project_candidates[], top3[], sources_consulted[]. Return a 5-line summary to the main session.

## Devin-specific
- You run in your own VM. Clone the repo, work on branch `research/<your-slug>`, commit your output/ and reports/ files and push. Do not push to main.
- When done, reply to the coordinator session with your 5-line summary and the branch name.
- Stay within your ACU limit: if you hit the saturation stop early, stop.
