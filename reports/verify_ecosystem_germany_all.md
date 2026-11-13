# Verification report: output/ecosystem_germany_all.json

Verifier run on branch `research/ecosystem-germany-all` (input commit b635e6c). No Notion read/write.

## Summary
- Rows in: 40 organizations + 19 robots/models = 59
- Verified: 54 · Corrected: 5 · Rejected: 0
- Rows out: 59, all Status = "To verify"
- URLs checked: 93 unique. All return 200 via curl except bosch-ai.com (TLS name error, redirects to bosch.com/research/bcai/), aibusiness.com (403) and helsing.ai (429). is.mpg.de, ceti.one and the hamburg-business.com Naiture article return bot/JS pages to curl. I opened all of these in Chrome (CDP) and checked the claims there. No 404s in cited sources.

## Global checks and corrections
- Removed non-Notion key `_relationship_reason` from all 40 organizations. No `Used in projects` key present.
- Every select / multi-select value checked against schemas/notion-schema.md: all valid. Every `Built by` / `Used by` name resolves to an organization in this file.
- Cross-file duplicate check against every output/*.json on origin/main (normalized names, website domains and keyword grep): no organization or robot/model in this file already exists there. Closest hits are different entities: Fraunhofer IPA (≠ Fraunhofer IML), "DLR David variable-stiffness joints" knowledge row (≠ neoDavid robot), "SCHUNK-Bosch humanoid robot hand" (≠ Bosch Center for AI). NEURA, Agile Robots, Franka and RobCo were already excluded by the researcher.

## Open issues
- Investors use `Size / stage` = Public/Large for established funds and agencies (same as ecosystem_europe_investors_in_robotics), which is only an approximation.
- UnternehmerTUM MakerSpace (Corporate, Non-profit) and MotionLab.Berlin (Startup, Pre-seed/Seed) are makerspace companies with no exact type/stage option. Left as given.
- Naiture: no official website found (Website left empty). Sitegeist and Naiture details rest on one press source each.
- Release year is null for most robots: not stated on the opened sources.
- CeTI Mobile Robotics Hackathon: ceti.one news confirms "over 100 participants" over two days. The October 2026 date comes from the news post timing ("two weeks ago", near the 6 Nov 2026 posts).

## Row-by-row
| Kind | Row | Result | Reason |
|---|---|---|---|
| Org | TUM MIRMI | verified | mirmi.tum.de about page: "over 70 professors", human-centered robotics. |
| Org | KIT H2T | verified | h2t.iar.kit.edu: ARMAR humanoids, KIT hands, ArmarX; 2026 news. |
| Org | TU Darmstadt IAS | verified | IAS homepage: robot learning (Jan Peters), HAINER humanoid; 2025-26 news. |
| Org | DLR Institute of Robotics and Mechatronics | verified | dlr.de/en/rm humanoids page lists Agile Justin, Rollin' Justin, neoDavid. |
| Org | Fraunhofer IML | verified | IML site + evoBOT page; Sep 2026 mobile-robotics conference (loginfo24). |
| Org | Max Planck Institute for Intelligent Systems | verified | is.mpg.de (via CDP): Stuttgart/Tübingen, theory/software/hardware, robotics/materials/optics/medical facilities. |
| Org | TU Dresden CeTI | verified | ceti.one (via CDP): Cluster of Excellence, tactile internet, Nov 2026 demos. |
| Org | TU Berlin RBO | verified | tu.berlin/en/robotics: Prof. Oliver Brock's lab. |
| Org | University of Bonn AIS | verified | NimbRo page: RoboCup 2023 Bordeaux AdultSize win with NimbRo-OP2X. |
| Org | University of Hamburg TAMS | verified | TAMS homepage: director Prof. Jianwei Zhang. |
| Org | DFKI Robotics Innovation Center | verified | About page: "around 125 employees", space/underwater/logistics robots. |
| Org | University of Technology Nuremberg (UTN) | verified | UTN CS & AI dept: Wolfram Burgard founding chair since Feb 2022. |
| Org | Robotics Institute Germany (RIG) | verified | RIG site + The Robot Report: 2024 launch, TUM coordinator. |
| Org | Cyber Valley | verified | cyber-valley.de/en: AI research and start-up ecosystem around MPI-IS, Stuttgart, Tübingen. |
| Org | Roboy | verified | roboy.org: Roboy 3.0 / XPRIZE, "student team of more than 50", not-for-profit research company. |
| Org | B-Human | verified | b-human.de: world champion thirteen times, Bremen/DFKI. |
| Org | Hamburg Bit-Bots | verified | bit-bots.de (1 Aug 2026 post): 2nd place Small Size Division, Humanoid League, RoboCup 2026. |
| Org | TUM.ai | verified | tum-ai.com: 150+ students from 30+ universities, ELAB incubator, hackathons. |
| Org | c-base | verified | c-base.org: "Raumstation unter Berlin", e.V., NixOS-Stammtisch and Netzpolitischer Abend in the Nov 2026 calendar. |
| Org | Fab Lab Aachen | verified | fablab.rwth-aachen.de: Media Computing Group, laser cutter; Sep 2026 notice. |
| Org | MotionLab.Berlin | verified | About page: founded 2018, 110+ startups. |
| Org | UnternehmerTUM MakerSpace | verified | maker-space.de: Garching courses (3D printing etc.) dated Nov 2026. |
| Org | Magazino | verified | magazino.eu: Jungheinrich company, "over 160 experts", TORU/SOTO. |
| Org | Jungheinrich | verified | jungheinrich.com: iF Design Award 2026 for mobile robot EAE 212a. |
| Org | Bosch Center for Artificial Intelligence | corrected | Website bosch-ai.com has an invalid TLS cert and redirects. Set it to https://www.bosch.com/research/bcai/ and added it as a source. HTD claim confirmed in AI Business (May 2026, via CDP). |
| Org | FERNRIDE | verified | fernride.com/news: Series A extension, Gen 4 vehicle kit. |
| Org | ARX Robotics | verified | arx-robotics.com: Gereon, Mithra OS, Hector; 2026 Euro Defence Expo. |
| Org | Unchained Robotics | verified | About page: founded 2019 in Paderborn, marketplace + MalocherBot. |
| Org | Roboception | verified | roboception.com: rc_visard NG, rc_reason; DLR spin-off. |
| Org | Sitegeist | corrected | Website was empty. Set it to https://sitegeist-robotics.com (linked from tech.eu, loads 200). tech.eu confirms Munich-based, €4M pre-seed, Feb 2026. |
| Org | Nature Robots | verified | naturerobots.com: autonomy OS for ag-machinery makers, hybrid localization with(out) GNSS/RTK. |
| Org | goodBytz | verified | goodbytz.com: AI robots + autonomous kitchen operations. |
| Org | Naiture | verified | hamburg-business.com (Nov 2025, via CDP): Friedrichsgabekoog-based, AI laser weeding "Beam", 2-5 km/h, starting serial production. |
| Org | Helsing | verified | helsing.ai (via CDP): Clarity, HX-2, CA-1 Europa, SG-1/Lura maritime autonomy. |
| Org | UVC Partners | corrected | Size / stage Non-profit → Public/Large (private VC, €250M fund IV per munich-startup.de). |
| Org | High-Tech Gründerfonds (HTGF) | corrected | Size / stage Non-profit → Public/Large (public-private VC). htgf.de confirms up to €30M growth tickets and companies under three years old. |
| Org | SPRIND | corrected | Size / stage Non-profit → Public/Large (federal agency). sprind.org lists AI-native chip design and biomanufacturing challenges (Nov 2026 deadlines). |
| Org | Chaos Communication Congress (40C3) | verified | events.ccc.de/congress: 40C3 "Model Citizens", 27-30.12.2026. |
| Org | TUM.ai Makeathon | verified | tum-ai.com: "Makeathon 500+ participants at our signature hackathon". |
| Org | CeTI Mobile Robotics Hackathon | verified | ceti.one news (via CDP): two-day Mobile Robotics Hackathon, over 100 participants. |
| R&M | ARMAR humanoid family | verified | h2t.iar.kit.edu; builder KIT H2T. |
| R&M | ArmarX | verified | h2t.iar.kit.edu; KIT H2T software framework. |
| R&M | Agile Justin | verified | DLR RM humanoids page. |
| R&M | Rollin' Justin | verified | DLR RM humanoids page. |
| R&M | neoDavid | verified | DLR RM humanoids page. |
| R&M | HAINER | verified | IAS homepage: "Our torque-controlled humanoid HAINER". |
| R&M | evoBOT | verified | Fraunhofer IML evoBOT page: two-wheeled inverted-pendulum transport robot. |
| R&M | TORU | verified | Magazino commissioning page. |
| R&M | SOTO | verified | magazino.eu. |
| R&M | rc_visard NG | verified | roboception.com. Kind Robot / Form factor N/A is the closest option for a 3D sensor. |
| R&M | Wolfgang-OP | verified | github.com/bit-bots/wolfgang_robot. |
| R&M | NimbRo-OP2X | verified | AIS NimbRo page: RoboCup 2023 AdultSize win. |
| R&M | Roboy 3.0 | verified | roboy.org nav lists Roboy 3.0 / XPRIZE. |
| R&M | MalocherBot | verified | Unchained about page. |
| R&M | FERNRIDE Gen 4 vehicle kit | verified | fernride.com/news: "Moves Towards Series Production with Release of Gen 4 Vehicle Kit". |
| R&M | Mithra OS | verified | arx-robotics.com. |
| R&M | Naiture laser weeding robot | verified | hamburg-business.com article (via CDP). |
| R&M | Humanoid Transformer with Touch Dreaming (HTD) | verified | AI Business (13 May 2026, via CDP): Bosch Center for AI + CMU, RL + VR data. |
| R&M | Nature Robots Farming Autonomy OS | verified | naturerobots.com. |
