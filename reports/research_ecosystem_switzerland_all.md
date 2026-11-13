# Research: Switzerland / all layers / exhaustive-depth discovery

## Scope and method

Deliverable: `output/ecosystem_switzerland_all.json`, **124 organizations**, **50 robots/models/tools**, **242 distinct consulted URLs**, and **188 distinct row-cited URLs**. Every organization is Region **Europe** and every row remains **To verify**. Switzerland includes Zurich/canton, Dübendorf, Zug, the EPFL/Lausanne corridor, Geneva, Basel, Bern, Ticino, central/eastern Switzerland and national networks.

Originally merged three work slices: Zurich (50 organizations / 22 robots/tools), rest plus Zurich top-ups (49 / 22), final gaps (22 / 5). The intermediate gap file is preserved in commit `94bb85b`; all three work files are removed from the final tree. A final bounded discovery pass added three startups (Jaipur Robotics, MESH and MIKAJAKI) and the EyeLib platform directly to the output, without restoring work/. The requested slice metadata says depth `exhaustive`; this describes research intent, **not evidence of a complete census**.

Read CLAUDE.md, the ecosystem playbook, schema, Paris row format and US report. Discovery used search, official institution/company/community pages, product documentation and financing announcements. Existing `output/*.json` and both earlier work files were compared before gap row selection, then names and relations were audited again in the merged output. Existing global rows are not recreated: e.g. ABB Robotics, ANYbotics, maxon, Bota Systems and Stäubli remain in their original files. This slice therefore is not a standalone total of every Swiss robotics actor.

Every new row has an opened HTTP(S) citation. Descriptions and contact paths distinguish announced products, historical events, company claims and realistic cold outreach. No sponsorship, warm introduction, hardware donation or formal collaboration has been secured. No Notion access/sync, hiring research, verifier pass or coverage-critic pass is claimed.

## Counts by Type

| Type | Organizations |
|---|---:|
| Research lab | 34 |
| Startup | 30 |
| Association | 20 |
| Corporate | 16 |
| Event | 9 |
| Investor | 8 |
| School | 5 |
| Open-source community | 2 |

## Counts by city

| City | Organizations |
|---|---:|
| Zurich | 47 |
| Lausanne | 13 |
| Renens | 6 |
| Winterthur | 4 |
| Basel | 3 |
| Dübendorf | 3 |
| Opfikon (Glattbrugg) | 3 |
| Bern | 2 |
| Carouge | 2 |
| Épalinges | 2 |
| Neuchâtel | 2 |
| Schlieren | 2 |
| St. Gallen | 2 |
| Yverdon-les-Bains | 2 |
| Allschwil | 1 |
| Bäretswil | 1 |
| Biel/Bienne | 1 |
| Birr | 1 |
| Bonaduz | 1 |
| Croglio | 1 |
| Dübendorf / Visp | 1 |
| Ebikon | 1 |
| Ecublens / Lausanne campus | 1 |
| Geneva | 1 |
| Gollion | 1 |
| Gollion (Swiss maintainer; distributed community) | 1 |
| Horw | 1 |
| La Chaux-de-Fonds | 1 |
| Langenthal | 1 |
| Lausanne (EPFL coordination; national network) | 1 |
| Lugano (Viganello) | 1 |
| Männedorf | 1 |
| Manno | 1 |
| Martigny | 1 |
| Opfikon | 1 |
| Paudex | 1 |
| Plan-les-Ouates | 1 |
| Rapperswil-Jona | 1 |
| Saint-Sulpice | 1 |
| Sonceboz-Sombeval | 1 |
| Thun | 1 |
| Windisch | 1 |
| Zurich (national network) | 1 |
| Zurich (origin; global community) | 1 |
| Zurich / Lausanne (edition-dependent) | 1 |

City is a descriptive location, not a normalized municipality identifier. Multi-site programs and edition-dependent events have composite labels and are counted once under that exact label; national networks are assigned their documented coordination location. These counts exclude existing Swiss rows elsewhere in output.

## Query log and saturation

Counts below are **new candidates promoted to a working comparison shortlist**, not every entity in every search result and not necessarily accepted rows. Source-traversal/verification queries can return zero without demonstrating discovery saturation. Concurrent batches are listed in submitted order, not result-arrival order.

Audit limitations: Zurich's inherited log has 34 entries. Rest has 31 entries, its first three explicitly reconstructed source-traversal summaries. The gap log has 33 entries: entries 1–27 are reconstructed thematic discovery counts from this research handoff, **not a contemporaneous complete query transcript**; the final six retain the actual broad search strings and shortlist counts. Some earlier exact strings and candidate-level counting provenance were lost during handoff compaction. Treat reconstructed counts as provisional, not an independently reproducible saturation statistic.

**Earlier handoff saturation: NO — not demonstrated.** The final three broad queries returned shortlist increments 0, 1 and 5. The last query exposed additional component/drone/AI hardware candidates; result sets were not exhaustively enumerated with a stable denominator. Therefore three consecutive independent queries with <10% new entries have not been established. The 22-organization gap fill meets the requested approximate row range, but it did not establish the earlier saturation rule. The follow-up below supersedes this stopping assessment using the user's newly specified fixed denominator. No percentage denominator has been invented by dividing by the entire accumulated corpus.

### Zurich

| # | Query / traversal summary | New shortlist candidates |
|---:|---|---:|
| 1 | Zurich robotics startups Sevensense Verity Wingtra Voliro Gravis Tethys Ascento | 12 |
| 2 | ETH Zurich robotics laboratories ASL CRL PDZ soft robotics vision robotics | 11 |
| 3 | Zurich robotics makerspace student associations investors robotics day | 5 |
| 4 | Zurich robotics investors Founderful Swisscom Ventures Venture Kick robotics | 4 |
| 5 | Zurich robotics ETH school ZHAW mechatronics InES labs | 4 |
| 6 | Zurich robotics open source PX4 Dronecode community | 1 |
| 7 | Zurich robotics Bitwäscherei AMZ Swissloop ARIS robotics | 4 |
| 8 | Loki Robotics Zurich official | 1 |
| 9 | Zurich robotics investors Swisscom Ventures Gravis robotics | 0 |
| 10 | Zurich robotics corporate Disney Research Studios robotics Zurich | 1 |
| 11 | Zurich Innovation Park robotics Dübendorf startups Auterion Duatic | 3 |
| 12 | Zurich robotics hackathon event Robo Hack | 1 |
| 13 | Ascento Zurich official security robots | 0 |
| 14 | Loki Robotics Zurich official cleaning | 0 |
| 15 | Zurich robotics company Sevensense Wingtra Voliro address | 0 |
| 16 | Zurich Lightly Auterion Embotech address | 1 |
| 17 | Founderful Zurich Wingman Ventures rebrand | 0 |
| 18 | site.disneyresearch.com Zurich robotics reinforcement learning robot | 0 |
| 19 | site.idsc.ethz.ch research robotics quadrocopter | 0 |
| 20 | site.ai.ethz.ch robotics embodied AI | 0 |
| 21 | Zurich robotics Flink Robotics Saeki Tinamu Nanoflex official | 4 |
| 22 | Zurich robotics Saeki official address | 0 |
| 23 | Tinamu Zurich official autonomous inventory drones | 0 |
| 24 | Flink Robotics Zurich address | 0 |
| 25 | Nanoflex Robotics Zurich address | 0 |
| 26 | Distran Zurich ultrasonic robotics sensor | 0 |
| 27 | Disney Research Zurich robotics robots BDX | 0 |
| 28 | SAEKI robotics official Oberglatt | 0 |
| 29 | site.nanoflexrobotics.com address Zurich | 0 |
| 30 | site.tinamu-labs.com Zurich address | 0 |
| 31 | SAEKI robotics automated manufacturing funding 2025 Zurich | 0 |
| 32 | Founderful Wingman Ventures rebrand 2024 Zurich | 0 |
| 33 | Fixposition address Schlieren 2026 | 0 |
| 34 | Duatic address Zurich 2026 | 0 |

### Rest of Switzerland / Zurich top-up

| # | Query / traversal summary | New shortlist candidates |
|---:|---|---:|
| 1 | Source traversal (earlier research notes): EPFL Robotics labs, experts, spinoffs, Robopoly, Xplore and Innovation Park | 20 |
| 2 | Source traversal (earlier research notes): ETH entrepreneurship/Pioneer Fellowships, Venture Kick, FabLab Zürich, Zurich robotics funders and industrial robotics suppliers | 10 |
| 3 | Source traversal (earlier research notes): Switzerland applied robotics institutes, medical and underwater robotics | 8 |
| 4 | Kistler headquarters Winterthur official contact | 0 |
| 5 | Twiice contact address Lausanne Renens | 0 |
| 6 | Flyability address Paudex official | 0 |
| 7 | BlueBotics official ANT navigation Saint Sulpice | 0 |
| 8 | Idiap robot learning interaction Sylvain Calinon Martigny official | 1 |
| 9 | Swiss HSLU robotics FHNW HEIG VD HEPIA robotics laboratory | 0 |
| 10 | Swiss Robotics Association NCCR Robotics NCCR Automation Innosuisse | 3 |
| 11 | HSLU robotics competence center robotics intelligent systems Horw | 1 |
| 12 | NCCR Automation Innosuisse Swiss Robotics Association official | 0 |
| 13 | AMLD EPFL LauzHack robotics Drone Days EPFL event | 3 |
| 14 | CSEM robotics Neuchatel robot automation official | 0 |
| 15 | Gudel Schindler RISE Hamilton robotics Switzerland official | 0 |
| 16 | OST robotics institute robotics Rapperswil Buchs official | 1 |
| 17 | Schindler RISE headquarters Ebikon official robot | 0 |
| 18 | Staubli Switzerland Pfaffikon headquarters Faverges robotics | 0 |
| 19 | Cyberbotics contact address Gollion Lausanne official | 0 |
| 20 | Hamilton Bonaduz robotics address official company | 0 |
| 21 | IdSIA address Viganello autonomous robotics official | 0 |
| 22 | AMLD 2026 Multimodal Intelligence Physical World official | 0 |
| 23 | Gudel contact Langenthal headquarters official | 0 |
| 24 | Idiap pbdlib robotics learning demonstration official | 0 |
| 25 | EPFL BioRob salamandra robotica Pleurobot amphibious official | 0 |
| 26 | Hydromea EXRAY Renens underwater robot official | 0 |
| 27 | Switzerland robotics community makerspace student robots Lausanne Bern Ticino | 6 |
| 28 | Switzerland robotics companies research labs nationwide robotics directory | 12 |
| 29 | Basel BIROMED Lab robotics official | 1 |
| 30 | Mobsya address Chavannes Renens official Thymio | 0 |
| 31 | TWIICE official contact Renens address | 0 |

### Final gap fill

| # | Query / traversal summary | New shortlist candidates |
|---:|---|---:|
| 1 | HackZurich START Hack START Summit BaselHack official | 4 |
| 2 | Post Tenebras Lab FIXME FabLab Lausanne makerspace Bern Basel official | 3 |
| 3 | Faulhaber Minimotor Croglio Portescap Sonceboz robotics official | 3 |
| 4 | NCCR Automation Swiss Drone Robotics Centre armasuisse Thun official | 2 |
| 5 | Rovenso ROVENSO Rovenso acquired ROVO robotics Daedalean acquisition | 1 |
| 6 | Swiss Drone Robotics Centre armasuisse Thun official | 0 |
| 7 | Faulhaber Minimotor Croglio Portescap Switzerland headquarters robotics | 0 |
| 8 | Polytech Ventures Flyability Wingman Founderful robotics investment | 1 |
| 9 | FAULHABER Minimotor SA Croglio official company | 0 |
| 10 | Portescap Switzerland La Chaux de Fonds address official | 0 |
| 11 | Daedalean acquired REGENT Zurich official | 0 |
| 12 | Swiss Eurobot CVRA association official | 1 |
| 13 | Polytech Ventures Flyability robotics Switzerland venture | 0 |
| 14 | Geneva university robotics laboratory official | 1 |
| 15 | FabLab Lausanne Renens official | 1 |
| 16 | Swiss Drone Days 2026 official | 1 |
| 17 | Swiss Drone and Robotics Centre site:ar.admin.ch/en | 0 |
| 18 | NCCR Robotics ended 2022 official Lausanne | 1 |
| 19 | Ecorobotix funding Swisscanto lead BIP Distalmotion official funding | 4 |
| 20 | Swiss Drone Days 2026 event Zurich | 0 |
| 21 | Swiss robotics hacker house Zurich Lausanne founders house | 0 |
| 22 | Dufour Aerospace headquarters Duebendorf Visp official autonomous | 1 |
| 23 | Kickfund official location robotics Tethys | 1 |
| 24 | Alpine VC Tethys location Switzerland official | 1 |
| 25 | Swisscanto growth Ecorobotix official | 0 |
| 26 | Coppelia Robotics Switzerland headquarters official | 1 |
| 27 | FabLab Basel official contact | 2 |
| 28 | Switzerland robotics ecosystem organisations research industry community | 3 |
| 29 | Swiss robotics ecosystem companies universities investors associations | 3 |
| 30 | Switzerland robotics startups components makerspaces student teams overview | 13 |
| 31 | Swiss robotics ecosystem overview national robotics map | 0 |
| 32 | robotics Switzerland industry research innovation network | 1 |
| 33 | Switzerland autonomous robotics ecosystem directory | 5 |

### Final short discovery pass (supersedes earlier stopping assessment)

**Saturation: YES under the user's fixed-121 rule**, not a claim of a complete Swiss census. Used five broad discovery searches, eight returned results per query, in submitted order. New candidate names were counted once across this pass after comparison against all existing output organization rows. Counts include unverified directory/technology-transfer candidates, not merely the three accepted rows; incidental foreign investors, people and obviously unrelated local businesses are not candidates. EPFL's mixed directory includes some uncertain robotics relevance/historical companies, retained conservatively in the candidate count rather than silently discarded to lower the yield.

The denominator is **121**, fixed at the starting Swiss organization count as requested; the threshold is <12.1 candidates per query. Queries 3–5 yielded 3/121 (2.48%), 10/121 (8.26%) and 7/121 (5.79%). Discovery stopped immediately after query 5. The second query's 27 candidates reset the streak. This operational stopping test is different from the earlier undefined/global saturation metric; it does not establish geographical completeness or small marginal yield relative to each result set.

| # | Discovery query | New candidate count | % of 121 | Candidate names absent from existing outputs |
|---:|---|---:|---:|---|
| 1 | Swiss robotics startup raises | 2 | 1.65% | Jaipur Robotics, Exclaim Robotics |
| 2 | EPFL spin-off robot | 27 | 22.31% | AICA, Artiria Medical, Autonomyo, Bionomous, Clearspace Today, Didel, Dexterous Endoscopes, Dronistics, ELYTHOR, Foldaway Haptics, IMINA Technologies, Intento, Isochronic, KB Medical, MindMaze, MIROS Technology, Pomelo, SENSARS, senseFly, Simulatory, Feeltronix, Alpine Intuition, Exomotion, DAAV, Fastree3D, PI Imaging Technology, Asterivir |
| 3 | ETH spin-off robot 2025 | 3 | 2.48% | RIVR, Witty Machines, MESH |
| 4 | Geneva robotics startup | 10 | 8.26% | MIKAJAKI, RB Labs, FONGIT, Roboteq Europe, Hiro Robotics, Effetto Venturi, Autodose, Robotique Q, Geneva Robotic Factory, naviq |
| 5 | Ticino robotics | 7 | 5.79% | Scuola di Robotica Ticino, Interroll, InnovaCH, AVISION ROBOTICS, Clinica del Robot, EVO ROBOTICS, Fela Ticino |

Accepted **Jaipur Robotics**, **MESH**, **MIKAJAKI** and **EyeLib** after opening primary sources and checking organization/product duplicates. Jaipur's AGIRE announcement and current company site support Manno, seed financing and waste-to-energy vision software. ETH's MESH article plus current mesh.ch contact support Birr and industrial rebar robotics. MIKAJAKI's current site and its ESCRS 2025 presenter abstract support Plan-les-Ouates and EyeLib; diagnostic benefits remain vendor/presenter claims.

Verification-only lookup: `MESH AG Birr robotics official website` (three results; 0 additional candidates) resolved the official domain to **mesh.ch** after mesh.swiss did not retrieve. It was not another broad discovery query. Subsequent page openings checked already surfaced candidates only. No Google News RSS fallback was necessary because web search returned usable results.

Deferred candidates are not declared irrelevant. AICA's current homepage only announces a new chapter, while the detailed EPFL robotics article is from 2020; Autonomyo's current page emphasizes a fully mechanical SkyWalk with a US contact, so historical Swiss robotic-exoskeleton descriptions should not be copied as current offerings. Bionomous has current automation products but its Swiss address was not reconciled in this short pass. Witty Machines and Exclaim require official current-site/location verification. Other EPFL/Geneva/Ticino candidates remain a verification backlog, not automatic additions. Basel/Bern/St. Gallen searches were not run because the stopping condition had already been met.

## Evidence-quality caveats

- The 242 consulted URLs are deduplicated across inherited lists. Zurich's inherited list includes unsuccessful access attempts. This is a count of consulted URL strings, **not 242 successfully retrieved distinct documents**. Every row has a source citation, but HTTP syntax validation does not independently prove historical retrieval. Redirect aliases may count separately.
- Prefer current official pages for contact/status. Undated marketing pages do not establish release year, autonomous reliability, revenue, safety, clinical efficacy or customer adoption. Null release years and unset stage selects avoid guesses; older funding rounds are labeled historical, not current financing status.
- **HackZurich is on hiatus** and its landing page contains unrelated promotional links. It is retained only as an explicitly inactive ecosystem brand, not a dependable upcoming hackathon. **Swiss Drone Days** is historical: opened archive covers 2017–2022; no 2026/27 edition was established. **NCCR Robotics** is a closed 2010–2022 program, not a live grant. These three historical/inactive rows are included in the 124 organizations, not current-access opportunities.
- START Summit's page advertises **18–19 March 2027**; START Hack's next flagship is 2027. Robotics-specific hardware cases are not guaranteed. BaselHack is a broad regional hackathon. Recheck dates, eligibility and hardware permissions before travel.
- FIXME's October/November 2026 posts show a community relaunch after a pause. Do not infer continuous opening from older pages. FabLab Bern is explicitly an **89grad GmbH project**, hence Corporate rather than an assumed nonprofit. Renens community spaces share an address but have distinct official association identities.
- FAULHABER SA is the consolidated Swiss operation since June 2023, headquartered in Croglio; its parent is German. Portescap SA is a Swiss operating location, not an assertion of Swiss global headquarters. Components relevance is explicit on manufacturer robotics pages, but affordability/student access remains unknown.
- Daedalean's January 2026 acquisition release is issued by Destinus via PRNewswire. The row is Corporate and explicitly a subsidiary/hub, not an independent startup. Civilian perception discussion is proposed; no military operational work is proposed.
- Nadine's hardware/software provenance spans Japan, NTU Singapore and Geneva. The official page spells the Japanese supplier “Rokoro”; identity needs corroboration before resolving a builder relation. MIRALab is attributed to the University of Geneva, not conflated with a similarly named commercial entity. Social/healthcare demonstrations are not proof of therapeutic benefit.
- Aero-200 figures are manufacturer claims, not independent performance measurements. CoppeliaSim license conditions need a separate check; Open source false means an open offering was not established for the row, not a claim that all source is proprietary. Open source true elsewhere means an identifiable published offering, not every company asset.
- Knowledge-node relations are left as inherited/name-based content; no live Notion identifier reconciliation was done. Built by/Used by resolve to organization names in this or other output files; 0 unresolved relation groups were moved into Builder (if not in map). Foreign hardware/software collaborators are not fabricated as Swiss organization rows.
- Student associations, public programs, investors and events do not fit startup funding-stage selects well. Unset values are deliberate; Non-profit is a coarse program/association category rather than a verified legal/tax determination for every lab.

## Updates to existing rows

The names below are exact names already in earlier outputs or inherited Swiss work slices. These are pending corrections/context for verification, **not additional organization rows** and not silent edits to other slices.

- **ABB Robotics** — Sevensense's live company page says it was acquired by ABB in January 2024 and is now merged into ABB as a dedicated business unit. Retain the separate local Sevensense contact rather than treating it as an independent startup. [Source](https://www.sevensense.ai/company)
- **Stäubli Robotics France** — Parent group is Swiss: Stäubli International AG is headquartered in Pfäffikon (SZ); Swiss robotics service/training is in Horgen and Peseux. Keeping this as an existing-row update rather than duplicating the robotics group. [Source](https://www.staubli.com/us/en/about-us/our-business-units/staubli-switzerland.html)
- **Founderful** — Wingman Ventures rebranded to Founderful in February 2024; do not add Wingman as a second investor. [Source](https://www.startupticker.ch/en/news/wingman-ventures-debuts-new-name-and-120-million-fund-ii)
- **Tethys Robotics** — Current official contact page lists Zürcherstrasse 39d, 8952 Schlieren; older Zurich university addresses should not be treated as current company contact addresses. [Source](https://www.tethys-robotics.ch/de-ch/contact)
- **Ecorobotix** — Company counsel documented CHF 46M Series B Prime financing in May 2023, led by AQTON and Cibus, with Swisscanto and others participating. Historical round, not a statement of current stage. [Source](https://www.nkf.ch/news/deals-cases/ecorobotix-sa-completes-series-b-prime-financing/)
- **Distalmotion** — Company announced USD 90M Series E in January 2022 led by Revival Healthcare Capital with 415 CAPITAL participating. Both are foreign funds, not Swiss investors to add to this slice. [Source](https://www.distalmotion.com/news/dexter-series-e-90m-to-make-sense-of-robotic-surgery)
- **Zürcher Kantonalbank** — Swisscanto Growth Fund participated in Ecorobotix's 2023 round; Swisscanto's January 2024 article documents the investment. Avoid counting the bank brand and fund as independent additional organizations without entity-level reconciliation. [Source](https://www.swisscanto.com/ch/en/private/blog/asset-management/2024/private-equity-investment-ecorobotix-nagi-sustainability.html)

Additional exact-name financing context: **Swisscom Ventures** and **Verve Ventures** are listed as existing investors in the opened [Ecorobotix 2023 financing record](https://www.nkf.ch/news/deals-cases/ecorobotix-sa-completes-series-b-prime-financing/); this is evidence for that historical round, not a claim they led it. **Tethys Robotics** is identified as a Kickfund portfolio company since January 2025 in its [July 2025 portfolio story](https://www.kickfund.ch/news/inspecting-the-blue-planet); a round expected in that article is not proof it later closed. The Tethys address correction above is intentionally pending rather than silently overwriting inherited Zurich data.

## Excluded candidates and unresolved coverage

- **Rovenso**: Nivalis's [10 October 2022 release](https://www.nivalisgroup.ch/news/rovenso-files-for-bankruptcy) states it filed bankruptcy on 29 September 2022. No evidence supporting the suggested ANYbotics acquisition was established. Not added as an active startup; ROVéo not added as a current procurement recommendation.
- **Wingman Ventures**: rebrand/alias of Founderful, not another investor. **Swisscanto**: fund/brand relationship with the existing bank row needs entity-level reconciliation; its robotics investment is documented above, not added as an unexamined duplicate.
- **SCHUNK**, **Festo**, **Elistair**, **Kinova**, **Rapyuta Robotics**, **Bitcraze/Crazyflie**, **automatica**, **SPS**, **BlueYard**: not added as Swiss-headquartered actors on the basis of foreign brands or international activity.
- **Polytech Ventures**, **Alpine VC**, **4FOX Ventures**, **ACE & Company**: considered, but no sufficiently complete Swiss organization/location plus robotics-specific primary-evidence row was assembled in this handoff. A named round participant is not automatically a verified Swiss VC row. Distalmotion's Revival and 415 CAPITAL and Ecorobotix's AQTON/Cibus are foreign investors, not Swiss additions.
- **Swiss AI Initiative / Swiss National AI Institute**: no separately opened robotics-specific primary evidence sufficient for a row was assembled; not conflated with ETH AI Center. **Bühler**, **Lambda**, **Akina**: no adequate independent robotics-specific inclusion case completed. This is a research gap, not a finding of no relevance.
- Additional **Swiss hacker/founder houses**, **ROS Zurich/Swiss meetups**, **Swiss RoboCup@Home teams** and a separately named **Swiss Robotics Student association**: no independently verified current entity beyond existing ETH/EPFL clubs/European Robotics House/CVRA was established; do not invent names from generic queries.
- Earlier broad discovery exposed **S3C**, **Rapid Manufacturing**, **Suter Industries**, **Roze Mobility**, **SwissDrones**, **RigiTech**, **Pix4D**, **Aerotainment**, **Distran**, **Fiveco**, **GCtronic**, **Mantis Technologies** and **Witty Machines**, among others. Some may already resolve to broader existing rows; primary-source, location and alias reconciliation is unfinished. Search snippets/directories alone do not justify new verified rows. Jaipur Robotics, also surfaced earlier, was verified and added in the final short pass.
- University-wide umbrella rows and sublabs can coexist where the lab has distinct research outputs and outreach contacts; a full entity-parent graph is not encoded. Historical networks/events are explicitly distinguished rather than excluded without explanation.

## Implications for 42AI and remaining work

Start with a small French-speaking peer build exchange via Robopoly/CVRA, and accessible makerspaces for fabrication/electronics. Use LASA/Idiap demonstrations and simulation tools as educational paths, not evidence that a proprietary industrial system accepts LeRobot policies. For three teams, compare scripted, demonstration-trained and compatible pretrained approaches on the same low-cost task, tracking success, recovery, data collection, calibration, computation and hardware failures.

High-priority unfinished work: coverage beyond this bounded stopping test, independent verifier/coverage-critic passes, current addresses and entity aliases, fundraising recency, product licensing and public access, non-Zurich smaller firms and current meetups, deployment corroboration and customer problem interviews. The lab's software strength does not remove mechanics/electronics/safety constraints; industrial/medical partnerships usually require more than a compelling demo.

## Five-line summary

1. ETH Zurich/UZH and EPFL lead research and spin-offs, with ZHAW/HES institutions, IDSIA, Idiap and CSEM extending applied expertise across Switzerland.
2. Capital flows through Founderful, Verve, Swisscom Ventures, bank/deep-tech programs and foreign robotics investors; grants and founder funding are not automatically available to a French student association.
3. Demand centers on industrial and infrastructure inspection, logistics, precision agriculture, surgical/rehabilitation systems and laboratory automation; safety and integration requirements remain substantial.
4. 42AI's best first contacts are ETH Robotics Club, Robopoly, CVRA and accessible makerspaces; pair small-arm demos with LASA/Idiap open software and scoped technical feedback.
5. Low-cost imitation learning/VLAs are a hypothesis for learning and visibility, not a proven moat: compare against scripted baselines, measure recovery/data costs, and avoid expensive hardware before validating a task.

## Earlier handoff validation (superseded counts)

Final validation output is recorded below after the script run. Blueprint commands reference a `viz/` tree absent from this checkout; no UI/dependency installation was attempted. JSON/schema/name/relation checks are the applicable data checks.

```text
PASS: JSON loads; exact requested top-level/Paris row keys plus _relationship_reason; 5-line summary
PASS: all select/multi-select values match schemas/notion-schema.md; Region Europe; Status To verify
PASS: every row has an HTTP(S) Sources URL; all organization websites HTTP(S)
PASS: no internal or other-output organization/robot name duplicates (case-insensitive)
PASS: Built by/Used by relations resolve; consulted URLs deduplicated; tracked work/ removed
Organizations: 121 {'Association': 20, 'Corporate': 16, 'Event': 9, 'Investor': 8, 'Open-source community': 2, 'Research lab': 34, 'School': 5, 'Startup': 27}
Robots/models/tools: 49
Distinct consulted URLs: 228
Distinct row-cited URLs: 181
Saturation: NO; three consecutive <10% discovery-query yields not demonstrated
PASS: merged rows exactly preserve the three checkpoint slices; no incidental data changes
```

The validation harness initially compared against Paris without allowing the explicitly requested `_relationship_reason` extension; that assertion was corrected, with no data change needed. No other output files were modified. Final whitespace validation uses `git diff --cached --check` before committing.

## Final short-pass validation

Updated validation output follows the final script run. No existing organization/robot rows were edited; three organizations and one robot were appended. The five-line strategic summary remains unchanged.

```text
PASS: JSON loads; exact requested top-level/Paris row keys plus _relationship_reason; 5-line summary
PASS: all select/multi-select values match schemas/notion-schema.md; Region Europe; Status To verify
PASS: every row has an HTTP(S) Sources URL; all organization websites HTTP(S)
PASS: no internal or other-output organization/robot name duplicates (case-insensitive)
PASS: Built by/Used by relations resolve; consulted URLs deduplicated; work/ absent
PASS: original 121 organizations, 49 robots/tools and strategic summary unchanged
Organizations: 124 {'Association': 20, 'Corporate': 16, 'Event': 9, 'Investor': 8, 'Open-source community': 2, 'Research lab': 34, 'School': 5, 'Startup': 30}
Robots/models/tools: 50
Distinct consulted URLs: 242
Distinct row-cited URLs: 188
Saturation: YES under fixed-121 rule; last three discovery yields 3/121, 10/121, 7/121 (<10%)
```
