# Verification report: output/ecosystem_japan_all.json

Verifier run on branch `research/ecosystem-japan-all` (input commit 40a5881). No Notion read/write.

## Summary
- Rows in: 17 organizations + 20 robots/models = 37
- Verified: 31 · Corrected: 6 · Rejected: 0
- Rows out: 37 (all with Status = "To verify"; file has no project candidates)
- URLs checked: 49 unique sources + websites (HTTP codes: {'200': 47, '403': 2}). The 2 sony.com 403s are bot walls; both pages read fine via Chrome CDP. JS-rendered pfrobotics.jp, kachaka.life and aibo.sony.jp were also read via CDP.

## Global corrections (all rows)
- Removed non-Notion key `_relationship_reason` from all 17 organizations (keys must be exactly Notion field names). Original text remains in the input commit.
- `Size / stage` = "unknown" set to empty (null) for Preferred Networks, Preferred Robotics, Rapyuta Robotics: not a valid select option.
- `Status` set to "To verify". No `Used in projects` key present (auto reverse relation).
- All select / multi-select values checked against schemas/notion-schema.md: no invalid values. All `Built by` / `Used by` names resolve to organizations in this file. `Knowledge nodes` are empty everywhere (left for the architect/syncer).

## Open issues for the next pass
- City still "unknown" for Yaskawa Electric (HQ Kitakyushu is widely reported but not on an opened page), Rapyuta Robotics, Preferred Robotics, AIST, ROS Japan Users Group.
- aibo weight and the exact model code ERS-1000 are not stated on the opened Sony release (specs table not in rendered text); name kept.
- Slice is thin for a 'top 15' Japan map (no Kawasaki, Denso, Mitsubishi Electric, Epson, Nachi, Harmonic Drive, Ascent Robotics, Mujin peers, AIRoA consortium); a coverage critic should flag these.

## Row-by-row
| Kind | Row | Result | Reason |
|---|---|---|---|
| Org | FANUC | verified | Sources open and support claims; selects valid. HQ Oshino-mura (profile), CRX/ROBOGUIDE/Omniverse Jan 2026 and Oct 2026 physical-AI news on product index; French offices confirmed. |
| Org | Yaskawa Electric | verified | Sources open and support claims; selects valid. MOTOMAN, servo motors and HC cobots confirmed; City left unknown (HQ not on opened pages). |
| Org | Sony | verified | Sources open and support claims; selects valid. sony.com 403 to curl, read via Chrome CDP; aibo Developer Program linked from aibo.sony.jp. |
| Org | Honda | corrected | City unknown -> Tokyo (Minato-ku HQ per global.honda/en/about/info). Avatar robot, UNI-ONE and post-ASIMO strategy confirmed. |
| Org | Toyota Motor Corporation | verified | Sources open and support claims; selects valid. 2015 HSR/Developers' Community page opens. |
| Org | Preferred Networks | corrected | Size / stage "unknown" -> empty (invalid select). AI chips, Fanuc among shareholders, Tokyo HQ and PLaMo-SemGround (PFR news 2026-09-09) confirmed. |
| Org | Preferred Robotics | corrected | Size / stage "unknown" -> empty. pfrobotics.jp (JS, read via CDP) confirms Kachaka Pro/Evo, HAPiiBOT with Amano; kachaka-api is Apache-2.0. |
| Org | Mujin | verified | Sources open and support claims; selects valid. Founded Tokyo 2011, $85M Series C (Sep 2023), $233M raise (Dec 2025), Eindhoven office Oct 2023. |
| Org | Telexistence | verified | Sources open and support claims; selects valid. TX Ghost 7-Eleven pilots (Sep 2025), $170M Series B (2023), 2026 humanoid/foundation-model news (NVIDIA Cosmos Coalition). |
| Org | Rapyuta Robotics | corrected | Size / stage "unknown" -> empty. PA-AMR, ASRS and 2026 news confirmed on live site. |
| Org | Kawada Robotics | verified | Sources open and support claims; selects valid. NXA (2018), Fillie (2022), OPEN variants, HRP-2/3/4 and Taito-ku Tokyo HQ confirmed. Public/Large kept: subsidiary of listed Kawada Industries. |
| Org | AIST | verified | Sources open and support claims; selects valid. HRP-5P 2018 press release confirmed. |
| Org | University of Tokyo — JSK Laboratory | verified | Sources open and support claims; selects valid. Research index lists musculoskeletal humanoids, aerial robots and open-source robot software. |
| Org | iREX (International Robot Exhibition) | verified | Sources open and support claims; selects valid. Site reports 2025 show; next iREX early Dec 2027; RoboNext 2026 (Intex Osaka) separate. |
| Org | Japan Robot Association (JARA) | verified | Sources open and support claims; selects valid. Quarterly stats through Jul-Sep 2026 (published 27 Oct 2026). |
| Org | ROS Japan Users Group | verified | Sources open and support claims; selects valid. GitHub profile links connpass, Slack, hackathon repo. |
| Org | SoftBank Group | corrected | City unknown -> Tokyo (Minato-ku HQ per group profile). Investor role in Telexistence Series B confirmed; SBRG distinction correct. |
| Robot/Model | FANUC CRX series | verified | Sources open and support claims; selects valid. |
| Robot/Model | FANUC ROBOGUIDE | verified | Sources open and support claims; selects valid. |
| Robot/Model | MOTOMAN HC10DTP | verified | Sources open and support claims; selects valid. |
| Robot/Model | MOTOMAN HC20DTP | verified | Sources open and support claims; selects valid. |
| Robot/Model | aibo ERS-1000 | corrected | Key specs: removed "approximately 2.2 kg" and "two cameras" (not in opened sources); kept 22 axes and fish-eye SLAM cameras per Sony 2017 press release. |
| Robot/Model | Honda Avatar Robot | verified | Sources open and support claims; selects valid. |
| Robot/Model | Toyota Human Support Robot (HSR) | verified | Sources open and support claims; selects valid. |
| Robot/Model | Kachaka Pro | verified | Sources open and support claims; selects valid. |
| Robot/Model | Kachaka Evo | verified | Sources open and support claims; selects valid. |
| Robot/Model | HAPiiBOT | verified | Sources open and support claims; selects valid. |
| Robot/Model | Kachaka API SDK | verified | Sources open and support claims; selects valid. |
| Robot/Model | PLaMo-SemGround | verified | Sources open and support claims; selects valid. |
| Robot/Model | MujinController PickWorker | verified | Sources open and support claims; selects valid. |
| Robot/Model | MujinOS | verified | Sources open and support claims; selects valid. |
| Robot/Model | TX Ghost | verified | Sources open and support claims; selects valid. |
| Robot/Model | Rapyuta PA-AMR | verified | Sources open and support claims; selects valid. |
| Robot/Model | NEXTAGE (NXA) | verified | Sources open and support claims; selects valid. |
| Robot/Model | NEXTAGE Fillie | verified | Sources open and support claims; selects valid. |
| Robot/Model | HRP-5P | verified | Sources open and support claims; selects valid. |
| Robot/Model | Kengoro | verified | Sources open and support claims; selects valid. |
