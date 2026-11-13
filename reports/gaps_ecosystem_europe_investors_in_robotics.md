# Coverage gaps: Europe / Investors in robotics (top 20)

Reviewed 2026-11-13 against `devin/playbooks/coverage-critic.md`, `CLAUDE.md`, `schemas/notion-schema.md` and `reports/verify_ecosystem_europe_investors_in_robotics.md`. Input: 20 investor organizations + 7 portfolio robots/models (verified). No rows added or edited; Notion not accessed.

**Result: 7 High / 8 Medium / 6 Low (21 gaps).** The slice is a top 20, so these are swap or extension candidates for a targeted re-run, not a request to grow the file to 41 rows.

## Method and references
- Canonical references: 2025-2026 funding announcements for the largest European robotics rounds (Sereact, Humanoid, RobCo, Quantum Systems, Agile Robots, Allonic, Neuracore, SE3, Jaipur Robotics, Six Robotics), fund-close announcements (Seedcamp, Lakestar, DTCP, Entourage), and the researcher's own runner-up list. Found via Google News RSS and read through Chrome CDP. Dealroom/Crunchbase investor rankings were not accessible (paywalled or no investor list for this query), so the canonical set is "who led or joined the big 2025-2026 European robotics rounds".
- Each gap name was checked against the full input JSON and the Paris pilot exclusions (Bpifrance, Supernova Invest, Sofinnova, Kima). None of them appear.
- By design, non-European leads (Prime Movers Lab for Humanoid $152M, SoftBank for Agile Robots $500M Series F on 12 Nov 2026, Blackstone/Advent/Airbus/Noteus for Quantum Systems $1.2B, Lightspeed for RobCo, CRV for THEKER) are out of scope and **not** counted as gaps.
- Importance: **High** = a European investor that led a 2025-2026 European robotics round or launched a physical-AI/robotics fund, with a clear entry path for the lab (Paris-reachable, robot-learning thesis, or a category the map is missing entirely). **Medium** = credible participant or thesis without a confirmed lead. **Low** = public/fund-of-funds money, old evidence, or a narrow niche.

## High (7)
- **H1 Earlybird Venture Capital (Berlin):** led Neuracore's $3M pre-seed (London robot-learning infrastructure, Hugging Face's Clem Delangue participating, free academic programme). Closest investor match to the robot-learning wedge. [tech.eu 2025-11-27](https://tech.eu/2025/11/27/neuracore-raises-3m-to-power-next-gen-robots-and-open-robotics-research/)
- **H2 Seedcamp (London):** $320M across two funds (Jun 2026), with physical AI named a key focus. Ticket sizes up to $1.3M; existing SE3 investor. The most realistic first-check investor for student spin-outs. [Yahoo Finance/Sifted](https://finance.yahoo.com/technology/ai/articles/seedcamp-eyes-physical-ai-320m-070000852.html), [Trending Topics](https://www.trendingtopics.eu/se3-30-million-series-a-accel/)
- **H3 Visionaries Club (Berlin):** led Allonic's record $7.2M pre-seed (robot-body manufacturing, angels from OpenAI/Hugging Face; PROTOTYPE, already in the map, also invested). [The Recursive 2026-02-10](https://www.therecursive.com/allonic-record-pre-seed-robotics-manufacturing/)
- **H4 Lakestar (Zurich/Berlin):** $300M Resilience Fund I (Jul 2026), led SE3's €5.5M seed (TUM spatial-AI for autonomous systems), seed investor in ARX Robotics; the researcher also saw it in Dexory. It is in the researcher's runner-up list but has stronger evidence than several retained rows. [Tectonic Defense](https://www.tectonicdefense.com/lakestar-raises-300m-resilience-fund-i/), [Trending Topics](https://www.trendingtopics.eu/se3-30-million-series-a-accel/)
- **H5 High-Tech Gründerfonds (HTGF, Bonn):** Germany's large public-private seed fund; co-led Jaipur Robotics' €4.3M seed (Sep 2026). Missing a major German seed robotics backer. [tech.eu 2026-09-07](https://tech.eu/2026/09/07/jaipur-robotics-raises-eur43m-to-bring-computer-vision-to-waste-plants/)
- **H6 Daphni (Paris):** participant in Sereact's $116M Series B (Headline-led). It is a Paris VC, and the map's Paris-reachable investors are few: the summary's "best entry point" list relies on Elaia/Cathay. [tech.eu 2026-07-20](https://tech.eu/2026/07/20/zalando-joins-sereacts-116m-series-b-to-accelerate-ai-powered-warehouse-automation/)
- **H7 Corporate / strategic investors (category missing): Schaeffler, Zalando:** the map has no corporate VC or strategic investor at all, although industrial corporates co-fund the biggest deals. Schaeffler's CEO says it is "actively backing" Humanoid in the $152M Series A, and Zalando joined Sereact's Series B as a strategic investor. Corporates are also the most plausible hardware/sponsor partners for the lab. [Business Wire 2026-07-23](https://www.businesswire.com/news/home/20260723238282/en/Humanoid-Raises-%24152-Million-at-%241.35-Billion-Post-Money-Valuation-Becoming-Europes-First-Pure-Play-Humanoid-Robotics-Unicorn), [tech.eu](https://tech.eu/2026/07/20/zalando-joins-sereacts-116m-series-b-to-accelerate-ai-powered-warehouse-automation/)

## Medium (8)
- **M1 Balderton Capital (London):** existing shareholder that participated in Quantum Systems' $1.2B Series D, but did not lead it. [White & Case](https://www.whitecase.com/news/press-release/white-case-advises-noteus-and-balderton-us12-billion-series-d-financing-quantum)
- **M2 Point Nine (Berlin):** returning investor in Sereact's Series B. [tech.eu](https://tech.eu/2026/07/20/zalando-joins-sereacts-116m-series-b-to-accelerate-ai-powered-warehouse-automation/)
- **M3 Felix Capital / Bullhound Capital (London):** new participants in Sereact's Series B. Treat as one slot candidate. [tech.eu](https://tech.eu/2026/07/20/zalando-joins-sereacts-116m-series-b-to-accelerate-ai-powered-warehouse-automation/)
- **M4 DTCP (Hamburg):** €455M Defence Fund first close (Sep 2026), already invested in Six Robotics (Norwegian unmanned-systems software). [tech.eu 2026-09-24](https://tech.eu/2026/09/24/dtcp-closes-eur455m-defence-fund-to-scale-europes-strategic-tech-capabilities/)
- **M5 Northzone (Stockholm/London):** published a robotics-first AI thesis ("Robots, not chatbots", Oct 2026); a specific 2026 robotics lead was not confirmed. [Techarenan](https://www.techarenan.news/2026/10/13/robots-not-chatbots-where-northzone-sees-the-real-money-in-ai/)
- **M6 HCVC (Hardware Club, Paris):** Paris hardware/deep-tech fund; participated in Chiral's €10M seed (robotic nanoassembly) and backed Gideon Brothers earlier. A Paris-reachable hardware investor. [Quantum Computing Report](https://quantumcomputingreport.com/chiral-raises-e10m-12m-usd-to-scale-robotic-nanomaterial-integration-for-post-silicon-computing/)
- **M7 Kfund (Madrid):** listed by the researcher as a THEKER backer (runner-up). I did not reopen the source; it would give the map its only Iberian VC.
- **M8 Entourage:** €100M second fund for AI, robotics and deep tech (Oct 2026, Dealroom headline). It is in the researcher's runner-up list; individual robotics deals were not checked.

## Low (6)
- **L1 British Business Bank:** Dexory co-investor (runner-up). It is public money, like EIC/EBRD/NIF already in the map, so it adds little for a student lab.
- **L2 EIB Group / European Tech Champions Initiative:** a fund-of-funds and venture-debt channel (>€10B initiative, 2026). It is indirect for robotics. [EIB](https://www.eib.org/en/press/all/2026-415-major-institutional-investors-join-eib-group-and-eu-member-states-to-channel-over-eur10-billion-into-european-scale-ups)
- **L3 Founderful (Zurich):** Swiss pre-seed fund in Chiral's robotic-platform seed. Niche.
- **L4 Oxford Science Enterprises:** Stateful Robotics backer per the researcher's runner-up list. University spin-out niche.
- **L5 Octopus Ventures:** led Touchlab's seed (robot e-skin), but the evidence is from 2022 with no 2025-2026 robotics deal found.
- **L6 Siemens Next47:** Wandelbots investor (2022). No 2025-2026 robotics deal was found; it is worth checking if H7 is re-researched.

## Recommended re-run (gaps only)
Re-run the ecosystem researcher on H1-H7: Earlybird, Seedcamp, Visionaries Club, Lakestar, HTGF, Daphni, and corporate/strategic investors (Schaeffler, Zalando, plus any other European corporate leading a 2025-2026 robotics round). Use them to replace the weakest retained rows if the slice must stay at 20. Possible candidates are public funds with low partner value, such as EBRD Venture Capital or the NATO Innovation Fund, but that choice belongs to the coordinator.

## 5-line summary
Coverage is solid on the generalist VCs that led 2025-2026 robotics deals (Creandum, Headline, HV, Speedinvest, Elaia, Lingotto) and on public money (EIC, EBRD, NIF).
The biggest misses are early-stage physical-AI backers: Earlybird (Neuracore, robot-learning infra), Seedcamp ($320M, physical-AI focus), Visionaries Club (Allonic) and HTGF (German seed).
Lakestar (Resilience Fund, SE3/ARX) is wrongly a runner-up, and Paris-reachable options beyond Elaia/Cathay are thin (Daphni, HCVC missing).
There are no corporate/strategic investors at all (Schaeffler in Humanoid, Zalando in Sereact), although they are the likeliest hardware/sponsor partners.
21 gaps: 7 High / 8 Medium / 6 Low. Re-run the researcher on H1-H7 only and swap out low-partner-value public funds if the slice must stay at top 20.
