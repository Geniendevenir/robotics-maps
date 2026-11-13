# Notion schema reference
Field names and select options must match exactly. Fetch live via Notion MCP before syncing.

## Knowledge Map
- Node (title)
- Branch (select): Mechanisms & actuation | Sensing | Embedded & electronics | Kinematics & dynamics |
  Control | Perception | State estimation & SLAM | Planning | Manipulation | Locomotion |
  Robot learning | Simulation | HRI & safety
- Level (select): Fundamental | Applied | Frontier
- Discipline (multi): Mechanical | Electrical | Software | AI/ML | Math
- What it is (text, 2-3 beginner sentences) · Prerequisites (text)
- Accessibility for us (select): 1 - Hard | 2 | 3 | 4 | 5 - Easy
- Starter hardware cost (select): €0 (sim only) | <€500 | €500-5k | €5k+
- Time to first demo (select): Days | Weeks | Months
- Frontier state 2026 · Key players · Best resources · Sources (text)
- Project ideas (text): DEPRECATED, leave empty; projects go to Projects (Holygraph)
- Status (status): Draft | To verify | Verified
- Relations (auto, from other DBs): Robots & models, Projects

## Ecosystem Map
- Organization (title)
- Type (select): Corporate | Startup | Research lab | School | Association | Investor | Event |
  Open-source community
- Region (select): Paris | France | Europe | US | China | Japan | South Korea | Other
- City (text)
- Value chain (multi): Components | Platforms | Software & AI | Integration | Demand
- Sector (multi): Industrial | Logistics | Humanoid | Medical | Consumer | Defense | Agri |
  Research | Mobility
- What they build (text)
- Size / stage (select): Pre-seed/Seed | Series A-B | Series C+ | Public/Large | Non-profit
- Open source (checkbox)
- Relationship potential (multi): Sponsor | Partner | Hackathon host | Mentor/Speaker | Hardware/Compute
- Warm contact path (text) · Website (url) · Sources (text)
- Status (status): Draft | To verify | Verified
- Relations (auto): Builds, Uses (-> Robots & Models), Related projects (-> Projects)

## Robots & Models
- Name (title)
- Kind (select): Robot | AI model | Simulator/Tool
- Form factor (select, robots): Arm | Humanoid | Quadruped | Mobile manipulator | Wheeled/AMR |
  Exoskeleton | Drone | Hand/Gripper | N/A
- Model type (select, models): VLA | World model | Policy (IL/RL) | Perception | N/A
- Built by (relation -> Ecosystem Map) · Used by (relation -> Ecosystem Map)
- Builder (if not in map) (text)
- Knowledge nodes (relation -> Knowledge Map)
- Open source (checkbox) · Price / access · Key specs (text) · Release year (number)
- Why it matters · Sources (text)
- Status (status): Draft | To verify | Verified

## Projects (Holygraph)
- Project (title)
- Kind (select): Onboarding | Project
- Branch (select, same 13 options as Knowledge Map) · Secondary branches (multi, same options)
- Novelty (select): 1 - Reproduce | 2 - Adapt | 3 - Combine | 4 - Original | 5 - Beyond SOTA
- Autonomy (select): 1 - Teleoperated | 2 - Scripted | 3 - Learned single task |
  4 - Multi-task or language | 5 - Open-world long-horizon
- Hardware (select): 1 - Off-the-shelf | 2 - Modified | 3 - Custom part | 4 - Custom subsystem |
  5 - Full custom robot
- Integration (select): 1 - Single component | 2 - Two subsystems | 3 - Three+ subsystems |
  4 - Full robot stack | 5 - Real-world deployment
- Level (formula, read-only): 0 for Onboarding, else average of the 3 highest axes
- Software % · Mechanical % · Electrical % (numbers, share of work hours, sum = 100)
- Mix check (formula, read-only)
- Deliverable (text: the filmable demo) · Description · References (text)
- Duration (select): 1 week | 2-4 weeks | 1-2 months | 3+ months
- Hardware cost (select): €0 (sim only) | <€500 | €500-5k | €5k+
- Wow factor (select): 1 | 2 | 3 | 4 | 5
- Prerequisites (relation -> Projects; reverse = Unlocks)
- Knowledge nodes (-> Knowledge Map) · Robots & models (-> Robots & Models) ·
  Relevant orgs (-> Ecosystem Map)
- Status (status): Idea | Shortlisted | Running | Done
