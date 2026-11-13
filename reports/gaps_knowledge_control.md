# Coverage gaps: knowledge_control.json (Control branch)

Reviewed file: `output/knowledge_control.json` (19 nodes, 22 robots/models, 55 project candidates), after verification (see `reports/verify_knowledge_control.md`).

References compared against: the Springer Handbook of Robotics (2nd ed.) TOC: Part A (motion control, force control, redundancy, underactuated) and Part B/E (legged robots, aerial robots, wheeled robots); Modern Robotics ch. 11 and MIT 6.832 Underactuated Robotics (Tedrake); classic control syllabi (Astrom & Murray "Feedback Systems", ETH "Control Systems I/II", MIT 6.302/16.30: state feedback + observers, digital control); ICRA/RSS/CoRL 2024-2026 control topics (legged and humanoid locomotion, MPC, safe control, learning-based control, RL sim-to-real); and the LeRobot/SO-101 low-cost wedge in CLAUDE.md.

Scope note: only gaps inside the Control branch, or rows a control map is expected to link to. Items that mainly belong to another branch are marked "(cross-branch)". Names below are well-known items from the field; their URLs were not re-opened in this pass, so the researcher must source and verify each one before adding a row. Mention counts come from a text search of the file.

## High

- **Legged locomotion control (convex/centroidal MPC, MIT Cheetah-style MPC + WBC)**, Knowledge node (Applied/Frontier): a major ICRA/RSS track and a Springer chapter; the file only touches it via projects (Crocoddyl jump, DIAL-MPC gaits, humanoid push recovery), with 0 mentions of "centroidal" or "convex MPC".
- **Digital control implementation (discretization, sample rate, saturation, anti-windup, fixed-point on microcontrollers)**, Knowledge node (Fundamental): in every control syllabus and the bridge to SO-101 servo and ODrive loops; "anti-windup" appears only inside other text and "discretization" has 0 mentions.
- **State observers and output feedback (Luenberger observer, Kalman filter, LQG / separation principle)**, Knowledge node (Fundamental/Applied): canonical second half of state-space control; 0 mentions of observer, Kalman or LQG. Controllers in the projects assume full state is measured (cross-branch with State estimation & SLAM for the filter itself).
- **Low-cost legged / balancing hardware platform (e.g. ODRI Solo-12 open quadruped from LAAS/MPI, Unitree Go2)**, Robots & Models: legged projects have no real hardware path; ODRI is a European open-source platform directly tied to the Pinocchio/Crocoddyl stack already listed.
- **Relevant orgs / Built by are empty for every row**: expected control players are never linked as organizations, e.g. LAAS-CNRS Gepetto (Pinocchio, Crocoddyl, TSID), Inria (ViSP), Bitcraze (Crazyflie), PX4/Dronecode, ETH Zurich RSL (OCS2), Google DeepMind (MuJoCo, MuJoCo MPC), Toyota Research Institute / MIT (Drake), Franka Robotics. For the ecosystem researcher; rows must not be added from this file.

## Medium

- **Force control and hybrid position/force control**, Knowledge content: a full Springer chapter; only partly covered under the Impedance & admittance node.
- **RL simulators for control: MuJoCo Playground / MJX, Isaac Lab, legged_gym**, Robots & Models: MJX/Playground appear in text (3 mentions) but have no row, yet the learning-based control and RL quadrotor projects depend on them (cross-branch with Simulation / Robot learning).
- **Actuator-level control: BLDC field-oriented control (FOC) and current loops**, Knowledge content: underlies the ODrive and torque-control projects; 0 mentions of FOC (cross-branch with Embedded & electronics).
- **Contact-implicit MPC / hybrid systems control**, Knowledge content: a 2024-2026 frontier for manipulation and locomotion; 0 mentions of contact-implicit.
- **Gain scheduling and iterative learning control (ILC)**, Knowledge content: standard practical techniques for repeated arm motions; 0 mentions.
- **Sliding-mode and H-infinity control**, Knowledge content: named methods of the Nonlinear, robust & adaptive node that are not mentioned by name.
- **Bilateral teleoperation / force-feedback control**, Knowledge content: links control to SO-101 leader-follower data collection (cross-branch with Manipulation).
- **Open flight stacks beyond PX4: ArduPilot, Betaflight**, Robots & Models: the most-used hobby and racing flight controllers; 0 mentions.
- **CVXPY / cvxpygen**, Robots & Models: the easiest Python entry to convex MPC and CBF-QPs for software students; 0 mentions.
- **Low-cost control lab kits (reaction-wheel pendulum, ball-on-plate, Quanser-style setups)**, Robots & Models: the "Build a reaction-wheel inverted pendulum" project has no hardware row.

## Low

- **Koopman operator / linear-embedding control**, Knowledge content: recurring frontier topic in data-driven control.
- **Differentiable simulation for control (Brax, MJX gradients)**, Knowledge content: only mentioned in passing.
- **Input shaping and vibration suppression**, Knowledge content: useful for flexible, cheap arms.
- **Event-triggered and networked control**, Knowledge content: niche for multi-robot and wireless setups.
- **MATLAB/Simulink Control System Toolbox**, Robots & Models: widely taught, but not open source and not the lab's stack.
- **Formation / multi-robot control**, Knowledge content: Crazyswarm-style swarms (cross-branch with Multi-robot).

## Summary

High: 5 · Medium: 10 · Low: 6. A targeted re-run of the researcher on the High items is recommended, especially legged locomotion control, digital control implementation and observers, because they are core syllabus topics and lie on the path from SO-101/ODrive loops to impressive legged demos.
