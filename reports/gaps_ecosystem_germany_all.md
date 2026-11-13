# Coverage gaps: output/ecosystem_germany_all.json

Coverage-critic run on branch `research/ecosystem-germany-all` (verified file, commit bb2f466). No rows added. No Notion read/write.

Scope checked: top ~40 German organizations for a student robot-learning lab, across all types, covering Munich, Berlin, Stuttgart/Karlsruhe, Dresden, Hamburg and Cologne/Aachen.
Organizations already in other `output/*.json` files on `origin/main` count as covered and are not listed here. Examples: NEURA, Agile Robots, Franka, RobCo, KUKA, Sereact, Wandelbots, Micropsi, microagi, Quantum Systems, Festo, SCHUNK, Schaeffler, SICK, Synapticon, Harmonic Drive, igus, Infineon, Dürr, Siemens, BMW, Mercedes-Benz, Zalando, DHL, Körber, Fraunhofer IPA, Headline, HV Capital, Vsquared, automatica, Hannover Messe, LogiMAT, RoboCup German Open / RoboCup 2027 Nuremberg, Formula Student Germany, euROBIN, ROS-Industrial Consortium Europe.

## References used
- Robotics Institute Germany site (research areas, GRC 2025/2026/2027 event pages): https://robotics-institute-germany.de/
- Lab and university pages opened: alr.iar.kit.edu, rl.uni-freiburg.de, dsme.rwth-aachen.de, igmr.rwth-aachen.de, ce.cit.tum.de/lsy, scienceofintelligence.de, fzi.de, lamarr-institute.org, tuhh.de/ics
- Event, startup and investor pages opened: hack.tum.de, unternehmertum.de, appliedai.de, idealworks.com, robominds.de, germanbionic.com, cellumation.com, matterwave.vc, earlybird.com, project-a.com
- Google News RSS discovery (Germany robotics funding 2026, Berlin/Dresden/Karlsruhe/Aachen robotics, German Robotics Conference, Robotik-Hackathon 2026). Hits included "New NEURA Gym with RWTH Aachen" (Business Wire), "VW unveils mobile charging robot prototype in Dresden" (electrive.com), "HU team takes third place at the German Robot Football Championship" (Technologiepark Adlershof), and "Robin Capital closes €15 million second fund" (EU-Startups).

## Hub coverage
- Munich: strong (10+ rows). No gap here at High level.
- Stuttgart/Karlsruhe: MPI-IS, Cyber Valley, KIT H2T, BCAI, plus NEURA/Sereact/IPA/Festo/SCHUNK on main. Missing the KIT robot-learning lab (ALR).
- Hamburg: good (TAMS, Bit-Bots, Jungheinrich, goodBytz, Naiture, 40C3).
- Dresden: CeTI and the CeTI hackathon, plus Wandelbots on main. No corporate.
- Berlin: RBO, c-base and MotionLab, plus Zalando/Micropsi/Headline on main. Thin on research beyond RBO and on student teams.
- Cologne/Aachen: weakest hub. Only Fab Lab Aachen (plus igus, euROBIN and RoboCup German Open on main). No university or research lab from the hub.

## High
- RWTH Aachen University robotics (e.g. Institute for Data Science in Mechanical Engineering, learning-based control, Prof. Trimpe; IGMR robotics institute): the main university of the Cologne/Aachen hub is missing, and the hub has no research row. NEURA opened a "NEURA Gym" physical-AI training site with RWTH (Business Wire, 2026).
- KIT Autonomous Learning Robots (ALR) Lab, Karlsruhe: KIT's lab dedicated to "novel machine learning methods for robotics" (alr.iar.kit.edu). It is the core robot-learning group at KIT, and the file only has KIT H2T (humanoids).
- German Robotics Conference (GRC, organized by Robotics Institute Germany): the national robotics research conference, with 2025, 2026 and 2027 editions, an exhibitor program and registration (robotics-institute-germany.de/event/grc2027/). It is the best German venue for 42AI to show research and meet labs, and no German research conference is in the file.
- University of Freiburg Robot Learning Lab (Prof. Abhinav Valada): one of Germany's leading robot-learning labs. Topics include language-grounded scene graphs for mobile manipulation, whole-body teleoperation and learning long-horizon manipulation from few demonstrations (rl.uni-freiburg.de). It is outside the six named hubs but central to the robot-learning wedge.

## Medium
- TUM Learning Systems and Robotics (Prof. Angela Schoellig), Munich: a separate TUM chair that teaches "Advanced Robot Learning" (ce.cit.tum.de/lsy). MIRMI is only the umbrella row.
- Science of Intelligence (SCIoI) Cluster of Excellence, Berlin (TU Berlin/HU Berlin): the main Berlin robotics/AI research cluster beyond RBO, including Marc Toussaint's learning & intelligent systems group (scienceofintelligence.de). The TU Berlin LIS page URL I tried returned 404.
- hackaTUM, Munich: TUM's large annual student hackathon with editions from 2016 to 2025 and corporate sponsors (hack.tum.de). It is a direct peer event for 42AI.
- UnternehmerTUM (the center itself: incubator/accelerator programs, Key Industries such as Advanced Manufacturing), Garching/Munich: only its MakerSpace subsidiary is in the file.
- FZI Research Center for Information Technology, Karlsruhe: an applied robotics/AI institute with the "House of Living Labs" (fzi.de). It is a natural industry-transfer partner.
- University of Stuttgart robotics (e.g. ISW/IFF and the Stuttgart AI ecosystem): Stuttgart's main university is missing. isr.uni-stuttgart.de timed out from this VM, so I could not confirm which specific lab to use.
- Volkswagen (Dresden Gläserne Manufaktur being turned into an AI/robotics innovation campus; mobile charging-robot prototype, 2026): Dresden has no corporate row, and VW is a potential sponsor or demand partner.
- idealworks (BMW Group subsidiary), Munich: iw.hub AMRs, the Idealworks OS fleet orchestration and the "iw.sim" simulation-to-live tool (idealworks.com). Relevant for sim-to-real, and not covered under BMW.
- robominds, Munich: "Künstliche Intelligenz für die Industrie-Robotik" (robobrain 2.0) and its own "robominds open" industrial AI-robotics event (robominds.de).
- Lamarr Institute for ML and AI (Bonn/Dortmund): has an "Embodied AI" research area (lamarr-institute.org). It is the NRW AI institute next to the Cologne/Aachen hub.

## Low
- Berlin United / Nao Team Humboldt (HU Berlin RoboCup team): took third place at the German Robot Football Championship (Technologiepark Adlershof). It would be a Berlin student-team peer; the file has none.
- Hacker spaces in the other hubs (e.g. muCCC Munich, shackspace Stuttgart, Entropia Karlsruhe, C3D2 Dresden, C4 Cologne): only c-base (Berlin) and Fab Lab Aachen are listed. Not opened in this run.
- German Bionic, Augsburg: AI-powered exoskeletons (Exia) (germanbionic.com).
- voraus robotik, Hannover: robot-control software. The site timed out from this VM.
- Cellumation, Bremen: modular conveyor technology (cellumation.com). Weak robot-learning fit.
- Earlybird (Berlin/Munich) and Project A (Berlin): large German VCs. The file has no Berlin investor apart from Headline on main. Their robotics portfolios were not checked.
- Robin Capital (Berlin solo VC): closed a €15M second fund for AI, robotics and space (EU-Startups, 2026).
- Matterwave Ventures, Munich: early-stage VC for European industrial-technology hardware and software (matterwave.vc).
- SECAI (School of Embedded Composite AI, Dresden/Leipzig): a Dresden AI graduate school (DAAD interview with its deputy director). Possible academic partner.
- TUHH (Hamburg University of Technology): Hamburg's technical university is missing, but TAMS already covers Hamburg robotics research.

## Notes for a re-run
- The file is already at 40 rows. Adding the High items means swapping out weaker fits. Possible candidates to drop: Fraunhofer IML (Dortmund, outside the hubs), Unchained Robotics (Paderborn), Nature Robots (Osnabrück), and Helsing/ARX (defence, which the summary itself calls "a poor fit for a student lab").
- I checked every gap against `output/*.json` on `origin/main` (name and keyword grep): none of them appears there.
