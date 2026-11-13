# Research: State estimation & SLAM

Research date: **2026-11-13**. Discovery output only; independent verification and coverage criticism remain the coordinator's next stages.

## Deliverables and scope

- `output/knowledge_state_estimation_slam.json`: **16 nodes, 21 Robots & Models rows, 48 project candidates, 3 recommendations, 44 opened source URLs**.
- Nodes: 5 Fundamental, 8 Applied, 3 Frontier. Every node has all writable Knowledge Map fields and the required `_accessibility_reason`; deprecated `Project ideas` is empty.
- Exactly **3 primary-node project candidates per node**: 10 Onboarding, 38 Project. References, filmable deliverables, four complexity axes, work-hour splits, cost bands and prerequisite names are provided for every candidate.
- Reference rows comprise 1 robot, 1 AI model and 19 Simulator/Tool entries. Datasets and papers are resources, not mislabeled robots or AI models.
- Scope is estimating robot/body/camera state and constructing/reusing maps. Motion planning, walking controllers, object pose for manipulation, sensor electronics and arm kinematics remain in their other branches. Secondary branches identify necessary interfaces, not separate research assignments.

Read `devin/playbooks/knowledge-researcher.md`, `CLAUDE.md`, `devin/knowledge.md`, `schemas/notion-schema.md`, `branches.yaml`, both knowledge pilots and `output/existing_projects.json`. No Notion read or write was performed. No PR was opened; the research branch is `research/knowledge-state-estimation-slam`, based on `main`.

## Taxonomy and pedagogical grounding

The Springer Handbook SLAM chapter's author manuscript supplies the Bayes/EKF, particle and graph paradigms and the distinction between estimating a path and mapping the world. The opened copy is an older manuscript, **not evidence of 2026 SOTA**. Modern Robotics 13.4 supplies wheel odometry and drift. Groningen's 2025-26 syllabus supplies spatial-state representation, uncertainty, filtering and graph optimization. Georgia Tech's Fall 2026 syllabus adds invariant EKF, preintegration, calibration, scan registration, data association and continuous-time extensions.

RSS 2025's program puts perception/navigation and multi-robot systems in distinct tracks. Its visual-SLAM workshop explicitly motivates reproducibility and failures beyond average trajectory error. PINGS and certifiable bundle-adjustment papers ground frontier map representations and optimization without confusing an offline reconstruction guarantee with an online SLAM guarantee. OpenLORIS provides an ICRA 2020 multi-session benchmark bridge to lifelong mapping.

| Node | Level | Main reference systems / first useful exercise |
|---|---|---|
| Bayesian state estimation & uncertainty | Fundamental | PythonRobotics; animate a probability belief |
| Wheel & inertial dead reckoning | Fundamental | Modern Robotics, robot_localization; square-loop drift |
| Kalman filtering & multisensor fusion | Fundamental | robot_localization, GTSAM; EKF replay and dropout tests |
| Particle filtering & global localization | Fundamental | PythonRobotics; multimodal corridor belief and kidnapping |
| Factor graphs, smoothing & pose-graph SLAM | Fundamental | GTSAM; anchored small graph and wrong-loop rejection |
| Estimator calibration, timing & observability | Applied | Kalibr, OpenVINS; timing and excitation audit |
| Visual odometry & visual-inertial SLAM | Applied | OpenVINS, ORB-SLAM3; public-sequence replay |
| 2D lidar SLAM & occupancy mapping | Applied | SLAM Toolbox; recorded floor-plan growth |
| 3D lidar-inertial odometry & mapping | Applied | KISS-ICP, FAST-LIO2, LIO-SAM, FAST-LIVO2; comparable replay |
| Place recognition, loop closure & relocalization | Applied | ORB-SLAM3, RTAB-Map, MASt3R; verified revisits |
| Robust, dynamic & lifelong state estimation | Frontier | SLAM Toolbox, RTAB-Map, DynaSLAM historical baseline; changed rooms |
| Dense, semantic & neural SLAM maps | Frontier | SplaTAM, MASt3R-SLAM, ScaRF-SLAM; geometry versus appearance |
| Multi-robot & distributed SLAM | Frontier | Kimera-Multi, GTSAM; independently framed overlapping sessions |
| SLAM benchmarking, consistency & failure analysis | Applied | evo, TUM, LaMAria; alignment-aware scorecards |
| Contact-aided & invariant state estimation | Applied | invariant-ekf, GTSAM; contact/IMU replay and slip |
| GNSS-aided localization & georeferencing | Applied | navsat_transform, LIO-SAM; ENU/heading and dropout tests |

Calibration is scoped to **estimator extrinsics, timing and observability**, not duplicating the embedded pilot's sensor interfacing. Robot/body localization is separate from the manipulation pilot's object-pose node. Contact-aided estimation does not design a gait. GNSS is included so state estimation is not reduced to indoor camera SLAM.

## What is actually current

- **2024:** MASt3R learned reconstruction/matching and SplaTAM Gaussian RGB-D mapping.
- **2025:** FAST-LIVO2 code release (January 23), MASt3R-SLAM, PINGS, LaMAria and CU-Multi; RSS workshop emphasis on failure-aware evaluation.
- **2026:** ScaRF-SLAM's official RA-L repository decouples classical pose tracking from geometric-foundation-model reconstruction. GTSAM's opened documentation includes 2026 legged-estimation material, while its development branch warns about API changes. The November Map2SLAM preprint instead describes persistent revisable state around streaming-model predictions.
- **Not ready to promise:** LIN-SLAM's October 2026 preprint says code will be released upon acceptance. Map2SLAM implementation availability was not checked. Neither is sold here as an already reproducible lab stack or assigned unverified benchmark superiority.

The `Frontier state 2026` fields are evidence snapshots, not exhaustive rankings. Published performance numbers were not copied into procurement or lab-success promises.

## Projects, complexity and practical feasibility

Durations: **7 × 1 week; 20 × 2-4 weeks; 16 × 1-2 months; 5 × 3+ months**. Hardware bands: **42 × €0 (sim only); 1 × <€500; 3 × €500-5k; 2 × €5k+**. The schema lacks an offline-dataset cost option, so `€0 (sim only)` also means public-data replay or analytic simulation on an existing computer; it does **not** mean a CUDA workstation is free. All node starter costs describe their cheapest offline exercise, not a complete physical deployment.

Work splits describe hours, not component prices; each sums to 100. Hardware bands, time, accessibility and wow factors are student-project planning judgments, not source-reported measurements or vendor quotes. Current kit, GPU and complete sensing-rig prices are **unknown**; physical project descriptions require a BOM and quote before purchase. The <€500 camera/IMU rig is a provisional parts ceiling with an existing host computer, not a verified shopping list. The full synchronized lidar rig has a deliberately conservative €5k+ planning band.

Axes span Novelty 1-4, Autonomy 1-3, Hardware 1-4 and Integration 1-5. Estimation pipelines are predominantly scripted; a neural mapping stage does not make a robot open-world autonomous. There are no unsupported Beyond-SOTA or full-custom-robot claims. The high-integration endpoint is a **supervised** repeated-session localization-health deployment, not unsupervised safe navigation.

Example chains (all links are names in the output, not invented Notion IDs):

1. Belief animation → covariance visualization → tiny pose graph → outlier rejection → IMU preintegration → filter-versus-smoother comparison.
2. Wheel-drift simulation → recorded 2D map → serialized-map reuse → supervised room mapping → changed-room testing → localization-health deployment.
3. Evaluation scorecard → public VIO replay → scale comparison → visual-loss tests → held-out city-scale audit.
4. Gaussian reconstruction → prior-driven/classical-tracked dense comparison → instrumented dense-map loop-correction study.

## Verification cautions surfaced during discovery

1. **Licenses:** DynaSLAM's opened license is CC BY-NC 4.0, so `Open source` is false despite public source availability. MASt3R is CC BY-NC-SA and the full MASt3R-SLAM stack is likewise not labeled unrestricted open source. GPL code is open source but carries obligations; model weights and dependencies need separate checks. Kalibr's license has an advertising-acknowledgement condition. RTAB-Map documents optional nonfree-module restrictions.
2. **Build friction:** Kalibr, LIO stacks and Kimera-Multi have older ROS build assumptions; DynaSLAM still documents Python 2.7. No automatic ROS 2 compatibility is inferred from related forks. Use isolated environments and exact revisions.
3. **Incomplete distributed stack:** Kimera-Multi's index README labels Remote Topic Manager as coming soon. Candidates must check module availability first and may use an explicitly labeled minimal GTSAM exchange harness rather than pretend to reproduce the entire system.
4. **Independent evidence:** Odometry is not global loop-corrected SLAM. Monocular scale ambiguity must not be hidden by alignment choices. Contact/IMU alone does not observe absolute position or global yaw. GNSS multipath and bad heading cannot be solved by setting covariance to zero.
5. **Dataset realism:** CU-Multi warns that arbitrary single-trajectory splitting misses realistic inter-agent viewpoint differences. OpenLORIS supplies actual changed-session data; LaMAria uses surveyed control-point annotations and needs its own evaluation protocol, not an assumed dense ground-truth stream.
6. **Safety:** Physical mapping remains supervised. Estimated pose, dropout detection and map-quality metrics are not safety certification. Drone flights and walking-policy deployment are intentionally excluded.

## Search process and scoped saturation

Initial searches covered university syllabi, Handbook/Modern Robotics grounding, current SLAM surveys, ROS tools, learned dense SLAM, distributed mapping, legged estimation and RSS programs. A freshness sweep explicitly searched 2025 benchmarks and 2026 methods, then opened ScaRF-SLAM, Map2SLAM and the 2026 syllabus. This sweep **did** yield substantive additions; it was not treated as a saturation stop.

The stopping criterion was then evaluated on **new nonredundant output-row candidates within this lab-focused taxonomy/reference-system scope**, not on new URLs. A new bibliography page, an alternative example of an already covered concept, or code promised but not released is not automatically a new node/tool/project. The final three consecutive queries were:

| Query | Returned results reviewed | New eligible row candidates | Yield |
|---|---:|---:|---:|
| `robot state estimation SLAM core concepts Bayesian Kalman particle factor graph syllabus` | 8 | 0 | 0% |
| `SLAM open source classical neural mapping visual inertial lidar 2026 overview` | 8 | 0 | 0% |
| `SLAM challenges uncertainty observability data association lifelong multirobot calibration evaluation` | 8 | 0 | 0% |

**Scoped saturation reached:** each was below 10%. The first repeated the existing filtering/graph taxonomy. The second surfaced another neural-LIO preprint (LIN-SLAM), opened and retained as a caveat rather than a runnable-tool row because code is pending. The third added useful OpenLORIS/CU-Multi evidence to existing lifelong/multi-robot nodes rather than exposing a missing node. This is not a claim of exhaustive worldwide algorithm or dataset enumeration; source novelty continues even after a practical taxonomy stops expanding.

Specialized radar/event/underwater estimators, range-only UWB localization, certifiable online solvers and continuous-time implementations are plausible deeper follow-ups. Their sensor physics belong partly in Sensing and their integration can build on the uncertainty/fusion/calibration nodes here; they are not asserted to be comprehensively researched. New neural-system releases and exact procurement/software availability remain verification priorities.

## Local validation

Programmatic checks passed for exact writable key sets; all enum/select values; branch/status consistency; required explanations; boolean and numeric types; empty deprecated field; no auto-managed relations or formulas; per-row sources belonging to the consulted ledger; 100% work splits; valid node/tool/project name relations; tool-node coverage; exactly three projects per node; and an acyclic prerequisite graph.

Normalized-name checks found no node duplicates against either knowledge pilot and no project-name duplicates against the 11 entries in `output/existing_projects.json`. A semantic read also checked that these are localization/mapping exercises rather than renamed arm/servo/robot-learning projects. All research rows remain `To verify`; project candidates remain `Idea`.

**No algorithm stack, hardware demo or proposed project was executed.** These checks validate the research artifact, not algorithm performance. They do not replace the coordinator's independent verifier and coverage-critic passes. Unknown numeric release years are `null` rather than fabricated years, matching the pilot JSON convention.

## Three best accessibility × visual-impact × relevance / cost choices

1. **2D lidar SLAM & occupancy mapping:** the most understandable cheap first win; a growing floor plan and loop correction can be recorded from public data, with a clear ROS 2 continuation path.
2. **Visual odometry & visual-inertial SLAM:** strong software-first learning and broad ecosystem reuse without a robot purchase; build and initialization risk must be budgeted.
3. **Dense, semantic & neural SLAM maps:** highest frontier visual payoff for an AI-oriented team, but behind the first two on predictable cost because GPU access, geometry validity and model licenses matter.

These are qualitative recommendations, not fabricated numerical products of subjective scores. They do not assume the robot-learning/low-cost-arm wedge is the right answer for mobile localization.

## Opened source ledger

The following URLs were actually opened through page retrieval or direct HTTP source reads. They include primary papers, official repositories/docs, university syllabi and conference programs. Multiple URLs can document one project (for example its license and API), so 44 URLs must not be mistaken for 44 independent organizations or systems.

1. https://www.ipb.uni-bonn.de/wp-content/papercite-data/pdf/springerbook-slamchapter.pdf — Springer Handbook SLAM chapter author manuscript; Bayesian, particle and graph taxonomy; foundational, not current SOTA.

2. https://modernrobotics.northwestern.edu/nu-gm-book-resource/13-4-odometry/ — Lynch and Park, Modern Robotics 13.4; wheel integration and accumulated drift.

3. https://ocasys.rug.nl/2025-2026/catalog/course/WMCS040-05 — University of Groningen 2025-26 state-estimation syllabus; uncertainty, filtering and graph SLAM.

4. https://gtsam.org/ — GTSAM documentation; factor graphs, IMU preintegration, 2026 legged-estimation material; version-specific claims are documentation snapshots.

5. https://github.com/borglab/gtsam — Official GTSAM source; Python/C++ interfaces and development-versus-stable warning.

6. https://github.com/AtsushiSakai/PythonRobotics — Educational localization, particle filters, GPS/IMU fusion and SLAM examples.

7. https://github.com/cra-ros-pkg/robot_localization — Official nonlinear state-estimation package repository.

8. https://raw.githubusercontent.com/cra-ros-pkg/robot_localization/ros2/doc/state_estimation_nodes.rst — ROS 2 EKF/UKF documentation; timeouts, covariance and map/odom conventions.

9. https://raw.githubusercontent.com/cra-ros-pkg/robot_localization/ros2/doc/navsat_transform_node.rst — GPS to world-frame odometry, ENU/UTM and heading conventions.

10. https://github.com/ethz-asl/kalibr — Spatial and temporal camera/IMU calibration, rolling shutter; legacy ROS installation constraints.

11. https://docs.openvins.com/ — Filter-based MSCKF visual-inertial estimation and calibration/evaluation features.

12. https://github.com/UZ-SLAMLab/ORB_SLAM3 — Visual, visual-inertial and multi-map SLAM; V1.0 December 2021, EuRoC/TUM-VI examples.

13. https://github.com/SteveMacenski/slam_toolbox — ROS 2 2D graph SLAM, serialized maps, lifelong mapping and localization.

14. https://github.com/introlab/rtabmap — Official RTAB-Map library, releases, installation and ROS distribution support.

15. http://introlab.github.io/rtabmap/ — RGB-D/stereo/lidar graph SLAM and appearance-based loop closure description.

16. https://github.com/PRBonn/kiss-icp — Minimal point-to-point ICP lidar odometry; official ROS 2 support, not full global SLAM.

17. https://github.com/hku-mars/FAST_LIO — Iterated-filter lidar/IMU odometry; FAST-LIO2 update dated July 2021.

18. https://github.com/TixiaoShan/LIO-SAM — Smoothing-based lidar/IMU mapping; GPS factors, two graphs and IMU/data prerequisites.

19. https://github.com/hku-mars/FAST-LIVO2 — Lidar-inertial-visual fusion; code release January 23 2025 and synchronized rig documentation.

20. https://emanual.robotis.com/docs/en/platform/turtlebot3/overview/ — ROBOTIS educational mobile platform; 2025 ROS 2/Gazebo support roadmap, not a price quote.

21. https://github.com/MichaelGrupp/evo — Odometry/SLAM trajectory formats, alignment and error evaluation tooling.

22. https://cvg.cit.tum.de/data/datasets/rgbd-dataset — Official RGB-D data and ground-truth trajectory evaluation workflow.

23. https://github.com/rmurai0610/MASt3R-SLAM — CVPR 2025 dense monocular SLAM; reconstruction prior, CUDA and checkpoint dependencies.

24. https://github.com/naver/mast3r — ECCV 2024 learned matching/reconstruction prior; explicitly noncommercial CC BY-NC-SA code.

25. https://github.com/spla-tam/SplaTAM — CVPR 2024 RGB-D Gaussian-splatting SLAM; GPU software environment and evaluation.

26. https://github.com/MIT-SPARK/Kimera-Multi — Distributed robust metric-semantic SLAM; peer-to-peer constraints and legacy ROS dependencies.

27. https://lamaria.ethz.ch/ — ICCV 2025 city-scale egocentric VIO/SLAM benchmark; long trajectories, dynamic content and calibration drift.

28. https://github.com/BertaBescos/DynaSLAM — 2018 dynamic-scene SLAM baseline; Mask R-CNN and legacy Python 2 dependencies, not a new SOTA claim.

29. https://github.com/RossHartley/invariant-ekf — Contact/landmark-aided invariant filter implementation and kinematic example.

30. https://www.roboticsproceedings.org/rss14/p50.html — RSS 2018 contact-aided InEKF; unobservable global position/yaw and Cassie evaluation.

31. https://roboticsconference.org/2025/program/overview/ — RSS 2025 tracks include perception/navigation and multi-robot systems.

32. https://vslam-lab.github.io/Unifying-VSLAM-RSS25/ — RSS 2025 workshop: standardized evaluation and failures beyond ATE.

33. https://www.roboticsproceedings.org/rss21/p040.html — RSS 2025 PINGS: neural distance/radiance maps for lidar-visual SLAM.

34. https://www.roboticsproceedings.org/rss21/p032.html — RSS 2025 Building Rome with Convex Optimization; certifiable scaled bundle adjustment, not a full online SLAM product.

35. https://github.com/ori-drs/ScaRF-SLAM — RA-L 2026 official Oxford/Georgia Tech implementation: classical tracking decoupled from foundation-model reconstruction; GPLv3 code, dependency terms separate.

36. https://arxiv.org/abs/2611.11169 — November 2026 Map2SLAM preprint: persistent revisable SLAM state around streaming predictions. Author-reported results, not independently reproduced; code access not checked.

37. https://syllabus.gatech.edu/sites/default/files/2026-04/Fall-2026-AE-8803-Gan-Advanced-Mobile-Robotics-Syllabus.pdf — Georgia Tech Fall 2026 mobile robotics syllabus; filtering, invariant EKF, graphs, preintegration, data association and continuous-time SLAM.

38. https://raw.githubusercontent.com/AtsushiSakai/PythonRobotics/master/LICENSE — MIT license verified directly.

39. https://raw.githubusercontent.com/ethz-asl/kalibr/master/LICENSE — BSD-style license including advertising acknowledgement condition; verify requirements before reuse.

40. https://raw.githubusercontent.com/BertaBescos/DynaSLAM/master/LICENSE.txt — CC BY-NC 4.0: publicly available research code is not unrestricted open source.

41. https://arxiv.org/html/2610.21199 — October 2026 LIN-SLAM preprint. Code promised upon acceptance; not included as a runnable reference-system row.

42. https://raw.githubusercontent.com/MIT-SPARK/Kimera-Multi/main/kimera_multi.repos — Official component manifest: multiple repositories and pinned/legacy dependencies; inspect component licenses separately.

43. https://lifelong-robotic-vision.github.io/dataset/scene — Official OpenLORIS-Scene ICRA 2020 multi-session benchmark; visual/inertial/wheel/laser data and reference trajectory caveats.

44. https://arxiv.org/html/2505.17576v2 — CU-Multi 2025 authors paper: overlap-controlled multi-run data association evaluation; splitting a single trajectory does not recreate true multi-view observations.
