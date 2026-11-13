# Coverage gaps — Europe Software & AI

Reviewed 2026-11-13 against `devin/playbooks/coverage-critic.md`, `CLAUDE.md`, `schemas/notion-schema.md`, and `reports/verify_ecosystem_europe_software_ai.md`.

**Result: 7 High / 10 Medium / 2 Low gaps (19 total).** These are coverage priorities, not factual rejections of the verified rows or a proposed 39-organization dataset. The input has 20 organizations and 21 robots/models/tools; 18 gaps concern absent organizations and their software, and one concerns a missing tool from an organization already present. No JSON rows were added or edited, and Notion was not accessed.

## Scope and comparison

The assigned slice is Europe, Software & AI, **top 20**. European operations count, consistent with the verifier's treatment of Hugging Face and Genesis AI; Intrinsic is assessed through its European subsidiary, not described as European-headquartered. Organization types include companies, labs and open-source communities, as in the input. Simulation, middleware, perception and navigation are software capabilities within this slice, not hardware-platform discovery.

The comparison used Dealroom's European robotics list and physical-AI market map [S1–S2], the official ERF 2026 sponsor/exhibitor list [S3], FOV Ventures' 2026 enabling-stack taxonomy [S4], the GdR Robotique national directory [S5], and ELLIS's robot-learning programme [S6]. These references reveal a broader software stack than the input's concentration on manipulation models, humanoid intelligence and recent financing. Official product pages, documentation, lab pages and repositories substantiate each ranked gap below. All names and tool aliases listed below were checked against the complete input JSON and are absent.

Importance is a review judgment: **High** means a substantial hole in a top-20 European software map or in the lab's accessible learning-tool choices; **Medium** means a credible contender that improves a particular capability or partner route; **Low** means a narrower alternative after those capabilities are represented. Funding rank alone does not determine importance, and accessibility does not establish that the proposed LeRobot wedge is best.

## High — 7

- **H1 — phospho / phosphobot:** Missing Paris-connected alternative for low-cost robot learning: its open-source software controls SO-100/SO-101 arms, records demonstrations and trains action models, providing a direct comparison with LeRobot rather than assuming one stack is the only accessible route [S2, S7–S9].
- **H2 — eProsima / Fast DDS / Vulcanexus:** Missing European middleware developer and practical ROS 2 infrastructure; its open-source stack combines robot communication, microcontroller integration, monitoring and simulation, capabilities not represented merely by listing ROS 2 under ROS-Industrial Europe [S3, S10].
- **H3 — Intrinsic / Flowstate / Intrinsic Core:** Missing major industrial-robot software contender with explicit European presence through Intrinsic Innovation GmbH; its developer environment combines perception, motion planning and sensor-based control, while Core supplies ROS-compatible open-source capabilities [S3, S11].
- **H4 — Cyberbotics / Webots:** Missing Swiss simulator maintainer and accessible open-source robot-development environment; Webots supports Python/ROS, ready-made robot assets and algorithm testing before buying hardware, filling a practical simulation-provider gap [S5, S12].
- **H5 — MuJoCo (Google DeepMind already present):** Missing open-source physics engine in `robots_models`, despite its maintainer already having an organization row; this is a tool-coverage gap for control and robot-learning simulation, not a request for another DeepMind organization [S13].
- **H6 — Oxa (formerly Oxbotica):** Missing established Oxford autonomy-software company identified by Dealroom; its vehicle-independent industrial driving and fleet software adds ports, airports and yard autonomy beyond Wayve's road-driving emphasis [S1, S14].
- **H7 — Helsing:** Missing major European autonomous-systems AI company at the top of Dealroom's robotics funding list; its official description explicitly covers AI-defined systems and connecting existing hardware, so omitting it leaves the software map's Defense sector unrepresented; practical student access and partnership availability are unknown [S1, S15].

## Medium — 10

- **M1 — Siemens / Tecnomatix Process Simulate:** Missing established industrial simulation and robot-programming software provider; its June 2026 release describes robotic process simulation, offline programming and AI-assisted workflows, balancing the startup-heavy selection [S16].
- **M2 — Coppelia Robotics / CoppeliaSim:** Missing Zurich-based simulator developer whose Python APIs, multiple physics engines, kinematics and motion planning offer another practical environment for manipulation and control experiments; assess alongside Webots rather than requiring both organization slots [S17].
- **M3 — BlueBotics / ANT:** Missing Swiss navigation-software and fleet-interoperability provider for AGVs/AMRs; its navigation and fleet tools demonstrate a mature software layer between middleware and complete mobile-robot platforms [S18].
- **M4 — Embotech:** Missing industrial-autonomy software contender whose official platform description combines prediction, motion planning and a separate safety architecture; useful comparison with Oxa for factory/yard autonomy, with certification and performance treated as company claims [S19].
- **M5 — Slamcore:** Missing London spatial-intelligence company and SLAM-derived software expertise; current official offerings emphasize positioning and awareness for industrial vehicles, including manual fleets, so research the current product scope rather than assuming the older robot SDK remains available [S20].
- **M6 — Roboception / rc_reason:** Missing perception-software provider offering object detection and grasp-point computation through modular AI/vision software; assess the software separately from its stereo sensors so the entry remains in Software & AI [S21].
- **M7 — TU Darmstadt Intelligent Autonomous Systems:** Previously considered but absent from the cleaned rows; its robot manipulation, reinforcement learning and multi-embodiment research provides a European academic comparison with ETH RSL and a potential technical-speaker route, with contact availability unknown [S6, S22].
- **M8 — Robotec.ai:** Missing Warsaw simulation-software company with open-source GPU sensor simulation, ROS 2/O3DE work and synthetic-data tooling; covers the simulation-and-validation infrastructure beyond model builders and robot-data visualization [S23].
- **M9 — Automatika Robotics / EMOS:** Missing Grenoble software startup with an open-source runtime combining perception/language components, navigation and robot application orchestration; its actual documentation gives a concrete European alternative to examine, without adopting its profile's speed or deployment claims as verified results [S24–S25].
- **M10 — Extend Robotics:** Missing Reading/London software company offering VR teleoperation, robot-training workflows and fleet/data management; adds a dedicated demonstration-collection interface provider alongside Neuracore's data infrastructure [S26].

## Low — 2

- **L1 — Algoryx / AGX Dynamics:** Missing Swedish physics-simulation provider and ERF 2026 sponsor; its contact dynamics, sensor simulation and machine-autonomy tools broaden industrial/heavy-machinery simulation, but are a lower priority for this beginner lab than accessible general-purpose simulators [S3, S27].
- **L2 — The Robot Learning Company / TRLC-DK1 software:** Missing Dealroom-listed European robot-learning entrant with a German company named in its repository and a LeRobot-compatible open-source kit/control package; useful as an alternative ecosystem route, but much of its differentiator is hardware and therefore overlaps the Platforms slice [S2, S28–S29].

## Top-20 decision and boundaries

Re-run discovery on H1–H7 only before accepting this slice as covered, then verify any proposed replacements. H5 can be addressed under the existing DeepMind identity; the other High gaps are contenders for the existing 20 organization slots. Re-rank rather than append every gap. The Medium and Low sections are alternatives for deliberate tradeoffs, not mandatory additions. In particular, the current file offers no standalone simulator maintainer and no dedicated European ROS 2 middleware developer, while several slots address closely related factory/humanoid learning products.

Do not duplicate Hugging Face, DeepMind, ETH RSL, Rerun, Neuracore or ROS-Industrial Europe. Merely listing ROS 2 does not also list its independent European suppliers. Hardware-first candidates such as THEKER, Neura Robotics and PAL Robotics require a distinct software case before displacing a software provider; investor directories contain many such adjacent-platform entries. Do not expand this pass into events, investors, hiring or a general directory of every European research lab. The EU is not the geographic boundary: the UK and Switzerland are in scope.

Directory presence is a discovery signal, not evidence of current funding, legal status or partnership willingness. GdR's public directory includes historical names and restricts some details behind login; it was used for cross-checking, not current rankings. FOV explicitly describes its selection as subjective and non-exhaustive; only its accessible taxonomy text was relied on. Undated official pages establish described offerings, not independently audited November 2026 deployment or performance. Prices, free academic eligibility, company stages and warm introductions remain unknown unless separately verified during the follow-up.

## Search stop and evidence register

The final three landscape queries below returned no **additional selected top-20 gap candidates** after screening against the accumulated directory/product evidence (0/10 returned pages per query, below 10%). This is saturation of this prioritized shortlist, not a claim that fewer than 10% of all named European companies are new or that every small provider has been researched. Earlier broad queries did discover additional candidates, including BlueBotics, Extend Robotics and Automatika, which are included above.

| Final query, in order | Returned pages | Newly selected gap candidates |
|---|---:|---:|
| Europe robot software companies AI middleware leading startups | 10 | 0 |
| European robotics software market companies simulation autonomy | 10 | 0 |
| Europe robotics robot learning open source software startup map | 10 | 0 |

The following **29 distinct URLs were opened and supporting returned content inspected** on 2026-11-13. Sources attached to a gap substantiate the entity or capability; they do not substantiate the priority judgment. Most are primary sources. No paywall or authentication restriction was bypassed.

| ID | Opened source | Role |
|---|---|---|
| S1 | https://dealroom.co/lists/robotics-startups-europe/ | European comparison list, marked updated 2026-10-31; Oxa and Helsing discovery/location. |
| S2 | https://dealroom.co/api/marketmap-render?slug=european-robotics-market-map | Physical-AI comparison map; phospho and TRLC discovery. |
| S3 | https://erf2026.eu/sponsors-exhibitors/ | Official 2026 roster; eProsima, Algoryx and Intrinsic Innovation GmbH. |
| S4 | https://viewpoints.fov.ventures/p/fov-robotics-market-map-2026 | March 2026 landscape and enabling-stack taxonomy. |
| S5 | https://www.gdr-robotique.org/entreprises/ | National research-network directory, including Cyberbotics; historical limitations noted above. |
| S6 | https://ellis.eu/research/programs/ellis-robot-learning-closing-the-reality-gap | European robot-learning programme, including Jan Peters/TU Darmstadt. |
| S7 | https://phospho.ai/ | Official robotics toolkit and service offering. |
| S8 | https://github.com/phospho-app/phosphobot | Primary software repository, supported robots and learning workflow. |
| S9 | https://www.cbinsights.com/company/phospho | Paris location corroboration; old funding fields not relied on. |
| S10 | https://www.eprosima.com/robotics/vulcanexus | Official open-source ROS 2 stack description and Madrid address. |
| S11 | https://www.intrinsic.ai/ | Official Flowstate and Intrinsic Core descriptions. |
| S12 | https://cyberbotics.com/ | Official Webots offering and Swiss address. |
| S13 | https://github.com/google-deepmind/mujoco | Primary simulator repository and maintainer identity. |
| S14 | https://oxa.tech/ | Official industrial-autonomy software offering. |
| S15 | https://helsing.ai/ | Official AI-defined autonomous-systems description. |
| S16 | https://blogs.sw.siemens.com/tecnomatix/discover-whats-new-in-tecnomatix-2606-june-2026/ | Dated June 2026 product release. |
| S17 | https://www.coppeliarobotics.com/ | Official simulator features and Zurich address. |
| S18 | https://bluebotics.com/ | Official ANT navigation/fleet offering and Swiss address. |
| S19 | https://www.embotech.com/ | Official autonomy, planning and safety-architecture description. |
| S20 | https://www.slamcore.com/about/ | Official current positioning, products and London location. |
| S21 | https://roboception.com/ | Official rc_reason perception/AI software description. |
| S22 | https://www.ias.informatik.tu-darmstadt.de/ | Official lab research descriptions. |
| S23 | https://www.robotec.ai/technologies | Official simulation tooling, open-source work and Warsaw address. |
| S24 | https://www.euroquity.com/en/company/automatika-robotics | Company profile and Grenoble location; promotional performance claims excluded. |
| S25 | https://emos.automatikarobotics.com/ | Primary EMOS documentation and component descriptions. |
| S26 | https://www.extendrobotics.com/ | Official teleoperation, training and fleet/data capabilities; UK addresses. |
| S27 | https://www.algoryx.se/ | Official AGX Dynamics and simulation capabilities. |
| S28 | https://github.com/robot-learning-co/trlc-dk1 | Primary kit software repository and named German company. |
| S29 | https://www.ycombinator.com/companies/the-robot-learning-company | Accelerator/company profile and imitation-learning positioning. |

Validation: input JSON unchanged; all 19 gap subjects absent from it; priorities counted from the one-line gap entries; only this report is intended for commit. No application code changed, so application tests are not applicable.
