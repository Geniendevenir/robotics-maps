# Verification — Europe / Components

Verified on **2026-11-13** against `devin/playbooks/verifier.md`, `CLAUDE.md` and `schemas/notion-schema.md`. The explicit instructions to use the existing branch, not access Notion, and not open a PR override generic playbook defaults. Branch: `research/ecosystem-europe-components`.

## Result

| Dataset | Input | Verified unchanged | Corrected | Rejected | Retained |
|---|---:|---:|---:|---:|---:|
| Ecosystem Map | 20 | 0 | 20 | 0 | 20 |
| Robots & Models | 16 | 0 | 16 | 0 | 16 |
| **Total** | **36** | **0** | **36** | **0** | **36** |

“Corrected” includes schema cleanup, source repairs, qualification of unsupported claims and omission of unset numeric properties. All organizations contained the non-Notion `_relationship_reason` key. Every product also required correction. No row needed rejection after repair. These report verdicts are not Notion status changes: **all retained rows have Status `To verify`**. No knowledge rows or project candidates occur in this file, so no Project statuses were changed.

## Source checks and access limitations

- Requested all **36 distinct original row-source URLs**, not just a sample. The web reader returned substantive text for 32, title-only shells for the Festo homepage and Schaeffler press index, and no body for the original Bota and Enact addresses. Supplemental primary product pages, legal imprints, investor/issuer releases and dated activity pages were opened where needed.
- A direct request to `https://www.enactintelligence.com` succeeded and redirected to `https://enact-intelligence.com/`. This is **canonicalization, not evidence of a broken or fraudulent original domain**. Its canonical homepage and imprint establish Enact / Eta Robotics AG in Zurich, correcting the initial working hypothesis about that URL.
- `https://www.botasys.com` timed out in the direct check. The readable official `https://botasys.com` site, sensor page and company seed release replace it. A timeout is not evidence that Bota is inactive.
- Direct Festo-homepage and Schaeffler-press-index checks returned HTTP 403; the web reader supplied only titles. Neither is retained as claim evidence. Readable replacements are Festo’s April 2026 group profile, Schaeffler’s August gearbox release and Humanoid’s May deployment/supply release.
- Every retained Sources URL was opened and read through the web reader. The ledger below contains only evidence actually retained, not search-query URLs or an annotated Reuters-homepage placeholder. Primary sources are present and the 15-source minimum is exceeded.
- Official domains were corroborated using product/company pages, legal identities, releases and contact information. Dated 2026 product, partnership, funding or event material supports activity; Raspberry Pi’s about page additionally has October 2026 modification metadata. These are documentary activity checks, not independent solvency or legal-status certificates.

## Row-by-row verdicts

All rows below are **corrected**. Each organization also loses `_relationship_reason`. Numbered evidence links resolve to the opened source ledger; the full row-specific Sources remain in the JSON.

### Ecosystem Map

| Row | Verdict | One-line reason | Opened evidence |
|---|---|---|---|
| Schaeffler | corrected | Replaced the press-index shell with primary releases; separated August 2026 gearbox announcement from planned 2027 production and future robot/actuator commitments from deliveries. | [18](#source-18) [33](#source-33) [46](#source-46) [24](#source-24) |
| maxon | corrected | Added the primary Young Engineers Program; student sponsorship is selective, not guaranteed. The 2026 exhibition reporting supports demonstrated integrated drives and humanoid joints. | [40](#source-40) [38](#source-38) [39](#source-39) |
| Harmonic Drive SE | corrected | Removed unsupported “most robot arm joints” market share; official products/address and SPS 2026 programme support identity, gearing and activity. | [12](#source-12) [11](#source-11) |
| SCHUNK | corrected | Removed non-schema rationale; company pages and June 2026 reporting support grippers and Bosch hand co-development, not a released commercial hand. | [20](#source-20) [26](#source-26) [21](#source-21) |
| Festo | corrected | Replaced a title-only homepage with the April 2026 official group profile; trimmed details not established by that source while retaining drives, Esslingen and Didactic. | [16](#source-16) |
| igus | corrected | Qualified the 2025 €47,999/$54,500 figure as historical and distinguished the June 2026 Iggy Rob Home from the Industrial model. | [34](#source-34) [55](#source-55) [29](#source-29) [17](#source-17) |
| OnRobot | corrected | Omitted invalid unknown funding-stage select; official product, imprint and 2026 milestone pages corroborate tooling, Odense and activity. | [15](#source-15) [14](#source-14) [13](#source-13) |
| Infineon Technologies | corrected | Added the actual IMR page and Neubiberg imprint; October challenge and March Nvidia reporting support 2026 activity without implying a donation offer. | [36](#source-36) [19](#source-19) [45](#source-45) [35](#source-35) [37](#source-37) |
| STMicroelectronics | corrected | Narrowed Nvidia work to the reported camera/motion-sensor integration and distinguished investment in Oversonic from building or using its robots. | [50](#source-50) [43](#source-43) [45](#source-45) |
| NXP Semiconductors | corrected | Removed non-schema rationale; official robotics and Eindhoven pages plus March 2026 reporting support components, networking and Nvidia work. | [41](#source-41) [45](#source-45) [42](#source-42) |
| Axelera AI | corrected | Added primary chip specifications and company history explicitly identifying the $250M+ financing as Series C; retained the supported Series C+ select. | [2](#source-2) [23](#source-23) [3](#source-3) [4](#source-4) |
| Arduino | corrected | Corrected Turin to Monza using September 2026 reporting; removed “first board for robotics” overreach and added official evidence for organization-level platform openness. | [28](#source-28) [56](#source-56) [27](#source-27) |
| Raspberry Pi | corrected | Removed non-schema rationale; current official about page supports low-cost computers, Pico/RP2 and education/industrial positioning, with October 2026 modification metadata. | [44](#source-44) |
| SICK | corrected | Removed non-schema rationale and added official Waldkirch address; homepage anniversary and 2026/2027 notice corroborate current activity. | [49](#source-49) [48](#source-48) |
| Shadow Robot Company | corrected | Changed established hand manufacturer from Startup to Corporate, omitted unknown funding stage and added London contact evidence; October 2026 Fraunhofer work supported. | [22](#source-22) [53](#source-53) [47](#source-47) |
| Bota Systems | corrected | Replaced timed-out www hostname with readable official sources and invalid unknown stage with the documented $2.5M seed; official release updated March 2026. | [5](#source-5) [54](#source-54) [7](#source-7) |
| Synapticon | corrected | Omitted unknown funding stage and changed “manufactures” to announced development/production plans; August 2026 partnership is not proof the joint line ships. | [52](#source-52) [30](#source-30) |
| Enact Intelligence | corrected | Canonicalized the redirecting official URL, added Eta Robotics AG’s Zurich imprint and normalized Pre-seed/Seed; October 2026 funding and force-aware stack supported. | [9](#source-9) [10](#source-10) [51](#source-51) [32](#source-32) |
| Allonic | corrected | Normalized stage, added the investor’s February 2026 round confirmation and clarified actuators connect after braiding; angels from OpenAI/Hugging Face are not corporate investors. | [1](#source-1) [8](#source-8) [31](#source-31) |
| AdapTronics | corrected | Replaced unknown Italian city with Bologna operations/Milan registered office and removed unevidenced seed stage; official EAAL details and October challenge supported. | [25](#source-25) [19](#source-19) |

### Robots & Models

| Row | Verdict | One-line reason | Opened evidence |
|---|---|---|---|
| Schaeffler formed strain wave gearbox | corrected | Changed Kind to Simulator/Tool; omitted announcement-only release year and stated planned 2027 mass production. | [18](#source-18) [46](#source-46) |
| HMND 01 Alpha | corrected | Renamed the generic “Humanoid robots at Schaeffler factories” contract entry to the actual wheeled 2025 robot, set Mobile manipulator and linked builder Humanoid; rollout remains future. | [33](#source-33) [24](#source-24) |
| maxon integrated joint actuator | corrected | Changed Kind to Simulator/Tool; added demonstrated motor/planetary gearbox/dual-encoder/EtherCAT architecture and removed release-year/off-the-shelf availability guesses. | [38](#source-38) |
| Harmonic Drive strain wave gears | corrected | Changed Kind to Simulator/Tool, removed “most joints” market-share assertion and omitted unknown numeric release year. | [12](#source-12) |
| SCHUNK-Bosch humanoid robot hand | corrected | Preserved joint-builder attribution but omitted 2026 as a commercial release year; June 2026 evidence establishes development/demonstration. | [26](#source-26) |
| igus ReBeL cobot | corrected | Added the reported 2022 launch, replaced “price not opened” with current price unknown and removed unsupported comparative affordability. | [55](#source-55) [29](#source-29) |
| Iggy Rob | corrected | Made price a 2025 target, added 2026 manufacturer evidence and distinguished Industrial/Home variants rather than merging their configurations and prices. | [55](#source-55) [29](#source-29) [17](#source-17) |
| OnRobot 2FGP20 | corrected | Separated the 20 kg electric palletizer from the separately listed 2FGP20 Fork and omitted unknown first-release year. | [15](#source-15) |
| Infineon Mobile Robot (IMR) | corrected | Changed Kind to Robot and replaced generic robotics source with its specific hardware platform page; kit availability/price remain unknown. | [35](#source-35) |
| RoBee | corrected | Retained Oversonic as builder, removed ST from Used by because investment alone is not usage evidence, and omitted unknown release year. | [43](#source-43) |
| Axelera Metis | corrected | Changed Kind to Simulator/Tool; primary source confirms up to 214 INT8 TOPS and typical 10 W as separate vendor metrics; omitted unknown release year. | [3](#source-3) [23](#source-23) |
| Arduino VENTUNO Q | corrected | Changed Kind to Simulator/Tool, qualified September 2026 preorder access and omitted hardware Open source checkbox because platform openness does not establish this board design’s license. | [28](#source-28) [56](#source-56) |
| Shadow Dexterous Hand | corrected | Clarified 20 actuated DOF plus four under-actuated movements/24 joints; omitted unknown release year. ROS integration is not an open hardware license. | [22](#source-22) |
| Bota SensONE | corrected | Changed Kind to Simulator/Tool, added actual sensor page and removed 2024 as a family release year: that article launches the T5 variant, not the family or T80. | [6](#source-6) [54](#source-54) |
| Synapticon-Stabilus humanoid actuators | corrected | Changed Kind to Simulator/Tool; August 2026 partnership is a development announcement, not shipping/series-production evidence or a release year. | [30](#source-30) |
| AdapTronics EAAL gripper | corrected | Retained manufacturer-supported 24 V/tactile/proximity details, qualified performance as vendor-reported, removed unevidenced commercial availability and omitted unknown release year. | [25](#source-25) [19](#source-19) |

## Schema, relations and interpretation

- Removed `_relationship_reason` from all 20 organizations and top-level `slice`, `summary` and `sources_consulted`. The remaining `organizations` and `robots_models` keys are structural arrays, not Notion row properties. Every entity key is an actual Notion field name.
- `Simulator/Tool` is the available schema umbrella for component hardware and developer electronics that are not complete robots or AI models; it does not imply a gearbox, sensor or board is simulated. Real arms/hands/grippers retain appropriate robot form factors. IMR is a mobile robot even though it is also a development platform.
- Select spellings match the schema. Unknown funding stages are omitted for OnRobot, Shadow, Synapticon and AdapTronics rather than outputting the invalid select `unknown`. Bota’s seed and Axelera’s Series C have explicit financing evidence. These are the last evidenced stages, not proof no later undiscovered round exists.
- Unknown or announcement-only release years are omitted from the numeric field. Unknown prices/access stay explicit in text. VENTUNO Q hardware-license uncertainty is represented by omitting its checkbox, not guessing false or inheriting organization-level openness.
- Relation values remain names. Humanoid already exists in `output/ecosystem_europe_software_ai.json` and is HMND 01 Alpha’s Built by relation. External co-builders Bosch/Stabilus and RoBee builder Oversonic are named in Builder (if not in map). No auto-managed `Used in projects` or other non-schema reverse relation is output.
- Relationship-potential tags are outreach hypotheses, not verified offers, warm introductions or commitments to sponsor 42AI. YEP is a public application route, not an introduction. No private contact or guaranteed donation was established.
- The narrative summary was removed rather than treating humanoid financing as proof of the lab’s preferred low-cost robot-learning wedge. This fixed-file verification is not a new discovery or coverage exercise.
- No row was rejected. Removed/qualified claims include unsupported market-share superlatives, inferred corporate OpenAI/Hugging Face funding, an unevidenced seed stage, release-year guesses, investment-as-use, guaranteed commercial access and already-achieved large-scale production/rollout.
- Performance, certification and future schedules remain manufacturer/reporter claims. No hardware was purchased, benchmarked, independently safety-certified or tested. A current site or announcement does not guarantee stock, solvency, future delivery or 42AI suitability.

## Validation and git scope

Final machine checks validate JSON parsing, entity field whitelists, select/multi-select membership, numeric/checkbox/text/relation types, unique row names, all To verify statuses, no prohibited reverse relation, nonempty source URLs and relation targets across local output files. The source ledger is generated from the cleaned JSON. Only the requested JSON and this report are committed; no Notion read/write, PR, main push or new research branch.

## Opened source ledger

**56 distinct retained source URLs.** Access limitations and replaced addresses are recorded above.

<a id="source-1"></a>1. https://allonic.com

<a id="source-2"></a>2. https://axelera.ai

<a id="source-3"></a>3. https://axelera.ai/ai-accelerators/aipu/metis

<a id="source-4"></a>4. https://axelera.ai/our-story

<a id="source-5"></a>5. https://botasys.com

<a id="source-6"></a>6. https://botasys.com/force-torque-sensors/sensone/

<a id="source-7"></a>7. https://botasys.com/news/bota-systems-announces-242-5-million-in-seed-round/

<a id="source-8"></a>8. https://dayonecapital.substack.com/p/why-we-invested-in-allonic

<a id="source-9"></a>9. https://enact-intelligence.com/

<a id="source-10"></a>10. https://enact-intelligence.com/imprint/

<a id="source-11"></a>11. https://harmonicdrive.de/de/landingpages/sps-2026

<a id="source-12"></a>12. https://harmonicdrive.de/en

<a id="source-13"></a>13. https://onrobot.com/en/about-us

<a id="source-14"></a>14. https://onrobot.com/en/imprint

<a id="source-15"></a>15. https://onrobot.com/en/products

<a id="source-16"></a>16. https://press.festo.com/en/company/the-festo-group

<a id="source-17"></a>17. https://press.igus.eu/humanoid-robotics-from-germany-igus-launches-new-service-robot/

<a id="source-18"></a>18. https://roboticsandautomationnews.com/2026/08/14/schaeffler-unveils-formed-strain-wave-gearboxes-for-humanoid-robots/104157/

<a id="source-19"></a>19. https://roboticsandautomationnews.com/2026/10/22/infineon-names-winners-of-humanoid-robotics-startup-challenge/106216/

<a id="source-20"></a>20. https://schunk.com/de/en

<a id="source-21"></a>21. https://schunk.com/de/en/company/about-schunk

<a id="source-22"></a>22. https://shadowrobot.com/dexterous-hand-series/

<a id="source-23"></a>23. https://siliconangle.com/2026/02/24/edge-ai-chip-startup-axelera-ai-raises-250m-funding-round/

<a id="source-24"></a>24. https://thehumanoid.ai/humanoid-secures-landmark-deal-with-schaeffler-to-deploy-thousands-of-humanoid-robots/

<a id="source-25"></a>25. https://www.adaptronics.it

<a id="source-26"></a>26. https://www.all-about-industries.com/schunk-and-bosch-are-developing-industrial-grade-robot-hands-for-humanoids-a-8ef3e76a9049d0792a5c6d4082ae1b03/

<a id="source-27"></a>27. https://www.arduino.cc/en/about

<a id="source-28"></a>28. https://www.arduino.cc/product-ventuno-q/

<a id="source-29"></a>29. https://www.designnews.com/automation/igus-unveils-affordable-humanoid-robot-iggy-rob-at-54-500-price-point

<a id="source-30"></a>30. https://www.designworldonline.com/synapticon-and-stabilus-partner-on-robot-actuators/

<a id="source-31"></a>31. https://www.eu-startups.com/2026/02/with-openai-backing-allonic-raises-e6-million-for-robotic-body-manufacturing-platform/

<a id="source-32"></a>32. https://www.eu-startups.com/2026/10/backed-by-yann-lecun-and-arthur-mensch-swiss-physical-ai-startup-enact-intelligence-exits-stealth-with-e26-68-million/

<a id="source-33"></a>33. https://www.forbes.com/sites/johnkoetsier/2026/05/13/humanoids-1000-robot-deal-with-schaeffler-hints-at-100000-units-by-2031/

<a id="source-34"></a>34. https://www.igus.eu

<a id="source-35"></a>35. https://www.infineon.com/application/development-platform

<a id="source-36"></a>36. https://www.infineon.com/applications/industrial/robotics

<a id="source-37"></a>37. https://www.infineon.com/legal/imprint

<a id="source-38"></a>38. https://www.machinedesign.com/show-coverage/automate/video/55387664/maxon-integrated-drives-and-humanoid-joints-highlight-maxons-automation-push

<a id="source-39"></a>39. https://www.maxongroup.com/en/cooperations/young-engineers-program

<a id="source-40"></a>40. https://www.maxongroup.com/en/news-and-events/news

<a id="source-41"></a>41. https://www.nxp.com/applications/industrial/robotics:ROBOTICS

<a id="source-42"></a>42. https://www.nxp.com/company/about-nxp/worldwide-locations/netherlands:NETHERLANDS

<a id="source-43"></a>43. https://www.prnewswire.com/news-releases/oversonic-robotics-stmicroelectronics-fondazione-enea-tech-biomedical-and-spotinvest-acquire-a-stake-in-the-company-302806639.html

<a id="source-44"></a>44. https://www.raspberrypi.com/about/

<a id="source-45"></a>45. https://www.reuters.com/business/nvidia-strikes-humanoid-robot-partnerships-with-european-chipmakers-2026-03-16/

<a id="source-46"></a>46. https://www.schaeffler.com/en/media/press-releases/press-releases-detail.jsp?id=88210241

<a id="source-47"></a>47. https://www.shadowrobot.com/contact/

<a id="source-48"></a>48. https://www.sick.com/de/de/kontakte/w/contactflyout_general_contacts

<a id="source-49"></a>49. https://www.sick.com/de/en/

<a id="source-50"></a>50. https://www.st.com/content/st_com/en/about/st_company_information/who-we-are.html

<a id="source-51"></a>51. https://www.startupticker.ch/en/news/physical-ai-company-enact-intelligence-emerges-from-stealth-with-30m

<a id="source-52"></a>52. https://www.synapticon.com

<a id="source-53"></a>53. https://www.theengineer.co.uk/content/news/shadow-robot-and-fraunhofer-iff-probe-dexterous-robotics

<a id="source-54"></a>54. https://www.therobotreport.com/bota-systems-launches-upgraded-force-torque-sensor-for-small-cobots/

<a id="source-55"></a>55. https://www.therobotreport.com/igus-introduces-iggy-rob-low-cost-humanoid-service-industrial-applications/

<a id="source-56"></a>56. https://www.therobotreport.com/new-ventuno-q-board-arduino-hopes-make-robotics-development-easier/
