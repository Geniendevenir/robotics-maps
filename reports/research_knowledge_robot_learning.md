# Robot learning discovery research

## Scope and interpretation

Discovery only: **16 new knowledge nodes, 24 new reference models/tools, 48 project candidates (three per node), and 49 distinct opened primary-source URLs**. Three fundamentals establish interfaces, data plumbing and evaluation; nine applied nodes cover practical learning methods; four frontier nodes cover grounded planning, cross-embodiment transfer, continual learning and uncertainty. Knowledge/model rows are `To verify`; project rows are `Idea`. No Notion calls, PR, live synchronization, independent verifier pass or coverage-critic pass. Only the two requested deliverables are committed.

Read `CLAUDE.md`, `devin/playbooks/knowledge-researcher.md`, `schemas/notion-schema.md` and both manipulation/electronics outputs. The checked-in schema controls fields and choices; no formula fields or deprecated project backlinks are emitted. All explanations target software students encountering robotics for the first time. `_accessibility_reason` is supplied on every node, and `Project ideas` is empty.

The proposed taxonomy was retained, with the deployment node narrowed to **Real-time learned-policy execution & inference scheduling**. Its subject is observation age, action queues and chunk stitching, not the existing embedded/edge-hardware node. The planning node concerns learned grounding and executable API contracts, not another manipulation task-and-motion-planning pipeline. Fine-tuning is about adaptation methodology, not another generalist/VLA survey. MIT's current manipulation course provides university-course grounding (including its learned perception/control organization); primary ACT, R3M, CrossFormer, KnowNo, MimicGen, RoboCasa and pi0 papers/project pages provide RSS/CoRL research grounding. No claim of a complete textbook or conference-session survey; Springer and Modern Robotics were not opened in this pass.

Accessibility and starter cost refer to a small offline/simulation first demo, not training a foundation model from scratch. Budget bands exclude existing computers, GPU rentals and model API use; these costs are **unknown** until the experiment is specified. Durations, percentages, wow ratings and complexity axes are explicitly student planning estimates. Simulation/offline projects are 100/0/0 software/mechanical/electrical; the two supervised physical testing projects are 85/10/5 and budgeted €500-5k, not quoted kit prices. Neither asserts certified safe autonomy.

## Queries actually run

Primary pages were first retrieved directly from the proposed taxonomy's named references. This avoids relying on web-search snippets for bibliographic claims. The JSON `sources_consulted` array is the deduplicated manifest of usable opened pages, not an unvisited reading list. Multiple URLs for a paper and its official code are separate retrieved URLs, not separate independent experiments. There are well over 15 distinct primary works even after collapsing paper/code pairs.

Discovery used the working 16-node taxonomy supplied in the task. These three arXiv API queries were actually executed **consecutively**, each with `sortBy=submittedDate&max_results=10`:

1. `all:"robot learning" AND (all:"evaluation" OR all:"policy")`
2. `all:"robot learning" AND (all:"adaptation" OR all:"reward" OR all:"representation")`
3. `all:"robot learning" AND (all:"uncertainty" OR all:"continual" OR all:"embodiment")`

Reproduce the request shape with Python's standard library:

```python
from urllib.parse import quote
from urllib.request import urlopen
q = 'all:"robot learning" AND (all:"evaluation" OR all:"policy")'
url = ('http://export.arxiv.org/api/query?search_query=' + quote(q)
       + '&sortBy=submittedDate&max_results=10')
print(urlopen(url).read().decode())
```

Additional **bibliographic**, not taxonomy-expansion, API lookups were run afterward: `ti:"KnowNo"` (no entry), `ti:"RoboCat"` (RoboCat), `ti:"Fail" AND all:"robot" AND all:"conformal"` (no entry), `ti:"Diffusion Policy"` (three related diffusion-policy variants), `ti:"RLPD"` (no entry), and `ti:"Implicit Q-Learning"` (IQL and two variants). These used `max_results=3`. KnowNo and RLPD were resolved through their actual paper titles/official pages rather than treating an acronym miss as absence of research. Subsequent retrievals filled fields, checked availability and corrected URLs, without adding knowledge nodes.

## Saturation-stop evidence

**Reached: three consecutive queries with 0/16 new scoped knowledge nodes (0%, below 10%).** A new entry means a new knowledge node, not every new paper or model. This is saturation of the bounded proposed taxonomy against three recent ten-result samples, **not exhaustive literature saturation**. Distinct results were reviewed as titles plus abstracts from the API; only sources actually opened separately can support detailed row claims. Search results change over time.

| Consecutive query | Results reviewed | New nodes / existing nodes | Mapping / evidence |
|---|---:|---:|---|
| Evaluation / policy query above | 10 | 0 / 16 | BEHAVIOR solution and stochastic manipulation challenges → evaluation; robotic chess adaptation → fine-tuning; asynchronous control → execution scheduling; diffusion multimodality → generative policies; BATCH → cross-embodiment. Ego Guidance and RoboMoCap belong to the existing human-video/data nodes, not new rows. PCTac is tactile hardware outside this slice. Coloured-noise exploration is a method within existing robot RL rather than a separate new node. |
| Adaptation / reward / representation query above | 10 | 0 / 16 | Repeats Ego Guidance, chess adaptation, PCTac, coloured-noise exploration, asynchronous control, RoboMoCap, multimodal diffusion and BATCH. UniOMA → representations (multimodal perception prerequisite); Augmentron → augmentation. No distinct additional knowledge node. |
| Uncertainty / continual / embodiment query above | 10 | 0 / 16 | Asynchronous control → scheduling; BATCH → cross-embodiment; D&A → reward specification; ODE Policy → action representation/generative control; Data Inoculation → interactive imitation. Open-HumanWAM and WorldBridge update existing human-video/world-model nodes. OdorSpaces is a sensory-navigation application, not a new generic robot-learning method; embodied scientific discovery is an application of evaluation/closed-loop learning. Coloured-noise exploration remains within existing robot RL. |

Four selected 2026 primary abstracts were then opened to check current-state details: [D&A](https://arxiv.org/abs/2611.03622), [control-aware asynchronous command generation](https://arxiv.org/abs/2611.11089), [Augmentron](https://arxiv.org/abs/2611.09145), and [Robotic Data Inoculation](https://arxiv.org/abs/2610.39054). They are preprints/reported research, not independently reproduced capability claims. Stable older sources remain necessary for DAgger, CQL/IQL, R3M/VC-1, Code as Policies, SayCan and KnowNo. 2024-2025 sources include CrossFormer, RoboCasa, pi0, FAST, GR00T N1 and RTC; current official LeRobot/openpi/GR00T docs supplement them.

Retrieval problems were resolved before finalizing citations: MIT `/imitation.html` and `/learning.html` returned 404, replaced by the usable course root; the LIBERO project landing page returned no useful content, replaced by its official repository and paper; guessed RLPD project/repository URLs returned 404, replaced by `github.com/ikostrikov/rlpd` and its actual paper; guessed FAST GitHub and NVIDIA/Eureka URLs returned 404, replaced by the official FAST Hugging Face model card and `github.com/eureka-research/Eureka`. A guessed KnowNo repository returned 404; the authors' actual project page supplies its code link. An unversioned LeRobot async URL contained only a redirect notice, so the actual `main/en/async` page was opened and cited. Three initially tried arXiv IDs resolved to unrelated papers (2502.09992, 2307.05949) or a different offline-RL paper (2306.00972); unrelated papers are excluded, while 2306.00972 is retained only for its actual implementation/benchmarking findings. A bulk re-open attempt exceeded the tool's 32-concurrent-call limit for its last 16 requests; these are not counted as newly retrieved evidence, and the pages used had already been opened individually/in smaller batches. Failed/empty/redirect-only pages are absent from the final manifest.

## Top three: qualitative benefit/cost judgement

1. **Action chunking & action tokenization** — FAST reconstruction and chunk-length experiments produce visible trajectory movies cheaply, connect to ACT/LeRobot practice, and isolate a transferable systems idea without buying an arm. Compression improvement is not automatically control improvement.
2. **Data augmentation & synthetic demonstration generation** — MimicGen makes data coverage visible and offers reusable student experiments with a modest seed dataset. Simulation-first demonstrations test the low-cost-learning wedge rather than presuming it; generation failures and untouched test scenes are central.
3. **Real-time learned-policy execution & inference scheduling** — Delay/queue overlays create a strong systems demo with near-zero incremental hardware cost, then an optional supervised physical extension. Direct relevance to open policy deployment and students' software strengths, without implying that async queues or quantization certify safety.

The requested `(accessibility × visual impact × ecosystem relevance) / cost` is a qualitative ranking: no invented ecosystem scores and no division by a zero simulation price.

## Updates to existing nodes

These are **report-only suggestions**, keyed by exact existing node names. None creates a duplicate knowledge row.

- **Vision-Language-Action models (VLAs)**: add [GR00T N1](https://arxiv.org/abs/2503.14734), [openpi](https://github.com/Physical-Intelligence/openpi), and [SmolVLA adaptation docs](https://huggingface.co/docs/lerobot/smolvla). Separate vision-language semantic capability, action-head training and actual supported embodiments. Model openness must be checked per artifact/license.
- **Reinforcement learning for robots**: add [CQL](https://arxiv.org/abs/2006.04779), [IQL](https://arxiv.org/abs/2110.06169), and [Efficient Online RL with Offline Data](https://arxiv.org/abs/2302.02948) as methodological links. Offline training and later online improvement have different data-coverage and safety assumptions; no new HIL-SERL project is proposed.
- **World models & world action models**: [RoboCat](https://arxiv.org/abs/2306.11706) is a goal-conditioned policy, not automatically a predictive world model. [pi0](https://arxiv.org/abs/2410.24164) is an action flow policy, not evidence of world-model planning. WorldBridge appeared in discovery results but was not separately opened, so no detailed update based on it is asserted.
- **Teleoperation & robot data collection**: add [LeRobotDataset v3](https://huggingface.co/docs/lerobot/lerobot-dataset-v3) for timing/episode metadata and [Data Inoculation](https://arxiv.org/abs/2610.39054) as a clearly labeled 2026 shared-control research direction. Keep basic collection distinct from policy-driven corrective data acquisition.
- **Learning from human video**: [R3M](https://arxiv.org/abs/2203.12601) and [VC-1](https://arxiv.org/abs/2303.18240) support visual representation pretraining. Do not equate useful image embeddings with recovered executable robot actions. Ego Guidance/Open-HumanWAM were discovery leads only; no detailed facts asserted without separately opening them.
- **Imitation learning (behavior cloning)**: add [DAgger](https://arxiv.org/abs/1011.0686) for induced-state distribution shift, [ACT](https://arxiv.org/abs/2304.13705) for chunking and [Diffusion Policy](https://diffusion-policy.cs.columbia.edu/) for multimodal action distributions. Lower supervised prediction loss is not a sufficient rollout-success metric.
- **Robot datasets & benchmarks**: add [LIBERO](https://arxiv.org/abs/2306.03310), [RoboCasa](https://arxiv.org/abs/2406.02523), and [Open X-Embodiment](https://github.com/google-deepmind/open_x_embodiment). RLDS repository is archived; its episode format remains a useful interchange reference. Distinguish benchmark suites, underlying data and policy checkpoints.
- **Sim-to-real transfer**: [MimicGen](https://mimicgen.github.io/) and [RoboCasa](https://arxiv.org/abs/2406.02523) motivate broader synthetic coverage. Neither source makes arbitrary simulator demonstrations transferable to an SO-101; camera/action calibration and real held-out tests remain necessary. No duplicate sim-to-real project is emitted.

## Gaps, unknowns and representation decisions

- All eight excluded knowledge titles were omitted. The two pilot knowledge files were also checked programmatically for title collisions. Existing names may appear in prerequisite prose but are not re-created.
- All pilot robot/model rows and every `Robots & models` name in `output/existing_projects.json` form the exclusion/resolution set. Therefore **ACT, SmolVLA, SO-101, LeRobot, pi0, Diffusion Policy, OpenVLA, Octo, Isaac Sim / Isaac Lab and MuJoCo are not new rows**. ACT and SmolVLA relation names use the exact existing spellings, not new aliases. LeRobotDataset v3 is explicitly a data-format tool, not a second LeRobot framework row. RT-1-X is the specifically released checkpoint, not an invented umbrella RT-X checkpoint.
- New references include tools and benchmarks, not 24 new robot bodies: this branch deliberately studies learning with existing hardware. CQL, IQL and RLPD rows name reference implementations, not pretrained universal checkpoints. RTC, KnowNo, Eureka, Code as Policies and SayCan are tools/frameworks. CrossFormer and RoboCat are policies. GR00T N1 is version-pinned to its 2025 paper rather than assigning newer repository features to that original model.
- Release years refer to the cited first paper/release, not the last repository update or conference year; unknown dates are numeric `null`, never an invented date or the string `unknown` in a numeric field. Other unknown quantities are stated as unknown in text.
- `Open source` means publicly inspectable referenced implementation, not blanket OSI approval or commercial rights. In particular VC-1/CortexBench show CC-BY-NC terms; their rows state the limitation. RoboCat is conservatively false because runnable public weights/access were not established. Code, pretrained weights, robot data, simulator assets and commercial APIs require separate license checks.
- All `Built by`, `Used by` and `Relevant orgs` relations are empty; attribution is in `Builder (if not in map)`. Robot/model and project knowledge relations resolve to this file's nodes; project model relations resolve locally or through the specified pilot/existing-project sets. Candidate prerequisites form 16 three-step chains without external project dependencies.
- Project titles were checked against all local project files; the 11 existing project descriptions were manually read for substance. No plain ACT pick/place, language-commanded SmolVLA arm, HIL-SERL, SO-101 sim-to-real, human-video data engine or world-model planner is proposed. The adaptation, offline-RL and continual-learning candidates are comparative experiments with distinct deliverables rather than renamed versions of those projects.
- Complexity is deliberately honest: novelty 1-4, autonomy 2-4, hardware 1-2 and integration 1-5. Frontier here means difficult research questions and rigorous comparisons, not fabricated beyond-SOTA novelty or a full-custom-robot build. High mechanical/electrical percentages would be misleading for representation/data/learning experiments. General control theory, tactile mechanics, new perception modalities and hiring are outside scope.
- No implementation, training run, physical rollout or visual verification was performed. The deliverable is research; proposed filmable demos, normal/empty/error trials, performance and durations remain experimentally unverified. Statistical planner uncertainty is not a safety certification. Real deployment requires independent command limits, emergency stop, supervision and a rollback protocol.
- Bibliographic coverage is not an exhaustive late-2026 SOTA audit. Foundation-model fine-tuning compute, current EU procurement totals and unattended lifelong-learning feasibility remain unknown. Query samples may miss niche learning paradigms; verification/coverage stages should assess that before approval or any later sync.

## Reproducible validation

Run the following standard-library script from the repository root. It adapts the manipulation report's schema validator and adds cross-file deduplication, external model-name resolution and cycle checks. It validates structure, not scientific correctness or live availability; opened-source evidence is the research retrieval described above.

```python
import json
import re
from pathlib import Path

data = json.loads(Path('output/knowledge_robot_learning.json').read_text())
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
assert data['branch'] == 'Robot learning'
sources = set(data['sources_consulted'])
assert len(sources) == len(data['sources_consulted']) >= 15
assert all(re.fullmatch(r'https?://\S+', url) for url in sources)
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
    assert node['Branch'] == 'Robot learning' and node['Status'] == 'To verify'
    assert node['Project ideas'] == '' and node['_accessibility_reason']
    assert 2 <= len(re.findall(r'[.!?](?:\s|$)', node['What it is'])) <= 3
pilots = [json.loads(Path('output/' + f + '.json').read_text())
          for f in ['knowledge_manipulation', 'knowledge_embedded_electronics']]
existing_projects = json.loads(Path('output/existing_projects.json').read_text())
external_models = {r['Name'] for d in pilots for r in d['robots_models']}
external_models.update(n for p in existing_projects for n in p['Robots & models'])
excluded_nodes = {'Vision-Language-Action models (VLAs)', 'Reinforcement learning for robots',
                  'World models & world action models', 'Teleoperation & robot data collection',
                  'Learning from human video', 'Imitation learning (behavior cloning)',
                  'Robot datasets & benchmarks', 'Sim-to-real transfer'}
excluded_nodes.update(n['Node'] for d in pilots for n in d['nodes'])
norm = lambda x: ' '.join(x.casefold().split())
assert not {norm(n) for n in names['nodes']} & {norm(n) for n in excluded_nodes}
assert not {norm(n) for n in names['robots_models']} & {norm(n) for n in external_models}
external_projects = {p['Project'] for p in existing_projects}
external_projects.update(p['Project'] for d in pilots for p in d['project_candidates'])
assert not {norm(n) for n in names['project_candidates']} & {norm(n) for n in external_projects}
for row in data['robots_models'] + data['project_candidates']:
    assert row['Knowledge nodes'] and set(row['Knowledge nodes']) <= names['nodes']
    if 'Robots & models' in row:
        assert row['Branch'] == 'Robot learning'
        assert row['Robots & models'] and set(row['Robots & models']) <= names['robots_models'] | external_models
        assert set(row['Prerequisites']) <= names['project_candidates']
        assert row['Project'] not in row['Prerequisites']
        assert all(isinstance(row[k], (int, float)) and 0 <= row[k] <= 100
                   for k in ['Software %', 'Mechanical %', 'Electrical %'])
        assert sum(row[k] for k in ['Software %', 'Mechanical %', 'Electrical %']) == 100
        assert row['Status'] == 'Idea' and not row['Relevant orgs']
        assert row['Deliverable'] and row['Description'] and 'Level' not in row and 'Mix check' not in row
    else:
        assert isinstance(row['Open source'], bool)
        assert row['Release year'] is None or (type(row['Release year']) is int and 1950 <= row['Release year'] <= 2026)
        assert row['Status'] == 'To verify' and not row['Built by'] and not row['Used by']
        assert row['Builder (if not in map)']
assert 12 <= len(data['nodes']) <= 17
assert 20 <= len(data['robots_models']) <= 30
for node in names['nodes']:
    assert sum(node in p['Knowledge nodes'] for p in data['project_candidates']) == 3
assert len(data['project_candidates']) == 3 * len(data['nodes'])
graph = {p['Project']: p['Prerequisites'] for p in data['project_candidates']}
seen, active = set(), set()
def visit(name):
    assert name not in active, ('cycle', name)
    if name in seen:
        return
    active.add(name)
    for parent in graph[name]:
        visit(parent)
    active.remove(name)
    seen.add(name)
for name in graph:
    visit(name)
assert len(data['top3']) == 3 and len({x['Node'] for x in data['top3']}) == 3
assert all(set(x) == {'Node', 'justification'} and x['Node'] in names['nodes'] and x['justification'] for x in data['top3'])
assert 'Used in projects' not in json.dumps(data)
print(f'PASS: {checks} select/multi-select/status values validated against schema')
print('PASS: exact row fields, unique names, 100% work splits, per-row source URLs and resolved relations')
print('PASS: excluded/pilot knowledge and model deduplication; local project-title deduplication; acyclic prerequisites')
print('PASS: 3 projects per node, To verify/Idea statuses, 3 top nodes; no formula or deprecated fields')
print(f"COUNTS: nodes={len(data['nodes'])}, robots_models={len(data['robots_models'])}, projects={len(data['project_candidates'])}, sources={len(sources)}")
```

Validation output (the exact Python block above, extracted and executed from this report):

```text
PASS: 720 select/multi-select/status values validated against schema
PASS: exact row fields, unique names, 100% work splits, per-row source URLs and resolved relations
PASS: excluded/pilot knowledge and model deduplication; local project-title deduplication; acyclic prerequisites
PASS: 3 projects per node, To verify/Idea statuses, 3 top nodes; no formula or deprecated fields
COUNTS: nodes=16, robots_models=24, projects=48, sources=49
```

No executable test suite for research JSON was found in the repository; validation covers the data/schema boundary, not empirical reproducibility. A final `git diff --check` is run separately. No Notion access or robot UI/visual check is involved.
