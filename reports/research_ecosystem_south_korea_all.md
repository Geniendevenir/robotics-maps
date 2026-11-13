# South Korea ecosystem — all layers, top 15

Research date: 2026-11-13. Discovery output, not independent verification. All rows remain `To verify`.

## Scope and selection

The JSON contains 15 Korean organizations and 27 robots/models/tools. “Top 15” is a curated shortlist for a 15-student, software-heavy French robotics lab, not a market-cap ranking. Selection balances national influence, hardware/software coverage, documented openness, and a realistic remote contact route. It includes all eight schema Types: 7 Corporate, 2 Startup, and one each of Research lab, School, Association, Investor, Event, and Open-source community.

Every organization has `Region = South Korea`. US-headquartered Boston Dynamics and RLWRLD are not organization rows even where Korean ownership, founders, or partners are relevant. Korean and foreign subsidiaries are not conflated. ACT is included only because ROBOTIS documents its use; its external builder is explicitly attributed and no US organization is added. CLIP-RT's SNU co-builder is attributed in text without creating a sixteenth organization.

The two pilot outputs were checked before selection. None of their organization names is emitted here. Existing shared tools such as LeRobot and ROS 2 are referenced in prose rather than duplicated as new rows. Relations contain organization names, not Notion IDs. No Notion calls or sync were made, and the reverse relation `Used in projects` is absent.

## Selected organizations

| Organization | Role and selection reason | Realistic first request |
| --- | --- | --- |
| Hyundai Motor Group | Korean Robotics LAB platforms and automotive deployment demand | Remote navigation/deployment speaker |
| Samsung Electronics | AI/home robotics and Rainbow investment | Home-robot perception/HRI speaker |
| LG Electronics | Household manipulation and actuator components | Manipulation/appliance integration speaker |
| Doosan Robotics | Industrial collaborative arms and public ROS 2 packages | Simulation contribution and automation talk |
| Rainbow Robotics | Korean dual-arm manipulation platform and SDK | SDK example, then researcher feedback |
| ROBOTIS | Actuators, research hardware, ROS 2/LeRobot interoperability | Small open-source contribution, then mentor or educational-access enquiry |
| WIRobotics | Wearables, humanoids, and BSD-licensed ALLEX simulation | Simulation benchmark and sim-to-real feedback |
| NAVER LABS | Cloud robotics and documented building-scale delivery | Fleet-orchestration speaker |
| KAIST | University research and HOUND locomotion hardware | Graduate-student paper discussion |
| KIRO | Applied robotics, industrial transfer, and training | Remote testing/education seminar |
| KAR | National industry/academia introductions | Introductions to robot-learning educators |
| ROBOTWORLD | Cross-layer industry exhibition and exhibitor network | Post-event introductions; future delegation enquiry |
| FuturePlay | Korean deep-tech capital and WIRobotics portfolio link | Portfolio introduction or venture speaker |
| OROCA | Korean open-source community and concrete TurtleBot-based project | Check current activity, then bilingual ROS tutorial |
| Tommoro Robotics | Korean VLA models with an open CLIP-RT reproduction route | Benchmark contribution and researcher feedback |

Each `_relationship_reason` is an analyst recommendation, not evidence of a willing partner. All personal warm contacts are unknown. Published mailboxes, issue trackers, and conference routes are public outreach paths. No sponsorship, loan, discount, free cloud allocation, or partnership is promised. No outreach was sent.

## What matters for 42AI

Start with ROBOTIS Physical AI Tools: its [Apache-2.0 ROS 2/LeRobot interface](https://github.com/ROBOTIS-GIT/physical_ai_tools) is a concrete bridge from software skills to recorded demonstrations. Compare an OMX leader/follower workflow against the existing SO-101 hypothesis before committing to hardware. The [OMX documentation](https://ai.robotis.com/omx/hardware_omx.html) lists a 100 g payload at full reach and 250 g at normal reach, which limits demo object choices. No current landed euro price was verified.

For a second team, reproduce a small language-conditioned manipulation task using [CLIP-RT code and checkpoints](https://github.com/clip-rt/clip-rt), or run a narrow dexterous-manipulation experiment with [ALLEX model assets](https://github.com/wirobotics-rih/allex_model). CLIP-RT is a VLA; ALLEX model assets are simulator inputs, not a learned policy. Simulation removes the first hardware purchase but still requires software setup and possibly a GPU. Full humanoid construction would be a poor initial match for the lab's mechanical/electrical skill gap.

A third team could reproduce a miniature delivery-fleet demonstration inspired by [NAVER 1784](https://www.naverlabs.com/en/blogDetail?seq=34068): measure successful deliveries, recovery from blocked routes, and repeated runs. NAVER's reported delivery totals are company claims about its own building, not validated student-accessible performance.

Money is concentrated in corporate-backed physical AI, actuation, industrial handling, and humanoid platforms. The [May 2026 WIRobotics announcement](https://www.wirobotics.com/media/newsDetail?idx=177) reports a KRW 95 billion Series B and names FuturePlay among investors. The strongest evidenced demand examples here are palletizing, building delivery, and walking assistance. Household manipulation is strategically prominent but has less certain student access. No funding target or proposed valuation is reported as a completed round.

## Evidence and uncertainty decisions

- Official current contact information places [Rainbow HQ in Sejong, with an AI center in Seongnam](https://rainbow-robotics.com/en/company/contact-location/). Older Daejeon addresses were superseded. Samsung and Rainbow are separate rows: investor/integrator versus hardware developer.
- [Samsung's Ballie announcement](https://news.samsung.com/global/samsung-and-google-cloud-expand-partnership-bring-gemini-to-ballie-a-home-ai-companion-robot) gave a summer-2025 launch target. Actual shipment, current price, and student access are unknown. The JSON does not infer them from the target date.
- [LG's CES 2026 CLOiD announcement](https://www.lg.com/global/newsroom/news/home-appliance-solution/lg-electronics-presents-lg-cloid-home-robot-to-demonstrate-zero-labor-home-at-ces-2026/) establishes a demonstration and VLM/VLA architecture, not a verified retail launch. The unnamed LG models are not given invented standalone model names.
- [ALLEX repository](https://github.com/wirobotics-rih/allex_model) is BSD-3-Clause, v0.2.0 pre-release, and describes research-prototype v2 hardware, limited research-edition shipments planned later in 2026, kinematic URDF, and experimental USD. A free simulation model does not establish freely reproducible complete hardware.
- [Doosan's root LICENSE](https://github.com/DoosanRobotics/doosan-robot2/blob/humble/LICENSE) says BSD-3-Clause; its README has an Apache badge. The JSON records the actual license file and flags the mismatch. Hardware and emulator terms require separate checks.
- Neuromeka was researched and its public ROS 2 drivers found, but a reusable license was not established. It was left out of the top 15 to make room for Tommoro's stronger robot-learning fit; this is not a claim that its hardware is unimportant.
- [HOUND 2](https://www.dynamicrobot.kaist.ac.kr/kaist-hound-2) says 53 kg in prose and 52 kg in a table. No exact consolidated weight or unsupported speed is emitted. HOUND 1's older result is dated, not presented as 2026 frontier performance.
- [RB-Y1's current product page](https://rainbow-robotics.com/en/products/rb-y1/) has inconsistent total-DOF descriptions across configurations. The JSON retains consistent arm-level facts and avoids one total joint count.
- [SNU's May 2025 CLIP-RT release](https://www.snu.ac.kr/snunow/press?bbsidx=154981&md=v) reports 92.8% LIBERO success; the [current research page](https://clip-rt.github.io/) and code repository report 93.1%. Both are attributed research results, not reproduced evidence. The initial preprint and later code release have different years, so the consolidated release year is null.
- [HABILIS Brain 0 preprint](https://arxiv.org/abs/2609.25558) reports 95.20% and 99.55% LIBERO success for different variants. Public paper access does not establish open weights, licensed model code, affordable API access, or general deployment reliability.
- [ROBOTWORLD's organizer page](https://eng.robotworld.or.kr/exhibition/introduction.php) mixes inconsistent participation counts. A [2026-11-05 government release](https://english.motir.go.kr/eng/article/EATCLdfa319ada/2780/view?bbsCdN=2&pageIndex=1) reports 402 companies/1,198 booths. Counts are omitted from the row instead of mixing years. November 4-7, 2026 has already passed; no next-edition date is invented.
- [OROCA's iTurtle repository](https://github.com/oroca/iTurtle) is historical (2019) and explicitly based on TurtleBot3. Current maintainers, active meetups, and English-language welcome are unknown. Its community identity is supported, but current activity requires verification before outreach planning.
- [KIRO's marine page](https://www.kiro.re.kr/dev/sintro.asp) documents P-SURO II with an older development period. The row is historical; it does not imply a 2026 product launch. Underwater vehicle form factor is `N/A` because the schema has no matching option.

## Schema handling

All Ecosystem Map and Robots & Models fields are present. `_relationship_reason` is the playbook-required research metadata exception and must not be sent to Notion as a property. Auto-managed Ecosystem relations are omitted. `Knowledge nodes` is an empty array because canonical cross-file knowledge-node relations have not been verified.

Unknown text uses “unknown”; unknown release years and unknown/not-applicable selects use JSON null, avoiding invalid invented select options. `Size / stage` is null for ROBOTWORLD (event, not a funding stage), FuturePlay (its own financing stage not established), OROCA (informal community, legal form unknown), and Tommoro (completed round not verified). `Public/Large` includes listed firms and large corporate groups; it does not claim every listed robotics vendor is large by headcount.

Open-source checkboxes are true only where public open resources or a verified license support that claim, with scope explained in text. A false value means no open-source evidence established for this row, not proof that no public code exists. RB-Y1 hardware is false while its Apache-licensed SDK is a separate true row. CLIP-RT code is MIT; checkpoint and dataset terms still require checking. Community/investor/association membership does not imply a `Used by` relationship with portfolio or member products.

## Search coverage and stopping record

Searches covered corporate robotics, collaborative arms, Korean robot learning, open-source communities, university labs, public applied institutes, venture investors, associations, and exhibitions. Primary pages were opened for all selected organizations and every artifact row. The JSON source ledger lists opened URLs, including consulted alternatives; search snippets alone are not the evidence for a row.

Broad follow-up discovery found Tommoro/CLIP-RT and changed the shortlist, so saturation was **not** claimed at that point. Final saturation checks are pending in this work-in-progress report. Depth remains capped at 15 organizations; alternatives are not additional rows.

Important bounded omissions for a future deeper slice include HD Hyundai Robotics (a separate group from Hyundai Motor Group), Hanwha Robotics, Neuromeka, Clobot, Yujin Robot, SNU as a separate institution, KIST, KIRIA, Korea Robotics Society, and Daegu ROBEX. These names were encountered during discovery; they are not promoted to verified organization rows. This shortlist cannot be read as exhaustive coverage of Korean medical, agricultural, defense, or component suppliers.

## Five-line summary

1. Hyundai, Samsung/Rainbow, LG, Doosan and ROBOTIS anchor Korean hardware; NAVER LABS, KAIST and Tommoro add deployed systems and AI research.
2. Capital targets industrial automation, actuators and humanoids; WIRobotics announced a KRW 95 billion Series B in May 2026.
3. Concrete demand examples are palletizing, building deliveries and walking assistance; home manipulation access remains less certain.
4. Test a software-first wedge through ROBOTIS ROS 2/LeRobot tools, open CLIP-RT reproduction, or ALLEX simulation before complex hardware purchases.
5. Publish a reproducible demo, ask maintainers/researchers for remote mentoring, then seek KAR/FuturePlay introductions; ROBOTWORLD 2026 has ended.
