# Manipulation discovery research

## Scope and interpretation

Discovery only: 17 manipulation nodes, 21 reference robots/models/tools, and 51 original student project proposals (three per node). All rows remain Draft/Idea. No Notion calls, verification-agent pass, coverage-agent pass, or final Holygraph selection were performed. The checked-in schema is authoritative. No deprecated `Used in projects` or formula fields are emitted.

The taxonomy keeps four fundamentals, eight applied areas and five frontiers. Springer Handbook of Robotics (opened publisher contents and Grasping chapter abstract) grounds contact, hands, force control and motion planning. Modern Robotics chapter 12 grounds friction, form/force closure and non-prehensile actions. MIT's manipulation course grounds pick/place, perception, control, planning and task integration. RSS XXI proceedings were opened to check current manipulation research themes (VLAs, action representations, simulation); individual project pages identify ICRA, RSS and CoRL papers. Conference session schedules could not be retrieved, so proceedings/paper coverage substitutes for a track-by-track analysis; no claim of complete program coverage.

Entry costs and accessibility refer to a simulation/offline first demo, not the cost of a real robot. Project durations, cost bands, wow ratings and work-hour splits are proposals, not sourced prices or measured results. Hardware projects need a procurement review. Software-only work is 100/0/0; projects needing mounting/assembly and wiring use 75/15/10 estimates. Frontier refers to the knowledge area, not a claim that a student proposal exceeds SOTA. No beyond-SOTA rating is assigned.

## Queries actually run

Initial discovery (search-result titles/snippets used to select primary pages):

1. `robot manipulation course grasping contact planning MIT manipulation`
2. `robot manipulation grasp pose motion tactile deformable benchmark`
3. `robot manipulation foundation models OpenVLA pi0 ReKep VoxPoser`

The 17-node working taxonomy was then written from the opened primary references. Additional source pages were opened directly by URL, rather than adding redundant searches for every product. A source URL appears in `sources_consulted` only when content was retrieved; the JSON is the complete opened-source manifest. It includes official docs, primary paper/project pages, repositories and publisher pages. Stable older sources remain useful for mechanics and benchmark provenance; 2024 ALOHA 2, Mobile ALOHA, FoundationPose, OpenVLA, Octo and pi0 are supplemented by 2025 RSS proceedings/openpi updates and 2026 DECO, M3-Tele and STAR. The latter two are preprints, not independently validated capability claims.

## Saturation-stop evidence

The unit of a new **entry** is a previously uncovered manipulation knowledge node, not every newly found paper/model. Denominator: 17 existing scoped nodes. Three consecutive discovery queries returned no new node (0/17 = 0%, below 10%). This is taxonomy saturation, not a claim that the literature or hardware list is exhaustive.

| Consecutive query | Results reviewed | New nodes | Mapping / evidence |
|---|---:|---:|---|
| `robot manipulation survey taxonomy grasping dexterous nonprehensile deformable task motion planning` | 8 | 0 | Unified manipulation survey, T-DOM, embodied-manipulation survey and nonprehensile survey all map to existing mechanics, deformables, dexterity, planning and policy nodes. Application settings such as surgery are not split into general knowledge nodes. |
| `robot manipulation recent research bimanual tactile mobile manipulation 2025 2026` | 8 | 0 | DECO, RoboMIND 2.0, M3-Tele, STAR, BiTAT, TAMEn, Mobile ALOHA and cooperative tactile grasping map to teleoperation, bimanual/mobile, tactile, contact-rich, dexterous and policy nodes. DECO, M3-Tele and STAR were subsequently opened for primary-source details. |
| `robot manipulation open vocabulary generalist policies contact rich manipulation survey` | 8 | 0 | Foundation-model surveys, manipulation-in-contact survey, action-unlabeled generalist learning and RoboDojo map to affordances, VLAs, teleoperation, contact-rich manipulation and evaluation within those nodes. |

Stopped discovery after this sequence. A later targeted bibliographic lookup, `Springer Handbook Robotics manipulation grasping chapters contents`, completed the required textbook grounding; it was not an attempt to expand the taxonomy. Direct retrievals after saturation filled citations and checked access/license claims. Failed retrievals: `https://contact-graspnet.github.io/` was replaced by the authors' repository; RSS program URLs (`https://roboticsconference.org/program/papers/`, `https://roboticsconference.org/2025/program/`, `https://roboticsconference.org/2024/program/`) returned no content and were replaced by RSS XXI proceedings. `https://dex-net.org/` returned no usable page and was not used. Empty retrievals are not counted as sources.

## Top three: qualitative benefit/cost judgement

1. **Pick-and-place pipeline** — highest accessibility, a very legible first video, and reusable infrastructure. Simulation costs no new hardware and avoids premature purchasing.
2. **Teleoperation & demonstration collection for arms** — direct LeRobot/SO-101 community relevance, visible leader/follower interaction, and reusable demonstrations. Better initial hardware complexity than a mobile or bimanual system, but real kit pricing is unknown and data quality must be tested before treating low-cost imitation learning as the lab's established wedge.
3. **Learning-based grasp detection** — strong fit to software/AI students, convincing overlays and clutter demos, public data/checkpoints and a cheap offline start. Real grasp execution requires calibrated cameras and a reachable, collision-free arm plan.

The ratio `(accessibility × visual impact × ecosystem relevance) / cost` is used qualitatively; no numeric division by a zero simulation price and no fabricated ecosystem scores.

## Gaps, unknowns and representation decisions

- Current delivered hardware prices, French/EU shipping/VAT, tool adapters, GPU procurement and complete lab budgets are unknown. No vendor quote is invented. Release years are `unknown` where not established by an opened source; this intentional string sentinel in a numeric Notion field must be handled as missing data by a future syncer.
- Checkbox `Open source` describes availability of the referenced implementation, not a blanket commercial license. AnyGrasp and GelSight Mini are conservatively false; AnyGrasp library commercial/access terms remain unknown. Sensor software availability is not proof of open hardware. Check code, weights, dataset and hardware licenses independently before reuse.
- GelSight Mini is a `Simulator/Tool` because the schema has no Sensor kind. GraspNet-1Billion is a benchmark/tool, not an AI model. ReKep/VoxPoser are composed planning tools, not a new policy checkpoint. Octo is `Policy (IL/RL)`, not automatically VLA because it accepts language.
- `Built by`, `Used by` and `Relevant orgs` are empty: this file has no ecosystem rows to resolve. Human-readable attribution goes in `Builder (if not in map)`. Every populated knowledge, robot/model and project-prerequisite relation resolves locally.
- Robot references are not purchase instructions. Not every listed tool is required by every project variant. Simulated/mobile/bimanual proposals need compatible robot assets and interfaces before implementation; no untested SO-101 compatibility is promised for the generalist policies.
- The narrow scope does not separately map full perception, SLAM, generic planning, low-level electronics or general robot learning; their manipulation-specific uses and prerequisites are retained. Flexible cables, VR/spacemouse interfaces, soft/suction hardware, DIGIT, Koch, FR3, UR5e, RT-2 and GR00T are candidates for later coverage work, not fabricated detailed rows. Cloth has a primary worked reference; cable handling has less depth. No organization outreach or hiring research.
- Project axes span onboarding through full-stack integration and an original affordance evaluation design. Full custom robot builds and claims beyond SOTA are intentionally not proposed for students weak in hardware. Mechanical/electrical skills should be developed through modest gripper/sensor work before full-body systems.
- No live Notion pilot-row deduplication was possible under the no-Notion constraint. Local names are unique; the later syncer must match existing pilot rows rather than duplicate them.
- This is research, not an implemented/visually checked robot demo. Published performance statements are bounded to their authors' setting; real reproducibility, safety, empty/error behavior and transfer need experiments.

## Reproducible validation

Run this from the repository root. It reads select/multi-select/status option lists from the authoritative schema, validates all emitted row options and field names, checks percentages and local relation targets, and ensures each row cites an opened-source-manifest URL. No third-party dependencies or network access are needed.

```python
import json
import re
from pathlib import Path

data = json.loads(Path('output/knowledge_manipulation.json').read_text())
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
assert data['branch'] == 'Manipulation'
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
    assert node['Branch'] == 'Manipulation' and node['Status'] == 'Draft'
    assert node['Project ideas'] == '' and node['_accessibility_reason']
for row in data['robots_models'] + data['project_candidates']:
    assert set(row['Knowledge nodes']) <= names['nodes']
    if 'Robots & models' in row:
        assert set(row['Robots & models']) <= names['robots_models']
        assert set(row['Prerequisites']) <= names['project_candidates']
        assert row['Project'] not in row['Prerequisites']
        assert sum(row[k] for k in ['Software %', 'Mechanical %', 'Electrical %']) == 100
        assert row['Status'] == 'Idea'
        assert not row['Relevant orgs']
    else:
        assert isinstance(row['Open source'], bool)
        assert isinstance(row['Release year'], int) or row['Release year'] == 'unknown'
        assert not row['Built by'] and not row['Used by']
assert 8 <= len(data['nodes']) <= 20
for node in names['nodes']:
    assert 3 <= sum(node in p['Knowledge nodes'] for p in data['project_candidates']) <= 6
assert len(data['top3']) == 3
assert len({x['Node'] for x in data['top3']}) == 3
assert all(x['Node'] in names['nodes'] and x['justification'] for x in data['top3'])
print(f'PASS: {checks} select/multi-select/status values validated against schema')
print('PASS: exact row fields, unique names, 100% work splits, local relations and per-row source URLs')
print('PASS: 3 projects per node, Draft/Idea statuses, 3 top nodes; no formula or deprecated fields')
print(f"COUNTS: nodes={len(data['nodes'])}, robots_models={len(data['robots_models'])}, projects={len(data['project_candidates'])}, sources={len(sources)}")
```

Validation output:

```text
PASS: 744 select/multi-select/status values validated against schema
PASS: exact row fields, unique names, 100% work splits, local relations and per-row source URLs
PASS: 3 projects per node, Draft/Idea statuses, 3 top nodes; no formula or deprecated fields
COUNTS: nodes=17, robots_models=21, projects=51, sources=32
```

`git diff --check` also completed without diagnostics. The initial validator run failed because its Markdown-heading regex was greedy; the regex was corrected before the successful output above. No research data was changed to accommodate validation. This repository has no existing executable test suite for these research JSON files.
