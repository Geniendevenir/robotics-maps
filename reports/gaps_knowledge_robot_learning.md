# Coverage gaps: knowledge_robot_learning.json (Robot learning branch)

Reviewed file: `output/knowledge_robot_learning.json` (16 nodes, 24 robots/models, 48 project candidates), after verification (see `reports/verify_knowledge_robot_learning.md`).

References compared against: CoRL/RSS/ICRA robot-learning topics from 2024-2026 (imitation and diffusion policies, VLAs and their post-training, real-world RL, cross-embodiment, datasets and benchmarks); the topics of the standard robot learning and deep RL courses (Berkeley CS285, Stanford CS224R, CMU 16-831), which cover imitation, DAgger, policy gradients/actor-critic, model-based RL, offline RL, inverse RL and preferences, goal-conditioned and hierarchical RL, exploration and meta-learning; the policies shipped in Hugging Face LeRobot (ACT, Diffusion, VQ-BeT, TD-MPC, pi0/pi0.5/pi0-FAST, SmolVLA, SAC/HIL-SERL); and the LeRobot/SO-101 wedge named in CLAUDE.md.

Scope note: the 8 pilot nodes already in Notion (Imitation learning, RL for robots, VLAs, World models, Teleoperation & data collection, Learning from human video, Robot datasets & benchmarks, Sim-to-real) are excluded on purpose. They are not listed as gaps, but items that should hang off them (rows, projects) are. Models defined in other output files (ACT, SmolVLA, pi0, Diffusion Policy, LeRobot, SO-101, MuJoCo, Isaac Sim / Isaac Lab, Genesis, RSL-RL, Gemini Robotics) were checked across files and are not counted as missing. "(cross-branch)" marks items that mostly belong to another branch. These are well-known items in the field. Their URLs were not re-opened in this pass, so the researcher must source and verify each one before adding a row.

## High

- **Real SO-101 robot-learning projects**, Projects: 46 of 48 candidates are "€0 (sim only)" and only 2 touch hardware. "SO-101" appears once in the whole file. The wedge being tested is "robot learning on low-cost hardware", but the file has no project that records demos on an SO-101 leader/follower, trains ACT/SmolVLA and deploys on the real arm.
- **Real-world online RL on hardware: HIL-SERL / SERL**, Knowledge node + Robots & Models: these are the human-in-the-loop RL methods built into LeRobot for SO-101 (SAC plus reward classifier plus interventions). They are mentioned only once and there is no row. RLPD is the only online-RL reference.
- **RL post-training of VLAs / generalist policies** (e.g. Physical Intelligence pi*0.6 / RECAP, RL fine-tuning of OpenVLA-type policies), Knowledge node (Frontier): this is a major 2025-2026 theme. The "Fine-tuning & adapting" node covers supervised adaptation only, and "RL fine-tuning" has 0 mentions.
- **Large robot-learning datasets as rows: Open X-Embodiment, DROID, BridgeData V2**, Robots & Models: no output file has dataset rows. Cross-embodiment, RT-1-X, CrossFormer and Octo are all trained on them, and the pilot "Robot datasets & benchmarks" node needs them (also flagged in gaps_knowledge_manipulation).
- **Relevant orgs / Built by / Used by are empty on every row**: key robot-learning players are never linked: Hugging Face LeRobot (Paris), Physical Intelligence, Google DeepMind, NVIDIA GEAR, Toyota Research Institute, Stanford/Berkeley/CMU labs, Inria and ISIR. This is for the ecosystem researcher. Rows must not be added from this file.

## Medium

- **Standard RL algorithm libraries: Stable-Baselines3 (PPO, SAC), Gymnasium, skrl**, Robots & Models: the first tools a software student uses for RL. Only RSL-RL exists, in another file.
- **Goal-conditioned & multi-task learning (hindsight relabeling / HER, language-goal relabeling)**, Knowledge node: a core course topic with 0 HER mentions and 1 "goal-conditioned" mention.
- **Inverse RL, adversarial imitation (GAIL) and learning from preferences (RLHF for robots)**, Knowledge content: the reward-learning node covers VLM rewards and Eureka but has 0 mentions of IRL, GAIL or preferences.
- **3D / point-cloud policy representations: 3D Diffusion Policy (DP3), PerAct, RVT-2**, Knowledge node + rows: a strong CoRL/RSS line. The visual-representation node is 2D-only, with 0 point-cloud mentions (cross-branch with Perception).
- **Teacher-student / privileged-information policy distillation**, Knowledge content: the standard sim-to-real learning recipe (legged robots, dexterous hands). Not attached to any node (cross-branch with the Simulation and Sim-to-real pilot).
- **Model-based RL references: TD-MPC2, DreamerV3**, Robots & Models: TD-MPC ships in LeRobot. There are no model-based rows to link to the World models pilot node.
- **Recent LeRobot-native / generalist policies: VQ-BeT, pi0-FAST, pi0.5, X-VLA, OpenVLA-OFT**, Robots & Models: newer policies the team would actually fine-tune. The FAST tokenizer row exists, but no policy built on it.
- **Benchmarks for the offline-RL and VLA nodes: D4RL / Minari, Meta-World, CALVIN, SimplerEnv**, Robots & Models: the offline RL node has no dataset benchmark (D4RL is mentioned once) and only LIBERO/RoboCasa anchor policy evaluation.

## Low

- **Hierarchical RL & skill discovery (options, latent skills)**, Knowledge content: a course topic, but less practical for a 4-6 month lab.
- **Exploration & intrinsic motivation (curiosity, curriculum)**, Knowledge content: 0 curiosity mentions. Inria Flowers is a French reference lab.
- **Safe / constrained RL**, Knowledge content (cross-branch with HRI & safety).
- **Meta-learning / few-shot policy adaptation (MAML-style)**, Knowledge content: partly covered by the fine-tuning node.
- **Residual policy learning (learned corrections on top of a scripted or classical controller)**, Knowledge content: a cheap, high-yield trick on low-cost arms.
- **Data/model scaling laws for robot policies**, Knowledge content: a frontier question that is only implicit.
- **Classic BC baselines: Implicit BC (IBC), Behavior Transformers (BeT)**, Robots & Models: historical baselines next to the diffusion node.
- **Deep-learning ops for robot learning (training compute/GPU budgeting, experiment tracking with W&B/Rerun)**, Knowledge content: the team is strong in AI, so this is low priority. Rerun is in ecosystem_europe_software_ai.
- **Name consistency**: projects relate to "pi0" (defined in knowledge_manipulation), while existing_projects uses "π0 / π0.5". The syncer must merge these so the map does not get two rows.

## Summary

High: 5 · Medium: 8 · Low: 9. The taxonomy covers learning methods well, but it is sim-first: the wedge (SO-101 real-robot learning, HIL-SERL) and VLA RL post-training are the main misses. A targeted researcher re-run on the High items is recommended.
