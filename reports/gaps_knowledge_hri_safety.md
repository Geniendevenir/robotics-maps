# Coverage gaps: knowledge_hri_safety.json (HRI & safety branch)

Reviewed file: `output/knowledge_hri_safety.json` (18 nodes, 19 robots/models, 54 project candidates), after verification (see `reports/verify_knowledge_hri_safety.md`).

References compared against: Springer Handbook of Robotics (2nd ed.) TOC, Part G "Robots and Humans" (HRI, social robotics, physical HRI, haptics/telepresence, wearable robots/exoskeletons, roboethics) and the safety chapters; ACM/IEEE HRI, IEEE RO-MAN, ICRA/RSS/CoRL HRI and safe-learning tracks (2024-2026); standard HRI course syllabi (Bartneck et al. textbook structure); the industrial safety standards stack (ISO 12100, ISO 10218-1/-2:2025, ISO/TS 15066, ISO 13849, IEC 62061, IEC 60204-1, ISO 3691-4, ISO 13482); and EU regulation relevant to a lab building robots (Machinery Regulation 2023/1230, AI Act 2024/1689, Cyber Resilience Act, GDPR).

Scope note: only gaps inside the HRI & safety branch, or rows this branch is expected to link to. "(cross-branch)" marks items another researcher may own. Items below are well-known names from the field; their URLs were not re-opened in this pass, so the researcher must source and verify each one before adding a row.

## High

- **Functional safety of control systems (ISO 13849-1/-2 Performance Levels, IEC 62061 SIL, IEC 60204-1 stop categories 0/1/2, e-stop, safety-rated monitored stop)**, Knowledge node (Fundamental): how a safety function is actually built and rated; the standards node lists ISO 12100/10218/13482 but none of these (0 mentions of 13849, 62061, "functional safety", "Performance Level").
- **Safety sensors & safety-rated hardware (safety laser scanners, light curtains, safety mats, safety PLCs/relays; vendors SICK, Pilz, Keyence, Omron)**, Knowledge node + Robots & Models: the SSM node explicitly says "industrial safety-sensor vendors (not researched)"; 0 mentions of SICK, Pilz or light curtains.
- **Teleoperation & immersive (VR/AR) interfaces for robots**, Knowledge node (Fundamental/Applied): "Basic teleoperation" is a stated prerequisite of Shared control and two projects are teleoperated, but there is no node; it is also how SO-101/LeRobot demonstration data is collected (wedge link).
- **Trust, transparency & explainability in HRI (trust calibration, over-/under-trust, explaining robot failures)**, Knowledge node: a core HRI/RO-MAN topic and Springer HRI chapter theme; only 1 incidental mention of "trust", 0 of explainability/transparency.
- **Ethics, privacy & data protection for HRI (GDPR/CNIL for camera, voice and user-study data; informed consent; roboethics)**, Knowledge node: many projects record people (webcam pose, voice, 10-person studies) yet 0 mentions of GDPR, privacy or ethics; the EU regulation node covers only the Machinery Regulation and AI Act.

## Medium

- **Robot cybersecurity (Cyber Resilience Act 2024/2847, Machinery Regulation corruption/protection requirements, SROS2 for ROS 2)**, Knowledge node or extension of the EU regulation node: 0 mentions of cyber/security; RoboPAIR covers only semantic jailbreaks.
- **Mobile robot / AMR safety standards (ISO 3691-4 driverless trucks, ANSI/A3 R15.08)**, extension of the standards node: Nav2 and social-navigation projects have no mobile-robot safety standard.
- **Nonverbal communication: gaze, gesture, proxemics, affect/emotion recognition**, Knowledge node: gaze/gesture appear only inside other rows; 0 mentions of proxemics, emotion or affective computing (a full HRI course unit).
- **Social navigation & human-motion datasets/benchmarks (ETH/UCY, JRDB, SocNavBench/CrowdNav; Human3.6M/AMASS for body motion)**, Robots & Models: "Trajectron++ on lab footage" and the social-nav projects have no dataset or benchmark row.
- **Socially assistive robotics for specific users (eldercare, autism therapy, education, rehabilitation)**, Knowledge node: only one coach project; 0 mentions of eldercare/children/autism.
- **Runtime monitoring & failure / out-of-distribution detection for learned policies (VLA failure detection, uncertainty, safe stop on anomaly)**, Knowledge node (Frontier): directly relevant to the VLA wedge; the safe-learning node covers CBF filters but not monitors (0 mentions of OOD/anomaly/runtime monitor).
- **Human-robot teaming & task allocation in collaborative assembly (role assignment, fluency metrics)**, Knowledge node: HRC prediction is covered but not joint task planning/teaming.
- **Augmented / mixed reality for HRI (intent visualization, VAM-HRI)**, Knowledge node or fold into teleoperation node: one MR kinesthetic project exists without a supporting node.
- **Common HRI/assistive platforms: PAL Robotics TIAGo / ARI (EU), Hello Robot Stretch, Kinova Gen3/JACO (assistive shared autonomy), Pollen Reachy 2 (Paris), SoftBank/Aldebaran Pepper**, Robots & Models: none are rows; Reachy Mini is referenced cross-file only.
- **Relevant orgs / ecosystem anchors for the branch (INRS, LAAS-CNRS HRI team, ISIR, euRobotics HRI topic group, A3, IFR, ACM/IEEE HRI and RO-MAN conferences)**, Relevant orgs relations (cross-branch with ecosystem files): Built by/Used by/Relevant orgs are all empty, so the branch has no link to the French/European ecosystem.

## Low

- **Haptics & force-feedback teleoperation (bilateral control, telepresence)**, Knowledge node: Springer Part G chapter; 0 mentions of haptic.
- **Wearable robots & exoskeletons (pHRI safety)**, Knowledge node (cross-branch, hardware-heavy, low fit for the lab).
- **Reachability analysis / formal verification for safety (Hamilton-Jacobi reachability, shielding)**, extension of the safe-learning node: only 2 passing mentions of "formal/reachability".
- **Impedance / admittance control and compliant actuation (series elastic actuators)**, Knowledge node (cross-branch, manipulation/control): prerequisite of hand-guiding but only 1 mention.
- **Standard HRI instruments (Godspeed questionnaire, NASA-TLX, Wizard-of-Oz method)**, Best resources of the HRI foundations node: questionnaires are mentioned but none named.
- **EU Product Liability Directive 2024/2853 (software and AI covered)**, extension of the EU regulation node.
- **Other cobots used in HRI research (KUKA LBR iiwa, Doosan, Fanuc CRX, Neura MAiRA)**, Robots & Models: UR5e and FR3 are enough for the lab; adding one EU-built cobot would help comparisons.
- **Speech-to-speech conversational models (e.g. realtime voice APIs, open speech-to-speech models)**, Robots & Models: only Whisper (ASR) is listed for the voice pipeline.

## Notes
- Overall coverage of the core topics (standards, PFL/SSM, pose tracking, shared autonomy, handovers, legibility, social navigation, safe learning, LLM/VLA semantic safety, humanoid safety) is good and current (2024-2026 sources).
- Re-run the researcher on the 5 High gaps only.
