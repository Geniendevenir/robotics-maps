# Verification report: knowledge_sensing.json

Rows checked: 105 (18 knowledge nodes, 33 robots/models/tools, 54 project candidates). Verified: 104. Corrected: 1. Rejected: 0.

## Method
- Opened all 70 distinct source/reference URLs with curl: all 70 returned HTTP 200.
- Checked key claims on the pages themselves, including: D405 7–50 cm range and global shutter, Livox Mid-360 360°×59° FOV, RPLIDAR A1 triangulation, VL53L1X up to 4 m with ROI, GP2Y0A21YK0F 10–80 cm, ICM-42688-P external clock input, BNO085/086 Cortex-M0+ with Bosch/Ceva, DCA1000EVM LVDS + 1-Gbps Ethernet, mmWave Studio Windows ADC capture, OAK-D IMU and rolling-shutter colour, Ouster OS1 vs OS1 Max, ZED-F9P RTK, UMI wrist GoPro, and Springer Handbook chapter 28 (Force and Tactile Sensing).
- Licenses checked on the repositories: Kalibr BSD, allan_variance_ros BSD, direct_visual_lidar_calibration MIT, rosbag2 Apache-2.0 (with MCAP and SQLite3 storage), ODAS MIT, AnySkin MIT, ReSkin MIT.
- Builders: RealSense is the spun-out company (realsenseai.com mentions the Intel spin-off). All builders match their official pages.
- Validated every select value against schemas/notion-schema.md: all valid. Every project's work split sums to 100. Prerequisites resolve within the file and contain no cycles. Every Knowledge nodes relation resolves to a node in this file. The Project ideas field is empty on every node.
- Schema cleanup: removed the non-Notion key `_accessibility_reason` from all 18 nodes. No `Used in projects` key is present. Top-level wrapper keys (branch, nodes, robots_models, project_candidates, top3, sources_consulted) are kept, matching the other verified files.
- Status: nodes and robots/models are now "To verify". Projects stay "Idea", because the Projects Status field has no "To verify" option.
- No Ecosystem Map organizations were checked. This file contains none: Built by, Used by and Relevant orgs are all empty, and builders sit in "Builder (if not in map)".

## Flags for human review
- Robots & models names that point outside this file: `SO-101 arm` and `LeRobot` (in ecosystem_paris_all / knowledge_embedded_electronics) and `ODrive S1 / Pro` (knowledge_embedded_electronics). knowledge_manipulation names the arm `SO-101`. The syncer must pick one canonical name.
- Sensors and dev boards (IMUs, cameras, LiDARs, radar EVMs) use Kind "Simulator/Tool" with Form factor N/A, because Robots & Models has no "Sensor" kind. Consider adding a Kind option.
- Onboarding "Radar point-cloud capture and no-target baseline" is priced at €500-5k. The IWR6843ISK board alone is probably <€500, but the delivered price is unknown, so I left it unchanged.
- The RSS 2025 papers index (cited on the mmWave node) is a generic program page that lists radar papers. It is supplementary only.
- Delivered EU prices are "unknown" for most hardware rows (honest, but not useful for budgeting).

## Rows

| Table | Row | Verdict | Reason |
|---|---|---|---|
| Knowledge node | Sensor characteristics, uncertainty & noise | verified | sources load and support claims; select values valid; `_accessibility_reason` removed |
| Knowledge node | Joint encoders & proprioceptive sensing | verified | sources load and support claims; select values valid; `_accessibility_reason` removed |
| Knowledge node | IMUs: accelerometers, gyroscopes & magnetometers | verified | sources load and support claims; select values valid; `_accessibility_reason` removed |
| Knowledge node | Force/torque sensing & current-based torque estimation | verified | sources load and support claims; select values valid; `_accessibility_reason` removed |
| Knowledge node | RGB cameras & intrinsic calibration | verified | sources load and support claims; select values valid; `_accessibility_reason` removed |
| Knowledge node | Depth cameras: stereo, structured light & ToF | verified | sources load and support claims; select values valid; `_accessibility_reason` removed |
| Knowledge node | 2D & 3D LiDAR hardware | verified | sources load and support claims; select values valid; `_accessibility_reason` removed |
| Knowledge node | Short-range ranging: ultrasonic, infrared & ToF | verified | sources load and support claims; select values valid; `_accessibility_reason` removed |
| Knowledge node | Extrinsic & multi-sensor calibration | verified | sources load and support claims; select values valid; `_accessibility_reason` removed |
| Knowledge node | Time synchronization & timestamping | verified | sources load and support claims; select values valid; `_accessibility_reason` removed |
| Knowledge node | ROS 2 sensor drivers, metadata & recording | verified | sources load and support claims; select values valid; `_accessibility_reason` removed |
| Knowledge node | Sensor simulation & noise models | verified | sources load and support claims; select values valid; `_accessibility_reason` removed |
| Knowledge node | Event cameras & asynchronous acquisition | verified | sources load and support claims; select values valid; `_accessibility_reason` removed |
| Knowledge node | mmWave radar sensing hardware | verified | sources load and support claims; select values valid; `_accessibility_reason` removed |
| Knowledge node | Robot skin & distributed tactile hardware | verified | sources load and support claims; select values valid; `_accessibility_reason` removed |
| Knowledge node | Microphone arrays & robot audio acquisition | verified | sources load and support claims; select values valid; `_accessibility_reason` removed |
| Knowledge node | GNSS & RTK receiver hardware | verified | sources load and support claims; select values valid; `_accessibility_reason` removed |
| Knowledge node | Wrist cameras & multi-camera data-collection rigs | verified | sources load and support claims; select values valid; `_accessibility_reason` removed |
| Robot/model | Allan Variance ROS | verified | official page loads; product/tool exists, builder and key specs match |
| Robot/model | AS5600 magnetic angle sensor (Adafruit breakout) | verified | official page loads; product/tool exists, builder and key specs match |
| Robot/model | BNO085/BNO086 IMU | verified | official page loads; product/tool exists, builder and key specs match |
| Robot/model | ICM-42688-P | verified | official page loads; product/tool exists, builder and key specs match |
| Robot/model | ATI Mini45 force/torque transducer | verified | official page loads; product/tool exists, builder and key specs match |
| Robot/model | OpenCV camera calibration tools | verified | official page loads; product/tool exists, builder and key specs match |
| Robot/model | Kalibr | verified | official page loads; product/tool exists, builder and key specs match |
| Robot/model | RealSense D405 | verified | official page loads; product/tool exists, builder and key specs match |
| Robot/model | Luxonis OAK-D | verified | official page loads; product/tool exists, builder and key specs match |
| Robot/model | Orbbec Gemini 2 | verified | official page loads; product/tool exists, builder and key specs match |
| Robot/model | Stereolabs ZED 2 | verified | official page loads; product/tool exists, builder and key specs match |
| Robot/model | RPLIDAR A1 | verified | official page loads; product/tool exists, builder and key specs match |
| Robot/model | Livox Mid-360 | verified | official page loads; product/tool exists, builder and key specs match |
| Robot/model | Ouster OS1 | verified | official page loads; product/tool exists, builder and key specs match |
| Robot/model | VL53L1X carrier (Pololu 3415) | verified | official page loads; product/tool exists, builder and key specs match |
| Robot/model | Sharp/Socle GP2Y0A21YK0F | verified | official page loads; product/tool exists, builder and key specs match |
| Robot/model | Direct visual LiDAR calibration toolbox | verified | official page loads; product/tool exists, builder and key specs match |
| Robot/model | LinuxPTP | verified | official page loads; product/tool exists, builder and key specs match |
| Robot/model | rosbag2 | verified | official page loads; product/tool exists, builder and key specs match |
| Robot/model | ROS image_pipeline | verified | official page loads; product/tool exists, builder and key specs match |
| Robot/model | Gazebo sensor simulation | verified | official page loads; product/tool exists, builder and key specs match |
| Robot/model | NVIDIA Isaac Sim sensors | verified | official page loads; product/tool exists, builder and key specs match |
| Robot/model | OpenEB / Metavision open modules | verified | official page loads; product/tool exists, builder and key specs match |
| Robot/model | iniVation event-camera systems | verified | official page loads; product/tool exists, builder and key specs match |
| Robot/model | TI IWR6843ISK evaluation board | verified | official page loads; product/tool exists, builder and key specs match |
| Robot/model | ReSkin magnetic tactile skin | corrected | Open source false->true (reskin_sensor repo is MIT, linked from reskin.dev); Release year null->2021 (CoRL 2021, arXiv 2111.00071); added repo + arXiv sources |
| Robot/model | AnySkin | verified | official page loads; product/tool exists, builder and key specs match |
| Robot/model | ReSpeaker USB 4-Mic Array XVF3000 v2.0 | verified | official page loads; product/tool exists, builder and key specs match |
| Robot/model | ODAS | verified | official page loads; product/tool exists, builder and key specs match |
| Robot/model | u-blox ZED-F9P GNSS module | verified | official page loads; product/tool exists, builder and key specs match |
| Robot/model | UMI data-collection gripper | verified | official page loads; product/tool exists, builder and key specs match |
| Robot/model | TI DCA1000EVM | verified | official page loads; product/tool exists, builder and key specs match |
| Robot/model | TI mmWave Studio | verified | official page loads; product/tool exists, builder and key specs match |
| Project | Measurement truth versus resolution: a sensor-error notebook | verified | select values valid; split sums to 100; relations resolve (see flags for external names) |
| Project | Sampling-rate aliasing on a moving distance target | verified | select values valid; split sums to 100; relations resolve (see flags for external names) |
| Project | Stationary IMU warm-up and temperature-drift dossier | verified | select values valid; split sums to 100; relations resolve (see flags for external names) |
| Project | Encoder rollover and index-reference explorer | verified | select values valid; split sums to 100; relations resolve (see flags for external names) |
| Project | Magnet alignment and standoff repeatability jig | verified | select values valid; split sums to 100; relations resolve (see flags for external names) |
| Project | Incremental versus magnetic joint-angle metrology fixture | verified | select values valid; split sums to 100; relations resolve (see flags for external names) |
| Project | IMU units, missing orientation and axis-sign replay | verified | select values valid; split sums to 100; relations resolve (see flags for external names) |
| Project | Allan-deviation repeatability across stationary sessions | verified | select values valid; split sums to 100; relations resolve (see flags for external names) |
| Project | IMU mount vibration transmission comparison | verified | select values valid; split sums to 100; relations resolve (see flags for external names) |
| Project | Six-axis wrench units and lever-arm replay | verified | select values valid; split sums to 100; relations resolve (see flags for external names) |
| Project | Wrist transducer zeroing and load-fixture calibration | verified | select values valid; split sums to 100; relations resolve (see flags for external names) |
| Project | Motor-current torque estimate versus an independent load reference | verified | select values valid; split sums to 100; relations resolve (see flags for external names) |
| Project | Checkerboard coverage and calibration holdout gallery | verified | select values valid; split sums to 100; relations resolve (see flags for external names) |
| Project | Rolling-shutter and exposure artifact ruler | verified | select values valid; split sums to 100; relations resolve (see flags for external names) |
| Project | Focus and resolution changes invalidate camera calibration | verified | select values valid; split sums to 100; relations resolve (see flags for external names) |
| Project | Depth-camera surface and illumination failure gallery | verified | select values valid; split sums to 100; relations resolve (see flags for external names) |
| Project | Close-range stereo occlusion and minimum-distance test rig | verified | select values valid; split sums to 100; relations resolve (see flags for external names) |
| Project | RGB-depth registration against a measured stepped target | verified | select values valid; split sums to 100; relations resolve (see flags for external names) |
| Project | Planar LiDAR scan geometry and blind-zone bench | verified | select values valid; split sums to 100; relations resolve (see flags for external names) |
| Project | LiDAR reflectivity and incidence-angle return audit | verified | select values valid; split sums to 100; relations resolve (see flags for external names) |
| Project | 3D LiDAR coverage and timestamped scan-density atlas | verified | select values valid; split sums to 100; relations resolve (see flags for external names) |
| Project | Ultrasonic beam-width and soft-surface echo chart | verified | select values valid; split sums to 100; relations resolve (see flags for external names) |
| Project | Analog infrared range curve and blind-zone calibration | verified | select values valid; split sums to 100; relations resolve (see flags for external names) |
| Project | ToF range validity across target color and ambient light | verified | select values valid; split sums to 100; relations resolve (see flags for external names) |
| Project | Hand-eye calibration observability in a synthetic camera rig | verified | select values valid; split sums to 100; relations resolve (see flags for external names) |
| Project | Camera-IMU calibration excitation and held-out residual study | verified | select values valid; split sums to 100; relations resolve (see flags for external names) |
| Project | Remountable camera-LiDAR calibration target and fixture | verified | select values valid; split sums to 100; relations resolve (see flags for external names) |
| Project | Acquisition-time versus arrival-time timestamp sandbox | verified | select values valid; split sums to 100; relations resolve (see flags for external names) |
| Project | Hardware-trigger exposure-skew measurement fixture | verified | select values valid; split sums to 100; relations resolve (see flags for external names) |
| Project | PTP clock alignment under sensor-network load | verified | select values valid; split sums to 100; relations resolve (see flags for external names) |
| Project | ROS sensor-message units and covariance contract linter | verified | select values valid; split sums to 100; relations resolve (see flags for external names) |
| Project | Sensor QoS loss-versus-latency capture experiment | verified | select values valid; split sums to 100; relations resolve (see flags for external names) |
| Project | Recording archive recovery and calibration-manifest integrity | verified | select values valid; split sums to 100; relations resolve (see flags for external names) |
| Project | Gazebo noise-model fingerprint with known ground truth | verified | select values valid; split sums to 100; relations resolve (see flags for external names) |
| Project | Synthetic sensor outage and saturation playback harness | verified | select values valid; split sums to 100; relations resolve (see flags for external names) |
| Project | Measured short-range sensor response versus simulated rays | verified | select values valid; split sums to 100; relations resolve (see flags for external names) |
| Project | Recorded event-stream polarity and time microscope | verified | select values valid; split sums to 100; relations resolve (see flags for external names) |
| Project | Event-camera illumination-flicker throughput envelope | verified | select values valid; split sums to 100; relations resolve (see flags for external names) |
| Project | Reusable event-RGB calibration target and coverage protocol | verified | select values valid; split sums to 100; relations resolve (see flags for external names) |
| Project | Radar point-cloud capture and no-target baseline | verified | select values valid; split sums to 100; relations resolve (see flags for external names) |
| Project | Radar ADC capture throughput and packet-loss characterization | verified | select values valid; split sums to 100; relations resolve (see flags for external names) |
| Project | Reproducible radar multipath and material test enclosure | verified | select values valid; split sums to 100; relations resolve (see flags for external names) |
| Project | Magnetic skin patch replacement repeatability bench | verified | select values valid; split sums to 100; relations resolve (see flags for external names) |
| Project | Magnetic skin array crosstalk and wiring characterization | verified | select values valid; split sums to 100; relations resolve (see flags for external names) |
| Project | Removable forearm skin sleeve with calibration identity | verified | select values valid; split sums to 100; relations resolve (see flags for external names) |
| Project | Microphone channel ordering and geometry clap board | verified | select values valid; split sums to 100; relations resolve (see flags for external names) |
| Project | Robot motor-noise audio acquisition dossier | verified | select values valid; split sums to 100; relations resolve (see flags for external names) |
| Project | Long-recording microphone sample-clock drift audit | verified | select values valid; split sums to 100; relations resolve (see flags for external names) |
| Project | RTK stationary receiver and correction-outage logbook | verified | select values valid; split sums to 100; relations resolve (see flags for external names) |
| Project | GNSS antenna mounting and multipath repeatability survey | verified | select values valid; split sums to 100; relations resolve (see flags for external names) |
| Project | GNSS receiver position-time metadata ingestion contract | verified | select values valid; split sums to 100; relations resolve (see flags for external names) |
| Project | Multi-camera USB topology and capture-bandwidth atlas | verified | select values valid; split sums to 100; relations resolve (see flags for external names) |
| Project | Quick-release wrist-camera remount calibration fixture | verified | select values valid; split sums to 100; relations resolve (see flags for external names) |
| Project | VLA-ready sensing rig with verifiable calibration provenance | verified | select values valid; split sums to 100; relations resolve (see flags for external names) |
