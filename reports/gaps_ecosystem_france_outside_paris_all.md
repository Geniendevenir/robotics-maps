# Coverage gaps: output/ecosystem_france_outside_paris_all.json

Critic run on branch `research/ecosystem-france-outside-paris-all`. File after verification: 89 organizations + 47 robots/models.
References: Paris-slice gaps report (items marked "move to a France slice"), French competitiveness clusters and IRT/RTO lists,
the GdR Robotique lab directory, regional trade shows, French robotics/medtech/agtech players most people in the field would
expect, and the 42AI wedge (robot learning on low-cost hardware). No rows added; no Notion access.
Items come from domain knowledge and were **not** web-checked in this pass. The researcher must confirm each one with a primary
source; "(verify)" marks less certain items. Names were checked against all output/*.json files so items already covered elsewhere are left out.

## High
- Naver Labs Europe (Meylan, Grenoble area): the largest industrial AI/robotics research lab in the region (robot learning, 3D vision, embodied AI). It's a direct fit for the robot-learning wedge and missing from the file.
- Airbus (Toulouse; Blagnac): largest corporate outside Paris, uses robotics in aircraft assembly and inspection, and is an obvious sponsor/demand anchor. Donecle and Delair are in the file, but their biggest demand-side customer is not.
- STMicroelectronics (Crolles/Grenoble, Rousset): the STM32 MCUs and ToF/IMU sensors that hobby and low-cost robots use. The Components layer has only 4-5 rows, and a team that's weak in electronics would expect this sponsor/partner.
- Medtech SA / Zimmer Biomet Robotics (Montpellier): designed the ROSA surgical robot, France's best-known surgical-robotics success. Add the ROSA robot row too.
- EasyMile (Toulouse): autonomous shuttles/tow tractors and a flagship Toulouse autonomy startup. Mobility is nearly absent (only TwinswHeel is there).
- ANITI (Toulouse), MIAI (Grenoble) and 3IA Côte d'Azur (Nice): France's interdisciplinary AI institutes, all with robotics/embodied-AI chairs. They're the main AI-research and partnership hubs outside Paris.
- 42 network campuses outside Paris (42 Lyon, 42 Nice, 42 Mulhouse, 42 Angoulême, 42 Perpignan, 42 Le Havre; verify the current list). These are sister campuses and the warmest contact path for 42AI to run multi-city robotics events or teams.
- GdR Robotique (CNRS national research network): the national directory of French robotics labs and the organiser of the JNRR/doctoral schools. The Paris critic already flagged it for this slice.
- Rhoban `placo` (LaBRI – Rhoban, Bordeaux): the open-source kinematics/whole-body solver that LeRobot uses for SO-101 kinematics. It's a key Robots & Models row for the wedge, and the file lists SigmaBan/UltraBan but not placo.

## Medium
- IRT Jules Verne (Nantes), IRT Saint Exupéry (Toulouse) and CETIM (Senlis/Saint-Étienne): technology research institutes with robotics/cobotics platforms. They're the industrial R&D partners that a student team needs for mechanics.
- CEA-Leti / CEA Grenoble: microelectronics and sensors for robotics (CEA-List is in the Paris file; the Grenoble side is missing).
- ONERA (Toulouse, Salon-de-Provence): aerospace research with drone autonomy and perception.
- CNES (Toulouse): space robotics (Mars rover instruments, operations centres) and a known sponsor of student challenges.
- INRAE (Clermont-Ferrand, Montpellier): agricultural robotics research behind much of the Agri sector in the file.
- Inria Grenoble/Lyon teams (CHROMA, Thoth; verify team names after the 2024-2025 Inria reorganisation) and Inria Sophia ACENTAURI: robot perception/learning and aerial robotics teams missing next to the Inria teams already listed.
- CRIStAL (Lille): the robotics/AI lab behind several Lille teams. Only Inria DEFROST is covered.
- Ampère (Lyon) and LIRIS (Lyon): Lyon robotics/vision labs. Lyon has only INSA Lyon and Clubelek on the research/education side.
- Navya → Gama (Lyon; verify post-2023 status): autonomous shuttle maker and a well-known Lyon name.
- Visual Behavior (Lyon; verify status): perception AI for autonomous robots, a software-first startup close to the wedge.
- Elistair (Lyon area): tethered drones. Drone coverage outside Bordeaux/Toulouse is thin.
- Pellenc (Pertuis) and Kuhn (Saverne): major agri-machinery makers with robotics/automation lines. These are the big corporates of the Agri sector.
- Sabi Agri (Clermont area; verify): electric agricultural robots.
- BA Systèmes (Mordelles, Rennes area): AGV/AMR manufacturer that's missing from the Logistics sector.
- Subsea Tech (Marseille) and ECA Robotics sites (Toulon/La Garde; check against Exail in the Paris file): underwater/naval robotics in the South.
- Michelin (Clermont-Ferrand), Stellantis plants (Sochaux, Mulhouse), Schneider Electric (Grenoble) and Orano (La Hague, nuclear robotics): large regional Demand-side corporates with robotics use.
- Thales Alenia Space (Cannes, Toulouse): space robotics demand/R&D.
- Competitiveness clusters Aerospace Valley (Toulouse/Bordeaux), Minalogic (Grenoble), EMC2 (Nantes) and Pôle Mer Méditerranée/Bretagne: national directories of robotics members. Only robotics-specific associations are listed.
- EuraTechnologies (Lille): major incubator with hardware/robotics startups next to Niryo/Exotec.
- Schools: Grenoble INP, Bordeaux INP (ENSEIRB-MATMECA, home of Eirbot), ENSTA Bretagne (Brest, underwater robotics), Arts et Métiers campuses, UTC Compiègne, IMT Atlantique, Polytech Montpellier. Only 4 schools are listed for an "exhaustive" slice.
- Student clubs that win Eurobot/Coupe de France: RCVA (Angers), Eirbot (Bordeaux) and other INSA/ENSEA-style clubs (check the coupederobotique.fr team lists). These are peer contacts for the 42AI hardware gap.
- JNRR (Journées Nationales de la Recherche en Robotique) and ROSCon France (verify the city of each edition): national research and ROS community events held outside Paris.
- SITEVI (Montpellier): vine/wine and agri-machinery show with a robotics area, a natural companion to World FIRA.
- Hi Inov (Lyon) and Sofimac Innovation (Clermont-Ferrand): regional VCs with industrial/deeptech portfolios. Only about 7 investors are listed for all regions.
- mc_rtc (LIRMM with AIST): open-source humanoid/multi-robot control framework, a Robots & Models row that's missing next to Pinocchio/Crocoddyl.

## Low
- RoboCup 2023 Bordeaux (past event; context for Rhoban's results) and Eurobot finals history.
- ABB, Yaskawa, KUKA and FANUC regional French sites/integrator networks (most French HQs are in Île-de-France, so check the slice before adding).
- Gaussin (Héricourt; verify status), Sterela (Toulouse), Akeoplus (Château-Renault; verify), Wyca (verify): smaller logistics/industrial robotics players.
- Lynred (Grenoble, IR sensors) and Sysnav (Vernon, navigation): Components niche players.
- KNDS/Nexter (Bourges) and Naval Group Toulon (verify site roles): Defense UGV/UUV programs.
- SATT Linksium (Grenoble), Toulouse Tech Transfer and other SATTs: lab-to-startup transfer offices.
- IRIMAS (Mulhouse), LITIS (Rouen), LIS (Marseille), IRIT (Toulouse), LIMOS (Clermont): smaller robotics teams from the GdR directory.
- Regional makerspaces/fablabs (e.g. Fabrique de Toulouse/Artilect, Lyon fablabs; verify): mechanics/electronics help.
- Robots & Models rows for listed orgs: Reachy 2 is only in the Paris file (check cross-file), Naïo Dino/Ted, Stäubli TX2/TS2 series, Niryo One (legacy), Kompaï robot, and LAAS TALOS "Pyrène" (PAL-built).
- Endocontrol (Grenoble) and Collin Medical (verify): smaller medical robotics.

## Counts
High: 9 · Medium: 26 · Low: 10
