# Research report: ecosystem slice Europe / Integration + Demand (top 20)

- Output: `output/ecosystem_europe_integration_demand.json` — 20 organizations, 16 robots & models, 57 opened sources (every row cites pages actually opened via Chrome CDP or curl).
- Scope: Integration = system integrators that deploy robots (factory + warehouse); Demand = European end users buying/piloting robots, plus one demand-side event (automatica). Builders of robots/AI (Hexagon, Humanoid, Nomagic, Sereact, Agile Robots, RobCo, Exotec...) were left to the Platforms / Software & AI slices.
- No duplicates with `ecosystem_paris_all.json` / `ecosystem_europe_software_ai.json` (checked by name). Renault, Capgemini, Dassault Aviation are in the Paris file. Robots already in other files (Nomagic "Richard", Sereact Cortex) were not re-created; the syncer should add **Zalando** to their "Used by".
- Discovery method: Google News RSS queries (~40) -> opened article/official pages in Chrome via CDP (many corporate sites return Akamai 403 to curl).
- Saturation: the last 4 discovery queries returned mostly already-seen names (new: Nucleus Robotics + igus humanoid plan, Accenture/Vodafone/SAP warehouse pilot, Guess). Roughly reached for a top-20 slice, not proven exhaustive.

## Caveats for the verifier
- Status "To verify" on all rows. HQ cities come from general knowledge, not from opened pages, for: Swisslog (Buchs AG), Vanderlande (Veghel), TGW (Marchtrenk), KNAPP (Hart bei Graz), SSI Schäfer (Neunkirchen), Dürr, Schaeffler, Airbus (Leiden registered HQ), Comau, Körber.
- "Size / stage" is null for Innov8 Group and automatica (no allowed option fits/unknown).
- Motion (Brussels): official domain not found -> Website "unknown". Innov8 uses Region "Paris" (Courbevoie) – syncer may move it to the Paris slice.
- Schaeffler-Humanoid "up to 2,000 robots" is from the Reuters headline/URL (body paywalled).
- Mercedes-Benz investment in Apptronik: from news headline (Assembly Magazine, Feb 2026, page blocked); the Apollo trial facts come from drivesncontrols.com.
- Stellantis (Dexory robot, US plant only), Amazon EU (US org), Decathlon/Exotec, Lidl/Boston Dynamics (page blocked), Edeka, Novares, GXO, Hai Robotics, Nowaste/Cognibotics, euRobotics/European Robotics Forum 2027 (Birmingham), LogiMAT: considered, not in top 20.
- Hiring not researched. Notion not touched. "Used in projects" not output.
