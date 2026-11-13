# Perception discovery research

## Scope
Discovery only: 20 Perception nodes (5 Fundamental, 7 Applied, 8 Frontier), 35 reference robots/models/tools, 58 project candidates (6 Onboarding, 52 Project). All nodes/models `To verify`, projects `Idea`. No Notion reads/writes. No `Used in projects` or formula fields emitted. 87 distinct source URLs in `sources_consulted`.

Taxonomy grounding: Szeliski *Computer Vision* (2nd ed.), Hartley & Zisserman, Corke *Robotics, Vision & Control*, Stanford CS231n, UMD ENPM673 "Perception for Autonomous Robots" (Spring 2026 syllabus), Gdańsk "3D Vision in Robotics" subject card, UVigo/IMCV photogrammetry & robot vision, and the CoRL 2025 main-conference program (oral session "Perception"). The Springer Handbook page returned a bot challenge and is not cited.

## Boundary decisions (no duplication)
- Not re-created because they exist in `knowledge_manipulation.json`: *Object pose estimation for manipulation*, *Learning-based grasp detection*, *Open-vocabulary & affordance manipulation*. Perception nodes stop at "what/where is it"; acting on it stays in Manipulation.
- Edge AI hardware stays in Embedded & electronics; projects reference `NVIDIA Jetson Orin Nano Super Developer Kit`, `SO-101`, `MuJoCo`, `LeRobot` **by name only** (rows already exist in pilot outputs, not re-emitted here).
- Multi-sensor fusion / VIO / SLAM left to State estimation & SLAM; raw sensor hardware to Sensing; safety certification to HRI & safety.
- Sensors (OAK-D Pro, ZED 2, Livox Mid-360) are `Simulator/Tool` because the schema has no Sensor kind (same convention as the Manipulation pilot for GelSight).

## Queries run
Discovery: `SAM 3 Segment Anything with Concepts paper`; `Depth Anything 3 recovering visual space`; `Gemini Robotics-ER 1.5 embodied reasoning pointing`; `robotic vision course syllabus camera calibration stereo point clouds university`; `robot perception survey open-vocabulary 3D scene understanding 2025`. Plus ~80 primary pages fetched directly (official docs, arXiv abstracts, GitHub repos, project pages, vendor pages).

## Saturation-stop evidence
Unit = new Perception knowledge node; denominator 20.

| Query | New nodes | Mapping |
|---|---:|---|
| `robot perception taxonomy survey detection segmentation tracking depth 3D` | 0 | Cobot CV survey (detection/segmentation/tracking/pose/gesture/safety), scene-understanding survey, multi-sensor fusion survey -> existing nodes or other branches |
| `CoRL 2025 perception papers robot vision foundation models` | 0 | CoRL 2025 Perception oral (6D pose -> Manipulation, FetchBot -> monocular depth, ScrewSplat -> splatting), GraspVLA -> Manipulation |
| `robot perception recent advances 2026 point tracking event cameras gaussian splatting` | 0 | EventGS (IROS 2026), EvTrajGS, IJCV 2026 event-SLAM survey -> event vision / splatting nodes |

Three consecutive queries at 0% new -> stopped.

## Top 3 (accessibility x visual impact x ecosystem relevance / cost, qualitative)
1. **Real-time 2D object detection** — accessibility 5, webcam-cost, reused by many later projects.
2. **Vision-language models for embodied perception** — Google's public SO-101 pointing sample makes a language-driven demo days away; API pricing unknown.
3. **Open-vocabulary detection & grounding** — open models, no training, feeds language-commanded manipulation.

## Gaps and unknowns
- Prices: only OAK-D Pro (US$429, Luxonis shop) is sourced; ZED 2, Livox Mid-360, Prophesee kits and Gemini API pricing are `unknown`. RealSense product pages timed out; only the SDK repo is cited.
- OpenCV docs returned 403 (Cloudflare) and are not cited; OpenCV appears only as text, with no Robots & Models row. ICRA 2025 site returned 403; RSS site gave no usable content. Coverage there uses the CoRL 2025 program only.
- The MDPI cobot survey (doi 10.3390/engproc2026124099) was read through search-result content; direct curl returned 403.
- Licenses: listed as "check" where weights or code have non-commercial or AGPL terms (Ultralytics, DUSt3R, Depth Anything sizes, 3DGS). `Open source` = public code/weights, not a commercial license.
- `Release year` is null where no opened source gave it. `Built by`/`Used by`/`Relevant orgs` are empty, and builders are in `Builder (if not in map)`. European/Paris actors worth linking later: Prophesee (Paris), NAVER LABS Europe (Grenoble), Inria GRAPHDECO.
- Project axes, durations, cost bands, wow and work splits are planning estimates. `Prerequisites` are left empty for the Holygraph architect.
- Candidates for coverage work: learned feature matchers (SuperPoint/LightGlue), transparent-object perception, thermal cameras, 6D pose datasets (BOP), RT-DETR/YOLO-World/YOLOE rows, MASt3R.
