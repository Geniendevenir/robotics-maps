# Research notes: ecosystem slice Japan / all / top 15

- Output: `output/ecosystem_japan_all.json` (16 organizations, 21 robots/models/tools; first-pass source inventory derived from row citations).
- Notion was not read or written. No `Used in projects` field is output. Knowledge nodes are empty; release years are numeric or null.
- First pass: primary organization/product pages opened with Python requests and HTML text extraction. JavaScript-only pages for Preferred Robotics, aibo, Mujin and iREX were additionally opened through Chrome CDP. Sony's 2017 aibo press release opened successfully in Chrome despite HTTP bot blocking.
- All included rows have a successfully opened primary source and are Draft. Historical sources establish historical products, not 2026 availability. This research still needs independent verification and coverage criticism before any sync.

## Counts and selection

- Top-15-scale means 16 curated organizations, not a quantitative league table. Parent/child Preferred Networks and Preferred Robotics are separate because the AI infrastructure and actual robot products differ.
- Six types: Corporate, Startup, Research lab, School, Event, Association, plus Open-source community (seven types represented). JSK is classified as School to represent University of Tokyo and its lab in one row. Kawada Robotics is a group corporate, not a newly founded venture merely because its legal entity dates to 2013.
- Kawasaki was replaced with ROS Japan Users Group: the robotics site timed out and the alternate official site was blocked in requests and Chrome. No unsupported Kawasaki robot row was retained.
- No investor row in this first pass. Telexistence's primary funding announcement verifies SoftBank investment, but a separate investor row is not needed to pad this short list. Component suppliers and direct demand-side buyers are not separately mapped.

## Discovery queries and saturation

Discovery used Google News RSS (`https://news.google.com/rss/search`, parameters `hl=en-US&gl=US&ceid=US:en`), not HTML search pages. All three queries returned HTTP 200. Titles are discovery leads, not row evidence; primary sites support the rows.

1. `Japan robotics startups industrial robots 2025 2026`: first 12 titles included O-ID/Techstars, Japan physical-AI startup roundups, Reuters adoption polling and IFR global factory-robot coverage. At least one new named Japan candidate (O-ID) beyond the seed list: >=1/15 (6.7%); unnamed Tokyo startups in other titles require follow-up.
2. `Japan robotics university humanoid laboratory ecosystem`: first 10 titles included GMO's Humanoids Summit 2026 Tokyo sponsorship, university robotics and lab-automation reports. At least two new named candidates (GMO, Humanoids Summit) beyond the seed list: >=2/15 (13.3%).
3. `Japan robotics association exhibition open source investors`: first 10 titles included Qualcomm's Japan Robotics Center investment, JETRO ecosystem material and Microsoft Japan infrastructure investment. At least one new robotics-relevant candidate (Qualcomm Japan Robotics Center): >=1/15 (6.7%); Microsoft excluded as generic infrastructure rather than a verified robotics row.

**Saturation not reached in this first pass:** query 2 exceeds the <10% threshold. These are conservative named-candidate lower bounds, not claims that every result was fully investigated. Final pass will add targeted queries and validation; do not interpret the top-N stopping decision as ecosystem exhaustiveness.

## Gaps / notes for verifier and coverage critic

- Funding-stage select values are `unknown` for Preferred Networks, Preferred Robotics, Mujin and Rapyuta Robotics: no opened primary round evidence yet. This deliberately prioritizes the no-guessing rule over inventing a select option; resolve before Notion sync.
- HQ cities remain unknown when not established by the opened evidence (FANUC, Yaskawa, Honda, Preferred Robotics, Rapyuta, AIST). No city was inferred from general knowledge.
- Mujin's website field names the Japanese entity's official domain, while opened evidence is from its US subsidiary's corporate history; the Japanese domain still needs direct opening in the final pass.
- European contact routes are verified for FANUC France, Yaskawa Europe and Mujin Europe. These are public cold routes, not personal warm introductions. Other paths are explicitly unknown.
- Product availability, prices, safety certification for a specific student setup, shipping/import/support in France, loans and sponsorship eligibility are unknown. No hardware donation is implied.
- PLaMo-SemGround is a September 2026 development announcement visible on Preferred Robotics' site, not verified released weights. No generic PFN LLM was mislabeled as a robotics policy. HRP-7 was not verified and is not included.
- aibo is the ERS-1000 model released in 2018, not the original 1999 AIBO. HSR release year refers to the first 2012 announcement described by Toyota, not the updated 2015 prototype.
- `Open source` for organizations means an explicit open-source activity, not all products. Kachaka hardware is closed although its SDK is Apache-2.0. NEXTAGE OPEN denotes an extensible software environment, not proven open hardware.
- Empty Used by relations mean no separately verified deployment by another mapped organization was asserted. HAPiiBOT's unmapped co-developer Amano is named in Builder (if not in map).
- No hiring research was performed; hiring navigation or incidental text in product/company pages was ignored.
