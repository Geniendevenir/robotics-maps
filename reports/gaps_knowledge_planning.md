# Coverage gaps: knowledge_planning.json — Planning

Reviewed 2026-11-13, after `reports/verify_knowledge_planning.md`: **17 knowledge nodes, 14 robots/models, 51 project candidates** in `output/knowledge_planning.json`. **3 High / 9 Medium / 3 Low gaps.** This is a coverage critique, not another verification pass; no research rows were added or edited, and Notion was neither read nor written.

## Basis and scope

Compared with the Springer Handbook of Robotics, second-edition TOC (Motion Planning, Behavior-Based Systems, AI Reasoning Methods for Robotics), LaValle's Planning Algorithms, CMU/IMR/MIT course material, and official ICRA/RSS/CoRL programs and papers. The 20 references below were opened in this pass. Older references establish foundations; 2024–2025 papers/programs establish recent directions, not an exhaustive late-2026 SOTA ranking. The local schema was read; no suggestion requires emitting the auto-managed `Used in projects` relation.

High means a major missing planning capability or a missing bridge to the lab's real-robot goal; Medium means an important method family or substantive depth gap; Low means useful tooling/linkage or a more specialized extension. A gap can be filled by extending an existing node/project, not necessarily by adding a node. Keep the researcher's 8–20-node scope in mind.

Already covered: configuration spaces and collision checking; A*/D* Lite; PRM/RRT/RRT*; retiming and trajectory optimization; Nav2/costmaps and DWA/MPPI/TEB; executives and PDDL; kinodynamics; MAPF; coverage; MDP/POMDP beliefs; GPU, learned/diffusion, language and world-model planning. These are not missing merely because a newer implementation is absent. Manipulation-specific TAMP is deliberately cross-referenced to Manipulation and should not be duplicated; SLAM, low-level control and safety certification stay in their own branches.

## High

- **H1 — Explicit unknown-map exploration and next-best-view planning (Knowledge Map / project depth):** the belief-space node already mentions information gathering and has an information-gathering-policy project, but no node/project specifies frontier extraction, next-best-view selection, information-gain scoring or exploration completion; extend it with a partially observed-map exploration comparison, keeping SLAM as an input rather than re-researching estimation. [5, 12]
- **H2 — Multi-robot task allocation and multi-goal routing (Knowledge Map / tool / project):** MAPF assigns collision-free routes to given goals and explicitly separates task allocation; none of the projects assigns jobs to robots or optimizes job order, leaving a major fleet-planning layer uncovered; introduce assignment/auction and route-order baselines, using Open-RMF as a sourced implementation reference rather than treating the educational MAPF examples as a fleet stack. [8, 13]
- **H3 — A physical navigation integration rung (Projects / platform reference; cross-branch inputs):** all 51 candidates use `€0 (sim only)` and 100% software, so the ladder never tests a planner on a real base; propose an optional borrowed/off-the-shelf low-speed mobile robot follow-up to the Nav2 delivery demo with documented TF/footprint/odometry interfaces, tracking-error and latency checks, and supervised stop handling; platform choice, price and availability remain unknown, and electronics/control/safety work belongs with the corresponding branches. [15; verifier's hardware-ladder flag]

## Medium

- **M1 — Predictive space-time planning for moving obstacles (Knowledge Map / project depth):** local rollouts, crossing-traffic tests and MAPF delays are present, but single-robot planning against predicted obstacle occupancy over time, explicit waiting and safe intervals are not; compare SIPP/time-expanded search with reactive replanning under bounded prediction error, without claiming that model-based guarantees imply real-world safety. [14]
- **M2 — Classical geometric and sensor-based baselines (Fundamental depth):** PRM/RRT and grids do not replace visibility/Voronoi roadmaps, exact cell decomposition, Bug algorithms or potential/navigation functions; coverage already mentions cell decomposition generically, but these methods and their completeness/local-minimum assumptions are not taught or compared; a compact classical-methods extension is enough, not a node for every algorithm. [1, 2, 5]
- **M3 — Anytime, bounded-suboptimal and real-time search (Fundamental / Applied depth):** the graph-search node covers optimal and incremental search, but not Weighted A*, ARA*/Anytime D* or agent-centered real-time search; add the distinction between finding a first feasible plan quickly and improving its bound under a deadline, rather than conflating D* Lite reuse with anytime behavior. [2, 3]
- **M4 — Formal mission specifications and synthesis (Knowledge Map / project depth):** PDDL preconditions/effects and behavior-tree monitoring do not cover temporal-logic missions, automata/product-graph planning or model checking; a small ordered-patrol/avoid-region example would bridge human goals to checkable specifications while stating abstraction assumptions; keep manipulation-specific TAMP in Manipulation. [8, 11]
- **M5 — Equality-constrained/manifold motion planning (generic planning depth; cross-branch applications):** collision-free sampling, nonholonomic dynamics and retiming are covered, but planning on a lower-dimensional constraint surface is not; use OMPL's sphere/implicit-chain demonstrations to explain projection/atlas approaches and intermediate-state constraint checking, linking arm/contact applications rather than duplicating Manipulation or Locomotion. [16]
- **M6 — Risk-sensitive and robust planning objectives (uncertainty/optimization depth; Control link):** POMDP beliefs and sensor-dropout/model-mismatch tests are present, but expected cost versus worst-case/CVaR objectives and chance constraints are not; add a simple risk-versus-route-length comparison and an explicit feedback-policy versus open-loop-path distinction, reusing Control for controller derivations rather than adding a second control syllabus. [5, 6, 20]
- **M7 — Human-aware navigation objectives (local/navigation depth; HRI & safety link):** the file tests crossing traffic and calls for conservative behavior, but does not model yielding, interpersonal-space/social costs or uncertainty in pedestrian predictions; add a navigation evaluation beyond collision counts, with HRI supplying interaction criteria and no implication of certified human safety. [10]
- **M8 — Convex-region / mixed-integer planning (optimization frontier depth):** optimization coverage names local CHOMP/TrajOpt/MPC methods, while GPU and learned approaches have dedicated frontier nodes; graphs of convex sets and discrete-route/continuous-trajectory coupling are missing, despite RSS 2024–2025 coverage; extend the optimization node with a small corridor-region comparison and distinguish relaxation/rounding guarantees from local-optimizer behavior. [7, 8, 18]
- **M9 — Task planning beyond instantaneous flat actions (symbolic depth):** the PDDL node explains preconditions/effects but not hierarchical task decomposition, durative actions, scheduling or resource conflicts; the coverage return-to-base and executive battery-condition ideas are not resource-constrained schedulers; extend with a small deadline/charger-resource example and distinguish HTN planning from executing a predefined behavior tree. [13, 19]

## Low

- **L1 — Reuse a standard planner benchmark harness (resources/project refinement):** seeded timing, quality and failure-count projects already exist, so benchmarking is not absent; what is missing is an explicit route to OMPL Benchmark and Planner Arena for repeatable time/memory budgets, logged planner configurations and cost-progress curves rather than a new bespoke harness. [17]
- **L2 — Cross-map organization linkage (relations; defer to ecosystem merge):** every `Built by`, `Used by` and `Relevant orgs` relation is empty, although builder text names real maintainers; reconcile supported names with the ecosystem outputs before sync instead of inventing organizations, asserting unverified users or treating the schema's text attribution fallback as invalid.
- **L3 — Communication-constrained cooperative information gathering (advanced project extension):** MAPF and coverage do not address connectivity/rendezvous constraints or information-distribution-driven search; an optional simulated extension could compare periodic rendezvous with unconstrained exploration, but this is lower priority than assignment, exploration baselines and the first physical navigation demo. [9]

## Opened reference register

1. Springer Handbook of Robotics, second edition (2016), publisher TOC: https://link.springer.com/book/10.1007/978-3-319-32552-1
2. CMU 16-735 Robot Motion Planning syllabus (classical algorithms and anytime search): https://www.cs.cmu.edu/~motionplanning/syllabus.html
3. CMU 16-350 Planning Techniques for Robotics, course schedule (interleaving planning/execution, anytime/incremental/real-time search): http://www.cs.cmu.edu/~maxim/classes/robotplanning_sp25/
4. IMR Lab Motion Planning course (search, sampling, optimization and advanced methods): https://imrclab.github.io/teaching/motion-planning
5. LaValle, Planning Algorithms, TOC (geometric planning, feedback, uncertainty and differential constraints): https://lavalle.pl/planning/
6. MIT Underactuated Robotics, course-note TOC (optimization, feedback planning and robustness): https://underactuated.mit.edu/
7. RSS 2025 official paper-session listing (includes convex-set and planning papers): https://roboticsconference.org/2025/program/papersession/?session=5.+Planning
8. RSS 2025, Hierarchical Temporal Logic Task and Motion Planning for Multi-Robot Systems: https://roboticsconference.org/2025/program/papers/99/
9. RSS 2025, A Probabilistic Measure of Multi-Robot Connectivity and Ergodic Optimal Control: https://roboticsconference.org/2025/program/papers/100/
10. CoRL 2025 main program, including Planning & Safety & Robustness and crowd-navigation uncertainty: https://2025.corl.org/program/main-conference
11. ICRA 2025, Language and Semantics of Task and Motion Planning workshop description: https://2025.ieee-icra.org/event/language-and-semantics-of-task-and-motion-planning/
12. CogniPlan: Uncertainty-Guided Path Planning with Conditional Generative Layout Prediction (2025; exploration/frontier/information-gain context): https://arxiv.org/abs/2508.03027
13. Open Robotics, Tasks in RMF (allocation/bidding and battery-aware scheduling): https://osrf.github.io/ros2multirobotbook/task.html
14. CMU Robotics Institute, SIPP: Safe Interval Path Planning for Dynamic Environments (2011; foundational space-time method): https://publications.ri.cmu.edu/sipp-safe-interval-path-planning-for-dynamic-environments
15. Nav2 official First-Time Robot Setup Guide (transforms, odometry, sensors, footprint and plugins): https://docs.nav2.org/rolling/configuration_and_development/first_time_robot_setup_guide/
16. OMPL official Constrained Planning documentation (constraint manifolds and projection/atlas methods): https://ompl.kavrakilab.org/core/constrainedPlanning.html
17. OMPL official How to Benchmark Planners (Benchmark, logs, SQLite and Planner Arena): https://ompl.kavrakilab.org/core/benchmark.html
18. RSS 2024, Implicit Graph Search for Planning on Graphs of Convex Sets: https://www.roboticsproceedings.org/rss20/p113.html
19. Örebro University, Planning and Scheduling course syllabus (classical/HTN planning, temporal/resource scheduling, coordinated motion): https://www.oru.se/contentassets/1de071f91ea046db91d5218cd6bae5ec/planning-and-scheduling-4-credits-course-syllabus-for-third-cycle-courses-and-study-programmes-50dt048.pdf
20. MIT Underactuated Robotics, Robust and Stochastic Control (risk objectives and stochastic constraints): https://underactuated.mit.edu/robust.html

## Saturation check and handoff

Unit: a materially distinct, in-scope gap category, not another paper or tool. The final list has 15 categories. After the initial comparison, these three consecutive discovery queries yielded fewer than 10% new categories each; search snippets were discovery aids, not supporting evidence unless the source was subsequently opened above.

| Query | Results inspected | New categories | Mapping |
| --- | ---: | ---: | --- |
| `robot motion planning syllabus taxonomy exploration task allocation formal methods constrained planning` | 5 | 1/15 = 6.7% | Örebro's HTN/temporal/resource scheduling material produced M9; other results mapped to H2/M4/M5 or the existing TAMP cross-reference. |
| `robot planning 2025 graph search convex sets risk dynamic obstacles uncertainty` | 5 | 0/15 = 0% | Risk, traversability and dynamic-obstacle results mapped to M1/M6 or existing costmaps; convex methods mapped to M8. |
| `robotics navigation planning curriculum potential fields anytime search multi robot connectivity temporal planning` | 5 | 0/15 = 0% | CMU and other syllabi mapped to M2/M3/M9; sampling, kinodynamics and optimization were already covered. |

This is saturation of this scoped gap list, not proof of exhaustive literature coverage. Researcher follow-up should prioritize H1–H3 only, then re-verify any proposed changes; the critic has added no rows. Resolve hardware access, full project cost and cross-database links before any approved sync. No benchmark, UI or physical experiment was executed in this critique.
