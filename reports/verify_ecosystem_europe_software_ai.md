# Verification — Europe Software & AI

Verified on 2026-11-13 against `devin/playbooks/verifier.md`, `CLAUDE.md` and `schemas/notion-schema.md`, with the user's no-Notion instruction. No Notion reads or writes were made.

## Result

| Dataset | Input | Verified | Corrected | Rejected | Retained |
|---|---:|---:|---:|---:|---:|
| Ecosystem Map organizations | 20 | 0 | 20 | 0 | 20 |
| Robots & Models | 21 | 2 | 19 | 0 | 21 |
| **Total** | **41** | **2** | **39** | **0** | **41** |

“Verified” means no change beyond the required Status reset. “Corrected” includes evidence repairs, unsupported-claim removal and schema cleanup. Every organization required correction because `_relationship_reason` is not a Notion property. No entity needed rejection after repair. Every retained entity has Status `To verify`; this report's verdicts are not changes to Notion status.

All 43 original consultation URLs were requested: 42 yielded readable pages; Wayve's /about/ returned HTTP 403 and was replaced with its readable official homepage and financing announcements. All 68 distinct URLs retained in entity Sources were opened and read. The JSON's consultation list is rebuilt from these row sources. More than 15 distinct sources and numerous primary company, lab, repository and issuer-announcement sources were checked.

## Interpretation and limits

- Organization identity and official domains were checked against live product/lab pages, repositories, legal notices and announcements. Dated 2026 evidence exists for the main company developments. An undated functioning website supports current web presence, not an independent legal or financial certificate that a company is trading in November 2026. Micropsi, Neuracore, Rerun and Wandelbots have such current product pages plus older dated supporting evidence; this limitation is not silently converted into a new dated activity claim.
- Funding stages are the last stage evidenced in the cited sources, not a claim that no later undiscovered round exists. AMI's asserted total was removed because its source only establishes one investor's contribution. Historical 2022 funding sources are used for stage corroboration, not current market claims.
- Performance, customer-pilot maturity, safety and future deployment dates remain attributed company/reporter claims. A rollout target is not an achieved rollout. Apollo 2's detailed demo evidence is secondary reporting; it was not independently reproduced.
- Open source at organization level means the described public artifacts are open, not that every commercial product or hosted service is open. Rerun's actual MIT license was opened despite repository metadata also identifying Apache; both license files exist. Neuracore's SDK is open, while access to its cloud/compute remains conditional.
- Unknown first-release years are omitted from the numeric property rather than guessed or written as the invalid string `unknown`. Unknown prices/eligibility remain explicit in text. VAM has no schema option; FLUX-mimic is mapped to the learned-policy category and described as video-action in text. KinetIQ is classified as a tool/framework.
- European presence is the scope, not necessarily European corporate headquarters: Hugging Face and Genesis span Europe/US; Micropsi's relocation is stated explicitly. Relationship-potential tags are proposed outreach hypotheses, not verified offers or warm introductions. No private contact or sponsorship commitment was established.
- The five summary statements were rewritten to avoid treating the preferred student-lab wedge as proven by funding and product announcements. This fixed-file verification does not add a new discovery/coverage pass.

## Organization verdicts

Each corrected organization also loses the non-schema `_relationship_reason` key. The cited Sources property in the cleaned JSON contains the full evidence set for each row.

| Organization | Verdict | One-line reason | Evidence |
|---|---|---|---|
| Google DeepMind | corrected | Removed non-schema outreach rationale; official model page and 10 November reporting support the model family, Apollo 2 and factory-pilot claims. | [source](https://deepmind.google/models/gemini-robotics/) |
| Wayve | corrected | Replaced blocked /about/ with official homepage and financing releases; removed unsupported cumulative funding and distinguished a conditional Uber commitment from closed Series D capital. | [source](https://wayve.ai) |
| Hugging Face | corrected | Changed Type to Startup, corrected departed LeRobot leadership, removed unsourced kit price, and attributed the pending Nvidia acquisition to reporting rather than treating it as completed. | [source](https://huggingface.co/lerobot) |
| AMI (Advanced Machine Intelligence) | corrected | Removed unsupported $1.03B total: the cited article establishes SBVA's €30M commitment; official site supports world-model goals and Paris presence. | [source](https://amilabs.xyz) |
| Genesis AI | corrected | Corrected San Carlos location and simulation-heavy training claim; added May model announcement, removed sole-originator attribution to the academic simulator, and marked the described proprietary stack closed. | [source](https://genesis.ai) |
| Sereact | corrected | Replaced unsupported Zalando/CEVA customer attribution with the customers actually named in the April article; model and Series B details supported. | [source](https://sereact.ai/en/about) |
| Nomagic | corrected | Added investor's Series B confirmation; official website and company-issued March announcement support warehouse picking and the planned Zalando rollout. | [source](https://nomagic.ai) |
| Humanoid | corrected | Added the official company website to corroborate identity and KinetIQ; July funding article supports Series A, UK operations and planned Q4 beta rollouts. | [source](https://pulse2.com/humanoid-raises-152-million-series-a-at-1-35-billion-valuation-to-scale-industrial-robots/) |
| Flexion Robotics | corrected | Added founder-written Series A announcement supporting the $50M round and simulation/RL stack. | [source](https://flexion.ai) |
| mimic robotics | corrected | Corrected Series A-B to Pre-seed/Seed using the company's $16M seed announcement; official site and July release support FLUX-mimic and Audi work. | [source](https://www.mimicrobotics.com) |
| microagi | corrected | Opened and added the official microagi site; its Atlas/shift products corroborate the data/deployment description and July reporting supports seed financing. | [source](https://pulse2.com/microagi-raises-55-million-seed-funding-to-scale-atlas-robotics-deployment-platform/) |
| Neuracore | corrected | Qualified free academic access as an announced phased programme with possible waitlist; removed any implied guarantee of compute or eligibility for 42AI. | [source](https://neuracore.com) |
| Rerun | corrected | Added primary seed announcement, dated financing coverage and actual MIT license; official site supports Swedish identity, SDK and commercial Hub. | [source](https://rerun.io) |
| Wandelbots | corrected | Added primary NOVA launch and Series C releases; official site supports current product, Dresden identity and Schaeffler case study. | [source](https://www.wandelbots.com) |
| Micropsi Industries | corrected | Replaced invalid unknown select with evidenced Series B; corrected headquarters move versus legal-reorganization claim and retained European origin explicitly. | [source](https://www.micropsi-industries.com) |
| Inbolt | corrected | Official product page and September article support vision-guided robotics, industrial deployments and financing; removed non-schema outreach rationale. | [source](https://www.inbolt.com) |
| Embodied AI | corrected | Replaced unknown Website with official embodiedai.ch; added investor's November AIR announcement to distinguish company launch/funding from robot unveiling. | [source](https://pulse2.com/embodied-ai-launches-with-funding-to-automate-european-manufacturing/) |
| Bleu Robotics | corrected | Replaced unknown Website with official site and Paris legal notice; separated the claimed task-teaching time from the goal for full deployment time. | [source](https://roboticsandautomationnews.com/2026/10/30/bleu-robotics-raises-e5-million-to-scale-humanoid-robot-deployment-in-factories/106554/) |
| ETH Zurich Robotic Systems Lab (RSL) | corrected | Removed unsupported world-model-method claim; direct RSL-RL repository and ETH ANYmal page support lab identity, robot learning and platform lineage. | [source](https://rsl.ethz.ch) |
| ROS-Industrial Consortium Europe | corrected | Removed non-schema outreach rationale; consortium page supports Fraunhofer IPA leadership, Stuttgart, training/events and supplies a public contact. | [source](https://rosindustrial.org/ric-eu) |

## Robot/model/tool verdicts

| Name | Verdict | One-line reason | Evidence |
|---|---|---|---|
| Gemini Robotics 2.5 | verified | Official model page plus 10 November reporting support the name, builder, VLA classification, task count and reported relative success. | [source](https://deepmind.google/models/gemini-robotics/) |
| Gemini Robotics On-Device | corrected | Added the dated June 2025 original On-Device announcement, avoiding confusion with today's On-Device 2; qualified trusted-tester access. | [source](https://deepmind.google/models/gemini-robotics/) |
| Apollo 2 | corrected | Reporting supports Apollo 2, Apptronik and the bow-tying demo; omitted Release year because appearing in a 2026 demo does not establish first release. | [source](https://arstechnica.com/google/2026/11/deepmind-reveals-gemini-robotics-2-5-and-open-safety-benchmark-asimov-jailbreak/) |
| LeRobot | corrected | Removed unsupported Rerun Uses relation and 'default stack' superlative; official Hub/GitHub support features, license and 2024 existence. | [source](https://huggingface.co/lerobot) |
| SO-101 | corrected | Added the actual design repository to support TheRobotStudio/Hugging Face provenance; replaced 'cheapest' with low-cost and omitted unevidenced first-release year. | [source](https://huggingface.co/docs/lerobot/so101) |
| Reachy Mini | corrected | Removed $299 claim absent from the cited InfoQ article; added Pollen's SDK repository to support builder/open-source provenance and qualified current price as unknown. | [source](https://www.infoq.com/news/2025/07/hugging-face-reachy/) |
| Eno | verified | June Reuters report and official waitlist support Eno's 2026 unveiling, Genesis builder, wheeled/foldable design and end-2026 deployment target. | [source](https://finance.yahoo.com/technology/ai/articles/french-startup-bets-non-humanoid-130135284.html) |
| GENE-26.5 | corrected | Added company-issued 6 May announcement: Reuters' Eno article alone does not name GENE-26.5; replaced headline-only specs with supported data-engine description. | [source](https://finance.yahoo.com/technology/ai/articles/french-startup-bets-non-humanoid-130135284.html) |
| Cortex 2.0 | corrected | Attributed world-model/VLA capabilities to the company; omitted 2026 Release year because article date does not establish model's first release. | [source](https://siliconangle.com/2026/04/27/sereact-raises-110m-scale-ai-robotic-brain-expand-us/) |
| Nomagic picking robot ('Richard' at Zalando) | corrected | Separated Richard's picking role from the shoebox solution and rollout plan; omitted first-release year rather than using rollout year. | [source](https://finance.yahoo.com/sectors/technology/articles/zalando-install-50-ai-powered-175200554.html) |
| KinetIQ | corrected | Changed Kind to Simulator/Tool and Model type to N/A: KinetIQ is a multi-layer orchestration framework, not one disclosed policy; added official site and omitted unestablished launch year. | [source](https://pulse2.com/humanoid-raises-152-million-series-a-at-1-35-billion-valuation-to-scale-industrial-robots/) |
| FLUX-mimic | corrected | Changed VLA to the schema's Policy (IL/RL) category for the video-action policy; added official site and qualified Audi testing/deployment maturity. | [source](https://finance.yahoo.com/technology/ai/articles/mimic-robotics-introduces-flux-mimic-150000192.html) |
| Atlas (microagi) | corrected | Added official microagi product page corroborating Atlas and recording/data infrastructure, rather than relying only on financing coverage. | [source](https://pulse2.com/microagi-raises-55-million-seed-funding-to-scale-atlas-robotics-deployment-platform/) |
| Neuracore platform | corrected | Qualified academic access, waitlist and unknown current eligibility; omitted launch year because academic opening is not the platform's first release. | [source](https://neuracore.com) |
| Rerun SDK | corrected | Removed unsupported 'best' superlative and unevidenced 2023 launch year; added adoption evidence and actual MIT license supporting Hugging Face use. | [source](https://rerun.io) |
| Wandelbots NOVA | corrected | Added the company-issued November 2024 NOVA launch announcement, which supports the release year absent from the current homepage. | [source](https://www.wandelbots.com) |
| MIRAI | corrected | Removed unsupported MIRAI 2/2024 launch assertion and numeric year; added company source describing human-trained MIRAI already in 2022. | [source](https://www.micropsi-industries.com) |
| AIR (Embodied AI) | corrected | Added official site and investor's 6 November AIR unveiling evidence; September company-funding article alone does not name AIR or substantiate its November launch. | [source](https://pulse2.com/embodied-ai-launches-with-funding-to-automate-european-manufacturing/) |
| RSL-RL | corrected | Replaced generic GitHub organization evidence with actual RSL-RL repository; removed erroneous 2023 release year (repository created in 2021, first release unknown). | [source](https://github.com/leggedrobotics) |
| ANYmal | corrected | Added ETH as original builder and ANYbotics as commercial manufacturer, direct platform pages and the 2016 paper; replaced subjective price description with unknown price. | [source](https://rsl.ethz.ch) |
| ROS 2 | corrected | Added original ROS 2 Ardent release documentation for middleware capabilities; omitted first-release year because the opened text did not establish its date. | [source](https://rosindustrial.org/ric-eu) |

## Schema and relation checks

Removed all 20 `_relationship_reason` fields and moved the three `_also_considered` notes out of import data. All retained entity property names and select/multi-select options match the reference schema; strings, booleans, arrays, numeric years and URL fields were checked. No auto-managed reverse relation (including `Used in projects`) appears. Forward relations remain arrays of organization names and resolve within this file, except explicitly external builders stored in `Builder (if not in map)`. Knowledge nodes remain empty rather than inventing targets. The outer `slice`, `organizations`, `robots_models`, `summary`, and `sources_consulted` keys are file metadata/containers, not Notion row properties.

Hugging Face is classified as Startup, and Micropsi's invalid `unknown` stage is replaced with its evidenced Series B. Built by / Used by were reviewed independently: Rerun consuming LeRobot is not established merely by LeRobot using Rerun, so that reverse claim was removed. ANYmal's original ETH development and present ANYbotics manufacturing are distinguished.

## Original source URL audit

“Opened” means readable page content was retrieved; it does not certify every original claim attached to that page. The row verdicts above identify unsupported details. The following log covers every original `sources_consulted` URL, including the non-row consideration notes.

| Original URL | Outcome |
|---|---|
| https://amilabs.xyz | Opened; retained for the supported claims, with row-level qualifications above. |
| https://arstechnica.com/google/2026/11/deepmind-reveals-gemini-robotics-2-5-and-open-safety-benchmark-asimov-jailbreak/ | Opened; retained for the supported claims, with row-level qualifications above. |
| https://deepmind.google/models/gemini-robotics/ | Opened; retained for the supported claims, with row-level qualifications above. |
| https://finance.yahoo.com/sectors/technology/articles/zalando-install-50-ai-powered-175200554.html | Opened; retained for the supported claims, with row-level qualifications above. |
| https://finance.yahoo.com/technology/ai/articles/french-startup-bets-non-humanoid-130135284.html | Opened; retained for the supported claims, with row-level qualifications above. |
| https://finance.yahoo.com/technology/ai/articles/mimic-robotics-introduces-flux-mimic-150000192.html | Opened; retained for the supported claims, with row-level qualifications above. |
| https://flexion.ai | Opened; retained for the supported claims, with row-level qualifications above. |
| https://genesis.ai | Opened; retained for the supported claims, with row-level qualifications above. |
| https://github.com/huggingface/lerobot | Opened; retained for the supported claims, with row-level qualifications above. |
| https://github.com/leggedrobotics | Opened; lab identity evidence, not enough for RSL-RL's launch year; direct repo added. |
| https://huggingface.co/docs/lerobot/so101 | Opened; retained for the supported claims, with row-level qualifications above. |
| https://huggingface.co/lerobot | Opened; retained for the supported claims, with row-level qualifications above. |
| https://neuracore.com | Opened; retained for the supported claims, with row-level qualifications above. |
| https://nomagic.ai | Opened; retained for the supported claims, with row-level qualifications above. |
| https://pulse2.com/ai-lab-ami-e30-million-seed-investment-to-develop-world-model-ai/ | Opened; confirms SBVA's €30M commitment, not a $1.03B total. |
| https://pulse2.com/embodied-ai-launches-with-funding-to-automate-european-manufacturing/ | Opened; company/funding evidence from September, not evidence for the later named AIR robot. |
| https://pulse2.com/humanoid-raises-152-million-series-a-at-1-35-billion-valuation-to-scale-industrial-robots/ | Opened; retained for the supported claims, with row-level qualifications above. |
| https://pulse2.com/inbolt-raises-12-5-million-to-expand-ai-powered-industrial-robotics-platform/ | Opened; retained for the supported claims, with row-level qualifications above. |
| https://pulse2.com/microagi-raises-55-million-seed-funding-to-scale-atlas-robotics-deployment-platform/ | Opened; retained for the supported claims, with row-level qualifications above. |
| https://pulse2.com/neuracore-3-million/ | Opened; retained for the supported claims, with row-level qualifications above. |
| https://rerun.io | Opened; retained for the supported claims, with row-level qualifications above. |
| https://rerun.io/about | Opened; retained for the supported claims, with row-level qualifications above. |
| https://roboticsandautomationnews.com/2026/10/30/bleu-robotics-raises-e5-million-to-scale-humanoid-robot-deployment-in-factories/106554/ | Opened; retained for the supported claims, with row-level qualifications above. |
| https://rosindustrial.org/ric-eu | Opened; retained for the supported claims, with row-level qualifications above. |
| https://rsl.ethz.ch | Opened; retained for the supported claims, with row-level qualifications above. |
| https://sereact.ai/en/about | Opened; retained for the supported claims, with row-level qualifications above. |
| https://siliconangle.com/2026/04/27/sereact-raises-110m-scale-ai-robotic-brain-expand-us/ | Opened; retained for the supported claims, with row-level qualifications above. |
| https://techcrunch.com/2026/06/08/uber-wayve-and-waymo-are-headed-towards-a-robotaxi-showdown-in-london/ | Opened; retained for the supported claims, with row-level qualifications above. |
| https://techcrunch.com/2026/08/26/nvidia-closes-in-on-hugging-face-acquisition/ | Opened; retained for the supported claims, with row-level qualifications above. |
| https://thenextweb.com/news/doj-nvidia-hugging-face-deal-antitrust-inquiry | Opened; retained for the supported claims, with row-level qualifications above. |
| https://thenextweb.com/news/theker-barcelona-73m-series-a-ai-robotics | Opened; background consideration only, moved out of cleaned JSON. |
| https://wayve.ai/about/ | HTTP 403; no readable content; removed and replaced by official homepage and Series D releases. |
| https://www.cnn.com/world/micropsi-robots-more-human-spc | Opened; retained for the supported claims, with row-level qualifications above. |
| https://www.heise.de/en/news/German-robotics-startup-raises-largest-seed-round-Coop-with-Google-Cloud-11372650.html | Opened; retained for the supported claims, with row-level qualifications above. |
| https://www.ias.informatik.tu-darmstadt.de | Opened; background consideration only, moved out of cleaned JSON. |
| https://www.inbolt.com | Opened; retained for the supported claims, with row-level qualifications above. |
| https://www.infoq.com/news/2025/07/hugging-face-reachy/ | Opened; supports hardware/features and 2025 launch, but contains no $299 price. |
| https://www.micropsi-industries.com | Opened; retained for the supported claims, with row-level qualifications above. |
| https://www.mimicrobotics.com | Opened; retained for the supported claims, with row-level qualifications above. |
| https://www.nx-ai.com | Opened; background consideration only, moved out of cleaned JSON. |
| https://www.techspot.com/news/112938-startup-taught-humanoid-robots-retrieve-packages-climb-stairs.html | Opened; retained for the supported claims, with row-level qualifications above. |
| https://www.techtimes.com/articles/317624/20260602/icra-2026-day-2-open-source-robotics-wave-crests-security-flaw-shadows-lerobot.htm | Opened; retained for the supported claims, with row-level qualifications above. |
| https://www.wandelbots.com | Opened; retained for the supported claims, with row-level qualifications above. |

## Additional opened evidence retained

- https://bleu-robotics.com/
- https://bleu-robotics.com/legal
- https://deepmind.google/about/
- https://deepmind.google/discover/blog/gemini-robotics-on-device-brings-ai-to-local-robotic-devices/
- https://embodiedai.ch/
- https://flexion.ai/news/flexion-raises-50m-to-build-the-brain-of-humanoid-robots-at-scale
- https://github.com/TheRobotStudio/SO-ARM100
- https://github.com/leggedrobotics/rsl_rl
- https://github.com/pollen-robotics/reachy_mini
- https://lookai.vc/embodied-ai-unveils-air-humanoid-robot/
- https://microagi.ai
- https://raw.githubusercontent.com/rerun-io/rerun/main/LICENSE-MIT
- https://raw.githubusercontent.com/ros2/ros2_documentation/rolling/source/Releases/Release-Ardent-Apalone.rst
- https://rerun.io/blog/physical-ai-data
- https://rsl.ethz.ch/robots-media/anymal.html
- https://salesforceventures.com/perspectives/welcome-hugging-face/
- https://techcrunch.com/2025/03/20/reruns-open-source-ai-platform-for-robots-drones-and-cars-revs-up-with-17m-seed/
- https://thehumanoid.ai
- https://wayve.ai
- https://wayve.ai/press/series-d-extension/
- https://wayve.ai/press/series-d/
- https://www.anybotics.com/robotics/anymal/
- https://www.businesswire.com/news/home/20241106616593/en/Wandelbots-Presents-NOVA-The-Worlds-First-Agnostic-Operating-System-for-Robots
- https://www.ebrd.com/home/news-and-events/news/2025/ebrd-invests-in-polish-based-robotics-company-nomagic.html
- https://www.globenewswire.com/news-release/2025/11/03/3179052/0/en/mimic-robotics-raises-16-million-to-deploy-frontier-physical-ai-across-industries.html
- https://www.micropsi-industries.com/blog/micropsi-industries-secures-30m-in-series-b
- https://www.prnewswire.com/news-releases/genesis-ai-unveils-gene-26-5--the-first-ai-brain-to-enable-robots-with-human-level-physical-manipulation-capabilities-302763638.html
- https://www.prnewswire.com/news-releases/robotics-software-company-wandelbots-raises-84-million-series-c-led-by-insight-partners-301467575.html
- https://www.research-collection.ethz.ch/server/api/core/bitstreams/09cfc536-6001-4295-b9ae-4e6b049c151e/content

## Non-row consideration notes

These were metadata, not members of the 41 entity rows; they are neither retained nor counted as rejected. Their URLs were opened, without expanding the assigned top-20 list.

- **THEKER**: Barcelona AI-native factory robots, €73M Series A Jun 2026; more Platforms than Software & AI. Source opened: https://thenextweb.com/news/theker-barcelona-73m-series-a-ai-robotics
- **NXAI**: Linz frontier lab (xLSTM, world models for industrial systems); robotics link via NEURA partnership seen only in headlines. Source opened: https://www.nx-ai.com
- **TU Darmstadt Intelligent Autonomous Systems**: Robot-learning research group (Prof. Jan Peters) with public robot-learning talks. Source opened: https://www.ias.informatik.tu-darmstadt.de

## Validation

The cleaned JSON parses; all 41 rows have valid property names/options and Status `To verify`; title uniqueness, scalar/array types, allowed relation targets, absence of auto-managed fields, and exact consultation/source coverage were checked locally. Every retained source URL has readable retrieved evidence. `git diff --check` passes. No application code changed and no Notion sync was attempted.
