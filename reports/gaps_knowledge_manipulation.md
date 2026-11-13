# Coverage gaps: knowledge_manipulation.json (Manipulation branch)

Reviewed file: `output/knowledge_manipulation.json` (17 nodes, 21 robots/models, 51 project candidates), after verification (see `reports/verify_knowledge_manipulation.md`).

References compared against: the Springer Handbook of Robotics (2nd ed.) TOC: Part C "Sensing and Perception" / Part D "Manipulation and Interfaces" (grasping, robot hands, force control, contact modeling, cooperative manipulators, visual servoing in Part A); the MIT 6.4210 Robotic Manipulation syllabus (Tedrake); Stanford CS326 / Berkeley CS287-style manipulation syllabi; ICRA/RSS/CoRL manipulation topics from 2024-2026 (VLAs, imitation learning, datasets and benchmarks, tactile, dexterous, articulated objects); and the LeRobot/SO-101 stack named in CLAUDE.md as the working wedge.

Scope note: only gaps inside the Manipulation branch, or rows a manipulation map is expected to link to. Items that mainly belong to another branch are marked "(cross-branch)" so the right researcher can pick them up. The names below are well-known items from the field. Their URLs were not re-opened in this pass, so the researcher must source and verify each one before adding a row.

## High

- **ACT (Action Chunking with Transformers)**, Robots & Models: the default LeRobot/ALOHA imitation policy. It is absent from the file (0 mentions), even though projects train policies from SO-101 demonstrations.
- **SmolVLA (Hugging Face, 2025)**, Robots & Models: a small VLA built for LeRobot/SO-101 and fine-tunable on a single consumer GPU. It fits the wedge hypothesis directly and is missing.
- **Manipulation datasets: Open X-Embodiment, DROID, LeRobot Hub datasets**, Robots & Models: these are the data the VLAs here (OpenVLA, Octo, pi0) are trained on. No dataset rows exist.
- **Manipulation benchmarks: LIBERO, SimplerEnv, RLBench/CALVIN**, Robots & Models: standard VLA/imitation evaluation suites. The project "Compare language-conditioned policies on held-out objects" has no benchmark to anchor it.
- **Hand-eye / camera-to-robot calibration**, Knowledge node (Fundamental): a basic requirement for any real camera-plus-arm pick-and-place on SO-101. It is not a node and is only mentioned in passing.
- **Visual servoing (closed-loop vision-based arm control)**, Knowledge node: a full Springer Handbook chapter and a standard course topic. Missing.
- **Low-cost demonstration interfaces: UMI (Universal Manipulation Interface), GELLO**, Robots & Models: key 2024-2026 low-cost data-collection tools for the teleop node. Missing.
- **Relevant orgs / Built by are empty for every row**: expected manipulation players are never linked as organizations: Hugging Face LeRobot and Pollen Robotics (both Paris), Physical Intelligence, Google DeepMind, Toyota Research Institute, NVIDIA, Franka Robotics, and Inria/ISIR labs. This is for the ecosystem researcher. Rows must not be added from this file.

## Medium

- **pi0.5 / pi0-FAST, NVIDIA GR00T N1, Gemini Robotics, RDT-1B**, Robots & Models: 2025-2026 generalist policies. The VLA node's "Frontier state 2026" field only cites OpenVLA, Octo and pi0.
- **Articulated object manipulation (doors, drawers; PartNet-Mobility/SAPIEN)**, Knowledge node: a recurring CoRL/ICRA track that is only touched indirectly by the "mobile cabinet" project.
- **LeRobot hardware variants: Koch v1.1, LeKiwi (SO-101 mobile base)**, Robots & Models: the cheapest real paths for the bimanual and mobile-manipulation nodes.
- **Franka Research 3 / UR5e**, Robots & Models: reference research arms that almost every cited paper uses. Needed to explain the gap from sim to lab hardware.
- **DIGIT / AnySkin low-cost tactile sensors**, Robots & Models: cheaper alternatives to GelSight Mini for the tactile node.
- **Dex-Net / suction grasp planning**, Robots & Models: the canonical suction and parallel-jaw grasp dataset. The "Simulate suction versus pinch" project has no reference.
- **Dexterous hands and datasets: Allegro Hand, Shadow Hand, DexGraspNet**, Robots & Models: the in-hand node only lists LEAP Hand.
- **LLM-based task planning for manipulation: SayCan, Code as Policies**, Knowledge content: missing from the long-horizon and open-vocabulary nodes (cross-branch with Planning).
- **Learning manipulation from human video / cross-embodiment transfer**, Knowledge node: a strong 2024-2026 RSS/CoRL theme (cross-branch with Robot learning).
- **Isaac Lab / Isaac Sim, Genesis**, Robots & Models: widely used manipulation simulators missing next to MuJoCo, ManiSkill and robosuite (cross-branch with Simulation).

## Low

- **Tool use manipulation**, Knowledge node: a niche but recurring frontier topic.
- **Dynamic manipulation (throwing, catching; TossingBot)**, Knowledge node: high wow factor but rarely accessible.
- **Cooperative multi-arm / multi-robot manipulation**, Knowledge content: a Springer chapter, partly covered by the bimanual node.
- **Manipulation failure detection and recovery evaluation**, Knowledge content: only covered by individual projects.
- **Real-to-sim digital twins for policy evaluation**, Knowledge content (cross-branch with Simulation).
- **Classic grasp planners: GraspIt!, GPD, GG-CNN**, Robots & Models: historical baselines for the grasp-detection node.
- **Arm inverse kinematics solvers (IKPy, TRAC-IK)**, Robots & Models (cross-branch with Kinematics & dynamics).

## Summary

High: 8 · Medium: 10 · Low: 7. A targeted re-run of the researcher on the High items is recommended, especially ACT, SmolVLA, datasets/benchmarks and hand-eye calibration, since they sit directly on the LeRobot/SO-101 wedge.
