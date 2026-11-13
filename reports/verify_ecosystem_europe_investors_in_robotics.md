# Verification — Europe Investors in Robotics

Verified on 2026-11-13 against `devin/playbooks/verifier.md`, `CLAUDE.md` and `schemas/notion-schema.md`. No Notion reads or writes were made.

## Result

| Dataset | Input | Verified | Corrected | Rejected | Retained |
|---|---:|---:|---:|---:|---:|
| Ecosystem Map organizations | 20 | 0 | 20 | 0 | 20 |
| Robots & Models | 7 | 5 | 2 | 0 | 7 |
| **Total** | **27** | **5** | **22** | **0** | **27** |

"Verified" = no change beyond the Status reset. "Corrected" includes source repair, unsupported-claim removal and schema cleanup. Every organization was corrected at least because `_relationship_reason` is not a Notion property and was removed. All retained rows have Status `To verify`. No project candidates exist in this file.

All 70 distinct row source/website URLs were requested (curl, then Chrome CDP for blocked ones). Unreadable: forbes.com (empty via CDP; replaced by Japan Times + Trending Topics), eu-startups.com (blocked; €214M Vsquared fund claim dropped), eic.ec.europa.eu/eic-funding-opportunities/eic-fund_en (404; replaced by https://eic.ec.europa.eu/eic-fund_en), lingotto.com/en/innovation (404; replaced by https://www.lingotto.com). British Business Bank, The Engineer and Atomico pages blocked curl but read via CDP. `sources_consulted` is rebuilt from the 67 retained row URLs.

## Limits
- `Size / stage` has no investor-specific option; values are kept as the researcher's proxy for fund scale/stage focus (e.g. large multi-stage VCs = Public/Large). Treat as indicative.
- Websites were checked as live official domains; an active, dated 2025-2026 deal or fund announcement is the evidence of 2026 activity.
- Relationship potential tags are outreach hypotheses; no contact or sponsorship offer was established. Warm contact path stays "unknown".
- The EU Scaleup Europe fund shortlist claim (Eurazeo, Atomico) could not be read in a primary source (pe-insights is Cloudflare-blocked) and Real Deals (19 May 2026) reports EQT was chosen to manage it, so the claim was removed.
- Summary rewritten to drop unsourced figures (NEURA $1.4B, Agile Robots $500M, Tether/Nvidia/Amazon leads, Flexion, "Speedinvest Paris").

## Organization verdicts

| Organization | Verdict | One-line reason |
|---|---|---|
| Creandum | corrected | Removed non-schema key; tech.eu confirms it led Sereact's €25M Series A and returned in the $110M Series B; Imperial confirms Machenta $40M seed co-led with USV. |
| Headline | corrected | Removed non-schema key; tech.eu and Osborne Clarke confirm Headline (SF/Berlin) led Sereact's ~$110M Series B and Cortex 2 launch. |
| Air Street Capital | corrected | Removed non-schema key; returning Sereact investor (tech.eu, Osborne Clarke); State of AI 2026 covers robotics. |
| Lingotto Innovation (Exor) | corrected | Website/source /en/innovation 404 replaced by lingotto.com; RobCo $100M Series C co-lead and NEURA €50M 2023 round confirmed. |
| HV Capital | corrected | Removed non-schema key; led ARX €31M Series A, NEURA 2023 co-lead, existing Quantum Systems investor ($1.2B round, 2 Jul 2026) all confirmed. |
| Speedinvest | corrected | Removed non-schema key; led ARX €11M extension, co-invested in mimic seed, >€1B AUM per mimic release confirmed. |
| Elaia | corrected | Removed non-schema key; led mimic $16M seed, Dexory investor, €120M Fund V first close confirmed. |
| Vsquared Ventures | corrected | €214M fund (source blocked) and NEURA $1.4B Series C (unsourced) removed; NEURA 2023 co-lead confirmed. |
| Amadeus Capital Partners | corrected | Removed non-schema key and unchecked "on humanoids"; Stateful $4.8M pre-seed (24 Mar 2026), NEOintralogistics €3M (20 Jan 2026), Slamcore portfolio confirmed. |
| IQ Capital | corrected | Removed non-schema key; Gravis $23M co-lead and SoftBank $200M Series A unicorn confirmed. |
| Zacua Ventures | corrected | Removed non-schema key; $135M Fund II (11 Nov 2026), corporate LPs and Gravis co-lead confirmed; city left unknown. |
| Plural | corrected | Removed non-schema key and unverified partner names; led Upside Robotics $7.5M seed and a production-line robotics seed with PROTOTYPE confirmed. |
| Eurazeo | corrected | Removed unsourced Scaleup Europe shortlist claim; Dexory £75M Series C lead within £124M raise confirmed. |
| Atomico | corrected | Removed unsourced shortlist claim; Great Rollout dated 24 Jun 2026 and Dexory investment confirmed. |
| Cathay Innovation | corrected | Removed unsourced Moon Surgical/Ganymed claim; THEKER $85M Series A participation and $1B fund (27 May 2025) with named corporate LPs confirmed. |
| EIC Fund (European Innovation Council) | corrected | Website 404 fixed; unsourced Cognibotics and defence-opening claims removed; Hyperion co-lead and Nanoflex €10M EIC Fund equity confirmed. |
| NATO Innovation Fund | corrected | Removed non-schema key; 24 allies, ARX and Greenjets backing confirmed. |
| EBRD Venture Capital | corrected | Removed non-schema key; led Nomagic $44M Series B with Khosla and Almaz confirmed. |
| PROTOTYPE Capital | corrected | Removed non-schema key; Fund III (Jan 2026, ~€15M) and robotics/physical-AI focus confirmed. |
| Redalpine | corrected | Removed non-schema key, reworded unverified "multi-stage"; Enact $30M pre-seed (22 Oct 2026, LeCun/Mensch angels) and Enact as first deal of $250M RAC VIII confirmed. |

## Robots & Models verdicts

| Name | Verdict | One-line reason |
|---|---|---|
| Gereon UGV | verified | tech.eu and ADS Advance confirm ARX's connected tactical UGVs with open software platform, trialled by UK forces; €31M+€11M = €42M Series A. |
| Gravis autonomous excavator retrofit kit | corrected | Forbes source unreadable, replaced by Japan Times; specs tightened to Trending Topics description (telemetry, retrofit of excavators). |
| Dexory autonomous warehouse-scanning robot | corrected | Unsourced "AI digital twin" wording replaced; builder city set to London; BusinessCloud source added. |
| Machenta instant-learning model | verified | Imperial confirms single-demonstration learning model and $40M seed. |
| mimic humanoid hand + physical-AI model | verified | Startupticker confirms humanoid robotic hands + foundation AI model, Elaia/Speedinvest. |
| THEKER generalist factory robot | verified | Cathay release confirms Barcelona, AI-native generalist robots, $85M Series A. |
| Stateful Robotics long-horizon planning platform | verified | Amadeus release confirms Oxford spin-out, long-horizon intelligence layer, $4.8M pre-seed. |
