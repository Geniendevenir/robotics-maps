# Verification report: knowledge_manipulation.json

Rows checked: 89 (17 knowledge nodes, 21 robots/models, 51 project candidates). Verified: 75. Corrected: 14. Rejected: 0.

## Method
- Opened all 32 distinct source/reference URLs: 31 returned HTTP 200 with matching content. The pi0 blog returned HTTP 429 (rate limit). pi0 is still backed by the openpi GitHub repo, which loads.
- The 2026 papers I cited are real and match the topics they support: arXiv 2609.07859 (M3-Tele, compliant whole-body mobile manipulation teleop), arXiv 2609.12549 (STAR, tactile VLA for dexterous manipulation) and PMLR v306 li26fs (DECO, bimanual dexterous with tactile adapter).
- I checked key facts on the pages themselves: builders and affiliations, STS3215 servos, ICRA/CVPR years, 7B params.
- I validated every select value against schemas/notion-schema.md. All valid. Project work splits sum to 100. All relation names resolve within the file. Prerequisite chains are acyclic.
- Schema cleanup: removed the non-Notion key `_accessibility_reason` from the nodes. Release year values of "unknown" became null, because Release year is a number field. No `Used in projects` key is present.
- Status: nodes and robots/models are now "To verify". Projects stay "Idea", because the Projects Status field has no "To verify" option.
- Not checked: Ecosystem Map organizations. This file contains none (Built by / Used by / Relevant orgs are empty).

## Flags for human review
- Project "Record leader-follower trajectories": real recording needs SO-101 hardware, but the row says €0 (sim only) and 100% software. The SO-101 kit price is unknown, so I left it unchanged.
- RSS XXI proceedings index (cited on the VLA node) is a generic index page, not a specific paper. It is supplementary only.

## Rows

| Table | Row | Verdict | Reason |
|---|---|---|---|
| Knowledge node | Grippers & end-effectors | verified |  |
| Knowledge node | Grasp mechanics | verified |  |
| Knowledge node | Pick-and-place pipeline | corrected | duplicate source removed; added MIT pick.html chapter (opened, covers pick-and-place) |
| Knowledge node | Teleoperation & demonstration collection for arms | verified |  |
| Knowledge node | Learning-based grasp detection | verified |  |
| Knowledge node | Object pose estimation for manipulation | verified |  |
| Knowledge node | Collision-free arm motion generation | verified |  |
| Knowledge node | Force/compliant & contact-rich manipulation | verified |  |
| Knowledge node | Bimanual manipulation | verified |  |
| Knowledge node | Mobile manipulation | verified |  |
| Knowledge node | Tactile sensing for manipulation | verified |  |
| Knowledge node | Deformable object manipulation | verified |  |
| Knowledge node | Dexterous in-hand manipulation | verified |  |
| Knowledge node | Non-prehensile manipulation | verified |  |
| Knowledge node | Long-horizon / task-and-motion planning | corrected | only one distinct source (listed twice); added MIT trajectories.html which has a Task and motion planning section |
| Knowledge node | Open-vocabulary & affordance manipulation | verified |  |
| Knowledge node | Generalist manipulation policies / VLAs | verified |  |
| Robot/model | SO-101 | corrected | HF LeRobot docs load; follower uses six STS3215 servos confirmed; Release year "unknown" -> null (number field) |
| Robot/model | ALOHA 2 | corrected | project page loads; builder "ALOHA 2 team" -> Google DeepMind (per aloha-2.github.io) |
| Robot/model | Mobile ALOHA | verified | project page loads; Stanford team, mobile bimanual teleop confirmed |
| Robot/model | LEAP Hand | verified | leaphand.com loads; CMU hand with CAD/URDF confirmed |
| Robot/model | GelSight Mini | corrected | official GelSight product page loads; product exists; Release year "unknown" -> null (number field) |
| Robot/model | MuJoCo | corrected | source loads and supports claims; Release year "unknown" -> null (number field) |
| Robot/model | ManiSkill | corrected | maniskill.ai loads; simulator with tasks and demos; Release year "unknown" -> null (number field) |
| Robot/model | robosuite | corrected | robosuite.ai loads; ARISE-Initiative repo confirmed; Release year "unknown" -> null (number field) |
| Robot/model | MoveIt 2 | verified | official MoveIt 2 docs load |
| Robot/model | cuRobo | corrected | curobo.org loads; NVIDIA confirmed; Release year "unknown" -> null (number field) |
| Robot/model | Contact-GraspNet | verified | NVlabs repo loads; ICRA 2021 confirmed |
| Robot/model | GraspNet-1Billion | corrected | source loads and supports claims; Release year "unknown" -> null (number field) |
| Robot/model | AnyGrasp | corrected | graspnet.net links AnyGrasp (SDK, not fully open); Release year "unknown" -> null (number field) |
| Robot/model | FoundationPose | verified | NVlabs page loads; CVPR 2024 confirmed |
| Robot/model | Cloth Funnels | corrected | project page loads; Columbia/TRI confirmed; Release year "unknown" -> null (number field); release year set to 2023 (ICRA 2023 on project page) |
| Robot/model | ReKep | verified | project page loads; Stanford/Columbia confirmed |
| Robot/model | VoxPoser | verified | project page loads; Stanford/UIUC confirmed |
| Robot/model | OpenVLA | verified | project page loads; 7B params confirmed |
| Robot/model | Octo | verified | project page loads; Octo Model Team confirmed |
| Robot/model | pi0 | verified | openpi repo loads with pi0 code/checkpoints (PI blog returned HTTP 429 to the bot, not used as sole source) |
| Robot/model | Diffusion Policy | verified | project page loads; Columbia/MIT/TRI confirmed |
| Project | Compare fingertip pads | corrected | deliverable implied physical pad materials but row is €0 (sim only) / 100% software; reworded to simulation |
| Project | Simulate suction versus pinch | verified | select values valid, % sum 100, relations resolve, references load |
| Project | Design a compliant fingertip | corrected | designing/fabricating a fingertip is a custom part, not "1 - Off-the-shelf" |
| Project | Draw friction cones | verified | select values valid, % sum 100, relations resolve, references load |
| Project | Test force closure numerically | verified | select values valid, % sum 100, relations resolve, references load |
| Project | Predict and measure slip | verified | select values valid, % sum 100, relations resolve, references load |
| Project | Script a cube transfer | verified | select values valid, % sum 100, relations resolve, references load |
| Project | Build a clutter-clearing state machine | verified | select values valid, % sum 100, relations resolve, references load |
| Project | Add failed-grasp recovery | verified | select values valid, % sum 100, relations resolve, references load |
| Project | Record leader-follower trajectories | verified | select values valid, % sum 100, relations resolve, references load; FLAG: real leader-follower recording needs SO-101 hardware though cost is €0 (sim only), human to confirm |
| Project | Audit demonstration timing | verified | select values valid, % sum 100, relations resolve, references load |
| Project | Train a transfer policy from demonstrations | verified | select values valid, % sum 100, relations resolve, references load |
| Project | Visualize grasp candidates | verified | select values valid, % sum 100, relations resolve, references load |
| Project | Filter grasps by reachability | verified | select values valid, % sum 100, relations resolve, references load |
| Project | Benchmark cluttered bin picking | verified | select values valid, % sum 100, relations resolve, references load |
| Project | Overlay tracked object axes | verified | select values valid, % sum 100, relations resolve, references load |
| Project | Connect pose tracking to a grasp | verified | select values valid, % sum 100, relations resolve, references load |
| Project | Test recovery after occlusion | verified | select values valid, % sum 100, relations resolve, references load |
| Project | Plan around a tabletop obstacle | verified | select values valid, % sum 100, relations resolve, references load |
| Project | Compare MoveIt and cuRobo paths | verified | select values valid, % sum 100, relations resolve, references load |
| Project | Replan a carried object through clutter | verified | select values valid, % sum 100, relations resolve, references load |
| Project | Simulate a virtual spring | verified | select values valid, % sum 100, relations resolve, references load |
| Project | Insert a peg with compliance | verified | select values valid, % sum 100, relations resolve, references load |
| Project | Adapt insertion to pose error | verified | select values valid, % sum 100, relations resolve, references load |
| Project | Coordinate two simulated grippers | verified | select values valid, % sum 100, relations resolve, references load |
| Project | Teleoperate a two-arm handover | verified | select values valid, % sum 100, relations resolve, references load |
| Project | Learn coordinated box opening | verified | select values valid, % sum 100, relations resolve, references load |
| Project | Choose reachable base poses | verified | select values valid, % sum 100, relations resolve, references load |
| Project | Carry an object between stations in simulation | verified | select values valid, % sum 100, relations resolve, references load |
| Project | Learn a mobile cabinet interaction | verified | select values valid, % sum 100, relations resolve, references load |
| Project | Visualize gel contact images | verified | select values valid, % sum 100, relations resolve, references load |
| Project | Detect slip from tactile sequences | verified | select values valid, % sum 100, relations resolve, references load |
| Project | Use touch to adjust grip during lift | verified | select values valid, % sum 100, relations resolve, references load |
| Project | Track cloth corners | verified | select values valid, % sum 100, relations resolve, references load |
| Project | Reproduce a cloth unfolding primitive | verified | select values valid, % sum 100, relations resolve, references load |
| Project | Compare policies across cloth materials | verified | select values valid, % sum 100, relations resolve, references load |
| Project | Replay hand joint motions | verified | select values valid, % sum 100, relations resolve, references load |
| Project | Rotate a cube in simulation | verified | select values valid, % sum 100, relations resolve, references load |
| Project | Transfer an object-rotation policy to a hand | verified | select values valid, % sum 100, relations resolve, references load |
| Project | Simulate a straight push | verified | select values valid, % sum 100, relations resolve, references load |
| Project | Push an object into a graspable pose | verified | select values valid, % sum 100, relations resolve, references load |
| Project | Learn feedback pushing under friction variation | verified | select values valid, % sum 100, relations resolve, references load |
| Project | Build a manipulation behavior tree | verified | select values valid, % sum 100, relations resolve, references load |
| Project | Plan rearrangement with geometric checks | verified | select values valid, % sum 100, relations resolve, references load |
| Project | Recover a multi-step task after a blocked grasp | verified | select values valid, % sum 100, relations resolve, references load |
| Project | Visualize language-conditioned action regions | verified | select values valid, % sum 100, relations resolve, references load |
| Project | Solve a keypoint-constrained manipulation task | verified | select values valid, % sum 100, relations resolve, references load |
| Project | Evaluate novel object instructions with safety rejection | verified | select values valid, % sum 100, relations resolve, references load |
| Project | Inspect a generalist policy action output | verified | select values valid, % sum 100, relations resolve, references load |
| Project | Fine-tune a policy on one tabletop task | verified | select values valid, % sum 100, relations resolve, references load |
| Project | Compare language-conditioned policies on held-out objects | verified | select values valid, % sum 100, relations resolve, references load |
