# Verification — Europe Platforms

Verified on 2026-11-13 against `devin/playbooks/verifier.md`, `CLAUDE.md` and `schemas/notion-schema.md`. No Notion reads or writes.

## Result

| Dataset | Input | Verified | Corrected | Rejected | Retained |
|---|---:|---:|---:|---:|---:|
| Ecosystem Map organizations | 20 | 0 | 20 | 0 | 20 |
| Robots & Models | 22 | 13 | 9 | 0 | 22 |
| **Total** | **42** | **13** | **29** | **0** | **42** |

"Verified" = no change beyond the Status reset. Every organization counts as corrected because `_relationship_reason` is not a Notion property and was removed. All retained rows have Status `To verify`. No `Used in projects` key is emitted.

## Method
- All 62 distinct URLs in Sources/Website were requested with curl; 16 that were blocked (403/401) or thin JS pages were re-opened in Chrome via CDP. Unreadable even via CDP: Reuters (RobCo) and Forbes (Hexagon/Schaeffler); both were replaced by readable sources stating the same facts.
- 10 extra sources were found (Google News RSS -> CDP) and opened to support or fix claims. Final Sources set: 68 distinct URLs, all opened.
- Each claim in `What they build`, `Key specs`, `Price / access` and `Why it matters` was checked by searching the opened page text.
- All select / multi-select values checked against the schema; all `Built by` / `Used by` names resolve to organizations in this file.

## Organizations

| Organization | Verdict | Reason |
|---|---|---|
| NEURA Robotics | corrected (format only) | $1.4B Series C, investors, ~$7B Bloomberg valuation, CNBC milestone caveat, 4NE1 Gen 4, Neuron AI, RoboGym confirmed. |
| Agile Robots | corrected | Thor, Agile Hand, AMRs confirmed on the products page (source added); "production cells" was unsupported and removed. $500M / $8.5B / ~$2B total confirmed. |
| Franka Robotics | corrected (format only) | Founded 2016, part of Agile since 2023, FR3 torque sensors, 1 kHz, Duo, GELLO confirmed on franka.de. |
| Universal Robots | corrected (format only) | Gen 7 (IMTS Sept 2026), CB7, PolyScope X, 100,000+ deployments, Teradyne, 35 kg (homepage), AI Trainer with Scale AI confirmed. |
| KUKA | corrected | 1898, €3.9B sales, 14,500 staff, Midea (fDi), Nvidia Automation 2.0 confirmed; 2D/3D AI vision system (Oct 2026) was unsourced, so a metrology.news source was added. |
| ABB Robotics | corrected (format only) | SoftBank $5.375B deal, China block, 7,000+ employees confirmed. |
| ANYbotics | corrected | ETH 2016, $110M Series B, ANYmal X ATEX/IECEx, Equinor/DSM-Firmenich, Barcelona office confirmed; removed the unread EU-Startups €127M claim. |
| RobCo | corrected | Reuters returned 401, so it was replaced by SiliconANGLE + AI Insider. Fixed: CEO moved to San Francisco (Austin is a manufacturing site), and Alfie launches March 2027. Rewrote the funding text to what the sources state. |
| PAL Robotics | corrected | 2004, Toulouse/Bari offices, 30+ countries, TIAGo Pro, Kangaroo, TALOS, SEA arm confirmed. Size / stage "Series A-B" had no source -> empty. |
| Hexagon Robotics | corrected | "Piloted at BMW Leipzig" was unsupported; changed to piloted by Pilatus and Schaeffler (mikekalil). Forbes was unreadable, so it was replaced by The Robot Report (Schaeffler 1,000 AEONs by 2032, 29 Apr 2026). AEON specs confirmed. |
| Engineered Arts | corrected | City Falmouth confirmed via contact page (added). "Custom lookalike robots" was unsupported and removed. Size / stage "unknown" -> empty (invalid select). |
| Shadow Robot Company | corrected | Removed the unsupported "Member of euRobotics" claim. Softened "DEX-EE co-developed with Google DeepMind", because the site only shows a DeepMind testimonial. Fraunhofer IFF six-month project confirmed (The Engineer, 28 Oct 2026). Size / stage "unknown" -> empty. |
| igus | corrected | The ~$1B sales figure had no source; added The Robot Report (€1.105B). ReBeL $6,899 / 8 kg, hand $2,760, ReBeL Move and Iggy Rob €47,999 confirmed. |
| Comau | corrected (format only) | One Equity Partners majority, Stellantis minority, 50 years old, Turin, MyCo/MyMR/MATE/education and Nvidia Jetson/Isaac Sim confirmed. |
| Quantum Systems | corrected (format only) | Founded 2015 in Gilching by Seibel, Series C €1B (May 2025) and $1.2B Series D at $8B (Jul 2026), Ukraine use confirmed. |
| CMR Surgical | corrected | Removed "45,000+ patients" and "US launch in 2026" (not in sources), and "portable" became "compact, modular". City Cambridge not in any opened source -> "unknown". Stryker ~$400M preferred equity and exclusive option confirmed. |
| Theker | corrected (format only) | $85M Series A by CRV, Samsung, Aglaé, "Europe's largest robotics Series A", Barcelona showroom confirmed. Official site is a teaser page. |
| Generative Bionics | corrected | €70M, Pucci, IIT spin-off, GENE.01 smart skin confirmed; official gbionics.ai added to Sources. |
| IIT – iCub Tech | corrected | "40+ built for labs worldwide" was not on the opened pages and was removed. 104 cm, GPL, full-body skin, YARP, ergoCub paper (13 Jul 2026) confirmed. |
| Starship Technologies | corrected | 2014, Estonia HQ, Helsinki R&D, 10M+ deliveries, 3,000 robots and 8 countries confirmed. "Left US campuses" sourced via Retail Tech Innovation Hub (added). "Six-wheeled" was unsourced and removed. |

## Robots & Models

| Name | Verdict | Reason |
|---|---|---|
| 4NE1 Gen 4 | verified | 20% lighter, series production, Smart Limbs, upgraded hands, runs Neuron AI. |
| Neuron AI | verified | AFP: 3D vision, touch, audio, robot state, language, memory; PLA architecture. |
| MAiRA | verified | Listed on neura-robotics.com. |
| Agile ONE | verified | Pictured humanoid in the dpa/Yahoo article. |
| Diana 7 | corrected | Products page added; specs filled (torque sensors in all seven axes). |
| Franka Research 3 (FR3) | verified | Claims confirmed on franka.de. |
| UR Gen 7 (g-Series) | verified | Three g-Series arms (UR10g-1750 etc.), CB7, PolyScope X. |
| UR AI Trainer | verified | GTC 2026 with Scale AI. |
| ANYmal X | corrected | "First legged robot certified for explosive sites" was unsupported; reworded. |
| Alfie (RobCo) | corrected | Reuters replaced; specs set to two-armed mobile robot launching March 2027. |
| TIAGo Pro | verified | 2x 7-DoF, 3 kg/arm, 1 kHz EtherCAT, i5, ROS 2. |
| PAL Robotics SEA arm (ICRA 2026) | verified | 7 DoF, <10 kg, 3 kg, SEA, ROS 2/ros_control, 1 kHz. |
| AEON | corrected | Forbes swapped for The Robot Report; mikekalil (June 2025 launch) added. |
| Ameca | verified | 61 actuated movements, 27 DoF head, eye cameras, binaural mics, Tritium, rentals. |
| Shadow Dexterous Hand / DEX-EE | corrected | DeepMind wording softened (see org). |
| igus ReBeL | corrected | Release year 2022 had no source -> empty. |
| Iggy Rob | verified | €47,999, The Robot Report, May 2025. |
| Versius Plus | verified | vLimeLite, modular, Stryker exclusive US sales agent. |
| iCub | corrected | "40+ units worldwide" removed (unsourced). |
| ergoCub | verified | Nature Machine Intelligence, published 13 Jul 2026. |
| GENE.01 | corrected | Official gbionics.ai added to Sources. |
| Starship delivery robot | corrected | "Six-wheeled" removed (unsourced); fleet figures confirmed. |

## Notes
- Hexagon Robotics City stays "unknown" (the AEON page says "Swiss-engineered"; Hexagon AB is Swedish; the division HQ wasn't confirmed).
- `sources_consulted` was rebuilt from the retained row Sources + Websites (68 URLs). In the summary, "BMW" was dropped from the AEON demand line.
- None rejected: every organization exists, is active in 2026 and has an official website that loads; every robot/model exists and the builder is correct.
