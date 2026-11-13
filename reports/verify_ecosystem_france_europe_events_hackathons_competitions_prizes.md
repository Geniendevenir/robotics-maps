# Verification report: ecosystem_france_europe_events_hackathons_competitions_prizes

Method: every Website and Sources URL fetched with curl (all returned 200 except roscon.fr 503 and robocup.de over https; robocup.de confirmed over http); key claims grepped from page text; select values checked against schemas/notion-schema.md. `_relationship_reason` keys removed (not Notion fields); Status set to "To verify"; `robots_models` was empty.

Totals: 43 rows -> 41 kept; rejected 2; corrected 12; verified 29.

| Organization | Result | Reason |
|---|---|---|
| Coupe de France de Robotique | verified | 2026 13-16 May and 2027 5-8 May at Parc Expo Les Oudairies, La Roche-sur-Yon; Junior + Legends categories confirmed. |
| Eurobot | verified | Created 1998, international amateur contest, Eurobot Junior confirmed on eurobot.org. |
| Planète Sciences | verified | National association, Evry-Courcouronnes address and robotics activities confirmed. |
| euRobotics | verified | Official site eu-robotics.net runs ERF, ERW, ERL, awards. |
| European Robotics Forum (ERF) | verified | Stavanger 2026, Birmingham 2027, Athens 2028; early bird until 1 Dec 2026 confirmed. |
| euRobotics Awards | verified | TechTransfer, Renaud Champion, Georges Giralt PhD awards + Sustainability Leadership Recognition confirmed. |
| European Robotics Week (ERW) | verified | Official ERW page loads. |
| European Robotics League (ERL) | verified | ERL 2026 13-15 May 2026, Scheveningen/The Hague confirmed. |
| IEEE ICRA 2026 (Vienna) and its competitions | verified | All 9 listed competitions confirmed on competitions page. |
| Robotics: Science and Systems (RSS) 2027 | verified | 23rd RSS, Athens, 6-11 July 2027 confirmed. |
| automatica (Munich) | verified | 22-25 June 2027 and munich_i confirmed. |
| HANNOVER MESSE and ROBOTICS AWARD | verified | 5-8 April 2027; award open to exhibitors or not; 199 EUR + VAT via Alpha Awards confirmed. |
| KUKA Innovation Award | verified | EUR 20,000 prize, robot free of charge, 2025 Medical Robotics Challenge 2.0, 2026 Circular Packaging Challenge confirmed. |
| LogiMAT | verified | Stuttgart Trade Fair Centre, 16-18 March 2027 confirmed. |
| SIDO Lyon | corrected | 'unknown' is not a valid Size / stage option; left empty. |
| Robotics & Automation UK (with IntraLogisteX) | corrected | 'unknown' is not a valid Size / stage option; left empty. |
| ROSCon France | corrected | roscon.fr returned HTTP 503; removed unverified 'Toulouse 2022' claim; venue per Discourse is Jussieu (Sorbonne Université campus). |
| GdR Robotique (CNRS) | verified | Journées 2026, JNRR and Défi Transfert Robotique pages confirmed. |
| RoboCup 2027 (Nuremberg) | corrected | robocup.org homepage does not show the 2027 dates; dates/venue confirmed on robocup.de (http) and source replaced. |
| RoboCup German Open | verified | GermanOpen 2026 10-14 March Cologne; junior finals 9-12 March 2027 Nuremberg confirmed (robocup.de reachable only over http). |
| RoboCup France | verified | robocup.fr lists RoboCup Junior Soccer/Rescue/Onstage. |
| CYBATHLON | corrected | Official site says CYBATHLON is 'taking a strategic pause' after 2024; description updated. |
| ELROB (European Land Robot Trial) | verified | 15-19 June 2026 Thun; Fraunhofer FKIE judge confirmed. |
| EnRicH (European Robotics Hackathon) | verified | EnRicH 2027 Zwentendorf, 3-9 July 2027, nuclear scenarios confirmed. |
| European Rover Challenge | verified | 124 teams, 29 countries, ~3756 participants (2026) confirmed. |
| Robotex International | verified | Founded 2001 TalTech Tallinn, 17+ countries, 150,000+ participants confirmed. |
| Formula Student Germany - Driverless Cup | verified | FSG 2026 results and Driverless Cup pages exist. |
| Hello Tomorrow Challenge | corrected | Page states a EUR 200,000 Grand Prize; the 'equity' form is not stated, removed. |
| i-Lab (Concours d'innovation) | corrected | Added grant ceiling from Bpifrance page (max 600 kEUR subvention). |
| AI for Good Global Summit and Robotics for Good Youth Challenge | verified | Summit 7-10 July 2026 Geneva; 75 chapters/50 countries/18,000 participants/2,000 teams; 2027 Summit listed. |
| METRICS (EU robot evaluation competitions) | rejected | H2020 project whose site still speaks in future tense and shows no 2024-2026 activity; competitions are finished, not an active 2026 opportunity. |
| euROBIN | verified | Competitions, Hackathons, Coopetitions sections confirmed. |
| Challenge ROSE | rejected | Programme ended: latest news is the 27 Mar 2023 closing webinar ('webinaire de clôture'); not active in 2026. |
| WorldSkills France | verified | Trades list includes 'Intégration Robotique' (mobile robotics wording not seen but plausible). |
| ESA-ESRIC Space Resources Challenge | verified | ESRIC site lists 'ESA & ESRIC Challenge'. |
| LeRobot Worldwide Hackathon | verified | 14-15 June 2025 online+local; 42AI Paris site at 96 bd Bessières; AMD AI DevMaster post dated 14 July 2026. |
| Humanoids Summit London | corrected | 'unknown' is not a valid Size / stage option; left empty. |
| Physical AI Hackathon (Robotics Nation, Helsinki) | corrected | 'unknown' is not a valid Size / stage option; left empty. |
| Apérobot | verified | 2,138 members, 133 past events, Discord editions, 'Robot Party au Rendez-vous des Makers' confirmed. |
| Women in Robotics Paris | corrected | luma.com/paris is a generic Luma city listing, not an official site; Website set to womeninrobotics.org (chapters page); event host is 'Women In Robotics - France'. |
| UK-RAS Network | verified | UK-RAS Showcase 7 Jan 2027 confirmed. |
| World FIRA | corrected | 'unknown' is not a valid Size / stage option; left empty. |
| Field Robot Event | corrected | Page (gzip) read: global student competition for autonomous agricultural robots; 2027 edition at University of Lincoln (UK). |
