# Coverage gaps: knowledge_mechanisms_actuation.json (Mechanisms & actuation branch)

Reviewed file: `output/knowledge_mechanisms_actuation.json` after verification (18 nodes, 10 robots/models/tools, 54 project candidates; see `reports/verify_knowledge_mechanisms_actuation.md`).

References used for comparison: the Springer Handbook of Robotics (2nd ed.), especially ch. 4 "Mechanism and Actuation", ch. 18 "Parallel Mechanisms", ch. 19 "Robot Hands" and the soft-robotics/actuator chapters. Syllabi: MIT 2.12 (Asada), MIT 2.72 "Elements of Mechanical Design" and Stanford ME 112 "Mechanical Systems Design". Recent ICRA/RSS/CoRL hardware work on low-cost, 3D-printed, quasi-direct-drive and humanoid actuators. The LeRobot/SO-101 working wedge from CLAUDE.md. Sibling files `knowledge_embedded_electronics.json`, `knowledge_manipulation.json` and `knowledge_locomotion.json`, checked to avoid flagging things they already cover.

Scope note: only gaps inside Mechanisms & actuation, or rows this branch is expected to link to. "(cross-branch)" marks items whose row should live in another branch file. I did not re-open URLs in this pass. The researcher must source and verify each item before adding a row. I added no rows.

## High

- **The wedge arm's mechanics are missing (SO-101 / Feetech STS3215 hobby-servo internals)**: no node, robot link or project covers the arm the lab will actually use (the file mentions SO-101 once and STS3215 zero times). Missing: the servo's spur gear train, backlash and stall torque, and printed-link load paths. Both rows already exist in other files, so add a node plus links, not duplicate rows.
- **No project modifies or extends the SO-101 mechanically** (wrist or gripper redesign, servo-to-QDD swap, gravity-compensated link, stiffer printed links): 0 of 54 projects touch the wedge hardware, and all 54 have Autonomy "2 - Scripted".
- **Compliant mechanisms and flexures**, Knowledge node (Fundamental): a standard machine-design and Springer topic. It suits 3D printing (flexure hinges, compliant grippers, printed springs) and is very accessible. Not present ("flexure" has 0 mentions).
- **Low-cost 3D-printed open-source actuators as Robots & Models links**: Berkeley Humanoid Lite (printed cycloidal actuator), Open Duck Mini v2, RobStride 00 and mjbots moteus/qdd100 are absent from this file. They exist in `knowledge_embedded_electronics.json`, so link them. Also check for new rows for printed reference designs (e.g. OpenTorque-style printed QDD/cycloidal actuators). Right now ODRI and the MIT Mini Cheetah actuator are the only accessible real actuators referenced.
- **Gravity compensation and counterbalancing (springs, counterweights, parallelograms)**, Knowledge node (Applied): the cheapest way to get more payload out of low-torque hobby-servo arms. A classic arm-design topic, with 0 mentions.
- **Relevant orgs / Built by / Key players are never linked as organizations**: expected players include Harmonic Drive, Nabtesco, maxon, Festo, Schaeffler, igus, Unitree, RobStride, CubeMars/T-Motor, Feetech/Robotis, ODRI partners (MPI-IS, LAAS-CNRS) and DLR. This is for the ecosystem researchers. Do not add rows from this file.

## Medium

- **Wheels and mobile-base drivetrains (differential drive, omni/mecanum wheels, tracks, suspension)**, Knowledge content: the mechanism side of wheeled robots, which Coupe de France / Eurobot teams build. `Wheeled mobile robot kinematics` exists in Locomotion, but no mechanism node covers it (cross-branch with Locomotion).
- **Parallel robots as Robots & Models (delta robot, Stewart/hexapod platform)**: a full Springer chapter. The linkages node has no concrete reference platform ("delta" and "Stewart" each have 0 mentions).
- **Brakes, clutches and fail-safe holding mechanisms**, Knowledge content: needed for joints that hold loads when power is off and for safety. 0 mentions (cross-branch with HRI & safety).
- **Planetary roller screws and humanoid linear actuators (2025-2026 humanoid trend, e.g. Tesla Optimus-style linear actuators)**, Frontier state: missing from the screws node and the humanoid co-design node.
- **Quasi-direct-drive (QDD) actuator design as a named topic**: it appears only twice inside other nodes. 2024-2026 legged and humanoid work treats it as the default low-cost actuator class (partly overlaps `Leg design & proprioceptive actuation` in Locomotion).
- **Stress, stiffness and fatigue analysis (hand calcs plus FEA, e.g. FreeCAD FEM/CalculiX)**, Knowledge content: the bearings/structures node gives no simulation-based check.
- **Tolerances, fits and fasteners (ISO 286 fits, heat-set inserts, threaded joints in printed parts)**, Knowledge content: only touched indirectly by the bearing-fit coupon projects.
- **Onshape and Fusion 360**, Robots & Models: Onshape is mentioned 22 times but has no row of its own, and only FreeCAD and onshape-to-robot exist as CAD tools.
- **Motor types and electromechanics (stepper, brushed DC and BLDC torque constant / motor constant from the mechanical side)**: steppers have only 2 mentions and there is no Kt/Km sizing anchor in the sizing node (cross-branch with Embedded & electronics `Motor drivers` / `BLDC & FOC`).
- **Commercial humanoid and legged robots as references for joint co-design**: Unitree G1/H1/Go2 and Stanford Pupper exist in Locomotion but are not linked from `Integrated legged and humanoid joint co-design`.
- **Underactuated and robot-hand references beyond RUKA (LEAP Hand, Shadow Hand tendon drive)**: the tendon node could link the LEAP Hand row from Manipulation (cross-branch with Manipulation).
- **Project mix**: there are no Autonomy level-3+ projects and no integration above 2 subsystems. Everything sits at Novelty 1-3 and Wow factor 2-4. There is no flagship "demo-able joint driving a real robot" project. 27 of 54 projects are €0 sim-only.

## Low

- **Dielectric elastomer actuators, twisted-string actuators and twisted-and-coiled polymer (fishing-line) muscles**: only one mention, inside the artificial-muscles node.
- **Magnetic and microrobot actuation**: niche, with low accessibility.
- **Cable-driven parallel robots**: niche variant of parallel mechanisms.
- **Continuously variable and dual-motor transmissions**: research niche.
- **Gear manufacturing processes (hobbing, laser-cut and CNC gears vs printed)**: partly covered in the CAD/DFM node.
- **Encoder and sensor mounting in joints (magnetic encoders on output shafts)** (cross-branch with Sensing).
- **Springer Handbook ch. 4 and the MIT 2.72 / Stanford ME 112 syllabi as Best resources**: currently MIT 2.12/865 dominate. Adding a design-course reference would round out the beginner path.

## Summary

High: 6 · Medium: 12 · Low: 7. A targeted re-run of the researcher on the High items is recommended. The most important are the SO-101/STS3215 mechanics node and projects, compliant mechanisms and gravity compensation, and linking the existing low-cost actuator rows. These sit directly on the LeRobot/SO-101 wedge, and the current file never touches that hardware.
