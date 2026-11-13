# Coverage gaps: output/ecosystem_switzerland_all.json

Critic run on branch `research/ecosystem-switzerland-all` (file after verification: 120 organizations + 49 robots/models).
Reference for depth: `output/ecosystem_paris_all.json` and its gaps report. References used: well-known Swiss players
(ETH/EPFL lab directories, spin-off lists, Swiss trade fairs and student competitions, Swiss VC/incubator landscape),
plus Google News RSS checks. Organizations already in other `output/*.json` files on main are treated as covered and
not listed (e.g. ANYbotics, ETH RSL, ABB Robotics, maxon, Swisslog, Bota Systems, Flexion Robotics, mimic robotics,
Hexagon Robotics, CYBATHLON, Redalpine, Google DeepMind, NVIDIA, Eurobot, Sony). Wingman Ventures = Founderful (present).
No rows added; no Notion access. "(site opened)" = official site returned HTTP 200 in this pass; everything else is
domain knowledge the researcher must confirm with a primary source ("verify" = less certain).

## High
- RIVR (formerly Swiss-Mile, Zurich) — ETH RSL spin-off, stair-climbing wheeled-legged delivery robots; acquired by Amazon (2026 news: swissinfo, Startupticker); best-known Zurich robotics startup missing (rivr.ai opened).
- CERN robotics (Geneva, EN-SMM mechatronics & robotics / CERN Knowledge Transfer) — teleoperated maintenance robots; biggest Geneva robotics player, Geneva coverage is thin (kt.cern opened).
- Hocoma / DIH (Volketswil, Zurich) — Lokomat/Armeo rehabilitation robots, Swiss medical-robotics anchor (dih.com opened; hocoma.com 404s, use DIH).
- Balgrist University Hospital / Balgrist Campus (UZH, Zurich) — orthopaedic surgical-robotics research (ROCS) and clinical partner for exoskeleton/rehab startups (site opened).
- ETH Zurich Gramazio Kohler Research + NCCR Digital Fabrication — robotic fabrication in architecture, maintains open-source COMPAS framework (site opened, COMPAS DEV event Dec 2026).
- Institute of Neuroinformatics (INI, UZH/ETH) — neuromorphic vision origin of iniVation/event cameras; major Zurich lab missing (site opened).
- Swiss AI Initiative + CSCS (Lugano, Alps supercomputer, Apertus) — compute grants for open AI research; key compute partner for a robot-learning lab and Ticino anchor (both sites opened).
- EPFL Racing Team (Lausanne) — ~150-student electric + driverless Formula Student team; EPFL counterpart of AMZ Racing (site opened).
- Pix4D (Prilly/Lausanne) — leading drone photogrammetry/mapping software company; drone software layer missing (site opened).
- Lakestar (Zurich) — top Swiss-founded VC; investor coverage (8 rows) is far below Paris depth (site opened).
- Missing EPFL robotics labs: Automatic Control Lab (LA), DISAL (Martinoli, swarm/distributed robotics), VITA (Alahi, autonomous-vehicle perception) — only 7 EPFL labs listed (sites opened).

## Medium
- EPFL CHILI (child-robot interaction/HRI), MOBOTS (Mondada, Thymio/education robots), REHAssist (rehab/assistive robotics) labs (sites opened).
- ETH Learning & Adaptive Systems group (Krause, safe RL/robot learning) and ETH Rehabilitation Engineering Lab (relab) (sites opened).
- ETH Environmental Robotics Lab (Mintchev, WSL/ETH drones in nature) — verify URL (erl.ethz.ch timed out).
- University of Bern ARTORG Center — surgical/medical robotics; mentioned in the file but no org row (verify).
- USI / SUPSI (Lugano) as School rows — only IDSIA is listed; Ticino schools absent (supsi.ch opened).
- ClearSpace (Renens/Lausanne) — EPFL spin-off, space-robotics debris removal/servicing (site opened).
- Flybotix (Lausanne) — EPFL spin-off, ASIO X inspection drone (site opened).
- Microsoft Mixed Reality & AI Lab Zurich (Pollefeys) — spatial AI/robot perception research (verify current status).
- OpenAI Zurich office (opened 2024-25) and other Zurich big-tech AI sites (Apple, Meta Reality Labs) — Mentor/Speaker potential (verify).
- World Robot Olympiad Switzerland — national student robotics competition, 2026 season (site opened).
- Eurobot Switzerland national qualifier — verify (eurobot.ch did not respond); visibility channel for a student lab.
- SINDEX (Bern) — main Swiss industrial-automation trade fair, next edition 31 Aug–2 Sep 2027 (site opened).
- b2venture (St. Gallen) and Ace & Company (Geneva) — active Swiss deeptech investors (sites opened).
- Venturelab / Venture Leaders Robotics (Zurich) — startup programs and Swiss robotics delegations (site opened).
- Kickstart Innovation (Zurich) — corporate-startup accelerator with robotics/smart-industry tracks (site opened).
- Fongit (Geneva) and ESA BIC Switzerland — incubators funding Geneva/space-robotics startups (sites opened).
- u-blox (Thalwil, GNSS modules) and Sensirion (Stäfa, sensors) — Components layer is thin (sites opened).
- Mikron (Biel, automation systems) and Asyril (Villaz-St-Pierre, flexible part feeders, 403 to curl) — Industrial suppliers (verify Asyril via CDP).
- Zühlke (Schlieren) — engineering/innovation services firm with robotics/embedded projects; potential sponsor (site opened).
- Hacker houses: none found for Zurich in the file or in a news search; researcher should confirm explicitly that none exist or add any (scope asks for them).

## Low
- EPFL Rocket Team and Swiss Solar Boat (EPFL) — student engineering teams with autonomy/embedded work (sites opened).
- Hackuarium (Renens, community biohacking lab) and Impact Hub Zurich — community spaces (sites opened).
- ETH Robotics Summer School — verify (site did not respond).
- HES-SO Valais-Wallis (HEVS) and HE-Arc (Neuchâtel) — applied-science schools with automation/robotics programs (sites opened).
- University of Geneva (as School) and University of Basel (as School) — only individual labs listed (sites opened).
- Leica Geosystems (Heerbrugg, Hexagon) — reality capture/LiDAR; Hexagon Robotics already covered, so low.
- Stadler Rail and Bystronic — Swiss industrial demand side (sites opened).
- Roche / Novartis lab-automation (Basel) — demand side for lab robotics, Basel is under-covered (verify).
- armasuisse W+T (Thun) — Defense demand; partly covered by the SDRC row.
- Nomoko and Picterra — Swiss geospatial/3D AI startups adjacent to robotics (sites opened).
- Polytech Ventures (Lausanne) — verify (site did not respond).
- Maker Faire Zürich — site shows editions only up to 2018; skip unless a current edition is found.
