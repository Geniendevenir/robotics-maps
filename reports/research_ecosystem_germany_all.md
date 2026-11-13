# Research report: ecosystem slice Germany / all / top 40

Output: `output/ecosystem_germany_all.json` — 40 organizations, 19 robots/models, 60 distinct sources.
All rows Region = "Europe" with the city in City; Status = "To verify".

## Method
- Discovery: Google News RSS queries (German robotics funding 2026, Berlin/Munich/Dresden/Hamburg startups, humanoid startups, robotics hackathons), known national structures (RIG, DLR, Fraunhofer, DFKI, Max Planck, clusters of excellence), RoboCup teams, maker/hacker spaces and investors.
- Every row's Sources were opened (curl, or Chrome CDP for bot-protected pages: is.mpg.de, ceti.one, htgf.de, tech.eu, aibusiness.com, therobotreport.com, hamburg-business.com, munich-startup.de).
- Duplicate check: names grepped against every `output/*.json` on main (organizations and robots_models) plus the coordinator's list; zero overlaps.
- Saturation: not formally reached (budget-limited "top 40" slice). The last three discovery queries (Hamburg/Dresden startups, hackathons, German Robotics Conference) returned mostly already-mapped orgs (NEURA, Agile Robots, RobCo, Sereact, Quantum Systems, microagi) or non-German ones.

## Coverage by hub
- Munich: TUM MIRMI, DLR RM (Oberpfaffenhofen), RIG, Roboy, TUM.ai, TUM.ai Makeathon, UnternehmerTUM MakerSpace, Magazino, FERNRIDE, ARX Robotics, Roboception, Sitegeist, Helsing, UVC Partners
- Berlin: TU Berlin RBO, c-base (hacker space), MotionLab.Berlin (makerspace)
- Stuttgart/Karlsruhe/Darmstadt: KIT H2T, MPI-IS, Cyber Valley, Bosch Center for AI, TU Darmstadt IAS
- Dresden: TU Dresden CeTI, CeTI Mobile Robotics Hackathon
- Hamburg/North: UHH TAMS, Hamburg Bit-Bots, Jungheinrich, goodBytz, Naiture, Chaos Communication Congress (40C3), DFKI RIC and B-Human (Bremen)
- Cologne/Aachen/Bonn: Uni Bonn AIS, Fab Lab Aachen, HTGF (Bonn)
- Other: Fraunhofer IML (Dortmund), UTN (Nuremberg), Unchained Robotics (Paderborn), Nature Robots (Osnabrück), SPRIND (Leipzig)

## Choices and caveats
- Type mapping: c-base, Fab Lab Aachen, Cyber Valley, Roboy, B-Human, Bit-Bots, TUM.ai = Association; MotionLab.Berlin = Startup (company) and UnternehmerTUM MakerSpace = Corporate (company), both described as "makerspace". UTN = School. Magazino = Corporate (Jungheinrich company).
- Sitegeist and Naiture: official website not confirmed (sitegeist.ai did not respond), so Website is left empty.
- Helsing and ARX Robotics are defence companies; included for completeness of the Munich autonomy scene with low relationship potential.
- Funding figures only where an opened page states them (FERNRIDE €75M total, Sitegeist €4M pre-seed, UVC €250M fund IV, HTGF up to €30M growth tickets). Nature Robots' €4M (2026) and goodBytz' KfW Award 2026 appear only in headlines whose pages blocked us, so they are not in the rows.
- Dropped candidates: German Robotics Conference (no reachable official page found), AILOS Robotics (Brussels, not German), Cherry Ventures (robotics portfolio not confirmed).

## Updates to existing rows
- "Gereon UGV" (robots_models in ecosystem_europe_investors_in_robotics.json): Built by can now link to the new org row "ARX Robotics" (Builder text currently holds it).
- "NAO" / "NAO6": Used by could add "B-Human" (RoboCup Humanoid / SPL team, 13 world titles).
- "Agile Robots": DLR spin-off per dlr.de Innovation & Transfer page; news (12 Nov 2026) reports a SoftBank-led $500M round at $8.5B valuation (Tech.eu/Forbes headlines, not opened).
- "RobCo": Oct 2026 news headlines report a $1B valuation and CEO relocation to the US (not opened).
- "NEURA Robotics": Aug 2026 headlines report acquisition of Bosch Rexroth's ACTIVE Shuttle and of Adlatus Robotics (not opened).
- "microagi": July 2026 headlines report a $55M seed round (largest German seed), led by redalpine (Osborne Clarke release headline, not opened).
- "Roboception" (new) is a DLR spin-off; "DLR David variable-stiffness joints" relates to the new robot row "neoDavid".

## 5-line summary
1. Leaders: Munich dominates (TUM MIRMI, DLR RM, RIG HQ, UnternehmerTUM, plus NEURA/Agile/Franka/RobCo already mapped); KIT, TU Darmstadt, Bonn, Bremen and Dresden are the other academic poles.
2. Money: big 2026 rounds went to scale-ups already in Notion; newly mapped startups are seed/Series A (Sitegeist, Nature Robots, Naiture, goodBytz, Unchained) or defence (ARX, Helsing), with HTGF, UVC and SPRIND as early capital.
3. Demand: logistics (Jungheinrich/Magazino, Fraunhofer IML, FERNRIDE), construction and agriculture are concrete buyers; defence autonomy grows but fits a student lab poorly.
4. Peers: TUM.ai, Roboy, B-Human and Hamburg Bit-Bots are the closest student counterparts to 42AI.
5. Entry point: joint robot-learning session with TUM.ai and TU Darmstadt IAS, then a team at the CeTI Mobile Robotics Hackathon or 40C3 for low-cost visibility.
