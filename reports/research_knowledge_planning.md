# Planning discovery research

## Scope and interpretation

Discovery only: 17 generic planning nodes (four Fundamental, nine Applied, four Frontier), 14 reference models/tools and 51 original student project proposals (three per node). Knowledge rows are Draft, reference rows To verify, projects Idea. No Notion access, verification-agent pass, coverage-agent pass or final Holygraph selection was performed. The checked-in schema is authoritative for this offline deliverable. No formula fields or `Used in projects` are emitted.

LaValle's *Planning Algorithms*, Modern Robotics chapters 10 (motion planning) and 13 (wheeled robots), TU Berlin IMRCLab's motion-planning syllabus and CMU's syllabus ground the taxonomy in configuration space, graph/sampling/optimization methods, kinodynamics and multi-robot planning. CoRL 2025's LaDi-WM paper provides conference grounding for predictive models. Springer content and full ICRA/RSS session schedules were not retrieved; this is not a track-by-track conference census.

Scope is reusable concepts for any robot, with mobile/drone examples where dynamics matter. **Collision-free arm motion generation** and **Long-horizon / task-and-motion planning** remain owned by Manipulation and are cross-referenced in prerequisite text, not recreated as nodes. No electronics curriculum is duplicated. Robot learning, control, perception and SLAM are prerequisites or neighboring branches rather than additional planning taxonomies. MoveIt 2 and cuRobo retain the existing Manipulation names; rows here add planning relations, not new product identities. A future merge/sync must reconcile shared-name rows, not create duplicate products.

All projects start in simulation/offline. Their cost bands, durations, wow ratings and work-hour splits are estimates, not quotes or measured outcomes. Costs exclude existing computers, GPUs, API usage and staff time. A one-week frontier onboarding project is a tiny teaching approximation, not reproduction of a large published model. Longer candidates reach three-plus months, original evaluation designs and monitored full-stack integration. Full custom hardware and beyond-SOTA claims are intentionally absent. All work is software-only (100/0/0), matching the actual proposed tasks rather than inventing assembly work.

## Queries actually run

Initial discovery queries (titles/snippets selected primary pages; only fetched full pages enter the manifest):

1. `robot motion planning course configuration space graph search sampling trajectory planning` (7 results)
2. `robot neural diffusion motion planning world model predictive planning 2025 2026` (8 results)

The first query and opened textbooks/course sources established the classical nodes; the second added the distinction between learned trajectory proposals and planning through predictive world models. The resulting 17-node working taxonomy preceded the three saturation queries below. Official documentation, author pages, primary papers and repositories were then retrieved directly to fill individual rows. `sources_consulted` contains 28 distinct URLs with retrieved content, not all search-result URLs. Stable older primary sources support classical algorithms; DINO-WM (2024), cascaded diffusion and LaDi-WM (2025), cuRobo/OMPL current documentation and two 2026 preprints support frontier discussion. Vendor timings and preprint claims are not independently reproduced here.

## Saturation-stop evidence

Unit of a new entry: a previously uncovered **knowledge node**, not another paper, application or implementation. Denominator is 17 scoped nodes. Three consecutive discovery queries each returned zero new scoped nodes (0/17 = 0%, below 10%). Saturation **was reached for this taxonomy**, not for all literature or tools.

| Consecutive query | Results reviewed | New nodes | Mapping / evidence |
|---|---:|---:|---|
| `robot planning taxonomy multi robot coverage uncertainty symbolic motion planning survey` | 6 | 0 | Coverage surveys map to coverage; multi-robot task/motion taxonomies map to MAPF, symbolic planning and executives. Manipulation-specific TAMP remains cross-referenced, not duplicated. |
| `robot planning 2025 2026 diffusion GPU world model task planning` | 6 | 0 | Sampling-based world-model planning, Rolling-WAM, WorldDP, MinD and video-world-model surveys map to predictive world models / learned planners; simulation announcements do not introduce another planning primitive. |
| `robot planning kinodynamic belief space coverage behavior trees PDDL recent methods` | 6 | 0 | Semantic uncertainty maps to belief-space planning; dispersive search/BOWConnect to kinodynamics; H-AIM/EmboTeam to language, PDDL and executives; KiTe to kinodynamics/uncertainty. |

Stopped expanding the taxonomy after that sequence. Subsequent direct retrievals checked details and provenance rather than expanding nodes. Search snippets were not treated as authoritative: arXiv 2601.11063 now resolves to **EmboTeam**, not the older H-AIM title in a search result. It is cited under its retrieved current title. Two guessed arXiv IDs (1707.01792, 2309.00941) returned unrelated physics/sequence-model papers and were excluded entirely. These are not supporting planning sources.

Retrieval gaps: detailed Nav2 costmap/MPPI/Smac/BT URLs (with and without `rolling`) and GitHub subdirectory URLs yielded no usable content through the fetch tool. The main rolling Nav2 overview and repository were retrieved instead; no parameter-level plugin claims depend on those failed pages. Guessed MPNet/steer repository URLs, a CHOMP PDF, TrajOpt site and a guessed CBS PDF also yielded no content and are excluded. D* Lite's primary paper, the MAPF example repository and the university syllabi provide the narrower claims actually retained. No standalone TEB source was opened: it is named only as a contrasting local-planning family, not given an implementation/performance claim.

## Top three: qualitative benefit/cost judgement

1. **Graph search & incremental replanning** — accessible to software students, visually legible expansion/replanning animations and direct warehouse/navigation relevance; no hardware purchase.
2. **Navigation stacks & costmaps** — visible destination-reaching and obstacle-clearance demos, reusable ROS 2/Nav2 integration skills and partner relevance. Supplied maps/localization avoid scope creep into SLAM.
3. **Behavior trees & task executives** — approachable async programming, compelling failure/recovery demos and cross-platform executive skills reusable throughout the lab.

The ratio `(accessibility × visual impact × ecosystem relevance) / cost` is a qualitative judgement, not fabricated measured ecosystem scores or numeric division by a zero simulation price. No assumption is made that low-cost robot learning is already the lab's validated wedge.

## Gaps, unknowns and representation decisions

- Current EU robot kit prices, complete lab budgets, GPU availability and hosted-model costs are unknown. No hardware purchase is required by these proposals. Reference rows favor executable tools/models over adding unsourced TurtleBot/Gazebo/Isaac hardware specifications.
- Release years use `unknown` rather than inferred repository creation dates; a future Notion syncer must map that sentinel to missing numeric data. Open-source checkboxes describe the referenced implementation, not all components, hardware, weights, datasets or optional commercial features. Check licenses before reuse. Cascaded diffusion is conservatively false because code/weights were not established by its opened paper.
- SayCan and the cascaded-diffusion framework are Simulator/Tool rows, not fabricated portable checkpoints. DINO-WM is World model. Ruckig, TOPPRA, Fields2Cover and the educational MAPF code have distinct roles; no production-ready fleet or safety certification is implied.
- `Built by`, `Used by` and `Relevant orgs` are empty; attribution is in `Builder (if not in map)`. Tool and project relations resolve locally. Cross-branch prerequisites are human-readable text, not unresolved local relations.
- There is no standalone manipulation TAMP, electronics, SLAM or low-level control node. LLM task planning emphasizes generic room/inspection skills and validation rather than recreating manipulation's long-horizon pipeline. Vehicle, aerial and continuous-time fleet dynamics need platform-specific follow-up; legged contact planning is not fully covered here.
- DWA/TEB, CHOMP/TrajOpt, CBS optimality assumptions and full belief-space planning deserve deeper primary-paper coverage in verification. No solver benchmark or real-world safety is established by this research. Publication claims remain bounded to their source settings.
- Empty environments/tasks, infeasible goals, stale sensing, invalid starts and action failures are explicitly included in project evaluation proposals. Those experiments have **not** been run. There is no implemented or visually verified robot/UI deliverable.
- No hiring/outreach work, Notion pilot deduplication or final Holygraph architecture occurred. Local project names were checked against `existing_projects.json`; later cross-branch merging still requires review.

## Reproducible validation

Adapted from the Manipulation report. Run from the repository root; no dependencies or network needed. This checks emitted field sets and schema choices, percentages, local relations, opened-manifest citations, three projects per node and cross-file node/project-name deduplication. It cannot establish that a paper's results reproduce.

```python
import json
import re
from pathlib import Path

data = json.loads(Path('output/knowledge_planning.json').read_text())
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
assert data['branch'] == 'Planning'
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
    assert node['Branch'] == 'Planning' and node['Status'] == 'Draft'
    assert node['Project ideas'] == '' and node['_accessibility_reason']
for row in data['robots_models'] + data['project_candidates']:
    assert row['Knowledge nodes'] and set(row['Knowledge nodes']) <= names['nodes']
    if 'Robots & models' in row:
        assert row['Branch'] == 'Planning'
        assert row['Robots & models'] and set(row['Robots & models']) <= names['robots_models']
        assert set(row['Prerequisites']) <= names['project_candidates']
        assert row['Project'] not in row['Prerequisites']
        assert sum(row[k] for k in ['Software %', 'Mechanical %', 'Electrical %']) == 100
        assert row['Status'] == 'Idea'
        assert not row['Relevant orgs']
    else:
        assert isinstance(row['Open source'], bool)
        assert isinstance(row['Release year'], int) or row['Release year'] == 'unknown'
        assert row['Status'] == 'To verify'
        assert not row['Built by'] and not row['Used by']
assert 8 <= len(data['nodes']) <= 20
for node in names['nodes']:
    assert sum(node in p['Knowledge nodes'] for p in data['project_candidates']) == 3
assert len(data['top3']) == 3
assert len({x['Node'] for x in data['top3']}) == 3
assert all(x['Node'] in names['nodes'] and x['justification'] for x in data['top3'])
for filename in ['knowledge_manipulation', 'knowledge_embedded_electronics']:
    other = json.loads(Path(f'output/{filename}.json').read_text())
    assert not names['nodes'] & {row['Node'] for row in other['nodes']}
existing = json.loads(Path('output/existing_projects.json').read_text())
assert not names['project_candidates'] & {row['Project'] for row in existing}
print(f'PASS: {checks} select/multi-select/status values validated against schema')
print('PASS: exact row fields, unique names, 100% work splits, local relations and per-row source URLs')
print('PASS: 3 projects per node, Draft/To verify/Idea statuses, 3 top nodes; no formula or deprecated fields')
print('PASS: no duplicate Manipulation/Embedded nodes or existing project names')
print(f"COUNTS: nodes={len(data['nodes'])}, robots_models={len(data['robots_models'])}, project_candidates={len(data['project_candidates'])}, distinct_sources={len(sources)}")
```

Validation output:

```text
PASS: 713 select/multi-select/status values validated against schema
PASS: exact row fields, unique names, 100% work splits, local relations and per-row source URLs
PASS: 3 projects per node, Draft/To verify/Idea statuses, 3 top nodes; no formula or deprecated fields
PASS: no duplicate Manipulation/Embedded nodes or existing project names
COUNTS: nodes=17, robots_models=14, project_candidates=51, distinct_sources=28
```

No existing executable research-data test suite is provided; the adapted validation above is the targeted check. This is a research artifact, not a visually checked robot demo.
