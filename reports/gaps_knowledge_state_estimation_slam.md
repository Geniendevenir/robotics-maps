# Coverage gaps: knowledge_state_estimation_slam.json (State estimation & SLAM branch)

Reviewed file: `output/knowledge_state_estimation_slam.json` (16 nodes, 21 robots/models, 48 project candidates), after verification (see `reports/verify_knowledge_state_estimation_slam.md`).

References compared against: the Springer Handbook of Robotics (2nd ed.) TOC, specifically Part E "Moving in the Environment" (Ch. 46 SLAM, plus the chapters on multisensor data fusion and visual odometry/localization in Parts C/E); Thrun, Burgard & Fox "Probabilistic Robotics"; Barfoot "State Estimation for Robotics"; Stachniss's Bonn SLAM/Mobile Sensing courses and the Cyrill Stachniss / Davide Scaramuzza VO/SLAM tutorials; ICRA/IROS/RSS 2024-2026 localization, SLAM and sensor-fusion tracks (learned VO, Gaussian/neural SLAM, feed-forward 3D foundation models, event/radar sensing, certifiable estimation); the ROS 2 Nav2 localization stack; and the LeRobot/SO-101 wedge in CLAUDE.md.

Method: keyword scan of the full file (all fields) for each expected item, then reading node names, Key players, robots/models and project candidates. Counts below are mentions found in the file. Scope note: only gaps inside this branch or rows a SLAM map should link to; "(cross-branch)" marks items that mainly belong elsewhere. Item URLs were not re-opened in this pass; the researcher must source and verify each one before adding a row.

## High

- **Ecosystem links are empty everywhere**: `Built by` and `Used by` are `[]` for all 21 Robots & Models rows and `Relevant orgs` is `[]` for all 48 projects. Expected players (ETH Zurich ASL/RSL, TUM CVG, University of Bonn PRBonn, HKU MARS, MIT SPARK, Borglab/Georgia Tech, University of Zaragoza, NAVER LABS Europe (Grenoble), and French labs: Inria, LAAS-CNRS, Mines Paris CAOR, ONERA) are named only as free text. For the ecosystem researcher; rows must not be added from this file.
- **Nav2 AMCL (Monte Carlo localization in ROS 2)**, Robots & Models: the default particle-filter localizer on every ROS mobile robot (0 mentions of AMCL/Nav2). The "Particle filtering & global localization" node has no deployable implementation row, only PythonRobotics.
- **Google Cartographer**, Robots & Models: the canonical open-source 2D/3D lidar graph SLAM (0 mentions); the 2D lidar node only lists SLAM Toolbox and RTAB-Map.
- **Low-cost SLAM sensors as rows: 2D lidar (Slamtec RPLIDAR / LDROBOT LD19), RGB-D/stereo-IMU cameras (Intel RealSense D435i, Luxonis OAK-D, Stereolabs ZED), Livox Mid-360**, Robots & Models: projects ask for "a rigid timestamped camera-IMU rig" and "a supervised mobile base" but there are no sensor rows with prices (RealSense/RPLIDAR/Livox: 0 mentions; ZED only in text). Critical for a team weak in hardware.
- **Standard benchmark datasets: EuRoC MAV, KITTI odometry, TUM RGB-D, Newer College / Hilti SLAM Challenge**, Robots & Models: each appears at most once in text (Newer College/Hilti 0), yet many projects are offline "replay a public trajectory" exercises and the benchmarking node needs them.
- **IMU attitude estimation (complementary / Madgwick / Mahony filters, AHRS) and the error-state Kalman filter (ESKF)**, Knowledge content (Fundamental): the first estimator most beginners build on a cheap IMU, and the ESKF is the form used by most VIO/LIO systems. 0 mentions of AHRS, complementary filter, Madgwick, error-state or ESKF.
- **Learned visual odometry / SLAM: DROID-SLAM, DPVO (Princeton)**, Robots & Models + Frontier state: the reference deep VO/SLAM baselines at ICRA/CVPR 2022-2026 (0 mentions). The frontier nodes jump from DynaSLAM to Gaussian and MASt3R systems without them.

## Medium

- **VINS-Mono / VINS-Fusion (HKUST)**, Robots & Models: the most-cited open optimization-based VIO; only OpenVINS (filter) and ORB-SLAM3 represent VIO.
- **Feed-forward 3D foundation models: DUSt3R, VGGT (CVPR 2025) and their SLAM uses**, Frontier content: MASt3R is present but its parent DUSt3R and VGGT are not (0 mentions) (cross-branch with Perception).
- **NVIDIA Isaac ROS cuVSLAM and nvblox**, Robots & Models: GPU VSLAM + mapping widely used on Jetson robots in 2024-2026 (0 mentions).
- **Volumetric mapping for navigation: OctoMap, Voxblox/nvblox, ESDF**, Knowledge content: how SLAM maps become planning maps; 0 mentions (cross-branch with Planning/Perception).
- **Nonlinear least-squares back-ends: Ceres Solver, g2o, iSAM2**, Robots & Models: only GTSAM is listed; ORB-SLAM3/VINS use g2o/Ceres (0 mentions).
- **Lie-group tooling for estimation (Solà "micro Lie theory", manif, Sophus)**, Best resources / Robots & Models: Lie groups are mentioned in text but no beginner reference or library row.
- **Visual localization against a prior map (hloc, SuperPoint + LightGlue, NetVLAD; NAVER Kapture)**, Robots & Models: the place-recognition node has no learned-feature rows (SuperPoint/LightGlue/NetVLAD: 0 mentions).
- **Robust / certifiable estimation (graduated non-convexity, TEASER++, robust kernels)**, Knowledge content: a strong RSS/T-RO theme from MIT SPARK; only the toy "malicious loop constraint" project touches it.
- **Ground truth for experiments: AprilTag fiducials and motion capture (OptiTrack/Vicon)**, Knowledge content: needed for any honest real-world evaluation project (0 mentions).
- **Gaussian/neural SLAM breadth: MonoGS, Photo-SLAM, NeRF-based NICE-SLAM**, Robots & Models: only SplaTAM represents the family.
- **Drone state estimation: PX4 EKF2 / ArduPilot EKF3**, Robots & Models: the most deployed open multi-sensor EKF in robotics (0 mentions) (cross-branch with Aerial).
- **Canonical textbooks and courses as Best resources: Probabilistic Robotics, Barfoot's State Estimation for Robotics, Stachniss SLAM course, Scaramuzza VO tutorial**: 0 mentions; current resources lean on PythonRobotics and the Groningen course.
- **Link to the LeRobot/SO-101 wedge (e.g. LeKiwi mobile base, camera calibration/hand-eye for SO-101)**: 0 mentions of LeRobot, SO-101 or LeKiwi; no project tests whether SLAM skills feed the robot-learning hypothesis (cross-branch with Manipulation/Robot learning).

## Low

- **Event cameras and radar/thermal odometry**, Frontier content: niche but recurring ICRA/RSS workshop topics (0 mentions).
- **UWB ranging and radio-based localization**, Knowledge content: cheap indoor positioning alternative (0 mentions).
- **Historical direct/semi-direct VO: LSD-SLAM, DSO, SVO**, Robots & Models: useful context, not needed for projects.
- **Other VIO systems: Basalt, OKVIS, ROVIO, MSCKF origin (Mourikis & Roumeliotis)**, Robots & Models: MSCKF mentioned once only.
- **Classic 2D lidar SLAM: GMapping, Hector SLAM**, Robots & Models: historical baselines still seen in tutorials.
- **Lidar place recognition: Scan Context**, Robots & Models: standard lidar loop-closure descriptor (0 mentions).
- **stella_vslam (OpenVSLAM fork)**, Robots & Models: alternative open monocular/stereo SLAM.
- **Classic scan registration variants (NDT, GICP)**, Knowledge content: ICP is covered; NDT 0 mentions.

## Summary

High: 7 · Medium: 13 · Low: 8. Core theory (Bayesian filtering, factor graphs, VIO, LIO, calibration, benchmarking) is well covered. A targeted researcher re-run on the High items is recommended: AMCL, Cartographer, low-cost sensor rows, benchmark datasets, IMU attitude/ESKF and DROID-SLAM/DPVO; ecosystem links go to the ecosystem researcher/syncer.
