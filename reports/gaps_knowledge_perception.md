# Coverage gaps: knowledge_perception.json (Perception branch)

Reviewed file: `output/knowledge_perception.json` (20 nodes, 35 robots/models, 58 project candidates), after verification (see `reports/verify_knowledge_perception.md`: 103 verified, 10 corrected, 0 rejected).

References compared against: the Springer Handbook of Robotics (2nd ed.) TOC, Part C "Sensing and Perception" (force/tactile, inertial, range sensing, 3D vision and recognition, visual object class recognition, visual servoing, multisensor fusion) plus visual servoing in Part A; Szeliski "Computer Vision: Algorithms and Applications" (2nd ed.) and Corke "Robotics, Vision and Control" chapters; Stanford CS231n, CMU 16-385 and UMD ENPM673 syllabi; ICRA/RSS/CoRL 2024-2026 perception topics (6D pose, visual pretraining for policies, open-vocabulary perception, 3D foundation models); and the LeRobot/SO-101 robot-learning wedge in CLAUDE.md.

Method: I searched the full JSON text for each candidate item; "missing" means 0 mentions or only a passing mention with no node/row. Scope is the Perception branch only. Items that mainly belong to another branch are marked "(cross-branch)". These are well-known items in the field, but I did not reopen their URLs in this pass, so the researcher must source and verify each one before adding a row.

## High

- **6D object pose estimation**, Knowledge node (Applied/Frontier): a core manipulation-perception topic (Springer "3D vision and recognition", a standard ICRA/CoRL track). There is no node and no rows for FoundationPose (NVIDIA), MegaPose/CosyPose (Inria Paris / ENPC) or the BOP benchmark, even though several SO-101 grasp projects need object pose.
- **Visual representations for robot policies (pretrained encoders)**, Knowledge node / Robots & Models: R3M, VC-1, Theia, and the SigLIP/CLIP encoders inside OpenVLA, pi0 and SmolVLA are all missing (SigLIP 0 mentions, CLIP 1). This node is the direct bridge to the robot-learning wedge, and the project "Frozen vs. fine-tuned vision encoder for a LeRobot policy" has no encoder rows to compare apart from DINOv2.
- **Open-weight VLMs for pointing/grounding**: Qwen2.5-VL, Molmo, PaliGemma 2, RoboPoint, Robots & Models. The "Open VLM vs. API VLM for robot pointing" project only links Gemini-ER, Florence-2 and Grounding DINO, so the open-VLM side of the comparison has no candidates.
- **Perception datasets & benchmarks**, Robots & Models: none exist (COCO 0, BOP 0, YCB 0, ScanNet 0, nuScenes 0; KITTI only appears in text). Detector, depth, 3D-detection and scene-graph projects have nothing to evaluate against.
- **Edge deployment & model optimization (ONNX, TensorRT, quantization)**, Knowledge node (Applied): 0 mentions of ONNX, TensorRT or quantization, yet "Edge YOLO on a Jetson" and "Edge open-vocabulary detection on Jetson" depend on it. This is a key skill for real-time on-robot perception.
- **Relevant orgs / Built by empty on every row** (58/58 projects, 35/35 robots & models): the expected perception players are never linked as organizations, including Prophesee (Paris), NAVER LABS Europe (Grenoble), Inria (GRAPHDECO, WILLOW), Meta FAIR Paris, Luxonis, Stereolabs, Intel RealSense, Ultralytics and NVIDIA. This needs ecosystem cross-linking; do not add rows from this file.

## Medium

- **Optical flow & scene flow (RAFT, SEA-RAFT)**, Knowledge node: a standard course and Szeliski topic. 0 mentions.
- **Learned local features & matching (SuperPoint, LightGlue, MASt3R)**, Robots & Models: the classical-features node stops at ORB/SIFT-era methods. MASt3R (NAVER LABS Europe) is the matching successor to DUSt3R.
- **Semantic / instance / panoptic segmentation (Mask R-CNN, SegFormer, Detectron2)**, Knowledge content: the closed-set segmentation baseline that comes before the SAM node (0 mentions).
- **3D hand pose for teleoperation (HaMeR, WiLoR)**, Robots & Models: the "Hand-tracking teleoperation of the SO-101" project only has MediaPipe, which gives coarse 3D.
- **Deep learning on point clouds (PointNet/PointNet++, Point Transformer)**, Knowledge content: 0 mentions. It is the basis for the 3D-detection and point-cloud-grasp projects.
- **Metric monocular depth & geometry (UniDepth, Metric3D v2, MoGe)**, Robots & Models: the monocular-depth node only has Depth Anything and Depth Pro rows. Metric scale matters for grasping.
- **Camera hardware & timing basics (global vs. rolling shutter, exposure, multi-sensor time synchronization, ROS 2 cv_bridge/image_transport)**, Knowledge content: a practical beginner need that is barely covered (synchronization 1 mention, shutter 0).
- **Multisensor fusion (camera-IMU-LiDAR)**, Knowledge node: a Springer Part C chapter, here only one "Camera-LiDAR fusion overlay" project (cross-branch with State estimation & SLAM).
- **Low-cost depth hardware rows: RealSense D435/D405, Orbbec Femto/Gemini**, Robots & Models: RealSense appears only as the SDK row, and Orbbec (the main low-cost alternative since RealSense was spun out) is missing.
- **Data labeling & synthetic data tooling (CVAT, Label Studio, Roboflow, BlenderProc, Isaac Replicator)**, Robots & Models: the "Synthetic data for detector training" and custom-YOLO projects have no tooling rows.
- **Visual servoing**, Knowledge content (cross-branch with Manipulation): a Springer chapter, also flagged in gaps_knowledge_manipulation.md.
- **Project Prerequisites empty on all 58 projects**: no lines between project circles yet. The holygraph-architect should set them.

## Low

- **Radar / mmWave and thermal perception**, Knowledge content: 0 mentions. Niche for us.
- **Time-of-flight sensors (VL53L-series, ToF cameras)**, Robots & Models: cheap range sensing for small robots (cross-branch with Embedded electronics).
- **Tactile and audio perception**, Knowledge content (cross-branch with Manipulation / HRI).
- **Transparent and reflective object perception (ClearGrasp-style)**, Knowledge content: only 2 passing mentions.
- **Volumetric/occupancy mapping (nvblox, Voxblox, KinectFusion)**, Robots & Models (cross-branch with State estimation & SLAM).
- **BEV / occupancy networks for 3D detection (nuScenes-style)**, Knowledge content: an AV-centric frontier, with low accessibility for us.
- **Perception debugging and visualization tools (Rerun, Foxglove)**, Robots & Models: useful for demos and content.
- **Low-cost edge AI cameras (Raspberry Pi AI Camera, Hailo-8L)**, Robots & Models: cheaper alternatives to Jetson and OAK-D.
