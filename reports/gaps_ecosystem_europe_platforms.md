# Coverage gaps — Europe Platforms

Reviewed 2026-11-13 following `devin/playbooks/coverage-critic.md`, `CLAUDE.md`, `schemas/notion-schema.md` and `reports/verify_ecosystem_europe_platforms.md`. No rows were added or edited, and Notion was not accessed.

**Result: 6 High / 10 Medium / 8 Low gaps (24 total).** The cleaned file has 20 organizations and 22 robots/models. Every name below was checked against all three ecosystem outputs (`ecosystem_europe_platforms`, `ecosystem_paris_all`, `ecosystem_europe_software_ai`) and is absent from all of them. Gaps already raised in `gaps_ecosystem_europe_software_ai.md` (Helsing, Oxa, BlueBotics, The Robot Learning Company) are not repeated here.

## Canonical references used
- [R1] Dealroom, "Robotics startups in Europe", top 50 by funding (updated 2026-10-31): https://dealroom.co/lists/robotics-startups-europe/ (opened via Chrome CDP)
- [R2] ERF 2026 sponsors & exhibitors: https://erf2026.eu/sponsors-exhibitors/ (opened via CDP)
- [R3] Players that people in the field would expect (industrial arms, AMRs, warehouse robots, research platforms). Official sites were opened for each name marked "site opened".

## What the file covers well
Large German players (NEURA, Agile/Franka, KUKA, RobCo, Quantum Systems), the major cobot makers (UR, Comau, igus), humanoids (AEON, Ameca, GENE.01, Theker) and research reference platforms (FR3, TIAGo Pro, Shadow Hand, iCub). Main structural holes: **no warehouse/logistics robot maker other than Starship**, **no AMR maker**, **no Agri platform** (the schema's `Agri` sector is unused), **no French platform maker outside Paris**, **no low-cost education arm besides igus**, only **one surgical company** and only **one defense company**.

## High — 6
- **H1 — Exotec (Croix/Lille, FR):** Dealroom #9, unicorn, $445M raised [R1]. Builds the Skypod warehouse robot system; founded 2015 in Lille, 400+ employees (exotec.com/company, opened). France's best-known platform unicorn and the obvious missing logistics-robot maker; not in the Paris file because it is based near Lille.
- **H2 — Niryo (FR):** French maker of the Ned education robot-arm platform (plus Nate for industry and Pulsar for healthcare; niryo.com, opened; €10M raise reported by Retail Technology Innovation Hub). It is the obvious European low-cost arm for schools, which matters directly for the lab's low-cost robot-learning hypothesis. The research report says igus ReBeL is "the only budget-compatible European arm found", and Niryo shows that claim is incomplete. Prices are not verified.
- **H3 — Stäubli Robotics (CH):** Long-established European industrial-arm maker: 6-axis, SCARA, mobile robots and medical arms such as the TX2-60L MedX Ready (staubli.com/robotics, opened via CDP). A top-20 European platforms list without Stäubli leaves a hole every industry reader will notice.
- **H4 — Mobile Industrial Robots (MiR, DK):** One of the best-known AMR makers ("leading manufacturer of autonomous mobile robots", mobile-industrial-robots.com, site opened). AMRs, the most widely deployed mobile platform class, are missing from the file. Its link to Teradyne/UR is not verified.
- **H5 — AutoStore (NO):** Cube-storage warehouse robots (robots, grid, ports, CarouselAI picking) with an investor-relations site (autostoresystem.com, opened). One of Europe's largest warehouse-robot platforms and a strong Logistics row.
- **H6 — DLR Institute of Robotics and Mechatronics (DE):** Europe's flagship robotics research institute: it builds platforms such as the TORO torque-controlled humanoid (1.74 m, 76 kg, 39 DoF; dlr.de/en/rm, opened). It is a research-platform peer of IIT iCub. The researcher flagged it but dropped it.

## Medium — 10
- **M1 — Distalmotion (Epalinges, CH):** Dealroom #10, $390M [R1], DEXTER surgical robot (distalmotion.com, opened). A second surgical platform alongside CMR.
- **M2 — MMI – Medical Microinstruments (Pisa, IT):** Dealroom #12, $332M [R1]; robotic microsurgery platform (mmimicro.com, opened).
- **M3 — Ecorobotix (Yverdon-les-Bains, CH):** Dealroom #20, $189M [R1]; ARA AI spot sprayers (ecorobotix.com, opened). The best candidate to fill the empty `Agri` sector.
- **M4 — TEKEVER (Lisbon, PT):** Dealroom #6, unicorn, $678M [R1]; AR3/AR5 autonomous UAS (tekever.com, opened). The largest platform maker missing after Exotec. It ranks only Medium because it is defense, which is less relevant to the lab.
- **M5 — Dexory (Wallingford, UK):** Dealroom #19, $194M [R1]; autonomous warehouse-scanning robots (dexory.com, opened).
- **M6 — Robotnik (Valencia, ES):** Mobile robots and mobile manipulators since 2002, including an R&D platform line (robotnik.eu, opened). A research-friendly ROS platform supplier, similar in role to PAL.
- **M7 — Milrem Robotics (Tallinn, EE):** THeMIS unmanned ground vehicles and EU iMUGS projects (milremrobotics.com, opened). The researcher dropped it "for space".
- **M8 — 1X (ex-Halodi Robotics, Norwegian origin):** NEO home humanoid. Founded in Norway in 2014, but its about page now says it is "based in San Carlos, CA" (1x.tech/about, opened). Include only if Norwegian operations qualify, otherwise leave it to the US slice.
- **M9 — Stark (Berlin, DE):** Dealroom #7, unicorn, $627M [R1]; unmanned defense systems. Site not opened.
- **M10 — Bitcraze (SE):** ERF 2026 exhibitor [R2]; maker of the open-source Crazyflie nano-drone. Cheap, open research platform that fits the lab's budget. Site not opened, so details need verification.

## Low — 8
- **L1 — RIVR (ex-Swiss-Mile, Zurich, CH):** Wheeled-legged delivery robots. Acquired by Amazon (swissinfo, CNBC via Google News RSS headlines), so it may no longer count as an independent European player.
- **L2 — Husarion (PL):** ERF 2026 silver sponsor [R2]; low-cost ROS 2 mobile robots. Site not opened.
- **L3 — fruitcore robotics (DE):** HORST industrial robot and PLEXA One industrial humanoid (fruitcore-robotics.com, opened).
- **L4 — Gravis Robotics (Zurich, CH):** Dealroom #16, unicorn, $223M [R1]; autonomy retrofit for excavators (gravisrobotics.com, opened). Partly software.
- **L5 — Lely (NL):** Dairy robots such as milking and feeding systems (lely.com, opened); a large Agri deployment base.
- **L6 — Automata (London, UK):** Dealroom #28, $134M [R1]; lab-automation robots.
- **L7 — Aerones (Riga, LV):** Dealroom #31, $122M [R1]; wind-turbine maintenance robots.
- **L8 — eCential Robotics (Gières, FR):** Dealroom #29, $126M [R1]; surgical imaging and navigation platform.

## Recommendation
Re-run the researcher on **H1–H6 only**, then verify. The slice is "top 20", so re-rank rather than append. Weaker candidates to swap out are slots that duplicate an already-covered parent or theme, for example Franka (owned by Agile Robots) or the second social/humanoid entries. That decision belongs to the researcher. Consider M3 (Ecorobotix) so that at least one Agri platform is listed. Also update the research report's claim that igus is the only budget European arm (see H2). Funding numbers come from a Dealroom snapshot and are discovery signals, not verified facts. Hiring was not researched.
