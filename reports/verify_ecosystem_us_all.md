# Verification report: output/ecosystem_us_all.json

Verifier run on branch `research/ecosystem-us-all` (input commit d14f526). No Notion read/write.

## Summary
- Rows in: 25 organizations + 21 robots/models = 46
- Verified: 40 · Corrected: 6 · Rejected: 0
- Rows out: 46, all Status = "To verify"
- URLs checked: 78 unique. All return 200 via curl except tesla.com, axios.com, automateshow.com, osralliance.org (403), physicalintelligence.company (429) and intuitive.com (empty JS shell); I opened those in Chrome (CDP) and checked the claims there. No 404s.

## Global corrections
- Removed non-Notion key `_relationship_reason` from all 25 organizations.
- No `Used in projects` key present (auto reverse relation).
- Checked every select and multi-select value against schemas/notion-schema.md: all valid. Every `Built by` / `Used by` name resolves to an organization in this file. Events keep `Size / stage` = null (no fitting option).

## Open issues
- 1X Technologies: latest labeled round found is the Jan 2024 $100M Series B; there may be newer rounds.
- Physical Intelligence stage 'Series A-B' rests on a secondary tracker (mekawire). Axios does not name the series.
- Lux Capital / DCVC 'Public/Large' approximates 'established firm'.
- Release year still null for several rows (Isaac Sim/Lab, Optimus, Boston Dynamics robots, Figure 03, Drake, Gazebo): not established from the opened sources.

## Row-by-row
| Kind | Row | Result | Reason |
|---|---|---|---|
| Org | NVIDIA | verified | nvidia.com/robotics lists Isaac Sim, Isaac Lab (robot learning on Isaac Sim), Jetson. |
| Org | Tesla | verified | tesla.com/AI (Chrome; redirects to /SI) describes the Tesla Optimus bipedal program. |
| Org | Amazon Robotics | verified | aboutamazon page describes Proteus, Vulcan (touch sensing), Sparrow. |
| Org | Boston Dynamics | verified | Homepage lists Spot (inspection), Stretch, Atlas. |
| Org | Intuitive | corrected | Source /about-us/company renders empty (curl and Chrome); replaced with intuitive.com/en-us homepage, which confirms da Vinci 5 and Ion robotic bronchoscopy. |
| Org | Figure | verified | Series C page: >$1B committed at $39B post-money, Sep 16, 2025; homepage presents Figure 03 for the home + Helix. |
| Org | Physical Intelligence | corrected | Website/Sources: physicalintelligence.company now redirects to pi.website (updated). Axios $600M round (CapitalG, $5.6B valuation) and pi0 (Oct 31, 2024) confirmed via Chrome. |
| Org | Skild AI | verified | Series C blog (Jan 14, 2026): $1.4B raised, valuation >$14B. |
| Org | Agility Robotics | verified | Homepage: Digit assembled in Salem, OR, plus Arc; NVIDIA page (Sep 10, 2025): NVentures Series C investment, Isaac Lab. |
| Org | Apptronik | verified | Release (Feb 11, 2026): over $935M Series A incl. $520M extension; Mercedes-Benz, GXO, Jabil, Google DeepMind. |
| Org | 1X Technologies | verified | About page: San Carlos, CA; Palo Alto HQ post Jul 11, 2025; $100M Series B page opens. |
| Org | FieldAI | verified | Release (Aug 20, 2025, Irvine CA): $405M in two rounds; stockanalysis labels the latest round Series B. |
| Org | Stanford Robotics Center | verified | src.stanford.edu: domestic/medical/field areas, OpenSAI. |
| Org | Berkeley Artificial Intelligence Research (BAIR) | verified | HIL-SERL page confirms reward classifier, demos, human interventions; SERL repo marked deprecated. |
| Org | Carnegie Mellon University Robotics Institute | verified | ri.cmu.edu: Robotics Innovation Center in Pittsburgh, education + research. |
| Org | Toyota Research Institute (TRI) | corrected | City 'unknown' -> 'Los Altos, California (HQ); Cambridge, Massachusetts' (tri.global footer). Drake core development by TRI confirmed on drake.mit.edu. |
| Org | Massachusetts Institute of Technology (MIT) | verified | drake.mit.edu: started by MIT CSAIL Robot Locomotion Group. |
| Org | MassRobotics | verified | Homepage: 'world's largest independent robotics hub'. |
| Org | Silicon Valley Robotics | verified | 2026 prospectus PDF: 501(c)(6) association; LeRobot Global Hackathon 2025. |
| Org | Open Source Robotics Foundation (Open Robotics) | verified | OSRF is a California nonprofit (2012); OSRC acquired by Intrinsic Dec 2022; OSRA governs OSRF projects (Chrome). |
| Org | Lux Capital | verified | Portfolio + Q2 2025 report list Physical Intelligence, Anduril, Auris Health. Size 'Public/Large' is an approximation for an established private VC. |
| Org | DCVC | verified | Agility Robotics page: first investment 2020. |
| Org | Conference on Robot Learning (CoRL 2026) | verified | corl.org: November 9-12, 2026, Austin, Texas. Size/stage empty (n/a for events). |
| Org | Automate (US trade show) | verified | Chrome: May 10-13, 2027, Las Vegas Convention Center. |
| Org | Robotics Summit & Expo | verified | Speakers from Universal Robots, PickNik, Open Robotics (Brian Gerkey); Boston. |
| Robot/Model | NVIDIA Isaac Sim | verified | Listed on nvidia.com/robotics; public GitHub repo isaac-sim/IsaacSim. |
| Robot/Model | NVIDIA Isaac Lab | verified | nvidia.com + Agility page (Agility uses Isaac Lab); GitHub Apache-2.0/BSD. |
| Robot/Model | Tesla Optimus | verified | tesla.com/AI (Chrome). |
| Robot/Model | Amazon Proteus | verified | aboutamazon: first fully autonomous AMR; next generation described. |
| Robot/Model | Amazon Vulcan | verified | aboutamazon: touch-sensing stow/pick arm, regulates force. |
| Robot/Model | Spot (Boston Dynamics) | verified | bostondynamics.com product list. |
| Robot/Model | Stretch (Boston Dynamics) | verified | bostondynamics.com product list. |
| Robot/Model | Atlas (Boston Dynamics) | verified | bostondynamics.com product list. |
| Robot/Model | da Vinci 5 | verified | intuitive da Vinci page: 'Da Vinci 5: our most advanced... multiport platform'. |
| Robot/Model | Figure 03 | verified | figure.ai homepage. |
| Robot/Model | Helix (Figure) | corrected | Model type 'Policy (IL/RL)' -> 'VLA', Release year -> 2025: figure.ai/news/helix (Feb 20, 2025) calls Helix a Vision-Language-Action model; source added. |
| Robot/Model | pi0 (Physical Intelligence) | verified | pi.website blog (Oct 31, 2024); openpi Apache-2.0. |
| Robot/Model | pi0.5 (Physical Intelligence) | verified | openpi README: pi05 released with better open-world generalization. |
| Robot/Model | Skild Brain | verified | skild.ai Series C post. |
| Robot/Model | Digit (Agility Robotics) | verified | agilityrobotics.com: Digit + Arc. |
| Robot/Model | NEO (1X Technologies) | corrected | Key specs said the about page distinguishes NEO Beta/Gamma from EVE Industrial; the about page (curl + Chrome) doesn't mention them. Claim removed. |
| Robot/Model | Field Foundation Models (FieldAI) | verified | FieldAI Aug 2025 release. |
| Robot/Model | Mobile ALOHA | corrected | Built by 'Stanford Robotics Center' -> empty; 'Builder (if not in map)' = Stanford researchers Zipeng Fu, Tony Z. Zhao, Chelsea Finn. The project page doesn't credit SRC. |
| Robot/Model | HIL-SERL | verified | hil-serl.github.io + github rail-berkeley/hil-serl. |
| Robot/Model | Drake | verified | drake.mit.edu: MIT CSAIL origin, TRI-led core development; GitHub opens. |
| Robot/Model | Gazebo | verified | gazebosim docs (SDF worlds, gz sim); OSRA governs OSRF projects. |
