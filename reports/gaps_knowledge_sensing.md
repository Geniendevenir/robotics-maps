# Coverage gaps: Sensing

Date: 2026-11-13. File reviewed: `output/knowledge_sensing.json` (verified version: 18 nodes, 33 robots/models/tools, 54 project candidates).
Branch: `research/knowledge-sensing`. No rows were added and Notion was not touched.

## How this was checked
- Compared against the sensing part of the Springer Handbook of Robotics (2nd ed., Part C "Sensing and Perception": force & tactile, inertial sensing/GPS/odometry, sonar, range sensing, 3D vision, visual object class recognition, multisensor fusion), the sensing and data-collection topics in ICRA/RSS/CoRL tracks (tactile sensing, calibration, robot-learning data collection), typical robotics sensing course syllabi, and the hardware a low-cost robot-learning lab (LeRobot / SO-101, UMI-style rigs) actually uses.
- Ran keyword checks on the file (and on the other output files, to avoid flagging topics another branch already owns). "Missing" means there is no dedicated node or row. A passing mention inside another row does not count as coverage.
- These gaps come from comparing the file against those reference outlines and from domain knowledge. No new web sources were opened for this report, so the researcher must source every gap before adding a row.

## High importance
1. **Vision-based tactile sensors (GelSight / GelSight Mini, Meta DIGIT, 9DTact-class DIY sensors)**: the dominant tactile modality in 2024-2026 manipulation and robot-learning papers. The "Robot skin" node covers only magnetic skins (ReSkin, AnySkin). GelSight appears only in knowledge_manipulation, DIGIT never in this file; no node or hardware row.
2. **Low-cost cameras and camera interfaces (USB UVC webcams, Raspberry Pi Camera Module / MIPI CSI-2, Arducam global-shutter modules)**: these are the cameras actually used on SO-101/LeRobot rigs. "webcam" has 1 mention, UVC and MIPI have 0, and there are no hardware rows (only D405, OAK-D, Gemini 2, ZED 2).
3. **Fiducial markers & calibration targets (AprilTag, ArUco, ChArUco)**: zero mentions, yet they are the standard tool for intrinsic/extrinsic/hand-eye calibration and cheap ground-truth pose. Calibration projects in the file rely on checkerboards only.
4. **Low-cost force sensing (load cells + HX711-class ADCs, strain gauges / Wheatstone bridges, FSRs)**: zero mentions. The only F/T hardware row is the ATI Mini45 (expensive); the lab needs a sub-€50 path for gripper/contact force.
5. **Smart-servo built-in sensing (Feetech STS3215 / Dynamixel position, load, voltage and temperature readouts)**: this is the actual proprioception of the SO-101 wedge. One passing Feetech mention; no node section, no row, no project measuring servo encoder/load-reading quality.

## Medium importance
6. **Motion capture & ground-truth measurement (OptiTrack/Vicon, low-cost alternatives such as AprilTag rigs or HTC Vive trackers)**: one passing "motion capture" mention; needed to evaluate any sensor or estimator.
7. **Human-demonstration sensing devices for teleop/data collection (VR headsets such as Meta Quest for hand tracking, data gloves, leader arms as sensors)**: zero mentions of VR/Quest/gloves here; overlaps Robot learning, so it could be owned there.
8. **Signal conditioning & digital filtering (anti-aliasing, low-pass/moving-average, debouncing, ADC basics for analog sensors)**: "filter" has 1 mention, "low-pass" and "anti-alias" 0. Sampling aliasing exists only as a project.
9. **Sensor buses and wiring for sensors (I2C, SPI, UART, address conflicts, pull-ups, bus speed limits)**: I2C has 1 mention, SPI 0. Partly overlaps Embedded & electronics.
10. **Odometry sensors (wheel encoders, optical-flow / mouse sensors such as PMW3901)**: Springer groups odometry with inertial sensing; zero dedicated coverage here.
11. **Contact, limit and proximity sensors (limit switches, bumpers, capacitive/inductive proximity, Hall-effect switches)**: zero mentions; they are the cheapest safety and homing sensors.
12. **Sensor data inspection & visualization (RViz, Foxglove, Rerun used by LeRobot)**: zero mentions; the ROS 2 recording node covers rosbag2/MCAP but not how students look at the data.
13. **Tactile sensor simulation (TACTO, Taxim, tactile in Isaac/MuJoCo)**: zero mentions; the simulation node covers cameras/LiDAR/IMU noise only.

## Low importance
14. **Thermal cameras (FLIR Lepton, MLX90640)**: zero mentions; niche for the lab.
15. **More common depth-camera rows (RealSense D435i, Orbbec Femto, ZED Mini)**: D435i is the most cited depth camera in student projects; only D405 is listed.
16. **Magnetometer calibration (hard/soft iron) and barometers/altimeters**: probably inside the IMU node text, but no explicit coverage.
17. **Safety-rated laser scanners (SICK, Hokuyo) and laser eye-safety classes**: industrial reference points, outside the lab budget.
18. **Polarization, hyperspectral and other exotic imaging**: frontier/niche; zero mentions.
19. **Wide-FOV / fisheye / 360° cameras (Insta360-class) and fisheye calibration models**: UMI uses a fisheye GoPro, but fisheye models are not named.

## Summary
- High: 5 · Medium: 8 · Low: 6.
- Per the pipeline, the High items should be sent back to the knowledge-researcher (gaps only) before the Holygraph step.
