# Verification report: knowledge_perception.json

Rows checked: 113 (20 knowledge nodes, 35 robots/models, 58 project candidates). Verified: 103. Corrected: 10. Rejected: 0.

## Method
- Opened all 80 distinct source/reference URLs with curl. 78 returned HTTP 200. Two did not:
  - `petercorke.com/rvc/home/` first returned 502, then a 301 redirect to `https://petercorke.com/`. The homepage loads and lists "Robotics, Vision & Control (all versions)", so I replaced the URL.
  - `doi.org/10.3390/engproc2026124099` (MDPI) returns 403 to curl. Crossref confirms the paper exists: "Computer Vision for Collaborative Robots in Industry 5.0: A Survey of Techniques, Gaps, and Future Directions", 2026. That matches the claim it supports (gesture recognition and safety monitoring for cobots), so I kept it.
- arXiv: I checked the titles of all 19 cited arXiv IDs on arxiv.org. Each one matches the named paper or model: SAM/SAM 2/SAM 3, DINOv2, Grounding DINO, OWLv2, Depth Anything V2/3, Depth Pro, FoundationStereo, VGGT, DUSt3R, CoTracker3, ByteTrack, ConceptGraphs, OK-Robot, Gemini Robotics, the event-vision survey and the multi-sensor fusion survey. 2512.03422 is "What Is The Best 3D Scene Representation for Robotics?". Crossref confirms the IJCV 2026 event-SLAM survey and the Knowledge-Based Systems 3D scene understanding survey.
- I checked these facts on the pages themselves:
  - Ultralytics docs: YOLO11 released 27 Sept 2024, YOLO26 listed, YOLO27 "coming soon".
  - SAM 3 arXiv HTML gives the affiliation Meta Superintelligence Labs.
  - Depth Anything 3 page: +35.7% camera-pose accuracy over VGGT, plain DINOv2 encoder.
  - vgg-t.github.io: CVPR 2025 Best Paper Award.
  - Livox Mid-360 page: 360°x59° FOV, 0.1 m minimum range, 40 m @10% reflectivity, 265 g.
  - DeepMind blog (25 Sept 2025): Gemini Robotics-ER 1.5 does pointing, detection and success detection.
  - Other pages: FetchBot (CoRL 2025, ML Anthology) and ScrewSplat in the CoRL 2025 program.
  - Builders: all robot/model builders match their official pages or repos.
- Schema checks:
  - Every select and multi-select value matches schemas/notion-schema.md.
  - Every project's work split sums to 100. Onboarding rows leave the 4 axes empty, because Level is 0 for Onboarding.
  - Prerequisites are acyclic. Every project prerequisite is currently empty.
  - All Knowledge-node relation names resolve within the file. Built by / Used by / Relevant orgs are empty, so no Ecosystem organizations needed checking.
- Schema cleanup: I removed the non-Notion key `_accessibility_reason` from all 20 nodes. No `Used in projects` key is present. Project ideas is empty.
- Status: nodes and robots/models are now "To verify". Projects stay "Idea", because the Projects Status field has no "To verify" option.
- Top-level `sources_consulted` URLs got the same two URL fixes. The top-level structure (branch, nodes, robots_models, project_candidates, top3, sources_consulted) is the same as in the other verified knowledge files.

## Flags for human review
- Cross-file relation names: `SO-101`, `LeRobot`, `MuJoCo` and `NVIDIA Jetson Orin Nano Super Developer Kit` appear in project "Robots & models" but are not defined in this file. They are defined in knowledge_manipulation / knowledge_embedded_electronics / ecosystem files, so the syncer must resolve them across files.
- OAK-D Pro, ZED 2 and Livox Mid-360 are sensors, filed as Kind "Simulator/Tool" (no better option exists in the schema). Their Form factor is "N/A".
- Jetson projects ("Edge YOLO on a Jetson with ROS 2", "Edge open-vocabulary detection on Jetson") use the €500-5k cost band. The Jetson price is "unknown" in the embedded-electronics file and the NVIDIA page didn't give a price to curl, so I left the band unchanged. If the dev kit is about $249, these projects belong in <€500.
- Many tools/libraries have Release year null (unknown). I left them null rather than guess.

## Rows

| Table | Row | Verdict | Reason |
|---|---|---|---|
| Knowledge node | Camera models & image formation | corrected | petercorke.com/rvc/home/ gave 502 then 301 to homepage; replaced with https://petercorke.com/ (RVC book page) |
| Knowledge node | Camera calibration (intrinsic, extrinsic & hand-eye) | corrected | petercorke.com/rvc/home/ gave 502 then 301 to homepage; replaced with https://petercorke.com/ (RVC book page) |
| Knowledge node | Classical image processing & feature matching | verified |  |
| Knowledge node | Fiducial markers (AprilTag, ArUco) | verified |  |
| Knowledge node | Stereo & RGB-D depth sensing | corrected | librealsense repo moved to github.com/realsenseai/librealsense; URL updated |
| Knowledge node | Point cloud processing | verified |  |
| Knowledge node | Real-time 2D object detection | verified |  |
| Knowledge node | Promptable image & video segmentation (SAM family) | verified |  |
| Knowledge node | Multi-object tracking | verified |  |
| Knowledge node | Monocular depth estimation | verified |  |
| Knowledge node | Human body & hand pose tracking | verified |  |
| Knowledge node | LiDAR perception & 3D object detection | verified |  |
| Knowledge node | Open-vocabulary detection & grounding | verified |  |
| Knowledge node | Self-supervised visual features (DINOv2-style backbones) | verified |  |
| Knowledge node | Point tracking (track-any-point) | verified |  |
| Knowledge node | Feed-forward 3D reconstruction (DUSt3R / VGGT) | corrected | VGGT wording fixed to "CVPR 2025 Best Paper Award" (per vgg-t.github.io) |
| Knowledge node | Neural scene representations (NeRF & Gaussian splatting) | verified |  |
| Knowledge node | Open-vocabulary 3D scene graphs & semantic maps | verified |  |
| Knowledge node | Vision-language models for embodied perception | verified |  |
| Knowledge node | Event-based vision | verified |  |
| Robot/model | AprilTag 3 library | verified |  |
| Robot/model | Kalibr | verified |  |
| Robot/model | OAK-D Pro | verified |  |
| Robot/model | ZED 2 | verified |  |
| Robot/model | librealsense (RealSense SDK) | corrected | repo moved to github.com/realsenseai/librealsense (RealSense spin-off); URL updated, builder "RealSense" confirmed |
| Robot/model | FoundationStereo | verified |  |
| Robot/model | Open3D | verified |  |
| Robot/model | Point Cloud Library (PCL) | verified |  |
| Robot/model | YOLO11 | verified |  |
| Robot/model | SAM 2 | verified |  |
| Robot/model | SAM 3 | verified |  |
| Robot/model | Grounding DINO | verified |  |
| Robot/model | Grounded-SAM-2 | verified |  |
| Robot/model | OWLv2 | verified |  |
| Robot/model | Florence-2 | corrected | Release year null -> 2023 (HF model card cites arXiv 2311.06242, Nov 2023) |
| Robot/model | Depth Anything V2 | verified |  |
| Robot/model | Depth Anything 3 | verified |  |
| Robot/model | Depth Pro | verified |  |
| Robot/model | DINOv2 | verified |  |
| Robot/model | MediaPipe Hand & Pose Landmarker | verified |  |
| Robot/model | ByteTrack | verified |  |
| Robot/model | CoTracker3 | verified |  |
| Robot/model | TAPIR | verified |  |
| Robot/model | DUSt3R | verified |  |
| Robot/model | VGGT | verified |  |
| Robot/model | nerfstudio | verified |  |
| Robot/model | gsplat | verified |  |
| Robot/model | 3D Gaussian Splatting (reference implementation) | verified |  |
| Robot/model | ConceptGraphs | verified |  |
| Robot/model | OK-Robot | verified |  |
| Robot/model | Gemini Robotics-ER 1.5 | verified |  |
| Robot/model | Livox Mid-360 | verified |  |
| Robot/model | OpenPCDet | verified |  |
| Robot/model | Prophesee Metavision SDK | verified |  |
| Robot/model | Isaac ROS | verified |  |
| Project | Intro: project 3D points onto a webcam image | corrected | dead petercorke.com/rvc/home/ reference replaced with https://petercorke.com/ |
| Project | Intro: calibrate a webcam with a printed board | corrected | dead petercorke.com/rvc/home/ reference replaced with https://petercorke.com/ |
| Project | Intro: color-blob tracker in OpenCV | verified |  |
| Project | Intro: AprilTag pose axes on a live video | verified |  |
| Project | Intro: first YOLO detector on custom objects | verified |  |
| Project | Intro: depth from a single photo | verified |  |
| Project | Camera-to-arm hand-eye calibration for the SO-101 | verified |  |
| Project | Camera-IMU calibration with Kalibr | verified |  |
| Project | Lens-distortion lab: cheap vs. good cameras | corrected | dead petercorke.com/rvc/home/ reference replaced with https://petercorke.com/ |
| Project | Feature-matching panorama and visual odometry toy | verified |  |
| Project | Line-following mobile robot with classical vision | verified |  |
| Project | Tag-based pick targets for the SO-101 | verified |  |
| Project | Tag-based ground truth rig for evaluating learned perception | verified |  |
| Project | Depth camera failure atlas | corrected | librealsense repo moved to github.com/realsenseai/librealsense; reference URL updated |
| Project | Learned stereo vs. on-board stereo | verified |  |
| Project | DIY stereo camera from two webcams | verified |  |
| Project | Tabletop segmentation: find objects on a table in 3D | verified |  |
| Project | Multi-view object scanning with ICP | verified |  |
| Project | Point-cloud grasp targets for the SO-101 | verified |  |
| Project | Edge YOLO on a Jetson with ROS 2 | verified |  |
| Project | Sorting robot: detect and bin objects by class | verified |  |
| Project | Synthetic data for detector training | verified |  |
| Project | Click-to-mask object cutout for robot datasets | verified |  |
| Project | Text-prompted segmentation of every instance with SAM 3 | verified |  |
| Project | Masked observations to make imitation policies robust | verified |  |
| Project | People counter and tracker for a lab entrance | verified |  |
| Project | Tracker benchmark on robot-workspace videos | verified |  |
| Project | Pan-tilt camera that follows a chosen object | verified |  |
| Project | Webcam-only obstacle map from monocular depth | verified |  |
| Project | Replace the depth camera: monocular depth for grasping | verified |  |
| Project | Gesture-commanded robot | verified |  |
| Project | Hand-tracking teleoperation of the SO-101 | verified |  |
| Project | Vision safety zone: slow the arm when a person is near | verified |  |
| Project | 3D detection on KITTI with OpenPCDet | verified |  |
| Project | LiDAR obstacle detection on a mobile robot | verified |  |
| Project | Camera-LiDAR fusion overlay | verified |  |
| Project | Language-pointing arm with open-vocabulary detection | verified |  |
| Project | Open-vocabulary detector shoot-out on lab objects | verified |  |
| Project | Edge open-vocabulary detection on Jetson | verified |  |
| Project | DINOv2 feature visualization and linear probes | verified |  |
| Project | Few-shot object re-identification with DINOv2 features | verified |  |
| Project | Frozen vs. fine-tuned vision encoder for a LeRobot policy | verified |  |
| Project | Turn human videos into motion tracks | verified |  |
| Project | Point-track keypoints as policy inputs | verified |  |
| Project | 3D scan of the lab from phone photos | verified |  |
| Project | Robot-mounted camera to live 3D workspace model | verified |  |
| Project | Gaussian-splat digital twin of a workbench | verified |  |
| Project | Splat-to-simulation asset pipeline | verified |  |
| Project | Language-queryable splat of the lab | verified |  |
| Project | Open-vocabulary 3D map of a room | verified |  |
| Project | Fetch-by-name with a mobile manipulator | verified |  |
| Project | Scene graph change detection: what moved? | verified |  |
| Project | Gemini-ER pointing on the SO-101 | verified |  |
| Project | VLM success detector for robot episodes | verified |  |
| Project | Open VLM vs. API VLM for robot pointing | verified |  |
| Project | Event-camera dataset exploration | verified |  |
| Project | High-speed ball catching cue with an event camera | verified |  |
| Project | Event + frame fusion under extreme lighting | verified |  |
