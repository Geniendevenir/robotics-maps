# Research report: ecosystem slice France / schools, student associations & research labs / exhaustive

- Output: `output/ecosystem_france_schools_student_associations_research_labs.json`
- Counts: 118 organizations (33 Research lab, 38 School, 47 Association), 11 robots/models, 151 sources consulted (122 distinct domains).
- Notion was not read or written. `Used in projects` is not output. `Knowledge nodes` left empty (to be linked later).
- Excluded as already on main (Paris pilot / Europe Software & AI): ISIR, Inria Paris (WILLOW), CEA-List, U2IS, Mines Paris CAOR, École 42, Sorbonne, ENSTA Paris, École polytechnique, CentraleSupélec, Mines Paris, 42AI, Unaite, AMI, LeRobot/Reachy/SO-101 rows. Their student clubs (X-Robot, Club Tech CentraleSupélec, ENSTA Robotique) are new rows.

## Method
- Web search engines are unusable from the VM (Bing/DuckDuckGo/Brave/Google return junk or bot pages via curl), so discovery used primary directories:
  1. CNRS GdR Robotique lab directory (49 labs): https://www.gdr-robotique.org/laboratoires/?list=1
  2. Coupe de France de Robotique team lists 2022 and 2023 (≈100 teams each, with school/structure and website): coupederobotique.fr
  3. Eurobot 2025 results (eurobot.org), PEPR O2R site, Inria team pages, school homepages.
- Every row has at least one source URL that was fetched (HTTP 200) during this session. Rows backed only by a team-list page (no official site reachable) are `To verify` and their Website is `unknown`.
- Saturation check (student clubs): the 2021 list, the 2020 list and the Eurobot teams page added ~4%, ~3% and 0% new engineering-school clubs → saturation reached for clubs. For research labs, saturation was NOT formally reached (no working search engine; GdR directory is dated, some lab sites down).

## Known gaps / for the verifier
- Sites down or bot-blocked: ampere-lab.fr, ism.univ-amu.fr (ISM Marseille not included), imerir.com (IMERIR robotics school not included), inria.fr team pages (Cloudflare-like check), tirrex.fr, maformationrobotique.fr (403; GdR/Evolis national robotics training directory), prairie-institute.fr.
- Not included for lack of robotics evidence on opened pages: ANITI, MIAI, 3IA (only cited as context), LISN, LIX, LAMIH, CRAN, LGP-ENIT, GREYC, LIS.
- Club ↔ school links are from Coupe de France "Structure" columns; Evolutek's EPITA affiliation and Sudriabotik's ESME link are inferred from names/towns (marked To verify).
- Robot release years and prices mostly unknown (null/"unknown") rather than guessed.
- Possible overlap with the parallel "France (outside Paris) / all" slice for NAVER LABS Europe and IRT Jules Verne (kept here as research labs).

## 5-line summary
1. Who leads: LAAS-CNRS (Pinocchio/Crocoddyl, humanoids), LIRMM (mc_rtc), Inria teams (Rainbow/ViSP, DEFROST/SOFA, Flowers, HuCeBot, Larsen, Chroma) and NAVER LABS Europe, networked by the CNRS GdR Robotique and the France 2030 PEPR O2R programme.
2. Where money is: public funding (CNRS/Inria/ANR/France 2030); NAVER LABS Europe and IRT Jules Verne are the only budget-holding non-academic labs in the slice.
3. Where demand is: ~100 student teams a year at the Coupe de France / Eurobot; clubs are strong in mechanics/electronics but almost none do robot learning.
4. Gap/opportunity: free academic open-source building blocks (Pinocchio, ViSP, SOFA, mc_rtc, Microban); mechanics-strong schools (Arts et Métiers, Centrale Nantes) and electronics schools (ENSEA) complement us.
5. Best entry point: join GdR Robotique as students, co-train with Paris clubs (VRAC/ARDIC, INTech, ECEBORG) for the Coupe de France, and invite Rhoban/LAAS/Inria researchers to talk on low-cost robot learning.
