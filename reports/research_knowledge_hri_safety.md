# Research report: knowledge branch "HRI & safety"

Researcher output for `output/knowledge_hri_safety.json` (discovery stage, all rows `To verify` / projects `Idea`). Notion was not read or written.

## Scope

Human-robot interaction and safety of robots working near people: safety standards and risk assessment, collaborative operation (speed and separation monitoring, power and force limiting), collision handling, physical HRI and kinesthetic teaching, handovers, legible motion, shared autonomy, social navigation, conversational interfaces, human motion prediction, EU regulation, safe learning / safety filters, semantic safety and guardrails for LLM/VLA-controlled robots, learning from human feedback, and humanoid safety.

Out of scope / deliberately not duplicated: the Embedded & electronics node "Electrical safety & functional safety for robots" (circuit-level and functional-safety electronics stay there; our "Robot safety standards & risk assessment" node covers the HRI-facing risk-assessment method and robot standards). Manipulation nodes (teleoperation, compliant/force control, grasping) are referenced but not repeated. Robots/models already in pilot outputs (SO-101, Reachy Mini, MuJoCo, LeRobot, Diffusion Policy) are referenced by name only. Hiring not researched.

## Counts

- Nodes: 18 (Fundamental: 4, Applied: 10, Frontier: 4)
- Robots & Models (new rows): 19
- Project candidates: 54 (21 Onboarding, 33 Project); every node has 3-6
- Distinct sources cited: 76

## Taxonomy

| Node | Level | Accessibility | Starter cost | Time to first demo | Accessibility reason |
|---|---|---|---|---|---|
| Robot safety standards & risk assessment | Fundamental | 4 | €0 (sim only) | Days | Reading-and-writing work (a risk table) that needs no hardware; the hard part is that full standards are paid. |
| Collaborative operation modes (cobots) | Fundamental | 3 | €0 (sim only) | Days | Concepts can be learned and simulated for free; applying them to a real cell needs a certified robot and expert review. |
| HRI foundations & user-study methods | Fundamental | 5 | €0 (sim only) | Days | Pure method and software; free textbook site and MOOC; any webcam or simulated robot is enough for a first study. |
| Human detection & body-pose tracking for HRI | Fundamental | 5 | <€500 | Days | A laptop webcam and a pretrained model give a demo within a day; matches the team AI strengths. |
| Speed & separation monitoring implementation | Applied | 3 | <€500 | Weeks | Software-heavy and can start in sim with a webcam; a real cell needs certified sensors, so student versions are demos only. |
| Collision detection & reaction (power and force limiting) | Applied | 2 | €0 (sim only) | Weeks | Needs dynamics and torque sensing; simulation is free but the real thing needs a torque-sensing cobot. |
| Shared control & shared autonomy | Applied | 4 | €0 (sim only) | Weeks | Fully doable in simulation with a game controller; reuses teleoperation skills from the manipulation branch. |
| Physical HRI: hand-guiding & kinesthetic teaching | Applied | 3 | €500-5k | Weeks | Real pHRI needs a backdrivable or torque-controlled arm; true hand-guiding on cheap servos is limited and unverified. |
| Human-robot handovers | Applied | 3 | <€500 | Weeks | Combines pose tracking with a cheap arm; benchmarks allow sim-first work. |
| Legible & expressive robot motion | Applied | 4 | €0 (sim only) | Days | Math plus trajectory code; demo in MuJoCo or on a cheap arm in days. |
| Social & human-aware navigation | Applied | 4 | €0 (sim only) | Weeks | Simulation-only start with free ROS 2 tools; software-only. |
| Conversational & multimodal robot interfaces | Applied | 5 | <€500 | Days | Pure software on a $399 open robot or a laptop; closest to team strengths and very filmable. |
| Human motion & intention prediction | Applied | 4 | €0 (sim only) | Weeks | Dataset-driven ML that needs no robot; outputs are easy to visualize. |
| Robotics regulation & compliance in the EU | Applied | 4 | €0 (sim only) | Days | Reading official texts is free; useful for startup credibility but needs expert confirmation. |
| Safe learning & safety filters | Frontier | 3 | €0 (sim only) | Weeks | Simulation-only and math-heavy; strong fit for AI students willing to learn some control. |
| Semantic safety & guardrails for LLM/VLA-controlled robots | Frontier | 4 | €0 (sim only) | Weeks | Text and simulation work using public benchmarks; matches LLM skills; real-robot tests optional. |
| Learning from human feedback & corrections | Frontier | 3 | <€500 | Weeks | Builds on a LeRobot/SO-101 setup the lab may already have; human-in-the-loop experiments take time. |
| Safety of humanoids & dynamically stable mobile robots | Frontier | 1 | €5k+ | Months | Expensive platforms and unsettled standards; mainly a reading and simulation topic for us. |

The `_accessibility_reason` key in the JSON is a non-schema helper field required by the playbook; the verifier/syncer should drop it before Notion sync (it is preserved in the table above).

## Top 3 (accessibility x visual impact x ecosystem relevance / cost)

1. **Conversational & multimodal robot interfaces**: Accessibility 5, under €500 on Reachy Mini (Paris-based Pollen Robotics and Hugging Face), demo in days and very filmable; pure software/AI.
2. **Human detection & body-pose tracking for HRI**: Accessibility 5, a webcam suffices, first demo in a day, and it feeds safety zones, handovers and assistive projects.
3. **Semantic safety & guardrails for LLM/VLA-controlled robots**: €0 sim/text work on public benchmarks (ASIMOV, RoboPAIR, RoboGuard), frontier topic tied to Google DeepMind and LLM robots, matches team LLM strengths.

## Method

- Primary sources opened directly: ISO catalogue pages (via the browser, because plain HTTP gets a Cloudflare challenge), EUR-Lex official texts, vendor pages/docs (Universal Robots, Franka, Unitree, Aldebaran, Furhat, Pollen/Hugging Face), GitHub repositories (HuNavSim, safe-control-gym, Trajectron++, Whisper, Nav2, Reachy Mini), project pages (RoboPAIR, ASIMOV, Gemini Robotics), HRI conference sites and textbook/course site.
- Paper discovery through the arXiv API (web search engines were unreliable); arXiv rows were opened as abstract pages via the API. Claims taken from abstracts only are limited to what the abstract states.
- Query families: HRI safety standards / ISO 10218 / ISO/TS 15066; speed and separation monitoring; power and force limiting and collision detection; perceived safety; social navigation benchmarks; legibility; shared autonomy; handover; kinesthetic teaching; interactive imitation / RLHF; control barrier functions and safe RL; LLM robot jailbreak / guardrails / semantic safety; humanoid safety; conversational and socially assistive robots; human motion prediction.

## Saturation

The last three arXiv queries (newest-first: "human-robot collaboration" AND safety; "social robot" AND "user study"; "shared control" AND teleoperation) returned mostly unseen *papers* (23/24 new) but 0 new *taxonomy entries*: every result mapped onto an existing node (human motion prediction, AR interfaces/communication, RLHF for HRC, social-navigation legibility, co-speech gestures, shared-control arbitration). Saturation is therefore reached at node level; the paper space itself is not saturated (the field publishes continuously), so the verifier/coverage critic may add references but should not expect new nodes.

## Limitations and open points

- ISO full texts are paid: only catalogue status/abstracts were used; contact force/pressure limits are deliberately not quoted.
- Several Robots & Models fields are `unknown` or empty (prices of UR5e, FR3, NAO6, Furhat; Go2 specs; license of Ultralytics YOLO26 and ASIMOV data; RoboPAIR/RoboGuard code availability). `Release year` is set only when tied to a paper/release seen; otherwise null.
- `Built by` / `Used by` relations left empty (Ecosystem Map not yet built for this branch); builders are given in `Builder (if not in map)`.
- Organisation attributions of some arXiv papers (e.g. TU Munich for SARA shield) come from author affiliations and are marked "not verified".
- Regulatory summary (Machinery Regulation 2023/1230 applies from 14 January 2027; AI Act 2024/1689) is not legal advice.
- All project descriptions carry a disclaimer: student demos are not certified safety functions.
- Project durations, cost bands and work splits are planning estimates.

## Sources consulted

- https://ai.google.dev/edge/mediapipe/solutions/vision/pose_landmarker
- https://arxiv.org/abs/1802.01744
- https://arxiv.org/abs/1805.07256
- https://arxiv.org/abs/1810.04953
- https://arxiv.org/abs/1903.11199
- https://arxiv.org/abs/1904.07379
- https://arxiv.org/abs/1908.03046
- https://arxiv.org/abs/2007.12952
- https://arxiv.org/abs/2105.14499
- https://arxiv.org/abs/2108.06266
- https://arxiv.org/abs/2109.06325
- https://arxiv.org/abs/2205.09747
- https://arxiv.org/abs/2211.00600
- https://arxiv.org/abs/2305.01303
- https://arxiv.org/abs/2306.16740
- https://arxiv.org/abs/2311.10582
- https://arxiv.org/abs/2403.05400
- https://arxiv.org/abs/2404.00938
- https://arxiv.org/abs/2404.05100
- https://arxiv.org/abs/2409.02305
- https://arxiv.org/abs/2409.12471
- https://arxiv.org/abs/2409.20184
- https://arxiv.org/abs/2410.13691
- https://arxiv.org/abs/2412.10180
- https://arxiv.org/abs/2412.19595
- https://arxiv.org/abs/2501.03515
- https://arxiv.org/abs/2503.07885
- https://arxiv.org/abs/2503.08663
- https://arxiv.org/abs/2503.20020
- https://arxiv.org/abs/2507.17317
- https://arxiv.org/abs/2508.07611
- https://arxiv.org/abs/2510.03342
- https://arxiv.org/abs/2511.23300
- https://arxiv.org/abs/2602.04056
- https://arxiv.org/abs/2602.20362
- https://arxiv.org/abs/2604.03451
- https://arxiv.org/abs/2606.21011
- https://arxiv.org/abs/2606.27079
- https://arxiv.org/abs/2606.29846
- https://arxiv.org/abs/2608.02809
- https://arxiv.org/abs/2608.10847
- https://arxiv.org/abs/2609.24547
- https://arxiv.org/abs/2609.32346
- https://arxiv.org/abs/2609.37599
- https://arxiv.org/abs/2609.40007
- https://arxiv.org/abs/2610.09891
- https://arxiv.org/abs/2610.11220
- https://asimov-benchmark.github.io/v1/
- https://deepmind.google/models/gemini-robotics/
- https://docs.nav2.org/rolling/
- https://docs.ultralytics.com/tasks/pose/
- https://eur-lex.europa.eu/eli/reg/2023/1230/oj
- https://eur-lex.europa.eu/eli/reg/2024/1689/oj
- https://frankarobotics.github.io/docs/
- https://github.com/StanfordASL/Trajectron-plus-plus
- https://github.com/openai/whisper
- https://github.com/pollen-robotics/reachy_mini
- https://github.com/robotics-upo/hunav_sim
- https://github.com/ros-navigation/navigation2
- https://github.com/utiasDSL/safe-control-gym
- https://huggingface.co/blog/reachy-mini
- https://humanrobotinteraction.org/2026/
- https://robopair.org/
- https://www.aldebaran.com/en/pepper
- https://www.furhatrobotics.com/
- https://www.human-robot-interaction.org/
- https://www.human-robot-interaction.org/course/
- https://www.iso.org/search.html?q=25785
- https://www.iso.org/standard/51528.html
- https://www.iso.org/standard/53820.html
- https://www.iso.org/standard/62996.html
- https://www.iso.org/standard/73933.html
- https://www.iso.org/standard/73934.html
- https://www.ri.cmu.edu/publications/legibility-and-predictability-of-robot-motion/
- https://www.unitree.com/g1/
- https://www.universal-robots.com/products/ur5e/
