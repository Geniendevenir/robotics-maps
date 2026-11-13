# Verification: State estimation & SLAM

Date: **2026-11-13**. Existing branch: `research/knowledge-state-estimation-slam`.

## Outcome

| Collection | Input / retained | Verified unchanged | Corrected | Rejected |
|---|---:|---:|---:|---:|
| Knowledge Map | 16 / 16 | 0 | 16 | 0 |
| Robots & Models | 21 / 21 | 18 | 3 | 0 |
| Project candidates | 48 / 48 | 47 | 1 | 0 |
| **Total** | **85 / 85** | **65** | **20** | **0** |

“Corrected” includes schema-only edits: all 16 knowledge rows lost the non-Notion helper `_accessibility_reason`; their factual content is retained. No database row was rejected. Research recommendations and the source inventory were metadata, not database rows, and are preserved below instead of counted as rejections.

## Method and limits

- Read `devin/playbooks/verifier.md`, `CLAUDE.md` and `schemas/notion-schema.md`. Used the offline schema plus the supplied live difference; **no Notion reads or writes**.
- Opened **all 44 distinct original source/reference URLs**, including every URL in Sources, Best resources, References and the discovery inventory. Each returned readable matching page, repository, raw-file or PDF content through web retrieval. Also opened the official ORB-SLAM3 changelog: **45 distinct URLs in the audit**. The source ledger records what each supports; URL loads are not a claim of independent experimental reproduction or archival permanence.
- Checked each knowledge explanation and frontier statement, each reference-system identity/builder, numeric dates where specified, and stated license/access restrictions. There are no Ecosystem Map organization rows or organization relations to verify for activity in 2026. All robot/tool/model rows have explicit builder text instead of unresolved organization links.
- Verified the actual late-2026 sources: ScaRF-SLAM is listed by its official repository as RA-L 2026; Map2SLAM is a November 2026 preprint; the October LIN-SLAM item is a supplemental paper resource, **not** a promised available implementation. Historical handbook/DynaSLAM evidence is not presented as 2026 SOTA.
- Project outputs are **proposals**, not published capabilities. Duration, accessibility, cost, wow and work split remain planning estimates. The `€0 (sim only)` option covers offline replay/simulation on an existing computer; it does not promise free GPUs, storage or physical sensors. No procurement quote, local build, benchmark or physical demo was performed.
- Retained knowledge and reference-system statuses are **To verify**. All project statuses remain **Idea**, because Projects has no To verify option. Verification verdicts belong in this report, not an invalid Status value.
- Removed discovery-only `branch`, `top3`, `sources_consulted` metadata and all helper properties from the cleaned payload. The only non-property keys left are the necessary structural containers `nodes`, `robots_models`, `project_candidates`; **every database-row property is an exact Notion field name**. No read-only formulas, auto-managed reverse relations or `Used in projects` are output. The source inventory, ranking and accessibility rationales are retained in this report.

## Notable corrections

1. **16 knowledge rows:** removed `_accessibility_reason`; retained the justifications below rather than sending a non-Notion property.
2. **Kalibr:** made its BSD-style advertising acknowledgement requirement explicit in Price / access; the opened raw license has four conditions. The open-source checkbox stays true.
3. **OpenVINS:** set Release year to **2019**, backed by the official August 15 initial-release announcement; made **RPNG, University of Delaware** provenance explicit.
4. **ORB-SLAM3:** changed Release year from **2021 to 2020**. The official changelog calls August 7, 2020 V0.2 the initial release; 2021 describes v1.0 and the journal paper, now distinguished in Key specs.
5. **Stage a sensor-dropout fusion challenge:** an IMU-only outage does not mean prediction-only operation while wheel measurements remain usable. Added an all-usable-measurement gap and clarified continuing wheel updates.

## Row-by-row verdicts

Evidence IDs link to the opened-source ledger. Each row's listed Sources/References were checked, not just its first URL.

### Knowledge Map

| Row | Verdict and one-line reason | Opened evidence |
|---|---|---|
| Bayesian state estimation & uncertainty | **corrected** — removed non-schema helper; Bayesian uncertainty and practical filtering supported by the handbook, course and PythonRobotics. | [S1](#s1), [S3](#s3), [S6](#s6) |
| Wheel & inertial dead reckoning | **corrected** — removed non-schema helper; Wheel integration/drift and fusion conventions match Modern Robotics and ROS documentation. | [S2](#s2), [S8](#s8), [S20](#s20) |
| Kalman filtering & multisensor fusion | **corrected** — removed non-schema helper; EKF/UKF descriptions, covariance and configurable timeouts match official ROS documentation. | [S8](#s8), [S7](#s7), [S3](#s3), [S6](#s6) |
| Particle filtering & global localization | **corrected** — removed non-schema helper; Particle methods and multimodal beliefs supported; recovery remains an experiment, not a guarantee. | [S1](#s1), [S6](#s6) |
| Factor graphs, smoothing & pose-graph SLAM | **corrected** — removed non-schema helper; Graph smoothing and preintegration supported; certifiable bundle-adjustment scope correctly limited. | [S4](#s4), [S5](#s5), [S1](#s1), [S34](#s34) |
| Estimator calibration, timing & observability | **corrected** — removed non-schema helper; Spatial/temporal calibration and observability supported; long-session calibration issue explicitly evidenced. | [S10](#s10), [S11](#s11), [S27](#s27), [S30](#s30), [S37](#s37) |
| Visual odometry & visual-inertial SLAM | **corrected** — removed non-schema helper; ORB-SLAM3 and OpenVINS modes and LaMAria limitations supported; odometry versus SLAM distinction sound. | [S12](#s12), [S11](#s11), [S27](#s27) |
| 2D lidar SLAM & occupancy mapping | **corrected** — removed non-schema helper; Planar mapping, graph reuse/localization and dataset scope supported; not sold as full 3D geometry. | [S13](#s13), [S20](#s20), [S1](#s1), [S43](#s43) |
| 3D lidar-inertial odometry & mapping | **corrected** — removed non-schema helper; Correctly separates lidar-only KISS-ICP, filter LIO, graph LIO and LIVO; FAST-LIVO2 code date supported. | [S16](#s16), [S17](#s17), [S18](#s18), [S19](#s19) |
| Place recognition, loop closure & relocalization | **corrected** — removed non-schema helper; Place proposals versus geometric verification/map reuse correctly distinguished; learned matching not a localization guarantee. | [S12](#s12), [S14](#s14), [S24](#s24), [S1](#s1) |
| Robust, dynamic & lifelong state estimation | **corrected** — removed non-schema helper; Historical DynaSLAM, persistent-map tools and changing-scene benchmarks support the limited snapshot. | [S28](#s28), [S13](#s13), [S27](#s27), [S32](#s32), [S40](#s40), [S43](#s43) |
| Dense, semantic & neural SLAM maps | **corrected** — removed non-schema helper; SplaTAM, MASt3R-SLAM, PINGS, ScaRF-SLAM and Map2SLAM identities/designs supported; no universal SOTA claim. | [S25](#s25), [S23](#s23), [S24](#s24), [S33](#s33), [S26](#s26), [S15](#s15), [S35](#s35), [S36](#s36) |
| Multi-robot & distributed SLAM | **corrected** — removed non-schema helper; Distributed Kimera-Multi and missing module caveat verified; CU-Multi warns against naive trajectory splitting. | [S26](#s26), [S31](#s31), [S1](#s1), [S42](#s42), [S44](#s44) |
| SLAM benchmarking, consistency & failure analysis | **corrected** — removed non-schema helper; Trajectory alignment, absolute/relative errors and control-point/failure-aware evaluation supported. | [S21](#s21), [S22](#s22), [S27](#s27), [S32](#s32), [S11](#s11) |
| Contact-aided & invariant state estimation | **corrected** — removed non-schema helper; Contact-aided implementation/theory and unobservable absolute position/yaw supported by RSS and GTSAM. | [S29](#s29), [S30](#s30), [S4](#s4) |
| GNSS-aided localization & georeferencing | **corrected** — removed non-schema helper; GNSS/heading/frame conversion and LIO-SAM GPS factors supported; no unsupported RTK-precision promise. | [S9](#s9), [S8](#s8), [S18](#s18), [S4](#s4) |

### Robots & Models

| Row | Verdict and one-line reason | Opened evidence |
|---|---|---|
| PythonRobotics | **verified** — Official Atsushi Sakai examples and raw MIT license support builder, scope and open-source flag. | [S6](#s6), [S38](#s38) |
| robot_localization | **verified** — Official CRA/ROS provenance, EKF/UKF and GNSS-transform docs support all stated features. | [S7](#s7), [S8](#s8), [S9](#s9) |
| GTSAM | **verified** — Official Borglab library and 2026 navigation material support factor graphs, interfaces and preintegration. | [S4](#s4), [S5](#s5) |
| Kalibr | **corrected** — Clarified the raw license's fourth-condition advertising acknowledgement; ETH ASL builder and calibration features confirmed. | [S10](#s10), [S39](#s39) |
| OpenVINS | **corrected** — Filled release year 2019 from official initial-release announcement and made RPNG/University of Delaware builder explicit. | [S11](#s11) |
| ORB-SLAM3 | **corrected** — Changed release year 2021 to 2020 from the initial-beta changelog; distinguished 2021 v1.0/paper from first release. | [S12](#s12), [S45](#s45) |
| SLAM Toolbox | **verified** — Official Macenski repository confirms ROS 2 planar graph mapping, serialization/localization and LGPLv2.1. | [S13](#s13) |
| RTAB-Map | **verified** — Official IntRoLab/project site confirms Labbé/Sherbrooke, modalities, loop/memory management and conditional BSD access. | [S14](#s14), [S15](#s15) |
| KISS-ICP | **verified** — Official PRBonn repository confirms lidar-only point-to-point ICP, ROS 2 and MIT; no global-SLAM claim. | [S16](#s16) |
| FAST-LIO2 | **verified** — Official MARS FAST_LIO confirms direct filtering/ikd-tree, July 2021 2.0 update and GPLv2. | [S17](#s17) |
| LIO-SAM | **verified** — Official Shan repository confirms two factor graphs, GPS and ROS 2 branch; sensor conventions remain prerequisites. | [S18](#s18) |
| FAST-LIVO2 | **verified** — Official MARS repository confirms builder, direct LIVO, January 2025 code release and GPLv2. | [S19](#s19) |
| TurtleBot3 | **verified** — Official ROBOTIS manual confirms builder, wheeled modular form and 2017 introduction; present kit price explicitly unknown. | [S20](#s20) |
| evo | **verified** — Official Michael Grupp repository confirms trajectory APE/RPE/alignment, formats and GPLv3. | [S21](#s21) |
| DynaSLAM | **verified** — Official Bescos code plus raw CC BY-NC license support historical scope and false open-source checkbox. | [S28](#s28), [S40](#s40) |
| SplaTAM | **verified** — Official Keetha/Karhade repository confirms RGB-D Gaussian SLAM, CVPR 2024, CUDA and BSD-3 top-level source. | [S25](#s25) |
| MASt3R-SLAM | **verified** — Official Murai/Dexheimer/Davison code confirms dense SLAM/CVPR 2025; noncommercial MASt3R dependency correctly flagged. | [S23](#s23), [S24](#s24) |
| MASt3R | **verified** — Official NAVER code confirms 2024 perception/reconstruction model and CC BY-NC-SA restrictions. | [S24](#s24) |
| Kimera-Multi | **verified** — Official MIT SPARK index/manifest confirm distributed mapping and Noetic; missing Remote Topic Manager not concealed. | [S26](#s26), [S42](#s42) |
| invariant-ekf | **verified** — Official Hartley repository/RSS paper confirm C++ invariant filter, contact examples and BSD-3. | [S29](#s29), [S30](#s30) |
| ScaRF-SLAM | **verified** — Official Oxford DRS repository confirms authors, RA-L 2026, classical-tracking/dense-map split and GPLv3. | [S35](#s35) |

### Projects (Holygraph) candidates

Every row also passed field/option, status, percentage-sum and name-relation checks. References support the underlying techniques; they do not certify the proposed project's success, cost or duration.

| Row | Verdict and one-line reason | Opened evidence |
|---|---|---|
| Animate a one-dimensional robot belief | **verified** — Feasible proposed histogram/Bayes-filter animation; educational references cover beliefs and measurement updates. | [S6](#s6), [S1](#s1) |
| Make covariance visible on a 2D trajectory | **verified** — Covariance-frame/containment experiment is a proposal, with supported estimation resources and no new hardware requirement. | [S6](#s6), [S3](#s3) |
| Expose correlated-sensor overconfidence | **verified** — Shared-noise Monte Carlo is explicitly a custom experiment; no unsupported claim that a cited package solves correlation automatically. | [S6](#s6), [S4](#s4) |
| Watch wheel odometry drift around a square | **verified** — Wheel-increment integration and drift test match the official odometry resource; simulation cost appropriate. | [S2](#s2), [S6](#s6) |
| Separate IMU bias from motion in replay | **verified** — Synthetic known-bias inertial replay is clearly scoped; gravity/frame/global-reference limitations explicit. | [S6](#s6), [S11](#s11) |
| Measure odometry drift on an encoder cart | **verified** — Physical modified cart/IMU/checkpoint work is budgeted separately with 80/10/10 hours and no survey-grade claim. | [S20](#s20), [S2](#s2), [S8](#s8), [S21](#s21) |
| Fuse simulated wheel and IMU messages | **verified** — ROS EKF wheel/IMU simulation, frames and known-noise evaluation match official documented inputs. | [S8](#s8), [S7](#s7), [S6](#s6) |
| Stage a sensor-dropout fusion challenge | **corrected** — Corrected: IMU-only loss can still receive wheel updates; added an all-usable-measurement gap for prediction-only operation. | [S8](#s8), [S21](#s21) |
| Compare filtering and fixed-lag smoothing | **verified** — Equivalent-noise filter/fixed-lag comparison is a proposed custom evaluation, not an assumed fair turnkey benchmark. | [S4](#s4), [S5](#s5), [S8](#s8) |
| Animate particles in a repeated corridor | **verified** — Particle-filter adaptation to ambiguity and resampling is supported by educational examples and handbook. | [S6](#s6), [S1](#s1) |
| Recover after a simulated robot kidnapping | **verified** — Explicitly tests global particle injection/recovery or failure rather than guaranteeing kidnapping recovery. | [S6](#s6), [S1](#s1) |
| Trade localization precision for particle budget | **verified** — Particle-budget sweep is a well-scoped simulation; report error and compute, not an unsupported runtime guarantee. | [S6](#s6), [S21](#s21) |
| Close a tiny pose graph | **verified** — Anchored GTSAM pose graph is supported; gauge freedom and controlled noise explicitly considered. | [S4](#s4), [S5](#s5), [S1](#s1) |
| Reject a malicious loop constraint in a toy graph | **verified** — Labeled false constraints and robust-loss comparison are proposed defensively; failure cases retained. | [S4](#s4), [S26](#s26), [S1](#s1) |
| Add preintegrated IMU factors to a trajectory | **verified** — Official GTSAM preintegration resources support the experiment; frames, bias, gravity and covariance checks required. | [S4](#s4), [S11](#s11), [S37](#s37) |
| Audit clock offsets before running VIO | **verified** — Clock-offset injection uses documented calibration/evaluation tools; dropped frames distinguished from offset. | [S11](#s11), [S10](#s10), [S21](#s21) |
| Design an observable calibration motion | **verified** — Target-based Kalibr excitation study has a synthetic fallback instead of assuming arbitrary VIO logs are calibratable. | [S10](#s10), [S11](#s11), [S37](#s37) |
| Build a rigid timestamped camera-IMU rig | **verified** — Physical custom camera/IMU bracket correctly budgeted separately; provisional <€500 band is not a verified quote. | [S10](#s10), [S11](#s11), [S19](#s19) |
| Replay a public visual-inertial trajectory | **verified** — Official OpenVINS dataset workflow plus evo support replay; initialization and tracking failures retained in results. | [S11](#s11), [S21](#s21) |
| Show where metric scale comes from | **verified** — ORB-SLAM3 supported configurations enable scale comparisons; monocular versus metric alignment caveat is appropriate. | [S12](#s12), [S11](#s11), [S21](#s21) |
| Compare filter and graph VIO under visual loss | **verified** — OpenVINS/ORB-SLAM3 ablation is explicitly a controlled comparison; VIO versus SLAM and build differences disclosed. | [S11](#s11), [S12](#s12), [S27](#s27), [S21](#s21) |
| Grow a floor plan from a recorded laser bag | **verified** — Laser-bag mapping is supported by SLAM Toolbox/OpenLORIS; no robot purchase claimed for replay. | [S13](#s13), [S1](#s1), [S43](#s43) |
| Save a graph and localize a second session | **verified** — Official serialized-graph localization is supported; initial-guess and wrong-place failure caveats explicit. | [S13](#s13), [S21](#s21) |
| Map one lab room with a supervised mobile base | **verified** — Real teleoperated ROS base/laser demo is correctly separated from offline cost and excludes navigation-policy design. | [S20](#s20), [S13](#s13), [S8](#s8) |
| Replay a 3D lidar odometry baseline | **verified** — KISS-ICP replay is supported and correctly labeled odometry, not global loop-corrected SLAM. | [S16](#s16), [S21](#s21) |
| Compare lidar filtering and smoothing on one bag | **verified** — Lidar-filter/smoother comparison requires compatible timing/IMU/extrinsics and equivalent GPS/loop settings. | [S17](#s17), [S18](#s18), [S16](#s16), [S21](#s21) |
| Engineer a synchronized lidar-camera-IMU mapper | **verified** — FAST-LIVO2 provides a sensing/synchronization reference; custom physical subsystem, time and €5k+ planning band explicit. | [S19](#s19), [S17](#s17), [S10](#s10), [S21](#s21) |
| Film a map correction after a verified loop | **verified** — ORB-SLAM3/RTAB-Map support loop correction; accepted constraints and loop-disabled baseline remain to be instrumented. | [S12](#s12), [S15](#s15), [S21](#s21) |
| Build a look-alike-room loop rejection test | **verified** — Look-alike place dataset plus geometric checks is a proposed custom test; recall/precision and graph damage separated. | [S15](#s15), [S4](#s4), [S26](#s26) |
| Compare geometric and learned place matching | **verified** — MASt3R/RTAB-Map comparison retains geometric verification, held-out data and noncommercial-license caveat. | [S24](#s24), [S15](#s15), [S4](#s4) |
| Break a SLAM replay with moving foregrounds | **verified** — TUM dynamic-scene data and baseline references support the custom masking test; DynaSLAM optional and historical. | [S22](#s22), [S12](#s12), [S28](#s28), [S21](#s21) |
| Revisit a changed room without corrupting its map | **verified** — Recorded multi-session map-reuse test supported by SLAM Toolbox/RTAB-Map/OpenLORIS; change policies are experimental. | [S13](#s13), [S15](#s15), [S32](#s32), [S43](#s43) |
| Pilot a localization-health monitor across lab sessions | **verified** — Real-base health-monitor deployment is an original proposal with held-out alarms, human supervision and no safety certification. | [S20](#s20), [S8](#s8), [S13](#s13), [S27](#s27) |
| Reconstruct a recorded room with Gaussian SLAM | **verified** — SplaTAM supports RGB-D Gaussian reconstruction; GPU costs explicitly excluded/unknown rather than claimed free. | [S25](#s25), [S22](#s22), [S21](#s21) |
| Compare prior-driven and classical-tracked dense maps | **verified** — MASt3R-SLAM/ScaRF-SLAM both exist; compatible data, compute, licensing and separation of tracking/map effects required. | [S23](#s23), [S24](#s24), [S35](#s35), [S21](#s21) |
| Measure whether loop corrections improve a dense map | **verified** — ScaRF-SLAM loop/submap behavior and Map2SLAM/PINGS designs support an original evaluation; no preprint code/performance assumed. | [S35](#s35), [S36](#s36), [S33](#s33), [S21](#s21) |
| Align two recorded robot sessions | **verified** — Kimera-Multi/GTSAM and CU-Multi support overlapping-session alignment; synthetic splitting is not called realistic validation. | [S26](#s26), [S4](#s4), [S44](#s44) |
| Keep cooperative maps consistent through packet loss | **verified** — Kimera-Multi module gap is disclosed; minimal GTSAM exchange harness is labeled a teaching adaptation, not full reproduction. | [S26](#s26), [S4](#s4), [S21](#s21) |
| Design a bandwidth-budgeted cooperative mapping protocol | **verified** — Bandwidth policy is an original proposal grounded in distributed mapping; duplicate evidence and clock assumptions explicit. | [S26](#s26), [S31](#s31), [S21](#s21) |
| Build a trajectory evaluation scorecard | **verified** — evo/TUM support small trajectory evaluation; scorecard adds coverage/alignment reporting rather than assuming perfect tooling. | [S21](#s21), [S22](#s22) |
| Turn trajectory failures into a reproducible test suite | **verified** — Deterministic failure injections are proposed custom tests; association tolerances and denominators fixed before comparing. | [S21](#s21), [S11](#s11), [S32](#s32) |
| Audit a city-scale SLAM claim on held-out sessions | **verified** — LaMAria's surveyed-control-point protocol is preserved; dense ground truth and effortless compatibility are not assumed. | [S27](#s27), [S11](#s11), [S12](#s12), [S32](#s32) |
| Visualize a contact-aided inertial estimate | **verified** — Official invariant-ekf contact example supports replay/simulation; global position/yaw ambiguity correctly retained. | [S29](#s29), [S30](#s30), [S4](#s4) |
| Detect when a stance-foot assumption becomes false | **verified** — Injected slip and contact-gating comparison is a custom experiment grounded in contact-aided estimation. | [S29](#s29), [S30](#s30), [S4](#s4) |
| Replay legged body-state estimates with camera outages | **verified** — Required joint/contact/IMU/camera compatibility is not assumed; simulation-only fallback and no gait controller. | [S29](#s29), [S30](#s30), [S4](#s4), [S11](#s11) |
| Convert synthetic GNSS fixes into a local map frame | **verified** — Official navsat_transform supports GNSS/heading/odometry conversion; frame, datum, altitude and yaw checks explicit. | [S9](#s9), [S8](#s8), [S6](#s6) |
| Survive GNSS dropout and bad fixes in replay | **verified** — GNSS corruption/gating experiment uses documented fusion/GPS tools; dropout and multipath bias are distinguished. | [S9](#s9), [S8](#s8), [S18](#s18), [S21](#s21) |
| Georeference a supervised outdoor mapping walk | **verified** — Physical GNSS/lidar mapping requires receiver/antenna/mount budget and independent checkpoints; no unverified RTK claim. | [S18](#s18), [S9](#s9), [S21](#s21) |

## Validation

A local validator constructed exact property and select/multi-select allowlists from `schemas/notion-schema.md` and checked the complete cleaned payload:

- Valid JSON; 16 knowledge, 21 reference-system and 48 project rows retained; unique titles within every collection.
- Only the 15/15/22 applicable writable Notion fields on knowledge/reference-system/project rows, respectively; no unexpected row keys, formula properties or auto reverse relations.
- Exact Branch/Level/Discipline/accessibility/time/cost/kind/form-factor/model-type/complexity/duration/wow options; correct checkbox and number types. Unknown Release year remains `null`, never the string "unknown" in a number property.
- 37 knowledge/reference-system statuses are To verify; 48 project statuses are Idea. Deprecated Project ideas stays empty.
- All 48 Software/Mechanical/Electrical work-hour splits are nonnegative and total **100**.
- All Knowledge nodes, Robots & models and project Prerequisites names resolve within this file; no duplicate relation targets, self-dependencies or prerequisite cycles. Built by, Used by and Relevant orgs are empty, with builder fallback text populated.
- Every row has at least one opened source/reference; **44 distinct URLs remain in row citations**, all from the 45-URL audit ledger. The LIN-SLAM supplemental paper remains only in the report. No duplicated URLs within a row's Sources/References.
- Diff-based verdict counts match the input backup: **65 unchanged, 20 corrected, 0 removed**.
- `python -m json.tool output/knowledge_state_estimation_slam.json` and `git diff --check` are the final syntax/whitespace checks. No software/lint/type-check suite or pre-commit configuration is present in this research-only repository.

## Remaining planning risks (not rejected facts)

- Real rig/base/GNSS prices and host/GPU access remain **unknown**; physical bands are estimates requiring a complete BOM/quote.
- Kimera-Multi's Remote Topic Manager is still marked coming soon. The candidates explicitly gate on availability and label a minimal GTSAM harness as an adaptation.
- ROS Noetic-era stacks, DynaSLAM's old dependencies and cross-pipeline bag compatibility can dominate integration time. No claim of a tested modern install is made.
- MASt3R, MASt3R-SLAM's dependencies and DynaSLAM carry noncommercial restrictions. Open-source checkboxes describe the identified source project, not a legal audit of every optional dependency/checkpoint/data combination; review the chosen full stack.
- Map2SLAM remains a paper/design comparison here; code availability and performance on 42AI hardware are not assumed. A realistic multi-robot demonstration needs real overlapping sessions, not merely relabeled segments from one trajectory.
- LaMAria evaluation uses surveyed control points; do not replace that protocol with a fictitious continuous dense reference trajectory.

## Researcher accessibility rationales (metadata moved out of JSON)

These are planning judgments, not source-measured performance.

| Knowledge node | Rationale |
|---|---|
| Bayesian state estimation & uncertainty | A small noisy-position simulation runs on a laptop and needs no robotics hardware. |
| Wheel & inertial dead reckoning | Synthetic wheel traces give a first demo before touching motors or buying a base. |
| Kalman filtering & multisensor fusion | Existing packages reduce implementation work, but tuning covariance and diagnosing frames takes mathematical care. |
| Particle filtering & global localization | 2D landmark simulations are easy to animate; designing informative likelihoods and resampling needs some probability. |
| Factor graphs, smoothing & pose-graph SLAM | Python bindings make tiny graphs accessible; gauge freedom and nonlinear optimization are the main learning cost. |
| Estimator calibration, timing & observability | Public bags avoid hardware work, but selecting excitation, interpreting uncertainty and handling clocks is demanding. |
| Visual odometry & visual-inertial SLAM | Public EuRoC/TUM-VI examples are software-first, although C++ dependencies and initialization are real obstacles. |
| 2D lidar SLAM & occupancy mapping | A recorded laser scan bag produces a recognizable floor plan without new hardware. |
| 3D lidar-inertial odometry & mapping | Datasets remove purchase barriers, but point formats, deskewing and ROS 1-era dependencies require substantial debugging. |
| Place recognition, loop closure & relocalization | Image sequences and graph visualizations suit software students, with no need to construct a moving robot. |
| Robust, dynamic & lifelong state estimation | Controlled dataset corruptions are cheap, but credible claims require failure detection, repeats and changing scenes. |
| Dense, semantic & neural SLAM maps | AI skills transfer well and public videos are enough, but GPU availability and geometry evaluation lower accessibility. |
| Multi-robot & distributed SLAM | Multiple recorded sessions avoid buying a fleet, but map alignment, networking and old dependencies are substantial integration work. |
| SLAM benchmarking, consistency & failure analysis | Small trajectory files and plotting scripts deliver useful results on an ordinary laptop. |
| Contact-aided & invariant state estimation | Replay examples need no biped purchase, but Lie-group reasoning and contact validation need mathematical effort. |
| GNSS-aided localization & georeferencing | Synthetic GNSS and public logs allow software-first fusion; real outdoor accuracy requires careful hardware and reference data. |

## Researcher top-three recommendations (metadata moved out of JSON)

These are recommendations, not verification rankings or guaranteed best choices.

1. **2D lidar SLAM & occupancy mapping:** Best immediate visual payoff: floor-plan growth and loop correction are understandable on video, a laser bag costs no new hardware, and the ROS 2 ecosystem makes the result reusable. Accessibility 5; physical deployment is a later purchase decision.
2. **Visual odometry & visual-inertial SLAM:** Strong software-to-robotics bridge: a public visual/inertial sequence yields a trajectory and map without a robot purchase. Accessibility 4; useful to mobile and handheld systems, with initialization and build risks made explicit.
3. **Dense, semantic & neural SLAM maps:** Most compelling frontier showcase for AI students: a navigable-looking dense reconstruction from recorded imagery. Accessibility 3 and high visual impact, but rank it third because GPU access, metric accuracy and noncommercial model terms can dominate the apparent low sensor cost.

## Opened-source ledger

Each original URL is listed once; S45 is the added official changelog. Primary documentation/repositories and original paper/proceedings pages are used for factual claims. S31 is conference context, not feature proof. S41 is supplemental discovery evidence only.

<a id="s1"></a>
**S1.** <https://www.ipb.uni-bonn.de/wp-content/papercite-data/pdf/springerbook-slamchapter.pdf> — Stachniss, Leonard and Thrun author manuscript, draft July 2013: probabilistic SLAM, EKF, particle and graph paradigms; historical foundation, not 2026 SOTA.

<a id="s2"></a>
**S2.** <https://modernrobotics.northwestern.edu/nu-gm-book-resource/13-4-odometry/> — Lynch/Park Modern Robotics 13.4: wheel odometry, chassis-frame increments and pose integration; supports drift exercises.

<a id="s3"></a>
**S3.** <https://ocasys.rug.nl/2025-2026/catalog/course/WMCS040-05> — Official Groningen 2025–26 Robotic State Estimation course: spatial-state models, sensor uncertainty, Kalman derivatives and graph SLAM.

<a id="s4"></a>
**S4.** <https://gtsam.org/> — Official GTSAM site: C++ factor graphs, Python/MATLAB, preintegration, continuous-time and 2026 contact/proprioceptive estimation material.

<a id="s5"></a>
**S5.** <https://github.com/borglab/gtsam> — Official Borglab GTSAM repository: factor-graph smoothing/mapping implementation, interfaces and development/stable-version cautions.

<a id="s6"></a>
**S6.** <https://github.com/AtsushiSakai/PythonRobotics> — Official Atsushi Sakai PythonRobotics repository: educational localization, filtering, mapping and ICP examples.

<a id="s7"></a>
**S7.** <https://github.com/cra-ros-pkg/robot_localization> — Official Charles River Analytics/ROS robot_localization repository: nonlinear state-estimation package and provenance.

<a id="s8"></a>
**S8.** <https://raw.githubusercontent.com/cra-ros-pkg/robot_localization/ros2/doc/state_estimation_nodes.rst> — Official ROS 2 state-estimation-node documentation: EKF/UKF, frames, covariance, sensor timeouts and prediction without corrections.

<a id="s9"></a>
**S9.** <https://raw.githubusercontent.com/cra-ros-pkg/robot_localization/ros2/doc/navsat_transform_node.rst> — Official ROS 2 navsat_transform documentation: GPS, heading and odometry inputs; local Cartesian/UTM transforms and yaw conventions.

<a id="s10"></a>
**S10.** <https://github.com/ethz-asl/kalibr> — Official ETH ASL Kalibr repository: camera/IMU spatial-temporal, multiple-camera/IMU and rolling-shutter calibration; named authors.

<a id="s11"></a>
**S11.** <https://docs.openvins.com/> — Official OpenVINS documentation: RPNG, University of Delaware; initial release August 15, 2019; MSCKF, calibration, simulation and NEES/evaluation.

<a id="s12"></a>
**S12.** <https://github.com/UZ-SLAMLab/ORB_SLAM3> — Official Zaragoza ORB-SLAM3 repository: listed authors, visual/inertial multi-map modes and GPLv3; README v1.0 is December 2021.

<a id="s13"></a>
**S13.** <https://github.com/SteveMacenski/slam_toolbox> — Official SLAM Toolbox repository: ROS 2 planar scan SLAM, graph serialization, localization and lifelong mapping; LGPLv2.1.

<a id="s14"></a>
**S14.** <https://github.com/introlab/rtabmap> — Official IntRoLab RTAB-Map repository: graph-SLAM implementation and ROS 1/2 build information.

<a id="s15"></a>
**S15.** <http://introlab.github.io/rtabmap/> — Official RTAB-Map project site: RGB-D/stereo/lidar graph SLAM, loop detection, memory management, Mathieu Labbé and dependency-sensitive BSD access.

<a id="s16"></a>
**S16.** <https://github.com/PRBonn/kiss-icp> — Official PRBonn KISS-ICP repository: point-to-point ICP lidar odometry, Python tools, ROS 2 wrapper and MIT license; ROS 1 deprecated.

<a id="s17"></a>
**S17.** <https://github.com/hku-mars/FAST_LIO> — Official HKU MARS FAST_LIO repository: FAST-LIO 2.0 update July 5, 2021; direct lidar/inertial filtering and ikd-tree; GPLv2.

<a id="s18"></a>
**S18.** <https://github.com/TixiaoShan/LIO-SAM> — Official Tixiao Shan LIO-SAM repository: GTSAM mapping/GPS and IMU-preintegration graphs, ROS 2 branch and sensor requirements; loop closure is a proof-of-concept component.

<a id="s19"></a>
**S19.** <https://github.com/hku-mars/FAST-LIVO2> — Official HKU MARS FAST-LIVO2 repository: direct lidar/inertial/visual fusion; code release January 23, 2025; synchronization resources and GPLv2.

<a id="s20"></a>
**S20.** <https://emanual.robotis.com/docs/en/platform/turtlebot3/overview/> — Official ROBOTIS TurtleBot3 manual: modular wheeled platform, ROBOTIS builder, 2017 introduction and ROS 2/Gazebo support; no current complete-kit quote asserted.

<a id="s21"></a>
**S21.** <https://github.com/MichaelGrupp/evo> — Official Michael Grupp evo repository: APE/RPE, trajectory alignment/formats and GPLv3-or-later; no claim that all quality metrics are automatic.

<a id="s22"></a>
**S22.** <https://cvg.cit.tum.de/data/datasets/rgbd-dataset> — Official TUM RGB-D benchmark: Kinect RGB/depth and independent motion-capture reference trajectories, evaluation resources and dynamic-scene data links.

<a id="s23"></a>
**S23.** <https://github.com/rmurai0610/MASt3R-SLAM> — Official Murai/Dexheimer/Davison MASt3R-SLAM repository: CVPR 2025 dense monocular SLAM, pretrained prior/checkpoint setup and licensing caveats.

<a id="s24"></a>
**S24.** <https://github.com/naver/mast3r> — Official NAVER MASt3R repository: 2024 learned image matching/3D reconstruction prior; CC BY-NC-SA 4.0 code and additional checkpoint/data restrictions.

<a id="s25"></a>
**S25.** <https://github.com/spla-tam/SplaTAM> — Official SplaTAM repository: Keetha, Karhade and collaborators; CVPR 2024 dense RGB-D Gaussian SLAM, CUDA setup and BSD-3 top-level source.

<a id="s26"></a>
**S26.** <https://github.com/MIT-SPARK/Kimera-Multi> — Official MIT SPARK Kimera-Multi index: distributed metric-semantic mapping; ROS Noetic/Ubuntu 20.04; Remote Topic Manager explicitly 'Coming Soon'.

<a id="s27"></a>
**S27.** <https://lamaria.ethz.ch/> — Official LaMAria project: ICCV 2025 city-scale egocentric VI-SLAM benchmark; time-varying calibration and surveyed control-point reference, not assumed dense truth.

<a id="s28"></a>
**S28.** <https://github.com/BertaBescos/DynaSLAM> — Official Berta Bescos DynaSLAM repository: 2018 dynamic-scene monocular/stereo/RGB-D SLAM, inpainting and legacy dependencies.

<a id="s29"></a>
**S29.** <https://github.com/RossHartley/invariant-ekf> — Official Ross Hartley invariant-ekf repository: C++ propagation, landmark and kinematic/contact examples; BSD-3.

<a id="s30"></a>
**S30.** <https://www.roboticsproceedings.org/rss14/p50.html> — RSS XIV official proceedings: Hartley et al., Contact-Aided Invariant Extended Kalman Filtering, 2018; absolute position and gravity-axis yaw unobservable from contact/IMU alone.

<a id="s31"></a>
**S31.** <https://roboticsconference.org/2025/program/overview/> — Official RSS 2025 conference program: navigation/perception and multi-robot research tracks; broad context only, not evidence for an implementation feature.

<a id="s32"></a>
**S32.** <https://vslam-lab.github.io/Unifying-VSLAM-RSS25/> — Official RSS 2025 visual-SLAM workshop: unified evaluation/reproducibility and failures beyond a single mean trajectory error.

<a id="s33"></a>
**S33.** <https://www.roboticsproceedings.org/rss21/p040.html> — RSS XXI paper 040: PINGS, 2025; coupled Gaussian radiance and signed-distance fields for lidar-visual mapping.

<a id="s34"></a>
**S34.** <https://www.roboticsproceedings.org/rss21/p032.html> — RSS XXI paper 032: Building Rome with Convex Optimization, 2025; certifiable scaled bundle adjustment, not a guarantee for arbitrary online SLAM.

<a id="s35"></a>
**S35.** <https://github.com/ori-drs/ScaRF-SLAM> — Official Oxford DRS ScaRF-SLAM repository: Zhang/Tao/Dellaert/Fallon, RA-L 2026; classical tracking separated from feed-forward dense reconstruction; GPLv3 with separate dependency terms.

<a id="s36"></a>
**S36.** <https://arxiv.org/abs/2611.11169> — Map2SLAM arXiv 2611.11169, November 2026: streaming-model observations of revisable persistent SLAM state; author preprint claims, no local performance reproduction or code availability assumed.

<a id="s37"></a>
**S37.** <https://syllabus.gatech.edu/sites/default/files/2026-04/Fall-2026-AE-8803-Gan-Advanced-Mobile-Robotics-Syllabus.pdf> — Official Georgia Tech Fall 2026 AE 8803 syllabus: invariant filtering, calibration, scan matching, graphs, preintegration and continuous-time SLAM.

<a id="s38"></a>
**S38.** <https://raw.githubusercontent.com/AtsushiSakai/PythonRobotics/master/LICENSE> — Official PythonRobotics LICENSE: MIT; confirms open-source checkbox despite generic GitHub 'Other' metadata.

<a id="s39"></a>
**S39.** <https://raw.githubusercontent.com/ethz-asl/kalibr/master/LICENSE> — Official Kalibr LICENSE: four BSD-style conditions, including advertising acknowledgement for ASL/Skybotix; not merely an unconditional free-use claim.

<a id="s40"></a>
**S40.** <https://raw.githubusercontent.com/BertaBescos/DynaSLAM/master/LICENSE.txt> — Official DynaSLAM LICENSE.txt: CC BY-NC 4.0; source-available but noncommercial, so Open source remains false.

<a id="s41"></a>
**S41.** <https://arxiv.org/html/2610.21199> — LIN-SLAM arXiv HTML 2610.21199, October 2026: lidar/inertial neural implicit SLAM, code release promised rather than a verified runnable tool. Supplementary discovery resource only.

<a id="s42"></a>
**S42.** <https://raw.githubusercontent.com/MIT-SPARK/Kimera-Multi/main/kimera_multi.repos> — Official Kimera-Multi component manifest: many repositories and legacy/pinned dependencies (including GTSAM 4.2a9); inspect component availability and licenses.

<a id="s43"></a>
**S43.** <https://lifelong-robotic-vision.github.io/dataset/scene> — Official OpenLORIS-Scene dataset: repeated real-robot sessions, camera/IMU/wheel data, scene changes, calibration/timing and reference-data caveats.

<a id="s44"></a>
**S44.** <https://arxiv.org/html/2505.17576v2> — CU-Multi arXiv 2505.17576v2, 2025: multi-robot data association and overlap-aware evaluation; arbitrary single-trajectory splitting may misrepresent realistic observations.

<a id="s45"></a>
**S45.** <https://raw.githubusercontent.com/UZ-SLAMLab/ORB_SLAM3/master/Changelog.md> — Official ORB-SLAM3 changelog: V0.2 initial release August 7, 2020, versus V1.0 December 22, 2021; resolves release-year correction.
