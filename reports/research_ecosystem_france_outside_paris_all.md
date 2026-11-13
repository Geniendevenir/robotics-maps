# France outside Paris — ecosystem research

Research date: 13 November 2026. Assigned depth: exhaustive; all ecosystem layers.

## Delivery and coverage

The dataset contains **89 organizations, 47 robot/model/tool records and 120 distinct cited URLs**. Every cited URL was opened, and every row has supporting source content. This is a budget-bounded discovery handoff: the requested depth remains `exhaustive` in the slice metadata, but exhaustive coverage and saturation are **not** claimed. Independent verification and the coverage-critic stage remain for the coordinator.

| Organization type | Rows |
| --- | ---: |
| Corporate | 20 |
| Startup | 28 |
| Research lab | 21 |
| School | 4 |
| Association | 6 |
| Investor | 6 |
| Event | 3 |
| Open-source community | 1 |

The coverage spans industrial manipulation and integration, warehouse fleets, agricultural autonomy, medical assistance, aerial/marine inspection, components, research software, student teams, regional clusters and capital. The product table includes tools as well as physical robots; it contains no newly established AI-model row.

## Scope and method

- Exclude Paris and its surrounding Île-de-France robotics ecosystem. Do not repeat organizations in either pilot output. Regional organizations and explicitly named regional operating entities are eligible; a multinational's global headquarters is not reassigned to France.
- Open official organization, product, research and funding pages. Search snippets are discovery aids; each retained row needs an opened supporting source. Keep commercial claims attributed and do not treat announced capacity as independently validated performance.
- Keep all rows `To verify`. This is research, not the independent verifier or coverage-critic pass. No Notion operations are performed.
- Every Ecosystem Map property is present, plus the playbook-required `_relationship_reason`. Auto-managed reverse relations are omitted. Relations in Robots & Models use organization names.
- `Size / stage: null` means unknown: the schema has no unknown select option. No financing round is inferred from age, headcount or marketing language. Unknown robot release years are also null. A false open-source checkbox means no positive licensing evidence was established for the scoped offering, not proof that every artifact is closed.
- Warm contact paths are unknown unless explicitly documented. Suggested public contact routes and relationship proposals are analysis, not existing relationships or promises of sponsorship.
- Keep acquired teams and regional operating units explicit: Pollen is the Bordeaux team acquired by Hugging Face, while Stäubli Robotics France refers to the Faverges operation of a Swiss-headquartered group. These are not additional rows for their parent companies. Research project teams are named instead of adding duplicate umbrella Inria rows. Shared software credits identify wider collaborators where supported.
- Pilot robot rows such as Reachy/Reachy Mini, LeRobot and SO-101 are not repeated. A regional organization can be relevant to those tools without creating another product row. Product procurement, licensing and present support must still be checked independently.

## Findings and practical implications

The strongest approachable routes are regional robotics clusters, education-oriented hardware suppliers and student robotics associations. Full industrial, agricultural and medical robots are chiefly case studies and potential speaker/demo partners for a fifteen-student lab.

Naïo's November 2025 official relaunch announcement describes a €6.4m financing plan. Its 12 June 2026 official notice ends commercialization and manufacturer support for Orio and Jo. The dataset marks these as discontinued rather than repeating older growth narratives.

Sources: <https://www.naio-technologies.com/actualite/naio-ecrit-une-nouvelle-page-de-son-histoire-et-renforce-son-ancrage-industriel/> and <https://www.naio-technologies.com/wp-content/uploads/2026/06/naio-information-officielle-fin-de-commercialisation-orio-jo-site-web-01062026.pdf>.

Siparex's July 2025 announcement records its France Nucléaire fund's exit from Siléane; it is historical evidence, not a current-shareholding claim: <https://www.siparex.com/le-fonds-france-nucleaire-1-cede-sa-participation-dans-sileane-acteur-cle-de-la-robotique-intelligente/>.

Pollen's August 2026 material announces Microduck at $399 before tax/shipping, with first deliveries targeted before Christmas 2026. Shipment is not confirmed here. The open-source claim covers its software; mechanical and electronic design files are not open. Sources: <https://pollen-robotics.com/microduck/press-kit/> and <https://pollen-robotics.com/microduck/blog/introducing-microduck/>. The current Quantum Surgical site also says the company is part of Precision IO: <https://www.quantumsurgical.com/>.

Capital evidence is dated rather than inferred. Exotec's historical Series D and AISPRID's 2025 Series A demonstrate financing around measurable warehouse and greenhouse tasks. Eclore's February 2026 release documents a €3m seed round for polymer protection/actuation components: <https://www.sodero.fr/wp-content/uploads/2026/02/09/cp-leveedefonds-eclore-2026.pdf>. Nimbl'Bot's 2023 seed announcement is older evidence; its present financing stage is deliberately unknown: <https://www.irdi.fr/nimbl-bot-levee-de-fonds-startup-deeptech-bordeaux/>. In total, 52 organization stages remain null rather than guessed.

WYCA and Keylo were removed from the earlier checkpoint. The domain now mixes robot material with unrelated articles, so it is unsuitable as evidence of a current partner or supported product. A company record also reports a November 2023 liquidation judgment; this supports caution but is not an independent determination of the present ownership of its assets: <https://www.societe.com/societe/wyca-814127684.html>. The Trektor domain opened as a domain-sale page; no standalone Trektor row was retained. This does not prove that the underlying technology ceased to exist.

The nimbleone.io domain currently presents the Nio Robotics brand and the same Aru offering as <https://nio-robotics.com/>. The row records that observed branding without asserting a verified legal-name change. Likewise, ACWA's Pathfinder and Nimbl'Bot's NB-120 have explicit field-test/prototype qualifications instead of assumed 2026 availability.

For the lab, the most credible first request is a remote technical talk, a bill-of-materials review or feedback on a reproducible demo. Aquitaine Robotics, Robotics Place, Coboteam and Proxinnov offer regional introduction paths; Pollen, Niryo, Génération Robots and research teams offer different hardware/software perspectives. A loan or sponsor agreement is a proposal, never an established benefit. Compare a low-cost learning experiment with a supported educational arm and a navigation demo before choosing the lab's wedge; this research does not establish that imitation learning is automatically the best route.

## Discovery stop and remaining gaps

The last three broad discovery queries were:

| Query | What it exposed | Saturation interpretation |
| --- | --- | --- |
| `France robotique entreprises fabricants régions annuaire robots industriels agricoles médicaux` | GdR Robotique's company directory, RobAgri, regional maps and a startup directory; additional manufacturers such as ACWA, E-COBOT and Nimble One | Large candidate lists still require triage; no defensible low-new-entry rate |
| `France robotique laboratoires écoles associations régionales plateformes` | Regional reference structures, research platforms, schools, Poppy Station and education networks | Several overlap with retained teams, but new associations and regional intermediaries remain |
| `France robotique startups composants intégrateurs investisseurs régionaux 2026` | Eclore's 2026 funding, regional industry portraits and additional actuator companies | Added a supported component supplier; wider regional coverage remains unfinished |

These queries were discovery checks, not proof of three consecutive queries below 10% new entries. **Saturation reached: false.** The 22.5-ACU branch budget favors handing off the sourced dataset and explicit gaps instead of claiming a national census.

Useful follow-up discovery sources, opened during this pass:

- GdR Robotique directory (155 listed companies, not all data available to an unauthenticated visitor): <https://www.gdr-robotique.org/entreprises/>.
- National regional-reference list: <https://c-robotique-france2030.org/fr/vos-structures-referentes-en-region-111>.
- Startup directory: <https://startupsrobotique.fr/annuaire-des-startups-francaises-de-la-robotique/>.

Priority gaps are additional SME integrators and component manufacturers, agricultural suppliers and their supported products, regional demand-side operators, and student/open-source communities beyond Bordeaux and Lyon. Meropy, TIBOT/Octopus Biosafety, STERELA and General Robotics are discovery leads, not verified rows in this handoff. Further regional cluster members must be filtered for actual operating geography: Paris/Île-de-France members and organizations already in either pilot remain excluded. Product coverage is selective; unnamed or insufficiently sourced products and foreign-built robots merely distributed by local firms were not invented to fill relations.

## Validation performed

Local validation passed for JSON parsing; exact top-level and row keys; allowed select/multiselect values; boolean/number/list types; five summary lines; unique organization/product names; organization-name relations; all cited URLs present in opened source content; and source-list equality with row citations. It found no case-insensitive name overlap with either pilot output. Every row remains `To verify`, every organization uses `Region: France`, and the forbidden `Used in projects` field is absent. `git diff --check` also passed. Geography, source interpretation, licensing and commercial availability still need independent human/verifier review; structural validation does not establish those facts.

No Notion read/write, PR creation or main-branch push was performed. Only the assigned JSON and report belong in the branch's commits. The 120-source count describes unique row-cited URLs, not a count of all search results or unique domains.

## Five-line summary

1. Regional leaders span industrial robotics (Sepro, Stäubli and Siléane), warehouse automation (Exotec), field autonomy around Toulouse, and research hubs such as Bordeaux, Rennes and Lille.
2. Capital follows deployable automation: Exotec's historical Series D and AISPRID's 2025 Series A illustrate logistics and agricultural investment; recent restructuring at Naïo shows commercialization risk.
3. Demand is concrete in warehouse throughput, repetitive factory handling, vineyard/greenhouse work, inspection and clinician-assisted procedures; these are distinct markets rather than one general humanoid opportunity.
4. For 42AI, regional clusters and student teams offer the clearest route to mechanics/electronics mentors, while open research tools support ambitious software-first demonstrations.
5. Start with an open, measurable low-cost manipulation or navigation demo, then approach Pollen/Niryo, regional robotics clusters and research teams for feedback; industrial and medical platforms are primarily learning/partner routes.
