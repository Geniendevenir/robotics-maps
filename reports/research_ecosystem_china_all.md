# Research notes: ecosystem slice China / all / top 20

- Output: `output/ecosystem_china_all.json` (20 organizations, 27 robots/models, 51 distinct sources consulted, all opened via curl or Chrome CDP).
- Notion was not read or written. `Used in projects` is not output. `Knowledge nodes` left empty (to be linked later).
- No overlap with `ecosystem_paris_all.json` / `ecosystem_europe_software_ai.json` (those contain no China-region organizations).
- Selection ("top 20"): by 2026 humanoid shipments (Omdia via Forbes; Global Times H1-2026 data), 2026 funding/IPO news (Caixin, TechNode, Crunchbase, Forbes VC ranking), relevance to our low-cost robot-learning wedge (AgileX, Galaxea, open models), plus one school and two events for Type coverage. No investor row: Chinese embodied-AI investors are mostly state funds/carmakers with no realistic link to a Paris student lab.
- `Size / stage` = "unknown" (not a valid select option; syncer should leave empty) for Fourier, AgileX, DEEP Robotics, Leju, X-Humanoid. AgileX HQ city unknown (not confirmed on an opened page).
- `Status`: all Draft; `To verify` for UBTech (Airbus deal only seen in a news headline) and Dobot ATOM (price only seen in headlines).
- Release year left null when not stated on an opened page.

## Saturation
Not reached, by design of the "top 20" depth: discovery queries keep surfacing new names (ACE Robotics, Kunlunxing, Paxini, Psibot, Matrix Robotics, Noetix, Engine AI, Mifeng, Stardust/Astribot, Xiaomi, Inovance, Siasun, Hikrobot). These are the first candidates if the slice is expanded.

## Method notes
- Google News RSS via curl for discovery; article links resolved through Chrome CDP (Reuters renders empty). Official sites (unitree.com, agilex.ai, galaxea-dynamics.com, dobot-robots.com, deeprobotics.cn, geekplus.com) are readable with plain curl.

## 5-line summary
1. China leads humanoid volume (>97% of H1-2026 shipments); AgiBot, Unitree, UBTech lead; Galbot, Galaxea, Fourier are the best-funded challengers.
2. Money: record embodied-AI funding and a 2026 IPO wave (Unitree ~$9bn; AgiBot, DEEP Robotics, Leju filing), with state funds and carmakers (XPeng) as backers.
3. Demand: factories (UBTech Walker S2, Dobot ATOM), logistics (Geek+), research/education platforms; state labs (BAAI, Shanghai AI Lab, X-Humanoid) open-source models and datasets.
4. For our wedge: cheapest hardware is Chinese (Go2 $1.6k, R1 $4.9k, PiPER ~$2.5k, LEMO $3k) and open VLAs/datasets (GO-1, G0, InternVLA-M1, RoboBrain, AgiBot World, RoboMIND) are free.
5. Best entry point: open-source engagement + hardware purchase (benchmark GO-1/G0 on PiPER/LEMO in LeRobot), then ask AgileX/Galaxea/Dobot for edu discounts.
