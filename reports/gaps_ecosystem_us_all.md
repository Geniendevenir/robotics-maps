# Coverage gaps: output/ecosystem_us_all.json

Critic run on branch `research/ecosystem-us-all` (file after verification: 25 organizations + 21 robots/models; slice US / all layers / top 25).
References used: the US players an industry reader would expect (A3/Automate exhibitor categories, Robotics Summit / RoboBusiness programs,
Crunchbase/Dealroom-style lists of the largest US robotics companies and investors, top US robotics universities, CoRL/ICRA sponsor lists),
plus the candidate list in reports/research_ecosystem_us_all.md. No rows added; no Notion access.
Items come from domain knowledge and were **not** web-checked in this pass: the researcher must confirm each with an opened primary source
(items marked "verify" are less certain). A top-25 cap means some gaps should replace weaker rows rather than be appended.
Cross-file names already present elsewhere (Google DeepMind in ecosystem_europe_software_ai, Hugging Face/LeRobot in ecosystem_paris_all,
OpenVLA, Diffusion Policy, ALOHA 2, MuJoCo in knowledge_manipulation, Jetson Thor in knowledge_embedded_electronics) are not listed as missing rows.

## High
- Waymo (Mountain View) — largest deployed driverless robot fleet in the US; the Mobility sector has no anchor row (Tesla row is humanoid/FSD-adjacent only).
- Intrinsic (Alphabet, Mountain View) — industrial robot software (Flowstate) and owner of the former Open Robotics commercial arm; referenced in the OSRF row but absent.
- Anduril Industries (Costa Mesa) — defense autonomy/drones leader; Defense sector appears only as a Lux Capital tag (researcher itself flags this as a material gap).
- Zipline (South San Francisco) — largest drone-delivery operator; no Drone form factor or drone company in the US slice.
- John Deere (incl. Blue River Technology) — autonomous tractors / See & Spray; the Agri sector is entirely absent.
- A3 — Association for Advancing Automation (Ann Arbor) — main US robotics trade association, organizer of Automate (already a row) and publisher of US robot-order statistics.
- Trossen Robotics (Downers Grove, IL) — maker of the ALOHA / WidowX arms used by Mobile ALOHA, Open X-Embodiment and many robot-learning papers; most directly relevant US hardware vendor for the low-cost robot-learning wedge.
- NVIDIA Isaac GR00T N1.x (robot/model row) — NVIDIA's open humanoid foundation model (VLA) is the best-known US open robot model besides pi0, missing under the NVIDIA row.
- Robotics-heavy US investors beyond Lux and DCVC — e.g. Eclipse Ventures, Khosla Ventures, Thrive Capital, a16z (American Dynamism), Playground Global; only 2 investors for the world's largest robotics funding market.

## Medium
- Covariant (Emeryville; RFM-1, team licensed to Amazon in 2024 — verify current status) — canonical warehouse-picking foundation-model company.
- Dyna Robotics and Generalist AI (verify) — 2025 robot-foundation-model startups the researcher shortlisted but did not investigate.
- Hello Robot (Stretch 3 mobile manipulator) — widely used affordable research mobile manipulator; note name clash with Boston Dynamics Stretch.
- Applied Intuition (Mountain View) — autonomy/simulation software for vehicles and defense; large Software & AI player.
- PickNik Robotics (Boulder) — maintainer of MoveIt (MoveIt 2 is a knowledge_manipulation row with no US builder org).
- Foxglove and Viam — robotics developer tooling (observability, robot platform) with community programs and events.
- Meta FAIR robotics (Menlo Park / Pittsburgh) — Habitat simulator, DIGIT/Sparsh tactile sensing, robot-learning research.
- OpenAI robotics team (verify current scope) — restarted robotics effort; frequently expected by readers.
- Components layer is only NVIDIA: Intel RealSense (depth cameras, spun out 2025 — verify), Ouster (lidar, SF), Qualcomm (robotics SoCs; Arduino acquisition announced 2025 — verify).
- Symbotic (Wilmington, MA) and Locus Robotics — warehouse automation beyond Amazon; Logistics demand side.
- Dexterity (Redwood City) — truck-loading/parcel manipulation with learned policies.
- Medical beyond Intuitive: Stryker (Mako) and Medtronic (Hugo) — orthopedic/soft-tissue surgical robots.
- Shield AI and Ghost Robotics — second-tier Defense (AI pilot software; military quadrupeds).
- Carbon Robotics (Seattle, LaserWeeder) — Agri startup counterpart to John Deere.
- Georgia Tech IRIM, UPenn GRASP Lab, University of Washington, University of Michigan Robotics — top US robotics schools beyond the four listed.
- IEEE Robotics and Automation Society (RAS) — organizer of ICRA/IROS/Humanoids; US-headquartered society with student chapters.
- Physical AI Hack / LeRobot hackathon San Francisco (page opened by the researcher) — the most wedge-relevant US event; the slice has no hackathon row.
- Humanoids Summit (Mountain View) and CES (Las Vegas) — major humanoid/consumer robotics showcases.
- Open X-Embodiment (Google DeepMind + US labs) and DROID (Stanford/Berkeley/TRI) datasets — key US-led robot-learning datasets, no row anywhere.
- TRI Large Behavior Models and UMI (Universal Manipulation Interface, Stanford/Columbia) — robot-learning model/tool rows tied to TRI and Stanford.
- NVIDIA Cosmos (world foundation models) — World model type has no US row.

## Low
- iRobot (Bedford, MA; Roomba; post-2025 restructuring — verify) — historic US consumer robotics company.
- Columbia (Diffusion Policy origin), NYU (Dobb-E/Stick), UT Austin Texas Robotics, Northeastern — additional robot-learning research groups.
- FIRST Robotics (Manchester, NH) — largest student robotics competition; community/visibility reference rather than a partner.
- RoboBusiness (Santa Clara) and the Robot Report — trade event and main US robotics news outlet.
- Pittsburgh Robotics Network, Texas Robotics, USARC (verify) — regional associations/clusters.
- NSF robotics funding programs (verify current program name) and DARPA (e.g. robotics challenges) — public funders, low relevance for a French student lab.
- Formic (robots-as-a-service), Bear Robotics, Serve Robotics — integration/service robotics.
- Saronic, Hadrian (verify) — defense maritime autonomy and automated manufacturing.
- World Labs — spatial-intelligence world models, adjacent to robotics simulation.
- Microsoft and Amazon AWS robotics/cloud programs (verify) — possible compute credits; Hardware/Compute potential otherwise only NVIDIA.
- Robot rows: Unitree-equivalent US low-cost platforms are absent; consider WidowX 250 / ALOHA (Trossen), Stretch 3 (Hello Robot), Spot Arm variants if those orgs are added.
- Process: saturation not established (per research report); 3 consecutive broad discovery queries with <10% new entries are still needed.
