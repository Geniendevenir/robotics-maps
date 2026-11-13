# Simulation knowledge research

## Scope and method

Discovery-only output for the **Simulation** branch: 14 nodes (3 Fundamental, 7 Applied, 4 Frontier), 14 robots/models/tools, 42 project candidates (exactly three per node), and 36 distinct successfully opened primary-source URLs. No Notion reads/writes, verification-agent pass, coverage-critic pass or Holygraph consolidation were performed. Everything remains **To verify** / **Idea**. Source pages were retrieved with Python urllib and read as stripped text; no robot experiments were run.

Taxonomy grounding:
- **Springer Handbook of Robotics, second edition:** the official multimedia companion https://handbookofrobotics.org/ exposes the chapter list. Chapters 3 (Dynamics), 6 (Model Identification), 16 (Design and Performance Evaluation), 37 (Contact Modeling and Manipulation), and 45 (World Modeling) ground the separation of dynamics, calibration, contact, evaluation and world representation. Only the companion and chapter list were checked, not inaccessible publisher chapter text.
- **Modern Robotics, Lynch & Park:** https://modernrobotics.northwestern.edu/nu-gm-book-resource/ and its opened section 8.5 https://modernrobotics.northwestern.edu/nu-gm-book-resource/8-5-forward-dynamics-of-open-chains/ explain the relationship between forward dynamics and numerical simulation.
- **MIT course syllabi/notes:** https://underactuated.mit.edu/contact.html explicitly distinguishes smooth dynamics, impacts and contact constraints; https://manipulation.csail.mit.edu/ provides the broader software-to-physical-model context. These motivate contact fidelity and gradient validation without remapping manipulation skills.
- **RSS 2025 program:** https://roboticsconference.org/2025/program/papers/ includes the Scaling Robot Learning session and the ManiSkill3 GPU-parallel simulation/rendering demonstration, plus a VLA Models session with Unified World Models. This supports parallel simulation and learned simulators as distinct current research directions. ICRA/CoRL programs were not separately audited; RSS supplied the conference grounding.

The local manipulation and embedded/electronics pilot node names were checked before designing the taxonomy. Contact here means collision models and solver validity, not compliant manipulation control. Deformables here means numerical/material fidelity, not deformable object manipulation. Embedded/HIL simulators were excluded. Generic RL algorithms, general robot dynamics instruction, perception models and robot planning are prerequisites or secondary branches, not extra Simulation nodes.

## Discovery queries actually run

Discovery used the arXiv Atom API (`https://export.arxiv.org/api/query`) with explicit `search_query`, `sortBy` and `max_results`. Official docs and repositories were then opened directly rather than manufacturing one search per row. The first pass used three submitted-date queries (8 results each):
- `all:"robot simulation" AND (all:"survey" OR all:"benchmark")` — 8 results.
- `all:"Gaussian" AND all:"robot" AND all:"simulation"` — 8 results.
- `all:"world model" AND all:"robot simulation"` — 8 results.

Targeted relevance-sorted bibliographic lookups (up to 3 results each):
- `ti:"RialTo"` — 0 results. No result; no RialTo product claims or rows were fabricated.
- `ti:"Genesis" AND all:"simulation"` — 3 results. Results concerned unrelated quantum/astronomy simulation, so they were excluded; the official Genesis docs/repository supplied robotics evidence.
- `ti:"world" AND ti:"simulator" AND all:"robot"` — 3 results. Relevant abstracts were reviewed; selected primary abstract pages were opened directly for detailed rows.
- `ti:"Gaussian" AND all:"real-to-sim"` — 3 results. Relevant abstracts were reviewed; selected primary abstract pages were opened directly for detailed rows.

All successful citations are listed in the JSON's `sources_consulted`; failed URLs below are not counted. Stable foundations may be older (Modern Robotics, domain randomization); current official documentation, maintained repositories and 2025–2026 papers supply the current snapshot. Mutable `stable`/`latest` documentation is not a historical version guarantee. This research does not assert an exhaustive 2026 SOTA ranking or copy unverified speed claims.

## Saturation-stop evidence

Unit: a new scoped **knowledge node**, not each new paper, engine or application sector. The 14-node taxonomy was already written and checkpointed before this final sequence. All queries below were actually issued, using `sortBy=submittedDate&max_results=8`. Each returned eight entries, reviewed by title and abstract. Three consecutive queries added 0/14 nodes (0%, below 10%); taxonomy saturation reached. This does not mean the literature or hardware catalog is exhaustive. Repeated papers across queries do not count as new entries.

| Consecutive query | Results reviewed | New nodes / denominator | Mapping |
|---|---:|---:|---|
| `all:"robot simulation" AND (all:"survey" OR all:"benchmark")` | 8 | 0 / 14 | Verifier exposure maps to benchmark integrity; VoxLution and Gym-Anything to procedural scenes; LucidLyra to digital twins; under-ice and planetary work to sensor/scene coverage; MuJoCable to contact/multiphysics. Mobility information capacity is control theory, not a new Simulation node. |
| `all:"robot simulation" AND (all:"differentiable" OR all:"multiphysics" OR all:"contact")` | 8 | 0 / 14 | Soft-helicoid models and FlashNeRD map to learned dynamics; TactileLab to sensor simulation; SpaRV and φ-RIE to twin reconstruction; PhySGA to scene generation; caregiver simulation to sensor/scene workflows; learned critics are primarily planning/control. |
| `all:"robot simulation" AND (all:"world model" OR all:"Gaussian" OR all:"procedural")` | 8 | 0 / 14 | LucidLyra and φ-RIE map to digital twins; Demiurge, WALL-SS, DF³ and DriftWorld to learned simulators; AgriGen to procedural scenes and ROS integration. Mobility information capacity remains out of scope as a separate node. |

### Reviewed result identifiers

Query 1:
- Mobility Information Capacity of Multi-Robot Systems: Safety-Aware Maneuver Design — http://arxiv.org/abs/2611.10298v1
- Learning the Task or Learning the Verifier? Rethinking Criteria Exposure in Embodied Self-Improvement — http://arxiv.org/abs/2611.08318v1
- VoxLution: Evolving Voxels for High-Fidelity 3D Scene Generation — http://arxiv.org/abs/2610.41501v1
- Gym-Anything for Robotics: Scaling physical simulations with digital agents — http://arxiv.org/abs/2610.40565v1
- LucidLyra: Feed-Forward Generative 3D Scene Reconstruction and Joint Understanding via Multi-Task Distillation — http://arxiv.org/abs/2610.40495v1
- Benchmarking 3D Reconstruction for Under-Ice Robotic Perception in Arctic Environments — http://arxiv.org/abs/2610.19097v1
- Simulation for Planetary Robotic Perception and Autonomy: A Concise Survey of Recent Capabilities and Gaps — http://arxiv.org/abs/2609.34743v1
- MuJoCable: Reduced-Order Surface-Routed Cable Transmission for Tendon-Driven Robots — http://arxiv.org/abs/2609.09612v2

Query 2:
- Data-Driven Precision Control of Soft Helicoid Robots — http://arxiv.org/abs/2611.11709v1
- TactileLab: Sim-to-Real Dexterous Robot Manipulation with Efficient Shear-Sensitive Tactile Simulation — http://arxiv.org/abs/2611.07881v1
- SpaRV: Sparse Radiance Voxels for Scalable Geometrically Consistent LiDAR-Visual Mapping and Rendering — http://arxiv.org/abs/2610.25665v1
- PhySGA: A Physics-Space Grounded Agentic Framework for Generalizable and Interactive 3D Composition — http://arxiv.org/abs/2610.20560v1
- FlashNeRD: Performance-First Contact-Rich Neural Robot Dynamics — http://arxiv.org/abs/2610.09130v1
- Infant simulator with an embodied caregiver: Generating infant-perspective touch and vision during social interaction — http://arxiv.org/abs/2610.05997v1
- Optimal Control with Learned Critics under Unmodeled State Dependencies — http://arxiv.org/abs/2610.05359v1
- φ-RIE: From Photorealistic Reconstruction to Interactive Environments — http://arxiv.org/abs/2609.26795v1

Query 3:
- Mobility Information Capacity of Multi-Robot Systems: Safety-Aware Maneuver Design — http://arxiv.org/abs/2611.10298v1
- LucidLyra: Feed-Forward Generative 3D Scene Reconstruction and Joint Understanding via Multi-Task Distillation — http://arxiv.org/abs/2610.40495v1
- Demiurge: Forging Navigable 4D Worlds via Autoregressive Video Rerendering — http://arxiv.org/abs/2610.14685v1
- φ-RIE: From Photorealistic Reconstruction to Interactive Environments — http://arxiv.org/abs/2609.26795v1
- AgriGen: Large-Scale Scene Generation Framework for Photorealistic Agricultural Robotics Simulation — http://arxiv.org/abs/2609.25725v1
- WALL-SS: Scaling Long-horizon World Models via Next-Scale Autoregression — http://arxiv.org/abs/2608.26239v1
- DF$^3$: World Modeling via Decoder-Free Feature Forecasting in Autonomous Navigation — http://arxiv.org/abs/2608.02428v1
- DriftWorld: Fast World Modeling through Drifting — http://arxiv.org/abs/2607.15065v3

Discovery stopped after the three-query sequence. The later direct Handbook companion retrieval completed the required textbook grounding without introducing a new node. Query-result identifiers above are discovery evidence, not an assertion that full paper text was read; only source URLs listed in the JSON support detailed rows.

## Failed or unusable retrievals

- `https://docs.ros.org/en/rolling/Tutorials/Intermediate/URDF/URDF-Main.html`: Anubis bot challenge rather than tutorial text. Replaced by the official `ros/urdf_tutorial` repository plus MuJoCo modeling and Gazebo SDF documentation.
- `https://link.springer.com/referencework/10.1007/978-3-319-32552-1` and `https://www.springer.com/gp/book/9783319325507`: client JavaScript challenge. Replaced by the official Handbook multimedia companion chapter list; no inaccessible chapter-content claims made.
- `https://github.com/NVlabs/diff-tactile`, `https://github.com/real-stanford/real-to-sim-to-real`, `https://github.com/InternRobotics/InternWorld`, `https://github.com/NVlabs/warp`: HTTP 404. These guessed retrieval candidates were not used as sources. NVIDIA Warp was found at `https://github.com/NVIDIA/warp`; real-to-sim and world-simulator evidence came from directly opened arXiv abstract pages.
- `https://mujoco.readthedocs.io/en/stable/XMLreference.html`: HTTP 403; modeling/computation pages sufficed.
- `https://roboticsconference.org/2025/program/sessions/`: HTTP 404; accepted-papers page includes session labels and was usable.
- `https://robocasa.ai/docs/introduction/overview.html`: redirect stub, not substantive documentation; `https://robocasa.ai/` provided actual project content. The separately attempted NVlabs RoboCasa GitHub endpoint did not provide usable README evidence and is not counted.

No failed or challenge pages appear in `sources_consulted`. Retrieval failures were content/URL-specific, not a missing shell environment; no new dependency installation was needed.

## Top three: qualitative benefit/cost judgement

1. **Robot and scene formats: URDF, MJCF, SDF & USD** — text editing and automated checks match the team's strengths; a broken-versus-fixed robot makes a clear video. Portable, trustworthy assets benefit every engine and community without requiring a hardware purchase.
2. **Sensor simulation, rendering & synthetic labels** — RGB/depth/semantic overlays make convincing demos quickly and exploit software/AI skills. Good labels, noise models and timestamps are reusable for ManiSkill/Isaac and dataset work; begin with affordable rendering rather than chasing photorealism.
3. **Domain randomization & transfer stress testing** — visible controlled perturbations and held-out robustness tests directly test the low-cost robot-learning wedge instead of assuming it. Start sim-only; collect calibration evidence before buying or attempting transfer.

The requested accessibility × visual impact × ecosystem relevance / cost ratio is qualitative: simulation's zero incremental hardware price is not divided numerically, and ecosystem scores are not invented.

## Gaps, unknowns and representation decisions

- Complete hardware quotes, EU shipping/VAT, GPU ownership, compute bills, commercial-license eligibility and deployment performance are **unknown**. `€0 (sim only)` excludes the existing computer and GPU/cloud consumption. Three proposals involve real tabletop calibration or twin evaluation and conservatively use the `€500-5k` band, not an unverified sub-€500 kit promise. Mechanical/electrical shares are estimated work hours.
- SO-101 proposals focus on simulator calibration and uncertainty, not duplicating the existing Notion **Sim-to-real transfer on the SO-101**, ACT pick-and-place, assembly/teleoperation or world-model planning projects. They produce the measurements needed to support transfer; no generic SO-101 transfer-policy project was added. The twin audit evaluates fixed policies; it is not the existing real-world RL fine-tuning project.
- Proposed names and ideas were manually compared with all 11 entries in `output/existing_projects.json`. Exact node-name deduplication covers both local pilot files. No live Notion deduplication was performed, as explicitly prohibited. A future approved sync must still match existing rows.
- Tool names shared with the manipulation pilot use its exact `Name` strings (**MuJoCo**, **ManiSkill**, **SO-101**). **Isaac Sim / Isaac Lab** also follows the existing-project reference string. These are reusable references, not instructions to create duplicate Notion records.
- `Open source` means a referenced implementation is publicly open-source, not that every associated asset, robot, model checkpoint or renderer has identical rights. In particular, Isaac Lab being open source does not imply all Isaac Sim components/assets have Apache terms. Asset/code/weights licenses must be checked independently before use. RoboCasa's project links code and data; individual asset terms were not audited.
- `Release year` is **unknown** rather than an invented numeric year; a future syncer must treat that string as missing for the numeric Notion field. `Built by`, `Used by` and `Relevant orgs` are empty because ecosystem resolution is a later pipeline step; attribution is in `Builder (if not in map)`. No formula fields or auto-managed reverse relations are emitted. `Project ideas` is empty everywhere.
- Every node has simulator/tool references. Learned world simulators additionally have DreamerV3 as a concrete model reference; BWM is cited as research evidence, not represented as a separately verified checkpoint/access offering. No primary-code audit or local reproduction of BWM/soft-body twin claims was performed.
- Candidate axes intentionally span reproduction, adaptation and original experimental designs, but not a promised beyond-SOTA result or full-custom robot. Scripted measurement tasks are marked Scripted rather than claiming full autonomy; only the actual learned single-task microbenchmark is marked Learned single task. The three stages per node chain via project-name prerequisites; overall Holygraph ring balancing is outside this discovery assignment.
- Proposed evaluation protocols include normal, empty/degenerate and error/failure trials. No code/demo exists here, so no unit tests, simulator performance tests or visual verification can be claimed. This is research, not a verified robot capability.
- Less-developed areas for a later coverage critic: tactile sensor physics in depth, specialized underwater/planetary simulators, detailed material-model selection and cross-engine asset conversion support matrices. They do not warrant invented product specifications. Hiring and organization outreach were excluded.

## Reproducible validation

There is no package/build/CI test configuration in this research-only repository. The following standard-library script checks exact pilot-style field sets, all select/multi-select/status choices from the schema, percentages, local relation targets, prerequisite cycles, source manifests, deduplication and the three-candidates-per-node requirement. It makes no network or Notion calls. Run from the repository root:

```python
import json
import re
from pathlib import Path

root = Path.cwd()
data = json.loads((root/'output/knowledge_simulation.json').read_text())
schema = (root/'schemas/notion-schema.md').read_text()
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
pilot = json.loads((root/'output/knowledge_manipulation.json').read_text())
groups = [('nodes','Knowledge Map','Node'),('robots_models','Robots & Models','Name'),('project_candidates','Projects (Holygraph)','Project')]
assert set(data) == {'branch','nodes','robots_models','project_candidates','top3','sources_consulted'}
assert data['branch'] == 'Simulation'
sources = set(data['sources_consulted'])
assert len(sources) == len(data['sources_consulted']) >= 15
names = {}; checks = 0
for group, section, title in groups:
    names[group] = {r[title] for r in data[group]}
    assert len(names[group]) == len(data[group])
    for row in data[group]:
        expected = set(pilot[group][0]) | ({'_accessibility_reason'} if group == 'nodes' else set())
        assert set(row) == expected, (group, row[title],set(row)^expected)
        for field, choices in options[section].items():
            if field in row:
                values = row[field] if isinstance(row[field],list) else [row[field]]
                for value in values:
                    assert value in choices, (row[title],field,value)
                    checks += 1
        urls = set(re.findall(r'https?://[^\s;]+',row.get('Sources',row.get('References',''))))
        assert urls and urls <= sources, (row[title],urls-sources)
assert 8 <= len(data['nodes']) <= 20
for n in data['nodes']:
    assert n['Branch']=='Simulation' and n['Status']=='To verify'
    assert n['Project ideas']=='' and n['_accessibility_reason']
    assert 3 <= sum(n['Node'] in p['Knowledge nodes'] for p in data['project_candidates']) <= 6
for r in data['robots_models']:
    assert set(r['Knowledge nodes']) <= names['nodes'] and r['Knowledge nodes']
    assert isinstance(r['Open source'],bool) and r['Status']=='To verify'
    assert r['Release year']=='unknown' or isinstance(r['Release year'],int)
    assert not r['Built by'] and not r['Used by']
for p in data['project_candidates']:
    assert sum(p[k] for k in ['Software %','Mechanical %','Electrical %']) == 100
    assert set(p['Knowledge nodes']) <= names['nodes']
    assert set(p['Robots & models']) <= names['robots_models']
    assert set(p['Prerequisites']) <= names['project_candidates'] and p['Project'] not in p['Prerequisites']
    assert p['Status']=='Idea' and p['Branch']=='Simulation'
def visit(name, stack):
    assert name not in stack, ('prerequisite cycle',stack,name)
    for p in data['project_candidates']:
        if p['Project']==name:
            for req in p['Prerequisites']: visit(req,stack+[name])
for p in names['project_candidates']: visit(p,[])
assert len(data['top3'])==3 and len({x['Node'] for x in data['top3']})==3
assert all(x['Node'] in names['nodes'] and x['justification'] for x in data['top3'])
for filename in ['knowledge_manipulation','knowledge_embedded_electronics']:
    other=json.loads((root/f'output/{filename}.json').read_text())
    assert not names['nodes'] & {r['Node'] for r in other['nodes']}
existing=json.loads((root/'output/existing_projects.json').read_text())
assert not names['project_candidates'] & {r['Project'] for r in existing}
assert 'Used in projects' not in json.dumps(data)
print(f'COUNTS: nodes={len(data["nodes"])}, robots_models={len(data["robots_models"])}, project_candidates={len(data["project_candidates"])}, distinct sources_consulted={len(sources)}')
print(f'PASS: {checks} select/multi-select/status values match schemas/notion-schema.md; all work percentages sum to 100')
print('PASS: exact pilot-style fields; unique names; source URLs; relations; acyclic prerequisites; 3 candidates per node; top3; statuses')
print('PASS: no node-name overlap with either pilot; no project-name overlap with existing_projects.json; no Used in projects')
```
