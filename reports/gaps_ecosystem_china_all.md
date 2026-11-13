# Coverage gaps: output/ecosystem_china_all.json

Critic run on branch `research/ecosystem-china-all` (file after verification: 20 organizations + 27 robots/models; slice China / all / top 20).
References used: well-known Chinese robotics players (humanoid, cobot, drone, logistics, consumer, components), China robotics
industry rankings and listed-company lists, WRC/WAIC exhibitor categories, major Chinese universities/institutes, CRIA (China Robot
Industry Alliance), national student competitions. No rows added; no Notion access.
Items are from domain knowledge and were **not** web-checked in this pass: the researcher must confirm each with a primary
source (items marked "verify" are less certain). Because the slice is capped at top 20, High items are candidates to swap in
for weaker rows, not only additions.

Overall: humanoid startups are well covered; the file misses the biggest Chinese robotics company (DJI), the whole Components
and compute layer, cobot makers other than Dobot, consumer/service robots, investors, and the student competitions most useful to 42AI.

## High
- DJI (Shenzhen) — world's largest drone maker (also Livox lidar, RoboMaster EP education robot); most obvious Chinese robotics player, absent; Drone sector is empty.
- RoboMaster (DJI university competition) — China's flagship student robotics competition (with an international track); prime visibility/benchmark channel for a student lab.
- Booster Robotics (Beijing) — low-cost T1/K1 research humanoids used in RoboCup humanoid league; fits the low-cost robot-learning wedge.
- LimX Dynamics (Shenzhen) — TRON 1 biped/wheel-legged research platform and humanoid; major RL-locomotion player missing.
- ByteDance Seed (robotics team) — GR-2/GR-3 VLA models; one of the most-cited Chinese VLA producers, no row (verify current naming).
- Horizon Robotics / D-Robotics (Beijing) — RDK X3/X5 robot dev boards (ROS 2 ready, low-cost edge AI compute); Components/compute layer gap.
- Orbbec (Shenzhen) — depth cameras (Astra/Femto/Gemini) widely used in research and low-cost robots; Components layer is almost empty.
- Cobot makers JAKA, AUBO, Elite Robots, Rokae (verify which is #1) — China leads global cobot shipments; only Dobot is listed.
- Investors (Type "Investor" absent): HongShan (ex-Sequoia China), Hillhouse, Matrix Partners China, Beijing Robotics Industry Development Investment Fund (verify) — the file has zero investors.

## Medium
- Unitree H1 / H2 and UnifoLM / unitree_rl_gym (open-source RL + world-model code) — robot/model rows; Unitree's open stack is central to low-cost sim-to-real.
- Xiaomi Robotics (CyberDog, CyberOne) — consumer quadruped/humanoid from a big-tech player.
- Huawei (Pangu embodied models, Ascend compute) and Tencent Robotics X — big-tech labs absent; only XPeng represents big corporates.
- Alibaba DAMO Academy (RynnVLA/RynnEC embodied models, verify) — another big-tech embodied-AI producer.
- X Square Robot (WALL-OSS open VLA, verify) and Spirit AI (verify) — embodied-AI model startups beyond AgiBot/Galbot.
- Astribot (Stardust Intelligence, S1) and Engine AI (PM01/SE01) — prominent humanoid startups not listed.
- Noetix Robotics (Bumi low-cost consumer humanoid, verify price) — sub-$2k humanoid directly relevant to the low-cost wedge.
- Pudu Robotics and Keenon Robotics — world-leading service/delivery robots; Consumer/service sector gap.
- Ecovacs, Roborock, Dreame — consumer cleaning robots (largest robot volume category); Roborock showed a robot-arm vacuum.
- Hai Robotics and Quicktron — logistics ACR/AMR makers; only Geek+ covers logistics.
- Siasun (Shenyang) and Inovance — large industrial robot makers; only Estun covers industrial OEMs.
- MicroPort MedBot (Toumai surgical robot) — Medical sector has only Fourier rehab.
- Mech-Mind (3D vision + AI for picking) — Software & AI for industrial manipulation.
- Hesai and RoboSense — lidar components (RoboSense also sells robotics vision modules).
- Leaderdrive (harmonic reducers) and Inspire Robots (dexterous hands, used on many humanoids) — key actuator/hand suppliers.
- Shanghai Jiao Tong University, Zhejiang University, Peking University, Harbin Institute of Technology — major robotics schools; only Tsinghua listed.
- Shenyang Institute of Automation (CAS) — national robotics research institute.
- World Humanoid Robot Games (Beijing, Aug 2025) and Beijing humanoid robot half-marathon (Apr 2025) — widely covered events.
- IROS 2025 Hangzhou — major international robotics conference held in China.
- CRIA (China Robot Industry Alliance) — national industry association, source of official statistics.

## Low
- CIIF Robotics Show (Shanghai) and CIROS (Shanghai) — industrial robotics trade shows.
- Shenzhen/Beijing municipal embodied-AI funds and Beijing E-Town robot programs — public funding (verify names).
- Kepler, MagicLab, Dataa Robotics (CloudMinds) — additional humanoid players (verify activity).
- GuYueHome (古月居) and ROS China community — main Chinese ROS learning community; Open-source community type absent.
- Discoverse / RoboTwin / other Chinese sim and benchmark projects (verify origin) — Simulator/Tool rows are thin (only InternUtopia).
- Peking University BIGAI (Beijing Institute for General AI) — embodied-AI research institute.
- HKUST / HKU robotics (Hong Kong) — strong labs; check whether Hong Kong is in the China slice.
- Huawei Developer / Ascend education programs and Unitree/AgileX education distributors in Europe — warm-contact paths for a Paris lab.
