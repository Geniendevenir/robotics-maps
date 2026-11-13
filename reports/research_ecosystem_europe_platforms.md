# Research report: Ecosystem slice Europe / Platforms (top 20)

Output: `output/ecosystem_europe_platforms.json` (20 organizations, 22 robots/models, 57 distinct source URLs).

## Scope and method
- Slice: European organizations whose main business is building robot **platforms** (complete robots: arms, humanoids, quadrupeds, mobile manipulators, AMRs, drones, surgical robots). Pure software/AI firms, component suppliers and integrators were left out unless they also ship a platform.
- De-duplication: excluded every organization already in `output/ecosystem_paris_all.json` and `output/ecosystem_europe_software_ai.json` (e.g. Wandercraft and Hugging Face are already in the Paris file). ANYmal (the older robot) was already listed in the Software & AI file; only the new ANYmal X was added.
- Discovery: Google News RSS queries (Bing/DuckDuckGo HTML are unreliable on this VM) on funding, launches and deployments 2024-2026, by country (DE, CH, DK, ES, IT, NL, SE, UK, EE) and by form factor (humanoid, cobot, quadruped, surgical, delivery, drone).
- Opening sources: `curl` for most pages; Chrome over CDP (`localhost:29229`) for sites that block scripts (anybotics.com, shadowrobot.com, engineeredarts.com, franka.de, pal-robotics.com, icub.iit.it, robotics.hexagon.com, news sites). Every row has at least one opened URL; official site first whenever it loaded.
- Ranking for "top 20": a mix of size/funding (KUKA, ABB, UR, NEURA, Agile), technical reference value for a robot-learning lab (Franka FR3, PAL TIAGo Pro, Shadow Hand, iCub) and 2026 momentum (Theker, Generative Bionics, RobCo, Hexagon AEON).

## Findings (for beginners)
1. **Germany leads.** NEURA Robotics (Series C up to $1.4B, June 2026; 4NE1 Gen 4 humanoid and Neuron AI model, Oct 2026), Agile Robots ($500M at $8.5B led by SoftBank, Nov 2026; owns Franka), RobCo ($1B valuation, Oct 2026), KUKA (~€3.9B sales) and Quantum Systems (defense drones, $8B valuation).
2. **Incumbent arm makers are adding "physical AI".** Universal Robots launched Gen 7 and an imitation-learning "UR AI Trainer" with Scale AI; KUKA and Comau announced Nvidia partnerships. Imitation learning (the LeRobot idea) is becoming mainstream in industry.
3. **Humanoids are the money magnet.** NEURA, Agile ONE, Hexagon AEON (Schaeffler: 1,000 units by 2032), Generative Bionics (€70M, IIT spin-off), igus Iggy Rob (€47,999), Engineered Arts Ameca (social), Theker (reconfigurable generalist, $85M Series A).
4. **Research reference platforms come from Europe.** Franka Research 3 (the arm in many robot-learning datasets), PAL TIAGo Pro, Shadow Dexterous Hand / DEX-EE (with Google DeepMind), IIT iCub (open-source humanoid).
5. **Real deployments**: Starship (10M+ sidewalk deliveries, ~3,000 robots), ANYbotics (ANYmal X for explosive sites, first customers Equinor and DSM-Firmenich), CMR Surgical (45,000+ patients; Stryker ~$400M with acquisition option).
6. **ABB Robotics ownership is uncertain**: sale to SoftBank blocked by China for the China business (5 Nov 2026).

## Hypothesis check (low-cost robot learning wedge)
European platform makers almost all sell expensive hardware (tens of thousands of euros or more). The only budget-compatible European arm found is igus ReBeL (~$6.9k in 2023). This does not contradict the low-cost wedge (SO-101/LeRobot): it means these firms are useful as **references, speakers and partners**, not as suppliers. Their move toward imitation learning (UR AI Trainer, Neuron AI) shows the skills the lab would build are in demand.

## Best entry points for the lab
- **PAL Robotics**: research-friendly, French office in Toulouse; joint project, demo or academic deal.
- **igus**: low-cost arms and humanoid, targets universities; ask for a sponsored/discounted ReBeL.
- **Franka Robotics**: community forum and webinars; academic access to FR3.
- **Engineered Arts**: Ameca can be rented for an event (visibility).
- **IIT iCub**: open-source community, summer schools, EU projects.
- Talks: NEURA, ANYbotics, RobCo, Theker, Shadow Robot.
All partnership terms are **unknown** (no programme was verified).

## Limits and items to verify
- Rows marked `To verify`: Agile Robots (funding sourced partly from a crypto-news aggregator plus Yahoo/Reuters syndication), ANYbotics (2025 raise page blocked), PAL Robotics (stage), Engineered Arts and Shadow Robot (size unknown), igus (official site not loaded; facts from The Robot Report), Generative Bionics (official site behind Cloudflare), plus several robots whose specs/prices were not on an opened page.
- Hexagon Robotics city is `unknown` (HQ not on opened pages). `Size / stage` is `unknown` for Engineered Arts and Shadow Robot.
- igus Website (`https://www.igus.eu`) and Theker/Generative Bionics domains were confirmed by redirect/title only.
- Saturation was **not formally reached**: the last discovery passes (country-level 2026 funding queries) still surfaced smaller candidates not included in the top 20, e.g. Beyond Vision, Tekever (drones, PT), Nature Robots, Versatile RobotX, Jaipur Robotics, Milrem Robotics (EE, defense UGVs, THeMIS; dropped for space), DLR RMC (TORO humanoid, research). A follow-up run could cover drones/defense and agri platforms more deeply.
- Hiring was not researched (out of scope). Notion was not read or written.
