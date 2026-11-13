# Coverage gaps: output/ecosystem_south_korea_all.json

Critic run on branch `research/ecosystem-south-korea-all` (file after verification: 15 organizations + 26 robots/models).
Slice depth in `branches.yaml` is "top 15", so gaps are judged against a top-15 shortlist: "High" means a player
everyone would expect in a Korea top 15 (or that would plausibly displace a current row), not just "missing".
References used: Korean national robotics bodies and directories (MOTIR, KIRIA, KAR), ROBOTWORLD / Daegu ROBEX exhibitor
categories, major Korean conferences, KOSDAQ-listed robotics companies, well-known Korean labs, and the researcher's own
"bounded omissions" list in reports/research_ecosystem_south_korea_all.md.
No rows added; no Notion access. Items come from domain knowledge and were **not** web-checked in this pass; the
researcher must confirm each with a primary source (items marked "verify" are less certain).

## High
- HD Hyundai Robotics — Korea's largest industrial-robot maker, separate group from Hyundai Motor Group; obvious Industrial anchor absent.
- Hanwha Robotics (Hanwha group) — HCR collaborative robots; second big cobot maker next to Doosan, absent.
- Neuromeka — Indy cobots with public ROS 2 drivers; researcher dropped it only for the 15 cap; strong student-accessible open-stack candidate.
- KIST (Korea Institute of Science and Technology) — main national robotics/AI research institute (humanoid, manipulation); the file has only KIRO as a public lab.
- Seoul National University (as its own row; robot-learning labs behind CLIP-RT/Tommoro) — top Korean robot-learning school; currently only implied via Tommoro.
- KIRIA (Korea Institute for Robotics Industry Advancement) — government agency running national robot programs, the eRobot directory and funding calls; key entry point and funder.
- MOTIR (Ministry of Trade, Industry and Resources) robot programs / K-Humanoid Alliance (launched 2025; verify name and current status) — main public money and coalition for Korean humanoids; cited as a source but not an org row.
- CoRL 2025 (Seoul) and IEEE-RAS Humanoids 2025 (Seoul) (verify) — the flagship robot-learning and humanoid conferences recently held in Korea; the only Event row is a trade show (ROBOTWORLD), nothing academic.
- Boston Dynamics (Hyundai-owned; Spot/Atlas) — not Korean-HQ, but the Hyundai row should at least mention it; Spot/Atlas absent from Robots & Models.
- RaiSim / Raibo (KAIST Hwangbo lab, Raion Robotics; verify licensing) — Korean RL simulator and quadruped widely used for sim-to-real locomotion; directly on the lab's wedge.

## Medium
- Korea Robotics Society (KROS) and its KRoC conference — national academic society; Mentor/Speaker path.
- Daegu ROBEX / Korea Robot Industry cluster in Daegu (KIRIA HQ city) — second major robot show and cluster.
- POSTECH and UNIST — strong robotics schools; POSTECH is KIRO's partner (already named in KIRO row).
- KAIST labs beyond HOUND: Hubo Lab (DRC-HUBO lineage, Rainbow origin), Urban Robotics / DreamWaQ quadruped RL, KAIST Humanoid (verify) — one KAIST row may hide several.
- Angel Robotics (KOSDAQ-listed wearable exoskeletons, WalkON Suit) — Medical/wearable sector beyond WIRobotics.
- Curexo and Koh Young Technology (Koh Young surgical robot; verify) — Korean medical robotics; Medical is nearly absent.
- Clobot (robot fleet/navigation software) and Yujin Robot (iClebo, LiDAR, GoCart AMR) — Software and Mobility gaps from researcher's own omissions list.
- Twinny and Bear Robotics (Korean-founded, US HQ; Servi) — logistics/service mobile robots.
- AeiRobot and Holiday Robotics (verify) — Korean humanoid startups besides WIRobotics.
- Hyundai Rotem / LIG Nex1 / Hanwha Aerospace — defense UGVs and drones; Defense sector entirely absent.
- Samsung Ventures, Kakao Ventures, NAVER D2SF, KB/KDB investors and Hyundai CRADLE — only one Investor row (FuturePlay); funding layer thin.
- Rebellions / FuriosaAI — Korean AI chips; Hardware/Compute and Components layers essentially empty.
- Aidin Robotics (force/torque sensors) and Korean actuator/reducer suppliers (e.g., SBB Tech; verify) — Components layer gap.
- Robots: HD Hyundai HH/YL series, Hanwha HCR, Neuromeka Indy, Rainbow RB cobot series, Doosan M/H/A/E series (only P3020 listed), LG CLOi GuideBot/ServeBot, Samsung Bot Handy (verify status), Spot.

## Low
- Kakao / Kakao Mobility robotics, KT and SK Telecom service-robot efforts — telco/platform players, mostly pilots.
- Korea Robot Game Festival / national student robot competitions and RoboCup Korea — student visibility channels.
- Seoul-region hackathons and ROS Korea user meetups beyond OROCA (verify).
- Gwangju/Busan robot clusters and regional technoparks — local support bodies.
- Agricultural robots (Daedong, TYM autonomous tractors) — Agri sector beyond KIRO.
- Korean university spin-offs in dexterous hands (e.g., Tesollo; verify) — niche hardware relevant to manipulation demos.
- Historical/legacy platforms (HUBO, DRC-HUBO+, P-SURO) — context only, low value for 2026 relevance.

## Notes for the re-run
- Several High items are blocked by the 15-row cap; if the cap stays, consider swapping in HD Hyundai Robotics, Hanwha Robotics/Neuromeka, KIST and KIRIA, and covering CoRL 2025 as an Event.
- Sector coverage today: no Defense, Agri only via KIRO, Medical only via KIRO; Value chain lacks Components and Compute.
