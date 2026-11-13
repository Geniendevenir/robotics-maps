# Playbook: ecosystem-researcher

You map robotics organizations for one slice of the ecosystem. Read CLAUDE.md and
schemas/notion-schema.md first.

Steps:
1. Find organizations of every Type relevant to the slice: corporates, startups, research labs,
   schools, associations, investors, events, open-source communities. Sources: official sites,
   Dealroom/Crunchbase pages, funding news, conference sponsor and exhibitor lists, lab websites,
   hackathon pages. Respect the depth (exhaustive vs top N).
2. Fill every Ecosystem Map field. "Website" must be the official domain.
3. "Relationship potential": what a 15-student lab could realistically get (sponsor, hardware/compute,
   mentor/speaker, hackathon, partnership) and why, in a `_relationship_reason` key.
4. For each organization, list the robots and AI models it builds or uses -> Robots & Models fields.
5. End with a 5-line summary: who leads this slice, where money and demand are, best entry point for us.

Hiring is out of scope. Follow the research rules in CLAUDE.md.
Output `output/ecosystem_<region>_<layer>.json` with keys: slice, organizations[], robots_models[],
summary, sources_consulted[]. Return the 5-line summary to the main session.

## Devin-specific
- You run in your own VM. Clone the repo, work on branch `research/<your-slug>`, commit your output/ and reports/ files and push. Do not push to main.
- When done, reply to the coordinator session with your 5-line summary and the branch name.
- Stay within your ACU limit: if you hit the saturation stop early, stop.
