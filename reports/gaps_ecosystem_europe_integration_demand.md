# Coverage gaps: Europe / Integration + Demand (top 20)

Reviewed on 2026-11-13 against `devin/playbooks/coverage-critic.md`, `CLAUDE.md` and `schemas/notion-schema.md`. Input: `output/ecosystem_europe_integration_demand.json` (cleaned; 20 organizations, 16 robots & models; see `reports/verify_ecosystem_europe_integration_demand.md`). No rows were added and no Notion reads or writes were made.

## Scope and method

Slice = European **system integrators** (factory + warehouse) and European **end users / buyers** of robots, plus demand-side enablers. Builders of robots/AI belong to the Platforms / Software & AI slices; events to the events slice. Every candidate below was checked by name against this file and against the organization lists of all other `research/ecosystem-*` branches (Paris, France outside Paris, Europe Platforms / Components / Software & AI / Investors, events, US, China, Japan, South Korea): none is present as an organization.

Canonical references used: IFR World Robotics 2026 (European installation figures) [S9], VDMA Robotics + Automation [S10], warehouse-automation vendor rankings surfaced in news (Supply Chain Digital "Top 10 warehouse automation vendors" 2026, Modern Materials Handling top-20 systems suppliers; headlines only), NVIDIA GTC Berlin 2026 announcements, and the "well-known players" test (Europe's largest carmakers, Tier-1s, logistics groups, intralogistics integrators). Discovery: ~40 Google News RSS queries; candidate pages opened in Chrome via CDP.

What the file covers well: German carmaker humanoid pilots (BMW, Mercedes), Schaeffler, Siemens, Airbus, e-commerce/grocery (Zalando, Ocado, DHL) and six mid-size warehouse integrators (KNAPP, SSI Schäfer, TGW, Swisslog, Vanderlande, Körber).

Structural gaps: (1) no **enterprise-software / consulting integrators**, the layer that connects robots to WMS/ERP and is the most software-heavy (= closest to the lab's skills); (2) the **largest** European warehouse integrator (KION/Dematic) and the largest robot buyer in Europe (Amazon EU) are missing while smaller ones are in; (3) no **demand data source** (IFR/VDMA); (4) Sectors **Defense, Agri, energy/nuclear and Medical demand** have zero buyer rows (Swisslog healthcare logistics is the only Medical tag).

Importance: **High** = a player most people in European robotics would expect in a top-20 Integration + Demand map, with 2025-26 primary evidence; **Medium** = credible contender that fills a sector, data or partner hole; **Low** = narrower or weakly evidenced.

## High — 6

- **H1 — Audi (Volkswagen Group):** Missing carmaker demand row: Oct 2026 proof-of-concept with Agile Robots, Dassault Systèmes and NVIDIA to automate parts sequencing with mobile humanoids at Ingolstadt (~1 million picks/day) — Europe's newest humanoid pilot, and links to the Platforms slice's Agile Robots [S1].
- **H2 — Bosch:** Missing Europe's largest Tier-1 as both buyer and integrator: Humanoid's HMND 01 ran a box-handling POC in Bosch's Bühl intralogistics site and Bosch will help manufacture Humanoid's robots (with Schaeffler parts); Bosch is also a large robot user across its plants [S2].
- **H3 — SAP (Embodied AI initiative):** Missing software-integration layer: SAP connects humanoids (NEURA 4NE1 at BITZER, Aimbo, Humanoid) to SAP EWM so robots act on live warehouse orders — exactly the "integration is software work" gap named in the file's own summary point 4 [S3, S4].
- **H4 — Accenture:** Missing physical-AI integrator/consultancy: ran the Accenture + Vodafone Procure & Connect + SAP humanoid warehouse pilot (Apr 2026), launched a "Physical AI Safety Suite" with TÜV SÜD at GTC Berlin 2026, and won Stellantis' AI/digital-twin manufacturing programme [S4, S5, S6].
- **H5 — KION Group / Dematic:** Missing one of the largest warehouse-automation integrators (German parent KION, brand Dematic) while six smaller integrators are listed; 2026 Dematic–Hai Robotics alliance to push AMR goods-to-person systems in Europe [S7, S8].
- **H6 — Amazon (European fulfilment network):** Europe's largest robot buyer is absent from this slice: €10 billion 2026 investment in European fulfilment centres including next-gen Proteus robots. `Amazon Robotics` exists in the US file (Region US), so cover it via a relation/note (add Europe context to that row, or add an EU demand row) rather than duplicating the org; the file's summary already names Amazon without a row [S21].

## Medium — 10

- **M1 — IFR (International Federation of Robotics, Frankfurt):** Missing canonical demand-data source: World Robotics 2026 gives European installations (Germany first, Italy ~7,800 units, France ~4,500, Spain ~4,300) and states Europe is growing slowest; useful Mentor/Speaker and context for every demand row [S9].
- **M2 — VDMA Robotics + Automation:** Missing German industry association (integrator/end-user network, market forecasts, 2040 humanoid scenarios); warned in 2026 that Germany is losing ground in robotics [S10].
- **M3 — Jungheinrich:** Missing German intralogistics group: autonomous EAC 212a AMR, Movu Robotics shuttle partnership (Aug 2026) and a €100 million deep-tech investment programme (possible Sponsor route) [S11, S12].
- **M4 — AutoStore:** Missing Norwegian cube-storage robot system that Swisslog and other listed integrators install; CubeVerse software with "28 proprietary AI models"; check against the Platforms slice owner before adding (builder/integration boundary) [S13].
- **M5 — DSV:** Missing major Danish logistics buyer: installed Exotec's Skypod (~100 robots, ~90,000 bins) at Venlo in June 2026 — a demand-side link to the France slice's Exotec [S14].
- **M6 — Fraunhofer IML (Dortmund):** Missing logistics counterpart of Fraunhofer IPA: evoBOT dynamic mobile robot tested at Munich Airport cargo; evidence opened is 2024 (RBR50), so current activity needs a 2026 check [S15].
- **M7 — TÜV SÜD:** Missing safety-certification gatekeeper for deployments (Physical AI Safety Suite with Accenture/NVIDIA, Oct 2026); integration in Europe cannot skip certification [S5].
- **M8 — Sellafield Ltd (UK nuclear decommissioning):** Energy/nuclear demand absent: customised Boston Dynamics Spot with radiation sensing and swabbing in active use (GOV.UK case study, Jan 2026) [S16].
- **M9 — Rheinmetall:** Defense sector has no demand/integrator row: 2026 autonomous military convoy work and UGV integration programmes [S17].
- **M10 — Missing relation, not org:** DHL's flagship robot deal is absent from its row: MOU (May 2025) for 1,000+ additional Boston Dynamics Stretch units, already deployed in the UK and Europe; `Stretch (Boston Dynamics)` exists in the US file, so the syncer should add DHL Group to its `Used by` (same pattern as the Zalando/Nomagic note in the research report) [S18].

## Low — 5

- **L1 — Sapa (Italian auto-parts supplier):** Signed with Paris-based Wandercraft to bring humanoids into its Benevento factory (Nov 2025); small, but a demand-side customer of a Paris builder [S19].
- **L2 — Lidl / Schwarz Group:** Headline (MMH, Dec 2025) reports a rollout of 22 Boston Dynamics robots for container unloading; article page blocked even via CDP, so unconfirmed — the researcher also could not open it [S22].
- **L3 — GXO Logistics:** Plan for up to 1,000 Apptronik Apollo humanoids (Nov 2026) but initial deployment is North America in late 2027; US-headquartered, weak European angle [S20].
- **L4 — Stellantis:** Europe's no. 2 carmaker (large French operations) is absent, but the opened source shows Accenture digital-twin pilots starting in North America; no European robot pilot confirmed [S6].
- **L5 — Volkswagen Group (beyond Audi):** Only FAW-Volkswagen (China) UBTech humanoid trials were found (Oct 2026 headlines); no European-plant evidence, so cover via H1 Audi.

## Considered, not ranked

Element Logic and Kardex (AutoStore integrators; headlines only), Fives (French intralogistics; MMH page blocked), Witron (no 2026 source), Kuehne+Nagel (software rollout, no robot pilot), Geodis (Locus AMRs, 2022), IKEA/Ingka, Carrefour, Nestlé, Volvo, Safran, La Poste, EDF, NHS robotic surgery (no 2025-26 robot-buyer evidence found). Accenture/SAP and Hexagon/Humanoid/Agile Robots must not be duplicated across slices; Agile Robots, NEURA, Boston Dynamics and Exotec are already rows elsewhere.

## Recommendation

Re-run the researcher on H1–H6 only, re-ranking within the 20 slots rather than appending (e.g. Dürr or one of the six mid-size warehouse integrators are the most replaceable). H6 and M10 are relation/cross-file fixes, not new organizations. Pick Medium items deliberately to cover the empty Defense/energy sectors and a demand-data source.

## Saturation

The last three consecutive discovery queries of the second batch (DB Schenker, Geodis, Kuehne+Nagel robots 2026) returned 0 new selectable candidates out of 8 results each, and the third batch's Safran / La Poste / EDF queries also returned 0 — below the 10% threshold for this top-20 shortlist. This is saturation of the prioritized gap list, not proof that every European buyer was found.

## Sources opened (2026-11-13)

| ID | URL | Supports |
|---|---|---|
| S1 | https://www.audi.com/en/media-releases/agile-robots-and-audi-to-transform-automotive-logistics-with-mobile-humanoids-supported-by-dassault-systemes-and-nvidia-18390 | Audi Ingolstadt mobile-humanoid POC |
| S2 | https://www.therobotreport.com/humanoid-partners-with-bosch-schaeffler-scale-robot-production/ | Bosch Bühl POC, Bosch manufacturing for Humanoid |
| S3 | https://news.sap.com/2025/11/sap-physical-ai-partnerships-new-robotics-pilots/ | SAP Embodied AI, BITZER/NEURA, Aimbo |
| S4 | https://newsroom.accenture.com/news/2026/accenture-vodafone-procure-connect-and-sap-pilot-humanoid-robotics-in-warehouse-operations | Accenture/Vodafone/SAP humanoid pilot |
| S5 | https://www.technische-logistik.net/en/news/tuv-sud-and-accenture-present-physical-ai-safety-suite-nvidia-gtc-berlin-2026-27178.html | TÜV SÜD + Accenture Physical AI Safety Suite |
| S6 | https://www.consultancy.eu/news/13715/stellantis-selects-accenture-for-ai-and-digital-twin-manufacturing-transformation | Stellantis–Accenture (North America first) |
| S7 | https://xpert.digital/en/strengthening-amr-competences-in-europe/ | Dematic–Hai Robotics European alliance, KION |
| S8 | https://www.dematic.com/en-gb/ | Dematic official site, European AMR case study |
| S9 | https://ifr.org/ifr-press-releases/news/five-million-robots-now-operate-in-factories-globally | IFR World Robotics 2026 European figures |
| S10 | https://www.therobotreport.com/vdma-warns-germany-losing-ground-in-global-robotics-race/ | VDMA position 2026 |
| S11 | https://www.ivtinternational.com/features/case-study-jungheinrichs-eac-212a-autonomous-mobile-robot.html | Jungheinrich EAC 212a AMR |
| S12 | https://www.technische-logistik.net/en/news/why-jungheinrich-wants-invest-100-million-euros-deep-tech.html | Jungheinrich €100m deep-tech programme |
| S13 | https://www.autostoresystem.com/ | AutoStore system, CubeVerse, AI models |
| S14 | https://www.logisticsmanager.com/dsv-modernises-venlo-logistics-centre-with-asrs/ | DSV Venlo Exotec Skypod |
| S15 | https://www.therobotreport.com/rbr50-spotlight-evobot-offers-unique-design-for-autonomous-mobile-robots/ | Fraunhofer IML evoBOT |
| S16 | https://www.gov.uk/government/case-studies/how-are-robot-dogs-helping-clean-up-sellafield | Sellafield Spot deployment |
| S17 | https://www.rheinmetall.com/en/media/news-watch/news/2026/07/2026-07-13-rheinmetall-is-driving-new-developments-in-autonomous-military-convoys | Rheinmetall autonomous convoys |
| S18 | https://group.dhl.com/en/media-relations/press-releases/2025/dhl-group-signs-mou-with-boston-dynamics-and-accelerates-cross-business-automation-strategy.html | DHL–Boston Dynamics Stretch MOU, UK/Europe deployments |
| S19 | https://en.ilsole24ore.com/art/sapa-bets-humanoid-robot-factory-and-makes-wandercraft-deal-AHSSlkkD | Sapa–Wandercraft |
| S20 | https://www.globenewswire.com/news-release/2026/11/12/3401413/0/en/gxo-and-apptronik-expand-partnership-to-scale-humanoid-deployment.html | GXO–Apptronik plan, North America first |
| S21 | https://www.aboutamazon.com/news/operations/amazon-proteus-robot-europe-investment-employee-support | Amazon €10bn Europe investment, Proteus |
| S22 | https://www.mmh.com/article/after_pilot_program_grocery_company_lidl_rolling_out_fleet_of_22_robots_from_boston_dynamics_to_automate_container_unloading | Lidl headline only (page blocked: "Your request was blocked") |

Hiring not researched. "Used in projects" not output. Input JSON unchanged.
