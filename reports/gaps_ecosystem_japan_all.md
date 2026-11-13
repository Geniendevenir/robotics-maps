# Coverage gaps: output/ecosystem_japan_all.json

Critic run on branch `research/ecosystem-japan-all` (file after verification: 17 organizations + 20 robots/models/tools; slice depth "top 15").
References used: well-known Japanese robotics players (IFR/JARA top industrial makers, iREX exhibitor categories), Japanese national
programs and directories (JARA members, RSJ, NEDO/JST), Japanese deeptech investor lists, and leads already named in
`reports/research_ecosystem_japan_all.md` (Kawasaki, Qualcomm Japan Robotics Center, GMO, Humanoids Summit Tokyo).
No rows added; no Notion access. Items come from domain knowledge and were **not** web-checked in this pass:
the researcher must confirm each with an opened primary source ("verify" marks less certain items).
Because the slice is top-15-scale, High = players a reader would be surprised to miss even in a short Japan map.

## High
- Kawasaki Heavy Industries (Kawasaki Robotics, Kobe/Akashi) — one of Japan's "big" industrial robot makers and Japan's first robot maker; dropped only because its site timed out (retry via Chrome CDP).
- Harmonic Drive Systems (Tokyo) — strain-wave gears inside most robot arms and humanoids worldwide; Components layer is otherwise empty.
- Nabtesco (Tokyo) — RV precision reducers with dominant industrial-robot joint share; second core Components anchor.
- Denso Wave (Aichi) — major industrial robot maker; COBOTTA small cobot is one of the few Japanese arms near a student budget.
- Seiko Epson (Suwa, Nagano) — world-leading SCARA robot maker; Industrial anchor missing next to FANUC/Yaskawa.
- Omron (Kyoto) — industrial automation, mobile robots (LD/MD series) and TM cobots (via Techman stake); also sensors/controllers.
- Cyberdyne (Tsukuba) — HAL medical exoskeleton, listed company; the file has no Medical-sector anchor org despite the Sector option.
- TIER IV (Tokyo) — leader of Autoware, the open-source autonomous-driving stack on ROS 2; strongest Japanese Open-source + Mobility player.
- JST Moonshot R&D program (Goal 3: AI robots) and NEDO — main national robotics funding/research programs; no public funder or program in the file.

## Medium
- Mitsubishi Electric (Tokyo) — MELFA industrial robots and factory automation.
- Nachi-Fujikoshi (Toyama/Tokyo) — industrial robot maker (often listed among Japan's top makers).
- Keyence (Osaka) — machine vision and sensors used in robot cells; Components/sensing.
- SoftBank Robotics (Tokyo) — Pepper/Whiz service robots and robot distribution; distinct from the SoftBank Group investor row.
- GROOVE X (Tokyo) — LOVOT consumer companion robot; Consumer startup besides Sony.
- Ory Laboratory (Tokyo) — OriHime avatar robots for remote work by people with disabilities; HRI/telepresence player.
- Kawasaki Kaleido / Toyota Research Institute & Woven by Toyota (verify which is in slice) — humanoid and robot-learning R&D (TRI's Large Behavior Models / diffusion policy work is directly on the team's wedge).
- Waseda University (humanoid robotics, WABOT lineage) and Osaka University (Ishiguro lab, android/HRI) — only one university row (JSK) exists.
- University of Tokyo Matsuo Lab and AI Robot Association (AIRoA, verify) — Japanese robot foundation-model / dataset efforts; closest to the robot-learning wedge.
- RIKEN (Guardian Robot Project / R-IH) — national research institute; second Research-lab row alongside AIST.
- Robotics Society of Japan (RSJ) and its annual conference — academic association and community entry point.
- World Robot Summit (METI/NEDO) and Humanoids Summit Tokyo — events besides iREX; Humanoids Summit was already a discovery lead.
- UTEC (University of Tokyo Edge Capital) and Global Brain / Real Tech Fund — Japanese deeptech/robotics VCs; only SoftBank Group is listed as Investor.
- Qualcomm Japan Robotics Center and NVIDIA Japan — compute/hardware partner leads named in discovery notes, not resolved.
- GMO Internet Group (GMO AI & Robotics) — Humanoids Summit Tokyo sponsor and humanoid-promotion activity (verify scope).
- Robot rows: Denso COBOTTA, Epson SCARA (e.g. LS series), Kawasaki Kaleido, Cyberdyne HAL, Pepper, LOVOT, Toyota Punyo/T-HR3 — would accompany the missing orgs.

## Low
- Kondo Kagaku and Futaba (hobby servos/humanoid kits) — cheap actuators for student builds (verify current catalogue).
- Yukai Engineering (Qoobo, BOCCO) and ugo (avatar/security robots) — small consumer/service startups.
- Fuji Corp, Daihen, Yamaha Motor (robotics division) — further industrial robot makers.
- Exiii / Shiftall / Mujin-like integrators (e.g. Ascent Robotics, Linkwiz; verify) — smaller startups.
- Tokyo Tech (Institute of Science Tokyo), Tohoku University (disaster robots), Kyoto University — additional academic labs.
- RoboCup Japan Open and ROBO-ONE — competitions for visibility; ROSCon JP — ROS community event besides the users group.
- JETRO — public route for foreign partners entering Japan's ecosystem.
- ASIMO (historical Honda humanoid) robot row — context for the Honda row.
- Sony Innovation Fund / Toyota Ventures (Woven Capital) — corporate VCs with robotics deals.
