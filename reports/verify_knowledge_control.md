# Verification report: knowledge_control.json

Rows checked: 96 (19 knowledge nodes, 22 robots/models, 55 project candidates). Verified: 92. Corrected: 4. Rejected: 0.

## Method
- Opened all 72 distinct source/reference URLs in nodes, robots/models and projects: all 72 returned HTTP 200 and the page titles match the cited work (arXiv papers, GitHub repos, official docs, product pages).
- Checked key claims on the pages: DIAL-MPC "ICRA 2025, Best Paper Finalist" (repo README); Crazyflie 2.1+ 29 g, 7 min flight, 15 g payload; Crazyflie firmware lists Mellinger, INDI, Brescianini and Lee controllers; Learning to Fly in Seconds: Sim2Real after 18 s of training on a laptop, tested on a real Crazyflie; Franka Research 3 3 kg payload, 855 mm reach; CoRE-MPC (arXiv 2610.19250) and A-SLS (arXiv 2610.20925) names; RSS 2025 accepted papers include AMO; arXiv 2501.01432 submitted Dec 2024 ("2024 survey" correct); do-mpc docs v5.1.2.
- Licences checked on GitHub: python-control BSD-3, Hydrax MIT, OSQP Apache-2.0, ProxSuite BSD-2, Pinocchio BSD-2, TSID BSD-2, Crocoddyl BSD-3, OCS2 BSD-3, MuJoCo MPC Apache-2.0, PX4 BSD-3, CasADi LGPL-3.0, ros2_controllers Apache-2.0, Ruckig MIT, libfranka Apache-2.0, ViSP GPL-2.0. All match the file. Repos checked via the API are active (pushed in 2026).
- Validated every select value against schemas/notion-schema.md: all valid. All project work splits sum to 100. Prerequisite names all resolve and the chains are acyclic. Knowledge-node relations all resolve within the file.
- Status: nodes and robots/models are now "To verify". Projects stay "Idea", because the Projects Status field has no "To verify" option.
- Schema cleanup: removed the non-Notion key `_accessibility_reason` from all 19 nodes. No `Used in projects` key is present. Release year is a number or null.
- Not checked: Ecosystem Map organizations. This file has none (Built by / Used by / Relevant orgs are empty; builders are in `Builder (if not in map)`).

## Flags for human review
- Several project "Robots & models" values point at rows defined in other files, not this one: `SO-101` and `MuJoCo` (knowledge_manipulation.json), and `ODrive S1 / Pro` and `ros2_control` (knowledge_embedded_electronics.json). The syncer has to resolve them across files. Note that knowledge_embedded_electronics.json names the arm `SO-101 arm` while manipulation uses `SO-101`. Dedupe these before syncing.
- Franka Research 3 and Crazyflie 2.1+: the price is unknown on the opened pages (left as written).

## Row results
### Knowledge nodes (19)
- Corrected: Underactuated & balancing control. Safe-Ballbot (arXiv 2611.03307) is validated only in MuJoCo simulation, not on "real ballbots". Text fixed.
- Corrected: Safety filters & control barrier functions. Same Safe-Ballbot fix ("on real robots" became "validated in MuJoCo simulation").
- Verified (17): Feedback control & PID; Dynamic system modeling & state-space; Stability & frequency-domain analysis; Trajectory generation & motion profiles; Joint-space control of robot arms; System identification & controller tuning; Optimal control & LQR; Model predictive control (MPC); Trajectory optimization; Impedance & admittance control; Task-space & whole-body control; Mobile robot path-tracking control; Multirotor flight control; Visual servoing; Nonlinear, robust & adaptive control; Sampling-based & GPU-parallel MPC; Learning-based & data-driven control. Sources load and support the claims, and select values are valid.

### Robots & models (22)
- Corrected: safe-control-gym. Licence filled in as MIT (from the repo), replacing "licence not checked".
- Corrected: DIAL-MPC. Licence filled in as Apache-2.0 (from the repo), replacing "licence not checked".
- Verified (20): Python Control Systems Library; ros2_controllers; Ruckig; CasADi; acados; do-mpc; OSQP; ProxSuite; Pinocchio; TSID; Crocoddyl; OCS2; Drake; MuJoCo MPC; Hydrax; PX4 Autopilot; Crazyflie 2.1+; ViSP; Nav2 controller plugins (Regulated Pure Pursuit, MPPI); Franka Research 3. Each exists, the builder matches the official repo or site, and the specs match the opened pages.

### Project candidates (55: 15 Onboarding, 40 Project)
- Verified (55): all select values are valid, work splits sum to 100, Prerequisites resolve with no cycles, Knowledge nodes resolve, and all References URLs load. Status stays "Idea".
