# Verification report: output/ecosystem_south_korea_all.json

Verifier run on branch `research/ecosystem-south-korea-all` (input commit 5f15776). No Notion read/write.

## Summary
- Rows in: 15 organizations + 27 robots/models = 42
- Verified: 38 · Corrected: 3 · Rejected: 1
- Rows out: 15 organizations + 26 robots/models = 41, all Status = "To verify" (no project candidates in this file).
- URLs checked: 67 unique via curl; non-200/empty ones (robotics.hyundai.com, robotworld, korearobot.or.kr, rainbow-robotics.com root, wirobotics.com root, naverlabs, cafe.naver.com, kaist.ac.kr, english.motir.go.kr) re-opened via Chrome CDP and load fine. Dead: forum.robotis.com (NXDOMAIN), kiro.re.kr (timeout, 3 URLs).

## Global corrections
- Removed non-Notion key `_relationship_reason` from all 15 organizations (original text remains in commit 5f15776).
- `Status` set to "To verify" on all rows. No `Used in projects` key present.
- All select / multi-select values checked against schemas/notion-schema.md: none invalid. `Size / stage` null kept for ROBOTWORLD, FuturePlay, OROCA, Tommoro (stage unknown). All `Built by` / `Used by` names resolve to organizations in this file.
- Top-level `summary` and `sources_consulted` kept unchanged (not synced rows).

## Open issues
- KIRO: official site unreachable from the VM; 2026 activity not confirmed by an opened source.
- Ballie commercial shipment and RB-Y1/OMX/OMY prices remain unknown (stated as such in rows).

## Row-by-row
| Kind | Row | Result | Reason |
|---|---|---|---|
| Org | Hyundai Motor Group | verified | Sources open and support claims; selects valid. MobED iREX 2025 release, H1 2026 mass production confirmed; robotics.hyundai.com official (via CDP). |
| Org | Samsung Electronics | verified | Sources open and support claims; selects valid. 35% Rainbow stake (Dec 31 2024) and Ballie/Gemini summer-2025 target confirmed; 2025 Q4 IR PDF lists Rainbow consolidation. |
| Org | LG Electronics | verified | Sources open and support claims; selects valid. CLOiD CES 2026: 7-DOF arms, 5-finger hands, VLM+VLA, AXIUM actuators confirmed. |
| Org | Doosan Robotics | verified | Sources open and support claims; selects valid. P3020 30 kg / 2030 mm / ±0.1 mm; Suwon + Bundang sites; doosan-robot2 BSD-3-Clause. |
| Org | Rainbow Robotics | verified | Sources open and support claims; selects valid. Sejong HQ + Seongnam centre on contact page; KOSDAQ-listed (DART). Root site 500s to curl, opens via CDP. |
| Org | ROBOTIS | verified | Sources open and support claims; selects valid. DYNAMIXEL, TurtleBot3, OMX/OMY, AI Worker, AI Sapiens, Physical AI Tools (Apache-2.0, LeRobot) confirmed. |
| Org | WIRobotics | verified | Sources open and support claims; selects valid. KRW 95bn Series B (2026-05-15, FuturePlay among investors), Cheonan registered HQ in site footer, ALLEX BSD model repo. |
| Org | NAVER LABS | verified | Sources open and support claims; selects valid. ARC, Rookie/AMBIDEX, ~100 robots and 60,000+ deliveries in 1784 confirmed. |
| Org | KAIST | verified | Sources open and support claims; selects valid. HOUND 1 (45 kg, 100 m in 19.87 s, single RL controller) and HOUND 2 52/53 kg conflict confirmed. |
| Org | Korea Institute of Robotics & Technology Convergence (KIRO) | corrected | kiro.re.kr times out (curl and CDP); both KIRO sources replaced by ko.wikipedia article (Pohang/POSTECH, founded 2005, KIRO since 2012, underwater/medical/safety/agri centres). Unverifiable P-SURO/RoTIC claims removed; Medical added to Sector; 2026 activity marked unknown. |
| Org | Korea Association of AI Robot Industry (KAR) | verified | Sources open and support claims; selects valid. MOTIR release names KAR as Robotworld 2026 co-organizer; English site title still "Korea Association of Robot Industry". |
| Org | ROBOTWORLD | verified | Sources open and support claims; selects valid. 2026 edition Nov 4-7 at KINTEX confirmed on organizer page (via CDP) and MOTIR release. |
| Org | FuturePlay | verified | Sources open and support claims; selects valid. Deep-tech early-stage investor; portfolio page lists WIRobotics. |
| Org | OROCA | verified | Sources open and support claims; selects valid. Naver cafe (opened 2012, ~49.6k members) and iTurtle README (Pangyo chapter, TurtleBot3-based, Apache-2.0) confirmed. |
| Org | Tommoro Robotics | verified | Sources open and support claims; selects valid. Seoul (Gangnam) address, SNU research roots, CLIP-RT MIT repo, HABILIS Brain/Console on site, arXiv 2609.25558 (22 Sep 2026) confirmed. |
| Robot/Model | MobED | verified | Sources open and support claims; selects valid. |
| Robot/Model | Ballie | verified | Sources open and support claims; selects valid. |
| Robot/Model | LG CLOiD | verified | Sources open and support claims; selects valid. |
| Robot/Model | P3020 | verified | Sources open and support claims; selects valid. |
| Robot/Model | doosan-robot2 | verified | Sources open and support claims; selects valid. BSD-3-Clause LICENSE confirmed. |
| Robot/Model | RB-Y1 | verified | Sources open and support claims; selects valid. 7-DOF x2 arms, 3 kg payload; total DOF 20/26 by config. |
| Robot/Model | RB-Y1 SDK | verified | Sources open and support claims; selects valid. Apache 2.0 stated in dev manual. |
| Robot/Model | TurtleBot3 | verified | Sources open and support claims; selects valid. 2017, Raspberry Pi 4. |
| Robot/Model | OMX | verified | Sources open and support claims; selects valid. 5+1 DOF, 400 mm reach, 560 g, 100/250 g payload. |
| Robot/Model | OMY | verified | Sources open and support claims; selects valid. 6-DOF DYNAMIXEL-Y. |
| Robot/Model | AI Worker | corrected | Source forum.robotis.com is NXDOMAIN; replaced by ai.robotis.com AI Worker intro + model-training docs + github.com/ROBOTIS-GIT/ai_worker (created 2025-04-04). Unverifiable "May 2025 demo" wording replaced by documented imitation-learning pipeline. |
| Robot/Model | AI Sapiens | verified | Sources open and support claims; selects valid. 23-DOF, DYNAMIXEL-Q, labelled open source. |
| Robot/Model | Physical AI Tools | verified | Sources open and support claims; selects valid. Apache-2.0, LeRobot + ROS 2. |
| Robot/Model | WIM | verified | Sources open and support claims; selects valid. 3,000+ cumulative units and WIM Premium subscription in 2026-05-15 news. |
| Robot/Model | ALLEX | verified | Sources open and support claims; selects valid. Unveiled 2025-08-20; research-prototype v2, limited research edition later this year (repo README). |
| Robot/Model | ALLEX Simulation Model | verified | Sources open and support claims; selects valid. BSD, 48 actuated DOF, 12 passive couplings; open-model news 2026-06-30. |
| Robot/Model | ARC | verified | Sources open and support claims; selects valid. |
| Robot/Model | Rookie 2 | verified | Sources open and support claims; selects valid. |
| Robot/Model | AMBIDEX | verified | Sources open and support claims; selects valid. |
| Robot/Model | KAIST HOUND 1 | verified | Sources open and support claims; selects valid. |
| Robot/Model | KAIST HOUND 2 | verified | Sources open and support claims; selects valid. |
| Robot/Model | P-SURO II | rejected | Only source (kiro.re.kr/dev/sintro.asp) unreachable from curl and Chrome CDP; no other source found; historical 2010-2015 platform with no form-factor fit. Removed. |
| Robot/Model | iTurtle | verified | Sources open and support claims; selects valid. |
| Robot/Model | ACT (Action Chunking with Transformers) | corrected | Dead forum.robotis.com source replaced by ai.robotis.com AI Worker model-training docs (--policy.type=act), which support Used by ROBOTIS; Release year null -> 2023 (RSS 2023 on ALOHA page). |
| Robot/Model | CLIP-RT | verified | Sources open and support claims; selects valid. RSS 2025, SNU, MIT license, 93.1% LIBERO; SNU release 2025-05-13. |
| Robot/Model | HABILIS Brain 0 | verified | Sources open and support claims; selects valid. arXiv abstract: GC-VLA 95.20% LIBERO, 99.55% with GCRF. |
| Robot/Model | HABILIS Console | verified | Sources open and support claims; selects valid. Described on tommoro.ai. |
