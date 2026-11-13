# Verification report: knowledge_hri_safety.json

Rows checked: 91 (18 knowledge nodes, 19 robots/models, 54 project candidates). Verified: 82. Corrected: 9. Rejected: 0.

## Method
- Opened all 76 distinct URLs in the file. 70 returned HTTP 200 to curl. The 6 iso.org URLs return a Cloudflare 403 to curl. I opened them in Chrome instead, and all 6 load and support the claims (editions, dates, review status, ISO/CD 25785-1 under development).
- arXiv: I read the title, authors, date and abstract of all 49 cited papers. All exist, and the dates match the years claimed (including the 2026 papers 2602-2610).
- Vendor and project pages: I checked the key numbers on the pages themselves. These include the G1 price, weight and DOF, the Reachy Mini Lite price, the HRI 2026 dates and venue, MediaPipe's 33 landmarks, UR's PFL wording, and the repo licenses (MIT for Whisper, Trajectron++ and safe-control-gym; AGPL-3.0 for Ultralytics).
- Select values: I checked every node, robot/model and project select value against schemas/notion-schema.md. Four nodes had invalid Accessibility values ("5"/"1"), which I fixed. All project selects are valid. Every work split sums to 100. All Knowledge-node relations resolve inside the file. Prerequisites are empty, so there are no cycles. No name collides with output/existing_projects.json.
- Schema cleanup: removed the non-Notion key `_accessibility_reason` from all 18 nodes. Project ideas stay empty. No `Used in projects` key is present. Built by / Used by / Relevant orgs are empty, so no Ecosystem orgs had to be checked.
- Status: nodes and robots/models are "To verify". Projects stay "Idea", because the Projects Status field has no "To verify" option.

## Flags for human review
- Cross-file relations: projects reference Robots & models that are not defined in this file: SO-101, MuJoCo, Diffusion Policy (defined in output/knowledge_manipulation.json) and LeRobot, Reachy Mini (defined in output/ecosystem_europe_software_ai.json / ecosystem_paris_all.json). The syncer must resolve these across files. I left them unchanged.
- Project "Gravity-compensated guiding mode": it uses the FR3, but its cost band is €500-5k (see the row).
- Nodes "Human-robot handovers" and "Speed & separation monitoring implementation" name the papers' author groups as Key players, not organizations. The row text already says so.
- ISO/TS 15066 is "to be revised" (to be replaced by ISO/AWI 15066-1). Re-check this before the Holygraph is published.

## Rows

| Table | Row | Verdict | Reason |
|---|---|---|---|
| Knowledge node | Robot safety standards & risk assessment | corrected | all 5 ISO pages opened via browser (curl gets Cloudflare 403); editions/dates confirmed; added that ISO marks TS 15066 "to be revised" -> ISO/AWI 15066-1 |
| Knowledge node | Collaborative operation modes (cobots) | verified | TS 15066 scope (industrial only), 2602.20362 blunt-impact gap, UR always-active PFL confirmed |
| Knowledge node | HRI foundations & user-study methods | corrected | Accessibility "5" -> "5 - Easy" (invalid select value); HRI 2026 Edinburgh Mar 16-19, 21st edition, next in Santa Clara confirmed |
| Knowledge node | Human detection & body-pose tracking for HRI | corrected | Accessibility "5" -> "5 - Easy"; MediaPipe 33 3D landmarks + Web and YOLO26 pose on COCO keypoints confirmed |
| Knowledge node | Speed & separation monitoring implementation | verified | ToF arrays (1904.07379) and RGB-D (1810.04953) papers match |
| Knowledge node | Collision detection & reaction (power and force limiting) | verified | 2409.20184 (ISO 10218-2:2025 PFL, per-part thresholds), SARA shield 2412.10180 (TUM authors), 2602.20362 shearing contacts confirmed |
| Knowledge node | Shared control & shared autonomy | verified | Reddy/Dragan/Levine 2018 and the 2026 legible shared autonomy / BlenDAgger papers match |
| Knowledge node | Physical HRI: hand-guiding & kinesthetic teaching | verified | FCI docs load; MR kinesthetic teaching 2409.02305 and observer-based hand-guiding 2608.10847 match |
| Knowledge node | Human-robot handovers | verified | review 2007.12952, HandoverSim 2205.09747, R2HandoverSim 2606.21011 match |
| Knowledge node | Legible & expressive robot motion | verified | CMU page: Dragan, Lee, Srinivasa, Mar 2013; Legibot and 2026 body-language paper match |
| Knowledge node | Social & human-aware navigation | verified | guidelines 2306.16740, HuNavSim repo (v2.0 Gazebo/Isaac/Webots wrappers), Arena 4.0/5.0, Nav2 docs confirmed |
| Knowledge node | Conversational & multimodal robot interfaces | corrected | Accessibility "5" -> "5 - Easy"; Reachy Mini Lite $399 (+taxes+shipping), Whisper MIT, MIRA full-duplex confirmed |
| Knowledge node | Human motion & intention prediction | verified | Trajectron++ repo (ECCV 2020, MIT), Social Force 2311.10582, HRC prediction 2609.32346 confirmed |
| Knowledge node | Robotics regulation & compliance in the EU | verified | EUR-Lex texts of 2023/1230 and 2024/1689 load |
| Knowledge node | Safe learning & safety filters | verified | CBF overview, safe-learning review, safe-control-gym (MIT) and 2609.40007 multi-link VLA filter confirmed |
| Knowledge node | Semantic safety & guardrails for LLM/VLA-controlled robots | verified | RoboPAIR (ICRA 2025, Go2, often 100% success), RoboGuard two-stage, ASIMOV (CoRL 2025, Google DeepMind) confirmed |
| Knowledge node | Learning from human feedback & corrections | verified | IIL survey 2211.00600, BlenDAgger, RLHF scoping review 2610.09891 match |
| Knowledge node | Safety of humanoids & dynamically stable mobile robots | corrected | Accessibility "1" -> "1 - Hard"; ISO/CD 25785-1 under development (ISO search via browser), fail-passive gap paper, G1 from US $13.5K confirmed |
| Robot/model | Universal Robots UR5e | verified | vendor page: configurable safety limits + always-active PFL |
| Robot/model | Franka Research 3 (FR3) | verified | FCI docs load (libfranka, franka_ros2) |
| Robot/model | Unitree G1 | verified | vendor page: from US $13.5K, about 35 kg, 23-43 joint motors |
| Robot/model | Unitree Go2 | verified | RoboPAIR page: GPT-3.5-integrated Unitree Go2 jailbroken |
| Robot/model | NAO6 | corrected | aldebaran.com now redirects to a Maxtronics site saying Aldebaran is closed and Maxtronics supports NAO6; builder text updated |
| Robot/model | Furhat | verified | vendor page: back-projected 3D face engine and voice synthesis (Form factor N/A, no social-robot option) |
| Robot/model | HuNavSim | verified | repo + 2023 paper (U. Pablo de Olavide authors) + v2.0 paper |
| Robot/model | Arena 4.0 | verified | 2024 paper + Arena 5.0 2026 paper |
| Robot/model | Nav2 | verified | docs + GitHub repo load |
| Robot/model | MediaPipe Pose Landmarker | verified | Google AI Edge docs: 33 3D landmarks, web/mobile/desktop |
| Robot/model | Ultralytics YOLO26 Pose | corrected | Open source false -> true: ultralytics GitHub repo is AGPL-3.0; source added |
| Robot/model | Whisper | verified | OpenAI repo, MIT license |
| Robot/model | Trajectron++ | verified | StanfordASL repo, MIT license, ECCV 2020 |
| Robot/model | safe-control-gym | corrected | repo now redirects to learnsyslab/safe-control-gym (README credits U. Toronto Dynamic Systems Lab); builder text updated |
| Robot/model | SARA shield | verified | 2412.10180 abstract names SARA shield, PFL with formal guarantees |
| Robot/model | ASIMOV Benchmark | verified | project page: Google DeepMind, accepted at CoRL 2025 |
| Robot/model | RoboPAIR | verified | project page + arXiv 2410.13691: Jackal UGV and Go2 tested |
| Robot/model | RoboGuard | verified | arXiv 2503.07885 abstract: two-stage guardrail |
| Robot/model | Gemini Robotics 1.5 | corrected | "ER model via API" not stated on the opened DeepMind page; access text made less specific. Page lists On-Device 2 and 2.5 models |
| Project | Intro: write a risk assessment for the lab robot | verified | select values valid, % sum 100, relations resolve (in file or cross-file), references load |
| Project | Safety-limit configurator for a simulated arm | verified | select values valid, % sum 100, relations resolve (in file or cross-file), references load |
| Project | Standards change map: ISO 10218:2025 explainer | verified | select values valid, % sum 100, relations resolve (in file or cross-file), references load |
| Project | Intro: simulate power-and-force-limited contact | verified | select values valid, % sum 100, relations resolve (in file or cross-file), references load |
| Project | Mode switcher: separation monitoring to force limiting | verified | select values valid, % sum 100, relations resolve (in file or cross-file), references load |
| Project | Cobot mode decision tool | verified | select values valid, % sum 100, relations resolve (in file or cross-file), references load |
| Project | Intro: run a 10-person perceived-safety study | verified | select values valid, % sum 100, relations resolve (in file or cross-file), references load |
| Project | Robot speed vs comfort experiment | verified | select values valid, % sum 100, relations resolve (in file or cross-file), references load |
| Project | HRI study toolkit for the lab | verified | select values valid, % sum 100, relations resolve (in file or cross-file), references load |
| Project | Intro: webcam human skeleton in real time | verified | select values valid, % sum 100, relations resolve (in file or cross-file), references load |
| Project | Virtual safety curtain with a webcam | verified | select values valid, % sum 100, relations resolve (in file or cross-file), references load |
| Project | Multi-person pose benchmark for the lab space | verified | select values valid, % sum 100, relations resolve (in file or cross-file), references load |
| Project | Depth-camera separation monitor | verified | select values valid, % sum 100, relations resolve (in file or cross-file), references load |
| Project | Robot-mounted distance sensor skin | verified | select values valid, % sum 100, relations resolve (in file or cross-file), references load |
| Project | Learned speed scaling vs analytic rule | verified | select values valid, % sum 100, relations resolve (in file or cross-file), references load |
| Project | Intro: detect collisions from motor current | verified | select values valid, % sum 100, relations resolve (in file or cross-file), references load |
| Project | Momentum-observer collision detection in sim | verified | select values valid, % sum 100, relations resolve (in file or cross-file), references load |
| Project | Region-aware force limits demo | verified | select values valid, % sum 100, relations resolve (in file or cross-file), references load |
| Project | Intro: joystick shared control in sim | verified | select values valid, % sum 100, relations resolve (in file or cross-file), references load |
| Project | Goal-inference assistive arm | verified | select values valid, % sum 100, relations resolve (in file or cross-file), references load |
| Project | Legible shared autonomy display | verified | select values valid, % sum 100, relations resolve (in file or cross-file), references load |
| Project | Intro: record a motion by moving the arm by hand | verified | select values valid, % sum 100, relations resolve (in file or cross-file), references load |
| Project | Gravity-compensated guiding mode | verified | select values valid, % sum 100, relations resolve (in file or cross-file), references load; FLAG: lists Franka Research 3 but cost is €500-5k; an FR3 is likely above €5k (FR3 price unknown in this file). Human to confirm the arm and cost band |
| Project | Mixed-reality kinesthetic teaching | verified | select values valid, % sum 100, relations resolve (in file or cross-file), references load |
| Project | Intro: detect an open hand ready to receive | verified | select values valid, % sum 100, relations resolve (in file or cross-file), references load |
| Project | Robot-to-human object handover on a desk arm | verified | select values valid, % sum 100, relations resolve (in file or cross-file), references load |
| Project | Handover benchmark in simulation | verified | select values valid, % sum 100, relations resolve (in file or cross-file), references load |
| Project | Intro: legible vs predictable reaching | verified | select values valid, % sum 100, relations resolve (in file or cross-file), references load |
| Project | Legibility online experiment | verified | select values valid, % sum 100, relations resolve (in file or cross-file), references load |
| Project | Expressive head cues on Reachy Mini | verified | select values valid, % sum 100, relations resolve (in file or cross-file), references load |
| Project | Intro: Nav2 robot among simulated pedestrians | verified | select values valid, % sum 100, relations resolve (in file or cross-file), references load |
| Project | Social costmap layer for Nav2 | verified | select values valid, % sum 100, relations resolve (in file or cross-file), references load |
| Project | LLM-generated social navigation scenarios | verified | select values valid, % sum 100, relations resolve (in file or cross-file), references load |
| Project | Intro: voice-commanded Reachy Mini | verified | select values valid, % sum 100, relations resolve (in file or cross-file), references load |
| Project | Interruptible conversational robot | verified | select values valid, % sum 100, relations resolve (in file or cross-file), references load |
| Project | Socially assistive coach robot | verified | select values valid, % sum 100, relations resolve (in file or cross-file), references load |
| Project | Intro: constant-velocity vs social-force prediction | verified | select values valid, % sum 100, relations resolve (in file or cross-file), references load |
| Project | Trajectron++ on lab footage | verified | select values valid, % sum 100, relations resolve (in file or cross-file), references load |
| Project | Reach-target prediction for collaboration | verified | select values valid, % sum 100, relations resolve (in file or cross-file), references load |
| Project | Intro: EU robot regulation one-pager | verified | select values valid, % sum 100, relations resolve (in file or cross-file), references load |
| Project | Compliance checklist for a lab demo robot | verified | select values valid, % sum 100, relations resolve (in file or cross-file), references load |
| Project | AI Act classifier for robot features | verified | select values valid, % sum 100, relations resolve (in file or cross-file), references load |
| Project | Intro: control barrier function on a 2D robot | verified | select values valid, % sum 100, relations resolve (in file or cross-file), references load |
| Project | Safety filter benchmark in safe-control-gym | verified | select values valid, % sum 100, relations resolve (in file or cross-file), references load |
| Project | Safety filter around a learned arm policy | verified | select values valid, % sum 100, relations resolve (in file or cross-file), references load |
| Project | Intro: run the ASIMOV semantic safety benchmark | verified | select values valid, % sum 100, relations resolve (in file or cross-file), references load |
| Project | Guardrail for a language-commanded arm | verified | select values valid, % sum 100, relations resolve (in file or cross-file), references load |
| Project | Red-team day: jailbreak our own robot agent | verified | select values valid, % sum 100, relations resolve (in file or cross-file), references load |
| Project | Intro: correct a robot with one keypress | verified | select values valid, % sum 100, relations resolve (in file or cross-file), references load |
| Project | Human-gated interactive imitation on SO-101 | verified | select values valid, % sum 100, relations resolve (in file or cross-file), references load |
| Project | Preference feedback for comfortable motion | verified | select values valid, % sum 100, relations resolve (in file or cross-file), references load |
| Project | Intro: why humanoids cannot just stop | verified | select values valid, % sum 100, relations resolve (in file or cross-file), references load |
| Project | Controlled-fall and safe-stop behaviours in sim | verified | select values valid, % sum 100, relations resolve (in file or cross-file), references load |
| Project | Humanoid safety readiness review | verified | select values valid, % sum 100, relations resolve (in file or cross-file), references load |
