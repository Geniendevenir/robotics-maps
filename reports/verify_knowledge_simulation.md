# Verification report: knowledge_simulation.json

Checked 70 rows: 14 knowledge nodes, 14 robots/models/tools and 42 project candidates. **Verified: 36. Corrected: 34. Rejected: 0.**

## Method and limits

- Opened all 36 distinct original source/reference URLs with web retrieval and read the relevant documentation, README, abstract or paper text; added and opened the official RobotStudio design repository (37 distinct sources total). The source appendix records each URL and what it supports. Shared URLs were opened once and checked against every row citing them.
- Checked existence, builder attribution, technical scope, licenses as described by the sources, all select options, field types and local relations. There are no Ecosystem Map rows; no Notion calls were made.
- The 2025 soft-body twin paper and July 2026 BWM paper are real and match their cited topics. Paper results are author reports, not independently reproduced results. No simulator, model checkpoint, real robot, throughput figure or project demo was tested.
- The Handbook multimedia home page and RSS program are canonical background/taxonomy sources only. They do not substantiate particular solver or model claims. Older foundational sources remain valid as fundamentals; current official docs/READMEs and 2025–2026 papers support current implementation statements.
- Kept all 70 rows: no fabricated or out-of-scope entry required rejection. “Verified” here is a research-audit verdict; retained non-project rows still have Status = To verify, and project candidates retain Status = Idea.

## Corrections

- Removed all 14 private _accessibility_reason row keys. Preserved their explanations below. Removed the three non-Notion justification keys from top3 and preserved their text below. The six documented file-envelope keys remain for pipeline compatibility; every row/top3 dictionary now contains only Notion field names.
- Replaced all 14 string-valued Release year fields: Genesis = 2024 from its official dated history; the other 13 are null (unknown numeric values). No first-release year was inferred from a repository creation timestamp.
- Clarified that current Playground main uses PyTorch/reaf-sim/MuJoCo Warp and the original JAX/MJX environments are on rss2025. Added the explicit MJX-Warp no-autodiff limitation to the differentiable node, Newton entry and three gradient projects. Warp differentiable kernels and a physics solver built on Warp are different claims.
- Changed four generic comparison/sweep project Novelty values from 4 - Original to 3 - Combine. The references establish existing methods, not an original research contribution by these unbuilt student proposals.
- Qualified MuJoCo and OpenUSD roles in learned-world/twin pipelines and Genesis community/Genesis AI attribution; added official SO-101 design evidence.
- Physical SO-101/twin projects already use €500-5k and 90/5/5 work shares. These were checked and retained. They are conservative planning bands, not supplier quotes; access, compute and full acquisition costs remain unknown. All time, accessibility, work-share and wow ratings are planning judgments, not measured results.

## Per-row verdicts

| Table | Row | Verdict | One-line reason | Opened sources |
|---|---|---|---|---|
| nodes | Time stepping & numerical fidelity | corrected | Forward dynamics and numerical-error tradeoffs supported by Modern Robotics and MuJoCo; removed private accessibility key. | S19, S02, S16, S01 |
| nodes | Collision geometry & contact solver fidelity | corrected | MuJoCo and MIT distinguish contact models and friction approximations; removed private accessibility key. | S03, S17, S27, S01 |
| nodes | Robot and scene formats: URDF, MJCF, SDF & USD | corrected | Official MJCF, URDF, SDF and USD sources support formats and differing semantics; removed private accessibility key. | S04, S32, S33, S11 |
| nodes | ROS 2 and Gazebo simulation integration | corrected | Official ros_gz bridge and sensor tutorials support integration; removed private accessibility key. | S09, S10, S33 |
| nodes | Sensor simulation, rendering & synthetic labels | corrected | Gazebo sensors, ManiSkill and Replicator support synthetic observations/labels; removed private accessibility key. | S10, S14, S22, S07 |
| nodes | GPU-parallel simulation & vectorized environments | corrected | Made current PyTorch/Warp Playground versus historical rss2025 JAX/MJX distinction explicit; removed private accessibility key. | S05, S06, S08, S15, S13, S23 |
| nodes | Domain randomization & transfer stress testing | corrected | Tobin et al. directly support visual domain randomization, with transfer treated as a hypothesis; removed private accessibility key. | S29, S07, S14, S24 |
| nodes | System identification & simulator calibration | corrected | MuJoCo overview/modeling and Drake support model-based calibration; removed private accessibility key. | S03, S16, S25, S04, S01 |
| nodes | Real-to-sim digital twins & Gaussian-splat rendering | corrected | 2025 paper confirms Gaussian rendering plus soft-body twins, with task-specific policy evaluation; removed private accessibility key. | S34, S24, S11 |
| nodes | Learned action-conditioned world simulators | corrected | DreamerV3 and BWM abstracts support action-conditioned prediction; no universal physics replacement claimed; removed private accessibility key. | S30, S31, S35 |
| nodes | Simulation benchmarks & reproducible evaluation | corrected | Official benchmark sources support task/evaluation protocols; RSS list is only taxonomy context; removed private accessibility key. | S14, S21, S24, S28 |
| nodes | Procedural scenes, asset pipelines & task generation | corrected | RoboCasa and Replicator support scene and synthetic-data workflows; removed private accessibility key. | S21, S22, S11, S04 |
| nodes | Differentiable physics & gradient validation | corrected | Added explicit MJX-Warp no-autodiff limitation and separated Brax maintenance advice from gradient support; removed private accessibility key. | S36, S27, S23, S17, S05 |
| nodes | Deformable and multiphysics simulation fidelity | corrected | Official Genesis/Newton sources support deformable and coupled solvers; clarified Genesis community attribution; removed private accessibility key. | S12, S13, S27, S07, S34 |
| robots_models | MuJoCo | corrected | Official Google DeepMind repository confirms physics engine; qualified its role in learned/twin pipelines; unknown numeric year becomes null. | S26 |
| robots_models | Drake | corrected | Official site confirms MIT origin and Toyota Research Institute-led development; unknown numeric year becomes null. | S16 |
| robots_models | Newton | corrected | Official repository confirms Linux Foundation and Disney/DeepMind/NVIDIA initiators; qualified solver-specific gradients; unknown numeric year becomes null. | S27, S05 |
| robots_models | Gazebo | corrected | Official Gazebo tutorial confirms bridge and simulated sensor workflows; unknown numeric year becomes null. | S09 |
| robots_models | OpenUSD | corrected | Official Pixar/OpenUSD documentation supports open scene framework, not complete physics or reconstruction; clarified role; unknown numeric year becomes null. | S11 |
| robots_models | ManiSkill | corrected | Official ManiSkill README confirms SAPIEN/GPU simulation, Apache code and distinct asset terms; unknown numeric year becomes null. | S15 |
| robots_models | Isaac Sim / Isaac Lab | corrected | Isaac Lab repository confirms NVIDIA framework and separate proprietary dependency/asset terms; unknown numeric year becomes null. | S08 |
| robots_models | MuJoCo Playground | corrected | Made current PyTorch/reaf-sim/Warp versus rss2025 JAX/MJX distinction explicit; unknown numeric year becomes null. | S06 |
| robots_models | Genesis | corrected | Official documentation explicitly dates academic Genesis to December 2024; set year 2024 and clarify community/Genesis AI support. | S13, S12 |
| robots_models | SO-101 | corrected | Added official RobotStudio design repository to confirm Hugging Face collaboration and Apache design; unknown numeric year becomes null. | S25, S37 |
| robots_models | SimplerEnv | corrected | Official repository confirms SAPIEN, visual matching, variant aggregation and ManiSkill3 branch; unknown numeric year becomes null. | S24 |
| robots_models | DreamerV3 | corrected | Official Hafner repository confirms latent-model RL and MIT implementation; unknown numeric year becomes null. | S31 |
| robots_models | RoboCasa | corrected | Official site confirms household simulation, 2026 updates and linked code/data; unknown numeric year becomes null. | S21 |
| robots_models | NVIDIA Warp | corrected | Official NVIDIA repository confirms CPU/GPU compiled Python kernels and differentiation; unknown numeric year becomes null. | S36 |
| project_candidates | Pendulum energy-drift cinema | verified | MuJoCo/Modern Robotics support pendulum stepping; proposed energy-drift demo, not a claimed experiment. | S19, S02, S16, S01 |
| project_candidates | Simulation speed versus fidelity dashboard | verified | Official dynamics tools support proposed timing/error comparison; no unverified throughput figure. | S19, S02, S16, S01 |
| project_candidates | Adaptive fidelity regression gate | verified | Numerical-model regression proposal has valid fields, local prerequisites and measurable error tolerances. | S19, S02, S16, S01 |
| project_candidates | Collision hull versus visual mesh gallery | verified | MuJoCo/URDF modeling references distinguish visual and collision geometry for the proposed overlay. | S03, S17, S27, S01 |
| project_candidates | Friction and restitution identification arena | verified | MuJoCo contact and MIT notes support proposed sliding/bounce parameter tests. | S03, S17, S27, S01 |
| project_candidates | Cross-engine contact disagreement atlas | verified | Both engines exist; comparison explicitly avoids declaring either a ground-truth contact solver. | S03, S17, S27, S01 |
| project_candidates | Robot asset lint and repair lab | verified | URDF/MJCF/SDF documentation supports the proposed units, mesh and inertia lint checks. | S04, S32, S33, S11 |
| project_candidates | Round-trip robot description loss report | verified | Conversion is explicitly limited to supported representations and reports losses rather than promising equivalence. | S04, S32, S33, S11 |
| project_candidates | Versioned portable scene package | verified | Scene package proposal includes repeatable loading, provenance and unsupported-property reporting. | S04, S32, S33, S11 |
| project_candidates | Simulation clock and bridge oscilloscope | verified | Official ROS/Gazebo bridge supports proposed clock/message experiment; not a claim that it was run. | S09, S10, S33 |
| project_candidates | ROS graph fault-injection sandbox | verified | Delay/drop monitoring is a student fault-injection proposal grounded in bridge and sensor messages. | S09, S10, S33 |
| project_candidates | Headless ROS replay acceptance rig | verified | Headless replay is a proposed acceptance experiment using pinned ROS/Gazebo interfaces. | S09, S10, S33 |
| project_candidates | Virtual sensor truth-versus-noise wall | verified | ManiSkill and Replicator support RGB/depth/labels; noise/dropout are proposed perturbations. | S10, S14, S22, S07 |
| project_candidates | Synthetic label quality auditor | verified | Official synthetic-data workflows support label inspection; auditor remains a student proposal. | S10, S14, S22, S07 |
| project_candidates | Camera latency and rolling exposure stress set | verified | Explicitly proposes controlled exposure/latency perturbations, not a calibrated real camera model. | S10, S14, S22, S07 |
| project_candidates | Batch-reset correctness kaleidoscope | verified | Batched simulator APIs support proposed isolation/reset checks; no execution success claimed. | S05, S06, S08, S15, S13, S23 |
| project_candidates | Parallel simulation throughput truth sheet | verified | Parallel backends exist; machine-specific compilation/rendering/VRAM are proposed measurements. | S05, S06, S08, S15, S13, S23 |
| project_candidates | Backend portability learning microbenchmark | verified | Actual learning microbenchmark correctly uses Learned single task; backend semantics remain explicit. | S05, S06, S08, S15, S13, S23 |
| project_candidates | Randomization coverage heatmap | verified | Domain randomization sources support proposed visual/physics sampling and coverage checks. | S29, S07, S14, S24 |
| project_candidates | Held-out nuisance robustness tournament | verified | Controlled held-out nuisance evaluation is a proposal, with valid fields and local relations. | S29, S07, S14, S24 |
| project_candidates | Counterexample-guided simulator curriculum | verified | Retains a final untouched test set; failure-guided distribution changes are proposed, not a claimed result. | S29, S07, S14, S24 |
| project_candidates | Recover hidden simulated pendulum damping | verified | MuJoCo/Drake support the proposed damping identification and held-out trajectory test. | S03, S16, S25, S04, S01 |
| project_candidates | SO-101 joint response calibration card | verified | Official SO-101 assembly/calibration exists; physical project already budgets €500-5k and 90/5/5 work shares. | S03, S16, S25, S04, S01 |
| project_candidates | SO-101 calibration uncertainty challenge | verified | Physical uncertainty study already budgets €500-5k, valid work shares and bounded use of existing arm. | S03, S16, S25, S04, S01 |
| project_candidates | Desk twin alignment before beauty contest | verified | Scene-alignment proposal separates geometric error from appearance; no robot interaction promised. | S34, S24, S11 |
| project_candidates | Twin appearance-versus-physics ablation | verified | 2025 soft-body twin paper and SimplerEnv support separating appearance and physics in a proposed ablation. | S34, S24, S11 |
| project_candidates | Digital twin policy-ranking audit | corrected | Downgraded unsupported Original rating to Combine; physical €500-5k and 90/5/5 estimates were already correct. | S34, S24, S11 |
| project_candidates | Imagined pendulum rollout microscope | verified | DreamerV3 supports a small learned predictive baseline; no video-model speed/compute claim. | S30, S31, S35 |
| project_candidates | Action-ignored video simulator detector | verified | Dreamer/BWM support action-conditioned models; sensitivity scorecard is proposed, not a reported result. | S30, S31, S35 |
| project_candidates | Learned-versus-physics evaluator disagreement study | corrected | Downgraded unsupported Original rating to Combine; cited world models support the proposed surrogate comparison. | S30, S31, S35 |
| project_candidates | Success-checker loophole film festival | verified | Task suites expose success checks; deliberately adversarial near-miss checker test remains a proposal. | S14, S21, S24, S28 |
| project_candidates | Seeded simulation leaderboard in a box | verified | Benchmark references support fixed seeds, failure accounting and comparisons; no executed leaderboard claimed. | S14, S21, S24, S28 |
| project_candidates | Simulator-to-real ranking credibility study | verified | Narrow SimplerEnv reproduction explicitly reports unreproducible real/sim parts; sim-only budget retained. | S14, S21, S24, S28 |
| project_candidates | Seeded tabletop scene generator | verified | RoboCasa/Replicator support scene generation; proposed validity checks are not claimed guarantees. | S21, S22, S11, S04 |
| project_candidates | Procedural scene solvability filter | verified | Proposed solvability filter includes rejected scenes and reasons; valid relations and work split. | S21, S22, S11, S04 |
| project_candidates | Compositional scene generalization split | verified | Proposed layout/identity split is consistent with scene and benchmark sources; no measured generalization claimed. | S21, S22, S11, S04 |
| project_candidates | Gradient versus finite-difference spotlight | corrected | Added supported-differentiable-solver requirement and explicit MJX-Warp no-autodiff caveat. | S36, S27, S23, S17, S05 |
| project_candidates | Contact gradient breakage gallery | corrected | Added supported-differentiable-solver requirement and explicit MJX-Warp no-autodiff caveat for contact optimization. | S36, S27, S23, S17, S05 |
| project_candidates | Differentiable system-ID versus black-box search | corrected | Downgraded unsupported Original to Combine and required a supported differentiable path instead of assuming MuJoCo Warp gradients. | S36, S27, S23, S17, S05 |
| project_candidates | Rigid-versus-soft drop comparison reel | verified | Genesis/Newton document deformables; proposed drop/energy comparison has valid fields and sim-only cost. | S12, S13, S27, S07, S34 |
| project_candidates | Soft material parameter observability lab | verified | Deformable solver sources support parameter fitting proposal; identifiability is evaluated rather than assumed. | S12, S13, S27, S07, S34 |
| project_candidates | Coupled solver stability frontier map | corrected | Downgraded unsupported Original rating to Combine; official solver examples support the narrow proposed coupling sweep. | S12, S13, S27, S07, S34 |

## Accessibility explanations retained outside Notion rows

- **Time stepping & numerical fidelity** (5 - Easy): A CPU laptop is enough to plot numerical errors and film a toy scene.
- **Collision geometry & contact solver fidelity** (4): Simple sliding and stacking scenes reveal contact errors without building a robot.
- **Robot and scene formats: URDF, MJCF, SDF & USD** (5 - Easy): Editing small text models fits software skills and needs no hardware.
- **ROS 2 and Gazebo simulation integration** (4): Official bridge tutorials provide a starting point, but middleware and version pairing add setup work.
- **Sensor simulation, rendering & synthetic labels** (4): RGB and depth demos are accessible; photorealistic rendering may require a suitable GPU.
- **GPU-parallel simulation & vectorized environments** (3): The batching concepts are familiar, but GPU access and backend compatibility can block the first run.
- **Domain randomization & transfer stress testing** (4): Randomization and held-out evaluation fit AI skills and can start entirely in simulation.
- **System identification & simulator calibration** (3): Offline fitting is approachable; real calibration needs careful synchronization and safe excitation.
- **Real-to-sim digital twins & Gaussian-splat rendering** (2): Capturing, aligning and validating appearance plus physics is substantially harder than loading a ready-made scene.
- **Learned action-conditioned world simulators** (2): Small latent-model experiments are feasible; large video simulators have uncertain compute and access costs.
- **Simulation benchmarks & reproducible evaluation** (4): Existing task suites enable immediate measurement, though fair protocol design takes discipline.
- **Procedural scenes, asset pipelines & task generation** (4): Python scene generation gives fast visual feedback; quality filters matter more than buying hardware.
- **Differentiable physics & gradient validation** (2): Gradient tooling fits AI skills, but physically meaningful derivatives through contact need mathematical care.
- **Deformable and multiphysics simulation fidelity** (2): Ready-made examples are runnable, but identifying material parameters and validating coupling is difficult.

## Top-three rationale retained outside Notion fields

- **Robot and scene formats: URDF, MJCF, SDF & USD**: Very low onboarding cost, immediate broken-versus-fixed visual evidence and reusable assets across ROS, MuJoCo and GPU stacks; strong value before choosing a learning wedge.
- **Sensor simulation, rendering & synthetic labels**: Visually legible RGB/depth/label galleries fit software and AI skills, support dataset-quality work and connect to ManiSkill and Isaac communities; start with modest rendering rather than expensive realism.
- **Domain randomization & transfer stress testing**: Colorful controlled stress tests make robustness visible and directly test the low-cost sim-to-real hypothesis; begin sim-only and require held-out evidence before buying hardware.

## Opened source register

| ID | URL | Evidence and limits |
|---|---|---|
| S01 | https://handbookofrobotics.org/ | Official 2016 Handbook multimedia companion; historical taxonomy only, not current engine evidence. |
| S02 | https://mujoco.readthedocs.io/en/stable/overview.html | MuJoCo identity, history, dynamics and system-identification uses. |
| S03 | https://mujoco.readthedocs.io/en/stable/computation/index.html | Dynamics, constraints, contact modeling and numerical computation. |
| S04 | https://mujoco.readthedocs.io/en/stable/modeling.html | MJCF/URDF modeling, collision geometry and physical parameters. |
| S05 | https://mujoco.readthedocs.io/en/stable/mjx.html | JAX and Warp implementations, batching and explicit MJX-Warp lack of automatic differentiation. |
| S06 | https://github.com/google-deepmind/mujoco_playground | Current PyTorch/reaf-sim/MuJoCo Warp stack; rss2025 retains original JAX/MJX tasks. |
| S07 | https://isaac-sim.github.io/IsaacLab/main/index.html | Current Isaac Lab multi-backend robot-learning documentation. |
| S08 | https://github.com/isaac-sim/IsaacLab | Isaac Lab attribution, multi-backend workflows and BSD/Apache/proprietary dependency distinction. |
| S09 | https://gazebosim.org/docs/harmonic/ros2_integration/ | Official ros_gz message bridge with supported-message limits. |
| S10 | https://gazebosim.org/docs/harmonic/sensors/ | Official Gazebo sensor tutorial and data streams. |
| S11 | https://openusd.org/release/intro.html | Official Pixar/OpenUSD scene composition and asset interchange. |
| S12 | https://genesis-world.readthedocs.io/en/latest/ | Genesis World multiphysics, CPU/GPU scaling, December 2024 origin and Genesis AI support. |
| S13 | https://github.com/Genesis-Embodied-AI/Genesis | Official Genesis code, community attribution and Apache license. |
| S14 | https://maniskill.readthedocs.io/en/latest/ | ManiSkill GPU/visual simulation and benchmarking documentation. |
| S15 | https://github.com/haosulab/ManiSkill | Official ManiSkill/SAPIEN code and separate code/asset licensing; redirects to mani-skill/ManiSkill. |
| S16 | https://drake.mit.edu/ | Drake MIT origin, TRI leadership and model-based dynamics/optimization. |
| S17 | https://underactuated.mit.edu/contact.html | MIT course notes on contact, hybrid dynamics and discontinuities. |
| S18 | https://modernrobotics.northwestern.edu/nu-gm-book-resource/ | Modern Robotics book/video index; canonical background, not current benchmark evidence. |
| S19 | https://modernrobotics.northwestern.edu/nu-gm-book-resource/8-5-forward-dynamics-of-open-chains/ | Modern Robotics forward dynamics and time integration tutorial. |
| S20 | https://manipulation.csail.mit.edu/ | MIT manipulation syllabus, simulation and robot-description context. |
| S21 | https://robocasa.ai/ | RoboCasa household tasks, code/data links and dated 2026 updates. |
| S22 | https://docs.isaacsim.omniverse.nvidia.com/latest/replicator_tutorials/index.html | Official Replicator synthetic-data workflows, randomization and annotators. |
| S23 | https://github.com/google/brax | Brax warning: only training actively maintained; recommends Playground/MJX/MuJoCo Warp for simulation. |
| S24 | https://github.com/simpler-env/SimplerEnv | Official SimplerEnv visual matching, variant aggregation and ManiSkill3 branch. |
| S25 | https://huggingface.co/docs/lerobot/so101 | Official Hugging Face SO-101 assembly, gearing and calibration workflow. |
| S26 | https://github.com/google-deepmind/mujoco | Official Google DeepMind MuJoCo code and license. |
| S27 | https://github.com/newton-physics/newton | Official Newton community/Linux Foundation attribution, initiators, solvers and examples. |
| S28 | https://roboticsconference.org/2025/program/papers/ | Official RSS 2025 accepted-paper/session list; taxonomy context only. |
| S29 | https://arxiv.org/abs/1703.06907 | Tobin et al. 2017 primary paper on visual domain randomization and real-image transfer. |
| S30 | https://arxiv.org/abs/2301.04104 | Hafner et al. DreamerV3 primary paper on world-model RL; older baseline, not a 2026 ranking. |
| S31 | https://github.com/danijar/dreamerv3 | Hafner DreamerV3 implementation, latent model/imagined trajectories and MIT license. |
| S32 | https://github.com/ros/urdf_tutorial | Official ROS URDF tutorial including physical/collision properties. |
| S33 | https://gazebosim.org/docs/harmonic/sdf_worlds/ | Official Gazebo SDF world/physics/scene tutorial. |
| S34 | https://arxiv.org/abs/2511.04665 | 2025 Zhang et al. Real-to-Sim Robot Policy Evaluation with Gaussian Splatting Simulation of Soft-Body Interactions; physics plus rendering, task-specific evaluation. |
| S35 | https://arxiv.org/abs/2607.29302 | 2026 BWM Team abstract: action-conditioned Boundless World Model; existence/topic confirmed, claimed results and released weights not independently reproduced. |
| S36 | https://github.com/NVIDIA/warp | Official NVIDIA Warp CPU/GPU kernels, differentiability and Apache code. |
| S37 | https://github.com/TheRobotStudio/SO-ARM100 | Official RobotStudio SO-100/SO-101 designs, Hugging Face collaboration, Apache license and region-dependent BOM. |

## Validation

Validation pending; this checkpoint contains the completed source/row audit and cleaned rows.
