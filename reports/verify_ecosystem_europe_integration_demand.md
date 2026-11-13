# Verification — Europe Integration + Demand

Verified on 2026-11-13 against `devin/playbooks/verifier.md`, `CLAUDE.md` and `schemas/notion-schema.md`. No Notion reads or writes were made.

## Result

| Dataset | Input | Verified | Corrected | Rejected | Retained |
|---|---:|---:|---:|---:|---:|
| Ecosystem Map organizations | 20 | 0 | 20 | 0 | 20 |
| Robots & Models | 16 | 9 | 7 | 0 | 16 |
| **Total** | **36** | **9** | **27** | **0** | **36** |

"Verified" = no change beyond the Status reset (and dropping a `null` Release year key). "Corrected" includes evidence repairs, removal of unsupported claims and schema cleanup. Every organization counts as corrected because the non-schema key `_relationship_reason` was removed. All retained rows have Status `To verify`.

## Method

- All 72 distinct URLs in the input (row Sources, Websites, sources_consulted) were requested with curl; 19 that failed or were bot-blocked (BMW, Mercedes, DHL, Schaeffler, Vanderlande, The Engineer, technische-logistik, autonews, 01net, manufacturingtodayindia, logisticsmiddleeast, drivesncontrols) were re-opened through Chrome and read.
- Still unreadable: the 3 Reuters articles (401 paywall even in Chrome) and one Forbes article. Each Reuters citation was replaced with two readable articles carrying the same story; the Forbes URL (consulted list only) was dropped.
- Key claims were checked by searching the page text for the specific numbers and names (e.g. 60 tote moves/hour, 450 picks/hour, 8,000 robots, up to 50 Nomagic robots, 82 % Trend Index, 1,000 AEON by 2032).
- Select values were checked against the schema; every `Built by` / `Used by` relation resolves to an organization in this file.
- `sources_consulted` was rebuilt as the deduplicated union of the original list (fixed) and all row sources (61 URLs).

## Limits

- Relationship-potential tags are outreach guesses, not confirmed offers. Warm contact paths are all `unknown`.
- Pilot numbers and rollout targets (Schaeffler 1,000 AEON by 2032, up to 2,000 Humanoid robots, Zalando up to 50 robots) are company plans, not completed deployments.
- The Mercedes/Apptronik source is dated March 2025; there is no 2026 confirmation that the pilot is still running.
- `Size / stage` was removed (left empty) for Innov8 Group and automatica because the input had `null` and no schema option is supported by the sources.

## Organization verdicts

| Organization | Verdict | One-line reason |
|---|---|---|
| BMW Group | corrected | Removed `_relationship_reason`; BMW Leipzig release (Sep 2026), AMS and Figure pages support AEON pilot, Figure 02/03 and competence centre. |
| Mercedes-Benz Group | corrected | Removed `_relationship_reason`; Drives & Controls (2025) supports Apollo at Marienfelde, teleop/AR training and Apptronik investment. |
| Schaeffler | corrected | Removed `_relationship_reason`; Reuters (paywalled) replaced by TimesLIVE + AI Business for the 2,000-robot deal and actuator supply; The Engineer supports 1,000 AEON by 2032. |
| Zalando | corrected | Removed `_relationship_reason`; Zalando release (19 Mar 2026) and Sourcing Journal support Nomagic, Sereact/Ceva sites and the Series B stake. |
| DHL Group | corrected | Removed `_relationship_reason`; Fortune (8,000 robots, 2017) and DHL page (SVT SOFTBOT) support claims. |
| Ocado Group | corrected | Removed `_relationship_reason`; Reuters replaced by Independent + Grocery Gazette; "fast-growing" wording replaced by sourced fact (go-live FY2028). |
| Siemens | corrected | Removed `_relationship_reason`; DC Velocity confirms Erlangen HMND 01 metrics. |
| Airbus | corrected | Removed `_relationship_reason`; Reuters replaced by SCMP + Aerospace Global News (Airbus purchased Walker S2); Airbus page supports Airbus Robotics (2023), CabinMarker 4 kg, FlexTrack, exoskeletons. City Leiden is the registered seat. |
| Comau | corrected | Removed `_relationship_reason`; removed unsupported "with Automha"; autonews supports post-Stellantis expansion into battery and warehouse logistics; TechTimes supports NVIDIA deal. |
| KNAPP | corrected | Removed `_relationship_reason`; KNAPP site (Hart bei Graz, Boston hub) and Edeka article (~450 picks/h) support claims. |
| SSI Schäfer | corrected | Removed `_relationship_reason`; technische-logistik confirms SSI Piece Picking at Würth (April 2026); materialfluss awards article loads. |
| TGW Logistics | corrected | Removed `_relationship_reason`; "Cultura" customer not found in any source and dropped; Dinosol/Kärcher found on official site. |
| Swisslog | corrected | Removed `_relationship_reason`; reworded hospital logistics as healthcare automation (site shows healthcare references); KUKA, AutoStore, ItemPiQ, Nowaste supported. |
| Vanderlande | corrected | Removed `_relationship_reason`; official site (airports/baggage) and MHD (Toyota Automated Logistics from 1 Apr 2026) support claims. |
| Dürr | corrected | Removed `_relationship_reason`; 20,000th robot to Ford Valencia and EcoRP4 supported. |
| Körber | corrected | Removed `_relationship_reason`; tech.eu (Oct 2026) supports NAiSE stake and vendor-agnostic FMS. |
| Motion | corrected | Removed `_relationship_reason`; removed invalid Website `unknown` (no official site found); tech.eu and Tech Funding News support founding 2026, $2M pre-seed (Extantia), five paid Belgian pilots, HaaS scope. |
| Innov8 Group | corrected | Removed `_relationship_reason` and null Size / stage; Logistics Manager confirms Unitree master distributor + Novares pilot; innov8.fr confirms Courbevoie HQ. |
| Fraunhofer IPA | corrected | Removed `_relationship_reason`; Robot Report (May 2026) supports six-criteria humanoid benchmark with G1; IPA site shows ROS2-Industrial training and euROBIN. |
| automatica | corrected | Removed `_relationship_reason` and null Size / stage; official site supports munich_i/MIRMI/Robothon and "largest portfolio"; 01net (Business Wire) supports 82 % Trend Index figure. |

## Robots & Models verdicts

| Name | Verdict | One-line reason |
|---|---|---|
| AEON (Hexagon Robotics) | verified | BMW release (wheeled legs, battery/component production) and The Engineer support row. |
| Figure 03 | corrected | Release year 2026 -> 2025 (Figure introduced F.03 on 9 Oct 2025); added that source. BMW Hall 52 / 30,000 cars supported. |
| Apollo (Apptronik) | verified | Drives & Controls supports use and teleop/AR training. |
| HMND 01 | corrected | Reuters replaced by TimesLIVE + AI Business; Siemens metrics confirmed by DC Velocity. |
| Walker S2 | corrected | Removed unverifiable "10,000+ capacity in 2026" (only in paywalled Reuters); purchase by Airbus sourced from SCMP / Aerospace Global News. |
| Unitree humanoids (Innov8 / Novares pilot) | verified | Logistics Manager and Robot Report (G1 in IPA benchmark) support row. |
| Ocado bot | verified | Two Ocado newsroom pages support 17,000+ bots and evolution. |
| KNAPP Pick-it-Easy Robot | verified | Edeka article supports 450 picks/h, barcode scan, weighing, 24/7. |
| SSI Piece Picking | verified | technische-logistik supports Würth integration, April 2026. |
| TGW RovoFlex | verified | Robot Report (13 Feb 2024) supports camera, PickCenter, manual/auto switching, 2024. |
| Swisslog ItemPiQ | corrected | Specs supported, but source is a 2019 launch article; flagged in Key specs. |
| Dürr EcoRP4 | corrected | "20,034 robots sold" not in any source; replaced with the sourced 20,000th-robot milestone. |
| Airbus CabinMarker | corrected | Release year 2026 not supported (June 2026 article does not give a release date); removed. 4 kg / Airbus Robotics supported. |
| NAiSE Fleet Management Software | verified | tech.eu supports vendor-agnostic AGV/AMR + manual trucks and WMS/WES/WCS agnosticism. |
| SVT Robotics SOFTBOT Platform | verified | DHL page supports standardized connectors. |
| NVIDIA Isaac Sim (in Comau controllers) | corrected | Open source false -> true: github.com/isaac-sim/IsaacSim is Apache 2.0 (some Omniverse dependencies under NVIDIA terms); added source. |

## Summary edits

Summary point 4 now names Humanoid's HMND 01 (UK) alongside Hexagon AEON as the European humanoids, since both appear in the data.
