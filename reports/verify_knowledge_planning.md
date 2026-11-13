# Verification report: knowledge_planning.json

Rows checked: 82 (17 knowledge nodes, 14 robots/models, 51 project candidates). Verified: 68. Corrected: 14. Rejected: 0.

## Method
- I opened all 28 distinct source/reference URLs with curl. All returned HTTP 200 with matching titles.
- For the 2024-2026 papers I checked authors, dates and key claims on the arXiv abstract pages. 2505.15157 Cascaded Diffusion (Sharma, Fishman, Kumar, Paxton, Kroemer, May 2025). 2610.12910 (Gao, Yang, Kingston, Oct 2026) uses nearest-neighbor RRT and KPIECE with an off-the-shelf DINO-WM, as the node claims. 2604.00401 (Ho, Sunberg, Lahijanian, Apr 2026) covers semantic-uncertainty task and kinodynamic planning. 2601.11063 EmboTeam (Jan 2026, v3 Nov 2026). LaDi-WM is in PMLR 305 (CoRL 2025).
- Builder checks:
  - PlanSys2: Francisco Martín et al., per the BibTeX in the PlanSys2/ros2_planning_system repo.
  - BehaviorTree.CPP: Davide Faconti, per the repo copyright line.
  - Ruckig: has Community vs paid versions, per the README.
  - Fields2Cover: built for agricultural vehicles.
  - cuRobo: NVIDIA, with 2026 whole-body and v0.9.0 updates on curobo.org.
- I validated every select and multi-select value against schemas/notion-schema.md. All valid.
- Other structural checks: all project work splits sum to 100. Every Knowledge nodes, Robots & models and Prerequisites name resolves within the file. The prerequisite graph is acyclic. There are no duplicate titles. Project ideas is empty on every node.
- Schema cleanup: removed the non-Notion key `_accessibility_reason` from all nodes. Release year "unknown" became null (it is a number field), except where I could verify a year. No `Used in projects` key is present.
- Status: nodes and robots/models are now "To verify". Projects stay "Idea", because Projects has no "To verify" option.
- Not applicable: no Ecosystem Map organizations are in this file. Built by, Used by and Relevant orgs are all empty, so builders are held in "Builder (if not in map)".

## Flags for human review
- All 51 projects are simulation-only, with 100% software and €0 hardware. This is consistent with the Planning branch scope, but there is no hardware ladder. The coverage critic may want a real-robot step, for example Nav2 on a low-cost AMR.
- Three sim-only benchmark/evaluation projects have Wow factor 5. Example: "build a reproducible cross-device parallel-planning benchmark". That looks generous for a filmable demo. I left the values unchanged.
- The language-planning projects mark €0, but the descriptions say they exclude API token cost.
- Release year is left null for OMPL, MoveIt 2, Nav2, Ruckig, TOPPRA, BehaviorTree.CPP, PlanSys2, the multi-agent examples, Fields2Cover and POMDPs.jl. I did not confirm a first-release year from the opened pages.
- "Multi-agent path planning examples" (atb033) is a small educational GitHub repo, not an established tool. It is fine as a learning reference.

## Rows

| Table | Row | Verdict | Reason |
|---|---|---|---|
| Knowledge node | Configuration space & collision checking | verified | all cited sources opened (HTTP 200) and support the claims; selects valid; removed non-Notion key `_accessibility_reason` |
| Knowledge node | Graph search & incremental replanning | verified | all cited sources opened (HTTP 200) and support the claims; selects valid; removed non-Notion key `_accessibility_reason` |
| Knowledge node | Sampling-based motion planning | verified | all cited sources opened (HTTP 200) and support the claims; selects valid; removed non-Notion key `_accessibility_reason` |
| Knowledge node | Trajectory generation & time parameterization | verified | all cited sources opened (HTTP 200) and support the claims; selects valid; removed non-Notion key `_accessibility_reason` |
| Knowledge node | Optimization-based trajectory planning | verified | all cited sources opened (HTTP 200) and support the claims; selects valid; removed non-Notion key `_accessibility_reason` |
| Knowledge node | Navigation stacks & costmaps | verified | all cited sources opened (HTTP 200) and support the claims; selects valid; removed non-Notion key `_accessibility_reason` |
| Knowledge node | Local planning & reactive obstacle avoidance | verified | all cited sources opened (HTTP 200) and support the claims; selects valid; removed non-Notion key `_accessibility_reason` |
| Knowledge node | Behavior trees & task executives | verified | all cited sources opened (HTTP 200) and support the claims; selects valid; removed non-Notion key `_accessibility_reason` |
| Knowledge node | Symbolic task planning with PDDL | verified | all cited sources opened (HTTP 200) and support the claims; selects valid; removed non-Notion key `_accessibility_reason` |
| Knowledge node | Kinodynamic & nonholonomic planning | verified | all cited sources opened (HTTP 200) and support the claims; selects valid; removed non-Notion key `_accessibility_reason` |
| Knowledge node | Multi-robot path finding & conflict resolution | verified | all cited sources opened (HTTP 200) and support the claims; selects valid; removed non-Notion key `_accessibility_reason` |
| Knowledge node | Coverage path planning | verified | all cited sources opened (HTTP 200) and support the claims; selects valid; removed non-Notion key `_accessibility_reason` |
| Knowledge node | Planning under uncertainty & belief space | verified | all cited sources opened (HTTP 200) and support the claims; selects valid; removed non-Notion key `_accessibility_reason` |
| Knowledge node | GPU-parallel motion planning | verified | all cited sources opened (HTTP 200) and support the claims; selects valid; removed non-Notion key `_accessibility_reason` |
| Knowledge node | Learned & diffusion motion planners | verified | all cited sources opened (HTTP 200) and support the claims; selects valid; removed non-Notion key `_accessibility_reason` |
| Knowledge node | Language-grounded task planning | verified | all cited sources opened (HTTP 200) and support the claims; selects valid; removed non-Notion key `_accessibility_reason` |
| Knowledge node | World-model predictive planning | verified | all cited sources opened (HTTP 200) and support the claims; selects valid; removed non-Notion key `_accessibility_reason` |
| Robot/model | OMPL | corrected | source opened (HTTP 200), builder/specs confirmed; Release year "unknown" -> null (number field) |
| Robot/model | MoveIt 2 | corrected | source opened (HTTP 200), builder/specs confirmed; Release year "unknown" -> null (number field) |
| Robot/model | Nav2 | corrected | source opened (HTTP 200), builder/specs confirmed; Release year "unknown" -> null (number field) |
| Robot/model | Ruckig | corrected | source opened (HTTP 200), builder/specs confirmed; Release year "unknown" -> null (number field) |
| Robot/model | TOPPRA | corrected | source opened (HTTP 200), builder/specs confirmed; Release year "unknown" -> null (number field) |
| Robot/model | BehaviorTree.CPP | corrected | source opened (HTTP 200), builder/specs confirmed; Release year "unknown" -> null (number field) |
| Robot/model | PlanSys2 | corrected | source opened (HTTP 200), builder/specs confirmed; Release year "unknown" -> null (number field) |
| Robot/model | Multi-agent path planning examples | corrected | source opened (HTTP 200), builder/specs confirmed; Release year "unknown" -> null (number field) |
| Robot/model | Fields2Cover | corrected | source opened (HTTP 200), builder/specs confirmed; Release year "unknown" -> null (number field) |
| Robot/model | POMDPs.jl | corrected | source opened (HTTP 200), builder/specs confirmed; Release year "unknown" -> null (number field) |
| Robot/model | cuRobo | corrected | curobo.org opened, NVIDIA builder and 2026 whole-body/v0.9.0 updates confirmed; Release year unknown -> 2023 (NVlabs/curobo repo created Oct 2023) |
| Robot/model | Cascaded Diffusion Models for Neural Motion Planning | corrected | arXiv 2505.15157 opened, authors match; Kind Simulator/Tool -> AI model, Model type N/A -> Policy (IL/RL) (learned planner trained on planner demonstrations); Release year 2025 (submitted 21 May 2025) |
| Robot/model | SayCan | corrected | say-can.github.io opened; it is a learned LLM+affordance system, not a tool: Kind -> AI model (Model type N/A); Release year 2022 (initial release 4/4/2022); open-source sim version confirmed (8/16/2022) |
| Robot/model | DINO-WM | corrected | arXiv 2411.04983 opened (Zhou, Pan, LeCun, Pinto); github.com/gaoyuezhou/dino_wm exists so Open source true holds; Release year unknown -> 2024 (submitted 7 Nov 2024) |
| Project | Planning lab: animate obstacle inflation for a disc robot | verified | references open; selects valid; splits sum to 100; relations resolve; Status stays Idea |
| Project | Planning lab: compare discrete and swept collision tests on thin walls | verified | references open; selects valid; splits sum to 100; relations resolve; Status stays Idea |
| Project | Planning lab: build a shared collision-validation service for two robot shapes | verified | references open; selects valid; splits sum to 100; relations resolve; Status stays Idea |
| Project | Planning lab: film A-star versus Dijkstra maze expansions | verified | references open; selects valid; splits sum to 100; relations resolve; Status stays Idea |
| Project | Planning lab: replay D-star Lite when a corridor closes | verified | references open; selects valid; splits sum to 100; relations resolve; Status stays Idea |
| Project | Planning lab: compare incremental and fresh search across changing warehouse maps | verified | references open; selects valid; splits sum to 100; relations resolve; Status stays Idea |
| Project | Planning lab: animate PRM and RRT in a two-dimensional maze | verified | references open; selects valid; splits sum to 100; relations resolve; Status stays Idea |
| Project | Planning lab: benchmark RRT-star quality versus runtime over fixed seeds | verified | references open; selects valid; splits sum to 100; relations resolve; Status stays Idea |
| Project | Planning lab: compare geometric and control-based planners for a simulated vehicle | verified | references open; selects valid; splits sum to 100; relations resolve; Status stays Idea |
| Project | Planning lab: animate a path with unsafe and bounded speed profiles | verified | references open; selects valid; splits sum to 100; relations resolve; Status stays Idea |
| Project | Planning lab: compare jerk-limited retargeting with path retiming | verified | references open; selects valid; splits sum to 100; relations resolve; Status stays Idea |
| Project | Planning lab: integrate online retargeting with collision revalidation and stop handling | verified | references open; selects valid; splits sum to 100; relations resolve; Status stays Idea |
| Project | Planning lab: optimize smooth waypoints around a two-dimensional obstacle | verified | references open; selects valid; splits sum to 100; relations resolve; Status stays Idea |
| Project | Planning lab: compare straight-line and sampling-based initializations | verified | references open; selects valid; splits sum to 100; relations resolve; Status stays Idea |
| Project | Planning lab: combine global search with receding-horizon trajectory optimization | verified | references open; selects valid; splits sum to 100; relations resolve; Status stays Idea |
| Project | Planning lab: navigate a supplied simulated map with visible cost overlays | verified | references open; selects valid; splits sum to 100; relations resolve; Status stays Idea |
| Project | Planning lab: measure footprint inflation effects in narrow corridors | verified | references open; selects valid; splits sum to 100; relations resolve; Status stays Idea |
| Project | Planning lab: build a multi-stop simulated delivery route with recoveries | verified | references open; selects valid; splits sum to 100; relations resolve; Status stays Idea |
| Project | Planning lab: animate candidate velocity rollouts around a moving obstacle | verified | references open; selects valid; splits sum to 100; relations resolve; Status stays Idea |
| Project | Planning lab: compare DWB and MPPI on identical simulated routes | verified | references open; selects valid; splits sum to 100; relations resolve; Status stays Idea |
| Project | Planning lab: stress-test local avoidance under sensor latency and crossing traffic | verified | references open; selects valid; splits sum to 100; relations resolve; Status stays Idea |
| Project | Planning lab: animate a patrol tree with battery and blocked-door conditions | verified | references open; selects valid; splits sum to 100; relations resolve; Status stays Idea |
| Project | Planning lab: add cancellation and bounded recovery to a navigation tree | verified | references open; selects valid; splits sum to 100; relations resolve; Status stays Idea |
| Project | Planning lab: orchestrate simulated inspection with injected action failures | verified | references open; selects valid; splits sum to 100; relations resolve; Status stays Idea |
| Project | Planning lab: visualize a PDDL courier plan between rooms | verified | references open; selects valid; splits sum to 100; relations resolve; Status stays Idea |
| Project | Planning lab: replan a courier task after a door action fails | verified | references open; selects valid; splits sum to 100; relations resolve; Status stays Idea |
| Project | Planning lab: connect PDDL goals to monitored simulated navigation actions | verified | references open; selects valid; splits sum to 100; relations resolve; Status stays Idea |
| Project | Planning lab: animate Dubins-style turns versus impossible sideways moves | verified | references open; selects valid; splits sum to 100; relations resolve; Status stays Idea |
| Project | Planning lab: compare lattice and Hybrid A-star parking routes | verified | references open; selects valid; splits sum to 100; relations resolve; Status stays Idea |
| Project | Planning lab: plan drone-like acceleration-limited detours with forward propagation | verified | references open; selects valid; splits sum to 100; relations resolve; Status stays Idea |
| Project | Planning lab: animate two robots resolving a corridor conflict | verified | references open; selects valid; splits sum to 100; relations resolve; Status stays Idea |
| Project | Planning lab: compare prioritized planning and conflict-based search | verified | references open; selects valid; splits sum to 100; relations resolve; Status stays Idea |
| Project | Planning lab: replan a simulated fleet after execution delays and blocked cells | verified | references open; selects valid; splits sum to 100; relations resolve; Status stays Idea |
| Project | Planning lab: animate stripe coverage with a visible missed-area heatmap | verified | references open; selects valid; splits sum to 100; relations resolve; Status stays Idea |
| Project | Planning lab: compare sweep direction and turning cost for irregular fields | verified | references open; selects valid; splits sum to 100; relations resolve; Status stays Idea |
| Project | Planning lab: integrate obstacle-aware coverage and return-to-base scheduling | verified | references open; selects valid; splits sum to 100; relations resolve; Status stays Idea |
| Project | Planning lab: animate a noisy corridor decision with belief bars | verified | references open; selects valid; splits sum to 100; relations resolve; Status stays Idea |
| Project | Planning lab: compare shortest-path and information-gathering policies | verified | references open; selects valid; splits sum to 100; relations resolve; Status stays Idea |
| Project | Planning lab: evaluate belief-aware routing under sensor dropout and model mismatch | verified | references open; selects valid; splits sum to 100; relations resolve; Status stays Idea |
| Project | Planning lab: plot batched collision-check timing against a CPU baseline | verified | references open; selects valid; splits sum to 100; relations resolve; Status stays Idea |
| Project | Planning lab: benchmark cuRobo planning seeds and collision resolution | verified | references open; selects valid; splits sum to 100; relations resolve; Status stays Idea |
| Project | Planning lab: build a reproducible cross-device parallel-planning benchmark | verified | references open; selects valid; splits sum to 100; relations resolve; Status stays Idea |
| Project | Planning lab: train a tiny maze waypoint predictor on generated plans | verified | references open; selects valid; splits sum to 100; relations resolve; Status stays Idea |
| Project | Planning lab: compare a learned sampler with uniform RRT on held-out maps | verified | references open; selects valid; splits sum to 100; relations resolve; Status stays Idea |
| Project | Planning lab: evaluate cascaded diffusion planning with repair and classical fallback | verified | references open; selects valid; splits sum to 100; relations resolve; Status stays Idea |
| Project | Planning lab: compare free-form and validated language-to-room plans | verified | references open; selects valid; splits sum to 100; relations resolve; Status stays Idea |
| Project | Planning lab: translate courier requests to PDDL with schema rejection | verified | references open; selects valid; splits sum to 100; relations resolve; Status stays Idea |
| Project | Planning lab: build a monitored language-to-inspection executive with adversarial requests | verified | references open; selects valid; splits sum to 100; relations resolve; Status stays Idea |
| Project | Planning lab: animate a learned toy dynamics model against real simulator rollouts | verified | references open; selects valid; splits sum to 100; relations resolve; Status stays Idea |
| Project | Planning lab: compare CEM and random shooting under dynamics mismatch | verified | references open; selects valid; splits sum to 100; relations resolve; Status stays Idea |
| Project | Planning lab: compare latent tree search and MPC on held-out detour tasks | verified | references open; selects valid; splits sum to 100; relations resolve; Status stays Idea |
