# Verification report: output/ecosystem_france_outside_paris_all.json

Verifier run on branch `research/ecosystem-france-outside-paris-all`. No Notion read/write.

## Summary
- Rows in: 89 organizations + 47 robots/models = 136
- Verified: 128 · Corrected: 8 · Rejected: 0
- Rows out: 136 (all Status = "To verify")
- URLs checked: 128 unique via curl (HTTP: {'200': 118, '000': 6, '503': 3, '403': 1}); every non-200/empty page retried via Chrome CDP. Still dead after retry: poppy-project.org (NXDOMAIN), flowers.inria.fr (no response), websites.isae-supaero.fr/gis-micro-drones (no response), decathlon-united.media (expired TLS cert) — all replaced.
- Dated claims checked against page publish metadata: Naïo €6.4M plan (2025-11-10), AISPRID €10M Series A (2025-01-22), Siparex/Siléane exit (2025-07-09), Exotec Series D (2022-01-17), Nimbl'Bot NB-55/NB-120 (2023-06-20), Naïo Orio/Jo end of sales (2026-06-12), Microduck (2026-08-27).

## Global corrections (all rows)
- Removed non-Notion key `_relationship_reason` from all 89 organizations.
- `Status` set to "To verify" on all rows. No `Used in projects` key present.
- All select/multi-select values checked against schemas/notion-schema.md: no invalid values. All `Built by` / `Used by` names resolve to organizations in this file; no duplicate names in this file or by exact name in other output/*.json files.
- `Size / stage` null kept where unknown (not a valid select value to write "unknown").

## Open issues for the next pass
- Poppy Project: domain dead and GitHub repos archived; consider whether it still belongs in the map as an active community.
- Stäubli: Faverges-Seythenex location not stated on the cited page (staubli.com location pages 403/bot-walled).
- Many company rows rest on a single official homepage (claims are generic product descriptions, confirmed there); funding stage is unknown (null) for most.

## Row-by-row
| Kind | Row | Result | Reason |
|---|---|---|---|
| Org | Pollen Robotics | corrected | Added primary source for the Hugging Face acquisition claim (HF blog); Microduck 25 cm / 27 Aug 2026 / closed hardware design confirmed by press kit + blog. |
| Org | Niryo | verified | Sources open (curl or Chrome CDP) and support claims; selects valid. |
| Org | Génération Robots | verified | Sources open (curl or Chrome CDP) and support claims; selects valid. |
| Org | HumaRobotics | verified | Sources open (curl or Chrome CDP) and support claims; selects valid. |
| Org | Agreenculture | verified | Sources open (curl or Chrome CDP) and support claims; selects valid. |
| Org | Naïo (Naïo Technologies brand) | verified | €6.4M financing plan confirmed in official release dated 2025-11-10; Orio/Jo end-of-sales notice dated 12 Jun 2026 confirmed. |
| Org | VitiBot | verified | Site 503 to curl, opened via CDP: confirms electric vineyard straddle robots (Bakus). |
| Org | Vitirover | verified | Opened via CDP: robots + human teams vegetation-maintenance service confirmed. |
| Org | AISPRID | verified | GO CAPITAL release (2025-01-22) confirms €10M Series A incl. €6.2M dilutive. |
| Org | SITIA | verified | Sources open (curl or Chrome CDP) and support claims; selects valid. |
| Org | Sepro Group | verified | Sources open (curl or Chrome CDP) and support claims; selects valid. |
| Org | Stäubli Robotics France | verified | Official robotics page opens via CDP (403 to curl); Faverges location not stated on the cited page (well-known site, not re-confirmed). |
| Org | Siléane | verified | Sources open (curl or Chrome CDP) and support claims; selects valid. |
| Org | Sherpa Mobile Robotics | verified | Sources open (curl or Chrome CDP) and support claims; selects valid. |
| Org | Effidence | verified | Sources open (curl or Chrome CDP) and support claims; selects valid. |
| Org | Exotec | verified | Series D $335M (Jan 2022) and Skypod made in Croix confirmed on official release. |
| Org | SAVOYE | verified | Official site Feb 2026 news confirms positioning within Noblelift group. |
| Org | Manitou Group | verified | Sources open (curl or Chrome CDP) and support claims; selects valid. |
| Org | Robocath | verified | Sources open (curl or Chrome CDP) and support claims; selects valid. |
| Org | eCential Robotics | verified | Sources open (curl or Chrome CDP) and support claims; selects valid. |
| Org | Quantum Surgical | verified | Official site: "Now part of Precision IO"; Epione confirmed. |
| Org | Delair | verified | Sources open (curl or Chrome CDP) and support claims; selects valid. |
| Org | Dronisos | verified | Sources open (curl or Chrome CDP) and support claims; selects valid. |
| Org | Donecle | verified | Sources open (curl or Chrome CDP) and support claims; selects valid. |
| Org | RTsys | verified | Sources open (curl or Chrome CDP) and support claims; selects valid. |
| Org | Aquitaine Robotics | verified | Sources open (curl or Chrome CDP) and support claims; selects valid. |
| Org | Robotics Place | verified | Sources open (curl or Chrome CDP) and support claims; selects valid. |
| Org | Coboteam | verified | Opened via CDP: regional robotics/cobotics cluster for Auvergne-Rhône-Alpes. |
| Org | Proxinnov | verified | Sources open (curl or Chrome CDP) and support claims; selects valid. |
| Org | Robotics Valley | verified | Sources open (curl or Chrome CDP) and support claims; selects valid. |
| Org | SIDO Lyon | verified | Sources open (curl or Chrome CDP) and support claims; selects valid. |
| Org | World FIRA | verified | Sources open (curl or Chrome CDP) and support claims; selects valid. |
| Org | Coupe de France de Robotique | verified | Official site: organised by Planète Sciences at Parc Expo Les Oudairies, La Roche-sur-Yon. |
| Org | Clubelek (INSA Lyon) | verified | Sources open (curl or Chrome CDP) and support claims; selects valid. |
| Org | GO CAPITAL | verified | Sources open (curl or Chrome CDP) and support claims; selects valid. |
| Org | Kreaxi | verified | BOA Concept portfolio page confirms "IPO en 2021". |
| Org | Siparex | verified | Siparex release (2025-07-09) confirms France Nucléaire 1 exit from Siléane. |
| Org | LAAS-CNRS | verified | Gepetto page (via CDP) + HPP/Pinocchio/Crocoddyl repos confirm. |
| Org | LIRMM | verified | Sources open (curl or Chrome CDP) and support claims; selects valid. |
| Org | LS2N | verified | Sources open (curl or Chrome CDP) and support claims; selects valid. |
| Org | FEMTO-ST | verified | Sources open (curl or Chrome CDP) and support claims; selects valid. |
| Org | ICube | verified | Sources open (curl or Chrome CDP) and support claims; selects valid. |
| Org | Inria Lille – DEFROST | verified | Sources open (curl or Chrome CDP) and support claims; selects valid. |
| Org | LORIA / Inria Nancy – Larsen | verified | Sources open (curl or Chrome CDP) and support claims; selects valid. |
| Org | IRISA / Inria Rennes – Rainbow | verified | Sources open (curl or Chrome CDP) and support claims; selects valid. |
| Org | Inria Bordeaux – Flowers | corrected | flowers.inria.fr unreachable (curl + CDP); Website/Sources -> inria.fr/en/flowers, which confirms curiosity-driven open-ended learning; Poppy link -> GitHub org. |
| Org | Inria Bordeaux – AUCTUS | verified | Sources open (curl or Chrome CDP) and support claims; selects valid. |
| Org | LaBRI – Rhoban | verified | Sources open (curl or Chrome CDP) and support claims; selects valid. |
| Org | Inria Sophia Antipolis – HEPHAISTOS | verified | Sources open (curl or Chrome CDP) and support claims; selects valid. |
| Org | Institut Pascal | verified | Sources open (curl or Chrome CDP) and support claims; selects valid. |
| Org | Heudiasyc | verified | Sources open (curl or Chrome CDP) and support claims; selects valid. |
| Org | GIPSA-lab | verified | Sources open (curl or Chrome CDP) and support claims; selects valid. |
| Org | TIMC | verified | Sources open (curl or Chrome CDP) and support claims; selects valid. |
| Org | Pprime | verified | Sources open (curl or Chrome CDP) and support claims; selects valid. |
| Org | LIG | verified | Sources open (curl or Chrome CDP) and support claims; selects valid. |
| Org | I3S | verified | Sources open (curl or Chrome CDP) and support claims; selects valid. |
| Org | Institut des Sciences du Mouvement Étienne-Jules Marey (ISM) | verified | Sources open (curl or Chrome CDP) and support claims; selects valid. |
| Org | LAB-STICC | verified | Sources open (curl or Chrome CDP) and support claims; selects valid. |
| Org | Poppy Project | corrected | poppy-project.org DNS NXDOMAIN; Website/Sources -> GitHub org/repos (open-source 3D-printed designs confirmed; repos archived, noted in text). |
| Org | Centrale Nantes | verified | Sources open (curl or Chrome CDP) and support claims; selects valid. |
| Org | INSA Lyon | verified | Sources open (curl or Chrome CDP) and support claims; selects valid. |
| Org | INSA Toulouse | verified | Sources open (curl or Chrome CDP) and support claims; selects valid. |
| Org | ISAE-SUPAERO | corrected | Dead source websites.isae-supaero.fr/gis-micro-drones removed (unreachable); replaced by isae-supaero.fr/recherche/. |
| Org | Shark Robotics | verified | Sources open (curl or Chrome CDP) and support claims; selects valid. |
| Org | Haption | verified | Sources open (curl or Chrome CDP) and support claims; selects valid. |
| Org | CEDRAT Technologies | verified | Sources open (curl or Chrome CDP) and support claims; selects valid. |
| Org | Starkenn SilMach Labs (SilMach) | verified | Sources open (curl or Chrome CDP) and support claims; selects valid. |
| Org | SYMÉTRIE | verified | Sources open (curl or Chrome CDP) and support claims; selects valid. |
| Org | MS-Innov | verified | Homepage opened via CDP (503 to curl); MORFOSE brochure PDF confirms modular cobot. |
| Org | Axilum Robotics | verified | Sources open (curl or Chrome CDP) and support claims; selects valid. |
| Org | Notilo Plus | verified | Sources open (curl or Chrome CDP) and support claims; selects valid. |
| Org | Hexadrone | verified | Sources open (curl or Chrome CDP) and support claims; selects valid. |
| Org | Azur Drones | verified | Sources open (curl or Chrome CDP) and support claims; selects valid. |
| Org | Roboplanet | verified | Sources open (curl or Chrome CDP) and support claims; selects valid. |
| Org | Japet Medical | verified | Sources open (curl or Chrome CDP) and support claims; selects valid. |
| Org | Les Companions | verified | Sources open (curl or Chrome CDP) and support claims; selects valid. |
| Org | Capsix Robotics | verified | Sources open (curl or Chrome CDP) and support claims; selects valid. |
| Org | Awabot | verified | Sources open (curl or Chrome CDP) and support claims; selects valid. |
| Org | TwinswHeel | verified | Sources open (curl or Chrome CDP) and support claims; selects valid. |
| Org | Kompaï Robotics | verified | Sources open (curl or Chrome CDP) and support claims; selects valid. |
| Org | FINOVAM Gestion | verified | Sources open (curl or Chrome CDP) and support claims; selects valid. |
| Org | Decathlon | corrected | decathlon-united.media has an expired TLS certificate; Website -> decathlon.com. Exotec release confirms Decathlon as Skypod customer. |
| Org | Nimbl'Bot | verified | Sources open (curl or Chrome CDP) and support claims; selects valid. |
| Org | Eclore Actuators | verified | Sources open (curl or Chrome CDP) and support claims; selects valid. |
| Org | Nio Robotics (Nimble One site) | verified | Sources open (curl or Chrome CDP) and support claims; selects valid. |
| Org | ACWA Robotics | verified | Sources open (curl or Chrome CDP) and support claims; selects valid. |
| Org | E-COBOT | verified | Sources open (curl or Chrome CDP) and support claims; selects valid. |
| Org | IRDI Capital Investissement | verified | Sources open (curl or Chrome CDP) and support claims; selects valid. |
| Org | Sodero | verified | Sources open (curl or Chrome CDP) and support claims; selects valid. |
| Robot/Model | Microduck | verified | Press kit + blog (27 Aug 2026): 25 cm biped, 15 DoF, open software, closed mech/electronic design. |
| Robot/Model | Ned2 | verified | Source opens and supports specs; selects valid; Built by resolves in this file. |
| Robot/Model | GR100 | verified | Source opens and supports specs; selects valid; Built by resolves in this file. |
| Robot/Model | AGC Autonomy Kit | verified | Source opens and supports specs; selects valid; Built by resolves in this file. |
| Robot/Model | Oz | verified | Official page: GNSS RTK, up to 8 h, 60 kg lift, 35+ tools confirmed. |
| Robot/Model | Orio / Jo (discontinued platforms) | verified | Source opens and supports specs; selects valid; Built by resolves in this file. |
| Robot/Model | Bakus | verified | Source opens and supports specs; selects valid; Built by resolves in this file. |
| Robot/Model | Vitirover mowing robot | verified | Source opens and supports specs; selects valid; Built by resolves in this file. |
| Robot/Model | AISPRID leaf-removal robot | verified | Source opens and supports specs; selects valid; Built by resolves in this file. |
| Robot/Model | Sepro 3-axis injection-molding robots | verified | Source opens and supports specs; selects valid; Built by resolves in this file. |
| Robot/Model | SHERPA AMR range | verified | Source opens and supports specs; selects valid; Built by resolves in this file. |
| Robot/Model | EffiBOT | verified | Source opens and supports specs; selects valid; Built by resolves in this file. |
| Robot/Model | Skypod | verified | Source opens and supports specs; selects valid; Built by resolves in this file. |
| Robot/Model | R-One+ | verified | Source opens and supports specs; selects valid; Built by resolves in this file. |
| Robot/Model | eCential integrated surgical platform | verified | Source opens and supports specs; selects valid; Built by resolves in this file. |
| Robot/Model | Epione | verified | Source opens and supports specs; selects valid; Built by resolves in this file. |
| Robot/Model | Donecle automated aircraft inspection system | verified | Source opens and supports specs; selects valid; Built by resolves in this file. |
| Robot/Model | Poppy Humanoid | corrected | poppy-project.org dead (NXDOMAIN); Sources -> archived GitHub repo, Price/access updated. |
| Robot/Model | Poppy Torso | corrected | poppy-project.org dead (NXDOMAIN); Sources -> archived GitHub repo, Price/access updated. |
| Robot/Model | Poppy Ergo Jr | corrected | poppy-project.org dead (NXDOMAIN); Sources -> archived GitHub repo, Price/access updated. |
| Robot/Model | SigmaBan | verified | rhoban.com names SigmaBan and "UltraBan: a human sized humanoid robot". |
| Robot/Model | UltraBan | verified | rhoban.com names SigmaBan and "UltraBan: a human sized humanoid robot". |
| Robot/Model | Humanoid Path Planner (HPP) | verified | GitHub: ISC license, copyright LAAS-CNRS. |
| Robot/Model | Pinocchio | verified | Source opens and supports specs; selects valid; Built by resolves in this file. |
| Robot/Model | Crocoddyl | verified | Source opens and supports specs; selects valid; Built by resolves in this file. |
| Robot/Model | ViSP | verified | Source opens and supports specs; selects valid; Built by resolves in this file. |
| Robot/Model | SOFA | verified | Source opens and supports specs; selects valid; Built by resolves in this file. |
| Robot/Model | C3Bots research prototypes | verified | Source opens and supports specs; selects valid; Built by resolves in this file. |
| Robot/Model | Colossus | verified | Official page: remote-controlled tracked firefighting robot; Form factor N/A acceptable (no tracked option). |
| Robot/Model | MORFOSE | verified | Source opens and supports specs; selects valid; Built by resolves in this file. |
| Robot/Model | TMS-Cobot | verified | Source opens and supports specs; selects valid; Built by resolves in this file. |
| Robot/Model | Seasam | verified | Official site confirms; Form factor "Drone" used for an underwater robot (closest schema option). |
| Robot/Model | iBubble | verified | Official site confirms; Form factor "Drone" used for an underwater robot (closest schema option). |
| Robot/Model | TUNDRA 2 | verified | Source opens and supports specs; selects valid; Built by resolves in this file. |
| Robot/Model | Skeyetech | verified | Source opens and supports specs; selects valid; Built by resolves in this file. |
| Robot/Model | Japet.W+ | verified | Source opens and supports specs; selects valid; Built by resolves in this file. |
| Robot/Model | PACO | verified | Source opens and supports specs; selects valid; Built by resolves in this file. |
| Robot/Model | iYU | verified | Source opens and supports specs; selects valid; Built by resolves in this file. |
| Robot/Model | ciTHy S | verified | Official site: follows a person carrying up to 50 kg, autonomous return/delivery. |
| Robot/Model | Delair UX11 | verified | Source opens and supports specs; selects valid; Built by resolves in this file. |
| Robot/Model | Notilo Cloud | verified | Source opens and supports specs; selects valid; Built by resolves in this file. |
| Robot/Model | NB-55 | verified | Source opens and supports specs; selects valid; Built by resolves in this file. |
| Robot/Model | NB-120 | verified | IRDI release dated 20/06/2023 names NB-55 and NB-120 as functional prototypes. |
| Robot/Model | Aru | verified | Official site: rover/snake/quadruped modes, magnetic feet confirmed. |
| Robot/Model | Pathfinder | verified | Source opens and supports specs; selects valid; Built by resolves in this file. |
| Robot/Model | HUSKY (E-COBOT) | verified | Source opens and supports specs; selects valid; Built by resolves in this file. |
| Robot/Model | MyCobot Suite | verified | Source opens and supports specs; selects valid; Built by resolves in this file. |
