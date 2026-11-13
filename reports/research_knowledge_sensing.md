# Research log: Sensing — parts 1 and 2

Final deliverable: 18 knowledge nodes, 33 reference sensors/tools, 54 project candidates (18 Onboarding / 36 Project), three top-node recommendations and 75 distinct substantive HTTP-200 sources. The initial discovery snapshot below is retained as an audit trail; part 2 adds project synthesis, additional discovery and final validation.

## Method and boundaries

- Read the researcher playbook, CLAUDE.md, schema, Embedded research/verification report and Embedded/Manipulation JSON before drafting. No Notion access. Projects and top-three selection are intentionally deferred to part 2.
- Taxonomy: 18 nodes spanning physical measurement, calibration, timing and acquisition. Excludes detection/segmentation, SLAM, EKF fusion, robot policy training and manipulation workflows. The existing Sensor interfacing & signal conditioning and Tactile sensing for manipulation nodes are referenced, not duplicated. Existing Embedded/Manipulation hardware/tool names were checked and not recreated.
- Springer grounding uses the actual Handbook multimedia companion (not a successful-looking HTTP challenge): chapter 28 Force and Tactile Sensing; 29 Inertial Sensing, GPS and Odometry; 30 Sonar Sensing; 31 Range Sensing. Chapter 5 Sensing and Estimation and 35 Multisensor Data Fusion mark the interface to the separate estimation branch. Companion chapter navigation was read directly; Springer publisher pages returned a JavaScript challenge and are not evidence.
- ETH Autonomous Mobile Robots sensor slides provide classification, encoders, IMU, sonar, laser and structured-light coverage; ETH course page and MIT RSS syllabus ground the progression from sensing to cameras and integration. These older educational sources are used for stable physics, not current availability. Current MIT course description distinguishes sensing, state estimation and perception. RSS 2025 program includes Doppler radar and visual-tactile work; CoRL 2026 establishes the learning interface, not vendor specifications. ICRA fetch was blocked and is not used as evidence.
- Primary URLs were fetched with curl -sL, a Mozilla browser user agent, a 45-second limit, saved bodies, and HTTP status/byte counts. HTML script/style markup was removed and rg (grep-equivalent) checked claimed terms in page text. The ETH PDF was text-extracted using pypdf and grepped; raw OpenCV and ROS source documentation replaced blocked/challenge docs. HTTP 200 alone never qualifies a page. Every row source is a successful substantive fetch, with evidence snippets below.
- Scope and timing: recent available research includes UMI and AnySkin (2024), RSS 2025 and CoRL 2026; current undated vendor/docs pages support present documented capabilities, not inferred product launch years. All release years are null except directly dated 2024 UMI/AnySkin references. No claim of exhaustive 2026 SOTA or stock availability.
- Price/access strings do not invent current prices. Cost buckets, time-to-demo and accessibility are lab planning estimates, not vendor facts or experimentally validated build results. Costs refer to the smallest proposed learning setup, not every reference product: current telemetry rather than an ATI transducer, basic 2D rather than Ouster, recorded events rather than buying an event camera, and a small camera rig rather than complete UMI. GNSS/radar have conservative larger integration allowances. Existing host compute is assumed; taxes, shipping and full robot costs are excluded and must be checked before purchase.
- Open source=true is scoped to public software/design repositories, not third-party silicon, optics or proprietary firmware; false for physical products means no whole-product open-source assertion was established here, not proof that all associated software is closed. Ecosystem relations are empty pending resolution; builder text carries checked attribution. Sensor components use Simulator/Tool, N/A form factor/model type per the pilot convention.
- Query-based gap checks followed the initial primary-source batches: “robot sensor hardware characterization calibration synchronization sensing taxonomy”, “robotics sensing course proprioceptive exteroceptive sensors overview”, and “robot sensing modalities event radar audio tactile GNSS sensor survey”. Each added 0 new in-scope node categories against the existing 18 (0%, below 10%, three consecutive queries). Search snippets were discovery aids only, never row evidence. This is taxonomy saturation, not proof of exhaustive coverage of all sensor products. Temperature, humidity and application-specific chemical sensors remain examples of general characterization rather than separate core robotics nodes.
- Acquisition caveats: RPLIDAR A1 is triangulation, not ToF; D405 is stereo, not ToF or a separate RGB camera; current-estimated motor torque is not wrist contact force or a safety function. BNO orientation firmware output is not raw inertial data. PTP aligns clocks but does not itself trigger simultaneous exposure. Record-time is not necessarily acquisition-time. Magnetic skin patches are not established full-body skin products. UMI’s downstream SLAM/policy stages are explicitly outside this branch. D435 was not given a new row: its attempted product URL failed and the current SDK README describes D435if instead; no specs were copied between variants. AS5047 also remains a follow-up rather than using a failed product URL.
- One local tooling issue: pdftotext was absent. Environment inspection found no project venv/dependency manifest (data-only repo); installed pypdf in the user Python environment to read the ETH PDF. No repository environment/build config was changed.

## Fetch-status log

All attempts, including rejected/challenge pages. Bytes are downloaded response bytes, not evidence of correctness. `accepted` means readable content matched the stated audit pattern; accepted taxonomy-only sources need not appear on a row. Raw fetch bodies and complete extracted text are retained in `/home/ubuntu/sensing_evidence/` for this handoff; the portable audit below contains the actual matched excerpts.

| Key | Status | Bytes | Decision | URL |
|---|---:|---:|---|---|
| noise | 200 | 215027 | accepted | https://github.com/ethz-asl/kalibr/wiki/IMU-Noise-Model |
| allan | 200 | 269893 | accepted | https://github.com/ori-drs/allan_variance_ros |
| as5600 | 200 | 282887 | rejected: status or no substantive match | https://ams-osram.com/products/sensors/position-sensors/ams-as5600-position-sensor |
| as5047 | 404 | 261031 | rejected: status or no substantive match | https://ams-osram.com/products/sensors/position-sensors/ams-as5047p-high-speed-position-sensor |
| encoder | 404 | 9379 | rejected: status or no substantive match | https://docs.simplefoc.com/encoders |
| bno085 | 200 | 73008 | accepted | https://www.ceva-ip.com/product/bno-9-axis-imu/ |
| icm42688 | 200 | 739938 | accepted | https://invensense.tdk.com/products/motion-tracking/6-axis/icm-42688-p/ |
| imu | 200 | 200174 | accepted | https://github.com/ethz-asl/kalibr/wiki/IMU-Supported-Models |
| ati | 200 | 78884 | accepted | https://www.ati-ia.com/products/ft/ft_models.aspx?id=Mini45 |
| current | 200 | 141380 | accepted | https://docs.odriverobotics.com/v/latest/manual/control.html |
| opencv | 403 | 5521 | rejected: status or no substantive match | https://docs.opencv.org/4.x/dc/dbb/tutorial_py_calibration.html |
| pinhole | 403 | 5494 | rejected: status or no substantive match | https://docs.opencv.org/4.x/d9/d0c/group__calib3d.html |
| kalibr | 200 | 254527 | accepted | https://github.com/ethz-asl/kalibr |
| kalibrcam | 200 | 198544 | accepted | https://github.com/ethz-asl/kalibr/wiki/multiple-camera-calibration |
| d435 | 404 | 95010 | rejected: status or no substantive match | https://www.realsenseai.com/depth-camera-d435/ |
| d405 | 200 | 228021 | accepted | https://www.realsenseai.com/depth-camera-d405/ |
| oak | 200 | 1137006 | accepted | https://docs.luxonis.com/hardware/products/OAK-D |
| gemini | 200 | 321150 | accepted | https://www.orbbec.com/products/stereo-vision-camera/gemini-2/ |
| zed | 200 | 572904 | accepted | https://www.stereolabs.com/en-us/products/zed-2 |
| rplidar | 200 | 42572 | accepted | https://www.slamtec.com/en/Lidar/A1 |
| livox | 200 | 425167 | accepted | https://www.livoxtech.com/mid-360 |
| ouster | 200 | 282718 | accepted | https://ouster.com/products/hardware/os1-lidar-sensor |
| vl53 | 000 | 0 | rejected: status or no substantive match | https://www.st.com/en/imaging-and-photonics-solutions/vl53l1x.html |
| ultrasonic | 200 | 71797 | accepted | https://learn.adafruit.com/ultrasonic-sonar-distance-sensors/overview |
| ir | 200 | 63358 | accepted | https://www.pololu.com/product/136 |
| kalibrimu | 200 | 201983 | accepted | https://github.com/ethz-asl/kalibr/wiki/camera-imu-calibration |
| lidarcal | 200 | 245797 | accepted | https://github.com/koide3/direct_visual_lidar_calibration |
| ptp | 200 | 7731 | accepted | https://www.linuxptp.org/ |
| trigger | 200 | 524254 | accepted | https://docs.baslerweb.com/triggered-image-acquisition |
| synch | 200 | 341328 | accepted | https://docs.baslerweb.com/precision-time-protocol |
| msgs | 500 | 2303 | rejected: status or no substantive match | https://docs.ros.org/en/rolling/p/sensor_msgs/ |
| bag | 200 | 8399 | rejected: status or no substantive match | https://docs.ros.org/en/jazzy/Tutorials/Beginner-CLI-Tools/Recording-And-Playing-Back-Data/Recording-And-Playing-Back-Data.html |
| pipeline | 200 | 7433 | rejected: status or no substantive match | https://docs.ros.org/en/rolling/p/image_pipeline/ |
| qos | 200 | 8358 | rejected: status or no substantive match | https://docs.ros.org/en/jazzy/Concepts/Intermediate/About-Quality-of-Service-Settings.html |
| gazebo | 200 | 79422 | accepted | https://gazebosim.org/docs/harmonic/sensors/ |
| gazebonoise | 200 | 25589 | accepted | https://gazebosim.org/api/sensors/8/classgz_1_1sensors_1_1GaussianNoiseModel.html |
| isaac | 200 | 104384 | accepted | https://docs.isaacsim.omniverse.nvidia.com/latest/sensors/index.html |
| prophesee | 200 | 316574 | accepted | https://www.prophesee.ai/event-based-vision/ |
| metavision | 200 | 18243 | accepted | https://docs.prophesee.ai/stable/index.html |
| inivation | 200 | 1257327 | accepted | https://inivation.com/ |
| radar | 200 | 549989 | accepted | https://www.ti.com/product/IWR6843 |
| radarisk | 200 | 1020683 | accepted | https://www.ti.com/tool/IWR6843ISK |
| reskin | 200 | 13024 | accepted | https://reskin.dev/ |
| anyskin | 200 | 21097 | accepted | https://any-skin.github.io/ |
| anyskinrepo | 404 | 224695 | rejected: status or no substantive match | https://github.com/rail-berkeley/anyskin |
| respeaker | 200 | 168254 | accepted | https://wiki.seeedstudio.com/ReSpeaker_Mic_Array_v2.0/ |
| odas | 200 | 232814 | accepted | https://github.com/introlab/odas |
| gnss | 200 | 86508 | accepted | https://www.u-blox.com/en/product/zed-f9p-module |
| rtklib | 000 | 0 | rejected: status or no substantive match | https://www.rtklib.com/ |
| umi | 200 | 34874 | accepted | https://umi-gripper.github.io/ |
| umirepo | 200 | 286468 | accepted | https://github.com/real-stanford/universal_manipulation_interface |
| lerobotcam | 200 | 169199 | accepted | https://huggingface.co/docs/lerobot/cameras |
| springer | 200 | 3038 | rejected: status or no substantive match | https://link.springer.com/referencework/10.1007/978-3-319-32552-1 |
| eth | 404 | 7885 | rejected: status or no substantive match | https://rsl.ethz.ch/education-students/lectures/robotics.html |
| mit | 404 | 3431 | rejected: status or no substantive match | https://ocw.mit.edu/courses/6-141-robotics-science-and-systems-i-fall-2014/ |
| rss | 404 | 8766 | rejected: status or no substantive match | https://roboticsconference.org/program/papers/ |
| icra | 403 | 5667 | rejected: status or no substantive match | https://2025.ieee-icra.org/ |
| corl | 200 | 306038 | accepted | https://www.corl.org/ |
| as5600doc | 200 | 3856 | rejected: status or no substantive match | https://raw.githubusercontent.com/ams-OSRAM/ams-OSRAM.github.io/master/README.md |
| encoder2 | 200 | 105040 | accepted | https://docs.simplefoc.com/encoder |
| opencvraw | 200 | 10651 | accepted | https://raw.githubusercontent.com/opencv/opencv/4.x/doc/py_tutorials/py_calib3d/py_calibration/py_calibration.markdown |
| opencvhand | 200 | 246463 | accepted | https://raw.githubusercontent.com/opencv/opencv/4.x/modules/calib3d/include/opencv2/calib3d.hpp |
| msgsraw | 200 | 1211 | accepted | https://raw.githubusercontent.com/ros2/common_interfaces/rolling/sensor_msgs/msg/Imu.msg |
| imageraw | 200 | 1396 | accepted | https://raw.githubusercontent.com/ros2/common_interfaces/rolling/sensor_msgs/msg/Image.msg |
| bagraw | 200 | 488505 | accepted | https://github.com/ros2/rosbag2 |
| pipelineraw | 200 | 233220 | accepted | https://github.com/ros-perception/image_pipeline |
| qosraw | 200 | 13272 | accepted | https://raw.githubusercontent.com/ros2/ros2_documentation/jazzy/source/Concepts/Intermediate/About-Quality-of-Service-Settings.rst |
| as5600board | 200 | 76291 | accepted | https://learn.adafruit.com/adafruit-as5600-magnetic-angle-sensor/overview |
| springerold | 200 | 3038 | rejected: status or no substantive match | https://link.springer.com/book/10.1007/978-3-540-30301-5 |
| springertoc | 200 | 3038 | rejected: status or no substantive match | https://www.springer.com/gp/book/9783319325507 |
| ethcourse | 404 | 7885 | rejected: status or no substantive match | https://rsl.ethz.ch/education-students/lectures/robotics-introduction.html |
| mitcourse | 404 | 3431 | rejected: status or no substantive match | https://ocw.mit.edu/courses/6-141-robotics-science-and-systems-i-spring-2014/ |
| rss2025 | 200 | 197708 | accepted | https://roboticsconference.org/2025/program/papers/ |
| anyskinpaper | 200 | 41456 | accepted | https://arxiv.org/abs/2409.08276 |
| kalibrmodels | 200 | 193568 | accepted | https://github.com/ethz-asl/kalibr/wiki/supported-models |
| d435repo | 200 | 393842 | accepted | https://github.com/realsenseai/librealsense |
| handbook28 | 200 | 21177 | accepted | https://www.handbookofrobotics.org/view-chapter/videodetails/28 |
| handbook | 200 | 20301 | accepted | https://www.handbookofrobotics.org/ |
| ethsensors | 200 | 4131318 | accepted | https://ethz.ch/content/dam/ethz/special-interest/mavt/robotics-n-intelligent-systems/asl-dam/documents/lectures/autonomous_mobile_robots/spring-2015/04_-_Perception_I_-_Sensors.pdf |
| ethsyllabus | 200 | 41772 | accepted | https://asl.ethz.ch/education/lectures/autonomous_mobile_robots/spring-2020.html |
| mitsyllabus | 200 | 27879 | accepted | https://courses.csail.mit.edu/6.141/spring2010/pub/syllabus.html |
| mitmodern | 200 | 127016 | accepted | https://meche.mit.edu/featured-classes/robotics-science-and-systems |
| anyskinreal | 200 | 229857 | accepted | https://github.com/raunaqbhirangi/anyskin |
| vl53board | 200 | 89805 | accepted | https://www.pololu.com/product/3415 |
| metavisionlicense | 200 | 350182 | accepted | https://github.com/prophesee-ai/openeb |
| opencvlicense | 200 | 11358 | accepted | https://raw.githubusercontent.com/opencv/opencv/4.x/LICENSE |
| gazeborepo | 200 | 314368 | accepted | https://github.com/gazebosim/gz-sensors |
| ptprepo | 200 | 467135 | accepted | https://github.com/richardcochran/linuxptp |
| umilicense | 200 | 1105 | accepted | https://raw.githubusercontent.com/real-stanford/universal_manipulation_interface/main/LICENSE |
| pipelinelicense | 200 | 1554 | accepted | https://raw.githubusercontent.com/ros-perception/image_pipeline/rolling/image_pipeline/package.xml |

## Grepped evidence (accepted sources)

Snippets are direct text matches, not independent verification or claims that all linked content was read. Long page navigation may appear before the relevant body text.

### noise

https://github.com/ethz-asl/kalibr/wiki/IMU-Noise-Model

Pattern: `noise|random walk|Allan`

```text
IMU Noise Model · ethz-asl/kalibr Wiki · GitHub Skip to content Navigation Menu Sign in Products Platform GitHub Repository hosting, code review, and
ull requests 19 ( 19 ) Actions Projects Wiki Security and quality Insights More items IMU Noise Model Jump to bottom Patrick Geneva edited this page Mar 28, 2023 · 11 revisions The Camera-IMU calibration routine needs to know how "nois
ation. Here, you can learn how to set these parameters and how to interpret them. The IMU Noise Model The IMU measurement model used in Kalibr contains two types of sensor errors: $n$ , an additive noise term that fluctuates very rapid
ly ("white noise"), and $b$ , a slowly varying sensor bias. The angular rate measurement $\tilde\omega$ (for one single axis of the gyro, in this case) is t
his model is tractable and often used to model inertial sensors [1], [2]. Additive "White Noise" The rapid fluctuations in the sensor signal are modelled heuristically with a zero-mean, independent, continuous-time white Gaussian noise
e higher $\sigma_g$ is, the more "noisy" your gyro measurements. The parameters gyroscope_noise_density and accelerometer_noise_density in the YAML file specify exactly these noise strengths $\sigma_g$ (gyro) and $\sigma_a$ (accel) for
identical to the discrete-time implementation within Kalibr. Note : This assumes that the noise was filtered with an ideal low-pass filter that filters noise above $f=\frac{1}{2\Delta t}$ (in other words, an ideal decimation stage). Th
s. If you si
```

### allan

https://github.com/ori-drs/allan_variance_ros

Pattern: `Allan|variance|noise`

```text
GitHub - ori-drs/allan_variance_ros: ROS compatible tool to generate Allan Deviation plots · GitHub Skip to content Navigation Menu Sign in Products Platform GitHub Repository hosting, code review, and collaboratio
nother tab or window. Reload to refresh your session. Dismiss alert {{ message }} ori-drs allan_variance_ros Repository navigation Code Issues 15 ( 15 ) Pull requests 5 ( 5 ) Actions Projects Wiki Security and quality Insights More ite
ms allan_variance_ros Public Notifications You must be signed in to change notification settings Fork 127 ( 127 ) Star 697 ( 697 ) You must be signed in to s
tar a repository About ROS compatible tool to generate Allan Deviation plots Topics allan-variance imu Resources Readme BSD-3-Clause license Activity Custom properties Stars 697 stars Watchers 18 watching Forks 127 forks Report repository
te .devcontainer .devcontainer .vscode .vscode bags bags config config figs figs include/ allan_variance_ros include/ allan_variance_ros launch launch scripts scripts src src .gitignore .gitignore CMakeLists.txt CMakeLists.txt LICENSE
age.xml View all files Repository files navigation README BSD-3-Clause license More items Allan Variance ROS ROS package which loads a rosbag of IMU data and computes Allan Variance parameters The purpose of this tool is to read a long
uild and run the tool. See the devcontainer README for more information. How to build The allan_variance_ros folder should be in the src folder of the catkin workspace. For exampl
```

### bno085

https://www.ceva-ip.com/product/bno-9-axis-imu/

Pattern: `BNO08|accelerometer|gyroscope`

```text
bal Offices Careers Contact Us Contact Us --> Home > Products > bno-9-axis-imu 9 axis IMU BNO085/BNO086 Download Product Note Speak to an expert to learn more about Ceva’s core sensor processing software system See how The Solution Ben
elopment of sensor-enabled robotics, AR, VR, and IoT devices. Learn More The Solution The BNO085/BNO086 is a 9 axis System in Package (SiP) which enables rapid development of sensor-enabled Augmented Reality (AR), Virtual Reality (VR),
 Robotics and IoT devices. Co-developed by Bosch and Ceva, it features a high-performance accelerometer, magnetometer, and gyroscope with a low-power 32-bit ARM Cortex M0+ MCU in a small package. Ceva’s sensor hub software pre-integrated on th
e BNO085 provides exceptional 9-Axis and 6-Axis motion tracking to enable exciting sensor applications in diverse consumer and IoT products. The BN
O085 and BNO086 allow operation with application specific external software libraries provided by Ceva, such as those supporting VR controllers and fixed
t such library provides additional advanced capabilities for use with VR controllers. The BNO085/BNO086 provides application specific configurations, features, and performance in a small turn-key component that benefits OEMs through fa
in Features MotionEngine™ 9-Axis and 6-Axis Sensor Fusion Dynamic calibration adjusts for accelerometer and gyroscope bias changes over factors like time and temperature Application-specific features with configurable modes specialized for var
```

### icm42688

https://invensense.tdk.com/products/motion-tracking/6-axis/icm-42688-p/

Pattern: `ICM.42688|gyroscope|accelerometer`

```text
ICM-42688-P | TDK InvenSense InvenSense Log In English Sensors Inertial Sensors Consumer Motion Automotive Motion Industrial Motion Ultrasonic Time o
es / Contact Sales Reps Distributors Custom Sensing Solutions Home | Sensors | Consumer | ICM-42688-P Production ICM-42688-P High-Precision 6-Axis MEMS MotionTracking® Device Product Details 6-Axis High performance IMU supporting highly ac
that helps to reduce system level sensitivity error, improve orientation measurement from gyroscope data, reduce ODR sensitivity to temperature and device to device variation. Read more... Shop Now Contact us Available variants General Fea
k (RTC) input, 19/18 bit data format in FIFO for Gyro/Accel Product Features and Benefits Gyroscope Noise: 2.8 mdps/√Hz & Accelerometer Noise: 70 μg/√Hz Low-Noise mode 6-axis current consumption of 0.88 mA User selectable Gyro Full-scale r
ange (dps): ±15.6/31.2/62.5/125/250/500/1000/2000 User selectable Accelerometer Full-scale range ( g ): ±2/4/8/16 User-programmable digital filters for gyro, accel, and temp sensor Noise and current consumption: APEX Mo
 features and events Datasheet Product details Documentation and Resources Support Center Gyroscope specs Accelerometer specs General specs Show More Product key details ICM-42688-P Shop Now Datasheet Operation - Package Size 0.91 × 2.50 ×
ources, easily filtered by application or product. Datasheet Version Download DS-000347 – ICM-42688-P Datasheet Version 1.9 Download 1.9 App Notes & User Guides Version
Focused claim audit:
g Solutions Home | Sensors | Consumer | ICM-42688-P Production ICM-42688-P High-Precision 6-Axis MEMS MotionTracking® Device Product Details 6-Axis High performance IMU supporting highly accurate external clock input, that helps to reduce system level sens
itivity error, improve orientation measurement from gyroscope data, reduce ODR sensitivity to temperature and device to device variation. Read more... Shop Now Contact us Available variants General Features Pedometer, Til
k (RTC) input, 19/18 bit data format in FIFO for Gyro/Accel Product Features and Benefits Gyroscope Noise: 2.8 mdps/√Hz & Accelerometer Noise: 70 μg/√Hz Low-Noise mode 6-axis current consumption of 0.88 mA User selectable Gyro Full-scale range (dps): ±15.6/31
& applications AR/VR/XR, Robotics, High-Performance IoT Key attribute Highest Performance 6-axis IMU with advanced motion features and events Datasheet Product details Documentation and Resources Support Center Gyroscope specs Accelerometer specs General s
```

### imu

https://github.com/ethz-asl/kalibr/wiki/IMU-Supported-Models

Pattern: `IMU|accelerometer|gyroscope`

```text
tems with non-globally shared overlapping fields of view Visual-Inertial Calibration (CAM-IMU) : Spatial and temporal calibration of an IMU w.r.t a camera-system along with IMU intrinsic parameters Multi-Inertial Calibration (IMU-IMU
) : Spatial and temporal calibration of an IMU w.r.t a base inertial sensor along with IMU intrinsic parameters (requires 1-aiding camera sensor). Rolling Shutter Camera Calibration : Full intrinsic calibration (projection, distor
ve ROS image streams For questions or comments, please open an issue on Github. Tutorial: IMU-camera calibration A video tutorial for the IMU-camera calibration can be found here: (Credits: @indigomega) Tutorial: Start-to-end Guide a
nd Discussion An informal recording of performing static, IMU noise, and dynamic calibration and a discussion of results. Full details can be found on the Calibrating Intel RealSense Cameras page. (Cre
inzmann, Roland Siegwart (2016). Extending kalibr: Calibrating the extrinsics of multiple IMUs and of individual axes. In Proceedings of the IEEE International Conference on Robotics and Automation (ICRA), pp. 4304-4311, Stockholm, S
F THE POSSIBILITY OF SUCH DAMAGE. Wiki pages Pages 18 Loading Home Introduction Tutorial: IMU-camera calibration Tutorial: Start-to-end Guide and Discussion Authors References License (BSD) Loading Bag format Uh oh! There was an erro
a focus Uh oh! There was an error while loading. Please reload this page . Loading Camera IMU calibration Uh oh! There was an error
```

### ati

https://www.ati-ia.com/products/ft/ft_models.aspx?id=Mini45

Pattern: `Mini45|force|torque`

```text
ATI Industrial Automation: F/T Sensor Mini45 简体中文 | English | Español | 日本語 | Português Home NEW Products Products Library Company Contact Us Site Map Robotic Tool Changers Force/Torqu
cy Sales and Support Partners and Integrators Request Info Driving Directions F/T Sensor: Mini45 Home > Products > Force/Torque Sensors > F/T Models > Mini45 Product Advantages The Mini45 has a compact, low-profile design with high capa
ieved version of this transducer is available and offers resistance to a 10 lb cable pull force. E-exit is offered in axial, radial, and right-angle configurations. IP65 and IP68 (10m) Versions Available: The IP65 version of the transd
10 meters. Typical Applications Telerobotics Robotic surgery Robotic-hand research Finger-force research Mini45-E Transducer Ranges and Resolutions Specifications Drawings Documents 3D CAD Models Select a system type. (For more informa
27539 USA Phone:+1 919-772-0115 | Fax:+1 919-772-8259 Home Products Robotic Tool Changers Force/Torque Sensors Utility Couplers Manual Tool Changers Material Removal Tools Compliance Devices Robotic Collision Sensors Library Glossary V
```

### current

https://docs.odriverobotics.com/v/latest/manual/control.html

Pattern: `torque|current|constant`

```text
D5065 270KV D5312s 330KV NEMA 34 Servomotor w/ 16384 CPR Absolute Encoder ODrive Botwheel Torque-Speed Curves MANUAL ODrive Overview System Status LED Per-Axis Commands State Machine Startup Procedure Control Mode System Monitoring Comm
ands Encoder Position and Velocity Motor Current and Torque Estimation General System Commands Saving the Configuration Diagnostics User Storage Hardware Configuration Power System Trip Levels Active
up Harmonic Compensation Controller Structure Position Control loop Velocity Control Loop Current Control Loop Control Modes Filtered Position Control Trajectory Control Circular Position Control Velocity Control Ramped Velocity Control
Torque Control Position Reference Frame Startup-Relative Reference Frame Homed Reference Frame Custom User Reference Frame Absolute Encoder Refere
ncoder ODrive.SpiEncoder ODrive.EncoderEstimator ODrive.Interpolator ODrive.OnboardThermalCurrentLimiter ODrive.BuiltinThermalCurrentLimiter ODrive.OffboardThermistorCurrentLimiter ODrive.AlphaBetaFrameController ODrive.FieldOrientedCont
LES Component Selection Power Supply Voltage Power Other Considerations Motor Kv-number / Torque Constant Current Other considerations Ground Loops The Problem Solutions Reduce Power Wire Isolation Current Limiting Magnetic Encoders Ove
shooting Resistance Calibration Inductance Calibration Calibration lock-in / Lock-in spin current CHANGELOG CHANGELOG [0.6.12-1] - 2026-07-29 Fixed [0.6.12] - 2026-05-05 Added Fixed Changed API migration
Focused claim audit:
D5065 270KV D5312s 330KV NEMA 34 Servomotor w/ 16384 CPR Absolute Encoder ODrive Botwheel Torque-Speed Curves MANUAL ODrive Overview System Status LED Per-Axis Commands State Machine Startup Procedure Control Mode System Monitoring Commands Encoder Position and Velocity Motor Current and Torque Estimation General System Commands Saving the Configuration Diagnostics User Storage Hardware Configuration Power System Trip Levels Active Power Limit Regenerated Power Brake Resistors (S1 Only) Voltage Feedback (S1 Only) Temperature Regulation Thermistors Fans (ODrive Pro Only) Encoders Overview Onboard Encoder Incremental Encoders RS-485 Encoders Hall Effect Encoders SPI Encoders Sensorless Gearbox Configuration Single-Encoder Dual-Encoder Gains Calibration Backup Harmonic Compensation Controller Structure Position Control loop Velocity Control Loop Current Control Loop Control Modes Filtered Position Control Trajectory Control Circular Position Control Velocity Control Ramped Velocity Control Torque Control Position Reference Frame Startup-Relative Reference Frame Homed Reference Frame Custom User Reference Frame Absolute Encoder Reference Frame Absolute Encoder Reference Frame (circular) Index-based Reference Frame Spinout Detection Application Interfaces USB UART Interface Connection Configuration ASCII Protocol Sending Commands Command Format Command Reference Parameter Reading/Writing System Commands ODrive Communication Protocol Packet Format Stream Format CRC Algorithms CAN Protocol Overview Cyclic Messages Watchdog Baudrate & Autobaud CAN-FD Broadcast Discovery & Addressing Bus-off handling DBC Files Interoperability with CANopen Messages Analog Input Overview Endpoint Mapping Velocity Control Example PWM Input Overview Configuration Position Control Example Step/Direction Pinout How to Configure Error/Enable Error Output Enable Input Endstops/Homing Endstop Configuration Example Homing E-Stop ODrive API Reference ODrive ODrive.test_function() ODrive.get_adc_voltage() ODrive.save_configuration() ODrive.erase_configuration() ODrive.reboot() ODrive.enter_dfu_mode() ODrive.enter_dfu_mode2() ODrive.disable_bootloader() ODrive.identify_once() ODrive.get_interrupt_status() ODrive.get_dma_status() ODrive.get_gpio_states() ODrive.set_gpio() ODrive.get_drv_fault() ODrive.clear_errors() ODrive.get_raw_8() ODrive.get_raw() ODrive.get_raw_32() ODrive.get_raw_256() ODrive.vbus_voltage ODrive.ibus ODrive.ibus_report_filter_k ODrive.control_loop_hz ODrive.serial_number ODrive.hw_version_major ODrive.hw_version_minor ODrive.hw_version_variant ODrive.hw_version_revision ODrive.fw_version_major ODrive.fw_version_minor ODrive.fw_version_revision ODrive.commit_hash ODrive.fw_version_unreleased ODrive.bootloader_version ODrive.n_evt_sampling ODrive.n_evt_control_loop ODrive.task_timers_armed ODrive.task_times ODrive.system_stats ODrive.user_config_loaded ODrive.misconfigured ODrive.oscilloscope ODrive.debug ODrive.can ODrive.test_property ODrive.identify ODrive.reboot_required ODrive.issues ODrive.auth ODrive.TaskTimes ODrive.SystemStats ODrive.Issues ODrive.Auth ODrive.HistogramLogger ODrive.CircularLog ODrive.Config ODrive.Can ODrive.Endpoint ODrive.Axis ODrive.BuiltinMotorAxis ODrive.ExternalMotorAxis ODrive.AnticoggingConfig ODrive.HarmonicCompensation ODrive.BrakeResistor ODrive.BrakeResistorConfig ODrive.Motor ODrive.BuiltinMotor ODrive.ExternalMotor ODrive.Mapper ODrive.OnboardEncoder ODrive.Rs485Encoder ODrive.IncrementalEncoder ODrive.HallEncoder
```

### kalibr

https://github.com/ethz-asl/kalibr

Pattern: `calibration|camera|IMU`

```text
GitHub - ethz-asl/kalibr: The Kalibr visual-inertial calibration toolbox · GitHub Skip to content Navigation Menu Sign in Products Platform GitHub Repository hosting, code review, and collaboration Copilo
5.8k ( 5.8k ) You must be signed in to star a repository About The Kalibr visual-inertial calibration toolbox Topics calibration calibration-toolbox camera imu Resources Readme License Activity Custom properties Stars 5.8k stars Watchers 148
 .github/ workflows Schweizer-Messer Schweizer-Messer aslam_cv aslam_cv aslam_incremental_calibration aslam_incremental_calibration aslam_nonparametric_estimation aslam_nonparametric_estimation aslam_offline_calibration aslam_offline_calibra
tion README License More items Introduction Kalibr is a toolbox that solves the following calibration problems: Multi-Camera Calibration : Intrinsic and extrinsic calibration of a camera-systems with non-globally shared overlapping fields of
 view with support for a wide range of camera models . Visual-Inertial Calibration (CAM-IMU) : Spatial and temporal calibration of an IMU w.r.t a camera-system along with IMU intrinsic parameters Multi-Inertial Calibration (IMU-IMU
) : Spatial and temporal calibration of an IMU w.r.t a base inertial sensor along with IMU intrinsic parameters (requires 1-aiding camera sensor). Rolling Shutter Camera Calibration : Full intrinsic calibration (projection, distor
tion and shutter parameters) of rolling shutter cameras. To install follow the install wiki page instruct
```

### kalibrcam

https://github.com/ethz-asl/kalibr/wiki/multiple-camera-calibration

Pattern: `calibration|overlap|camera`

```text
Multiple camera calibration · ethz-asl/kalibr Wiki · GitHub Skip to content Navigation Menu Sign in Products Platform GitHub Repository hosting, code review, and colla
equests 19 ( 19 ) Actions Projects Wiki Security and quality Insights More items Multiple camera calibration Jump to bottom Patrick Geneva edited this page Mar 28, 2023 · 37 revisions The multiple camera calibration tool estimates the i
ntrinsic and extrinsic parameters of a multiple camera-system with the requirement that neighbouring cameras have overlapping fields of view. The image data is provided as a ROS bag containing t
he image streams for all cameras. The calibration routine will go through all images and pick images based on information theoretic measures in order to get a good estimate of the system pa
see 1 ) Arbitrary combinations of projection and distortion models can be combined in one calibration run. Have a look at Supported models page for a list of available models. How to use? 1) Collect images Create a ROS bag containing the raw
m a ROS sensor stream or by using the bagcreater script on a sequence of image files. The camera system is fixed and the calibration target is moved in front of the cameras to obtain the calibration images. It is recommended to lower th
e frequency of the camera streams to around 4 Hz while capturing the calibration data. This reduces redundant information in the dataset and thus lowering the runtime of the calibration. 2) Running the calibration The to
: --bag f
```

### d405

https://www.realsenseai.com/depth-camera-d405/

Pattern: `D405|close|stereo`

```text
D405 - RealSense Products Products → Stereo Depth Cameras D430 Series Widest field-of-view + global shutter, built for fast motion D450 Series Long-range depth with a wide baseline fo
r mobile robots and spatial awareness. D555 Long-range, PoE stereo depth for networked industrial, inspection, and mobile robotics applications. Industrial GMSL 3D Vision D585 Pro Series Our flagship model
with AI-native depth for high-performance physical AI systems. D405 Series Built for precision Physical AI at the point of interaction. D415 Series A standard field of view well suited for high accuracy appl
artners Events & Webinars Shop Company Support ENG 中文 Log In Buy Now RealSense » Products D405 RealSense™ D405. See the world up close. The RealSense™ Depth Camera D405 is a short-range stereo camera providing sub-millimeter accuracy
for your close-range computer vision needs. FOV 87° × 58° Ideal Range 7 cm to 50 cm Global Shutter Small features, high impact RGB without a dedicated RGB
m the depth sensor allows for matched RGB and depth data. Sub-millimeter accuracy RGB The D405 operates at an ideal range of 7 cm to 50 cm with minimum object detection down to <1 mm at 7 cm. Sub-millimeter accuracy The D405 operates
make a smaller camera without sacrificing quality – at 42 mm × 42 mm × 23 mm and 60 g the D405 is smaller than a golf ball. A closer look Precise accuracy lets the RealSense Depth Camera D405 open up a whole new world of use cases tha
t require close range depth sensing. Rob
```

### oak

https://docs.luxonis.com/hardware/products/OAK-D

Pattern: `OAK.D|stereo|RGB`

```text
OAK-D Overview Hardware Software Cloud Search... Press "f" to search Overview Getting Started Platform RVC Features Depth Deployment Camera Senso
mental Specifications Comparisons OAK4 Status Light Switch to navigation View as Markdown OAK-D Shop Datasheet Based on RVC2 Connection USB 2/3 (up to 10 Gbps) Dot projector No Infrared No IMU Yes Sensor 1, 3 - OV9282 Type Monochrome D
 Type Color DFOV / HFOV / VFOV 81° / 69° / 55° Size 1/2.3 Shutter Type Rolling Focus Auto Stereo Looking for more details? Visit specific features at Platform -> Features RVC2 inside This OAK device is built on top of the RVC2 architect
ImageManip node, edge detection , feature tracking . You can also run custom CV functions Stereo depth perception with filtering, post-processing , RGB-depth alignment , and high configurability Object tracking : 2D and 3D tracking with
 ObjectTracker node On-device programming : Run custom logic/tasks on-device ( guide ) Stereo depth perception This OAK camera has a baseline of 7.5 cm (75 mm) - the distance between the left and the right stereo camera. Minimal and
he VPU: Base consumption + camera streaming: 2.5W - 3W AI subsystem consumption: Up to 1W Stereo depth pipeline subsystem: Up to 0.5W Video Encoder subsystem: Up to 0.5W To reduce the power consumption, you can reduce FPS of the whole p
ip damage). To find out more, see our Operating temperature documentation. Similar models OAK-D Lite OAK-D U.S. export classification This product is classified as EAR99 un
Focused claim audit:
p Datasheet Based on RVC2 Connection USB 2/3 (up to 10 Gbps) Dot projector No Infrared No IMU Yes Sensor 1, 3 - OV9282 Type Monochrome DFOV / HFOV / VFOV 81° / 72° / 49° Size 1/4 Shutter Type Global Focus Fixed Sensor 2 - IMX378 Type Color DFOV / HFOV /
 VFOV 81° / 69° / 55° Size 1/2.3 Shutter Type Rolling Focus Auto Stereo Looking for more details? Visit specific features at Platform -> Features RVC2 inside This OAK device is built on top of the RVC2 architectur
le pipeline - that way, subsystems won't be utilized at 100% and will consume less power. IMU This OAK camera has an integrated BNO086, a 9-axis IMU (Inertial Measurement Unit). See IMU node for the API details on how to use it. Operating temperature Th
```

### gemini

https://www.orbbec.com/products/stereo-vision-camera/gemini-2/

Pattern: `Gemini|stereo|depth`

```text
Gemini 2: Stereo Vision Camera | Orbbec Skip to content Products Stereo Vision Camera TOF Camera Structured Light Camera Camera Computer LiDAR Robot-free Data Collection Stereo Vision Camera Gemini 338Le Gemini
338Lg Gemini 305 Gemini 305g Gemini 345Lg Gemini 435Le Gemini 330 Series Enhanced Depth Filter Gemini 335 Gemini 336 Gemini 335L Gemini 336L Gemini 335Lg Gemini 335Le Gemini 215 Gemini 2 Gemini 2 L Gemini 2 XL TOF Camera Femto
lity Disclosure Policy Company News Blog Technology Ecosystem Careers Contact Us Products Stereo Vision Camera TOF Camera Structured Light Camera Camera Computer LiDAR Robot-free Data Collection Stereo Vision Camera Gemini 338Le Gemini
338Lg Gemini 305 Gemini 305g Gemini 345Lg Gemini 435Le Gemini 330 Series Enhanced Depth Filter Gemini 335 Gemini 336 Gemini 335L Gemini 336L Gemini 335Lg Gemini 335Le Gemini 215 Gemini 2 Gemini 2 L Gemini 2 XL TOF Camera Femto
ers Contact Us Store Language English 简体中文 日本語 한국어 Language English 简体中文 日本語 한국어 Products Stereo Vision Camera Gemini 338Le Gemini 338Lg Gemini 305 Gemini 305g Gemini 345Lg Gemini 435Le Gemini 330 Series Enhanced Depth Filter Gemini 335
 Gemini 336 Gemini 335L Gemini 336L Gemini 335Lg Gemini 335Le Gemini 215 Gemini 2 Gemini 2 L Gemini 2 XL TOF Camera Femto Bolt Femto Mega Femto Mega I Structured Light Camera Astra 2 Astra Mini S Pro Astra Mini Pro Camera Comput
pany News Blog Technology Careers Contact Us Store Language English 简体中文 日本語 한국어 Products Stereo Vision Camera Gemini 338Le Gemi
```

### zed

https://www.stereolabs.com/en-us/products/zed-2

Pattern: `ZED|stereo|depth`

```text
ZED 2 - AI Stereo Camera | Stereolabs Skip to content Meet the New ZED Box 2 Series – Physical AI Power for Robotics. Up to 2,070 TFLOPS, 8× GMSL inputs & Full I/O. Learn more Products ZED X One Learn Order ZED
 X Series Learn Order ZED Series Learn Order Digital Lidar Learn Talk to an expert ZED Box 2 Series Learn Order SDK Learn Download Solutions By machine Robotic Arms Humanoid Robots Forklifts AMRs Tractors & AGbots By Segment P
s Parcel counting Dimensioning Pallet occupancy monitoring Integrations Partner Ecosystem ZED Box 2 Series Supercomputers for Physical AI and Robotics Powered by NVIDIA® Jetson Thor™ and Orin™ NX platforms, the NEW ZED Box 2 is a pow
erful computer designed for Perception. Learn more Ouster + Stereolabs Developers Get Started SDK Overview SDK Downloads ZED X Drivers Resources Documentation API Reference Code Samples Integrations Support
tal Lidar Embedded PC Accessories Kits Shop All There are currently no items in your bag. ZED 2 Versatile stereo camera for spatial perception Order now Multiple generations, infinite solutions. With unbeatable depth sensing and ease
-of-use at its core, the ZED family is the go-to choice for teams working at the edge of robotics, digital twins and immersive experiences. $499 ZED 2i The world’s most
 powerful camera for depth perception, motion and AI, the ZED 2i is a durable and versatile stereo camera that can be deployed in most environments. 120mm Stereo Baseline USB 3.1 Built-in IMU, baromete
r & magnetomete
```

### rplidar

https://www.slamtec.com/en/Lidar/A1

Pattern: `RPLIDAR|360|laser`

```text
RPLIDAR-A1 Cost-Effective 360° Lidar Sensor | SLAMTEC Home Products LIDAR Robot Platform 3D Localization & Mapping Solution 2D Localization & Mapping Solution Developmen
t Software LPX Industrial Lidar LPX-E3 LPX-T1 TOF Lidar RPLIDAR C1 RPLIDAR S3 RPLIDAR S2 Triangulation Lidar RPLIDAR A3 RPLIDAR A2 RPLIDAR A1 Embodied Intelligence Robot Platform Poseidon 48V Hermes Industrial Robot Platform
-> Contact Us Eng 中文 한국어 Home Products LIDAR LPX Industrial Lidar LPX-E3 LPX-T1 TOF Lidar RPLIDAR C1 RPLIDAR S3 RPLIDAR S2 Triangulation Lidar RPLIDAR A3 RPLIDAR A2 RPLIDAR A1 Robot Platform Embodied Intelligence Robot Platform Poseidon
it Development Software Cases News Buy Support About Us Partner --> Contact Us 中文 Eng 한국어 RPLIDAR A1 Overview Apps Spec Download Buy RPLIDAR A1 is based on laser triangulation ranging principle and uses high-speed vision acquisition and
veloped by Slamtec. The system measures distance data in more than 8000 times per second. 360 Degree Omnidirectional Laser Range Scanning The core of RPLIDAR A1 runs clockwise to perform a 360 degree omnidirectional laser range scann
e sample rate of LIDAR directly decides whether the robot can map quickly and accurately. RPLIDAR improves the internal optical design and algorithm system to make the sample rate up to 8000 times,which is the highest in the current econ
djust the scan rate by alternating the motor PWM signal Plug and Play Just connecting the RPLIDAR and a computer via a micro USB cable, users can use the R
```

### livox

https://www.livoxtech.com/mid-360

Pattern: `360|LiDAR|field`

```text
Livox Mid-360 Products Developer Application Downloads Newsroom Support Become a Dealer Contact Us MID-360 Specs Downloads FAQ Contact Us key::v4.mid360.
title Small But Mighty Mid-360 is the latest generation of Livox LiDAR for low speed robotics. This new product inherits the cost-effectiveness of the Livox Mid series and delivers 3D perception in 360 degrees.
 Compact and lightweight, this LiDAR module is easy to install. The Mid-360 is optimized based on the navigation and obstacle avoidance requirements of mobile robots. This allows you to use the LiDAR with algorithms
 to deliver a wide range of functions such as SLAM and obstacle avoidance. 360° * 59° FOV [1] 0.1m Min. Detection Range [2] 40m @10% Reflectivity [3] 40-line Point Cloud Density 65*65*60 L × W × H (mm) 265g Weight 360°
 Super-Wide FOV Unlike conventional mechanical LiDAR, the Mid-360 is powered by Livox's unique rotating mirror hybrid-solid technology. And Mid-360 is the first to improve the horizontal FOV to 360° and th
e vertical FOV to 59°. The omnidirectional ultra-large FOV coverage provided by the Mid-360 LiDAR helps mobile robots accurately perceive their surroundings in all directions. This provides the basis on which mobile robots can form
ulate plans and make decisions. replay Smaller and Lighter The miniature Mid-360 unlocks a new world of possibility in robot design. For the first time 3D LiDAR can be seamlessly integrated without compromise. Greater Pe
rformance with Reduced Blind Spot Short
```

### ouster

https://ouster.com/products/hardware/os1-lidar-sensor

Pattern: `OS1|lidar|field`

```text
OS1: High-Res Mid-Range Lidar Sensor for Automation & Security | Ouster Sensors OS Sensors ZED Cameras Compute Quicklinks Ouster + Stereolabs Distribution Partners Softw
 Partners Developers Developer Forum SDK Ouster Studio Downloads Store Talk to Sales Menu OS1 A mid-range sensor balancing resolution and range, making it a versatile choice for security, smart infrastructure, and autonomous vehicles
. Discover more Technical Specifications & Details OS1 OS0 OSDome OS1 Max OS1 90 m Range @ 10% 250 m Maximum Range 0.0 m Minimum Range 45° Vertical FoV 10.4 Million Points per Second Request a Quote Comparing across t
color 3D vision required to bring Physical AI to life. See All Sensors Long-Range FOV 45° OS1 Max The long-range Rev8 OS1 MAX delivers industry-leading price, performance, and automotive-grade reliability for the most rugged conditio
ns. Mid-Range FOV 45° OS1 A mid-range sensor balancing resolution and range, making it a versatile choice for security, smart infrastructure, and autonomous vehicles
. Ultra-Wide FOV 90° OS0 An ultra-wide field-of-view sensor designed for short-range, high-precision perception in robotics, warehouse automation, and industrial applications. Hemisphe
rical FOV 180° OSDome Hemispherical lidar sensor with a 180º field of view, ideal for security, smart infrastructure, and autonomous system awareness. Now in Native Color From ultra-wide hemispherical cover
color 3D vision required to bring Physical AI to life. See All Sensors Long-Range FOV
```

### ultrasonic

https://learn.adafruit.com/ultrasonic-sonar-distance-sensors/overview

Pattern: `ultrasonic|sound|distance`

```text
Overview | Ultrasonic Sonar Distance Sensors | Adafruit Learning System --> Skip to main content Skip to article content Shop Learn Blog Forums IO LIVE! AdaBox toggle menu Sear
s Wearables Explore Groups to get your gears turning Explore Groups New Guides Playground Ultrasonic Sonar Distance Sensors Overview Ultrasonic Sonar Distance Sensors Find your distance with the power of sonar! by Kattni Rembor published De
View Guide Products view all Your browser does not support the video tag. Primary HC-SR04 Ultrasonic Sonar Distance Sensor + 2 x 10K resistors $3.95 Add to Cart View product details 42 Beginner Product guide 💖 3 Overview If you're like me,
atches up with our desires, we'll just have to make do with these handy HC-SR04 and US100 Ultrasonic Sonar Distance Sensors and a pair of flippers. These ubiquitous sensors are really common in robotics projects, but they can also be used f
that you can ready with your 3V device. The US-100 is very similar to the popular HC-SR04 ultrasonic sensors, and even looks the same, but has a few extra tricks This sensor can run from 3-5V so you don't need any logic level shifters or di
ith the sensor. In UART mode, send 0x55 and read back two bytes (16 bit value) that is mm distance, or 0x50 to read the temperature in degrees C. Handy if you want to use with a computer and a USB-serial converter, or some other device th
st edited March 08, 2024 Pinouts Related Guides Jack-o-Theremin By Sophy Wong beginner 12 Distance Measurement with Ult
```

### ir

https://www.pololu.com/product/136

Pattern: `infrared|10|80`

```text
Pololu - Sharp/Socle GP2Y0A21YK0F Analog Distance Sensor 10-80cm Sensors » Proximity Sensors and Range Finders » Sharp Distance Sensors » Sharp/Socle GP2Y0A21YK0F Analog Distance Sensor 10-80cm New! Pol
ional: desired quantity Remove Save Price break Unit price (US$) 1 12.95 5 12.17 25 11.44 100 10.76 Quantity: backorders allowed Add to cart Add to list Get price notification Notify me Cancel on any price change on any price drop a
r motion sensing to your robot or any other project. With a detection range of 4″ to 32″ (10 cm to 80 cm) and an analog voltage indicating the distance, this sensor is very easy to use. Compare all products in Sharp Distance Sensors
ith 3-Pin JST PH Connectors or Classic TI-RSLK Parts and Accessories . Description Specs (10) Pictures (3) Resources (1) FAQs (0) On the blog (3) Distributors (3) Overview The Sharp distance sensors are a popular choice for many pro
 comparator for threshold detection. The detection range of this version is approximately 10 cm to 80 cm (4″ to 32″). The GP2Y0A21 uses a 3-pin JST PH connector that works with our 3-pin JST PH cables for Sharp distance sensors (not
is sensor draws current in large, short bursts, and the manufacturer recommends putting a 10 µF capacitor or larger across power and ground close to the sensor to stabilize the power supply line) Distance measuring range: 10 cm to 8
tage Output voltage differential over distance range: 1.9 V (typical) Update period: 38 ± 10 ms Size: 44.5 mm × 18.9 mm × 13.5 mm (
```

### kalibrimu

https://github.com/ethz-asl/kalibr/wiki/camera-imu-calibration

Pattern: `temporal|spatial|calibration`

```text
Camera IMU calibration · ethz-asl/kalibr Wiki · GitHub Skip to content Navigation Menu Sign in Products Platform GitHub Repository hosting, code review, and colla
uests 19 ( 19 ) Actions Projects Wiki Security and quality Insights More items Camera IMU calibration Jump to bottom Patrick Geneva edited this page May 24, 2023 · 35 revisions The camera-imu calibration tool estimates the spatial and tempor
 an intrinsically calibrated IMU. Image and IMU data has to be provided in a ROS bag. The calibration parameters are estimated in a full batch optimization using splines to model the pose of the system. Detailed information about the approac
h can be found in the following papers: (see 1 , 2 ) Tutorial: IMU-camera calibration A video tutorial for the IMU-camera calibration can be found here: (Credits: @indigomega) How to use it 1) Requirements The intrinsic param
eater script on a list of image files and a CSV file containing the IMU measurements. The calibration target is fixed in this calibration and the camera-imu system is moved in front of the target to excite all IMU axes. It is important to en
sure good and even illumination of the calibration target and to keep the camera shutter times low to avoid excessive motion blur. Good results have been obtained by using a camera rate of 2
 good illumination ensure low jitter timestamps in same clock WARNING: If you are using a calibration target with symmetries (checkerboard, circlegrid), movements which could lead to flips in t
Focused claim audit:
dited this page May 24, 2023 · 35 revisions The camera-imu calibration tool estimates the spatial and temporal parameters of a camera system with respect to an intrinsically calibrated IMU. Image and IMU data has to be provided in a ROS bag. The calibration
ra --bag [filename.bag] --cam [camchain.yaml] --imu [imu.yaml] --target [target.yaml] The temporal calibration is turned on by default and can be disabled using the --no-time-calibration argument. More information about options is available using the help ar
t in an academic publication. Paul Furgale, Joern Rehder, Roland Siegwart (2013). Unified Temporal and Spatial Calibration for Multi-Sensor Systems. In Proceedings of the IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS), Tokyo, Japa
n. Paul Furgale, T D Barfoot, G Sibley (2012). Continuous-Time Batch Estimation Using Temporal Basis Functions. In Proceedings of the IEEE International Conference on Robotics and Automation (ICRA), pp. 2088–2095, St. Paul, MN. Wiki pages Pages 18 Loadin
```

### lidarcal

https://github.com/koide3/direct_visual_lidar_calibration

Pattern: `calibration|camera|LiDAR`

```text
GitHub - koide3/direct_visual_lidar_calibration: A toolbox for target-less LiDAR-camera calibration [ROS1/ROS2] · GitHub Skip to content Navigation Menu Sign in Products Platform GitHub Repository hosting, code review, and collaboration Co
 window. Reload to refresh your session. Dismiss alert {{ message }} koide3 direct_visual_lidar_calibration Repository navigation Code Issues 71 ( 71 ) Pull requests 3 ( 3 ) Actions Projects Security and quality Insights More items dir
ect_visual_lidar_calibration Public Notifications You must be signed in to change notification settings Fork 241 ( 241 ) Star 1.6k ( 1.6k ) You must be signed in to sta
r a repository About A toolbox for target-less LiDAR-camera calibration [ROS1/ROS2] koide3.github.io/direct_visual_lidar_calibration/ Topics calibration camera lidar nid ros ros2 Resources Readme Activity Stars
 Name Name Last commit message Last commit date .github .github cmake cmake direct_visual_lidar_calibration direct_visual_lidar_calibration docker docker docs docs include include scripts scripts src src thirdparty thirdparty .clang-fo
ml package.xml View all files Repository files navigation README More items direct_visual_lidar_calibration This package provides a toolbox for LiDAR-camera calibration that is: Generalizable : It can handle various LiDAR and camera pr
ojection models including spinning and non-repetitive scan LiDARs, and pinhole, fisheye, and omnidirectional projection cameras. Target-less : It does not require a calib
```

### ptp

https://www.linuxptp.org/

Pattern: `IEEE|1588|PTP`

```text
Welcome to The Linux PTP Project LinuxPTP Project About Install Getting Involved Documentation Donate Your Donations Help Support LinuxPTP -- Donate Today! Welcome to The Linux PTP
Project This software is an implementation of the Precision Time Protocol (PTP) according to IEEE standard 1588 for Linux. The project’s dual design goals are to provide a robust implementation of the standard, and to
 and other platforms is not a goal. Network Time Foundation provides support for the LinuxPTP Project and hosts the PTP/SyncE Consortium . Learn more about the Foundation’s work at https://www.nwtime.org . Download Linux PTP Report a

Focused claim audit:
ware is an implementation of the Precision Time Protocol (PTP) according to IEEE standard 1588 for Linux. The project’s dual design goals are to provide a robust implementation of the standard, and to use the most relevant and modern Application Programm
```

### trigger

https://docs.baslerweb.com/triggered-image-acquisition

Pattern: `trigger|exposure|hardware`

```text
Triggered Image Acquisition | Basler Product Documentation Skip to content STAGING SERVER DEVELOPMENT SERVER Basler Product Documentation Draft Ver
sion Triggered Image Acquisition Your camera model: None selected Home Cameras Lenses Illumination Acquisition Cards Accessories Software This topic has
 Device Temperature Digital Shift Dual ROI Encoder Control Error Codes Event Notification Exposure Auto Exposure Mode Exposure Overlap Time Max Exposure Start Delay Exposure Time Feature Sequence (dart, pulse) Flat-Field Correction Freque
Test Images Test Patterns Timer Timestamp Tonal Range Tonal Range Auto Transfer Bit Depth Triggered Image Acquisition Triggered Image Acquisition In this topic Using the Feature Hardware and Software Triggering Configuring Triggered Imag
e Acquisition Example 1: Basic Hardware Triggering Example 2: Advanced Hardware Triggering Example 3: Software Triggering Example 4: Triggering a Series of Images Trigger Types Frame and Line Triggers Frame Burst Triggers Expos
ure Triggers Trigger Sources Hardware Trigger Sources Software Trigger Sources Trigger Activation Modes Trigger Delay Specifics Sample Code Two-Wire Interface User-Defined Data User Output Value User Sets Vignetting Correction
 Installation Installation Overview Hardware Installation (CoaXPress Cameras) Hardware Installation (GigE Cameras) Hardware Installation (GMSL Cameras) Hardware Installation (USB 3.0 Cameras) Network Configuration (GigE Camera
MSL Cameras) Installing Camera Enableme
```

### synch

https://docs.baslerweb.com/precision-time-protocol

Pattern: `PTP|timestamp|synchron`

```text
t Precision Time Protocol Precision Time Protocol In this topic Using the Feature Why Use PTP How It Works Timestamp Synchronization Enabling PTP Clock Synchronization Configuring PTP Clock Synchronization Priority 1 PTP Delay Mechan
ism Network Mode PTP Management One-Step or Two-Step Clock Checking the Status of the PTP Clock Synchronization What's In A Latched Data Set? External Links Sample Code Processed Raw Enable Remove Parameter Limits Resulting Acqui
ding Correction Software Signal Pulse Spatial Correction Stacked ROI Stacked Zone Imaging Synchronous Free Run Temperature State TDI Test Images Test Patterns Timer Timestamp Tonal Range Tonal Range Auto Transfer Bit Depth Triggered Image
Scan 3d Calibration Offset Scan 3d Focal Length Scan 3d Invalid Data Value Spatial Filter Synchronous Free Run Temperature State Temporal Filter Thermal Drift Correction Trigger Thermal Drift Stabilization Web Server Enable Camera Operati
s Interface KUKA Ethernet KRL Interface gRPC Image Stream Interface OPC UA Interface Time Synchronization Maintenance Maintenance General Lens Cleaning Camera Calibration Creating and restoring backups of settings Updating the Firmware Re
lumination Acquisition Cards Accessories Software In this topic Using the Feature Why Use PTP How It Works Timestamp Synchronization Enabling PTP Clock Synchronization Configuring PTP Clock Synchronization Priority 1 PTP Delay Mechan
ism Network Mode PTP Management One-Step or Two-Step Clock Checking the Status of the
```

### gazebo

https://gazebosim.org/docs/harmonic/sensors/

Pattern: `IMU|lidar|sensor`

```text
Sensors — Gazebo harmonic documentation Skip to main content Back to top Ctrl + K This is documentation for Gazebo Harmonic , an older but still s
e Install Troubleshooting ROS/Gazebo Installation ROS 2 Gazebo Vendor Packages For Users Simulation Tutorials Building your own robot Moving the robot SDF worlds Sensors Actors Understanding the GUI Manipulating Models Model Insertio
ntegration overview Launch Gazebo from ROS 2 Use ROS 2 to interact with Gazebo Use ROS 2 Simulation Interfaces to Interact with Gazebo Use ROS 2 to spawn a Gazebo model ROS 2 interoperability ROS 2 integration template Web Visualizat
e Library Reference cmake common fuel_tools gui launch math msgs physics plugin rendering sensors sim tools transport utils sdformat Simulation Tutorials Sensors Sensors # Note: This tutorial is a continuation from the Moving the robot
tutorial . In this tutorial we will learn how to add sensors to our robot and to other models in our world. We will use three different sensors: an IMU sensor, a Contact sensor and a Lidar sensor. We
ins in use here . You may also find an extensive set of world examples with many possible sensors and actuation capabilities in gz-sim/examples/worlds for individual examples. The full set of sensors can be found in the gz-sensors libra
which does not currently contain one, the default plugins are not loaded. Before adding a sensor, make sure to add in a couple of logical defaults to your world so that it is possible to continue to use the GZ
```

### gazebonoise

https://gazebosim.org/api/sensors/8/classgz_1_1sensors_1_1GaussianNoiseModel.html

Pattern: `Gaussian|noise|Bias`

```text
Gazebo Sensors: GaussianNoiseModel Class Reference Gazebo Sensors API Reference 8.3.0 insert_drive_file Tutorials library_books Classes toc Namespaces insert_drive_file
: Enumerator List Members Functions Typedefs Variables Enumerations Enumerator gz sensors GaussianNoiseModel List of all members | Public Member Functions GaussianNoiseModel Class Reference Gaussian noise class. More... #include < gz/sens
ors/GaussianNoiseModel.hh > Public Member Functions GaussianNoiseModel () Constructor. More... virtual ~GaussianNoiseModel () Destructor. More... double ApplyImpl (double _in, double _dt) override Apply no
t data value. This gets overriden by derived classes, and called by Apply. More... double Bias () const Accessor for bias. More... virtual void Load (const sdf::Noise &_sdf) override Load noise parameters from sdf. More... double Mean
ouble StdDev () const Accessor for stddev. More... Public Member Functions inherited from Noise Noise ( NoiseType _type) Constructor. This should not be called directly unless creating an empty noise model. Use NoiseFactory::NewNoiseMo
del to instantiate a new noise model. More... virtual ~Noise () Destructor. More... double Apply (double _in, double _dt=0.0) Apply noise to input data value. More... virtual void SetCustomNoiseCallba
ck ( std::function < double(double, double)> _cb) Register a custom noise callback. More... NoiseType Type () const Accessor for NoiseType. More... Detailed Description Gaussian noise class. Constructor & Destruc
```

### isaac

https://docs.isaacsim.omniverse.nvidia.com/latest/sensors/index.html

Pattern: `sensor|Lidar|Camera`

```text
Sensors — Isaac Sim Documentation Skip to main content Back to top Ctrl + K Isaac Sim Documentation Choose version Search Ctrl + K discord github
saac Sim 6.0 Migration Strategy Project Migration Audit Core API to Core Experimental API Sensor Timing and RTX Lidar Asset Migration Camera Sensors RTX Sensors Physics Sensors PhysX Lidar PhysX Generic Sensor PhysX Lightbeam Replicator
t Path Migration URDF, MJCF, and Robot Asset Pipeline Changes ROS 2 OmniGraph Nodes ROS 2 Sensor Graph Migration ROS 2 Workspace Package Migration Benchmark Services Migration Removed Tools and Replacements Extension Template Generator
 Assets Aerial Robot Assets Isaac Sim Simple Robot Assets Mobile Manipulator Robot Assets Sensor Assets Camera Sensors Depth Sensors RTX Lidar Sensors RTX Radar Sensors Tactile Sensors IMU Sensors Prop Assets Environment Assets Third-Pa
ic Stage and Robot Setup Stage Setup Assemble a Simple Robot Articulate a Basic Robot Add Camera and Sensors Rig a Mobile Robot Setup a Manipulator Setup a Manipulator Configure a Manipulator Generate Robot Configuration File Pick and P
pector Physics Static Collision Extension Simulation Data Visualizer Physics Debug Window Sensor Simulation Camera Sensors Depth Sensors Structured Light Cameras Authoring a Camera Sensor USD Asset RTX Sensors RTX Lidar Sensor RTX Radar
 Sensor RTX Acoustic Sensor RTX Sensor Annotators RTX Sensor Non-Visual Materials Multi-Tick Rendering Creating Custom RTX Sensor Profiles Physics-based Sensors Articu
```

### prophesee

https://www.prophesee.ai/event-based-vision/

Pattern: `event|pixel|change`

```text
What Is Event-Based Vision? Neuromorphic Vision | Prophesee Skip to content Industries All Industries Defense & Aerospace Industry Robotics & Autonomous
tion Kit Embra Platform & services Hearth Services & Integration Custom Design Technology Event-Based Vision Sensors Data & AI architecture Research Library Inventors Community Resources Developer Hub Log in / Support Company About New
sroom Ecosystem Careers Contact us Event-Based Vision technology What is Event-Based Vision? The world does not move in frames. Download the white paper Explore Event-Based Vision use cases Event-Based Vision is a tech
uires visual information. This neuromorphic machine-vision approach captures visual scene changes as they happen, while ignoring static parts of the scene. Instead of recording complete images at fixed intervals, each pixel of an Event-
Based Vision sensor responds independently and autonomously to local changes in light and generates precisely time-stamped events. Together, these events create a sparse yet highly informative, continuous stream of
ption . For more than a decade, Prophesee has pioneered and advanced this approach – from pixel-level sensing to complete perception systems – enabling machines to perceive what matters and act at the speed of change . How it works Why
 it matters Where it’s used Why Prophesee FAQs How does Event-Based Vision work? Inspired by how the human eye acquires visual information, Event-Based Vision works fundamentally differently from conve
Focused claim audit:
 static parts of the scene. Instead of recording complete images at fixed intervals, each pixel of an Event-Based Vision sensor responds independently and autonomously to local changes in light and generates precisely time-stamped events. Together, these
ption . For more than a decade, Prophesee has pioneered and advanced this approach – from pixel-level sensing to complete perception systems – enabling machines to perceive what matters and act at the speed of change . How it works Why it matters Where it
etween frames . An event camera does not capture the complete scene again and again. Each pixel responds independently when a change in light crosses a defined threshold . It generates an event recording where and when the change occurred, and whether the
s between them unrepresented. Event-Based Vision responds instantly as the scene changes, pixel by pixel . Instead of waiting for the next frame, the pixels capture the movement as a precise stream of events, creating a time-continuous representation of t
ata does an event camera produce? Each event contains four essential values: X Horizontal pixel position Y Vertical pixel position T Timestamp in microseconds P Polarity: an increase or decrease in light intensity Computer-vision algorithms and AI models
ed Vision Generates data continuously as the scene changes Frame-based vision Samples all pixels simultaneously using a global or rolling shutter to capture each frame Event-Based Vision Allows each pixel to respond autonomously and asynchronously Frame-b
ased vision Repeats information from unchanged areas Event-Based Vision Keeps inactive pixels silent Frame-based vision Represents motion through a sequence of static snapshots Event-Based Vision Records continuous time-domain information without a fix
lumination to capture rapid movement Event-Based Vision Records precise points in time at pixel-level without an exposure window, revealing details between the frames with zero motion blur What are the advantages of Event-Based Vision? Capture fleeting mo
rophesee advances Event-Based Vision across the complete perception chain – from patented pixel architecture to the software and intelligence that transform events into system-level information machines can interpret and act on. 01 Sense change Scene chan
ge → Independent pixel events Pixels, sensors, camera modules and evaluation systems generate precise, asynchronous event data. Patented pixel architecture · Sensors · Camera modules Y X T 02 Pro
ave a frame rate? No. An event camera does not capture visual data at a fixed frame rate. Pixels generate events asynchronously when they detect pre-defined changes in light. How is an event camera different from a high-speed camera? A high-speed camera s
requirements and processing demand. An event camera reports changes independently at each pixel, providing precise temporal information without repeatedly capturing the entire scene. Why is event data blur-free? A conventional image integrates light over
an exposure period, allowing moving objects to blur across multiple pixel positions. An event records the exact time at which a local brightness change crosses a threshold. It is not formed through a light exposure process. An event
```

### metavision

https://docs.prophesee.ai/stable/index.html

Pattern: `Metavision|event|SDK`

```text
Welcome to Metavision SDK — Metavision SDK Docs 5.3.1 documentation METAVISION INTELLIGENCE BUY PRODUCTS PROPHESEE CONTACT Metavision SDK Docs 5.3.1 Discover Installation Modules and Packaging Metavision Studio Event-B
ing File Formats Hardware Supported Products Discontinued Products Biases Pixel Selection Event Signal Processing Timing Interfaces Cameras Synchronization Optics calculator Resources Release Notes Camera Plugin Upgrade Guide Open Sour
ce Licenses FAQ Glossary Index Metavision SDK Docs » Welcome to Metavision SDK Welcome to Metavision SDK  Discover Metavision SDK v5.3.1 , an all-in-one toolkit for event-based vision, from powerful visualization tools, such as Metavision
xt-generation vision applications. Get Started  Follow our installation guides to set up Metavision SDK and stream data from a live event-based camera. No camera yet? No problem! You can replay our data recordings and datasets to experienc
e the power of event-based vision. For the best experience, try slow-motion playback in Metavision Studio . Want to dive deeper? Explore the Event-Based Vision technology and products through our series of Training Videos . Ready to build
t started with development . 🌟 New here? 🔍 Exploring 🚀 Developing Start your journey into event-based vision What is event-based vision ? Recordings and datasets Data visualization with Metavision Studio Dive deeper with examples and v
 for full access. With these tools at your disposal, you can unlock the full potential
```

### inivation

https://inivation.com/

Pattern: `event|vision|neuromorphic`

```text
iniVation – Neuromorphic vision systems Skip to content Technology Solutions Buy Buy Distributors Developer Developer Tutorials DVS Videos Company Company News Contact Con
tact Subscribe Search for: Home Christy Aerne 2023-09-07T10:41:15+02:00 Extreme Machine Vision High-performance neuromorphic vision systems for demanding real-time applications iniVation is a world leader in neuromorphic vision system
inspired intelligent technology offers unprecedented advantages over conventional machine vision systems: ultra-low response latency, low data rates, high dynamic range, and ultra-low power consumption. Founded by the inventors of event
-based vision, iniVation combines decades of world-leading R&D experience with the world’s largest community of customers and partners across multiple in
now in use at over 700 organizations in over 40 countries worldwide. We created the first neuromorphic systems to be used in space, and also the first to be used in Antarctica. Technology Solutions Buy Developer News A SynSense Group company
```

### radar

https://www.ti.com/product/IWR6843

Pattern: `60|64|radar|antenna`

```text
parametric-filter Switches & multiplexers parametric-filter Wireless connectivity mmWave radar sensors parametric-filter Humidity sensors parametric-filter Magnetic sensors parametric-filter mmWave radar sensors parametric-filter Opti
rametric-filter Specialty sensors parametric-filter Temperature sensors Industrial mmWave radar sensors parametric-filter Automotive mmWave radar sensors parametric-filter Industrial mmWave radar sensors Home Sensors mmWave radar senso
rs Industrial mmWave radar sensors IWR6843 ACTIVE Single-chip 60-GHz to 64-GHz intelligent mmWave sensor integrating processing capability Order now Data sheet document-pdfAcrobat IWR6843, IWR6443 Single-Chip 60 to
 64GHz mmWave Sensor datasheet (Rev. F) PDF | HTML User guides document-pdfAcrobat IWR14xx/16xx/18xx/68xx/64xx Industrial Radar Family Technica
 the compared device. NEW IWRL6844 ACTIVE Single-chip low-power high-performance 57GHz to 64GHz industrial mmWave radar sensor Newer low power variant is being released to market IWR6843 ACTIVE Data sheet Order now Product details T
ype IC Frequency range 60 - 64 GHz Number of receivers 4 Number of transmitters 3 ADC sampling rate (ksps) 25000 TX power (dBm) 12 Arm CPU Arm Cortex-R4F at 200 MHz Hardw
are accelerators Radar hardware accelerator Edge AI enabled Yes DSP type 1 C67x DSP @ 600MHz Interface type CAN-FD, I2C, LVDS, QSPI, SPI, UART RAM (kByte) 1792 Operating temperature range (°C) -40 to 105 TI functional safety cat
are IP protection Power supply solut
```

### radarisk

https://www.ti.com/tool/IWR6843ISK

Pattern: `IWR6843|antenna|evaluation`

```text
IWR6843ISK Evaluation board | TI.com Home Design & development IWR6843ISK IWR6843 evaluation module for single-chip 60GHz long-range antenna mmWave sensor Order now IWR6843ISK Order now Overview IWR6843ISK is an easy-to-use 60 GHz m
mWave sensor evaluation kit based on IWR6843 device with long-range antenna. The IWR6843ISK may be used to evaluate the IWR6843 and IWR6443 devices. This board enables access to point-cloud data and power over USB interface. Thi
nterface. MMWAVEICBOOST enables software development and trace capabilities via TI’s CCS. IWR6843ISK paired with MMWAVEICBOOST can interface with the MCU LaunchPad™ development kit ecosystem. Features 60- to 64-GHz mmWave sensor 4 receiv
e (RX) 3 transmit (TX) antenna with 120° azimuth field of view (FoV) and 30° elevation FoV Direct interface with MMWAVEICBOOST and DCA1000 Supports 60-pin high-speed inte
rface for host-controlling interface Onboard capability for power-consumption monitoring IWR6843ISK Warranty card (disclaimer sheet) Quick Start Guide Industrial mmWave radar sensors IWR6443 — Single-chip 60-GHz to 64-GHz intelligent mm
Wave sensor integrating MCU and hardware accelerator IWR6843 — Single-chip 60-GHz to 64-GHz intelligent mmWave sensor integrating processing capability Download View video with transcript Video Order
documentation HARDWARE AND SOFTWARE PACKAGE Get started with running application demos on IWR6843 View package Get started with running application demos on IWR6843 close Explore mmWave sens
```

### reskin

https://reskin.dev/

Pattern: `magnetic|skin|ReSkin`

```text
ReSkin: versatile, replaceable, lasting tactile skins --> ReSkin: versatile, replaceable, lasting tactile skins Raunaq Bhirangi* CMU Tess Hellebrekers* FAIR Carmel Majidi CMU Abhinav Gupta CMU/FAIR * equa
ver time and across samples, inhibiting their ability to be long-lasting and replaceable. ReSkin is a tactile soft sensor that leverages machine learning and magnetic sensing to offer a low-cost, diverse and compact solution for long-te
rm use. Magnetic sensing separates the electronic circuitry from the passive interface, making it easier to replace interfaces as they wear out while allowi
rformance enhancement with small, inexpensive data collection procedures. We believe that ReSkin opens the door to more versatile, scalable and inexpensive tactile sensation modules than existing alternatives. In The News Talk --> Sourc
e Code The reskin library can be found on GitHub at this link . The trained model from the paper can be downloaded here . here . All the code for the CoRL pa
des] --> Design and Fabrication Materials used in the Fabrication video: Smooth-On Dragon Skin 10 NV Magnequench MQP-15-7-20065(~80 mesh) Bonded Neo Powder Thin plastic film (link is representative) here . All the code for the CoRL pa
 and Bibtex Citation Raunaq Bhirangi, Tess Hellebrekers, Carmel Majidi and Abhinav Gupta. ReSkin: versatile, replaceable, lasting tactile skins . CoRL 2021. [Bibtex] [arXiv] [Bibtex] --> Acknowledgements This template was originally mad
```

### anyskin

https://any-skin.github.io/

Pattern: `magnetic|AnySkin|skin`

```text
AnySkin: Plug-and-play Skin Sensing for Robotic Touch --> --> More Research HyperNeRF Nerfies LatentFusion PhotoShape --> --> --> --> --> --> AnySkin: Plug-and-play Sk
e Mellon University, 3 Columbia University, 4 Meta Paper arXiv Code Request a sample! Buy AnySkin CAD Files Design Tool Nerfies turns selfie videos from your phone into free-viewpoint portraits. --> Abstract While tactile sensing is wide
, its use pales in comparison to other sensory modalities like vision and proprioception. AnySkin addresses the critical challenges of versatility, replaceability, and data reusability, which have so far impeded the development of an eff
ective solution. Building on the simplistic design of ReSkin, and decoupling the sensing electronics from the sensing interface, AnySkin simplifies integration making it as straightforward as putting
on a phone case and connecting a charger. Furthermore, AnySkin is the first sensor with cross-instance generalizability of learned manipulation policies. This work makes three key contributions: first,
n process and a design tool for creating an adhesive-free, durable and easily replaceable magnetic tactile sensor; second, we characterize slip detection and policy learning with a AnySkin sensor; and finally, we demonstrate the generaliz
ability of models trained on one instance of AnySkin to new instances, and compare it with popular existing tactile solutions like DIGIT and ReSkin. We present AnySkin , a skin sensor made for
is easy to assemble
```

### respeaker

https://wiki.seeedstudio.com/ReSpeaker_Mic_Array_v2.0/

Pattern: `microphone|USB|direction`

```text
reSpeaker USB 4-Mic Array XVF3000 v2.0 | Seeed Studio Wiki Skip to main content Collaborate with Seeed - Creator , Ranger , or Contributor , there is alw
 3800 reSpeaker Flex reSpeaker 44mm reSpeaker Lite reSpeaker XVF 3000 v3.0/v3.2 reSpeaker USB 4-Mic Array XVF3000 v3.0/v3.2 reSpeaker USB 4-Mic Array XVF3000 v2.0 reSpeaker USB Mic Array reSpeaker 2-Mics Pi HAT Sound Event Detection
roducts Product List About Seeed License reSpeaker reSpeaker XVF 3000 v3.0/v3.2 reSpeaker USB 4-Mic Array XVF3000 v2.0 On this page reSpeaker USB 4-Mic Array XVF3000 v2.0 We are excited to formally introduce the reSpeaker XVF3800 — a
ensive upgrade to the reSpeaker XVF 3000. Building upon its predecessor's foundation of 4-microphone array architecture, universal compatibility (Windows / macOS / Linux), and dual-firmware (I2S / USB) plug-and-play convenience, the XVF3800
ated suite featuring AEC (Acoustic Echo Cancellation), AGC (Automatic Gain Control), DoA (Direction of Arrival) detection, beamforming, VAD (Voice Activity Detection), noise suppression, and dereverberation — laying robust groundwork for a
 intelligent interaction, and voice-controlled scenarios. Dual Operating Modes : Flexible USB/I2S firmware switching to meet diverse development and deployment requirements. Product Details & Specifications : ReSpeaker XVF3800 4-Mic
he original ReSpeaker Core to significantly improve the voice interaction performance.The microphones have also been improved in this version allowing significant
Focused claim audit:
 reSpeaker USB 4-Mic Array XVF3000 v2.0 | Seeed Studio Wiki Skip to main content Collaborate with Seeed - Creator , Ranger , or Contributor , there is always a role ideal for you!
 3800 reSpeaker Flex reSpeaker 44mm reSpeaker Lite reSpeaker XVF 3000 v3.0/v3.2 reSpeaker USB 4-Mic Array XVF3000 v3.0/v3.2 reSpeaker USB 4-Mic Array XVF3000 v2.0 reSpeaker USB Mic Array reSpeaker 2-Mics Pi HAT Sound Event Detection Module reSpeaker Cli
roducts Product List About Seeed License reSpeaker reSpeaker XVF 3000 v3.0/v3.2 reSpeaker USB 4-Mic Array XVF3000 v2.0 On this page reSpeaker USB 4-Mic Array XVF3000 v2.0 We are excited to formally introduce the reSpeaker XVF3800 — a comprehensive upgra
de to the reSpeaker XVF 3000. Building upon its predecessor's foundation of 4-microphone array architecture, universal compatibility (Windows / macOS / Linux), and dual-firmware (I2S / USB) plug-and-play convenience, the XVF3800 delivers a s
 intelligent interaction, and voice-controlled scenarios. Dual Operating Modes : Flexible USB/I2S firmware switching to meet diverse development and deployment requirements. Product Details & Specifications : ReSpeaker XVF3800 4-Mic Array Store Page Qui
lowing significant performance improvements over the first generation mic array with only 4 microphones. The ReSpeaker Mic Array v2.0 supports USB Audio Class 1.0 (UAC 1.0) directly. All major Operating System, including Windows,macOS, and Linux are compa
 and reduce the Mics from 7 to 4. Jan 25, 2018 Features ​ Far-field voice capture Support USB Audio Class 1.0 (UAC 1.0) Four microphones array 12 programmable RGB LED indicators Speech algorithms and features Voice Activity Detection Direction of Arriva
directional) Acoustic overload point: 120 dBSPL SNR: 61 dB Power Supply: 5V DC from Micro USB or expansion header Dimensions: 70mm (Diameter) 3.5mm Audio jack output socket Power consumption: 5V, 180mA with led on and 170mA with led off Max Sample Rate:
 with a capacitive sensing element and an IC interface. ③ RGB LED: Three-color RGB LED. ④ USB Port: Provide the power and control the mic array. ⑤ 3.5mm Headphone jack: Output audio, We can plug active speakers or Headphones into this port. ⑥ WM8960: Th
 provide 1 W per channel into 8 W loads. System Diagram Pin Map Dimensions Applications ​ USB Voice Capture Smart Speaker Intelligent Voice Assistant Systems Voice Recorders Voice Conferencing System Meeting Communicating Equipment Voice Interacting Rob
it with emteria.OS (andriod 7.1) on Raspberry. We plug the mic array v2.0 to raspberry pi USB port and select the ReSpeaker mic array v2.0 as audio device. Here is the audio recording screen. Here is the audio playing screen. We plug speaker to ReSpeake
Channel 4: mic4 raw data Channel 5: merged playback For Linux: The Mic array supports the USB DFU. We develop a python script dfu.py to update the firmware through USB. sudo apt - get update sudo pip install pyusb click git clone https : // github . com
 / respeaker / usb_4_mic_array . git cd usb_4_mic_array sudo python dfu . py - - download 6_channels_firmware . bin # The 6 channels version # if you want to use 1 channel,then the command should be like: sudo
e is the Acoustic Echo Cancellation example with 6 channels firmware. Step 1. Connect the USB cable to PC and audio jack to speaker. Step 2. Select the mic array v2.0 as output device in PC side. Step 3. Start the audacity to record. Step 4. Play music
 and LED Control Driver ​ Windows: Audio recording and playback works w
```

### odas

https://github.com/introlab/odas

Pattern: `localization|tracking|separation|sound`

```text
repository About ODAS: Open embeddeD Audition System Topics audition beamformer embedded localization real-time robotics separation sound tracking Resources Readme MIT license Activity Custom properties Stars 1.1k stars Watchers 56 watching
DAS ODAS stands for Open embeddeD Audition System. This is a library dedicated to perform sound source localization, tracking, separation and post-filtering. ODAS is coded entirely in C, for more portability, and is optimized to run ea
alization Please have a look at the odas_web project. Open Source Hardware from IntRoLab 8SoundsUSB , 8 inputs, USB powered, configurable microphone array. 16SoundsUSB , 16 inputs, USB powered, configurable microphone array. Papers You
s in Robotics and AI, Volume 9, 2022 F. Grondin and F. Michaud, Lightweight and Optimized Sound Source Localization and Tracking Methods for Opened and Closed Microphone Array Configurations , Robotics and Autonomous Systems, 2019 Abou
t ODAS: Open embeddeD Audition System Topics audition beamformer embedded localization real-time robotics separation sound tracking Resources Readme MIT license Activity Custom properties Stars 1.1k stars Watchers 56 watching
```

### gnss

https://www.u-blox.com/en/product/zed-f9p-module

Pattern: `RTK|multi.band|ZED.F9P`

```text
ZED-F9P module | u-blox Applications Automation & Robotics Autonomous robotic lawn mowers Autonomous vehicles (UGV) Connected factory Construction
es Overview Standard precision positioning High precision positioning LEAP technology PPP-RTK GNSS correction services Support Support Support portal Evaluation kits & Development boards Service status Documentation Product documenta
ts Careers Working at u-blox Discover Us What we offer Job openings Home Product Selector ZED-F9P module ZED-F9P module u-blox F9 high precision GNSS module Multi-band GNSS receiver delivers centimeter level accuracy in seconds Concurren
t reception of all constellations Multi-band RTK with fast convergence times and reliable performance Centimeter-level accuracy in a small and energy-efficient module Easy integration of R
for PointPerfect simplifies integration Standard Professional Automotive Product variants ZED-F9P-02B u-blox F9 high precision GNSS module with SBAS This product is not longer available Buy Now ZED-F9P - 04B u-blox F9 dual band GNSS modu
ofessional Grade LGA, 17x22 mm, 250 pcs/reel This product is not longer available Buy Now ZED-F9P - 05B u-blox F9 dual band L1/L2 GNSS module high precision Professional Grade LGA, 17x22 mm, 250 pcs/reel This product is not longer availa
ble Buy Now ZED-F9P - 15B u-blox F9 dual band L1/L5 GNSS module high precision Professional Grade LGA, 17x22 mm, 250 pcs/reel This product is not longer availa
l. Register for free trial *Offer applies to new Thing
Focused claim audit:
es Overview Standard precision positioning High precision positioning LEAP technology PPP-RTK GNSS correction services Support Support Support portal Evaluation kits & Development boards Service status Documentation Product documentation Service documen
 Home Product Selector ZED-F9P module ZED-F9P module u-blox F9 high precision GNSS module Multi-band GNSS receiver delivers centimeter level accuracy in seconds Concurrent reception of all constellations Multi-band RTK with fast convergence times and reliable
ance Centimeter-level accuracy in a small and energy-efficient module Easy integration of RTK for fast time-to-market Native support for PointPerfect simplifies integration Standard Professional Automotive Product variants ZED-F9P-02B u-blox F9 high pre
cision GNSS module with SBAS This product is not longer available Buy Now ZED-F9P - 04B u-blox F9 dual band GNSS module high precision Professional Grade LGA, 17x22 mm, 250 pcs/reel This product is not longer available Buy No
GNSS module high precision Professional Grade LGA, 17x22 mm, 250 pcs/reel This product is not longer available Buy Now ZED-F9P - 15B u-blox F9 dual band L1/L5 GNSS module high precision Professional Grade LGA, 17x22 mm, 250 pcs/reel This product is not longer available
ase output ✓ Data logging ✓ Jamming detection ✓ Programmable flash memory ✓ RTC crystal ✓ RTK rover ✓ Secure boot and updates ✓ Time pulse output ✓ Galileo OSNMA - ✓ - General features Antennas Pin (active) for external antenna Dimensions Dimensions [mm
cision GNSS module EVK-F9P u-blox F9P high precision GNSS evaluation kit Ardusimple simpleRTK2B Pro Arduino compatible shield with ZED-F9P multiband RTK module ANN-MB2 antenna All-band high precision GNSS antennas ANN-MB1 antenna L1/L5 multi-band, high
precision GNSS antennas ANN-MB series L1/L2 multi-band, high precision GNSS antennas No results have been found for . Product selector Read more Product resources Read more Blogs Read more White papers Read more
```

### umi

https://umi-gripper.github.io/

Pattern: `camera|gripper|Universal|2024`

```text
Universal Manipulation Interface: In-The-Wild Robot Teaching Without In-The-Wild Robots --> Universal Manipulation Interface In-The-Wild Robot Teachi
obots Human Demonstration with UMI Fully Autonomous Policy Rollout 1x 1x 1x 1x We present Universal Manipulation Interface (UMI) -- a data collection and policy learning framework that allows direct skill transfer from in-the-wild human de
monstrations to deployable robot policies. UMI employs hand-held grippers coupled with careful interface design to enable portable, low-cost, and information-rich data collection for challenging bimanual and dyna
ons. Paper here . --> Latest version: arXiv or here . Robotics: Science and Systems (RSS) 2024 ★ Best Systems Paper Award Finalist, RSS ★ Code and Tutorial Codebase Hardware Guide Data Collection Instruction --> --> --> 3D Printing Tu
yota Research Institute 4 MIT --> * Indicates equal contribution BibTeX @inproceedings{chi2024universal, title={Universal Manipulation Interface: In-The-Wild Robot Teaching Without In-The-Wild Robots}, author={Chi, Cheng and Xu, Zhenj
 and Song, Shuran}, booktitle={Proceedings of Robotics: Science and Systems (RSS)}, year={2024} } Hardware Design How can we capture sufficient information for a wide variety of tasks with just a wrist-mounted camera? UMI’s data colle
ction hardware takes the form of a hand-held parallel jaw gripper, mounted with a GoPro camera ①. To gather policy-deployable observations, UMI needs to capture sufficient visual context to i
```

### umirepo

https://github.com/real-stanford/universal_manipulation_interface

Pattern: `camera|latency|calibration`

```text
SLAM pipeline (umi)$ python run_slam_pipeline.py example_demo_session ... Found following cameras: camera_serial C3441328164125 5 Name: count, dtype: int64 Assigned camera_idx: right=0; left=1; non_gripper=2,3... camera_serial gripper_h
w_idx example_vid camera_idx 0 C3441328164125 0 demo_C3441328164125_2024.01.10_10.57.34.882133 99% of raw data are used. defaultdict(<function main.<locals>.<lambda
m with the cup arrangement policy. While this policy setup only requires a single arm and camera, the our system supports up to 2 arms and unlimited number of cameras. ⚙️ Hardware Setup Build deployment hardware according to our Hardwar
line is adapted from Steffen Urban 's fork of OBR_SLAM3 . We used Steffen Urban 's OpenImuCameraCalibrator for camera and IMU calibration. The UMI gripper's core mechanism is adpated from Push/Pull Gripper by John Mulac . UMI's soft fin

Focused claim audit:
ild Robot Teaching Without In-The-Wild Robots umi-gripper.github.io/ Resources Readme MIT license Activity Custom properties Stars 1.6k stars Watchers 19 watching Forks 297 forks Report repository main Branches Tags Go to file Code Open more actions menu La
eal scripts_slam_pipeline scripts_slam_pipeline tests tests umi umi .gitignore .gitignore LICENSE LICENSE README.md README.md conda_environment.yaml conda_environment.yaml eval_real.py eval_real.py franka_instruction.md franka_instruction.md run_slam_pipeli
_slam_pipeline.py train.py train.py View all files Repository files navigation README MIT license More items Universal Manipulation Interface [Project page] [Paper] [Hardware Guide] [Data Collection Instruction] [SLAM repo] [SLAM docker] Cheng Chi 1,2 , Zhe
ings > System Enable Startup Script Select /user/cmd_measure.lua you just uploaded. Setup GoPro: Install GoPro Labs firmware . Set date and time. Scan the following QR code for clean HDMI output Setup 3Dconnexion SpaceMouse : Install libspnav sudo apt ins
egs for hardware modification and umi-arx for detailed policy deployment instructions. 🏷️ License This repository is released under the MIT license. See LICENSE for additional details. 🙏 Acknowledgement Our GoPro SLAM pipeline is adapted from Steffen Urban
ild Robot Teaching Without In-The-Wild Robots umi-gripper.github.io/ Resources Readme MIT license Activity Custom properties Stars 1.6k stars Watchers 19 watching Forks 297 forks Report repository Releases Packages Contributors Languages Footer © 2026 GitHu
```

### lerobotcam

https://huggingface.co/docs/lerobot/cameras

Pattern: `camera|OpenCV|RealSense`

```text
Cameras · Hugging Face Hugging Face Search models, datasets, users... Ctrl K Models Datasets Spaces Buckets Docs Enterprise Pricing Website Tasks
erence Providers Inference Endpoints Storage Buckets Log In Sign Up LeRobot documentation Cameras LeRobot 🏡 View all docs AWS Trainium & Inferentia Accelerate Bitsandbytes CLI Chat UI Dataset viewer Datasets Deploying on AWS Diffusers G
an In the Loop Data Collection Training with PEFT (e.g., LoRA) Using Rename Map and Empty Cameras Compute & Hardware Compute Hardware Guide PyTorch accelerators Datasets Using LeRobotDataset Training Dataset Streaming Porting Large Data
eBot B601 YAM Third-Party Robots & Teleoperators Teleoperators Phone Isaac Teleop Sensors Cameras Third-Party Cameras & Sensors Resources Notebooks Updating Feetech Firmware Damiao Motors and CAN Bus About Contribute to LeRobot Writing
docstrings Backward compatibility API Reference Robots Teleoperators Cameras Motors Datasets Policies Processors Environments Configuration Join the Hugging Face community and get access to the augmented documentati
ccelerated inference Switch between documentation themes Sign Up to get started Copy page Cameras LeRobot offers multiple options for video capture: Class Supported Cameras OpenCVCamera Phone, built-in laptop, USB webcams ZMQCamera Netw
ork-connected cameras RealSenseCamera Intel RealSense (with depth) Reachy2Camera Reachy 2 robot cameras For OpenCVCamera compatibility details, see the Video I/O with OpenCV Overview . Fin
```

### corl

https://www.corl.org/

Pattern: `sensor|robot|learning`

```text
etting to Austin Hotel Information Local Tips Local Tours Inclusion at CoRL Childcare and Robotics Camp Registration Poster Printing Women and Allies Lunch Contributions Call for Early Career Keynotes Call for Papers Call for Workshops
sults Organizing Committee Sponsorship About CoRL CoRL 2025 CoRL 2026 202 6 Conference on Robot Learning November 9-12 , 202 6 | Austin , Texas, US Welcome to CoRL 2026! The Conference on Robot Learning (CoRL) is an annual internationa
l conference focusing on the intersection of robotics and machine learning. CoRL 202 6 will be held in Austin , Texas, US . Main conference: November 9-11 Workshops : November 12 Local information posted under the
Attending p age! Childcare and Robotics Camp info rmation posted! Registration is open! Hotel Information is posted! Discounted rates for hotel rooms expire on October 16th. Bo
results . 10/14 - Local information posted under the Attending page! 10/9 - Childcare and Robotics Camp information posted! 9/10 - Hotel Information is posted! 08/31 - Registration is open! 08/06 - Call for Demos posted! 06/24 - Call f
```

### encoder2

https://docs.simplefoc.com/encoder

Pattern: `incremental|quadrature|Encoder`

```text
Encoder | Arduino-FOC Encoder | Arduino-FOC Link Simple FOC Docs Menu Home Simple FOC Boards Simple FOC Shield Getting Started Soldering pads Soldering Pads v1.x Solderi
WM BLDCDriver 6PWM StepperDriver Stepper Driver 4PWM Stepper Driver 2PWM Position Sensors Encoder Hall sensors Magnetic sensor Magnetic sensor SPI Magnetic sensor I2C Magnetic sensor Analog Magnetic sensor PWM Generic sensor Current Sens
scord Community Shop Contact Arduino Simple FOC library Writing the Code Position Sensors Encoder ★ Loading... Helpful? 👍 0 👎 0 How can we improve this page? × Skip Send Feedback ✓ Thank you! Your feedback helps improve SimpleFOC docs. O
n this page Encoder setup Step 1. Instantiate Encoder class Step 2. Configuration Step 3. Encoder interrupt setup Hardware external interrupt Index pin configuration Software pin change interrupt Index pin configuration Step 4. Using enc
oder in real-time Position sensor for FOC algorithm Standalone sensor Example code Encoder setup Step 1. Instantiate Encoder class To initialize the encoder you need to provide the encoder A and B channel pins, encoder PPR and opt
ionally index pin. // Encoder(int encA, int encB , int cpr, int index) // - encA, encB - encoder A and B pins // - ppr - impulses per rotation (cpr=ppr*4) // - index pin - (optional input) Encoder encoder = Encoder ( 2 , 3 , 8192 , A0 )
; Step 2. Configuration When the Encoder class is instantiated, we need to configure it. First feature we can configure is enabling or disabling th
```

### opencvraw

https://raw.githubusercontent.com/opencv/opencv/4.x/doc/py_tutorials/py_calib3d/py_calibration/py_calibration.markdown

Pattern: `distortion|camera matrix|calibration`

```text
Camera Calibration {#tutorial_py_calibration} ================== Goal ---- In this section, we will learn about * types of distortion caused by cameras * how to find the intrinsic and
mages based off these properties Basics ------ Some pinhole cameras introduce significant distortion to images. Two major kinds of distortion are radial distortion and tangential distortion. Radial distortion causes straight lines to appear
 curved. Radial distortion becomes larger the farther points are from the center of the image. For example, one image is shown below in which two edges of a chess boa
d doesn't match with the red line. All the expected straight lines are bulged out. Visit [Distortion (optics)](http://en.wikipedia.org/wiki/Distortion_%28optics%29) for more details. ![image](images/calib_radial.jpg) In the following sectio
ns several new parameters are introduced. Visit [Camera Calibration and 3D Reconstruction](#tutorial_table_of_content_calib3d) for more details. Radial distortion can be represented as follows: \f[x_{distort
 k_3 r^6) \\ y_{distorted} = y( 1 + k_1 r^2 + k_2 r^4 + k_3 r^6)\f] Similarly, tangential distortion occurs because the image-taking lense is not aligned perfectly parallel to the imaging plane. So, some areas in the image may look nearer t
han expected. The amount of tangential distortion can be represented as below: \f[x_{distorted} = x + [ 2p_1xy + p_2(r^2+2x^2)] \\ y_{distorted} = y + [ p_1(r^2+ 2y^2)+ 2p_2xy]\f] In short,
 we need to find five param
```

### opencvhand

https://raw.githubusercontent.com/opencv/opencv/4.x/modules/calib3d/include/opencv2/calib3d.hpp

Pattern: `pinhole|calibrateHandEye|intrinsic`

```text
3d Camera Calibration and 3D Reconstruction The functions in this section use a so-called pinhole camera model. The view of a scene is obtained by projecting a scene's 3D point \f$P_w\f$ into the image plane using a perspective transform
r instead of homogeneous vector. The distortion-free projective transformation given by a pinhole camera model is shown below. \f[s \; p = A \begin{bmatrix} R|t \end{bmatrix} P_w,\f] where \f$P_w\f$ is a 3D point expressed with respect t
 world coordinate system, \f$p\f$ is a 2D pixel in the image plane, \f$A\f$ is the camera intrinsic matrix, \f$R\f$ and \f$t\f$ are the rotation and translation that describe the change of coordinates from world to camera coordinate system
rojective transformation's arbitrary scaling and not part of the camera model. The camera intrinsic matrix \f$A\f$ (notation used as in @cite Zhang2000 and also generally notated as \f$K\f$) projects 3D points given in the camera coordinat
e system to 2D pixel coordinates, i.e. \f[p = A P_c.\f] The camera intrinsic matrix \f$A\f$ is composed of the focal lengths \f$f_x\f$ and \f$f_y\f$, which are expressed in pixel units, and the principal point \f$(c_
cthreethree{f_x}{0}{c_x}{0}{f_y}{c_y}{0}{0}{1} \vecthree{X_c}{Y_c}{Z_c}.\f] The matrix of intrinsic parameters does not depend on the scene viewed. So, once estimated, it can be re-used as long as the focal length is fixed (in case of a zo
in{bmatrix} X_w \\ Y_w \\ Z_w \\ 1 \end{bmatrix}.\f] The following figure illustrates t
Focused claim audit:
3d Camera Calibration and 3D Reconstruction The functions in this section use a so-called pinhole camera model. The view of a scene is obtained by projecting a scene's 3D point \f$P_w\f$ into the image plane using a perspective transformation which forms the correspondi
r instead of homogeneous vector. The distortion-free projective transformation given by a pinhole camera model is shown below. \f[s \; p = A \begin{bmatrix} R|t \end{bmatrix} P_w,\f] where \f$P_w\f$ is a 3D point expressed with respect to the world coordinate system, \f
in{bmatrix} X_w \\ Y_w \\ Z_w \\ 1 \end{bmatrix}.\f] The following figure illustrates the pinhole camera model. ![Pinhole camera model](pics/pinhole_camera_model.png) { width=70% } Real lenses usually have some distortion, mostly radial distortion, and slight tangential
 projected to the same image point, e.g. all points along the red ray in the image of the pinhole camera model above would be mapped to the same image coordinate. This property is also the source for the scale ambiguity s in the equation of the pinhole camera model. As
pressed in the camera frame onto the image plane assuming a perspective projection model (pinhole camera model). Image coordinates extracted from classical image processing functions assume a (u,v) top-left coordinates frame. \note - for an online video course on this t
are required, but it is strongly recommended to use many more poses. */ CV_EXPORTS_W void calibrateHandEye( InputArrayOfArrays R_gripper2base, InputArrayOfArrays t_gripper2base, InputArrayOfArrays R_target2cam, InputArrayOfArrays t_target2cam, OutputArray R_cam2grip
or fisheye camera models, which use a different distortion model compared to the standard pinhole camera model used by #undistortPoints. The fisheye model is suitable for wide-angle cameras. The function transforms points from the distorted fisheye image to undistorted
```

### msgsraw

https://raw.githubusercontent.com/ros2/common_interfaces/rolling/sensor_msgs/msg/Imu.msg

Pattern: `covariance|angular|acceleration`

```text
# This is a message to hold data from an IMU (Inertial Measurement Unit) # # Accelerations should be in m/s^2 (not in g's), and rotational velocity should be in rad/sec # # If the covariance of the measurement is known, it should
ance of each measurement, e.g. from the datasheet, just put those along the diagonal) # A covariance matrix of all zeros will be interpreted as "covariance unknown", and to use the # data a covariance will have to be assumed or gotten from
ur IMU doesn't produce an # orientation estimate), please set element 0 of the associated covariance matrix to -1 # If you are interpreting this message, please check for a value of -1 in the first element of each # covariance matrix, and d
imate. std_msgs/Header header geometry_msgs/Quaternion orientation float64[9] orientation_covariance # Row major about x, y, z axes geometry_msgs/Vector3 angular_velocity float64[9] angular_velocity_covariance # Row major about x, y, z axes
 geometry_msgs/Vector3 linear_acceleration float64[9] linear_acceleration_covariance # Row major x, y z
```

### imageraw

https://raw.githubusercontent.com/ros2/common_interfaces/rolling/sensor_msgs/msg/Image.msg

Pattern: `timestamp|optical|frame`

```text
ncompressed image # (0, 0) is at top-left corner of image std_msgs/Header header # Header timestamp should be acquisition time of image # Header frame_id should be optical frame of camera # origin of frame should be optical center of camea
# +y should point down in the image # +z should point into to plane of the image # If the frame_id here and the frame_id of the CameraInfo # message associated with the image conflict # the behavior is undefined uint32 height # image h
```

### bagraw

https://github.com/ros2/rosbag2

Pattern: `record|playback|storage`

```text
rosbag2_interfaces rosbag2_performance rosbag2_performance rosbag2_py rosbag2_py rosbag2_storage rosbag2_storage rosbag2_storage_default_plugins rosbag2_storage_default_plugins rosbag2_storage_mcap rosbag2_storage_mcap rosbag2_storage_s
qlite3 rosbag2_storage_sqlite3 rosbag2_test_common rosbag2_test_common rosbag2_test_msgdefs rosbag2_test_msgdefs rosbag2_tests rosbag2_tests rosbag2_transport ros
README Contributing Apache-2.0 license Security More items Rosbag2 Rosbag2 — the tool for recording and playback of communications in ROS 2 systems. This is the ROS 2 successor of https://wiki.ros.org/rosbag . A "rosbag" is simply a fil
e full of timestamped messages. The first goal of the tool is efficient recording, to support complex systems in real time. Its second goal is efficent playback, to allow for viewing and using recorded data. For histor
 bag : ros2 bag burst ros2 bag convert ros2 bag info ros2 bag list ros2 bag play ros2 bag record ros2 bag reindex For up-to-date information on the available options for each, use ros2 bag <verb> --help . Moreover, rosbag2_transport::Pl
ayer and rosbag2_transport::Recorder components can be instantiated in rclcpp component containers, which makes possible to use intra-process communication for greater effici
ency. See composition section for details. Recording data In order to record all topics currently available in the system: $ ros2 bag record -a The command above will record all available topics and discovers new top
ics as they ap
Focused claim audit:
 to star a repository About No description, website, or topics provided. Resources Readme Apache-2.0 license Contributing Contributing Security policy Security policy Activity Custom properties Stars 448 stars Watchers 32 watching Forks 340 forks Report re
mmit message Last commit date .github .github docs docs lz4_cmake_module lz4_cmake_module mcap_vendor mcap_vendor ros2bag ros2bag rosbag2 rosbag2 rosbag2_compression rosbag2_compression rosbag2_compression_zstd rosbag2_compression_zstd rosbag2_cpp rosbag
2_storage rosbag2_storage_default_plugins rosbag2_storage_default_plugins rosbag2_storage_mcap rosbag2_storage_mcap rosbag2_storage_sqlite3 rosbag2_storage_sqlite3 rosbag2_test_common rosbag2_test_common rosbag2_test_msgdefs rosbag2_test_msgdefs rosbag2_
NOTICE README.md README.md View all files Repository files navigation README Contributing Apache-2.0 license Security More items Rosbag2 Rosbag2 — the tool for recording and playback of communications in ROS 2 systems. This is the ROS 2 successor of https:
n specified by the CLI options --compression-mode and --compression-format . Notably, the MCAP file format offered by the rosbag2_storage_mcap storage plugin supports compression in a way that produces files that are still indexable (whereas using the Ro
ize performance for specific use cases. See storage plugin documentation for more detail: mcap sqlite3 Controlling recordings via services The Rosbag2 recorder provides the following services for remote control, which can be called via ros2 service comma
taining metadata.yaml and one or more storage files, or to a single storage file such as .mcap or .db3 . The Player will automatically detect which storage implementation to use for playing. A progress bar to track the playback progress will be displayed
d see something along these lines: Files: demo_strings.db3 Bag size: 44.5 KiB Storage id: sqlite3 Duration: 8.501s Start: Nov 28 2018 18:02:18.600 (1543456938.600) End Nov 28 2018 18:02:27.102 (1543456947.102) Messages: 27 Topic information: Topic: /chatte
must exist. Example input_options.yaml : input_bags : - uri : /path/to/bag_a storage_id : sqlite3 - uri : /path/to/bag_b storage_id : mcap Note: Either --input or --input-options must be provided, but not both. The --output-options argument must point to t
ly messages between specific timestamps input_bags: - uri: /path/to/input_bag storage_id: mcap start_time_ns: 1744227144744197147 end_time_ns: 1744227145734665546 # output.yaml output_bags: - uri: /path/to/fragment_bag storage_id: mcap all_topics: true a
false start_paused : false storage : uri : " /path/to/destination/folder " storage_id : " sqlite3 " max_cache_size : 20000000 and player : ros__parameters : play : read_ahead_queue_size : 1000 node_prefix : " " rate : 1.0 loop : false # Negative timestamps
ec : 00000000 start_paused : false storage : uri : " path/to/rosbag/file " storage_id : " mcap " storage_config_uri : " " For a full list of available parameters, you can refer to player and recorder configurations from the test folder of rosbag2_transpo
e formats to adapt to individual use cases. This repository provides two storage plugins, mcap and sqlite3 . The default is mcap , which is provided to code by rosbag2_storage::get_default_storage_id() and defined in default_storage_id.cpp If not specifi
r ├── rosbag2_2025_02_21-15_35_35 | ├── metadata.yaml │ └── rosbag2_2025_02_21-15_35_35_0.mcap └── rosbag2_2025_02_21-15_37_17 ├── metadata.yaml └── rosbag2_2025_02_21-15_37_1
```

### pipelineraw

https://github.com/ros-perception/image_pipeline

Pattern: `calibration|image|processing`

```text
GitHub - ros-perception/image_pipeline: An image processing pipeline for ROS. · GitHub Skip to content Navigation Menu Sign in Products Platform GitHub Repository hosting, code review, and collaborat
tab or window. Reload to refresh your session. Dismiss alert {{ message }} ros-perception image_pipeline Repository navigation Code Issues 38 ( 38 ) Pull requests 22 ( 22 ) Actions Security and quality Insights More items image_pipelin
ngs Fork 789 ( 789 ) Star 978 ( 978 ) You must be signed in to star a repository About An image processing pipeline for ROS. docs.ros.org/en/rolling/p/image_pipeline/ Topics c-plus-plus image-processing python ros Resources Readme Lice
me Name Last commit message Last commit date .github/ workflows .github/ workflows camera_calibration camera_calibration depth_image_proc depth_image_proc image_pipeline image_pipeline image_proc image_proc image_publisher image_publisher im
age_rotate image_rotate image_view image_view stereo_image_proc stereo_image_proc tools tools tracetools_image_pipeline tracetools_image_pipeline wiki_files wiki_files .gitignore .gitignore CONTRIBUTING.md CONTRIBUTI
ADME.md View all files Repository files navigation README Contributing License More items image_pipeline This package fills the gap between getting raw images from a camera driver and higher-level vision processing. Documentation is ho
sted in the ROS 2 API docs. The image_pipeline documentation includes an overview, details on camera_info , and links to the documen
Focused claim audit:
rolling/p/image_pipeline/ Topics c-plus-plus image-processing python ros Resources Readme License Contributing Contributing Activity Custom properties Stars 978 stars Watchers 37 watching Forks 789 forks Report repository rolling Branches Tags Go to file Co
iles Name Name Last commit message Last commit date .github/ workflows .github/ workflows camera_calibration camera_calibration depth_image_proc depth_image_proc image_pipeline image_pipeline image_proc image_proc image_publisher image_publisher image_rotate image_rot
mage_pipeline wiki_files wiki_files .gitignore .gitignore CONTRIBUTING.md CONTRIBUTING.md LICENSE LICENSE README.md README.md View all files Repository files navigation README Contributing License More items image_pipeline This package fills the gap between
rolling/p/image_pipeline/ Topics c-plus-plus image-processing python ros Resources Readme License Contributing Contributing Activity Custom properties Stars 978 stars Watchers 37 watching Forks 789 forks Report repository Releases Packages Used by Contribut
```

### qosraw

https://raw.githubusercontent.com/ros2/ros2_documentation/jazzy/source/Concepts/Intermediate/About-Quality-of-Service-Settings.rst

Pattern: `sensor data|best effort|reliability`

```text
ity of the underlying DDS transport in environments with lossy wireless networks where a "best effort" policy would be more suitable, or in real-time computing systems where the right Quality of Service profile is needed to meet deadlines. A
iven scenario, ROS 2 provides a set of predefined QoS profiles for common use cases (e.g. sensor data). At the same time, developers are given the flexibility to control specific policies of the QoS profiles. QoS profiles can be specified fo
e. * Depth * *Queue size*: only honored if the "history" policy was set to "keep last". * Reliability * *Best effort*: attempt to deliver samples, but may lose them if the network is not robust. * *Reliable*: guarantee that samples are deliv
 policies in ROS 2 combine to provide functionality akin to the queue size in ROS 1. The "reliability" policy in ROS 2 is akin to the use of either UDPROS (only in ``roscpp``) for "best effort", or TCPROS (ROS 1 default) for "reliable". Note
bscriptions in ROS 2 have "keep last" for history with a queue size of 10, "reliable" for reliability, "volatile" for durability, and "system default" for liveliness. Deadline, lifespan, and lease durations are also all set to "default". * S
nses, the server is not protected from side-effects of receiving the outdated requests. * Sensor data For sensor data, in most cases it's more important to receive readings in a timely fashion, rather than ensuring that all of them arrive. T
es as soon as they are captured, at the expense
Focused claim audit:
ity of the underlying DDS transport in environments with lossy wireless networks where a "best effort" policy would be more suitable, or in real-time computing systems where the right Quality of Service profile is needed to meet deadlines. A set of QoS "policie
iven scenario, ROS 2 provides a set of predefined QoS profiles for common use cases (e.g. sensor data). At the same time, developers are given the flexibility to control specific policies of the QoS profiles. QoS profiles can be specified for publishers, subscr
ueue size*: only honored if the "history" policy was set to "keep last". * Reliability * *Best effort*: attempt to deliver samples, but may lose them if the network is not robust. * *Reliable*: guarantee that samples are delivered, may retry multiple times. * D
eliability" policy in ROS 2 is akin to the use of either UDPROS (only in ``roscpp``) for "best effort", or TCPROS (ROS 1 default) for "reliable". Note however that even the reliable policy in ROS 2 is implemented using UDP, which allows for multicasting if appr
nses, the server is not protected from side-effects of receiving the outdated requests. * Sensor data For sensor data, in most cases it's more important to receive readings in a timely fashion, rather than ensuring that all of them arrive. That is, developers w
es as soon as they are captured, at the expense of maybe losing some. For that reason the sensor data profile uses best effort reliability and a smaller queue size. * Parameters Parameters in ROS 2 are based on services, and as such have a similar profile. The
 policies:* .. list-table:: :header-rows: 1 * - Publisher - Subscription - Compatible * - Best effort - Best effort - Yes * - Best effort - Reliable - No * - Reliable - Best effort - Yes * - Reliable - Reliable - Yes *Compatibility of durability QoS policies:*
```

### as5600board

https://learn.adafruit.com/adafruit-as5600-magnetic-angle-sensor/overview

Pattern: `12.bit|AS5600|magnet`

```text
Overview | Adafruit AS5600 Magnetic Angle Sensor | Adafruit Learning System --> Skip to main content Skip to article content Shop Learn Blog Forums IO LIVE! AdaBox toggle me
es Explore Groups to get your gears turning Explore Groups New Guides Playground Adafruit AS5600 Magnetic Angle Sensor Overview Adafruit AS5600 Magnetic Angle Sensor Rotational sensing without a mechanical connection by Liz Clark publis
iew Guide Products view all Your browser does not support the video tag. Primary Adafruit AS5600 Magnetic Angle Sensor $5.95 Add to Cart Featured High-strength 'rare earth' magnet $2.50 Add to Cart View product details 7 Beginner Produc
e video tag. Add rotational sensing - without a mechanical connection - with the Adafruit AS5600 Magnetic Angle Sensor . Featuring the classic ams AS5600 , this board can sense a rotating N/S magnetic field up to 3mm away from the chip
less' rotary encoders or potentiometers, without the risk of mechanical failure or noise. Magnetic angle sensors get the best of 'both worlds': like rotary encoders they can rotate freely 360 degrees around, and like potentiometers, the
Arduino, Python and CircuitPython driver support. Then, identify the north and south of a magnet: we recommend a rare earth magnet. Note that many round magnets have the N/S on alternate 'coin face' sides, so you'll need to rotate it on
 the edge. Place the magnet near the middle of the chip and rotate it in place. The firmware will detect the magnetic field and report the a
Focused claim audit:
have absolute location detection. All you need is a microcontroller or microcomputer with I2C - we have Arduino, Python and CircuitPython driver support. Then, identify the north and south of a magnet: we recommend a rare earth magnet. Note that many ro
ake usage plug-and-play, we added SparkFun qwiic -compatible STEMMA QT connectors for the I2C bus, so you don't even need to solder the I2C and power lines. Simply wire up to your favorite micro using a STEMMA QT adapter cable. The Stemma QT connectors
```

### rss2025

https://roboticsconference.org/2025/program/papers/

Pattern: `sensor|tactile|calibr|radar|event`

```text
inwoo Lee, Woojae Shin, Hyondong Oh 6 Perception and Navigation DRO: Doppler-Aware Direct Radar Odometry with Gyroscope --> DRO: Doppler-Aware Direct Radar Odometry with Gyroscope --> DRO: Doppler-Aware Direct Radar Odometry with Gyros
lison Pinosky, Todd Murphey 52 Manipulation I Reactive Diffusion Policy: Slow-Fast Visual-Tactile Policy Learning for Contact-Rich Manipulation --> Reactive Diffusion Policy: Slow-Fast Visual-Tactile Policy Learning for Contact-Rich Mani
pulation --> Reactive Diffusion Policy: Slow-Fast Visual-Tactile Policy Learning for Contact-Rich Manipulation Han Xue, Jieji Ren, Wendi Chen, Gu Zhang, Fang Yuan, Guoying Gu, Huazhe Xu, Cewu Lu Han Xue,
arik Kelestemur, Jiuguang Wang, Tao Pang, Russ Tedrake 54 Manipulation I ViTaSCOPE: Visuo-tactile Implicit Representation for In-hand Pose and Extrinsic Contact Estimation --> ViTaSCOPE: Visuo-tactile Implicit Representation for In-hand
Pose and Extrinsic Contact Estimation --> ViTaSCOPE: Visuo-tactile Implicit Representation for In-hand Pose and Extrinsic Contact Estimation Jayjun Lee, Nima Fazeli Jayjun Lee, Nima Fazeli 55 Manipulation I
e, Yujin Jang, Beomjoon Kim 56 Manipulation I PP-Tac: Paper Picking Using Omnidirectional Tactile Feedback in Dexterous Robotic Hands --> PP-Tac: Paper Picking Using Omnidirectional Tactile Feedback in Dexterous Robotic Hands --> PP-Tac:
 Paper Picking Using Omnidirectional Tactile Feedback in Dexterous Robotic Hands Pei Lin, Yuzhe Huang, Jianpeng Ma, Chenxi Xiao, Wanlin Li
```

### anyskinpaper

https://arxiv.org/abs/2409.08276

Pattern: `AnySkin|magnetic|2024`

```text
[2409.08276] AnySkin: Plug-and-play Skin Sensing for Robotic Touch Skip to main content Search Submit Donate Log in Search arXiv Press Enter to search · Advance
d search --> Computer Science > Robotics arXiv:2409.08276 (cs) [Submitted on 12 Sep 2024 ( v1 ), last revised 27 Sep 2024 (this version, v3)] Title: AnySkin: Plug-and-play Skin Sensing for Robotic Touch Authors: Raunaq Bhirangi
es Erciyes , Yifeng Cao , Tess Hellebrekers , Lerrel Pinto View a PDF of the paper titled AnySkin: Plug-and-play Skin Sensing for Robotic Touch, by Raunaq Bhirangi and 5 other authors View PDF HTML (experimental) Abstract: While tactile
, its use pales in comparison to other sensory modalities like vision and proprioception. AnySkin addresses the critical challenges that impede the use of tactile sensing -- versatility, replaceability, and data reusability. Building on
stic design of ReSkin, and decoupling the sensing electronics from the sensing interface, AnySkin simplifies integration making it as straightforward as putting on a phone case and connecting a charger. Furthermore, AnySkin is the first
n process and a design tool for creating an adhesive-free, durable and easily replaceable magnetic tactile sensor; second, we characterize slip detection and policy learning with the AnySkin sensor; and third, we demonstrate zero-shot gen
eralization of models trained on one instance of AnySkin to new instances, and compare it with popular existing tactile solutions like DIGIT and ReSkin. Vid
```

### kalibrmodels

https://github.com/ethz-asl/kalibr/wiki/supported-models

Pattern: `pinhole|distortion|camera`

```text
upported models Jump to bottom Patrick Geneva edited this page May 3, 2022 · 24 revisions Camera models Kalibr supports the following projection models: pinhole camera model (pinhole) 1 ( intrinsics vector : [fu fv pu pv]) omnidirection
al camera model (omni) 2 ( intrinsics vector : [xi fu fv pu pv]) double sphere camera model (ds) 3 ( intrinsics vector : [xi alpha fu fv pu pv]) extended unified camera model (eucm) 4 ( intrinsics vector : [alpha beta fu fv p
re model parameters (only ds) alpha, beta : extended unified model parameters (only eucm) Distortion models Kalibr supports the following distortion models: radial-tangential (radtan) * ( distortion_coeffs : [k1 k2 r1 r2]) equidistant (equi
) ** ( distortion_coeffs : [k1 k2 k3 k4]) fov (fov) 5 ( distortion_coeffs : [w]) none (none) ( distortion_coeffs : []) References Please cite the appropriate papers when using this toolbox or parts of it in
 an academic publication. J. Kannala and S. Brandt (2006). A Generic Camera Model and Calibration Method for Conventional, Wide-Angle, and Fish-Eye Lenses, IEEE Transactions on Pattern Analysis and Machine Intellige
 8, pp. 1335-1340 Mei, Christopher, and Patrick Rives. "Single view point omnidirectional camera calibration from planar grids." Proceedings 2007 IEEE International Conference on Robotics and Automation. IEEE, 2007. Usenko, Vladyslav, N
ikolaus Demmel, and Daniel Cremers. "The double sphere camera model." 2018 International Conference on 3D Vision (3DV). IEEE, 2018. Khom
```

### d435repo

https://github.com/realsenseai/librealsense

Pattern: `D435|D405|stereo`

```text
(Python, ROS, C#, Unity and more... ) Active developer community and defacto-standard 3D stereo camera for robotics Cross-platform support: Windows, Linux, macOS, Android, and Docker Product Line RealSense stereo depth products use ste
. D457 GMSL/FAKRA The RealSense™ Depth Camera D457 is our first GMSL/FAKRA high bandwidth stereo camera. The D457 has an IP65 grade enclosure protecting it from dust ingress and projected water. D455 The RealSense D455 is a long-range s
s, an RGB sensor, and a built-in IMU, delivering accurate depth at distances up to 10 m.. D435if The D435if is one of RealSense™ Depth Camera with IR pass filter family expanding our portfolio targeting the growing robotic market. The
 pass filter to enhance depth quality and performance range in many robotic environments. D405 The RealSense™ Depth Camera D405 is a short-range stereo camera providing sub-millimeter accuracy for your close-range computer vision need
s. 🛍️ Explore more stereo products Getting Started Start developing with RealSense in minutes using either method below. 1️. Precompiled SDK This is the best option

Focused claim audit:
era-api computer-vision developer-kits hardware library librealsense sdk Resources Readme Apache-2.0 license Code of conduct Code of conduct Contributing Contributing Security policy Security policy Activity Custom properties Stars 9.1k stars Watchers 272
 readme.md View all files Repository files navigation README Code of conduct Contributing Apache-2.0 license Security More items RealSense SDK 2.0 is a cross-platform library for RealSense depth cameras. The SDK allows depth and color streaming, and provid
 pass filter to enhance depth quality and performance range in many robotic environments. D405 The RealSense™ Depth Camera D405 is a short-range stereo camera providing sub-millimeter accuracy for your close-range computer vision needs. 🛍️ Explore more s
era-api computer-vision developer-kits hardware library librealsense sdk Resources Readme Apache-2.0 license Code of conduct Code of conduct Contributing Contributing Security policy Security policy Activity Custom properties Stars 9.1k stars Watchers 272
```

### handbook28

https://www.handbookofrobotics.org/view-chapter/videodetails/28

Pattern: `Force|Tactile|proximity|skin`

```text
ensing and Estimation 6 - Model Identification 7 - Motion Planning 8 - Motion Control 9 - Force Control 10 - Redundant Robots 11 - Robots with Flexible Elements 12 - Robotic Systems Architectures and Programming 13 - Behavior-Based Sys
24 - Wheeled Robots 25 - Underwater Robots 26 - Flying Robots 27 - Micro-/Nanorobots 28 - Force and Tactile Sensing 29 - Inertial Sensing, GPS and Odometry 30 - Sonar Sensing 31 - Range Sensing 32 - 3-D Vision for Navigation and Graspi
79 - Robotics for Education 80 - Roboethics: Social and Ethical Implications Chapter 28 — Force and Tactile Sensing Mark R. Cutkosky and William Provancher This chapter provides an overview of force and tactile sensing, with the primar
y emphasis placed on tactile sensing. We begin by presenting some basic considerations in choosing a tactile sensor and then review a wide variety of sensor types, incl
uding proximity, kinematic, force, dynamic, contact, skin deflection, thermal, and pressure sensors. We also review various transduction methods, appropriate for each general sensor type. We consid
on or being responsive to contacts from external agents. Concerning the interpretation of tactile information, we describe the general problems and present two short illustrative examples. The first involves intrinsic tactile sensing, i.
 e., estimating contact locations and forces from force sensors. The second involves contact pressure sensing, i. e., estimating surface normal and shear stress distributions from an arra
```

### handbook

https://www.handbookofrobotics.org/

Pattern: `Handbook|Sensing|Robotics`

```text
--> Springer Handbook of Robotics - Multimedia Extension - Handbook of Robotics Search Chapter Videos Part Videos About Multimedia App Select Chapter 0 - Preface 1 - Robotics and the Handbook 2 - Kinematics 3 - Dynamics
 4 - Mechanism and Actuation 5 - Sensing and Estimation 6 - Model Identification 7 - Motion Planning 8 - Motion Control 9 - Force Control 10 - Redundant Robots 11 - Robots with Fle
s Architectures and Programming 13 - Behavior-Based Systems 14 - AI Reasoning Methods for Robotics 15 - Robot Learning 16 - Design and Performance Evaluation 17 - Limbed Systems 18 - Parallel Mechanisms 19 - Robot Hands 20 - Snake-Like an
d Continuum Robots 21 - Actuators for Soft Robotics 22 - Modular Robots 23 - Biomimetic Robots 24 - Wheeled Robots 25 - Underwater Robots 26 - Flying Robots 27 - Micro-/Nanorobots 28 - Force
and Tactile Sensing 29 - Inertial Sensing, GPS and Odometry 30 - Sonar Sensing 31 - Range Sensing 32 - 3-D Vision for Navigation and Grasping 33 - Visual Object Class Recognition 34 - Visual Servoing 35 - Multisensor Data Fusion 36 - Mot
- Mobility and Manipulation 41 - Active Manipulation for Perception 42 - Haptics 43 - Telerobotics 44 - Networked Robots 45 - World Modeling 46 - Simultaneous Localization and Mapping 47 - Motion Planning and Obstacle Avoidance 48 - Model
 Modeling and Control of Aerial Robots 53 - Multiple Mobile Robot Systems 54 - Industrial Robotics 55 - Space Robotics 56 - Robotics in Agriculture and Forestry 57 - Robotics in Construction
```

### ethsensors

https://ethz.ch/content/dam/ethz/special-interest/mavt/robotics-n-intelligent-systems/asl-dam/documents/lectures/autonomous_mobile_robots/spring-2015/04_-_Perception_I_-_Sensors.pdf

Pattern: `sensor`

```text
 resolution
 bandwidth
 price
 energy needed
|
--
unstructured
environments
|
Autonomous Mobile Robots
--
 Sonar range finder
 Camera
|
Autonomous Mobile Robots
--
 Indoors (Museum: unstructured and dynamic)

 Sensors
 Wheel encoders
 Ring of sonar sensors
 Pan-tilt camera

C University of Bonn
--
 Proprioceptive sensors
 measure values internally to the system (robot),
 e.g. motor speed, wheel load, heading of the robot, battery status
 Exteroceptive sensors
--
 Sonar
 Laser
 Structured light
 Vision (next lectures)


--
 optical encoders are proprioceptive sensors
 typical resolutions: 64 - 2048 increments per revolution.
 for high resolution: interpolation

 Working principle of optical encoders
 regular: counts the number of transitions but cannot tell the direction of motion
--
the direction of motion. Additionally, resolution is 4 times bigger
 a single slot in the outer track generates a reference pulse per revolution
4 - Perception: Sensor Overview
23
--
 Heading sensors can be proprioceptive (gyroscope, accelerometer) or
exteroceptive (compass, inclinometer).
 Allows, together with an appropriate velocity information, to integrate the
movement to a position estimate.
--
 bandwidth limitations (0.5 Hz) and susceptible to vibrations
 not suitable for indoor environments for absolute orientation
 useful indoor (only locally)
|
--
 Bandwidth up to 50 KHz
 An accelerometer measures
acceleration only along a single axis. By
mounting three accelerometers
--
 Accuracy depends on size and angle of sight of the tag (e.g., with a 10 cm tag
and 2 meters distance -> 2 cm accuracy 5 deg precision)
 Good for rough localization
4 - Perception: Sensor Overview
Augmented Reality Tag
--
 position accuracy proportional to precision of time measurement
 Real time update of the exact location of the satellites:
 monitoring the satellites from a number of widely distributed ground stations
 master station analyses all the measurements and transmits the actual position to each of the satellites
--
 Commercial GPS receivers have nominal position accuracy of 3 meters
|
Autonomous Mobile Robots
Margarita Chli, Paul Furgale, Marco Hutter, Martin Rufli, Davide Scaramuzza, Roland Siegwart
--
 Sonar



--
 Structured light

|
Autonomous Mobile Robots
--
 Resolution of ~ 2 cm
 Relative error 2%
 sound beam propagates in a cone (approx.)
 opening angles around 20 to 40 degrees
--
 Angular resolution 0.25 deg
 Depth resolution ranges between ~10 mm and the typical accuracy is 35 mm, over a range from 5 cm up
to 20 m or more (up to 80 m), depending on the reflectivity of the object being ranged.
 This device performs 75 180-degrees scans per second

--
 By lowering the rotational speed of the turn-table, the angular resolution in the horizontal direction can be
made as small as desired.
 A full spherical field of view can be covered (360° in azimuth and +/-90° in elevation).

--
 Angular resolution is 0.09° and 0.4° respectively
 Delivers over 1.3 million data points per second
 The distance accuracy is 2 cm and can measure depth up to 50 m
 This sensor was the primary means of terrain map construction and obstacle detection for all the top DARPA 2007 Urban Challenge
teams. However, the Velodyne is currently still 10 times more expensive than a Sick laser range finder (SICK ~ 4000 $, Velodyne
~40,000 $)
--
Structured Light (vision, 2D or 3D): Structured Light
 Eliminate the correspondence problem by projecting structured light on the scene.
 Slits of light or emit collimated light (possibly laser) by means of a rotating mirror.
 Light perceived by camera
 Range to an illuminated point can then be determined from simple geometry.
--
 Camera resolution: 640x480 pixels
|
Autonomous Mobile Robots
Margarita Chli, Paul Furgale, Marco Hutter, Martin Rufli, Davide Scaramuzza, Roland Siegwart
--
 The technique of analyzing a known pattern is “structured light
 The IR projector projects a pseudo-random pattern across the surface of the room.
 The direction of each speckle of the patter is known (from pre calibration during manufacturing) and is
hardcoded into the memory of the Kinect
--
 However very low resolution (174x144 pixels)
 Range Camera SR-3000
C MESA Imaging AG
|
--
 Resolution 1920x1080 pixels
 Field of view: 70 deg (H), 60 deg (V)
 Claimed accuracy: 1 mm
 Claimed max range: 6 meters
4 - Perception: Sensor Overview
79
```

### ethsyllabus

https://asl.ethz.ch/education/lectures/autonomous_mobile_robots/spring-2020.html

Pattern: `Perception|Sensors|Robots`

```text
Autonomous Mobile Robots - Spring 2020 – Autonomous Systems Lab | ETH Zurich Homepage Navigation Search Content Footer Contact Sitemap Autonomous Systems Lab Servic
ASL Language Selection English You are here Homepage Education Lectures Autonomous Mobile Robots Spring 2020 Autonomous Mobile Robots - Spring 2020 This course is jointly taught by Roland Siegwart, Margarita Chli, Juan Nieto and Nichola
atform (enroll here ), and closely follows the textbook Introduction to Autonomous Mobile Robots by Roland Siegwart, Illah Nourbakhsh, Davide Scaramuzza, The MIT Press, second edition 2011. The MOOC units are extended by weekly lectures
```

### mitsyllabus

https://courses.csail.mit.edu/6.141/spring2010/pub/syllabus.html

Pattern: `Sensing|Cameras|Sensors`

```text
oard Th 02/04 F 02/05 CI-M Lecture: Getting started with communication in RSS M 02/08 L2: Sensing and Control Architectures-Part I (UMO) Lab 1 due (wiki and briefing) Lab 2: Chassis Build, Light Sensors and Braitenberg Behaviors T 02/09
ab 2 due (wiki and briefing) Lab 3: Motor Characterization and Motion Control W 02/17 L5: Cameras, Images, and Low-Level Robot Vision (ST) Th 02/18 F 02/19 Individual Project Architecture Reports Due at 5PM M 02/22 L6: Carmen (NR) Lab 3
```

### mitmodern

https://meche.mit.edu/featured-classes/robotics-science-and-systems

Pattern: `sensing|embedded|state estimation`

```text
ations for robots and autonomous vehicles operating in the physical world. Topics include sensing, kinematics and dynamics, state estimation, computer vision, perception, learning, control, motion planning, and embedded system developmen
```

### anyskinreal

https://github.com/raunaqbhirangi/anyskin

Pattern: `MIT license|AnySkin|magnetic`

```text
GitHub - raunaqbhirangi/anyskin: Interfacing Repository for the AnySkin tactile sensor · GitHub Skip to content Navigation Menu Sign in Products Platform GitHub Repository hosting, code review, and collaboration
tab or window. Reload to refresh your session. Dismiss alert {{ message }} raunaqbhirangi anyskin Repository navigation Code Issues Pull requests 1 ( 1 ) Actions Projects Security and quality Insights More items anyskin Public Notificati
91 ( 91 ) You must be signed in to star a repository About Interfacing Repository for the AnySkin tactile sensor Resources Readme MIT license Activity Stars 91 stars Watchers 2 watching Forks 10 forks Report repository main Branches Tags
iles Name Name Last commit message Last commit date .github/ workflows .github/ workflows anyskin anyskin arduino arduino tests tests .gitignore .gitignore .gitmodules .gitmodules .pre-commit-config.yaml .pre-commit-config.yaml LICENSE L
t.toml pyproject.toml setup.py setup.py View all files Repository files navigation README MIT license More items AnySkin Sensor Library This is a python library to interface with AnySkin sensors. Much of this is adapted and streamlined from
the reskin_sensor library. We provide two classes for interfacing with AnySkin . The AnySkinBase class is good for standalone data collection: it blocks code execution while data is being collected. The AnySkinProcess class can be u
table release is v1.0.0 Installation This package can be installed using pip: pip install anyskin
```

### vl53board

https://www.pololu.com/product/3415

Pattern: `VL53L1X|time.of.flight|4 m`

```text
Pololu - VL53L1X Time-of-Flight Distance Sensor Carrier with Voltage Regulator, 400cm Max Sensors » Proximity Sensors and Range Finders » Carriers for ST Time-of-Flight (T
oF) Distance Sensors » VL53L1X Time-of-Flight Distance Sensor Carrier with Voltage Regulator, 400cm Max New! Pololu item #: 3415 Brand: Pololu supply outlook Get stock notification Noti
any price drop at or below $ at qty Save This sensor is a carrier/breakout board for ST’s VL53L1X laser-ranging sensor, which offers fast and accurate ranging up to 4 m . It uses the time of flight (ToF) of invisible, eye-safe laser puls
s like color, shape, and texture (though these things will affect the maximum range). The VL53L1X also features a programmable region of interest (ROI), so the full field of view can be reduced or divided into multiple zones. Distance me
ndard solderless breadboards and 0.1″ perfboards. Compare all products in Carriers for ST Time-of-Flight (ToF) Distance Sensors . Description Specs (11) Pictures (10) Resources (13) FAQs (0) On the blog (4) Distributors (87) Overview The VL53L1
X from ST Microelectronics is a long-distance ranging time-of-flight (TOF) sensor integrated into a compact module. This board is a carrier for the VL53L1X, so we recommend careful reading of the VL53L1X data
sheet (1MB pdf) before using this product. The VL53L1X is effectively a tiny, self-contained lidar system featuring an integrated 940 nm Class 1 laser, which is invisible and eye-safe. Unlike co
sors that use th
```

### metavisionlicense

https://github.com/prophesee-ai/openeb

Pattern: `Apache|OpenEB|HAL`

```text
GitHub - prophesee-ai/openeb: Open source SDK to create applications leveraging event-based vision hardware equipment · GitHub Skip to content Navigation Menu Sign in P
r tab or window. Reload to refresh your session. Dismiss alert {{ message }} prophesee-ai openeb Repository navigation Code Issues 21 ( 21 ) Pull requests 5 ( 5 ) Actions Security and quality Insights More items openeb Public Notificati
ders and files Name Name Last commit message Last commit date .github .github cmake cmake hal hal hal_psee_plugins hal_psee_plugins licensing licensing sdk sdk standalone_samples standalone_samples utils utils .gitignore .gitignore .
est.py pytest.ini pytest.ini View all files Repository files navigation README More items OpenEB OpenEB is the open source project associated with Metavision SDK It enables anyone to get a better understanding of event-based vision, dir
cientist, academic, join and contribute to the fast-growing event-based vision community. OpenEB is composed of the Open modules of Metavision SDK : HAL: Hardware Abstraction Layer to operate any event-based vision device. Base: Foundat
to_video and video_to_event pipelines. Stream: High-level abstraction built on the top of HAL to easily interact with event-based cameras. UI: Viewer and display controllers for event-based data. OpenEB also contains the source code
s are: EVK3 - VGA/320/HD EVK4 - HD This document describes how to compile and install the OpenEB codebase. For further information, refer to our online
```

### opencvlicense

https://raw.githubusercontent.com/opencv/opencv/4.x/LICENSE

Pattern: `Apache|License`

```text
Apache License Version 2.0, January 2004 http://www.apache.org/licenses/ TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION 1. Definitions. "License" shall mean the terms and conditions for use, repro
mean the copyright owner or entity authorized by the copyright owner that is granting the License. "Legal Entity" shall mean the union of the acting entity and all other entities that control, are controlled by, or are under common contr
r "Your") shall mean an individual or Legal Entity exercising permissions granted by this License. "Source" form shall mean the preferred form for making modifications, including but not limited to software source code, documentation sou
l mean the work of authorship, whether in Source or Object form, made available under the License, as indicated by a copyright notice that is included in or attached to the work (an example is provided in the Appendix below). "Derivative
fications represent, as a whole, an original work of authorship. For the purposes of this License, Derivative Works shall not include works that remain separable from, or merely link (or bind by name) to the interfaces of, the Work and D
received by Licensor and subsequently incorporated within the Work. 2. Grant of Copyright License. Subject to the terms and conditions of this License, each Contributor hereby grants to You a perpetual, worldwide, non-exclusive, no-charg
e, royalty-free, irrevocable copyright license to reproduce, prepare Derivative Works of, publicly
```

### gazeborepo

https://github.com/gazebosim/gz-sensors

Pattern: `Apache|License|sensor`

```text
GitHub - gazebosim/gz-sensors: Provides numerous sensor models designed to generate realistic data from simulation environments. · GitHub Skip to content Navigation Menu Sign in Products Platform
r tab or window. Reload to refresh your session. Dismiss alert {{ message }} gazebosim gz-sensors Repository navigation Code Issues 61 ( 61 ) Pull requests 22 ( 22 ) Actions Projects Security and quality Insights More items gz-sensors P
111 ) Star 177 ( 177 ) You must be signed in to star a repository About Provides numerous sensor models designed to generate realistic data from simulation environments. gazebosim.org Topics gazebo gazebosim hacktoberfest ignition-rende
ring ignition-robotics ignition-sensors robotics robotics-simulation sensors sensors-models simulation Resources Readme Apache-2.0 license Contributing Contributing Security policy Security policy Activity Custom properties
l CMakeLists.txt CMakeLists.txt CONTRIBUTING.md CONTRIBUTING.md Changelog.md Changelog.md LICENSE LICENSE MODULE.bazel MODULE.bazel Migration.md Migration.md NEWS NEWS README.md README.md api.md.in api.md.in package.xml package.xml tutor
ials.md.in tutorials.md.in View all files Repository files navigation README Contributing Apache-2.0 license Security More items Gazebo Sensors : Sensor models for simulation Maintainer: ichen AT openrobotics DOT org Build Status Test c
rage GitHub: Ubuntu Noble Jenkins: Ubuntu Noble Jenkins: Homebrew Jenkins: Windows Gazebo Sensors, a component of Gazebo , provide
```

### ptprepo

https://github.com/richardcochran/linuxptp

Pattern: `GPL|license|PTP`

```text
GitHub - richardcochran/linuxptp: User space PTP stack for the GNU/Linux operating system. · GitHub Skip to content Navigation Menu Sign in Products Platform GitHub Repository hosting, cod
r window. Reload to refresh your session. Dismiss alert {{ message }} richardcochran linuxptp Repository navigation Code Pull requests 11 ( 11 ) Actions Security and quality Insights More items linuxptp Public Notifications You must
 232 ( 232 ) Star 443 ( 443 ) You must be signed in to star a repository About User space PTP stack for the GNU/Linux operating system. Resources Readme GPL-2.0 license Activity Stars 443 stars Watchers 29 watching Forks 232 forks Re
ile.h power_profile.h pqueue.c pqueue.c pqueue.h pqueue.h print.c print.c print.h print.h ptp4l.8 ptp4l.8 ptp4l.c ptp4l.c raw.c raw.c raw.h raw.h refclock_sock.c refclock_sock.c refclock_sock.h refclock_sock.h rtnl.c rtnl.c rtnl.h rt
nl.h sad.c sad.c sad.h sad.h View all files Repository files navigation README GPL-2.0 license More items Introduction This software is an implementation of the Precision Time Protocol (PTP) according to IEEE standard 1588 for Linux.
I) offered by the Linux kernel. Supporting legacy APIs and other platforms is not a goal. License The software is copyrighted by the authors and is licensed under the GNU General Public License. See the file, COPYING, for details of the
license terms. Features Supports hardware and software time stamping via the Linux SO_TIMESTAMPING socket option. Supports the Linux PT
```

### umilicense

https://raw.githubusercontent.com/real-stanford/universal_manipulation_interface/main/LICENSE

Pattern: `MIT|License|Copyright`

```text
MIT License Copyright (c) 2023 Columbia Artificial Intelligence and Robotics Lab Permission is hereby granted, free of charge, to any person obtaining a copy of
 files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to
whom the Software is furnished to do so, subject to the following conditions: The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software. THE SOFTWARE IS PROVIDED "AS IS"
, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HO
```

### pipelinelicense

https://raw.githubusercontent.com/ros-perception/image_pipeline/rolling/image_pipeline/package.xml

Pattern: `license|BSD`

```text
a driver and higher-level vision processing. Vincent Rabaud Jacob Perron Michael Ferguson BSD https://index.ros.org/p/image_pipeline/ https://github.com/ros-perception/image_pipeline/issues https://github.com/ros-perception/image_pip
```

## Coverage and handoff

- **Sensor characteristics, uncertainty & noise** — Fundamental; accessibility 5 - Easy: Recorded data and Python plots suffice initially; long stationary captures are needed for useful low-frequency noise characterization.
- **Joint encoders & proprioceptive sensing** — Fundamental; accessibility 4: A small breakout and magnet are approachable; a repeatable mechanical mount still takes care.
- **IMUs: accelerometers, gyroscopes & magnetometers** — Fundamental; accessibility 4: USB or MCU breakout logging is easy; reliable calibration needs deliberate motion, stationary tests and consistent coordinate frames.
- **Force/torque sensing & current-based torque estimation** — Applied; accessibility 3: Existing actuator current telemetry keeps entry cost low; calibrated multi-axis force hardware and safe load fixtures are harder.
- **RGB cameras & intrinsic calibration** — Fundamental; accessibility 5 - Easy: An existing webcam and printed target suffice; software students can inspect reprojection errors without building electronics.
- **Depth cameras: stereo, structured light & ToF** — Applied; accessibility 4: A single entry depth camera can produce a point cloud quickly; calibration, surface failures and delivered kit prices require checking.
- **2D & 3D LiDAR hardware** — Applied; accessibility 3: A 2D bench scan is accessible; 3D devices, power/network integration and calibrated mounts raise the cost.
- **Short-range ranging: ultrasonic, infrared & ToF** — Fundamental; accessibility 5 - Easy: Single-sensor breakouts make a simple ruler-versus-reading exercise; interfaces reuse Embedded knowledge.
- **Extrinsic & multi-sensor calibration** — Applied; accessibility 3: A webcam/IMU pair is affordable, but transforms, observability and data quality are more demanding than running a single sensor.
- **Time synchronization & timestamping** — Applied; accessibility 3: Timestamp audits are cheap; verified hardware synchronization requires compatible devices and measurements of residual timing error.
- **ROS 2 sensor drivers, metadata & recording** — Applied; accessibility 4: Recorded or simulated topics allow a no-hardware start; real devices add bandwidth and driver-version constraints.
- **Sensor simulation & noise models** — Applied; accessibility 4: Gazebo offers a no-hardware route; Isaac Sim has separate GPU and deployment requirements, not a guaranteed free compute setup.
- **Event cameras & asynchronous acquisition** — Frontier; accessibility 3: File-based exploration avoids a camera purchase; real timing and bias calibration remain specialist work.
- **mmWave radar sensing hardware** — Frontier; accessibility 2: A supported evaluation kit helps, but RF configuration, clutter tests and raw-data access add integration risk; budget is a conservative planning allowance.
- **Robot skin & distributed tactile hardware** — Frontier; accessibility 2: A small patch is plausible within an entry budget; reliable large-area packaging, fabrication and drift tests are substantially harder.
- **Microphone arrays & robot audio acquisition** — Applied; accessibility 4: A USB array gives quick multichannel recording; reverberation and motor noise make on-robot validation harder.
- **GNSS & RTK receiver hardware** — Applied; accessibility 3: An outdoor receiver, antenna and correction source are feasible, but two-receiver setups and field validation need more budget and logistics.
- **Wrist cameras & multi-camera data-collection rigs** — Applied; accessibility 4: Commodity cameras are approachable for software students; mounts, USB bandwidth and actual capture-time alignment still require engineering.

Part 1 snapshot: 18 knowledge nodes; 31 reference hardware/tools; 67 distinct substantive 200-OK sources. Projects and top3 were deferred at this point and are now supplied in part 2 below. Knowledge/tool rows remain To verify; this is discovery, not the independent verifier pass. Sources may overlap across rows and are counted once. No physical hardware, performance benchmarks or visual UI were tested.

## Validation

Ran `python /home/ubuntu/validate_sensing.py` against the JSON, checked-in schema, pilot key sets and accepted HTTP-200 rows of this report. The only extra node key relative to the corrected pilot is the explicitly requested `_accessibility_reason`. No auto-managed reverse relations are emitted. All reference-tool relations resolve to local Sensing nodes; every node has a reference tool. No application test runner is defined in this data-only repository; the data audit is the relevant check.

```text
PASS: 18 knowledge nodes; 31 reference tools; exact pilot keys (+ required _accessibility_reason on nodes).
PASS: schema select/multi-select values, field types, unique names, no Embedded/Manipulation duplicates, local tool relations, all nodes covered.
PASS: every row has >=1 accepted HTTP-200 source; 67 distinct accepted sources, 62 used in rows; status=To verify; no Used in projects.
PASS: project_candidates=[]; top3=[]; all release years null except directly sourced 2024 AnySkin and UMI.
```

The first staged whitespace check flagged trailing spaces inside fetched excerpts; these were mechanically trimmed without changing claims or source URLs. The final `git diff --cached --check` returned exit 0 with no output. No physical sensor demo or independent verifier pass was performed. The home-directory Python generator, fetch scripts, validator and evidence cache are retained for continuation but are not additional repository deliverables.

## Part 2: additional source discovery and saturation

Three additional discovery batches used web searches for (1) Prophesee recorded data/calibration, (2) TI radar raw capture/calibration, and (3) robot-camera calibration/data integrity. Search results selected URLs; only the direct curl/grep audit below qualifies evidence. Batches were evaluated against the existing Knowledge + Robots & Models entry count, not projects (proposals are synthesis, not discovered products).

| Batch | Entries before | New nodes | New reference tools | New entries / prior entries | New substantive URLs | Result |
|---|---:|---:|---:|---:|---:|---|
| Event acquisition/calibration | 49 | 0 | 0 | 0/49 = 0% | 2 | below 10% |
| Radar raw capture/calibration | 49 | 0 | 2 | 2/49 = 4.08% | 3 | below 10% |
| Camera metadata/data integrity | 51 | 0 | 0 | 0/51 = 0% | 3 | below 10% |

**Saturation reached: yes**, under the requested entry-based rule: three consecutive new discovery/fetch batches each added less than 10% new nodes/reference tools. This does not imply every product or possible project was enumerated. The radar batch genuinely added TI DCA1000EVM and TI mmWave Studio; these make raw-capture hardware and the Windows-host constraint explicit. No new node was warranted. The third batch also re-opened the existing UMI page: it is logged, but not counted as a new distinct URL. One guessed event-camera synchronization URL returned 404 and is excluded. New sources were attached to affected knowledge rows; no launch years or numerical prices were inferred.

### Additional fetch-status log

| Key | Status | Bytes | Decision | URL |
|---|---:|---:|---|---|
| eventsamples | 200 | 34628 | accepted | https://docs.prophesee.ai/stable/datasets.html |
| eventcal | 200 | 90730 | accepted | https://docs.prophesee.ai/stable/samples/modules/calibration/calibration_pipeline.html |
| eventtime | 404 | 4308 | rejected: status or no substantive match | https://docs.prophesee.ai/stable/hardware/cameras/synchronization.html |
| dca1000 | 200 | 257651 | accepted | https://www.ti.com/tool/DCA1000EVM |
| mmwavestudio | 200 | 259952 | accepted | https://www.ti.com/tool/MMWAVE-STUDIO |
| radartraining | 200 | 786265 | accepted | https://www.ti.com/video/series/mmwave-training-series.html |
| camerainfo | 200 | 6319 | accepted | https://raw.githubusercontent.com/ros2/common_interfaces/rolling/sensor_msgs/msg/CameraInfo.msg |
| jointstate | 200 | 999 | accepted | https://raw.githubusercontent.com/ros2/common_interfaces/rolling/sensor_msgs/msg/JointState.msg |
| lerobotdataset | 200 | 205572 | accepted | https://huggingface.co/docs/lerobot/lerobot-dataset-v3 |
| umihardware | 200 | 34874 | accepted | https://umi-gripper.github.io/ |

### Additional grepped evidence

#### eventsamples

https://docs.prophesee.ai/stable/datasets.html

Pattern: `RAW|EVT3|recording|HDF5`

```text
Recordings and Datasets — Metavision SDK Docs 5.3.1 documentation METAVISION INTELLIGENCE BUY PRODUCTS PROPHESEE CONTACT Metavision SDK Docs 5.3.1 Di
ted Architecture Programming Guides Code Samples Python Tutorials Algorithms and API Data Recordings and Datasets Sample recordings Datasets Precomputed Datasets Data Encoding Formats Streaming and Decoding File Formats Hardware Supported
Camera Plugin Upgrade Guide Open Source Licenses FAQ Glossary Index Metavision SDK Docs » Recordings and Datasets Recordings and Datasets  Sample recordings  Those recordings are available in multiple formats: RAW ( EVT2 or EVT3 ), DAT a
nd HDF5 event files . Note Those files are shared under the Creative Commons Zero v1.0 Universal (CC0 1.0) license . This means that you are free t
the full license details . Name Screenshot Description Sensor Duration Event Rate (Mev/s) Recordings spinner Turning Spinner Gen3.0 5 s 10.8 HDF5 (152.8 MB) RAW EVT2 (207.9 MB) DAT (413.2 MB) hand_spinner Turning 3-Blade Hand Spinner Gen3.
1 5 s 2.4 HDF5 (38.7 MB) RAW EVT2 (46.9 MB) laser High-speed laser motion Gen4.1 3 s 38.8 HDF5 (236.5 MB) RAW EVT3 (326.2 MB) 80_balls Falling 80 balls (to use with Counting Sample ) Gen3.0 6.3 s 0.73 HDF5 (14.8 MB) RAW EVT2 (19.2 MB)
articles of different sizes (synthetic data) (to use with PSM Sample ) Gen3.1 32 ms 322.4 HDF5 (58.2 MB) RAW EVT2 (77.3 MB) industrial_fluid_flow Particles suspended and moving within a fluid flow Gen4.0 5.6 s 1.9 HDF5 (35 MB) RAW EVT
(43 MB) ind
```

#### eventcal

https://docs.prophesee.ai/stable/samples/modules/calibration/calibration_pipeline.html

Pattern: `intrinsic|validation|re.projection`

```text
tion_recording samples. Quick start guide  If you are just interested in calibrating the intrinsics of a camera, you can run the following command: Linux metavision_calibration_pipeline Windows metavision_calibration_pipeline.exe It will
start a live intrinsics calibration pipeline that will detect a calibration pattern from different viewpoints and estimates the intrinsics from those detections.
ve marker pattern), the user can press the ‘q’ key to stop the process and proceed to the intrinsics estimation step. The intrinsics estimation step will use the detections to estimate the camera intrinsics. When the estimation is done, th
e pipeline will automatically execute the intrinsics validation step. The intrinsics validation step will display the detected pattern, the re-projected pattern using the estimated intrinsics and the re-projection errors. The user can
er the step should be executed. Can be useful to only restart parts of the pipeline (e.g. intrinsics estimation using a different camera model). Each step generally have additional fields that are specific to its function. Some of those sp
emented in Metavision SDK include: Event-based pattern detection ( eb-pattern-detection ) Intrinsics estimation ( intrinsics-estimation ) Intrinsics validation ( intrinsics-validation ) Event-based synchronized patterns detection ( eb-sync
ed-pattern-detection ) Extrinsics estimation ( extrinsics-estimation ) Extrinsics validation ( extrinsics-validation ) Example JSON file  {
```

#### dca1000

https://www.ti.com/tool/DCA1000EVM

Pattern: `DCA1000|LVDS|raw|Ethernet`

```text
DCA1000EVM Evaluation board | TI.com Home Design & development DCA1000EVM DCA1000 evaluation module for real-time data capture and streaming Order now DCA1000EVM Order now Overview The DCA1000 evaluation module (EVM) prov
ime data capture and streaming for two- and four-lane low-voltage differential signaling (LVDS) traffic from TI AWR and IWR radar sensor EVMs. The data can be streamed out via 1-Gbps Ethernet in real time to a PC running the MMWAVE-ST
and algorithm development. Features Supports lab and mobile collection scenarios Captures LVDS data from AWR/IWR radar sensors Streams output in real time through 1-Gbps Ethernet Controlled via onboard switches or GUI/library DCA1000E
VM Warranty card (disclaimer sheet) Ethernet cable Standoffs Samtec® coaxial micro ribbon cable (HQCD-030-02.00-SEU-TBR-1) Audio & radar DSP SoCs AM2732-Q1 — Automotive dual-core Arm®
Cortex-R5F MCU up to 400 MHz with C66x DSP, Ethernet, safety, security Automotive mmWave radar sensors AWR1243 — 76-GHz to 81-GHz high-performance automotive MMIC AWR1443 — Single-chip 76-GHz
, DSP and MCU DC/DC converters LM26400Y — Dual 2A, 500kHz Wide Input Range Buck Regulator Ethernet PHYs DP83867IR — Industrial temperature, robust gigabit Ethernet PHY transceiver Industrial mmWave radar sensors IWR1443 — Single-chip 76-G
ingle-chip, 76GHz to 81GHz industrial high-performance radar with integrated DSP, MCU and ethernet IWR6443 — Single-chip 60-GHz to 64-GHz intelligent mmWave sensor integrating MCU and hardwa
```

#### mmwavestudio

https://www.ti.com/tool/MMWAVE-STUDIO

Pattern: `capture|mmWave|calibration`

```text
MMWAVE-STUDIO IDE, configuration, compiler or debugger | TI.com Home Design & development MMWAVE-STUDIO mmWave studio Downloads MMWAVE-STUDIO Down
loads Overview MMWAVE-STUDIO is a stand-alone Windows® GUI that provides the ability to configure and control mmWave sensor modules and collect analog-to-digital
 (ADC) data for offline analysis. ADC data capture is intended to enable evaluation and characterization of radio-frequency (RF) performance, and PC development of signal-processing algorith
ms. MMWAVE-STUDIO provides the capability to evaluate and prototype chirp designs and experiment with advanced features of our radar devices. MMWAVE-S
g low-level chirp parameters. It is not needed for typical evaluation of our radar demos. MMWAVE-STUDIO provides basic post-processing and visualization of ADC data, as well as post-processing examples based on MATLAB®, which can be use
d as getting-started reference. MMWAVE-STUDIO connects directly to our sensor modules and requires: DCA1000EVM connected to BOOST and ISK sensor modules for streaming of ADC data
 to PC for capture MMWCAS-DSP-EVM connected to MMWCAS-RF-EVM (cascade imaging) sensor module is required for streaming of ADC data to PC for capture MMWAVE-ST
 includes a standalone utility for the DCA1000EVM that can be used independently from the MMWAVE-STUDIO GUI and used to capture application-specific data. This capability is demonstrated by MMWAVE-SDK. Features Post-processing of ADC da
rd control (SOP change, reset contro
```

#### radartraining

https://www.ti.com/video/series/mmwave-training-series.html

Pattern: `mmWave|radar|training`

```text
mmWave radar sensors | TI.com Home Design & development Educational resources Video Series mmWave radar sensors Home Design & development Educational re
sources Video Series mmWave radar sensors VIDEO SERIES mmWave radar sensors The mmWave training curriculum provides foundational content and hands-on examples for you to learn the fundamentals of FMCW technology and mmWave sensors to s
tart development quickly. Our portfolio of mmWave sensors include: Automotive mmWave radar sensors and industrial mmWave radar sensors. View series mmWave radar sensors Introduction to mmWave radar sensing: FMCW radars ( 5 ) Intro
 to mmWave Sensing : FMCW Radars - Module 1 : Range Estimation 00:22:22 Intro to mmWave Sensing : FMCW Radars - Module 2 : The Phase of the IF Signal 00:16:27 Intro to mmWave Sensing : FMCW Radars - Module 3 : Velocity Estimati
on 00:13:51 Intro to mmWave Sensing : FMCW Radars - Module 4 : Some System Design Topics 00:16:30 Intro to mmWave Sensing : FMCW Radars - Module 5 : Angle Estimation 00:18:42 mmWave radar
sensor devices ( 14 ) TI Automotive mmWave Sensors Device Overview 00:20:34 TI Industrial mmWave Sensors Device Overview 00:20:32 Introduction to mmWave SDK 00:15:53 DCA1000 Training Video 00:16:42 mmWave Radar Programming Model 00:24:3
2 mmWave EVMs Deep Dive 00:06:23 Hardware Setup for IWR6843ISK and IWR6843ISK-ODS 00:09:22 Hardware Setup for IWR6843AOP 00:08:38 Hardware Setup for
 MMWAVEICBOOST and antenna module 00:12:35 Introduction to mmWave Sensor 144
```

#### camerainfo

https://raw.githubusercontent.com/ros2/common_interfaces/rolling/sensor_msgs/msg/CameraInfo.msg

Pattern: `calibration|frame|timestamp|distortion`

```text
########################################## # Time of image acquisition, camera coordinate frame ID std_msgs/Header header # Header timestamp should be acquisition time of image # Header frame_id should be optical frame of camera # orig
in of frame should be optical center of camera # +x should point to the right in the image # +y should point down in the image # +z should point into t
ne of the image ####################################################################### # Calibration Parameters # ####################################################################### # These are fixed during camera calibration. Their val
mally this will be the full camera resolution in pixels. uint32 height uint32 width # The distortion model used. Supported models are listed in # sensor_msgs/distortion_models.hpp. For most cameras, "plumb_bob" - a # simple model of radial
and tangential distortion - is sufficent. string distortion_model # The distortion parameters, size depending on the distortion model. # For "plumb_bob", the 5 parameters are: (k1, k2, t1, t2, k3). float64[] d # Intrinsic
es. # [fx 0 cx] # K = [ 0 fy cy] # [ 0 0 1] # Projects 3D points in the camera coordinate frame to 2D pixel # coordinates using the focal lengths (fx, fy) and principal point # (cx, cy). float64[9] k # 3x3 row-major matrix # Rectificat
ntrinsic matrix for the rectified image. # It projects 3D points in the camera coordinate frame to 2D pixel # coordinates using the focal lengths (fx', fy') and principal
```

#### jointstate

https://raw.githubusercontent.com/ros2/common_interfaces/rolling/sensor_msgs/msg/JointState.msg

Pattern: `position|velocity|effort|empty`

```text
rolled joints. # # The state of each joint (revolute or prismatic) is defined by: # * the position of the joint (rad or m), # * the velocity of the joint (rad/s or m/s) and # * the effort that is applied in the joint (Nm or N). # # Each j
state. # The goal is to make each of the fields optional. When e.g. your joints have no # effort associated with them, you can leave the effort array empty. # # All arrays in this message should have the same size, or be empty. # This i
 the joint name with the correct # states. std_msgs/Header header string[] name float64[] position float64[] velocity float64[] effort
```

#### lerobotdataset

https://huggingface.co/docs/lerobot/lerobot-dataset-v3

Pattern: `video|timestamp|metadata|dataset`

```text
LeRobotDataset v3.0 · Hugging Face Hugging Face Search models, datasets, users... Ctrl K Models Datasets Spaces Buckets Docs Enterprise Pricing Website Tasks HuggingChat Collections Languages Organizations Comm
Providers Inference Endpoints Storage Buckets Log In Sign Up LeRobot documentation LeRobotDataset v3.0 LeRobot 🏡 View all docs AWS Trainium & Inferentia Accelerate Bitsandbytes CLI Chat UI Dataset viewer Datasets Deploying on AWS Diffuse
name Map and Empty Cameras Compute & Hardware Compute Hardware Guide PyTorch accelerators Datasets Using LeRobotDataset Training Dataset Streaming Porting Large Datasets Using the Dataset Tools Language Columns and Recipes Tools Annotati
on Pipeline Video encoding parameters Streaming Video Encoding Policies ACT SmolVLA π₀ (Pi0) π₀-FAST (Pi0Fast) π₀.₅ (Pi05) FineART-VLA MolmoAct2 VLA-JEPA LaWAM EO-1 LingBot-VA LingBot-VLA 2.0 O
iting docstrings Backward compatibility API Reference Robots Teleoperators Cameras Motors Datasets Policies Processors Environments Configuration Join the Hugging Face community and get access to the augmented documentation experience Co
llaborate on models, datasets and Spaces Faster examples with accelerated inference Switch between documentation themes Sign Up to get started Copy page LeRobotDataset
v3.0 LeRobotDataset v3.0 is a standardized format for robot learning data. It provides unified access to multi-modal time-series data, sensorimotor signals and
 multi‑camera video, as well as rich metadata for i
```

#### umihardware

https://umi-gripper.github.io/

Pattern: `camera|latency|GoPro`

```text
licy learning, UMI incorporates a carefully designed policy interface with inference-time latency matching and a relative-trajectory action representation. The resulting learned policies are hardware-agnostic and deployable across multip
n we capture sufficient information for a wide variety of tasks with just a wrist-mounted camera? UMI’s data collection hardware takes the form of a hand-held parallel jaw gripper, mounted with a GoPro camera ①. To gather policy-deploya
cific robot kinematic constraints ⑥. · Policy Robustness Enabled by our unique wrist-only camera setup and camera-centric action representations, UMI is 100% calibration-free (functioning even with base movement) and robust against dist
t (between robot and gripper). --> Ablation Without inference-time observation and action latency matching, the policy exhibits significantly more jittery movements, due to the misalignment between observations and action executions. Our
s No Latency Matching (2) Cup Arrangement ☕ Task Pick up and place an espresso cup on the saucer with its handle facing to the left of the robot. Capabi
y of learning multi-modal action distributions and sense relative depth through monocular camera observation and side mirrors. --> Ablation Data collected by UMI is robot agnostic. Here we can deploy the same policy on both UR5e and Fra
 with the Franka setup. We especially thank Steffen Urban for his open-source projects on GoPro SLAM and Camera-IMU calibration, and John @ 3D printing world fo
```

## Project synthesis and duplicate review

54 distinct proposals: three primary proposals per node, plus limited multi-node relations for meaningful integration. Onboarding includes synthetic/recorded €0 work and small hardware demos; later projects progress to custom calibration fixtures, event-camera acquisition, raw radar capture, modular magnetic skin and a VLA-ready acquisition rig. All remain Sensing-led: acquisition experiments are scripted, so autonomy is deliberately not inflated to learned/open-world robot behavior. Novelty ranges from reproduce to original fixture/protocol; no Beyond SOTA claim. Hardware and integration range from single off-the-shelf components to custom subsystems/full acquisition stacks. Four-axis values are stored; no computed Level or reverse relations are emitted.

Titles and descriptions/deliverables of all 11 existing projects, 28 Embedded candidates and 51 Manipulation candidates were read before synthesis. Concept collisions were removed or explicitly narrowed:
- No servo bring-up, SO-101 assembly, micro-ROS publisher, real-time controller jitter benchmark, firmware CI, BLDC test-bench dynamics or contact detector. Current/torque work is static metrology against an independent load reference, not Embedded's learned contact detector or actuator step response.
- No tactile slip detector, fingertip friction comparison, compliant insertion, teleoperation training workflow, policy fine-tuning, pick-and-place, world model or sim-to-real policy training. Skin work is material/readout/packaging metrology rather than manipulation control.
- Manipulation's “Audit demonstration timing” already plots camera/joint alignment and missing demonstration frames. Sensing proposals instead isolate capture-versus-arrival clocks, hardware exposure skew, PTP, USB topology, message units/covariance and calibration provenance. The final acquisition rig does not duplicate that action-alignment audit or train a policy.
- The camera fixture does not redesign a gripper; sensor simulation compares measurement response, not an SO-101 electronics or policy digital twin. Audio work is acquisition/noise characterization, not keyword control or localization implementation. Radar work does not implement detection, odometry or surveillance.

Durations, cost bands, work shares and wow factors are planning judgments; no completed result or guaranteed stock/price is asserted. Physical work requires compatibility/procurement checks and safe fixtures. Existing host compute is assumed; €0 means synthetic/replayed data without new hardware, not free compute. Professional sensor loans may be needed within the proposed €500-5k experiments. One-week onboardings assume a supported setup and pre-provisioned data/parts. mmWave Studio requires an appropriate Windows host; no attempt was made to install it on this Linux machine. Project references are fetched official technical sources, not evidence that our proposed experiment has already succeeded.

### Per-node project coverage

- **Sensor characteristics, uncertainty & noise** (4): Measurement truth versus resolution: a sensor-error notebook; Sampling-rate aliasing on a moving distance target; Stationary IMU warm-up and temperature-drift dossier; Gazebo noise-model fingerprint with known ground truth
- **Joint encoders & proprioceptive sensing** (3): Encoder rollover and index-reference explorer; Magnet alignment and standoff repeatability jig; Incremental versus magnetic joint-angle metrology fixture
- **IMUs: accelerometers, gyroscopes & magnetometers** (5): Stationary IMU warm-up and temperature-drift dossier; IMU units, missing orientation and axis-sign replay; Allan-deviation repeatability across stationary sessions; IMU mount vibration transmission comparison; Camera-IMU calibration excitation and held-out residual study
- **Force/torque sensing & current-based torque estimation** (3): Six-axis wrench units and lever-arm replay; Wrist transducer zeroing and load-fixture calibration; Motor-current torque estimate versus an independent load reference
- **RGB cameras & intrinsic calibration** (5): Checkerboard coverage and calibration holdout gallery; Rolling-shutter and exposure artifact ruler; Focus and resolution changes invalidate camera calibration; Hardware-trigger exposure-skew measurement fixture; Quick-release wrist-camera remount calibration fixture
- **Depth cameras: stereo, structured light & ToF** (3): Depth-camera surface and illumination failure gallery; Close-range stereo occlusion and minimum-distance test rig; RGB-depth registration against a measured stepped target
- **2D & 3D LiDAR hardware** (4): Planar LiDAR scan geometry and blind-zone bench; LiDAR reflectivity and incidence-angle return audit; 3D LiDAR coverage and timestamped scan-density atlas; Remountable camera-LiDAR calibration target and fixture
- **Short-range ranging: ultrasonic, infrared & ToF** (5): Sampling-rate aliasing on a moving distance target; Ultrasonic beam-width and soft-surface echo chart; Analog infrared range curve and blind-zone calibration; ToF range validity across target color and ambient light; Measured short-range sensor response versus simulated rays
- **Extrinsic & multi-sensor calibration** (5): RGB-depth registration against a measured stepped target; Hand-eye calibration observability in a synthetic camera rig; Camera-IMU calibration excitation and held-out residual study; Remountable camera-LiDAR calibration target and fixture; Reusable event-RGB calibration target and coverage protocol
- **Time synchronization & timestamping** (5): 3D LiDAR coverage and timestamped scan-density atlas; Acquisition-time versus arrival-time timestamp sandbox; Hardware-trigger exposure-skew measurement fixture; PTP clock alignment under sensor-network load; Long-recording microphone sample-clock drift audit
- **ROS 2 sensor drivers, metadata & recording** (6): ROS sensor-message units and covariance contract linter; Sensor QoS loss-versus-latency capture experiment; Recording archive recovery and calibration-manifest integrity; Synthetic sensor outage and saturation playback harness; GNSS receiver position-time metadata ingestion contract; VLA-ready sensing rig with verifiable calibration provenance
- **Sensor simulation & noise models** (3): Gazebo noise-model fingerprint with known ground truth; Synthetic sensor outage and saturation playback harness; Measured short-range sensor response versus simulated rays
- **Event cameras & asynchronous acquisition** (3): Recorded event-stream polarity and time microscope; Event-camera illumination-flicker throughput envelope; Reusable event-RGB calibration target and coverage protocol
- **mmWave radar sensing hardware** (3): Radar point-cloud capture and no-target baseline; Radar ADC capture throughput and packet-loss characterization; Reproducible radar multipath and material test enclosure
- **Robot skin & distributed tactile hardware** (4): Magnetic skin patch replacement repeatability bench; Magnetic skin array crosstalk and wiring characterization; Removable forearm skin sleeve with calibration identity; VLA-ready sensing rig with verifiable calibration provenance
- **Microphone arrays & robot audio acquisition** (3): Microphone channel ordering and geometry clap board; Robot motor-noise audio acquisition dossier; Long-recording microphone sample-clock drift audit
- **GNSS & RTK receiver hardware** (3): RTK stationary receiver and correction-outage logbook; GNSS antenna mounting and multipath repeatability survey; GNSS receiver position-time metadata ingestion contract
- **Wrist cameras & multi-camera data-collection rigs** (5): Recording archive recovery and calibration-manifest integrity; Removable forearm skin sleeve with calibration identity; Multi-camera USB topology and capture-bandwidth atlas; Quick-release wrist-camera remount calibration fixture; VLA-ready sensing rig with verifiable calibration provenance

### Top three nodes

The ratio is qualitative (accessibility × visual impact × relevance / cost), not a numerical score derived from ordinal select values.

- **Wrist cameras & multi-camera data-collection rigs**: Best direct link to the low-cost SO-101/LeRobot wedge: a small USB rig yields an immediately filmable multi-view stream and reusable acquisition infrastructure without claiming a policy result. Commodity entry hardware and existing host compute keep the initial experiment modest; synchronization and mounting remain real integration work.
- **RGB cameras & intrinsic calibration**: High accessibility with an existing webcam, printable target and open calibration tools. Distortion correction and held-out reprojection overlays are visually clear, and this knowledge unlocks depth, wrist rigs and multi-sensor data quality without new robot hardware.
- **Depth cameras: stereo, structured light & ToF**: Live depth and point-cloud failures are easy to demonstrate and directly inform tabletop manipulation data collection. A single entry stereo device can give strong visual impact before a complete robot exists; verify actual camera price and host requirements, and do not extend the entry budget to every reference camera.

## Part 2 final validation

Ran the extended `/home/ubuntu/validate_sensing.py`. It reads schema select options, matches row keys against the pilot (plus required node `_accessibility_reason`), checks field types and HTTP-200 fetch-log coverage, verifies numeric effort shares, resolves relation names, checks prerequisite cycles and compares normalized project titles/deliverables against all 90 existing/pilot proposals. Concept-level duplicate review is a separate manual step documented above, not something normalized-title checks can establish. Each knowledge node has 3–6 associated proposals. Knowledge/tool status stays To verify; projects stay Idea.

```text
PASS: 18 knowledge nodes; 33 reference tools; exact pilot keys (+ required _accessibility_reason on nodes).
PASS: schema select/multi-select values, field types, unique names, no Embedded/Manipulation duplicates, local tool relations, all nodes covered.
PASS: every row has >=1 accepted HTTP-200 source; 75 distinct accepted sources, 70 used in rows; status=To verify; no Used in projects.
PASS: 54 projects; exact pilot project keys; all schema selects; effort sums=100; status=Idea; fetched HTTP-200 References.
PASS: project relations resolve across Sensing/pilots; prerequisite DAG is acyclic; 3-6 candidates per node; 3 valid top3 recommendations.
PASS: no normalized title/deliverable duplicates internally or against 90 existing/pilot projects; concept overlap manually reviewed in report.
COUNTS: {"accepted_sources": 75, "nodes": 18, "project_candidates": 54, "project_kinds": {"Onboarding": 18, "Project": 36}, "robots_models": 33, "top3": 3}
```

`git diff --check` returned exit 0 without output. No application test runner exists for this data-only change. Physical experiments, hardware compatibility/procurement, visual demos, performance claims and independent verification remain untested. No Notion access, PR or main-branch changes.

## Five-line summary

Mapped 18 Sensing nodes and 33 reference sensors/tools, retaining To verify status and beginner-readable scope boundaries.
Proposed 54 deduplicated projects: 18 Onboarding and 36 Project, with 3–6 candidates per node and schema-valid complexity/work-share fields.
Audited 75 distinct substantive HTTP-200 sources; three further discovery batches added 0, 2 and 0 entries, reaching the <10% saturation rule.
Top priorities are wrist/multi-camera rigs, RGB intrinsic calibration and depth cameras, supporting low-cost SO-101/LeRobot data acquisition.
Schema, sources, relations, prerequisite DAG, coverage and duplicate-title checks passed; physical results and independent verification remain outstanding.
