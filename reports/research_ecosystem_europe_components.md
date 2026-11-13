# Research notes: ecosystem slice Europe / Components (top 20)

- Output: `output/ecosystem_europe_components.json` (20 organizations, 16 robots & models, 37 opened sources).
- Discovery: Google News RSS queries (actuators, humanoid actuators, grippers, robot hands, force-torque/tactile sensors, chipmakers + humanoid, maker boards), then opened official sites and press articles through the Chrome CDP (curl gets 403 on maxon, Schaeffler, Festo, Raspberry Pi).
- Saturation stop NOT reached: stopped to stay inside the ACU budget. The last queries still surfaced new names (Enact Intelligence, Allonic, AdapTronics).
- All rows are "To verify". Weak points for the verifier:
  - Nvidia partnerships with Infineon/ST/NXP (Mar 2026): Reuters page opened but body did not render; claim from headline.
  - Allonic: OpenAI / Hugging Face angels from headlines only; $7.2M stated on allonic.com.
  - Enact: amount stated by Startupticker ($30M); EU-Startups page body did not render.
  - maxon "Young Engineers Program": only seen as a menu item on maxongroup.com.
  - Festo: only the home page was opened (about page 404).
  - "Size / stage" = "unknown" for OnRobot, Shadow Robot, Bota Systems, Synapticon (not a Notion option; syncer should leave empty).
  - AdapTronics city unknown (Italy).
- Not duplicated: none of these orgs are in ecosystem_paris_all.json or ecosystem_europe_software_ai.json. Humanoid (UK) is referenced only as a builder name (it lives in the Software & AI file). Prophesee, Exwayz, Outsight (Paris sensors) left to the Paris file.
- Also considered, not in the top 20: Arm (Cambridge), Faulhaber, Basler, Bosch Sensortec, Wittenstein, Zimmer Group, Stabilus, Seed Robotics, Generative Bionics (more Platforms), Oversonic (Platforms).
- Hiring not researched. Notion not touched. "Used in projects" not output.
