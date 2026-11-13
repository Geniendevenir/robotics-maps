# Research notes: ecosystem slice Japan / all / top 15

- Output: `output/ecosystem_japan_all.json` (17 organizations, 20 robots/models/tools, 33 distinct opened primary source URLs).
- Notion was not read or written. No `Used in projects` field is output. Knowledge nodes are empty; release years are numeric or null.
- First pass: primary organization/product pages opened with Python requests and HTML text extraction. JavaScript-only pages for Preferred Robotics, aibo, Mujin and iREX were additionally opened through Chrome CDP. Sony's 2017 aibo press release opened successfully in Chrome despite HTTP bot blocking.
- All included rows have a successfully opened primary source and are Draft. Historical sources establish historical products, not 2026 availability. This research still needs independent verification and coverage criticism before any sync.

## Counts and selection

- Top-15-scale means 17 curated organizations, not a quantitative league table. Parent/child Preferred Networks and Preferred Robotics are separate because the AI infrastructure and actual robot products differ.
- All eight Types are represented: Corporate (6), Startup (5), Research lab (1), School (1), Event (1), Association (1), Open-source community (1), Investor (1). JSK is classified as School to represent University of Tokyo and its lab in one row. Kawada Robotics is a group corporate, not a newly founded venture merely because its legal entity dates to 2013.
- Kawasaki was replaced with ROS Japan Users Group: the robotics site timed out and the alternate official site was blocked in requests and Chrome. No unsupported Kawasaki robot row was retained.
- Final pass added SoftBank Group as Investor because Telexistence's primary funding announcement explicitly verifies its participation. This is not SoftBank Robotics, and investment/sponsorship for 42AI is not assumed. Component suppliers and direct demand-side buyers are not separately mapped; components and demand remain represented in the value-chain fields.

## Discovery queries and saturation

Discovery used Google News RSS (`https://news.google.com/rss/search`, parameters `hl=en-US&gl=US&ceid=US:en`), not HTML search pages. All three queries returned HTTP 200. Titles are discovery leads, not row evidence; primary sites support the rows.

1. `Japan robotics startups industrial robots 2025 2026`: first 12 titles included O-ID/Techstars, Japan physical-AI startup roundups, Reuters adoption polling and IFR global factory-robot coverage. At least one new named Japan candidate (O-ID) beyond the seed list: >=1/15 (6.7%); unnamed Tokyo startups in other titles require follow-up.
2. `Japan robotics university humanoid laboratory ecosystem`: first 10 titles included GMO's Humanoids Summit 2026 Tokyo sponsorship, university robotics and lab-automation reports. At least two new named candidates (GMO, Humanoids Summit) beyond the seed list: >=2/15 (13.3%).
3. `Japan robotics association exhibition open source investors`: first 10 titles included Qualcomm's Japan Robotics Center investment, JETRO ecosystem material and Microsoft Japan infrastructure investment. At least one new robotics-relevant candidate (Qualcomm Japan Robotics Center): >=1/15 (6.7%); Microsoft excluded as generic infrastructure rather than a verified robotics row.

First-pass saturation was not reached because query 2 exceeded the threshold. A second batch of broad queries returned HTTP 200:

4. `Japan robotics ROS community association industrial startup ecosystem`: 1 result, IFR President's Report. No new named Japan-based organization in the title: 0/15 = 0%.
5. `Japan robotics investors SoftBank humanoid startups 2026`: first 10 titles included SoftBank/Agile Robots, SoftBank/Gravis, global humanoid coverage and Tether/Neura. One new clearly Japan-based organization relative to the working candidate inventory: SoftBank Group (1/15 = 6.7%). Other named acquisition/investment targets were not established as Japan-based by the titles and were not added; their eligibility remains unchecked. SoftBank was subsequently primary-source verified and included. The title about Japan's tech titans does not name its companies, so its underlying entities are unresolved.
6. `Japan robotics leading companies research institutes 2026`: first 10 titles included Qualcomm's Japan Robotics Center (already discovered in query 3), SoftBank (already query 5), NVIDIA/Japan partnerships and global China/Korea coverage. Zero new explicitly named Japan-based organizations relative to the working inventory: 0/15 = 0%.

**Saturation reached at the explicitly named, title-screened top-15 discovery level:** queries 4-6 yielded 0%, 6.7%, 0% new eligible organizations, three consecutive queries below 10%. This is a limited discovery stop, not full-text ecosystem saturation: only the returned title sets above were screened, unnamed organizations remain unresolved, and the unselected candidate backlog is not exhausted. No claims from RSS titles were promoted into rows without an opened primary source.

## Gaps / notes for verifier and coverage critic

- Funding-stage values are `unknown` for Preferred Networks, Preferred Robotics and Rapyuta Robotics: no opened primary round evidence established. This deliberately prioritizes the explicit no-guessing rule over inventing a select option; resolve these three non-schema select values before Notion sync. Mujin's official news index verifies Series C in 2023 and a later $233M raise in December 2025, supporting Series C+; Telexistence's 2023 Series B supports Series A-B, without claiming that it is the latest round.
- HQ cities remain unknown when not established by the opened evidence (Yaskawa, Honda, Preferred Robotics, Rapyuta, AIST, SoftBank). No city was inferred from general knowledge. FANUC's official corporate outline establishes Oshino, Yamanashi.
- Mujin's Japan domain was successfully opened in the final pass and confirms the manufacturing/logistics business. Its US subsidiary's corporate history supplies the Tokyo origin and Eindhoven Europe-office evidence.
- European contact routes are verified for FANUC France, Yaskawa Europe and Mujin Europe. These are public cold routes, not personal warm introductions. Other paths are explicitly unknown.
- Product availability, prices, safety certification for a specific student setup, shipping/import/support in France, loans and sponsorship eligibility are unknown. No hardware donation is implied.
- PLaMo-SemGround is a September 2026 development announcement visible on Preferred Robotics' site, not verified released weights. No generic PFN LLM was mislabeled as a robotics policy. HRP-7 was not verified and is not included.
- aibo is the ERS-1000 model released in 2018, not the original 1999 AIBO. HSR release year refers to the first 2012 announcement described by Toyota, not the updated 2015 prototype.
- `Open source` for organizations means an explicit open-source activity, not all products. Kachaka hardware is closed although its SDK is Apache-2.0. NEXTAGE OPEN denotes an extensible software environment, not proven open hardware.
- Empty Used by relations mean no separately verified deployment by another mapped organization was asserted. HAPiiBOT's unmapped co-developer Amano is named in Builder (if not in map).
- No hiring research was performed; hiring navigation or incidental text in product/company pages was ignored.

## Access and final-pass evidence

- `sources_consulted` contains distinct successfully opened primary URLs used in row citations, not failed guesses, RSS aggregators or blocked pages. Requests returned substantive HTML for most sources; Chrome body text supplied substantive content for Sony's aibo press release, the live aibo site, Preferred Robotics, Mujin homepage and iREX. A 200 status alone was not treated as evidence on JavaScript shells.
- Current anchors include FANUC 2026 product updates, JARA 2026 statistics, PFR's September/October 2026 development/product announcements, Rapyuta's 2026 site news, Telexistence's 2025 deployment/2026 research material and Mujin's 2025 financing index. Older primary releases are retained only for historical models/specifications.
- Failed candidates/paths: Kawasaki robotics Japan timed out and alternate Kawasaki Robotics was blocked; guessed PF Robotics domains did not resolve before the actual `pfrobotics.jp` domain was found; several guessed Yaskawa/Toyota/ROS paths returned 404 before valid primary sources were located. Rapyuta corporate/funding subpages returned 403, so its stage/city were not guessed. Python lacked websocket-client; installed it in the user environment to read Chrome CDP (no repository dependency/config changes).
- iREX is an association-led recurring event, mapped to Non-profit as the nearest schema category, not a claim that commercial co-organizer Nikkan Kogyo Shimbun is nonprofit. Website text differentiates the next iREX (early December 2027) from RoboNext 2026.
