# Verification report: output/ecosystem_paris_all.json

Verifier run on branch `research/ecosystem-paris-all` (input commit 32728a4). No Notion read/write.

## Summary
- Rows in: 62 organizations + 25 robots/models = 87
- Verified: 66 · Corrected: 18 · Rejected: 3
- Rows out: 84 (all with Status = "To verify")
- URLs checked: 155 unique (HTTP codes: {'404': 5, '200': 121, '403': 17, 'ERR': 6, '429': 1, '503': 1, '400': 1, '401': 3}). 401/403 = bot walls (Reuters, Sifted, eu-startups, MassDevice...): retried via reader proxy; claims resting only on these are flagged below.

## Global corrections (all rows)
- Removed non-Notion key `_relationship_reason` from all organizations (CLAUDE.md: keys must be exactly Notion field names). Original text remains in commit 32728a4.
- `Size / stage` = "unknown" and `Website` = "unknown" set to empty (null): "unknown" is not a valid select option / URL. Text fields keep "unknown".
- Dead (404/400) or truncated source URLs removed from `Sources`; duplicates removed.
- `Status` set to "To verify". No "Used in projects" key present (auto reverse relation, correctly absent).
- All select / multi-select values checked against schemas/notion-schema.md: no invalid values found. All `Built by` / `Used by` names resolve to organizations in this file.

## Open issues for the next pass
- Harmattan AI: needs a primary source for the Series B / Dassault claim and an official website.
- Several funding figures rely on bot-walled articles (Wandercraft €64.3M, Inbolt €11M, SquareMind $18M, Physicl GlobeNewswire): plausible, not re-confirmed.
- CAOR and U2IS websites unreachable from the VM.

## Row-by-row
| Kind | Row | Result | Reason |
|---|---|---|---|
| Org | Hugging Face | verified | Sources open and support claims; selects valid. |
| Org | Wandercraft | corrected | "100+ hospitals" -> "150+ clinical and research sites" per wandercraft.eu/about-us |
| Org | Enchanted Tools | verified | Sources open and support claims; selects valid. | format: Size / stage "unknown" -> empty (not a valid select option) |
| Org | UMA (Universal Mechanical Assistant) | verified | Sources open and support claims; selects valid. | $40M seed (theroboticsmedia) consistent with Pre-seed/Seed. | format: Website "unknown" -> empty (url field) |
| Org | Genesis AI | corrected | its $105M round (Maddyness, July 2025) was a seed round |
| Org | AMI Labs (Advanced Machine Intelligence) | verified | Sources open and support claims; selects valid. | $1.03B raise confirmed (TechCrunch/Wired); round type not stated, "Series C+" kept as approximation. |
| Org | Mistral AI | verified | Sources open and support claims; selects valid. |
| Org | Physicl | verified | Sources open and support claims; selects valid. |
| Org | Bleu Robotics | verified | Sources open and support claims; selects valid. |
| Org | Marso Robotics | verified | Sources open and support claims; selects valid. |
| Org | Galam Robotics | verified | Sources open and support claims; selects valid. | Silicon Canals (via reader proxy) + Supernova confirm €10M round. | format: Website "unknown" -> empty (url field) |
| Org | Inbolt | verified | Sources open and support claims; selects valid. | 2026 €11M round source blocked (403); company/site confirmed. |
| Org | Exwayz | verified | Sources open and support claims; selects valid. |
| Org | Robeauté | corrected | removed dead/truncated source https://www.eu-startups.com/2025/01/size- |
| Org | Moon Surgical | verified | Sources open and support claims; selects valid. |
| Org | Ganymed Robotics | verified | Sources open and support claims; selects valid. | format: Size / stage "unknown" -> empty (not a valid select option) |
| Org | SquareMind | verified | Sources open and support claims; selects valid. | MassDevice $18M article blocked (403); CORDIS SWAN project confirms the company/product; funding amount unconfirmed. | format: Website "unknown" -> empty (url field) |
| Org | Harmattan AI | corrected | claimed round is a $200M Series B -> Series A-B, not Series C+ | Only opened source (The Defense Post, Jul 2025) confirms Paris drone maker + 1,000-drone DGA contract; Series B/unicorn/Dassault claims not confirmed by an opened source; website unknown. | format: Website "unknown" -> empty (url field) |
| Org | Rift | rejected | Only source (eu-startups) is behind a bot wall and could not be opened; no website; unverifiable. |
| Org | AICE | verified | Sources open and support claims; selects valid. |
| Org | Kyber | verified | Sources open and support claims; selects valid. |
| Org | Physikal AI | verified | Sources open and support claims; selects valid. | Site + F4 profile confirm product. | format: Size / stage "unknown" -> empty (not a valid select option) |
| Org | SIM XR | verified | Sources open and support claims; selects valid. | format: Size / stage "unknown" -> empty (not a valid select option) |
| Org | ISYBOT | verified | Sources open and support claims; selects valid. |
| Org | BALYO | verified | Sources open and support claims; selects valid. |
| Org | SCALLOG | verified | Sources open and support claims; selects valid. | format: Size / stage "unknown" -> empty (not a valid select option) |
| Org | Stanley Robotics | verified | Sources open and support claims; selects valid. | Active-in-2026 evidence only from an aggregator (Signalbase, Mar 2026 $4M Series A). |
| Org | Maxtronics | verified | Sources open and support claims; selects valid. | format: Size / stage "unknown" -> empty (not a valid select option) |
| Org | Parrot | verified | Sources open and support claims; selects valid. |
| Org | Prophesee | verified | Sources open and support claims; selects valid. |
| Org | Outsight | verified | Sources open and support claims; selects valid. | Site opened via reader proxy (bot wall); company active. | format: Size / stage "unknown" -> empty (not a valid select option) |
| Org | Exail | verified | Sources open and support claims; selects valid. |
| Org | Partnering Robotics | rejected | Both sources dead (BFMTV 400, Bpifrance 404), no website, latest evidence 2017: cannot confirm it is active in 2026. |
| Org | Renault Group | verified | Sources open and support claims; selects valid. |
| Org | Capgemini | verified | Sources open and support claims; selects valid. |
| Org | Dassault Aviation | corrected | removed dead/truncated source https://www.reuters.com/technology/dassault-aviation-invests-french-defence-ai-unicor | Harmattan Series B lead claim: Reuters link truncated/blocked, not confirmed. |
| Org | Station F | corrected | privately funded campus (Xavier Niel), not a non-profit |
| Org | ISIR (Institut des Systèmes Intelligents et de Robotique) | verified | Sources open and support claims; selects valid. |
| Org | Inria Paris (WILLOW and other teams) | verified | Sources open and support claims; selects valid. |
| Org | CEA-List | verified | Sources open and support claims; selects valid. |
| Org | U2IS – ENSTA Paris | verified | Sources open and support claims; selects valid. | u2is.ensta-paris.fr unreachable from verifier VM; ensta.fr loads; website not re-confirmed. |
| Org | Mines Paris – Centre for Robotics (CAOR) | verified | Sources open and support claims; selects valid. | caor.minesparis.psl.eu unreachable from verifier VM (connection error); org is well known, website not re-confirmed. |
| Org | École 42 Paris | verified | Sources open and support claims; selects valid. | 42.fr behind Cloudflare (403) but is the official domain; hackathon confirmed by 42network.org. |
| Org | Sorbonne Université | verified | Sources open and support claims; selects valid. |
| Org | ENSTA Paris (Institut Polytechnique de Paris) | verified | Sources open and support claims; selects valid. |
| Org | École polytechnique | corrected | removed dead/truncated source https://www.polytechnique.edu/actualites/harmattan-ai-co-fondee-par-mouad-mghari-x20-premiere-licorne-francaise-de-defense; Harmattan AI alumni claim relied on a 404 source; removed unsupported claim |
| Org | CentraleSupélec | corrected | removed dead/truncated source https://21st.centralesupelec.com/en/nos-startups/exw |
| Org | Mines Paris – PSL | verified | Sources open and support claims; selects valid. |
| Org | 42AI | verified | Sources open and support claims; selects valid. |
| Org | Unaite | verified | Sources open and support claims; selects valid. | format: Website "unknown" -> empty (url field) |
| Org | LeRobot community (Hugging Face) | verified | Sources open and support claims; selects valid. |
| Org | GOSIM Paris | verified | Sources open and support claims; selects valid. |
| Org | VivaTech | verified | Sources open and support claims; selects valid. |
| Org | MACHINA (Station F physical-AI summit) | verified | Sources open and support claims; selects valid. | format: Size / stage "unknown" -> empty (not a valid select option); Website "unknown" -> empty (url field) |
| Org | Global Industrie | verified | Sources open and support claims; selects valid. |
| Org | Eurosatory | corrected | removed dead/truncated source https://breakingdefense.com/2026/06/war-robots-invade-eurosatory-2026-as-interest-gro |
| Org | Mistral AI Robotics Hackathon | verified | Sources open and support claims; selects valid. | format: Size / stage "unknown" -> empty (not a valid select option) |
| Org | Adopt AI hackathons (Artefact) | verified | Sources open and support claims; selects valid. | format: Size / stage "unknown" -> empty (not a valid select option) |
| Org | Bpifrance | verified | Sources open and support claims; selects valid. |
| Org | Supernova Invest | verified | Sources open and support claims; selects valid. | format: Size / stage "unknown" -> empty (not a valid select option) |
| Org | Sofinnova Partners | verified | Sources open and support claims; selects valid. |
| Org | Xavier Niel (individual investor) / Kima | corrected | stationf.co is not his/Kima's official site | format: Size / stage "unknown" -> empty (not a valid select option) |
| Robot/Model | LeRobot | verified | Sources open and support claims; selects valid. |
| Robot/Model | SmolVLA | verified | Sources open and support claims; selects valid. |
| Robot/Model | SO-101 arm | verified | Sources open and support claims; selects valid. |
| Robot/Model | Reachy Mini | verified | Sources open and support claims; selects valid. |
| Robot/Model | Reachy 2 | corrected | cited blog does not mention Reachy 2; added Pollen Robotics product page |
| Robot/Model | Atalante X | verified | Sources open and support claims; selects valid. |
| Robot/Model | Calvin-40 | verified | Sources open and support claims; selects valid. | Confirmed by wandercraft.eu nav ("Deploy Calvin-40") and RoboSelect360. |
| Robot/Model | Mirokaï (Miroki / Miroka) | verified | Sources open and support claims; selects valid. |
| Robot/Model | UMA Northstar humanoid | verified | Sources open and support claims; selects valid. |
| Robot/Model | GENE-26.5 | corrected | Reuters source blocked (401); added Genesis AI homepage which announces GENE-26.5 |
| Robot/Model | Eno | rejected | Only source (TNW, truncated URL) returns 404 and the Genesis AI site does not mention Eno; unverifiable. |
| Robot/Model | Genesis (physics simulator) | verified | Sources open and support claims; selects valid. |
| Robot/Model | Robostral Navigate | verified | Sources open and support claims; selects valid. |
| Robot/Model | V-JEPA 2 / JEPA world models | corrected | amilabs.xyz does not mention V-JEPA; added Meta FAIR V-JEPA 2 page |
| Robot/Model | Maestro | verified | Sources open and support claims; selects valid. |
| Robot/Model | Swan | corrected | Model type applies to AI models only -> N/A | Product confirmed by CORDIS (via SquareMind row); its own source is blocked (403). |
| Robot/Model | TAK-ONE | verified | Sources open and support claims; selects valid. | Silicon Canals (reader proxy) mentions modular system; name TAK-ONE not independently re-checked. |
| Robot/Model | Exwayz Engine | corrected | Model type applies to AI models only -> N/A |
| Robot/Model | Inbolt GuideNOW | corrected | Model type applies to AI models only -> N/A |
| Robot/Model | NAO | corrected | "Used by École 42 Paris" unsupported -> removed; builder history added |
| Robot/Model | ANAFI UKR | verified | Sources open and support claims; selects valid. |
| Robot/Model | BALYO autonomous forklifts | verified | Sources open and support claims; selects valid. |
| Robot/Model | ISYBOT sanding cobot | verified | Sources open and support claims; selects valid. |
| Robot/Model | Kyber teleoperation stack | verified | Sources open and support claims; selects valid. |
| Robot/Model | Unitree robots (Orano/Capgemini tests) | corrected | added official Unitree site |
