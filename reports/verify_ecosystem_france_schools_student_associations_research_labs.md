# Verification report: output/ecosystem_france_schools_student_associations_research_labs.json

Verifier run on branch `research/ecosystem-france-schools-student-associations-research-labs` (input commit 25c0a20). No Notion read/write.

## Summary
- Rows in: 118 organizations + 11 robots/models = 129
- Verified: 122 · Corrected: 7 · Rejected: 0
- Rows out: 129 (all with Status = "To verify")
- URLs checked: 200 unique (first pass: {'200': 193, '000': 7}). The 7 timeouts (davincibot.org, europe.naverlabs.com x2, ifremer.fr, isep.fr x2, telecom-paris.fr) were retried: all load except https://davincibot.org (http:// works, Website fixed).
- Every row's name was found in the text of at least one of its cited sources; every Coupe de France club was found in the cited team list(s) with its structure and city.

## Global corrections (all rows)
- Removed non-Notion key `_relationship_reason` from all 118 organizations (keys must be exactly Notion field names). Original text remains in commit 25c0a20.
- `Website` = "unknown" set to empty (null) on 30 rows (url field). Text fields keep "unknown".
- `Status` set to "To verify" on all rows (87 were "Draft"). No "Used in projects" key present.
- All select / multi-select values checked against schemas/notion-schema.md: no invalid values. All `Built by` / `Used by` names resolve to organizations in this file. No duplicate organizations.

## Open issues for the next pass
- Activity in 2026 of student clubs: coupederobotique.fr publishes team lists only up to 2023 (2024-2026 list URLs 404), so most clubs are confirmed active only up to 2022-2023. VRAC is confirmed via Eurobot 2025 podium. Robotech Montpellier is cited only from the 2021 list.
- Evolutek: EPITA affiliation still unconfirmed (no club website found).
- Ampère: no official website found (ampere-lab.fr did not load); Website left empty.
- "Hackathon host" is assigned to nearly every student club by default; plausible as inter-club events but not evidenced per club.
- GdR Robotique figures (49 labs, 3,249 members, 1,438 students) confirmed on gdr-robotique.org as of the check; they change over time.

## Row-by-row
| Kind | Row | Result | Reason |
|---|---|---|---|
| Org | LAAS-CNRS | verified | Sources open (HTTP 200) and support name/claims; selects valid. |
| Org | LIRMM (Robotics department) | verified | Sources open (HTTP 200) and support name/claims; selects valid. |
| Org | Inria Rainbow (IRISA, Rennes) | verified | Sources open (HTTP 200) and support name/claims; selects valid. |
| Org | Inria DEFROST (Lille) | verified | Sources open (HTTP 200) and support name/claims; selects valid. |
| Org | Inria Flowers (Bordeaux) | verified | Sources open (HTTP 200) and support name/claims; selects valid. |
| Org | Inria Larsen (LORIA, Nancy) | verified | Sources open (HTTP 200) and support name/claims; selects valid. |
| Org | Inria HuCeBot (Nancy) | verified | Sources open (HTTP 200) and support name/claims; selects valid. |
| Org | Inria Auctus (Bordeaux) | verified | Sources open (HTTP 200) and support name/claims; selects valid. |
| Org | Inria Chroma | verified | Sources open (HTTP 200) and support name/claims; selects valid. |
| Org | Inria Acentauri (Sophia Antipolis) | verified | Sources open (HTTP 200) and support name/claims; selects valid. |
| Org | Rhoban (LaBRI, Bordeaux) | verified | Sources open (HTTP 200) and support name/claims; selects valid. |
| Org | LS2N | verified | Sources open (HTTP 200) and support name/claims; selects valid. |
| Org | ICube (Strasbourg) | verified | Sources open (HTTP 200) and support name/claims; selects valid. |
| Org | Heudiasyc (UTC) | verified | Sources open (HTTP 200) and support name/claims; selects valid. |
| Org | Institut Pascal | verified | Sources open (HTTP 200) and support name/claims; selects valid. |
| Org | GIPSA-lab | verified | Sources open (HTTP 200) and support name/claims; selects valid. |
| Org | FEMTO-ST – AS2M department | verified | Sources open (HTTP 200) and support name/claims; selects valid. |
| Org | Institut Pprime | verified | Sources open (HTTP 200) and support name/claims; selects valid. |
| Org | LISV (UVSQ / Paris-Saclay) | verified | Sources open (HTTP 200) and support name/claims; selects valid. |
| Org | IBISC (Univ. Évry / Paris-Saclay) | verified | Sources open (HTTP 200) and support name/claims; selects valid. |
| Org | I3S (Université Côte d'Azur) | verified | Sources open (HTTP 200) and support name/claims; selects valid. |
| Org | MIS (UPJV Amiens) | verified | Sources open (HTTP 200) and support name/claims; selects valid. |
| Org | LISPEN (Arts et Métiers) | verified | Sources open (HTTP 200) and support name/claims; selects valid. |
| Org | CESI LINEACT | verified | Sources open (HTTP 200) and support name/claims; selects valid. |
| Org | ONERA – DTIS | verified | Sources open (HTTP 200) and support name/claims; selects valid. |
| Org | Lab-STICC | verified | Sources open (HTTP 200) and support name/claims; selects valid. |
| Org | TIMC (Grenoble) | verified | Sources open (HTTP 200) and support name/claims; selects valid. |
| Org | CRIStAL (Lille) | verified | Sources open (HTTP 200) and support name/claims; selects valid. |
| Org | Ampère | verified | Sources open (HTTP 200) and support name/claims; selects valid. | format: Website "unknown" -> empty (url field) |
| Org | IFREMER | verified | Sources open (HTTP 200) and support name/claims; selects valid. |
| Org | NAVER LABS Europe | verified | Sources open (HTTP 200) and support name/claims; selects valid. |
| Org | IRT Jules Verne | verified | Sources open (HTTP 200) and support name/claims; selects valid. |
| Org | PEPR O2R (Organic Robotics programme) | corrected | "7 challenges" -> 3 scientific challenges + 7 targeted projects (€34M) per pepr-o2r.fr; unsourced "piloted by CNRS" dropped; removed utc.fr source (no O2R mention) |
| Org | GdR Robotique (CNRS research network) | verified | Sources open (HTTP 200) and support name/claims; selects valid. |
| Org | Centrale Nantes | verified | Sources open (HTTP 200) and support name/claims; selects valid. |
| Org | Arts et Métiers (ENSAM) | verified | Sources open (HTTP 200) and support name/claims; selects valid. |
| Org | Télécom Paris (IP Paris) | verified | Sources open (HTTP 200) and support name/claims; selects valid. |
| Org | ENS Paris-Saclay | verified | Sources open (HTTP 200) and support name/claims; selects valid. |
| Org | Université Paris-Saclay | corrected | removed U2IS from lab list (U2IS belongs to ENSTA Paris / IP Paris, not Paris-Saclay; no source cited it) |
| Org | Grenoble INP – UGA | verified | Sources open (HTTP 200) and support name/claims; selects valid. |
| Org | INSA Lyon | verified | Sources open (HTTP 200) and support name/claims; selects valid. |
| Org | INSA Toulouse | verified | Sources open (HTTP 200) and support name/claims; selects valid. |
| Org | INSA Rennes | verified | Sources open (HTTP 200) and support name/claims; selects valid. |
| Org | INSA Strasbourg | verified | Sources open (HTTP 200) and support name/claims; selects valid. |
| Org | UTC – Université de technologie de Compiègne | verified | Sources open (HTTP 200) and support name/claims; selects valid. |
| Org | UTT – Université de technologie de Troyes | verified | Sources open (HTTP 200) and support name/claims; selects valid. |
| Org | IMT Atlantique | verified | Sources open (HTTP 200) and support name/claims; selects valid. |
| Org | IMT Nord Europe | verified | Sources open (HTTP 200) and support name/claims; selects valid. |
| Org | Bordeaux INP (ENSEIRB-MATMECA, ENSC) | verified | Sources open (HTTP 200) and support name/claims; selects valid. |
| Org | Université de Montpellier / Polytech Montpellier | verified | Sources open (HTTP 200) and support name/claims; selects valid. |
| Org | Clermont Auvergne INP (incl. SIGMA Clermont) | verified | Sources open (HTTP 200) and support name/claims; selects valid. |
| Org | ISAE-SUPAERO | verified | Sources open (HTTP 200) and support name/claims; selects valid. |
| Org | ENAC | verified | Sources open (HTTP 200) and support name/claims; selects valid. |
| Org | Toulouse INP – ENSEEIHT | verified | Sources open (HTTP 200) and support name/claims; selects valid. |
| Org | EPITA | verified | Sources open (HTTP 200) and support name/claims; selects valid. |
| Org | ESILV (Pôle Léonard de Vinci) | verified | Sources open (HTTP 200) and support name/claims; selects valid. |
| Org | ECE Paris | verified | Sources open (HTTP 200) and support name/claims; selects valid. |
| Org | ESIEA | verified | Sources open (HTTP 200) and support name/claims; selects valid. |
| Org | Efrei | verified | Sources open (HTTP 200) and support name/claims; selects valid. |
| Org | ESME | verified | Sources open (HTTP 200) and support name/claims; selects valid. |
| Org | ESTACA | verified | Sources open (HTTP 200) and support name/claims; selects valid. |
| Org | ENSEA | verified | Sources open (HTTP 200) and support name/claims; selects valid. |
| Org | Isep | verified | Sources open (HTTP 200) and support name/claims; selects valid. |
| Org | Epitech | verified | Sources open (HTTP 200) and support name/claims; selects valid. |
| Org | CESI | verified | Sources open (HTTP 200) and support name/claims; selects valid. |
| Org | ESEO | verified | Sources open (HTTP 200) and support name/claims; selects valid. |
| Org | ESTIA | verified | Sources open (HTTP 200) and support name/claims; selects valid. |
| Org | École Centrale de Lyon | verified | Sources open (HTTP 200) and support name/claims; selects valid. |
| Org | Centrale Méditerranée | verified | Sources open (HTTP 200) and support name/claims; selects valid. |
| Org | Télécom Saint-Étienne | verified | Sources open (HTTP 200) and support name/claims; selects valid. |
| Org | ISAE-ENSMA | verified | Sources open (HTTP 200) and support name/claims; selects valid. |
| Org | Université Côte d'Azur | verified | Sources open (HTTP 200) and support name/claims; selects valid. |
| Org | VRAC (ARDIC – IUT Cachan alumni) | verified | Listed in cited Coupe de France team list(s) with matching structure/city; selects valid. | format: Website "unknown" -> empty (url field) |
| Org | Planète Sciences | verified | Listed in cited Coupe de France team list(s) with matching structure/city; selects valid. |
| Org | Poppy Station | verified | Sources open (HTTP 200) and support name/claims; selects valid. |
| Org | Electrolab | verified | Listed in cited Coupe de France team list(s) with matching structure/city; selects valid. | format: Website "unknown" -> empty (url field) |
| Org | RCVA | verified | Sources open (HTTP 200) and support name/claims; selects valid. |
| Org | MiAM Robotique | verified | Listed in cited Coupe de France team list(s) with matching structure/city; selects valid. |
| Org | PM-ROBOTIX | verified | Listed in cited Coupe de France team list(s) with matching structure/city; selects valid. |
| Org | X-Robot (École polytechnique) | verified | Listed in cited Coupe de France team list(s) with matching structure/city; selects valid. | format: Website "unknown" -> empty (url field) |
| Org | Club Tech CentraleSupélec | verified | Listed in cited Coupe de France team list(s) with matching structure/city; selects valid. | format: Website "unknown" -> empty (url field) |
| Org | ENSTA Robotique (ENSTAR) | verified | Listed in cited Coupe de France team list(s) with matching structure/city; selects valid. | format: Website "unknown" -> empty (url field) |
| Org | Télécom Robotic | verified | Listed in cited Coupe de France team list(s) with matching structure/city; selects valid. | format: Website "unknown" -> empty (url field) |
| Org | INTech | verified | Listed in cited Coupe de France team list(s) with matching structure/city; selects valid. |
| Org | Evolutek | verified | Listed in cited Coupe de France team list(s) with matching structure/city; selects valid. | format: Website "unknown" -> empty (url field) |
| Org | DaVinciBot (ESILV) | corrected | https://davincibot.org times out; http://davincibot.org loads (DaVinciBot site) -> Website set to http URL |
| Org | ECEBORG | verified | Sources open (HTTP 200) and support name/claims; selects valid. |
| Org | Crobot'ic (EFREI Robotique) | verified | Listed in cited Coupe de France team list(s) with matching structure/city; selects valid. | format: Website "unknown" -> empty (url field) |
| Org | Sudriabotik (ESME) | verified | Listed in cited Coupe de France team list(s) with matching structure/city; selects valid. | format: Website "unknown" -> empty (url field) |
| Org | SiERA (ESTACA) | verified | Listed in cited Coupe de France team list(s) with matching structure/city; selects valid. | format: Website "unknown" -> empty (url field) |
| Org | ARES ENSEA | verified | Listed in cited Coupe de France team list(s) with matching structure/city; selects valid. |
| Org | Robotium (ECAM-EPMI) | verified | Listed in cited Coupe de France team list(s) with matching structure/city; selects valid. |
| Org | IUT Cachan CRAC | verified | Listed in cited Coupe de France team list(s) with matching structure/city; selects valid. | format: Website "unknown" -> empty (url field) |
| Org | Eirbot (ENSEIRB-MATMECA) | verified | Listed in cited Coupe de France team list(s) with matching structure/city; selects valid. |
| Org | 7Robot (ENSEEIHT) | verified | Listed in cited Coupe de France team list(s) with matching structure/city; selects valid. |
| Org | Club Robot INSA Toulouse | verified | Listed in cited Coupe de France team list(s) with matching structure/city; selects valid. |
| Org | Club Robotique de Supaéro | verified | Listed in cited Coupe de France team list(s) with matching structure/city; selects valid. | format: Website "unknown" -> empty (url field) |
| Org | ENAC Robotique | verified | Listed in cited Coupe de France team list(s) with matching structure/city; selects valid. | format: Website "unknown" -> empty (url field) |
| Org | ClubElek (INSA Lyon) | verified | Listed in cited Coupe de France team list(s) with matching structure/city; selects valid. |
| Org | Robotronik (Grenoble INP Phelma) | verified | Listed in cited Coupe de France team list(s) with matching structure/city; selects valid. |
| Org | Polybot Grenoble | verified | Listed in cited Coupe de France team list(s) with matching structure/city; selects valid. |
| Org | RobotESEO | verified | Listed in cited Coupe de France team list(s) with matching structure/city; selects valid. |
| Org | Atlantic Robotic Club (IMT Atlantique) | verified | Listed in cited Coupe de France team list(s) with matching structure/city; selects valid. | format: Website "unknown" -> empty (url field) |
| Org | Club Robotique ENSTA Bretagne | verified | Listed in cited Coupe de France team list(s) with matching structure/city; selects valid. | format: Website "unknown" -> empty (url field) |
| Org | CRIS – Club de Robotique de l'INSA de Strasbourg | verified | Listed in cited Coupe de France team list(s) with matching structure/city; selects valid. | format: Website "unknown" -> empty (url field) |
| Org | Robotik UTT | verified | Listed in cited Coupe de France team list(s) with matching structure/city; selects valid. | format: Website "unknown" -> empty (url field) |
| Org | EsialRobotik | verified | Listed in cited Coupe de France team list(s) with matching structure/city; selects valid. | format: Website "unknown" -> empty (url field) |
| Org | Robotech Nancy (Polytech Nancy) | verified | Listed in cited Coupe de France team list(s) with matching structure/city; selects valid. | format: Website "unknown" -> empty (url field) |
| Org | Robotech Montpellier | verified | Listed in cited Coupe de France team list(s) with matching structure/city; selects valid. | format: Website "unknown" -> empty (url field) |
| Org | Club Robot ECM (E-Gab) | verified | Listed in cited Coupe de France team list(s) with matching structure/city; selects valid. | format: Website "unknown" -> empty (url field) |
| Org | AREM (ISMIN) | verified | Listed in cited Coupe de France team list(s) with matching structure/city; selects valid. | format: Website "unknown" -> empty (url field) |
| Org | Projet & Tech' (Télécom Saint-Étienne) | verified | Listed in cited Coupe de France team list(s) with matching structure/city; selects valid. | format: Website "unknown" -> empty (url field) |
| Org | Association Robotique INSA Rouen (ARI) | verified | Listed in cited Coupe de France team list(s) with matching structure/city; selects valid. | format: Website "unknown" -> empty (url field) |
| Org | Esigelectronix (ESIGELEC) | verified | Listed in cited Coupe de France team list(s) with matching structure/city; selects valid. | format: Website "unknown" -> empty (url field) |
| Org | Club Robotik ENSIL | verified | Listed in cited Coupe de France team list(s) with matching structure/city; selects valid. | format: Website "unknown" -> empty (url field) |
| Org | Ensma Space Project (Ensmasteel) | verified | Listed in cited Coupe de France team list(s) with matching structure/city; selects valid. | format: Website "unknown" -> empty (url field) |
| Org | ERAA (ESIPE Robotics & Automation Association) | verified | Listed in cited Coupe de France team list(s) with matching structure/city; selects valid. | format: Website "unknown" -> empty (url field) |
| Org | ESTIA SYSTEM | verified | Listed in cited Coupe de France team list(s) with matching structure/city; selects valid. | format: Website "unknown" -> empty (url field) |
| Robot/Model | Pinocchio | verified | Sources open (HTTP 200) and support name/claims; selects valid. |
| Robot/Model | Crocoddyl | corrected | license confirmed BSD-3-Clause on GitHub; removed "verify" |
| Robot/Model | Pyrène (TALOS humanoid) | verified | Sources open (HTTP 200) and support name/claims; selects valid. |
| Robot/Model | ViSP | verified | Sources open (HTTP 200) and support name/claims; selects valid. |
| Robot/Model | SOFA | corrected | sofa-framework.org confirms v26.06; "July 2026" release month not found on cited pages, removed |
| Robot/Model | mc_rtc | verified | Sources open (HTTP 200) and support name/claims; selects valid. |
| Robot/Model | SigmaBan | verified | Sources open (HTTP 200) and support name/claims; selects valid. |
| Robot/Model | Microban | verified | Sources open (HTTP 200) and support name/claims; selects valid. |
| Robot/Model | Poppy robots (Poppy Humanoid / Ergo Jr) | verified | Sources open (HTTP 200) and support name/claims; selects valid. |
| Robot/Model | DUSt3R | corrected | license confirmed CC BY-NC-SA 4.0 (non-commercial) in repo README |
| Robot/Model | Solo (ODRI open quadruped) | corrected | ODRI site credits the Gepetto team at LAAS/CNRS; replaced "LAAS involvement to verify" |
