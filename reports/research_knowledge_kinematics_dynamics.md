# Kinematics & dynamics discovery research

## Scope
Discovery only. The file has 16 nodes (6 Fundamental, 6 Applied, 4 Frontier), 19 new Robots & Models rows and 48 project candidates (3 per node; 16 Onboarding, 32 Project). Statuses are Draft and Idea. I made no Notion calls. `Built by`, `Used by` and `Relevant orgs` are empty because this file has no ecosystem rows. I never emit `Used in projects`.

Grounding:
- Springer Handbook of Robotics, 2nd ed. I opened the contents (Part A: Kinematics, Waldron & Schmiedeler; Dynamics, Featherstone & Orin) and the chapter 2 page.
- Modern Robotics (Lynch & Park): book home page and the ch. 13.3.1 page.
- Stanford CS223A, Winter 2026 syllabus.
- MIT Underactuated, "Multi-Body Dynamics" chapter.

I could not retrieve ICRA/RSS/CoRL session tracks. Track coverage was replaced by primary 2024-2026 papers and repos (GMR, BeyondMimic, DiffMJX, MuJoCo Warp, RA-L 2025 calibration).

Boundaries with neighbouring branches:
- Collision-free motion planning stays in Manipulation/Planning.
- Here, trajectory work covers only time scaling.
- Controllers stay in Control. Gravity compensation and feedforward appear here only as uses of dynamics.
- Learned dynamics/world models stay in Robot learning. The Science Robotics 2025 review was opened and noted, but it is not a node here.

## Cross-file relations (for the syncer)
- Project `Robots & models` reuse pilot rows `MuJoCo` and `SO-101` from `knowledge_manipulation.json`. I did not re-emit them.
- `Prerequisites` reuse existing Notion projects from `output/existing_projects.json`: "Assemble & teleoperate an SO-101", "Intro: robot anatomy & coordinate frames in sim", "Intro: drive a servo motor from code", "Design a custom SO-101 gripper", "Autonomous pick-and-place with ACT".
- There are no duplicate node names with the pilot files and no duplicate project names with existing projects. My onboarding projects are deliberately different from the existing "Intro: robot anatomy & coordinate frames in sim".

## Queries run (main)
Searches covered:
1. The Springer Handbook kinematics/dynamics chapters.
2. Pinocchio analytical derivatives.
3. mink/Pink differential IK.
4. GMR retargeting.
5. TOPP-RA/Ruckig.
6. Dynamic identification surveys.
7. Ruckig.
8. Differentiable contact / MJX / Warp.
9. Centroidal dynamics / Crocoddyl.
10. Robotics Toolbox for Python.
11. onshape-to-robot.
12. BAM servo friction.
13. CS223A.
14. TRAC-IK.
15. Delta robots.
16. MuJoCo Menagerie.
17. BeyondMimic.
18. Diff-drive kinematics.
19. Survey/taxonomy.
20. Calibration.
21. Screw theory / PoE.
22. ICRA 2025 humanoid whole-body IK.

All URLs in `sources_consulted` (38) were retrieved with full-page fetches. Search snippets alone are not counted.

Failed or empty fetches, not used: ROS 2 URDF tutorial (docs.ros.org), Pinocchio ROS docs page.

## Saturation-stop evidence
An "entry" means a new knowledge node (denominator 16).

| Consecutive query | New nodes | Notes |
|---|---:|---|
| `kinematics dynamics robotics survey taxonomy 2025 open problems` | 1 candidate (continuum/soft robot kinematics) → not added, 1/16 = 6% | Learned dynamics models are mapped to Robot learning. Kinematic loops are already covered. |
| `robot kinematic calibration low-cost arm camera hand-eye 2025` | 0 | Maps to the calibration node. |
| `screw theory product of exponentials ... singularity` | 0 | Maps to the FK and Jacobian nodes. |
| `ICRA 2025 ... humanoid whole-body IK retargeting parallel mechanisms` | 0 | Maps to differential IK, retargeting and floating-base. |

All were below 10%, so I stopped.

## Top 3 (qualitative ratio)
1. **Differential IK & redundancy resolution**: one codebase serves teleop, retargeting and humanoid reach. It is free in sim and very visual.
2. **Human-to-robot motion retargeting**: software-only, with public code and data and a filmable humanoid demo. Real humanoids are expensive (Unitree G1 from $13.5K on the vendor page), so stay in sim.
3. **Dynamic parameter identification & actuator models**: a cheap servo bench, and the tooling comes from a French lab (Rhoban's BAM). STS3215 is not in BAM's bundled models, which is an opening for an original community contribution.

## Gaps and unknowns
- Not mapped: continuum/soft-robot kinematics, flexible-link dynamics, dual quaternions as a separate node, and closed-form IK generators (IKFast; not opened). These are candidates for coverage review.
- Release years are null where no opened source gave one. Open source = code availability, not a licence audit.
- DiffMJX code availability is unknown. The MuJoCo Warp differentiable-contact work is an open PR: its merge status was not verified.
- "Gravity-compensated SO-101" depends on whether the STS3215 supports current/torque mode. This is not verified; check before starting.
- The cost bands, durations, wow ratings and work splits are planning estimates, not quotes. "<€500" assumes an SO-101 or a few servos; the exact kit price is unknown.
- The delta robot row is a paper design (IJMERR 2024), not a product. The total cost is not stated in the source.

## Validation
I checked every select, multi-select and status value against `schemas/notion-schema.md`. Each row's source URLs are in `sources_consulted`. Names are unique. There is no overlap with the pilot nodes or existing projects. All relations resolve to this file, the pilot files or `existing_projects.json`. Work splits sum to 100, and each node has 3-6 projects.

Output: `PASS 737 option values; 16 19 48 38`.
