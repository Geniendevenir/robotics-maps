# Coverage gaps: knowledge_locomotion.json (Locomotion branch)

Reviewed file: `output/knowledge_locomotion.json` (18 nodes, 17 robots/models, 54 project candidates), after verification (see `reports/verify_knowledge_locomotion.md`).

References compared against: the Springer Handbook of Robotics (2nd ed.) TOC, mainly Part B "Design" (Legged Robots, Wheeled Robots, Underwater/Flying/Snake-like Robots in Part E "Field and Service Robotics", Exoskeletons in Part F "Robots and Humans"). The handbook site is bot-blocked from these VMs, so chapter titles come from the reviewer's knowledge of the published TOC, not from an opened page. Also compared: MIT 6.832 Underactuated Robotics and ETH "Robot Dynamics" / Legged Robotics syllabi; ICRA/RSS/CoRL/Humanoids 2024-2026 locomotion topics (RL sim-to-real, teacher-student adaptation, humanoid whole-body tracking, perceptive and agile locomotion); and the low-cost robot-learning wedge from CLAUDE.md.

Scope note: only gaps inside the Locomotion branch, or rows a locomotion map is expected to link to. Items that mainly belong to another branch are marked "(cross-branch)". Item names are well-known in the field, but their URLs were not re-opened in this pass. The researcher must source and verify each one before adding a row. Several Robots & Models rows already exist in other output files (noted as "exists in <file>"); there, the gap is the missing link from locomotion nodes, not a new row.

## High

- **Sim-to-real adaptation methods (domain randomization, teacher-student / privileged learning, RMA, actuator networks)**, Knowledge node (Applied): this is the core recipe behind every learned-locomotion result cited here (ANYmal, Extreme Parkour). It is only implied inside "RL locomotion with sim-to-real", and "Domain randomization" appears just once.
- **Legged state estimation (IMU + leg kinematics fusion, contact detection, base-velocity estimation)**, Knowledge node (Applied, cross-branch with State estimation & SLAM): needed by every real MPC/RL walker. Missing.
- **Low-cost open legged hardware**, Robots & Models: ODRI Solo-8/12 (LAAS-CNRS / MPI open-source quadruped), Upkie (open-source wheel-legged biped, Inria), and ToddlerBot (low-cost open humanoid, 2025) are missing. Open Duck Mini v2 and Berkeley Humanoid Lite exist in knowledge_embedded_electronics.json but are not linked to any locomotion node. This fills the verifier's flag that the branch has no low-cost hardware entry point, which is the wedge hypothesis.
- **Locomotion RL training libraries: rsl_rl, mjlab, Humanoid-Gym / HumanoidVerse**, Robots & Models (Simulator/Tool): these are the standard PPO and training stacks behind Isaac Lab / legged_gym. The verifier notes that BeyondMimic was retired in favour of mjlab, which has no row.
- **Human motion data and tracking for retargeting: AMASS dataset, PHC (Perpetual Humanoid Control), BeyondMimic / GMR retargeting**, Robots & Models: the top-3 node "Humanoid motion imitation & retargeting" has no data source or motion-tracking model row.
- **Exoskeletons and assisted walking**, Knowledge node + robot (Form factor "Exoskeleton"): a Springer chapter and the main Paris locomotion player (Wandercraft Atalante, which exists as an org in ecosystem_paris_all.json). No node or robot exists.
- **Relevant orgs / Built by are empty for every row**: expected locomotion players are never linked. These include Unitree, Boston Dynamics, ANYbotics, ETH RSL, LAAS-CNRS Gepetto (Pinocchio/Crocoddyl/ODRI, Toulouse), Inria, Wandercraft, NVIDIA, Google DeepMind and Agility Robotics. This is for the ecosystem researcher. Rows must not be added from this file.

## Medium

- **Reference humanoids and bipeds: Agility Digit / Cassie, Boston Dynamics Atlas (electric), Booster T1/K1, Fourier GR-1, PAL TALOS, MIT Mini Cheetah**, Robots & Models: these are the platforms most cited papers use. Mini Cheetah is cited through Cheetah-Software but has no row. Booster was dropped as unverified.
- **Trajectory optimization and contact planning for legs (TOWR, contact-implicit TO, Drake)**, Knowledge content/tool: an ETH and MIT syllabus staple that sits between the reduced models and MPC.
- **Footstep and terrain-aware planning (elevation mapping, foothold selection)**, Knowledge node (cross-branch with Planning/Perception): the perceptive node relies on it implicitly.
- **Raibert hopping and heuristic foot-placement controllers**, Knowledge content: a classic beginner-friendly bridge from SLIP to real controllers.
- **Style- and command-conditioned gaits (AMP adversarial motion priors, Walk These Ways)**, Knowledge content/models: a common 2024-2026 student-reproducible RL extension.
- **Locomotion benchmarks and competitions (e.g. humanoid sports/games events, ICRA legged challenges, Isaac Lab locomotion task suite)**, Knowledge content: without them, projects have no external yardstick (cross-branch with ecosystem events).
- **MuJoCo (base engine), Gazebo / ROS 2 Nav2 integration**, Robots & Models: MuJoCo exists in knowledge_manipulation.json and ROS 2 in ecosystem_europe_software_ai.json, but neither is linked to locomotion nodes. Gazebo is missing (cross-branch with Simulation).
- **Actuator modeling for locomotion (quasi-direct-drive, series-elastic, torque/PD gains, motor saturation)**, Knowledge content: only partly covered by "Leg design & proprioceptive actuation" (cross-branch with Mechanisms & actuation).
- **Energy efficiency and cost of transport**, Knowledge content: a standard metric that the gait projects measure without a node to explain it.
- **Fixed-wing / VTOL and aerial agility (drone racing, learned flight control)**, Knowledge content: the aerial coverage stops at multirotor basics.

## Low

- **Snake / serpentine and modular locomotion**, Knowledge node: a Springer chapter, but niche for this lab.
- **Underwater and swimming locomotion**, Knowledge node: a Springer chapter, but out of reach on budget.
- **Tracked and skid-steer vehicles**, Knowledge content: a missing extension of wheeled kinematics.
- **Jumping and hopping robots (Disney/ETH monopods, small jumpers)**, Knowledge content: partly covered by agile/parkour.
- **Soft and bio-inspired crawling locomotion**, Knowledge content: frontier, but rarely accessible.
- **Legged odometry and SLAM on quadrupeds**, Knowledge content (cross-branch with State estimation & SLAM).
- **Multi-robot / swarm locomotion (Crazyswarm)**, Knowledge content: would extend the Crazyflie row.

## Summary

High: 7 · Medium: 10 · Low: 7. The node taxonomy is solid on control theory and frontier RL. The main misses are the practical sim-to-real recipe (adaptation methods, state estimation), the training libraries and motion data behind the top-3 nodes, low-cost open legged hardware, and exoskeletons (Wandercraft). A targeted researcher re-run on the High items is recommended.
