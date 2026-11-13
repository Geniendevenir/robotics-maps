# Research: US / all layers / top 25

## Scope and method

Deliverable: `output/ecosystem_us_all.json`, 25 organizations, 21 robots/models/tools, 56 distinct opened source URLs. All rows are **To verify**. This is discovery, not a verifier or coverage-critic pass. No Notion access, hiring research, PR or main push.

Read CLAUDE.md, the ecosystem-researcher playbook, schema, pilot JSONs and Europe research notes. Used web search for discovery, then full-page retrieval of official sites, financing releases, research projects and GitHub repositories. Each row cites opened pages; sources_consulted retains successful pages, not failed requests or snippets.

The selection is editorial, balancing financing/deployment evidence, research influence and usefulness to a software-heavy 15-student Paris lab. It is not a quantitative global ranking. Coverage is 5 Corporate, 7 Startup, 4 Research lab, 1 School, 2 Association, 1 Open-source community, 2 Investor and 3 Event. All Region values are US. All Types are represented; all sectors are not equally covered.

Pilot organization and robot lists were loaded before selection and used only for deduplication, not as evidence for factual claims. Apptronik is not a pilot organization; Apollo 2 is a pilot robot. No pilot organization or robot/model is recreated. Automatically managed reverse relations, including Used in projects, are absent.

### Query audit and stopping limitation

A provisional seed set contained the final 25 plus RSS and a16z. The counts below are **new candidates explicitly promoted to the working comparison set**, not an exhaustive count of every organization in snippets. People, university sublabs, sponsor logos and already-considered parents are excluded. Concurrent queries are listed in submitted order. These are shortlist counts, not sufficient evidence of global saturation.

| Query | New candidate count and names retained for comparison |
|---|---|
| US robotics leading companies physical intelligence funding humanoids | 9: Dyna, World Labs, Anduril, Shield AI, Saronic, Atoms, Hadrian, Mind Robotics, Generalist AI |
| US robotics research universities open source associations investors conferences | 3: USARC, Texas Robotics, Nova Robotics Institute |
| RSS 2026 robotics science systems location | 0 |
| Physical Intelligence Skild Figure Apptronik funding official 2025 2026 | 0 |
| Skild AI Series C site:skild.ai | 0 |
| Physical Intelligence funding site:physicalintelligence.company | 0; irrelevant paper discarded |
| 1X Palo Alto headquarters site:1x.tech | 0; location/eligibility check |
| US robot learning robotics investors startups open source hackathons 2026 | 7: MakerMods, World Intelligence, Physical AI Hack World Tour SF, Viam, New York Robotics, Uncork Capital, Supercharge VC |
| Agility Robotics Series B funding official | 2: Playground Global, Amazon Industrial Innovation Fund |
| Field AI 405 million funding official | 0 |
| Lux Capital Physical Intelligence robotics portfolio | 2: Auris Health, Applied Intuition |
| a16z robotics investment Skild AI official | 0; no a16z–Skild investment claim established |
| Agility Robotics Series C 2025 2026 funding | 0 |
| FieldAI funding 405 million Series B 2025 | 3: Khosla, Canaan, Prysm |
| Physical Intelligence 600 million Series B CapitalG official | 1: CapitalG |
| US robotics ecosystem NVIDIA Figure Agility Stanford CMU investors events | 5: Robotics Fair, EON, Actuate, Formic, Bonsai Robotics |
| US robotics ecosystem Boston Dynamics Intuitive Open Robotics MassRobotics | 0 promoted; existing comparison revisited |
| US robotics robot learning ecosystem companies universities conferences investors | 5: Ambi Robotics, Azalea Robotics, Sensible Robotics, Terranova, Berkeley Startup Cluster |
| 1X Series B 100 million official 2024 | 0 |
| FieldAI Series B stage 2025 | 0 |
| US robotics events investors associations universities leading ecosystem | 5: Robotics Invest, Cybernetix, Ghost Robotics, A3, Pittsburgh Robotics Network |
| US leading humanoid robotics companies | 2: Jabil, Fauna |
| US robotics foundation model companies | 9: General Intuition, Rhoda, Covariant, Config, MoreAI, Acumino, Eka, General Trajectory, Mbodi |
| US robotics research universities open source robotics associations conferences | 3: IEEE RAS, Georgia Tech, University of Michigan |
| United States robotics associations research labs leading universities | 0; already-considered parent institutions |

**Saturation NOT established.** Three funding-validation queries returning zero are not three independent discovery queries showing <10% new entries. Broad late queries still exposed new model companies and investors. This bounded handoff prioritizes the sourced top-25 deliverable; continuing discovery is unfinished process work. Do not interpret these shortlist counts as an exhaustive saturation measurement.

## Evidence quality: opened versus headline-only

Every fact used in the JSON has an opened-page citation. No numeric claim is copied from an unopened headline. Official current pages establish product existence but do not necessarily establish launch year, commercial scale, safety or autonomous reliability.

- Figure's opened September 2025 release states **more than $1B committed** Series C capital and $39B valuation; commitment is not revenue.
- Skild's opened January 2026 release states $1.4B and >$14B valuation. “Any robot” is a company claim, not an independently demonstrated guarantee.
- Apptronik's opened February 2026 release states **>$935M total Series A**, including a $520M extension; do not confuse the total with one new round.
- FieldAI's opened August 2025 release states **$405M across two rounds**, not one $405M Series B. An opened Stock Analysis table supplies Series B labeling; verify against a primary financing record before sync.
- An opened Axios article supplies PI's $600M November 2025 round. Its Series B label comes from the separately opened MEKAWIRE table, not the Axios article or a primary announcement. Secondary funding tables remain To verify.
- 1X's opened January 2024 Series B release is the last explicitly labeled round checked, not a guarantee of current financing status. Opened 2025 HQ announcement says Palo Alto; current About page says San Carlos. Both are retained.
- Mobile ALOHA's 50-demonstration result is reported by its authors; it is not a promise for SO-101. openpi explicitly warns that task checkpoints may fail on a new setup.
- The deprecated SERL page points to HIL-SERL; the inventory uses HIL-SERL, not a recommendation to start with deprecated SERL.
- Direct URL guesses for a CapitalG PI post, PI /blog/series-b, an a16z PI post, the first 1X financing slug, a TRI breakthrough article, CMU /project/tartanair and /robotics, Gazebo homepage and separate NVIDIA Isaac product pages returned no retrievable text. They are not retained as sources. Working alternatives were opened: correct 1X financing URL, NVIDIA overview, Gazebo get-started documentation and Drake project/GitHub.
- Research candidates from search only carry no funding, performance or launch assertions in the output. No claim is made that each candidate below was fully investigated.
- Pages and snippets sometimes include careers text; jobs, recruiting benefits and openings were not extracted.

## Selection decisions and candidates not included

- NVIDIA covers compute/components and simulation; Amazon is a concrete buyer/operator. Boston Dynamics and Intuitive anchor deployed industrial and clinical systems. Tesla is included for influence, not because its program page proves commercial humanoid autonomy.
- Seven startups contrast hardware stacks, downloadable policies, cross-body intelligence, logistics and field autonomy. FieldAI provides a useful counterpoint to a camera-plus-language-only learning narrative.
- Stanford, Berkeley, CMU, MIT and TRI balance education and research. MIT is a School row; CSAIL is not duplicated as an additional organization. OSRF is the community steward, not the commercial subsidiaries acquired by Intrinsic.
- MassRobotics and SVR offer plausible community entry points. Lux and DCVC have opened robotics portfolio evidence; neither is asserted to be the “most active US VC” by deal count.
- CoRL is specifically **2026 Austin**. Automate's opened homepage now advertises **2027 Las Vegas**; this does not imply its 2026 edition was in Las Vegas. Robotics Summit's opened 2026 speaker page supports an engineering-focused Boston entry.
- RSS was considered but its current opened homepage advertises **2027 Athens, Greece**. No US edition was established here, so it is not forced into this slice.
- Dyna, Covariant, Generalist, Rhoda, General Intuition, Config, Acumino and smaller model/data firms need more primary-source diligence. They are not rejected as unimportant; a cross-Type top 25 cannot contain every model startup.
- World Labs is relevant to simulation/world models but loses a slot to actionable robotics infrastructure. Anduril, Shield AI, Saronic and Hadrian would strengthen defense/manufacturing coverage; their exclusion is a material sector gap. Atoms and Mind Robotics need primary-source checks.
- Playground, Cybernetix, CapitalG, Khosla and other investors deserve a dedicated comparative pass. a16z's opened homepage returned little substantive text; DCVC's opened Agility portfolio page provided better direct evidence.
- USARC, Pittsburgh Robotics Network, IEEE RAS, A3 and Texas Robotics are alternatives for association/education coverage. Foxglove was considered from the brief but not investigated enough to classify as an open-source community.
- The **opened Physical AI Hack World Tour SF page** documents a May 2026 XLeRobot/LeRobot build event. It is a useful low-cost-wedge follow-up but not a fourth Event within the 25-slot cap. Viam events remain search-only pending organizer-page checks.
- TartanAir documentation was opened, but institute attribution was not established enough here to add a CMU model. The CMU row explicitly leaves its specific product attribution unknown.

## Field, relation and uncertainty conventions

- Every Ecosystem field is present, plus _relationship_reason. Auto reverse fields are omitted, matching the pilot output structure.
- Unknown textual information is “unknown”; unknown release years are null. The three Event Size / stage values are null because the schema lacks unknown/not-applicable. Do not invent a select option. These are **known unset fields**, not invalid selections.
- Public/Large for Lux/DCVC is the closest available mature-organization category, not publicly traded status. For TRI it denotes corporate backing; investors/events do not fit a startup-funding taxonomy perfectly.
- Unknown City values were not guessed from memory. Salem is a documented assembly location, not verified legal HQ. Stanford/Berkeley locality follows the campus identity; precise address checks remain for verification.
- Open source true means an identifiable open offering, not the entire organization stack. False means no open offering established for this row, not proof of universal closed-source activity; CMU is an important conservative-unknown case.
- Mobile ALOHA's Stanford Robotics Center builder relation is an umbrella attribution for its Stanford team and documented facility support, not sole authorship. Drake lists MIT and TRI because the official page distinguishes origin from current core development.
- Policy (IL/RL) for Helix, Skild Brain and FieldAI is a broad robot-control-policy bucket, **not a verified training recipe**. Exact proprietary architectures are unknown.
- The inventory is representative, not every SKU. Investors/events/associations need not manufacture a robot. Amazon's other drive units/arms, Intuitive's other systems and 1X EVE are not separately inventoried. CMU's specific robot/model remains an explicit gap.
- Apollo 2, ROS 2, LeRobot and SO-101 already exist in pilots; do not recreate them. Apollo 2 can be resolved to the existing row later. Boston Dynamics Atlas is distinct from microagi Atlas; Gazebo is distinct from Genesis.
- Built by and Used by contain only names in this output or pilots. Knowledge nodes are deliberately empty: exact node-name reconciliation was not checked. No auto-managed Used in projects field appears.
- **No warm introduction or promised sponsorship, hardware, compute, partnership or hackathon has been secured.** _relationship_reason is analyst advice. Public contact routes are labeled cold rather than warm. Prices/eligibility are unknown where not established.

## Implications for the Paris lab

The working hypothesis is plausible for learning and visibility, not yet established as a startup moat. Three teams should share a held-out evaluation protocol on inexpensive hardware: a scripted baseline, a demonstration-trained policy, and a compatible pretrained policy. Measure data-collection hours, success rate, cycle time, interventions, recovery and hardware failures, not only the best video. Cheap hardware does not remove GPU, data, calibration or safety costs. Mobile ALOHA is “low-cost” relative to research systems, not necessarily a sub-€500 build.

Publish a reproducible comparison and short failure-aware demo, then request remote author feedback and community speakers. Starting with proprietary humanoids would increase mechanics, procurement and safety burdens before the lab has validated a useful task. Industrial/medical demand is real in the opened examples but comes with integration and validation requirements that tabletop imitation does not solve.

## Remaining gaps

**High:** saturation not established; independent customer/deployment corroboration; detailed policy/hardware compatibility and compute budgets; exact addresses and funding-stage recency; license checks; CMU product attribution; empirical test of the wedge against conventional automation.

**Medium:** defense, agriculture, actuators/components, mobility, medical areas beyond surgery and integrators are underrepresented. Compare VC activity using a consistent time window. Investigate US hackathons supporting international/remote students. Recheck event editions and product versions before sync.

No numerical acquisition claims from pilot outputs were reused. No additional verification or coverage-critic stage is claimed complete.

## Five-line summary

1. NVIDIA supplies enabling compute and simulation; Amazon, Boston Dynamics and Intuitive show deployed systems, while Stanford, Berkeley, CMU, MIT and TRI anchor research.
2. Large disclosed rounds concentrate in humanoids and general robot intelligence: Figure reports >$1B committed Series C, Skild $1.4B, and Apptronik >$935M total Series A.
3. Concrete demand is visible in warehouse handling, industrial inspection/manufacturing and robot-assisted medicine; home humanoids remain a higher-uncertainty bet.
4. For a 15-student Paris lab, start with open policies/tools, publish a measured small-arm demo, and seek remote author feedback and community links through Open Robotics and Silicon Valley Robotics.
5. Low-cost robot learning is a credible learning and visibility wedge, not yet a proven business moat: test robustness, data cost and recovery against scripted baselines before scaling to expensive humanoids.
