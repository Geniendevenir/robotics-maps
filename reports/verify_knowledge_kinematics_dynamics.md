# Verification report: knowledge_kinematics_dynamics.json

Rows checked: 83 (16 knowledge nodes, 19 robots/models, 48 project candidates). Verified: 75. Corrected: 8. Rejected: 0.

## Method
- Opened all 38 distinct source/reference URLs with curl. 35 returned HTTP 200 with matching titles/content.
- Not reachable by curl: MDPI (403), Science Robotics adt1497 (Cloudflare), IEEE DOI 10.1109/lra.2025.3600169 (bot block, also via browser). I opened MDPI in Chrome and it matched. I confirmed the IEEE and Science DOIs through the Crossref API: "Robot Arm Self-Calibration Using RGB-D Camera" (RA-L 2025) and "A review of learning-based dynamics models for robotic manipulation" (Sci. Robot. 2025).
- link.springer.com (Springer Handbook of Robotics, 2016) shows a bot "Client Challenge" page. Crossref confirms the book exists. Every row that cites it also has other sources that load.
- Checked key facts on the pages themselves: builders and maintainers (Pinocchio, Crocoddyl, MuJoCo Warp, BAM, GMR, BeyondMimic, DiffMJX, TOPP-RA, TRAC-IK), the Ruckig 250 µs figure, the Unitree G1 price, IJMERR delta specs, GMR robot list, Menagerie models.
- Checked every select value against schemas/notion-schema.md: all valid. Every project's work split sums to 100. Prerequisite graph is acyclic. No duplicate titles.
- Relations: every knowledge-node name used inside this file resolves. These names point to rows outside this file: "SO-101", "MuJoCo" (Robots & models) and "Assemble & teleoperate an SO-101", "Intro: robot anatomy & coordinate frames in sim", "Intro: drive a servo motor from code", "Autonomous pick-and-place with ACT", "Design a custom SO-101 gripper" (Prerequisites). All of them exist in output/existing_projects.json and/or other branch files, so the syncer must resolve them against Notion.
- Schema cleanup: removed the non-Notion key `_accessibility_reason` from all nodes. No `Used in projects` key was present. Project ideas left empty (deprecated).
- Status: nodes and robots/models are now "To verify". Projects stay "Idea", because the Projects Status field has no "To verify" option.
- Not applicable: Ecosystem Map organizations. The file has none (Built by / Used by / Relevant orgs are all empty).
- Also corrected: the top3 justification for "Dynamic parameter identification", which implied no STS3215 model exists.

## Flags for human review
- All 48 project rows share the same boilerplate Description ("Start in simulation; report success and failure counts ... unreachable targets and limit violations"). It does not fit several projects (e.g. dance retargeting, odometry, delta build). The specific content is in Deliverable. Left unchanged.
- Release year is null for most tools (unknown). Not guessed.
- Projects using a real SO-101 are priced "<€500". Plausible, but I did not verify the kit price.

## Rows

| Table | Row | Verdict | Reason |
|---|---|---|---|
| Knowledge node | Rigid-body motion & coordinate frames | verified | sources load and support the row; select values valid |
| Knowledge node | Robot description formats (URDF / MJCF) | verified | sources load and support the row; select values valid |
| Knowledge node | Forward kinematics (DH & product of exponentials) | verified | sources load and support the row; select values valid |
| Knowledge node | Velocity kinematics, Jacobians & singularities | verified | sources load and support the row; select values valid |
| Knowledge node | Inverse kinematics (analytic & numerical) | verified | sources load and support the row; select values valid |
| Knowledge node | Differential IK & redundancy resolution (QP-based) | verified | sources load and support the row; select values valid |
| Knowledge node | Wheeled mobile robot kinematics | verified | Caltech diff-drive notes and Modern Robotics 13.3.1 load and match |
| Knowledge node | Parallel & closed-chain mechanisms | verified | arXiv 2504.19771 (kinematic loops) and IJMERR delta paper match |
| Knowledge node | Rigid-body dynamics (equations of motion) | verified | sources load and support the row; select values valid |
| Knowledge node | Efficient dynamics algorithms & analytical derivatives | verified | sources load and support the row; select values valid |
| Knowledge node | Trajectory generation & time scaling | verified | sources load and support the row; select values valid |
| Knowledge node | Dynamic parameter identification & actuator models | corrected | Frontier state said BAM covers Dynamixel only; BAM README also lists eRob80 and Feetech STS3215 |
| Knowledge node | Kinematic & hand-eye calibration | verified | DOI 10.1109/LRA.2025.3600169 = "Robot Arm Self-Calibration Using RGB-D Camera" (RA-L, Oct 2025, Crossref); IEEE page bot-blocked |
| Knowledge node | Floating-base & centroidal dynamics (legged/humanoid) | corrected | Crocoddyl maintainers per README are Heriot-Watt RoMI Lab, LAAS Gepetto and Inria Willow (not "University of Edinburgh") |
| Knowledge node | Contact dynamics & differentiable simulation | corrected | removed "2026 pull request adds reverse-mode gradients" (MJWarp README: differentiability not yet available, issue #500); DiffMJX key player "TU Darmstadt" not supported by the arXiv author list, replaced with the author names |
| Knowledge node | Human-to-robot motion retargeting | verified | GMR + BeyondMimic claims confirmed |
| Robot/model | Pinocchio | verified | README: developed by Inria Willow (Paris); RSS14 paper by Carpentier & Mansard (LAAS) |
| Robot/model | Featherstone spatial_v2 | verified | sources load and support the row; select values valid |
| Robot/model | Robotics Toolbox for Python | verified | sources load and support the row; select values valid |
| Robot/model | TRAC-IK | verified | README confirms concurrent KDL-Newton + SQP solvers |
| Robot/model | mink | verified | sources load and support the row; select values valid |
| Robot/model | Pink | verified | sources load and support the row; select values valid |
| Robot/model | Ruckig | verified | 250 µs cycle time confirmed on ruckig.com |
| Robot/model | TOPP-RA | verified | arXiv 1707.07239 title/authors match |
| Robot/model | Crocoddyl | corrected | Builder fixed to RoMI Lab (Heriot-Watt) + LAAS Gepetto + Inria Willow per README |
| Robot/model | MuJoCo Warp | corrected | unverified 2026 PR claim replaced with README statement: differentiability not yet available (issue #500) |
| Robot/model | DiffMJX | corrected | Builder now names the arXiv 2506.14186 authors (Paulus, Geist, Schumacher, Musil, Rappenecker, Martius) |
| Robot/model | MuJoCo Menagerie | verified | repo has unitree_g1, booster_t1, toddlerbot, spot, go2 folders |
| Robot/model | onshape-to-robot | verified | sources load and support the row; select values valid |
| Robot/model | BAM (Better Actuator Models) | corrected | Key specs now list eRob80 and Feetech STS3215 pre-identified models plus MuJoCo Warp support (README) |
| Robot/model | BIRDy | verified | MDPI page (opened via browser) is the survey "Inertial Parameter Identification in Robotics" introducing BIRDy |
| Robot/model | GMR (General Motion Retargeting) | verified | arXiv authors match; README table lists 19 robots incl. G1 and Berkeley Humanoid Lite |
| Robot/model | BeyondMimic | verified | project page authors, LAFAN1 and guided diffusion confirmed |
| Robot/model | Unitree G1 | verified | vendor page shows "Price from $13.5K", G1 and G1 EDU variants |
| Robot/model | Low-cost 3D-printed delta robot (IJMERR 2024) | verified | PDF confirms 3 servos, Arduino Uno, Thingiverse parts, 2.2 mm / 0.4 m/s / 30 picks/min / 200 g |
| Project | Frame-transform quiz app | verified | sources load and support the row; select values valid |
| Project | Camera-to-gripper frame chain on the SO-101 | verified | sources load and support the row; select values valid |
| Project | Quaternion pitfalls benchmark | verified | sources load and support the row; select values valid |
| Project | Write an MJCF for the SO-101 from scratch | verified | sources load and support the row; select values valid |
| Project | CAD-to-sim pipeline for a custom gripper | verified | sources load and support the row; select values valid |
| Project | URDF/MJCF linter for student robots | verified | sources load and support the row; select values valid |
| Project | Forward kinematics three ways | verified | sources load and support the row; select values valid |
| Project | Leader-arm FK pose streamer | verified | sources load and support the row; select values valid |
| Project | FK accuracy check against a camera | verified | sources load and support the row; select values valid |
| Project | Live manipulability ellipsoid | verified | sources load and support the row; select values valid |
| Project | Singularity-aware teleop for the SO-101 | verified | sources load and support the row; select values valid |
| Project | Jacobian-transpose force estimation | verified | sources load and support the row; select values valid |
| Project | Analytic vs numerical IK shoot-out | verified | sources load and support the row; select values valid |
| Project | Click-to-reach SO-101 | verified | sources load and support the row; select values valid |
| Project | IK for 5-DoF arms with orientation trade-offs | verified | sources load and support the row; select values valid |
| Project | Follow a moving target with mink | verified | sources load and support the row; select values valid |
| Project | Phone-pose teleoperation of the SO-101 | verified | sources load and support the row; select values valid |
| Project | Whole-body reach on a simulated humanoid | verified | sources load and support the row; select values valid |
| Project | Diff-drive odometry from scratch | verified | sources load and support the row; select values valid |
| Project | Encoder odometry on a cheap rover | verified | sources load and support the row; select values valid |
| Project | SO-101 on wheels: base + arm kinematics | verified | sources load and support the row; select values valid |
| Project | Delta robot IK/FK in simulation | verified | sources load and support the row; select values valid |
| Project | Build a 3D-printed delta picker | verified | sources load and support the row; select values valid |
| Project | Closed-loop leg linkage in MuJoCo | verified | sources load and support the row; select values valid |
| Project | Gravity compensation torques in sim | verified | sources load and support the row; select values valid |
| Project | Derive and verify a 2-link arm's equations | verified | sources load and support the row; select values valid |
| Project | Gravity-compensated SO-101 'floating arm' | verified | sources load and support the row; select values valid |
| Project | RNEA vs ABA timing notebook | verified | sources load and support the row; select values valid |
| Project | Gradient-based trajectory optimization of a throw | verified | sources load and support the row; select values valid |
| Project | Model-based torque feedforward on the SO-101 | verified | sources load and support the row; select values valid |
| Project | Smooth vs jerky: S-curve demo | verified | sources load and support the row; select values valid |
| Project | Time-optimal SO-101 drawing | verified | sources load and support the row; select values valid |
| Project | Smoothing learned-policy actions | verified | sources load and support the row; select values valid |
| Project | Servo pendulum friction fit | verified | sources load and support the row; select values valid |
| Project | STS3215 actuator model for sim-to-real | corrected | Deliverable claimed STS3215 is "not bundled in BAM", but the BAM README lists Feetech STS3215; reframed as validate/extend, Novelty 4 -> 2 |
| Project | Full inertial identification of the SO-101 | verified | sources load and support the row; select values valid |
| Project | Hand-eye calibration in sim | verified | sources load and support the row; select values valid |
| Project | Calibrate a real SO-101 and camera | verified | sources load and support the row; select values valid |
| Project | Marker-free self-calibration | verified | sources load and support the row; select values valid |
| Project | Centroidal momentum viewer | verified | sources load and support the row; select values valid |
| Project | Humanoid jump with Crocoddyl | verified | sources load and support the row; select values valid |
| Project | Trajectory-optimized motions as RL references | verified | sources load and support the row; select values valid |
| Project | Contact gradient sanity check | verified | sources load and support the row; select values valid |
| Project | System identification via differentiable sim | verified | sources load and support the row; select values valid |
| Project | Gradient-based push policy | verified | sources load and support the row; select values valid |
| Project | Retarget your own dance to a humanoid | verified | sources load and support the row; select values valid |
| Project | Retarget human arm video to the SO-101 | verified | sources load and support the row; select values valid |
| Project | Retargeting-quality study on BeyondMimic | verified | sources load and support the row; select values valid |
