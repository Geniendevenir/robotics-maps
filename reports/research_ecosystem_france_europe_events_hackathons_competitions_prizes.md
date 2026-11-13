# Research report: France + Europe, events, hackathons, competitions & prizes

Slice: `{"region": "France + Europe", "layer": "events, hackathons, competitions & prizes", "depth": "exhaustive"}`
Output: `output/ecosystem_france_europe_events_hackathons_competitions_prizes.json`. It has 43 organizations, 0 new robots/models and 59 sources consulted.

## Method
- Read `devin/playbooks/ecosystem-researcher.md`, `CLAUDE.md` and `schemas/notion-schema.md`. Took the organization names from `output/ecosystem_paris_all.json` and `output/ecosystem_europe_software_ai.json` and checked every row in this output against them. No exact-name duplicates remain.
- Generic search engines were unreliable from the VM: Bing returned junk results, DuckDuckGo returned 202, Brave 429, Mojeek 403 and Google returned an empty page. Discovery therefore relied on:
  - fetching official event sites directly;
  - the Wikipedia search API;
  - ROS Discourse search JSON;
  - Meetup and Luma listings;
  - the GitHub search API and raw READMEs.
- Every URL in `Sources` was opened during this session. Facts I could not confirm on an opened page are written as `unknown`.
- All rows have `Status` = `To verify`. The one exception is Field Robot Event, set to `Draft` because its page content was not readable.

## How rows are modelled
- Recurring events, competitions and prizes are `Type` = `Event`.
- Organisers are separate rows only when they are a durable partner for 42AI: Planète Sciences, euRobotics, RoboCup France, GdR Robotique, euROBIN, UK-RAS, Apérobot and Women in Robotics Paris.
- `Value chain` has no option for events. I used these conventions:
  - `Software & AI` + `Integration` for build-a-robot competitions;
  - `Demand` (+ `Integration`) for trade fairs and startup prizes.
- `Region` is `Paris` only for Paris-anchored items: LeRobot hackathon Paris site, Apérobot, Women in Robotics Paris. ROSCon France is `France` because it moves between cities.

## Robots & Models
No new rows. The events here mostly use custom robots or robots that are already rows in the pilot outputs. For example, the LeRobot hackathon uses `LeRobot` and the SO-101 arm, which belong to Hugging Face rows in the pilot. When syncing, the syncer can add `Used by` = `LeRobot Worldwide Hackathon` to those existing rows. The reverse relation `Used in projects` is not output.

## Key findings (beginner-readable)
1. **Planète Sciences** runs the French ladder of student robot contests: **Coupe de France de Robotique** (5-8 May 2027, La Roche-sur-Yon), which leads to **Eurobot**. This is the most visible way to become known among French engineering-school robotics clubs.
2. **euRobotics** is the European hub: the **ERF** (Birmingham 2027, Athens 2028) and its awards, the **European Robotics League** (The Hague 2026) and the **European Robotics Week**. A local ERW event costs nothing to register.
3. Robot-learning competitions fit the 42AI wedge:
   - **ICRA 2026 Vienna** challenges: LeHome garment manipulation, REAL-I, AgiBot World;
   - **euROBIN** hackathons and coopetitions;
   - the **LeRobot Worldwide Hackathon**, which 42AI already hosted at 42 Paris in June 2025.
4. Prizes and money:
   - **KUKA Innovation Award**: 20k EUR, plus a robot on loan and coaching;
   - **Hello Tomorrow**: 200k EUR equity Grand Prize, Industrial AI & Robotics track;
   - **i-Lab**: French deep-tech grants;
   - **HANNOVER MESSE ROBOTICS AWARD**: 199 EUR entry fee.
5. Paris events: **ROSCon France** (Sorbonne, June 2026), the **Apérobot** monthly meetup (2,138 members, strong in mechanics and electronics) and **Women in Robotics Paris**.

## Relationship opportunities (priority)
1. Re-host the next LeRobot hackathon site at 42 (Hugging Face, already in the pilot data).
2. Enter a team in the Coupe de France de Robotique 2027 and talk to Planète Sciences about mentoring.
3. Submit a talk or demo to ROSCon France. Attend Apérobot to find mechanics and electronics mentors.
4. Target an ICRA or euROBIN robot-learning challenge in the 2027 season.
5. Apply to the KUKA Innovation Award when the theme fits, to get hardware access.

## Excluded / out of slice
- World Robot Olympiad: headquarters in Singapore; national rounds not researched.
- IMAV 2027: in Brazil.
- CoRL 2026: in Austin.
- Innorobo: the site has been frozen since the 2018 edition.
- AMD AI DevMaster Hackathon: location not found.
- Nebius/NVIDIA physical-AI hackathon: only a participant repository was found, not an official event source.

## Known gaps
- Saturation was **not** formally reached because of the ACU budget and search-engine blocking. Likely misses:
  - national RoboCup and Eurobot committees in other countries;
  - Station F / VivaTech robotics side events;
  - regional French hackathons such as school-run robotics hackathons;
  - EU Horizon "open call" competitions;
  - drone competitions in Europe.
- Unverified: city for euRobotics, KUKA Award, World FIRA and Field Robot Event; Planète Sciences address; current activity of METRICS and Challenge ROSE.
