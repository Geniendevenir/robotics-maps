# Verification report: output/ecosystem_china_all.json

Rows: 47 (20 organizations, 27 robots/models). Verified 38, corrected 9, rejected 0.

Method: all 58 source URLs fetched with curl; pages that blocked curl or rendered via JS (Pandaily, SCMP, Forbes, robotera.com, fftai.com, AgileX PiPER page) opened through Chrome CDP. Key numbers, dates and product names grepped in page text. All 20 orgs are real, active in 2026, and their Website is the official domain. All Built by relations resolve to orgs in this file.

Global cleanup: removed non-Notion key `_relationship_reason` from all 20 orgs; Status set to "To verify" on all rows; select values checked against schemas/notion-schema.md (only invalid value was "unknown" in Size / stage, now empty). Release year left empty where sources give none.

Unresolved: https://www.forbes.com/sites/johnkoetsier/2026/01/09/top-10-humanoid-robot-companies-by-shipments-revealed/ returns 403 to curl and an empty body via CDP; it remains as a secondary source on UBTech only where other sources cover the claims.

| Row | Kind | Verdict | Reason |
|---|---|---|---|
| Unitree Robotics | org | verified | unitree.com pages give Go2 $1,600, R1 $4,900, G1 $13.5K; CNBC confirms STAR IPO at ~61bn yuan (~$9bn). |
| UBTech Robotics | org | corrected | Airbus cooperation deal (Jan 2026) was unsourced; confirmed and added aerospaceglobalnews.com source (Airbus bought Walker S2, early-stage trials). |
| AgiBot (Zhiyuan Robotics) | org | verified | TechNode: founded 2023, RMB 50bn round Oct 2026; Caixin: HK IPO Jul 2026; Global Times: overtook Unitree as top H1-2026 vendor. |
| Galbot | org | verified | The AI Insider: ~$362M, National AI Industry Investment Fund, Sinopec; galbot.com lists G1/S1/ET1 and AstraBrain models. |
| Fourier | org | corrected | Size / stage "unknown" -> Series C+ (TechNode: Series E ~RMB 800m Jan 2025, E3 round later in 2025); dropped Forbes source (empty body even via CDP). |
| XPeng Robotics (IRON) | org | verified | XPeng release 8 Sep 2026: IRON production line, >80% core-process automation. |
| Dobot | org | corrected | "third batch in mass delivery from Feb 2026" overstated: Pandaily (4 Feb 2026) says third batch launched, mass delivery targeted for 2026; reworded. |
| AgileX Robotics | org | corrected | City unknown -> Dongguan (head office XbotPark, Songshan Lake per global.agilex.ai); Size "unknown" (not a select option) -> empty. |
| DEEP Robotics | org | corrected | Size "unknown" is not a select option -> empty (IPO filed, not listed; no round data). Claims (2.5bn-yuan STAR IPO, Lite3/X30/M20/DR02, J80/J100 joints) confirmed. |
| Galaxea AI (Galaxea Dynamics) | org | verified | Caixin: 1bn-yuan Series B, 10bn valuation; site: R1 from $39,999, A1Z from $2,999, G0.5 (Jun 2026). |
| RobotEra | org | verified | Caixin: Tsinghua spinout, ~500m-yuan Series A, STAR1; robotera.com (via CDP) lists L7, XHAND. |
| Leju Robotics | org | corrected | Removed "4th in 2025 shipments (Omdia, ~500 units)": only source was a Forbes page that never rendered; added 2.6bn-yuan ChiNext target (BigGo); Size "unknown" -> empty. |
| Beijing Innovation Center of Humanoid Robotics (X-Humanoid) | org | corrected | Size "unknown" -> empty (company limited, state-backed; no stage data). TianGong 3.0 H2-2026 delivery and RoboMIND numbers confirmed. |
| BAAI (Beijing Academy of Artificial Intelligence) | org | verified | GitHub/HF: RoboBrain 2.0-7B (Jun 2025), RoboBrain 2.5, FlagScale; SCMP (via CDP) confirms non-profit and open-source models. |
| Shanghai AI Laboratory | org | verified | InternVLA-M1 repo shows MIT license; GRUtopia repo renamed InternUtopia (Jul 2025). |
| Geek+ | org | verified | KrASIA article (14 Jul 2025) on Hong Kong listing; geekplus.com official. |
| Estun Automation | org | verified | 36Kr: "first share of industrial robots", 7 Sep 2026 acquisition of Estun Kuozhuo; estun.com redirects (official domain). |
| World Robot Conference (WRC) | org | verified | Guardian: 19-23 Aug 2026, 3,000+ products; official site loads. |
| World Artificial Intelligence Conference (WAIC) | org | verified | Jiemian: 17-20 Jul 2026, 1,100+ companies, 3,000+ products. |
| Tsinghua University (robotics & embodied AI) | org | verified | Tsinghua news: Youth2Real won two ICRA 2026 manipulation tracks; Caixin: RobotEra spinout. |
| Unitree Go2 | robot/model | verified | unitree.com/go2: $1,600 / $2,800 / $4,500 trims. |
| Unitree R1 | robot/model | verified | unitree.com/R1: AIR $4,900, R1 $5,900, 1230 mm, 27-29 kg, 20-26 DoF. |
| Unitree G1 | robot/model | verified | unitree.com/g1: from $13.5K, 23-43 joint motors. |
| UBTech Walker S2 | robot/model | verified | Official product page + Antara (mass production Nov 2025, >800m yuan orders). |
| AgiBot World (dataset) | robot/model | verified | OpenDriveLab/AgiBot-World repo (Colosseo platform). |
| GO-1 (Genie Operator-1) | robot/model | verified | Same repo: GO-1 and GO-1 Air (no latent planner) checkpoints. |
| AgiBot X1 | robot/model | verified | AgibotTech/agibot_x1_infer: modular humanoid developed and open-sourced by AgiBot. |
| Galbot G1 | robot/model | verified | galbot.com lists G1; The AI Insider describes wheeled humanoids. |
| Fourier Max (Meta humanoid) | robot/model | verified | TechNode: 1.5 m, 48 kg, built in ~3 months with Meta. |
| XPeng IRON | robot/model | verified | XPeng release Sep 2026. |
| Dobot ATOM | robot/model | corrected | Price "unknown (~199,000 yuan, to verify)" -> "unknown" (price not in any source); key specs reworded as for Dobot. |
| Dobot Magician E6 | robot/model | verified | dobot-robots.com: "Desktop Cobot for Education & Research". |
| AgileX PiPER | robot/model | verified | Product page (via CDP) + TechEBlog: 4.2 kg, 1.5 kg payload, 626 mm, ±0.1 mm, $2,499. |
| AgileX Cobot Magic (Mobile ALOHA kit) | robot/model | corrected | Source was the PiPER product page; replaced with global.agilex.ai, whose product menu lists COBOT MAGIC / Modular ALOHA. |
| DEEP Robotics Jueying Lite3 | robot/model | verified | Listed on deeprobotics.cn/en. |
| DEEP Robotics Jueying X30 | robot/model | verified | Listed on deeprobotics.cn/en ("built for industry"). |
| Galaxea R1 | robot/model | verified | galaxea-dynamics.com: R1 series from $39,999. |
| Galaxea LEMO A1Z | robot/model | verified | Site: A1Z from $2,999; A1Z-T teleop arm and G1Z gripper sold separately. |
| Galaxea G0 / G0.5 | robot/model | verified | OpenGalaxea/GalaxeaVLA repo (G0.5 code + license); site post Jun 2026. |
| RobotEra STAR1 | robot/model | verified | Caixin lists STAR1. |
| Leju KUAVO | robot/model | verified | lejurobot.com: KUAVO 4Pro, KUAVO 5 / 5-W research platforms. |
| TianGong 3.0 | robot/model | verified | Gasgoo: mass delivery H2 2026. |
| RoboMIND (dataset) | robot/model | verified | Global Times: 300k+ trajectories, 700+ tasks, 20m downloads. |
| RoboBrain 2.0 | robot/model | verified | GitHub + HF (created 2025-06-05). |
| InternVLA-M1 | robot/model | verified | GitHub repo, MIT license. |
| InternUtopia (ex-GRUtopia) | robot/model | verified | GitHub repo (renamed Jul 2025). |
| Geek+ warehouse AMRs | robot/model | verified | geekplus.com. |
