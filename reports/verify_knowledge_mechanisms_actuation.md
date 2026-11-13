# Verification report: knowledge_mechanisms_actuation.json

Rows checked: 82 (18 knowledge nodes, 10 robots/models/tools, 54 project candidates). Verified: 80. Corrected: 2. Rejected: 0.

## Method
- Opened all 33 distinct source/reference URLs. 27 returned HTTP 200 to curl, and their titles and content match the claims (Harmonic Drive technology, Nabtesco cycloidal engineering, MIT 865 transmissions page with capstan/belt/screw/cycloid/harmonic sections, Modern Robotics 8.9, MIT 2.12 Asada chapters 2 and 3, SKF, Prusa, FreeCAD, onshape-to-robot, ODRI, ToddlerBot, RUKA, RSS XXI p131, RSS XX p099, arXiv 2504.17736, DLR David, DLR elib VSA review, Nature Microsyst. Nanoeng. SMA paper, MIT DSpace Cheetah actuator paper, Boston Dynamics posts).
- 6 URLs returned 403 to curl. I opened 4 of them in a real browser: maxon support, Soft Robotics Toolkit home, the PneuNets page and Festo DMSP all loaded with the matching content. 2 stay behind a Cloudflare bot check even in the browser: Science Advances 10.1126/sciadv.adi9319 and PNAS 10.1073/pnas.2110023118. I confirmed both through Crossref metadata. HALVE (Gravert et al., Sci. Adv. 2024) states "4.9 times lower driving voltage (1100 volts)". The PNAS paper is the 2021 magnetic origami arm (Wu et al.).
- Key facts I checked on the pages: RUKA has 5 fingers, 15 underactuated DoF and is RSS 2025 work from NYU. ToddlerBot has 30 active DoF, a 2.0 release on 2025-08-25 and a locomotion release on 2026-01-08; its code is MIT-licensed and its hardware is non-commercial. ODRI is BSD-3-Clause. Boston Dynamics did retire hydraulic Atlas.
- I validated every select value against schemas/notion-schema.md. All are valid. Software/Mechanical/Electrical % sum to 100 for all 54 projects. Prerequisite chains are acyclic, and every Prerequisites / Knowledge nodes / Robots & models name resolves. One exception: `MIT Mini Cheetah actuator`, used by 6 projects, is not defined in this file. It is an existing pilot row (verified in verify_knowledge_embedded_electronics.md), so it resolves at sync.
- Schema cleanup: removed the non-Notion key `_accessibility_reason` from all 18 nodes. No `Used in projects` key is present. Project ideas is left empty (deprecated).
- Status: nodes and robots/models are now "To verify". Projects stay "Idea", because the Projects Status field has no "To verify" option.
- Ecosystem relations (Built by / Used by / Relevant orgs) are empty, so there were no organizations to check.

## Flags for human review
- All 18 nodes have Starter hardware cost "€0 (sim only)", including hands-on topics like soft actuators and series-elastic joints. This is defensible because each node can be learned in CAD/sim first, but you may want to review it.
- The file has only 10 robot/model/tool rows, mostly components and tools, and no Ecosystem relations. Coverage is for the critic to judge.

## Rows

| Table | Row | Verdict | Reason |
|---|---|---|---|
| Knowledge node | Electric actuator architectures: mechanical trade-offs | verified |  |
| Knowledge node | Actuator sizing: torque, inertia and thermal duty | verified |  |
| Knowledge node | Spur and planetary gear trains | verified |  |
| Knowledge node | Cycloidal reducers and output mechanisms | verified |  |
| Knowledge node | Strain-wave gearing and flexspline design | verified |  |
| Knowledge node | Timing-belt and capstan transmissions | verified |  |
| Knowledge node | Lead screws, ball screws and linear joint packaging | verified |  |
| Knowledge node | Linkages, cams and parallel mechanism design | verified |  |
| Knowledge node | Tendon routing, antagonism and underactuated mechanisms | verified |  |
| Knowledge node | Backdrivability, friction and mechanical transparency | verified | Modern Robotics 8.9 and MIT Cheetah proprioceptive actuator paper load |
| Knowledge node | Series-elastic actuator mechanics | verified |  |
| Knowledge node | Variable-stiffness and antagonistic spring mechanisms | verified |  |
| Knowledge node | Bearings, structures and printed load paths | verified |  |
| Knowledge node | CAD and design for manufacture of robot joints | verified |  |
| Knowledge node | Hydraulic and pneumatic transmission mechanics | verified | Festo DMSP page (via browser), RSS 2024 pneumatic-muscle tendon arm, BD hydraulic Atlas retirement post confirmed |
| Knowledge node | Soft pneumatic actuators and compliant-body fabrication | verified |  |
| Knowledge node | Artificial muscles: electrohydraulic and smart-material actuation | corrected | HALVE (Sci. Adv. 2024, 1100 V), SMA microactuator (Microsyst. Nanoeng. 2025) and PNAS 2021 origami arm confirmed; Discipline += Electrical (kV drive electronics) |
| Knowledge node | Integrated legged and humanoid joint co-design | verified | ODRI, ToddlerBot, MIT Cheetah proprioceptive actuator paper (DSpace) and BD Atlas 2026 post load |
| Robot/model | FreeCAD | verified |  |
| Robot/model | onshape-to-robot | verified | docs confirm URDF/SDF/MuJoCo export |
| Robot/model | ODRI actuator module | verified | repo loads, BSD-3-Clause, pulley prep/assembly guides present |
| Robot/model | Harmonic Drive strain-wave gearing | verified |  |
| Robot/model | Nabtesco RV reducer family | verified |  |
| Robot/model | RUKA | corrected | project page + RSS 2025 page confirm 5 fingers / 15 underactuated DoF, NYU authors; Open source false -> true (ruka-hand/RUKA repo is MIT-licensed), repo added to Sources |
| Robot/model | DLR David variable-stiffness joints | verified |  |
| Robot/model | Festo DMSP fluidic muscle | verified |  |
| Robot/model | PneuNets bending-actuator toolkit | verified |  |
| Robot/model | ToddlerBot | verified | 30 active DoF on site; repo MIT code, hardware non-commercial licence, 2.0 (2025-08) and 2026-01 locomotion release confirmed |
| Project candidate | Motor architecture decision notebook | verified |  |
| Project candidate | Interchangeable motor mounting plate study | verified |  |
| Project candidate | Modular rotary joint cartridge | verified |  |
| Project candidate | Torque-speed envelope from a load case | verified |  |
| Project candidate | Joint duty-cycle thermal estimator | verified |  |
| Project candidate | Instrumented continuous-duty joint fixture | verified |  |
| Project candidate | Planetary tooth-count explorer | verified |  |
| Project candidate | Hand-cranked printed planetary cutaway | verified |  |
| Project candidate | Interchangeable ratio gearbox bench | verified |  |
| Project candidate | Cycloidal eccentric-to-output animation | verified |  |
| Project candidate | Hand-driven cycloidal tolerance experiment | verified |  |
| Project candidate | Guarded dual-disc cycloidal joint prototype | verified |  |
| Project candidate | Strain-wave tooth engagement explainer | verified |  |
| Project candidate | Printed flexspline fit and compliance coupons | verified |  |
| Project candidate | Strain-wave versus cycloidal joint CAD trade study | verified |  |
| Project candidate | Belt and capstan preload explorer | verified |  |
| Project candidate | Hand-driven belt tension reversal rig | verified |  |
| Project candidate | Remote-drive elbow transmission fixture | verified |  |
| Project candidate | Screw lead force-speed visualizer | verified |  |
| Project candidate | Horizontal screw-guide alignment jig | verified |  |
| Project candidate | Supported linear joint module | verified |  |
| Project candidate | Four-bar path sketchbook | verified |  |
| Project candidate | Cardboard cam and follower comparison | verified |  |
| Project candidate | Parallel-link remote-actuated joint prototype | verified |  |
| Project candidate | Tendon routing and slack simulator | verified |  |
| Project candidate | Antagonistic tendon hinge board | verified |  |
| Project candidate | Underactuated tendon differential demonstrator | verified |  |
| Project candidate | Reflected inertia gear-ratio dashboard | verified |  |
| Project candidate | Passive joint friction identification fixture | verified |  |
| Project candidate | Low-impedance joint architecture comparison | verified |  |
| Project candidate | Spring-in-series resonance notebook | verified |  |
| Project candidate | Passive series-spring calibration board | verified |  |
| Project candidate | Guarded series-elastic rotary joint | verified |  |
| Project candidate | Variable-stiffness cam geometry notebook | verified |  |
| Project candidate | Hand-adjusted antagonistic spring hinge | verified |  |
| Project candidate | Dual-adjustment variable-stiffness joint CAD prototype | verified |  |
| Project candidate | Bearing support and load-path CAD review | verified |  |
| Project candidate | Printed bearing-seat fit coupon matrix | verified |  |
| Project candidate | Stiffness-to-mass robot bracket challenge | verified |  |
| Project candidate | Parametric robot joint assembly walkthrough | verified |  |
| Project candidate | CAD-to-robot mass and joint audit | verified |  |
| Project candidate | Manufacturable serviceable elbow design pack | verified |  |
| Project candidate | Pressure-area actuator comparison notebook | verified |  |
| Project candidate | Pneumatic supply architecture digital review | verified |  |
| Project candidate | Supervised low-pressure muscle hinge bench | verified |  |
| Project candidate | PneuNet chamber geometry sketch study | verified |  |
| Project candidate | Soft actuator mold and seal coupon kit | verified |  |
| Project candidate | Supervised soft bending fatigue bench | verified |  |
| Project candidate | Artificial muscle force-stroke evidence atlas | verified |  |
| Project candidate | Electrohydraulic pouch mechanics model | verified |  |
| Project candidate | Thermal magnetic folding mechanism digital twin | verified |  |
| Project candidate | Humanoid knee packaging teardown in CAD | verified |  |
| Project candidate | Equal-envelope leg joint Pareto study | verified |  |
| Project candidate | Captive single-leg actuator test stand | verified |  |
