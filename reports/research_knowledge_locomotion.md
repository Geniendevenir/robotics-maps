# Locomotion discovery research

## Scope and interpretation

Discovery only: **18 knowledge nodes, 17 reference robots/tools and 54 original student proposals**, three per node. Nodes are Draft, robots/tools To verify and projects Idea. No Notion access or downstream verification/coverage/Holygraph pass. The local schema governs fields and choices. The validated JSON and this report were committed and pushed as a WIP checkpoint before the final report was completed.

Four fundamentals cover wheel kinematics, stability, gait timing and reduced models. Ten applied nodes cover oscillators, biped control, MPC, whole-body control, RL transfer, mechanical leg design, perceptive walking, recovery, multirotors and wheel-legged hybrids. Four frontiers cover imitation/retargeting, parkour, loco-manipulation and cross-embodiment policies. General state estimation, SLAM, navigation planning, electronics and general grasping are outside scope. Objects and terrain appear only where they affect balance, contact or movement execution. No hiring research.

Grounding: Modern Robotics chapter 13 supplies differential-drive/nonholonomic and mecanum/omnidirectional distinctions; MIT Underactuated Robotics chapters 4–5 supply hybrid walking dynamics, simple leg models, ZMP and contact-force optimization. EPFL BioRob's neuromechanical page explicitly lists programmable central pattern generators. Primary project pages identify Extreme Parkour as ICRA 2024 and ASAP as RSS 2025; OmniH2O supplies recent whole-body human-to-humanoid work. Springer Handbook and RSS XXI proceedings returned bot challenges, so their contents were **not** consulted. Conference session schedules and complete textbook coverage were not verified; the above university material and individual papers are substitutes, not a claim of comprehensive track coverage.

Costs, durations, wow ratings and work-hour splits are student-project planning estimates, not vendor quotes or measurements. All knowledge entry costs refer to a simulation/offline first demo. Computer/GPU cost is excluded, so “€0 (sim only)” does not mean free compute. Most proposals are sim-first; three optional hardware extensions use Bittle, a passive linkage, or guarded Crazyflie flight. Their bands are provisional budget envelopes, not an assertion that a complete kit fits that price. Robot references are not purchase requirements or tested compatibility promises. No Go2 or humanoid purchase is needed for the initial plan.

## Queries actually run

arXiv Atom API discovery, with `sortBy=submittedDate`, `sortOrder=descending`, `max_results=8`. The six requests were fetched as a batch and reviewed in the order below; the last three form the saturation sequence. No Bing/DuckDuckGo snippets were used.

| Order | Exact `search_query` | Entries returned |
|---|---|---:|
| 1 | `all:"legged locomotion" AND all:"survey"` | 2 |
| 2 | `all:"humanoid locomotion" AND all:"imitation"` | 8 |
| 3 | `all:"locomotion" AND all:"wheel-legged"` | 8 |
| 4 | `all:"locomotion" AND all:"generalist"` | 8 |
| 5 | `all:"locomotion" AND all:"recovery"` | 8 |
| 6 | `all:"locomotion" AND all:"perceptive"` | 8 |

The initial 18-node working taxonomy came from the task's proposed categories and opened university/project sources, not from claiming these six queries discovered every category independently. The survey query included non-inertial environments, retained as a stability/robustness evaluation setting, not a separate knowledge node. The wheel-legged query supported retaining the optional hybrid node.

Direct retrievals then filled details and checked availability: official robot documentation, repository README content, author project pages and selected arXiv abstract pages. No additional discovery queries were run after the saturation sequence. URLs are recorded verbatim in JSON `sources_consulted`; **44 distinct usable opened URLs: 38 primary/reference pages and 6 discovery API responses**. Different URLs can concern the same paper, so this is not a count of independent research results. Older textbooks, DeepMimic and 2019 ANYmal recovery are retained for foundational provenance. Current-state coverage includes 2024 Extreme Parkour/OmniH2O, 2025 ASAP and 2026 VioLA, FetchMan, Rapid Embodiment Adaptation and STEP. The 2026 abstracts are author-reported preprints, not independently replicated capabilities; performance numbers were deliberately not promoted into the map.

## Saturation-stop evidence

“New entry” means a previously uncovered **in-scope knowledge node**, not a new paper or robot variant. Denominator: 18 working nodes. Each of three consecutive reviewed queries produced 0/18 = 0% new nodes, below 10%. This is taxonomy saturation relative to the working taxonomy, not exhaustive literature coverage.

| Consecutive query | Results reviewed | New nodes | Mapping / exclusions |
|---|---:|---:|---|
| `all:"locomotion" AND all:"generalist"` | 8 | 0 | VioLA and MuscleMimic map to motion imitation/generalist policies; Rapid Embodiment Adaptation and ABot-C0 to cross-embodiment/RL; FetchMan and both HAF papers to loco-manipulation. Cross-Embodiment Motion Planning is relevant only for body-conditioned execution, not a new general-planning node. VioLA, FetchMan and Rapid Embodiment Adaptation abstracts were opened directly afterward. |
| `all:"locomotion" AND all:"recovery"` | 8 | 0 | CompliantBot and ThinkLocoManip map to whole-body control/loco-manipulation; SkateNav to wheel-legged gait; Geometry-Aware Predictive Control to biped/MPC; Around the World to RL gait. EgoXperience and MobiAgent are broader representation/navigation work, not new locomotion categories. The adversarial robotic-security result is excluded from scope and not investigated. No recovery-specific claim was inferred from a keyword match; the directly opened ANYmal paper provides recovery evidence. |
| `all:"locomotion" AND all:"perceptive"` | 8 | 0 | STEP and Watch Your Step map to perceptive locomotion; HC2Robot to parkour; GRAFT to motion tracking; ReGATE and ThinkLocoManip to whole-body interaction. The XR perception and operating-room orchestration results are out of scope. STEP's abstract was subsequently opened for its perception/dropout evaluation framing. |

Stopped discovery after this sequence. Later direct pages served citation and access checks only. New hardware variants or application sectors are not automatically separate knowledge nodes.

## Top three: qualitative benefit/cost judgement

1. **Gaits & gait cycles** — fastest readable animation and contact diagram for beginners, strong visible progression to small quadrupeds, and no purchase for a first demo. Bittle/Pupper community references make the work reusable; physical walking is a later supervised extension.
2. **RL locomotion with sim-to-real** — best fit to the students' AI/software skills and a compelling learned-walking video. Public frameworks reduce infrastructure cost, but GPU budget, reproducibility and hardware transfer remain real risks. This tests the proposed low-cost-learning wedge rather than assuming it is proven.
3. **Humanoid motion imitation & retargeting** — highly legible human/robot side-by-side video and strong current ecosystem relevance. Start with offline retargeting and simulation, not a humanoid purchase. Retargeting animation alone is not physically feasible motion tracking.

The requested `(accessibility × visual impact × ecosystem relevance) / cost` is a qualitative trade-off, not numeric division by a zero sim price or fabricated ecosystem scores. Wheeled kinematics and hover control are cheaper foundations but less distinctive public research showcases; parkour is visually stronger but harder and riskier.

## Gaps, unknowns and representation decisions

- Hardware price, French/EU shipping/VAT, current research-control access, complete kit budgets and release years are `unknown` unless established. All release years remain `unknown`; a numeric Notion field will need missing-value handling at any later approved sync. Unitree advertised base prices were not treated as delivered research-capable configurations.
- `Open source` means a public implementation is available, not that every robot part, asset, policy weight or commercial use is unrestricted. Petoi OpenCat is a legacy-platform repository; current Bittle variants can need different code. TurtleBot software being public does not make its Create 3 base open hardware. Spot SDK availability does not mean open low-level locomotion control. Individual component licenses need checking before reuse.
- Stanford Pupper is grounded in `StanfordQuadruped`; the guessed `Pupper-v3` URL returned 404, so no v3 claim is made. Booster's homepage now highlights T2/K1 and did not establish a T1 specification, so no Booster T1 row is emitted. ANYmal's current vendor page was inaccessible; its locomotion/recovery row is grounded in the primary ETH research abstract, not a current product-spec claim. The Crazyflie product URL returned an older vendor stock announcement rather than a specification sheet; current firmware was opened separately, and numeric specs/price were left unknown.
- No duplicate rows or relations to robots/tools already mapped in manipulation or embedded/electronics are emitted. MuJoCo Playground is a distinct environment library, not another MuJoCo engine row. Cheetah-Software is a cited control implementation, not a duplicate Mini Cheetah actuator row. Local project names are checked against `output/existing_projects.json`; all prerequisites are local, directed onboarding-to-extension chains.
- `Built by`, `Used by`, `Relevant orgs` are empty; readable attribution uses `Builder (if not in map)`. `Project ideas` is empty. No formula or deprecated fields are emitted. No live Notion deduplication was attempted under the no-Notion constraint; a future approved sync must match existing pilot rows.
- Projects needing terrain, retargeted motion, checkpoints or robot models require compatibility/license checks. PX4 and Crazyflie are alternative flight-control references, not a claim that Crazyflie runs PX4 firmware. Recovery and parkour stay in simulation; do not intentionally drop or launch physical robots. Hardware flight needs prop guards, supervised clearance, a positioning solution and local safety review.
- Normal, empty/no-command and error/failure evaluations are specified in every proposal. These are proposed tests, not completed experiments. No robot code was implemented or run; reproducibility, hardware safety, sim-to-real transfer and visuals are unverified.

### Retrieval exclusions

HTTP success alone was not sufficient to count a source. Spot's commercial page and RSS XXI proceedings returned “One moment, please” challenges; Springer returned “Client Challenge”; none is in `sources_consulted`. ANYbotics product page returned 403, and its homepage could not be retrieved. Guessed CPG, Pupper-v3, ETH parkour and loco-manipulation URLs returned 404 and were excluded. The `ijrr.org` DOI-shaped URL returned unrelated gambling content and was rejected. Three attempted arXiv identifiers (`2406.10479`, `2402.06170`, `0807.1263`) resolved to unrelated LLM/HCI/materials papers, not the intended locomotion references; they were excluded after reading the actual titles/abstracts. Booster's usable homepage was inspected but not used as a locomotion source because T1 was not verified. Only the content-bearing, relevant URLs in JSON count toward the total.

## Reproducible validation

Run from the repository root with Python 3; no third-party dependencies or network access. This adapts the manipulation report's schema validator, adds cross-file exclusions, robot statuses, exact top3 fields, per-node project counts, branch consistency and prerequisite-cycle checks. Sources are checked against the opened-source manifest; structural validation does not independently fact-check their contents.

```python
import json
import re
from pathlib import Path

data = json.loads(Path('output/knowledge_locomotion.json').read_text())
schema = Path('schemas/notion-schema.md').read_text()
sections = dict(re.findall(r'^## ([^\n]+)\n(.*?)(?=^## |\Z)', schema, re.M | re.S))
options = {}
for section, body in sections.items():
    fields = {}
    for bullet in re.split(r'\n(?=- )', body.strip()):
        match = re.match(r'- (.+?) \((select[^)]*|multi|status)\):\s*(.*)', bullet, re.S)
        if match:
            field, _, values = match.groups()
            fields[field] = [' '.join(v.split()) for v in values.split('|')]
    options[section] = fields
branches = options['Knowledge Map']['Branch']
options['Projects (Holygraph)']['Branch'] = branches
options['Projects (Holygraph)']['Secondary branches'] = branches
allowed = {
    'nodes': set('Node|Branch|Level|Discipline|What it is|Prerequisites|Accessibility for us|Starter hardware cost|Time to first demo|Frontier state 2026|Key players|Best resources|Sources|Project ideas|Status|_accessibility_reason'.split('|')),
    'robots_models': set('Name|Kind|Form factor|Model type|Built by|Used by|Builder (if not in map)|Knowledge nodes|Open source|Price / access|Key specs|Release year|Why it matters|Sources|Status'.split('|')),
    'project_candidates': set('Project|Kind|Branch|Secondary branches|Novelty|Autonomy|Hardware|Integration|Software %|Mechanical %|Electrical %|Deliverable|Description|References|Duration|Hardware cost|Wow factor|Prerequisites|Knowledge nodes|Robots & models|Relevant orgs|Status'.split('|')),
}
groups = [('nodes', 'Knowledge Map', 'Node'), ('robots_models', 'Robots & Models', 'Name'), ('project_candidates', 'Projects (Holygraph)', 'Project')]
assert set(data) == {'branch', 'nodes', 'robots_models', 'project_candidates', 'top3', 'sources_consulted'}
assert data['branch'] == 'Locomotion'
sources = set(data['sources_consulted'])
assert len(sources) == len(data['sources_consulted']) >= 15
names = {}
checks = 0
for group, section, title in groups:
    rows = data[group]
    names[group] = {row[title] for row in rows}
    assert len(names[group]) == len(rows), ('duplicate', group)
    for row in rows:
        assert set(row) == allowed[group], (group, row[title], set(row) ^ allowed[group])
        for field, choices in options[section].items():
            if field not in row:
                continue
            values = row[field] if isinstance(row[field], list) else [row[field]]
            for value in values:
                assert value in choices, (row[title], field, value, choices)
                checks += 1
        urls = set(re.findall(r'https?://[^\s;]+', row.get('Sources', row.get('References', ''))))
        assert urls and urls <= sources, (row[title], urls - sources)
for node in data['nodes']:
    assert node['Branch'] == 'Locomotion' and node['Status'] == 'Draft'
    assert node['Project ideas'] == '' and node['_accessibility_reason']
for row in data['robots_models'] + data['project_candidates']:
    assert set(row['Knowledge nodes']) <= names['nodes']
    if 'Robots & models' in row:
        assert set(row['Robots & models']) <= names['robots_models']
        assert set(row['Prerequisites']) <= names['project_candidates']
        assert row['Project'] not in row['Prerequisites']
        assert sum(row[k] for k in ['Software %', 'Mechanical %', 'Electrical %']) == 100
        assert row['Branch'] == 'Locomotion' and row['Status'] == 'Idea'
        assert not row['Relevant orgs']
    else:
        assert isinstance(row['Open source'], bool)
        assert isinstance(row['Release year'], int) or row['Release year'] == 'unknown'
        assert row['Status'] in ['To verify', 'Draft']
        assert not row['Built by'] and not row['Used by']
assert 8 <= len(data['nodes']) <= 20
for node in names['nodes']:
    assert sum(node in p['Knowledge nodes'] for p in data['project_candidates']) == 3
assert len(data['top3']) == 3
assert len({x['Node'] for x in data['top3']}) == 3
assert all(set(x) == {'Node', 'justification'} and x['Node'] in names['nodes'] and x['justification'] for x in data['top3'])
for file in ['knowledge_manipulation.json', 'knowledge_embedded_electronics.json']:
    other = json.loads((Path('output') / file).read_text())
    assert not names['robots_models'] & {r['Name'] for r in other['robots_models']}
existing = json.loads(Path('output/existing_projects.json').read_text())
assert not names['project_candidates'] & {p['Project'] for p in existing}
graph = {p['Project']: p['Prerequisites'] for p in data['project_candidates']}
done = set()
def visit(name, active):
    assert name not in active, ('cycle', name)
    if name not in done:
        for dep in graph[name]:
            visit(dep, active | {name})
        done.add(name)
for name in graph:
    visit(name, set())
print(f'PASS: {checks} select/multi-select/status values validated against schema')
print('PASS: exact row fields, unique names, 100% work splits, local relations and per-row source URLs')
print('PASS: 3 projects per node, Draft/To verify/Idea statuses, 3 top nodes; no formula or deprecated fields')
print('PASS: no excluded robot/tool duplicates, no existing project-name collisions, acyclic prerequisites')
print(f"COUNTS: nodes={len(data['nodes'])}, robots_models={len(data['robots_models'])}, projects={len(data['project_candidates'])}, sources={len(sources)}")
```

Validation output:

```text
PASS: 775 select/multi-select/status values validated against schema
PASS: exact row fields, unique names, 100% work splits, local relations and per-row source URLs
PASS: 3 projects per node, Draft/To verify/Idea statuses, 3 top nodes; no formula or deprecated fields
PASS: no excluded robot/tool duplicates, no existing project-name collisions, acyclic prerequisites
COUNTS: nodes=18, robots_models=17, projects=54, sources=44
```

`git diff --check` completed without diagnostics. There is no existing executable test suite for these research JSON files. This is a research deliverable, not an implemented or visually verified robot demo. Independent source verification and coverage criticism remain downstream pipeline steps.
