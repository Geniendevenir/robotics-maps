# Control discovery research

## Scope
Discovery only for the **Control** branch: 19 knowledge nodes (5 Fundamental, 11 Applied, 3 Frontier), 22 new Robots & Models rows (2 robots, 20 tools), 55 project candidates (15 Onboarding, 40 Project; 2-3 per node). Rows are `Draft` (nodes, robots/models) and `Idea` (projects). Notion was not read or written. The `Used in projects` reverse relation and formula fields (Level, Mix check) are not emitted. `_accessibility_reason` is a non-synced helper key.

Boundaries with other branches:
- **Manipulation** (pilot) owns contact-rich manipulation tasks. Here, *Impedance & admittance control* covers only the control law (virtual spring/damper, admittance on position robots). No pilot node or project is duplicated; the pilot's "Simulate a virtual spring" and "Insert a peg with compliance" are not repeated.
- **Embedded & electronics** (pilot) owns FOC/motor drivers, RTOS timing and ros2_control hardware interfaces. Control nodes stay at the algorithm level. `ros2_controllers` (the controller library) is a separate row from the pilot's `ros2_control` (the framework).
- **Robot learning / Locomotion / Planning**: only the control-specific side is covered (residual RL, learned dynamics, sampling MPC, path tracking). General policy learning, gaits and global planning are left to those branches.
- No project in `output/existing_projects.json` is duplicated. "Close the sim-to-real gap of the SO-101 simulator" is system identification of the simulator. It complements the existing "Sim-to-real transfer on the SO-101" policy project and is not a copy of it.

## Taxonomy grounding
- Modern Robotics ch. 11 "Robot Control" (Lynch & Park), opened at modernrobotics.northwestern.edu plus Coursera Course 4 syllabus: error dynamics, PID/feedforward, computed torque, force/hybrid/impedance control.
- Murray, Li & Sastry *A Mathematical Introduction to Robotic Manipulation* (full PDF, Caltech): joint/computed-torque, nonlinear control.
- Åström & Murray *Feedback Systems* 2e (FBSwiki): PID, state space, frequency domain, LQR.
- MIT 6.832 Underactuated Robotics (Tedrake 2024 notes + OCW): LQR, Lyapunov, trajectory optimization, cart-pole/acrobot/quadrotor.
- ETH Zurich Robot Dynamics lecture (model and control of arms, legged, rotary-wing systems).
- IEEE RAS Technical Committee on Robot Control page; RSS 2025 accepted-paper list (keyword counts in titles: "Whole-Body" 15, "MPC" 9, "Model Predictive" 6, "Safety Filter" 6, "Quadrotor" 6, "Barrier" 3). Those counts were used to confirm the frontier nodes.
- **Springer Handbook of Robotics** (link.springer.com, 2nd ed. book page and the Motion Control / Force Control chapters): every request returned a bot "Client Challenge" page, so it was **not opened**. It is not cited as a row source.
- ICRA session tracks: ieee-icra.org now shows ICRA 2027 (Seoul, May 24-28, 2027) without a track list, so ICRA tracks were not used. DIAL-MPC's ICRA 2025 best-paper-finalist status is taken from its GitHub README only.

## Queries actually run
Searches used the arXiv API (sorted by submission date), because web-search engines returned no usable results from this VM. Docs, product pages and repositories were opened directly by URL. 74 distinct URLs were retrieved with content (full list in `sources_consulted`).

Discovery and saturation queries (arXiv `search_query`):

| # | Query | Results | New nodes |
|---|---|---:|---:|
| 1 | `all:"robot control" AND all:survey AND cat:cs.RO` | 10 | 1 (safety filters, from the 2024 survey on safe robot control via learning) |
| 2 | `abs:"model predictive control" AND abs:robot AND abs:real-time` | 10 | 1 (robust/adaptive MPC: merged into *Nonlinear, robust & adaptive control*) |
| 3 | `abs:"control barrier function" AND abs:robot` | 10 | 0 |
| 4 | `abs:"impedance control" AND abs:learning` | 10 | 0 |
| 5 | `abs:"whole-body control" AND abs:humanoid AND abs:optimization` | 10 | 0 |
| 6 | `abs:"visual servoing" AND cat:cs.RO` | 10 | 1 (*Visual servoing* added) |
| 7 | `abs:"system identification" AND abs:robot AND abs:dynamics` | 10 | 0 (fits *System identification*) |
| 8 | `abs:quadrotor AND abs:control AND abs:agile` | 10 | 0 (fits *Multirotor flight control*) |
| 9 | `abs:"path tracking" AND abs:"mobile robot" AND abs:controller` | 10 | 0 (fits *Mobile robot path-tracking*) |
| 10 | `abs:"trajectory optimization" AND abs:robot AND abs:contact` | 10 | 0 (fits *Trajectory optimization*; contact-implicit work is a sub-topic) |
| 11 | `abs:"reinforcement learning" AND abs:"low-level control" AND abs:robot` | 10 | 0 (fits *Learning-based & data-driven control*; humanoid gaits are Locomotion) |

**Saturation stop**: queries 7-11 gave 0 new nodes out of 19 (0% < 10%), five in a row (at least 3 required). Some results belong to other branches (ultrasound imaging, crop-row segmentation, movement primitives, which are Robot learning) and were not turned into Control nodes. This is taxonomy saturation, not a claim that the literature list is complete.

Opened 2024-2026 primary sources used for "Frontier state 2026": arXiv 2501.01432 (safe robot control via learning survey, Dec 2024), 2409.15610 (DIAL-MPC), 2510.05443 (AD-NODE), 2601.02379 (movement primitives survey), 2606.25212 (RigPI), 2609.28312 (VGM-VS), 2609.30842 (Impedance Cloning), 2610.08695 (NMPP), 2610.19250 (CoRE-MPC), 2610.20925 (A-SLS), 2611.03307 (Safe-Ballbot), 2611.04204 (humanoid iLQR-MPC + WBC). The 2026 items are preprints. Their claims are what the authors report, not independent validation.

Failed retrievals (not counted): databook.uw.edu (DNS), docs.nav2.org controller pages (404, replaced by the navigation2 GitHub package pages), frankaemika.github.io/docs/libfranka.html and frankarobotics.github.io/docs/libfranka.html (404, replaced by the FCI docs index and the libfranka repo), mathworks.com (403), robotics.stanford.edu/~khatib (404). Two arXiv IDs I guessed during exploration (2202.11188, 2404.10566) were unrelated papers. They are not cited anywhere and were removed from the source list.

## Top 3 (accessibility x visual impact x ecosystem relevance / cost, qualitative)
1. **Feedback control & PID**: accessibility 5, €0 in sim, and it directly improves the SO-101/LeRobot stack. Every other node builds on it.
2. **Sampling-based & GPU-parallel MPC**: training-free humanoid/quadruped behaviours (MuJoCo MPC, Hydrax, DIAL-MPC) make filmable demos and fit JAX/GPU skills, with zero hardware.
3. **Multirotor flight control**: the 29 g open-source Crazyflie lets students write real flight controllers safely indoors (high wow). It needs hardware plus a positioning deck. The price is unknown.

## Unknowns and representation decisions
- Prices: Crazyflie 2.1+ and Franka Research 3 prices were not on the opened pages, so they are written as "unknown". The €5k+ band for FR3 is an inference.
- Release year is filled only where an opened source gives it (MuJoCo MPC 2022, DIAL-MPC 2024). Everywhere else it is `null`.
- Licences: these were stated on the opened pages: python-control BSD-3, ros2_controllers Apache-2.0, Ruckig MIT (community), CasADi LGPL, OSQP Apache-2.0, ProxSuite/Pinocchio/TSID/Crocoddyl BSD, OCS2 BSD-3, MuJoCo MPC Apache-2.0, Hydrax MIT, PX4 BSD-3, ViSP GPL, libfranka Apache-2.0. For acados, do-mpc, Drake, DIAL-MPC and safe-control-gym the code is public but the licence terms were not checked. "Open source" = true means the code is publicly available, not a commercial-use clearance.
- `Built by`, `Used by` and `Relevant orgs` are empty because there are no ecosystem rows to resolve. Attribution is in `Builder (if not in map)`.
- **Relations to pilot rows**: projects reference 4 Robots & Models rows that are already defined in the pilot files and are **not re-created here**: `MuJoCo`, `SO-101` (knowledge_manipulation.json), `ODrive S1 / Pro` and `ros2_control` (knowledge_embedded_electronics.json). The syncer should resolve them to those rows and add the Control knowledge nodes to them if wanted. Every other relation resolves inside this file. Project prerequisites resolve locally and are acyclic, with no cross-file prerequisites.
- SO-101 servo-level claims: LeRobot docs confirm calibration and position control. Using current/load readings or a lowered servo gain to approximate compliance is a hypothesis that the projects must test.
- Durations, cost bands, wow ratings and work splits are planning estimates.

## Coverage gaps for a critic
Hybrid force/position control is only covered inside the impedance node text. Iterative learning control, Kalman-filter-based observers (State estimation branch), and passivity/teleoperation-with-time-delay control (an HRI/teleop overlap) have no nodes. Koopman/linear-embedding control and differentiable-simulation control are mentioned only implicitly.
