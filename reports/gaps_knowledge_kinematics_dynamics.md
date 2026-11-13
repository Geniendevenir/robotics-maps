# Coverage gaps: knowledge_kinematics_dynamics.json (Kinematics & dynamics branch)

Reviewed file: `output/knowledge_kinematics_dynamics.json` (16 nodes, 19 robots/models, 48 project candidates), after verification (see `reports/verify_knowledge_kinematics_dynamics.md`).

References compared against: the Springer Handbook of Robotics (2nd ed.) TOC, Part A "Robotics Foundations" (kinematics, dynamics, mechanisms & actuation, model identification, motion planning, motion control) and Part B "Design" (performance evaluation and design criteria, limbs, parallel mechanisms, flexible robots); Lynch & Park "Modern Robotics" chapters 2-13 (incl. ch. 5 velocity kinematics & statics, ch. 8 dynamics, ch. 13 wheeled robots); Stanford CS223A and MIT 6.832 Underactuated Robotics syllabi; ICRA/RSS/CoRL 2024-2026 kinematics/dynamics topics (GPU-parallel IK, differentiable simulation, retargeting); and the LeRobot/SO-101 stack named in CLAUDE.md as the working wedge.

Scope note: only gaps inside the Kinematics & dynamics branch, or rows this map is expected to link to. Items that mainly belong to another branch are marked "(cross-branch)". Except where noted, URLs for the items below were not re-opened in this pass; the researcher must source and verify each one before adding a row.

## High

- **Statics: wrenches, Jacobian-transpose force/torque mapping**, Knowledge node (Fundamental): Modern Robotics ch. 5 and CS223A core topic; zero mentions of "wrench"/"statics", yet the project "Jacobian-transpose force estimation" depends on it.
- **Actuators & transmissions (gear ratio, reflected inertia, backlash, compliance, quasi-direct-drive vs series-elastic)**, Knowledge node: a Springer Part A chapter and the key mechanics gap for a software-strong team on cheap geared servos; only friction is covered by the identification node.
- **placo (Rhoban, Pinocchio-based QP IK/whole-body solver)**, Robots & Models: LeRobot's own kinematics module imports placo for SO-101 end-effector control (checked in huggingface/lerobot `src/lerobot/model/kinematics.py` and `pyproject.toml`); missing although it sits directly on the wedge and is French.
- **Drake (MIT/TRI multibody dynamics toolbox)**, Robots & Models: the reference toolbox of MIT Underactuated/Manipulation courses for dynamics, trajectory optimization and contact; only one passing mention.
- **Relevant orgs / Built by / Used by empty for every row**: expected players are never linked as Ecosystem organizations: Inria Willow (Paris, Pinocchio), LAAS-CNRS Gepetto (Toulouse, Pinocchio/Crocoddyl), Rhoban/LaBRI (Bordeaux, BAM/placo/onshape-to-robot), Hugging Face LeRobot, Google DeepMind (MuJoCo), Unitree. This is for the ecosystem researcher; rows must not be added from this file.

## Medium

- **Simple underactuated systems (pendulum, cart-pole, acrobot) as dynamics teaching models**, Knowledge content: MIT Underactuated staple; a cheap first dynamics demo (cross-branch with Control).
- **Workspace analysis & kinematic design (reachability, dexterity, link-length choice)**, Knowledge node: Springer Part B chapter; needed for the custom gripper and delta-build projects.
- **Omnidirectional (mecanum/omni) and car-like (Ackermann) kinematics**, Knowledge content: wheeled node and projects focus on differential drive only (LeKiwi uses omni wheels).
- **MuJoCo MJX (JAX)**, Robots & Models: mentioned 5 times in text but has no row, unlike MuJoCo Warp.
- **GPU-parallel IK / kinematics: cuRobo (NVIDIA), PyRoki (Berkeley, 2025)**, Robots & Models: 2024-2026 frontier for batched IK used in retargeting and data generation (cross-branch with Planning).
- **Reduced-order legged models (LIPM, ZMP, SLIP)**, Knowledge content: missing from the floating-base/centroidal node (cross-branch with Locomotion).
- **Operational-space / task-space dynamics (Khatib)**, Knowledge content: the bridge from dynamics to force/impedance control; absent (cross-branch with Control).
- **ROS 2 tf2 / robot_state_publisher**, Robots & Models: the standard frame-tree tooling a student will meet first; no ROS mention at all.
- **Collision geometry & distance libraries (Coal/hpp-fcl, used by Pinocchio)**, Robots & Models: needed for collision-aware IK limits mentioned in the mink node.

## Low

- **Soft, flexible and continuum robot kinematics**, Knowledge node: Springer chapter; niche for this team.
- **Aerial robot (quadrotor) dynamics**, Knowledge content (cross-branch, likely out of the team's scope).
- **Classic IK libraries: KDL/Orocos, IKFast, IKPy**, Robots & Models: KDL only mentioned via TRAC-IK; IKFast/IKPy absent.
- **Visualization tools (Meshcat, Rerun, viser)**, Robots & Models: useful for the frame-quiz and manipulability-ellipsoid projects.
- **Isaac Sim/Lab, Genesis, PyBullet**, Robots & Models (cross-branch with Simulation).
- **Classic textbooks as resources (Craig; Siciliano et al.; Spong)**: Best resources lean on Modern Robotics, Corke and CS223A only.
- **Other low-cost arms/bases as kinematic targets (Koch v1.1, LeKiwi)**, Robots & Models (cross-branch with Manipulation; already flagged there).

## Summary

High: 5 · Medium: 9 · Low: 7. Core theory (frames, FK/IK, Jacobians, dynamics algorithms, trajectories, identification, retargeting) is well covered. A targeted researcher re-run on the High items is recommended, especially statics, actuators/transmissions and placo, since they sit directly on the SO-101/LeRobot wedge.
