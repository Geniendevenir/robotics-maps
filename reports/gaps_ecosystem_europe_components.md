# Coverage gaps — Europe / Components

Reviewed 2026-11-13 against `devin/playbooks/coverage-critic.md`, `CLAUDE.md`, `schemas/notion-schema.md` and `reports/verify_ecosystem_europe_components.md`. Input: the verified file `output/ecosystem_europe_components.json` (20 organizations, 16 robots/models). No rows were added or edited, and Notion was not accessed.

**Result: 4 High / 11 Medium / 7 Low gaps (22 total).**

## Scope and method

The slice is Europe, Components, **top 20**: actuators (motors, gearboxes, bearings, screws), sensors (vision, force/torque, tactile, encoders, IMUs), compute/electronics and end effectors. Integrators, finished robots and software are out of scope unless the company is mainly a component supplier.

Canonical references used: the 2026 Fraunhofer IPA / P3 humanoid-supply-chain study, as reported by Euronews and The News [S1–S2], which names the German suppliers everyone in the field expects (Schaeffler, Bosch, Schunk, Wittenstein, Neugart); 2026 trade coverage of humanoid components (Schaeffler's Hermes Award, Faulhaber, SKF) [S3–S5]; the Arm physical-AI launch [S6]; and official sites of European robot-vision, sensing and drive suppliers, opened during this review [S7–S22]. Other output files were checked so that rows mapped elsewhere aren't reported as missing (e.g. Prophesee is in `ecosystem_paris_all.json`).

What the input covers: the main German drive and gripper companies (Schaeffler, maxon, Harmonic Drive, SCHUNK, Festo, igus), the chip companies (Infineon, ST, NXP, Axelera), maker boards (Arduino, Raspberry Pi), SICK, and several hand, sensor and actuator startups. What's missing: **robot 3D vision (no camera supplier at all), Bosch as a supplier in its own right, the second tier of German precision gearbox makers, the compute IP layer (Arm), and tactile sensing.**

Importance is my judgment. **High** = a player people in the field would expect in a European top 20, or a component category with no entry at all. **Medium** = a credible contender for a slot, or useful to the lab as a partner. **Low** = a narrower or borderline alternative.

## High — 4

- **H1. Bosch (Bosch Rexroth + Bosch Sensortec)** — named in the Fraunhofer IPA study as a key German humanoid-parts supplier and slated to produce the SCHUNK–Bosch robot hand. It appears only as a partner inside the SCHUNK row: no row covers Rexroth's drives, linear motion and roller screws or Sensortec's MEMS IMUs, which are common on low-cost robots [S1–S2, S9].
- **H2. Wittenstein** — German maker of precision planetary gearboxes and servo actuators, named alongside Schaeffler and Schunk in the 2026 IPA study. It's the most obvious missing gearbox company after Harmonic Drive [S2, S10].
- **H3. Zivid** — Norwegian maker of industrial 3D cameras for bin-picking and robot guidance. The file has **no robot-vision camera supplier at all**, and 3D perception for manipulation is central to the lab's robot-learning hypothesis [S7].
- **H4. Arm** — UK compute IP behind nearly every robot SoC and MCU in the file (STM32, NXP, Raspberry Pi, Arduino). Its "Total Design for Physical AI" robotics programme launched in September 2026. It's the main European compute player missing from the compute/electronics layer [S6].

## Medium — 11

- **M1. Photoneo (Brightpick spin-off, Zebra Technologies since 2025)** — Slovak 3D-vision maker (MotionCam-3D, PhoXi), still active in Nov 2026. A second European 3D-vision contender. Region needs a call because Zebra owns it [S8, S20].
- **M2. Faulhaber** — German micro-drive maker focused on humanoid hands and exoskeletons in 2026 (DirectIndustry, Apr 2026). The relevant motor supplier for dexterous hands [S4, S11].
- **M3. Beckhoff** — German automation/motion-control company and originator of EtherCAT, the usual joint-bus standard. It appears only in `knowledge_embedded_electronics.json`, not as an ecosystem organization [S12].
- **M4. SKF** — Swedish bearing maker that formed a humanoid precision-components JV with Leaderdrive in July 2026. A major European bearing supplier now moving into robot joints [S5, S13].
- **M5. Neugart** — German planetary gearbox maker named in the IPA study as a humanoid-parts supplier [S2].
- **M6. Prophesee** — Paris event-based vision sensors. It raised €20m in June 2026 and has a GenX320 kit for Raspberry Pi 5. It's already in `ecosystem_paris_all.json`; make sure that row also carries Value chain = Components, rather than duplicating it here [S14].
- **M7. Touchlab** — Edinburgh maker of robot e-skin and tactile sensing (2026 coverage). The file has no tactile-skin supplier, and touch is a key input for dexterous learning [S15].
- **M8. Renishaw / RLS** — UK/Slovenian magnetic and optical encoders used in robot joints, including PAL Robotics humanoids. No encoder supplier is in the file [S16].
- **M9. Zimmer Group** — German gripper and end-of-arm maker, the main European alternative to SCHUNK and OnRobot [S17].
- **M10. Schmalz / Piab** — German and Swedish vacuum-gripping suppliers. Vacuum end effectors dominate logistics picking and are absent from the file [S18–S19].
- **M11. Sonair** — Norwegian 3D ultrasonic safety sensor for mobile robots. Funded in 2025 (US$6m) and launched in April 2026. An emerging-sensor contender [S21].

## Low — 7

- **L1. Spinea** — Slovak cycloidal reducers. A niche alternative to strain-wave gears [S22].
- **L2. Rollvis** — Swiss planetary roller screws for linear humanoid actuators. Niche [site opened].
- **L3. Nanotec** — German stepper/BLDC motors and controllers. A low-cost motor alternative to maxon [site opened].
- **L4. SBG Systems** — French IMU/INS maker for mobile and field robots. Borderline (mostly navigation and aerospace).
- **L5. Haption** — French haptic devices for teleoperation. Relevant to collecting teleop data but niche.
- **L6. Basler / IDS Imaging** — German 2D industrial cameras (IDS also partners with Prophesee). Lower priority if a 3D-vision supplier is added.
- **L7. Distributors (RS Group, Farnell)** — UK component distributors. These are hardware-sponsor channels, not makers; include them only if the map is meant to track sponsor routes.

## Product (Robots & Models) gaps

The 16 products are mostly humanoid-industry parts. If the orgs above are added, the matching products belong with them (e.g. a Zivid 2+ camera, Prophesee GenX320 kit). The lab-relevant gap is that **Raspberry Pi has an org row but no product row** (e.g. Raspberry Pi 5 / AI Camera), even though these are the boards students on the SO-101/LeRobot stack actually use. This counts under M-level priority and isn't added to the totals above.

## Boundaries (not counted as gaps)

- Hailo (Israel, being acquired by Microchip) is outside Europe. It's already mentioned in the embedded-electronics knowledge file.
- Pollen Robotics, Wandelbots, Inbolt and Exail are platform, software or other-slice companies, and are already in other files.
- Heidenhain (encoders) blocked access during this review. It's an alternative to M8, not listed separately.

## Recommendation

Re-run the researcher on **H1–H4 only**, re-ranking against the current 20 rather than appending. The weakest current slots for a top-20 list are probably the very early startups (Allonic, AdapTronics, Enact Intelligence), but that's a ranking call for the researcher and verifier. Medium items are deliberate tradeoffs, not required additions.

## Sources (opened)

- S1. https://www.euronews.com/2026/10/01/humanoid-robots-china-builds-them-but-germany-could-supply-the-joints-and-hands
- S2. https://www.thenews.com.pk/latest/1418316-study-reveals-germanys-edge-in-humanoid-robot-parts
- S3. https://www.machinedesign.com/markets/robotics/video/55373890/schaeffler-group-us-integrated-actuation-is-key-to-affordable-humanoidsschaefflers-hermes-award-win-shows-why
- S4. https://emag.directindustry.com/2026/04/14/humanoid-robotics-demands-dexterity-in-motion-by-faulhaber/
- S5. https://autonews.gasgoo.com/articles/news/skf-partners-with-leaderdrive-to-establish-joint-venture-targeting-humanoid-robot-precision-components-2073279071470268417
- S6. https://www.artificialintelligence-news.com/news/arm-total-design-for-physical-ai-and-robotics-framework/
- S7. https://www.zivid.com
- S8. https://www.photoneo.com
- S9. https://www.bosch-sensortec.com
- S10. https://www.wittenstein.de/en-en/ (Cloudflare check page via curl. Identity is also confirmed by S2.)
- S11. https://www.faulhaber.com/en/
- S12. https://www.beckhoff.com/en-en/
- S13. https://www.skf.com
- S14. https://www.prophesee.ai and https://aeromorning.com/en/prophesee-raises-e20m-and-launches-mantara/
- S15. https://touchlab.io and https://www.techradar.com/pro/groundbreaking-technology-often-enters-the-market-at-a-premium-before-scaling-touch-sensitive-e-skin-could-soon-be-commonplace-in-robotics
- S16. Google News RSS: "Renishaw and RLS help to drive a robot revolution", The Robot Report, 2024 (headline only)
- S17. https://www.zimmer-group.com/en/
- S18. https://www.schmalz.com/en/
- S19. https://www.piab.com
- S20. Google News RSS: "Zebra Technologies Completes Acquisition of Photoneo", Business Wire, Mar 2025; "Photoneo Updates 3D Scanning Platform with PhoXi Control 1.18", Nov 2026 (headlines)
- S21. https://www.sonair.com, plus Google News RSS headlines (ArcticStartup Sep 2025; MMH Apr 2026)
- S22. https://www.spinea.com/en/
- Also opened (title check): https://www.rollvis.com, https://www.nanotec.com/eu/en, https://www.sbg-systems.com, https://www.haption.com/en/, https://www.ewellix.com/en (now redirects to Schaeffler, so it's covered by the existing Schaeffler row)
