# Verification report: knowledge_locomotion.json

Rows checked: 89 (18 knowledge nodes, 17 robots/models, 54 project candidates). Verified: 72. Corrected: 17. Rejected: 0.

## Method
- Opened all 44 distinct source/reference URLs (curl, HTTP 200 for all, page titles match the cited topic).
- Read the arXiv abstract pages for every cited paper. All are real and on topic: 1901.08652 (Hwangbo et al., ANYmal; abstract states it recovers "from falling even in complex configurations"), 2309.14341 (Extreme Parkour), 2502.01143 (ASAP, RSS 2025), 2608.01506 (Rapid Embodiment Adaptation for Quadrupedal Locomotion, Aug 2026), 2608.17027 (FetchMan, visual humanoid loco-manipulation, Aug 2026), 2610.12435 (VioLA, generalist humanoid control from human data, Oct 2026), 2611.08097 (STEP, perceptive humanoid locomotion, Nov 2026).
- Spot-checked claims on pages: Unitree G1 page says "23~43 joint motors"; Unitree lists H1 / H1-2 as distinct; the legged_gym README says its environments migrated to Isaac Lab; MuJoCo Playground keeps its original JAX/MJX environments; DeepMimic is UC Berkeley + UBC; ASAP page says RSS 2025.
- Validated every select value against schemas/notion-schema.md: all valid. Software/Mechanical/Electrical % sum to 100 for all projects. Every relation name (Knowledge nodes, Robots & models, Prerequisites) resolves inside the file. Prerequisite chains have no cycles. Onboarding projects have no prerequisites. Top3 nodes exist.
- Schema cleanup (not counted as corrections): removed the non-Notion key `_accessibility_reason` from all 18 nodes. Changed `Release year` "unknown" to null on all 17 robots/models, because it is a number field. No `Used in projects` key is present. Status is now "To verify" on nodes (they were "Draft") and on robots/models. Projects stay "Idea", because Projects has no "To verify" option.
- Not applicable: Ecosystem Map organizations. Built by / Used by / Relevant orgs are empty; builders are given as text.

## Corrections
Several Sources/References fields cited arXiv API *search-query* URLs instead of papers. Each one was replaced with concrete papers from that query's results (opened and abstract read), or dropped where the row already cited the specific papers.
- Node "Wheel-legged hybrid locomotion": the only sources were an arXiv query URL plus OCS2. Replaced the query with 2610.38502 (OmniQuad, wheeled-legged hybrid) and 2606.30243 (KYON, wheel-legged quadruped). The vague Key players "Wheel-legged research teams in the opened arXiv results" became named authors/teams.
- Node "Perceptive rough-terrain locomotion": replaced the query URL with 2610.29612 ("Watch Your Step: Anticipated Perception for Humanoid Locomotion"). Added Discipline AI/ML, since the cited methods are learned policies. Key players are now specific.
- Node "Loco-manipulation coordination": dropped the query URL (FetchMan 2608.17027 and OmniH2O stay). Added Discipline AI/ML, since the cited methods are learned policies.
- Node "Cross-embodiment locomotion policies": dropped the query URL (2610.12435 and 2608.01506 stay).
- Node "Humanoid motion imitation & retargeting": Key players listed "UC San Diego", which no opened source supports. Replaced with sourced entities: DeepMimic (UC Berkeley, UBC), OmniH2O authors, ASAP authors, UC Berkeley HybridRobotics.
- 12 project candidates (3 each under Perceptive rough-terrain, Wheel-legged hybrid, Loco-manipulation, Cross-embodiment): the same query-URL replacements in References.

## Verified (one-line reasons)
- 13 other nodes: sources load and support the beginner explanations (Modern Robotics ch.13.1, MIT Underactuated ch.4/5, EPFL BioRob CPG pages, Cheetah-Software/OCS2 MPC, Pinocchio/Crocoddyl WBC, legged_gym/Isaac Lab/MuJoCo Playground RL, PX4 controller diagrams, ANYmal fall recovery).
- 17 robots/models: each exists, and its official page or repo loads with the stated builder (Unitree Go2/G1/H1, Boston Dynamics Spot SDK, ANYmal via ETH paper, Petoi Bittle/OpenCat, Stanford Pupper repo, TurtleBot 4, Bitcraze Crazyflie 2.1, Isaac Lab, legged_gym, MuJoCo Playground, Genesis, Pinocchio, Crocoddyl, OCS2, PX4). Price and Release year are honestly "unknown"/null, not guessed.
- 42 other projects: references load. They are student proposals with plausible selects and cost bands.

## Flags for human review
- Every node has Starter hardware cost "€0 (sim only)". This is accurate for a sim-first entry point, but the branch has no low-cost hardware node. Hardware appears only in projects (Bittle/Pupper €500-5k, Crazyflie €500-5k, passive leg <€500).
- github.com/HybridRobotics/whole_body_tracking (BeyondMimic) says it is retired and points to mjlab. It is still a valid reference.
- github.com/Genesis-Embodied-AI/Genesis now redirects to "genesis-world".
- Kept `sources_consulted` (top-level metadata, not a Notion row) unchanged, including the arXiv query URLs used for saturation.
