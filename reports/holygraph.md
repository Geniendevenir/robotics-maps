# Holygraph report

Branch: `research/holygraph`. Output: `output/projects.json` (624 rows: 11 Onboarding steps + 613 Projects).

Inputs: 11 existing Notion projects (`output/existing_projects.json`) + 645 `project_candidates` from the 13 `output/knowledge_*.json` files (455 Kind=Project, 190 Kind=Onboarding).

## How the graph was built

1. **Existing rows kept**: all 11 Notion projects are in the file with their `notion_url` (update, never duplicate). Level, Mix check and Unlocks are not output (formula / reverse relation); Level was computed only for validation (0 for Onboarding, else mean of the 3 highest of Novelty/Autonomy/Hardware/Integration).
2. **Deduplication**: 42 candidates were merged into a survivor row (references, knowledge nodes, robots & models, prerequisites unioned; merged deliverable appended to the survivor's Description as "Also covers ..."; merged row's Branch added to Secondary branches). List below.
3. **Onboarding core**: 11 steps (Kind = Onboarding). The other 164 candidates proposed as "Onboarding" by the researchers were too specialised for a shared core, so they were re-typed **Kind = Project** with their own complexity axes (they form the Level 1.33-1.67 inner ring). 17 of them had an "Intro: " prefix, which was dropped so they are not confused with core steps.
4. **Prerequisites**: candidate links kept when the prerequisite has a strictly lower Level. 32 links violated that (equal/higher Level, mostly after onboarding candidates became Level-1.33 projects) and were replaced by the nearest lower-Level ancestor of the offending prerequisite. 262 projects with no valid prerequisite were attached to the core onboarding step of their branch; 32 projects that use a physical SO-101 got `Assemble & teleoperate an SO-101` added when it was not already upstream. 19 curated cross-branch links were added (e.g. ACT -> on-board Jetson policy, hand-eye calibration -> visual servoing). Every Project has 1-3 prerequisites, all with lower Level.
5. **Validation (scripted)**: every prerequisite name resolves to a row in the file; no cycles; every Project traces back to at least one Onboarding step; Software % + Mechanical % + Electrical % = 100 on every row; all select values are from `schemas/notion-schema.md`.

Note: the only Level-0 -> Level-0 link is the pre-existing Notion one, `Assemble & teleoperate an SO-101` <- `Intro: drive a servo motor from code` (onboarding ordering, kept as is).

## Onboarding core (11 steps, ~1 week each)

| Step | Branch | Covers | Origin | Unlocks (direct) |
|---|---|---|---|---|
| Intro: robot anatomy & coordinate frames in sim | Kinematics & dynamics | kinematics, sim (MuJoCo) | existing Notion row | 52 |
| Intro: drive a servo motor from code | Embedded & electronics | electronics, actuators | existing Notion row | 8 |
| Intro: run a pretrained policy in simulation | Robot learning | learning toolchain (LeRobot) | existing Notion row | 17 |
| Assemble & teleoperate an SO-101 | Robot learning | mechanics, electronics, data collection | existing Notion row | 48 |
| Intro: microcontroller, breadboard & I2C sensors | Embedded & electronics | electronics, sensing | new (architect) | 36 |
| Intro: CAD and 3D-print a robot part | Mechanisms & actuation | mechanics (CAD, 3D printing) | new (architect) | 20 |
| Intro: ROS 2 and Nav2 with a simulated mobile robot | Planning | robot software toolchain, sim | new (architect) | 20 |
| Intro: train an RL policy in a GPU simulator | Simulation | simulation, learning toolchain (RL) | new (architect) | 17 |
| Intro: calibrate a webcam and track AprilTags | Perception | perception, sensing | new (architect) | 46 |
| PID tuning playground in simulation | Control | control | promoted candidate con0 | 20 |
| Intro: write a risk assessment for the lab robot | HRI & safety | safety | promoted candidate hri0 | 45 |

## Projects per Branch x Level band

| Branch | 0 (Onboarding) | 1.0-1.99 | 2.0-2.99 | 3.0-3.49 | 3.5+ | Total | Max Level |
|---|---|---|---|---|---|---|---|
| Control | 1 | 21 | 26 | 5 | 1 | 54 | 3.67 |
| Embedded & electronics | 2 | 1 | 17 | 5 | 1 | 26 | 4.0 |
| HRI & safety | 1 | 18 | 20 | 10 | 1 | 50 | 3.67 |
| Kinematics & dynamics | 1 | 15 | 22 | 3 | 1 | 42 | 3.67 |
| Locomotion | 0 | 17 | 18 | 13 | 3 | 51 | 3.67 |
| Manipulation | 0 | 16 | 22 | 9 | 1 | 48 | 3.67 |
| Mechanisms & actuation | 1 | 17 | 23 | 14 | 1 | 56 | 3.67 |
| Perception | 1 | 13 | 30 | 7 | 1 | 52 | 3.67 |
| Planning | 1 | 15 | 27 | 4 | 3 | 50 | 4.0 |
| Robot learning | 2 | 16 | 18 | 16 | 3 | 55 | 3.67 |
| Sensing | 0 | 25 | 20 | 1 | 4 | 50 | 4.0 |
| Simulation | 1 | 13 | 27 | 1 | 1 | 43 | 3.67 |
| State estimation & SLAM | 0 | 13 | 26 | 6 | 2 | 47 | 3.67 |
| **Total** | 11 | 200 | 296 | 94 | 23 | 624 | |

The graph is bottom-heavy: only 23 projects reach Level 3.5+, because most candidates are Hardware = 1 (off-the-shelf) and Autonomy = 2 (scripted).

## Continuity: one path from Onboarding to Level 3.5+ per branch

Before this step, 5 branches had no project at Level 3.5+: Control, HRI & safety, Kinematics & dynamics, Mechanisms & actuation, Simulation. One **bridge project** was added for each (Status Idea, prerequisites taken from the top of that branch's existing chain):

- **Disturbance-rejecting balancer: MPC with a learned residual on real hardware** (Control, Level 3.67, Wow 4) <- Real-time MPC on a reaction-wheel or ballbot-style balancer (3.33); Neural-network dynamics + MPC for a toy car (2.67); Build a reaction-wheel inverted pendulum (3.0)
- **Safe shared-workspace SO-101 assistant: language guardrail, safety filter and handover** (HRI & safety, Level 3.67, Wow 5) <- Guardrail for a language-commanded arm (3.33); Safety filter around a learned arm policy (3.33); Robot-to-human object handover on a desk arm (2.33)
- **Identified-model dynamic throw on the real SO-101** (Kinematics & dynamics, Level 3.67, Wow 4) <- Gradient-based trajectory optimization of a throw (2.0); Full inertial identification of the SO-101 (2.67); Model-based torque feedforward on the SO-101 (2.67)
- **Custom 2-DoF leg module with printed cycloidal joints on a hopping test stand** (Mechanisms & actuation, Level 3.67, Wow 5) <- Captive single-leg actuator test stand (3.0); Guarded dual-disc cycloidal joint prototype (3.0); Low-cost quasi-direct-drive actuator test bench (2.67)
- **Calibrated SO-101 digital twin that predicts real policy success** (Simulation, Level 3.67, Wow 4) <- SO-101 calibration uncertainty challenge (2.67); Digital twin policy-ranking audit (2.67); Sim-to-real transfer on the SO-101 (2.67)

Longest path to the highest-Level project in each branch (all branches now reach 3.5+):

- **Control**: PID tuning playground in simulation (0.0) -> Balance a cart-pole with LQR (1.33) -> Real-time MPC on a reaction-wheel or ballbot-style balancer (3.33) -> Disturbance-rejecting balancer: MPC with a learned residual on real hardware (3.67)
- **Embedded & electronics**: Assemble & teleoperate an SO-101 (0.0) -> Audit demonstration timing (2.0) -> Autonomous pick-and-place with ACT (2.33) -> On-board policy: run an ACT/diffusion policy on Jetson Orin Nano (2.67) -> VLA on board a mobile manipulator with Jetson Thor (4.0)
- **HRI & safety**: PID tuning playground in simulation (0.0) -> CBF safety filter for a 2D robot (1.33) -> Safety filter around a learned arm policy (3.33) -> Safe shared-workspace SO-101 assistant: language guardrail, safety filter and handover (3.67)
- **Kinematics & dynamics**: PID tuning playground in simulation (0.0) -> Identify friction and inertia of one joint (1.67) -> STS3215 actuator model for sim-to-real (2.33) -> Full inertial identification of the SO-101 (2.67) -> Identified-model dynamic throw on the real SO-101 (3.67)
- **Locomotion**: Intro: robot anatomy & coordinate frames in sim (0.0) -> Retarget your own dance to a humanoid (1.33) -> Retargeting-quality study on BeyondMimic (2.67) -> Compare nominal and residual-dynamics tracking (3.67)
- **Manipulation**: Intro: robot anatomy & coordinate frames in sim (0.0) -> Visualize language-conditioned action regions (1.33) -> Solve a keypoint-constrained manipulation task (2.0) -> Evaluate novel object instructions with safety rejection (3.67)
- **Mechanisms & actuation**: Intro: CAD and 3D-print a robot part (0.0) -> Humanoid knee packaging teardown in CAD (1.33) -> Equal-envelope leg joint Pareto study (2.0) -> Captive single-leg actuator test stand (3.0) -> Custom 2-DoF leg module with printed cycloidal joints on a hopping test stand (3.67)
- **Perception**: Intro: calibrate a webcam and track AprilTags (0.0) -> Open-vocabulary 3D map of a room (2.33) -> Fetch-by-name with a mobile manipulator (3.67)
- **Planning**: Intro: ROS 2 and Nav2 with a simulated mobile robot (0.0) -> Planning lab: compare free-form and validated language-to-room plans (1.33) -> Planning lab: translate courier requests to PDDL with schema rejection (2.0) -> Planning lab: build a monitored language-to-inspection executive with adversarial requests (4.0)
- **Robot learning**: Assemble & teleoperate an SO-101 (0.0) -> Audit demonstration timing (2.0) -> Autonomous pick-and-place with ACT (2.33) -> Language-commanded arm with SmolVLA (3.0) -> World-model planning on the SO-101 (3.67)
- **Sensing**: Intro: microcontroller, breadboard & I2C sensors (0.0) -> Magnetic skin patch replacement repeatability bench (2.0) -> Magnetic skin array crosstalk and wiring characterization (3.33) -> Removable forearm skin sleeve with calibration identity (4.0)
- **Simulation**: PID tuning playground in simulation (0.0) -> Identify friction and inertia of one joint (1.67) -> STS3215 actuator model for sim-to-real (2.33) -> SO-101 calibration uncertainty challenge (2.67) -> Calibrated SO-101 digital twin that predicts real policy success (3.67)
- **State estimation & SLAM**: Intro: ROS 2 and Nav2 with a simulated mobile robot (0.0) -> Build a trajectory evaluation scorecard (1.33) -> Replay a public visual-inertial trajectory (1.67) -> Audit clock offsets before running VIO (2.0) -> Design an observable calibration motion (2.33) -> Build a rigid timestamped camera-IMU rig (3.0) -> Engineer a synchronized lidar-camera-IMU mapper (3.67)

## Mix check (Software / Mechanical / Electrical)

All rows sum to 100. Flagged outliers (data left as proposed; adjust before sync if you agree):

- **100% software but a hardware budget** (16): these run on a real webcam, robot or Reachy Mini, so some setup/wiring/mounting time is likely missing (suggest ~90/5/5): Robot speed vs comfort experiment; Multi-person pose benchmark for the lab space; Interruptible conversational robot; Socially assistive coach robot; Reach-target prediction for collaboration; Preference feedback for comfortable motion; Lens-distortion lab: cheap vs. good cameras; Tag-based ground truth rig for evaluating learned perception; Learned stereo vs. on-board stereo; People counter and tracker for a lab entrance; Webcam-only obstacle map from monocular depth; Scene graph change detection: what moved?; Webcam human skeleton in real time; Detect an open hand ready to receive; Voice-commanded Reachy Mini; Color-blob tracker in OpenCV.
- **Sim-only but >=20% mechanical/electrical** (28): mostly Mechanisms & actuation CAD/analysis notebooks at 70/30/0. Acceptable if CAD and mechanical analysis hours count as "Mechanical"; otherwise they are 100% software: CAD-to-sim pipeline for a custom gripper; Closed-loop leg linkage in MuJoCo; Motor architecture decision notebook; Torque-speed envelope from a load case; Joint duty-cycle thermal estimator; Planetary tooth-count explorer; Cycloidal eccentric-to-output animation; Strain-wave tooth engagement explainer; Strain-wave versus cycloidal joint CAD trade study; Belt and capstan preload explorer; Screw lead force-speed visualizer; Four-bar path sketchbook ....
- **>=85% software but custom hardware (Hardware 3-5)** (0): none.
- **>=70% software with a custom subsystem / full custom robot (Hardware 4-5)** (0): none.
- **Off-the-shelf hardware but >=50% mechanical** (0): none.

## Orphans and weak spots

- Projects without prerequisites: 0. Projects that cannot be traced to Onboarding: 0. Unreferenced onboarding steps: 0.
- 262 projects had no candidate prerequisite and were attached only to their branch's onboarding step (the researchers proposed them as standalone starters). Of these, **123 are isolated leaves** (onboarding -> project, unlock nothing), i.e. orphans in the Holygraph sense; by branch: HRI & safety 41, Perception 40, Embedded & electronics 20, Kinematics & dynamics 15, Sensing 5, Control 2. Biggest clusters: Perception (most rows came without chains) and Embedded & electronics. Candidates for pruning or linking at review:
  - Control: Energy-shaping pendulum swing-up; Lyapunov certificate for a pendulum controller
  - Embedded & electronics: Arduino UNO Q split-brain robot; Berkeley Humanoid Lite reproduction; CAN-FD bus sniffer & dashboard; Custom BLDC driver PCB; Custom power & e-stop board for the SO-101; Edge AI accelerator benchmark for robot perception; Embedded Rust (Embassy) firmware for a robot joint; EtherCAT test cell with SOEM; Firmware CI with hardware-in-the-loop; Jitter lab: FreeRTOS vs Zephyr vs PREEMPT_RT; Joint bus shoot-out: serial vs CAN-FD vs EtherCAT; Open Duck Mini build; Protected battery pack + BMS telemetry for a walking robot; Reachy Mini custom expressive behaviours on the edge; Sim-matched digital twin of the arm electronics; SimpleFOC gimbal motor: position, velocity, torque modes; TinyML gesture/keyword control on an MCU; micro-ROS ESP32 sensor node; ros2_control driver for an EtherCAT servo drive; ros2_control hardware interface for SO-101
  - HRI & safety: AI Act classifier for robot features; Cobot mode decision tool; Compliance checklist for a lab demo robot; Constant-velocity vs social-force prediction; Controlled-fall and safe-stop behaviours in sim; Correct a robot with one keypress; Depth-camera separation monitor; Detect an open hand ready to receive; EU robot regulation one-pager; Goal-inference assistive arm; HRI study toolkit for the lab; Handover benchmark in simulation; Humanoid safety readiness review; Interruptible conversational robot; Joystick shared control in sim; LLM-generated social navigation scenarios; Learned speed scaling vs analytic rule; Legibility online experiment; Legible shared autonomy display; Legible vs predictable reaching; Mode switcher: separation monitoring to force limiting; Momentum-observer collision detection in sim; Multi-person pose benchmark for the lab space; Nav2 robot among simulated pedestrians; Preference feedback for comfortable motion; Reach-target prediction for collaboration; Red-team day: jailbreak our own robot agent; Region-aware force limits demo; Robot speed vs comfort experiment; Robot-mounted distance sensor skin; Run the ASIMOV semantic safety benchmark; Safety filter benchmark in safe-control-gym; Safety-limit configurator for a simulated arm; Simulate power-and-force-limited contact; Social costmap layer for Nav2; Socially assistive coach robot; Standards change map: ISO 10218:2025 explainer; Trajectron++ on lab footage; Voice-commanded Reachy Mini; Webcam human skeleton in real time; Why humanoids cannot just stop
  - Kinematics & dynamics: Analytic vs numerical IK shoot-out; Build a 3D-printed delta picker; Centroidal momentum viewer; Closed-loop leg linkage in MuJoCo; Delta robot IK/FK in simulation; Derive and verify a 2-link arm's equations; Follow a moving target with mink; Gradient-based push policy; IK for 5-DoF arms with orientation trade-offs; Live manipulability ellipsoid; Quaternion pitfalls benchmark; RNEA vs ABA timing notebook; URDF/MJCF linter for student robots; Whole-body reach on a simulated humanoid; Write an MJCF for the SO-101 from scratch
  - Perception: 3D detection on KITTI with OpenPCDet; Camera-LiDAR fusion overlay; Click-to-mask object cutout for robot datasets; Color-blob tracker in OpenCV; DIY stereo camera from two webcams; Depth from a single photo; Edge YOLO on a Jetson with ROS 2; Edge open-vocabulary detection on Jetson; Event + frame fusion under extreme lighting; Feature-matching panorama and visual odometry toy; Few-shot object re-identification with DINOv2 features; First YOLO detector on custom objects; Gaussian-splat digital twin of a workbench; Gemini-ER pointing on the SO-101; Gesture-commanded robot; Hand-tracking teleoperation of the SO-101; High-speed ball catching cue with an event camera; Language-pointing arm with open-vocabulary detection; Language-queryable splat of the lab; Learned stereo vs. on-board stereo; Lens-distortion lab: cheap vs. good cameras; LiDAR obstacle detection on a mobile robot; Line-following mobile robot with classical vision; Multi-view object scanning with ICP; Open VLM vs. API VLM for robot pointing; Open-vocabulary detector shoot-out on lab objects; Pan-tilt camera that follows a chosen object; People counter and tracker for a lab entrance; Replace the depth camera: monocular depth for grasping; Robot-mounted camera to live 3D workspace model; Scene graph change detection: what moved?; Sorting robot: detect and bin objects by class; Splat-to-simulation asset pipeline; Synthetic data for detector training; Tag-based ground truth rig for evaluating learned perception; Text-prompted segmentation of every instance with SAM 3; Tracker benchmark on robot-workspace videos; VLM success detector for robot episodes; Vision safety zone: slow the arm when a person is near; Webcam-only obstacle map from monocular depth
  - Sensing: Analog infrared range curve and blind-zone calibration; RGB-depth registration against a measured stepped target; Rolling-shutter and exposure artifact ruler; Stationary IMU warm-up and temperature-drift dossier; Ultrasonic beam-width and soft-surface echo chart
- Low-level dead ends (Level < 2, unlock nothing): 55.
- Many chains are researcher-made 3-step ladders (intro -> 2.0 -> 2.67/3.0) inside one branch (Planning, Simulation, Mechanisms, Locomotion, Robot learning). Cross-branch links are sparse outside the SO-101 / LeRobot spine.

## 10 projects closest to our skills

Filter: Kind = Project, Wow factor >= 4; sorted by Software % (desc), then Level (asc), then Wow (desc).

| # | Project | Branch | Level | Software % | Wow | Hardware cost | Duration |
|---|---|---|---|---|---|---|---|
| 1 | Gaussian-splat digital twin of a workbench | Perception | 1.33 | 100 | 4 | €0 (sim only) | 1 week |
| 2 | Training-free quadruped gaits with DIAL-MPC | Control | 1.67 | 100 | 4 | €0 (sim only) | 2-4 weeks |
| 3 | Reconstruct a recorded room with Gaussian SLAM | State estimation & SLAM | 1.67 | 100 | 4 | €0 (sim only) | 2-4 weeks |
| 4 | Crocoddyl jump for a simulated quadruped | Control | 2.0 | 100 | 4 | €0 (sim only) | 1-2 months |
| 5 | GPU sampling MPC for the SO-101 in Hydrax | Control | 2.0 | 100 | 4 | €0 (sim only) | 1-2 months |
| 6 | Humanoid jump with Crocoddyl | Kinematics & dynamics | 2.0 | 100 | 4 | €0 (sim only) | 1-2 months |
| 7 | Walk with a moving virtual payload | Locomotion | 2.0 | 100 | 4 | €0 (sim only) | 1-2 months |
| 8 | Rotate a cube in simulation | Manipulation | 2.0 | 100 | 4 | €0 (sim only) | 2-4 weeks |
| 9 | Push an object into a graspable pose | Manipulation | 2.0 | 100 | 4 | €0 (sim only) | 2-4 weeks |
| 10 | Plan rearrangement with geometric checks | Manipulation | 2.0 | 100 | 4 | €0 (sim only) | 2-4 weeks |

These are all simulation-first; they test the robot-learning-on-low-cost-hardware wedge only indirectly. The highest-Software, Wow>=4 projects on the real SO-101 are: Sim-to-real transfer on the SO-101 (2.67); Human video → robot data engine (3.0); Language-commanded arm with SmolVLA (3.0); World-model planning on the SO-101 (3.67); Real-world RL fine-tuning (HIL-SERL) (2.67); Goal-inference assistive arm (2.67).

## Merges

| Survivor | Merged candidate (branch) |
|---|---|
| Intro: drive a servo motor from code | Drive one STS3215 servo from Python (Embedded & electronics) |
| Assemble & teleoperate an SO-101 | Build and calibrate an SO-101 leader/follower pair (Embedded & electronics) |
| Assemble & teleoperate an SO-101 | Record leader-follower trajectories (Manipulation) |
| Autonomous pick-and-place with ACT | Train a transfer policy from demonstrations (Manipulation) |
| Intro: robot anatomy & coordinate frames in sim | Frame-transform quiz app (Kinematics & dynamics) |
| Intro: calibrate a webcam and track AprilTags | Intro: project 3D points onto a webcam image (Perception) |
| Intro: calibrate a webcam and track AprilTags | Intro: calibrate a webcam with a printed board (Perception) |
| Intro: calibrate a webcam and track AprilTags | Intro: AprilTag pose axes on a live video (Perception) |
| Intro: calibrate a webcam and track AprilTags | Checkerboard coverage and calibration holdout gallery (Sensing) |
| Intro: microcontroller, breadboard & I2C sensors | Blink to bus: simulated firmware bootcamp (Embedded & electronics) |
| Intro: microcontroller, breadboard & I2C sensors | Breadboard power & multimeter lab (Embedded & electronics) |
| Intro: CAD and 3D-print a robot part | Parametric robot joint assembly walkthrough (Mechanisms & actuation) |
| Intro: ROS 2 and Nav2 with a simulated mobile robot | Planning lab: navigate a supplied simulated map with visible cost overlays (Planning) |
| CBF safety filter for a 2D robot | Intro: control barrier function on a 2D robot (HRI & safety) |
| Safety filter around a learned arm policy | Safety filter around a learned policy (Control) |
| Gravity compensation for a simulated arm | Gravity compensation torques in sim (Kinematics & dynamics) |
| Gravity-compensated SO-101 'floating arm' | Gravity-compensated guiding mode (HRI & safety) |
| Model-based torque feedforward on the SO-101 | Feedforward torque for SO-101 shoulder (Control) |
| Identify friction and inertia of one joint | Servo pendulum friction fit (Kinematics & dynamics) |
| STS3215 actuator model for sim-to-real | SO-101 joint response calibration card (Simulation) |
| Camera-to-arm hand-eye calibration for the SO-101 | Calibrate a real SO-101 and camera (Kinematics & dynamics) |
| Hand-eye calibration in sim | Hand-eye calibration observability in a synthetic camera rig (Sensing) |
| Camera-IMU calibration with Kalibr | Camera-IMU calibration excitation and held-out residual study (Sensing) |
| Depth camera failure atlas | Depth-camera surface and illumination failure gallery (Sensing) |
| Recorded event-stream polarity and time microscope | Event-camera dataset exploration (Perception) |
| Vision safety zone: slow the arm when a person is near | Virtual safety curtain with a webcam (HRI & safety) |
| HRI study toolkit for the lab | Intro: run a 10-person perceived-safety study (HRI & safety) |
| Reachy Mini custom expressive behaviours on the edge | Expressive head cues on Reachy Mini (HRI & safety) |
| Retarget your own dance to a humanoid | Retarget a short standing motion (Locomotion) |
| Retargeting-quality study on BeyondMimic | Reproduce simulated humanoid motion tracking (Locomotion) |
| Contact gradient breakage gallery | Contact gradient sanity check (Kinematics & dynamics) |
| Differentiable system-ID versus black-box search | System identification via differentiable sim (Kinematics & dynamics) |
| Smooth arm motions with Ruckig | Smooth vs jerky: S-curve demo (Kinematics & dynamics) |
| Smooth arm motions with Ruckig | Planning lab: animate a path with unsafe and bounded speed profiles (Planning) |
| Diff-drive odometry from scratch | Watch wheel odometry drift around a square (State estimation & SLAM) |
| Measure odometry drift on an encoder cart | Encoder odometry on a cheap rover (Kinematics & dynamics) |
| Fly a Crazyflie with the stock cascaded PID | Demonstrate guarded Crazyflie hover (Locomotion) |
| Admittance hand-guiding in simulation | Simulate a virtual spring (Manipulation) |
| URDF/MJCF linter for student robots | Robot asset lint and repair lab (Simulation) |
| Frozen-encoder low-data race | Frozen vs. fine-tuned vision encoder for a LeRobot policy (Perception) |
| Robot-camera feature atlas | DINOv2 feature visualization and linear probes (Perception) |
| Gaussian-splat digital twin of a workbench | 3D scan of the lab from phone photos (Perception) |

## Relation names for the syncer

- Knowledge nodes not found in any knowledge_*.json `nodes` (expected to be the existing Notion pilot nodes): Imitation learning (behavior cloning), Learning from human video, Reinforcement learning for robots, Sim-to-real transfer, Teleoperation & robot data collection, Vision-Language-Action models (VLAs), World models & world action models.
- Robots & models not found in any knowledge_*.json `robots_models` (expected to exist in Notion already): ACT (Action Chunking Transformer), SmolVLA, π0 / π0.5.
- Relevant orgs used: Advanced Machine Intelligence (AMI), Hugging Face (LeRobot) (candidates carried no org links).
- Normalised names: `SO-101 arm` -> `SO-101`, `Isaac Lab` -> `Isaac Sim / Isaac Lab`. Other near-duplicate Robots & models names exist across files (e.g. `Crazyflie 2.1+` vs `Bitcraze Crazyflie 2.1`, `MuJoCo Playground` in two files); the syncer should dedupe them in Robots & Models.
- `Used in projects` (Robots & Models reverse relation), Level, Mix check and Unlocks are never output.

