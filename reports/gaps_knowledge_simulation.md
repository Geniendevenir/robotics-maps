# Coverage gaps: knowledge_simulation.json (Simulation branch)

Reviewed file: `output/knowledge_simulation.json` (14 nodes, 14 robots/models/tools, 42 project candidates, top3), after verification (see `reports/verify_knowledge_simulation.md`).

References compared against: the Springer Handbook of Robotics (2nd ed.) TOC (Part A ch. "Robot Simulation" and dynamics/contact chapters; the Handbook site is used for taxonomy only); ICRA/RSS/CoRL 2024-2026 simulation topics (GPU-parallel RL, sim-to-real, real-to-sim twins, world models, benchmarks); course syllabi such as MIT 6.4210/6.8210 (Tedrake, Drake), Berkeley CS285 and ETH "Robot Dynamics"/legged-gym style sim-to-real material; the LeRobot/SO-101 stack named in CLAUDE.md as the working wedge.

Method: full-text keyword checks on the JSON (e.g. 0 mentions of "sim-to-real", "reinforcement", "locomotion", "legged", "PyBullet", "Webots", "robosuite", "LIBERO", "Cosmos", "NeRF", "Menagerie", "tactile", "MoveIt", "ros2_control", "Objaverse"). Scope note: only gaps inside the Simulation branch, or rows a simulation map is expected to link to; items that mostly belong elsewhere are marked "(cross-branch)". The names below are well-known in the field; their URLs were not re-opened in this pass, so the researcher must source and verify each one before adding a row.

## High

- **Sim-to-real transfer as its own node (zero-shot policy transfer, reality gap, teacher-student/privileged distillation)**, Knowledge node: the branch's main purpose for robot learning; the file covers domain randomization and system ID but never names sim-to-real transfer or the teacher-student pipeline (0 mentions).
- **RL training in simulation (PPO on vectorized envs; rsl_rl, Stable-Baselines3, skrl; Gymnasium API)**, Knowledge node + Robots & Models: GPU-parallel envs are covered, but nothing explains how a policy is actually trained on them (0 mentions of reinforcement learning or an RL library).
- **Legged locomotion sim-to-real (Isaac Lab/legged_gym, MuJoCo Playground locomotion, actuator networks)**, Knowledge content: the flagship 2020-2026 sim-to-real success story taught in every course; absent (cross-branch with Locomotion).
- **LeRobot simulation environments (gym-aloha, gym-pusht, gym-hil, MuJoCo SO-100/101 sim envs)**, Robots & Models: the direct simulation entry point to the wedge stack; SO-101 appears only as hardware, with no sim env row.
- **Actuator and motor modeling (servo dynamics, backlash, delay, PD gains; Feetech STS3215 on SO-101)**, Knowledge node: the main reality-gap source for low-cost arms; only touched indirectly by the SO-101 calibration projects.
- **Relevant orgs / Built by are empty for every row**: Google DeepMind (MuJoCo), NVIDIA (Isaac, Warp), Toyota Research Institute (Drake), Open Robotics/Intrinsic (Gazebo), Hugging Face (LeRobot, Paris), Genesis AI, Disney Research appear only as free text. For the ecosystem researcher; rows must not be added from this file.

## Medium

- **NVIDIA Cosmos world foundation models; Google DeepMind Genie 3; 1X world model**, Robots & Models: 2025-2026 reference action-conditioned/video world simulators; the learned-simulator node cites only DreamerV3 and BWM.
- **PyBullet**, Robots & Models: still the most common simulator in tutorials, courses and older benchmarks; absent.
- **Webots and CoppeliaSim**, Robots & Models: classic open/educational simulators used in student competitions; absent.
- **robosuite and LIBERO / Meta-World / RLBench / CALVIN**, Robots & Models: standard simulated manipulation benchmarks next to ManiSkill, SimplerEnv and RoboCasa (cross-branch with Manipulation).
- **MuJoCo Menagerie and robot_descriptions**, Robots & Models: curated robot model libraries (Menagerie includes an SO-ARM100 model); they directly support the asset-format node.
- **3D asset datasets: Objaverse, PartNet-Mobility (SAPIEN)**, Robots & Models: the source of objects for procedural scenes; the procedural node names no asset dataset.
- **NeRF-based real-to-sim** (alongside Gaussian splats), Knowledge content: the digital-twin node only covers Gaussian splatting.
- **ros2_control, MoveIt 2 and Nav2 in simulation**, Knowledge content: the standard way a ROS 2 robot is driven in Gazebo; the ROS 2/Gazebo node only covers the bridge and sensors.
- **Simulation-based CI / software- and hardware-in-the-loop testing**, Knowledge node: industry-standard use of simulation (regression tests, HIL); covered only by individual projects.
- **Tactile sensor simulation (TACTO, Taxim, Isaac TacSL)**, Knowledge content: missing from the sensor simulation node (cross-branch with Manipulation/Perception).
- **Teleoperation and demonstration collection in simulation (sim teleop for imitation data, MimicGen/DexMimicGen data augmentation)**, Knowledge content: a key sim role for imitation learning; absent (cross-branch with Robot learning).

## Low

- **Isaac Gym (legacy) and Brax as standalone rows**, Robots & Models: historically important; Brax is only mentioned in text.
- **Embodied-AI navigation simulators: Habitat, AI2-THOR/ProcTHOR, BEHAVIOR-1K/OmniGibson**, Robots & Models (cross-branch with Navigation).
- **Aerial and driving simulators: CARLA, AirSim, Pegasus/Flightmare**, Robots & Models (cross-branch with Mobile/Aerial).
- **Other physics engines: PhysX, DART, Bullet, RaiSim, Project Chrono**, Robots & Models: engines underneath the listed simulators; useful for the contact-comparison projects.
- **Rendering for synthetic data: Blender/BlenderProc, Kubric, Unreal/Unity robotics**, Robots & Models: Unity is mentioned only in passing.
- **Contact-implicit trajectory optimization using simulators**, Knowledge content (cross-branch with Planning/Control).
- **Visualization and logging tools: MeshCat, Rerun, Foxglove**, Robots & Models: used to inspect sim rollouts; minor.

## Summary

High: 6 · Medium: 11 · Low: 7. The 14 nodes cover simulator internals, formats, sensors, GPU batching, twins and evaluation well, but the branch never explains the end-to-end use case: training a policy in sim (RL/imitation) and transferring it to a real robot. A targeted researcher re-run on the High items is recommended, especially sim-to-real, RL training, actuator modeling and the LeRobot SO-101 sim environments, since they sit directly on the wedge.
