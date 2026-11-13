# Mechanisms & actuation — discovery research

Date: 2026-11-13. Branch: `research/knowledge-mechanisms-actuation`.

## Scope and deliverables

Discovery only: **18 knowledge nodes, 10 new robot/component/tool rows, 54 project candidates (three per node), 33 distinct opened primary-source URLs**. Knowledge and reference rows remain **To verify**, projects **Idea**. No Notion access, verifier pass, coverage-critic pass, Holygraph architecture, PR or main-branch push. An early taxonomy-only WIP was committed and pushed as `8aca939`; this report describes the completed discovery file.

Read the playbook, CLAUDE.md, schema, both pilot JSON files, manipulation report/validator and both knowledge verification/gaps reports before writing. Avoided their pitfalls: no unsupported delivered prices, no guessed release years, no component masquerading as a complete robot, no universal power-cut-is-safe assumption, no electrical-bus/FOC/gripper node duplicates, no automatic reverse relations or read-only formula fields.

## Taxonomy grounding and boundaries

Springer's **second-edition publisher contents** explicitly lists **Mechanism and Actuation** (Scheinman, McCarthy, Song, pp. 67–90). Only the contents/metadata were read, not the complete chapter. Modern Robotics **§8.9 Actuation, Gearing, and Friction** grounds transmission and reflected-inertia reasoning. MIT **2.12** course description and opened chapters **2 (Actuators and Drive Systems)** and **3 (Robot Mechanisms)** ground the mechanical subdivisions. MIT **865.24** machine-design notes distinguish belts, screws, capstans, planetary, strain-wave and cycloidal drives.

Recent research grounding uses **RSS 2024** pneumatic/tendon-arm and **RSS 2025** RUKA proceedings abstracts and the **CoRL 2025** ToddlerBot author project/repository. DLR David's official page explicitly links its variable-stiffness mechanisms to **ICRA 2008/2011** and IROS research. This is topic-level grounding, **not a complete audit of ICRA/RSS/CoRL 2026 session tracks**. Newer sources supplement stable mechanics rather than replacing foundational geometry with unsourced trend claims.

| Node | Level |
|---|---|
| Electric actuator architectures: mechanical trade-offs | Fundamental |
| Actuator sizing: torque, inertia and thermal duty | Fundamental |
| Spur and planetary gear trains | Fundamental |
| Cycloidal reducers and output mechanisms | Applied |
| Strain-wave gearing and flexspline design | Applied |
| Timing-belt and capstan transmissions | Applied |
| Lead screws, ball screws and linear joint packaging | Applied |
| Linkages, cams and parallel mechanism design | Fundamental |
| Tendon routing, antagonism and underactuated mechanisms | Applied |
| Backdrivability, friction and mechanical transparency | Fundamental |
| Series-elastic actuator mechanics | Applied |
| Variable-stiffness and antagonistic spring mechanisms | Frontier |
| Bearings, structures and printed load paths | Fundamental |
| CAD and design for manufacture of robot joints | Fundamental |
| Hydraulic and pneumatic transmission mechanics | Applied |
| Soft pneumatic actuators and compliant-body fabrication | Applied |
| Artificial muscles: electrohydraulic and smart-material actuation | Frontier |
| Integrated legged and humanoid joint co-design | Frontier |

Seven fundamentals, eight applied nodes and three frontiers. The scope is mechanical hardware and design. Control laws, FOC, power electronics, communications, gripper functions, grasp planning and locomotion policies remain in their existing branches. Motor architectures concern torque-speed, packaging and support, not driver implementation. Linkages concern mechanism synthesis/load paths, not a duplicate general kinematics course. Tendons concern routing, slack and mechanical coupling, not a second gripper node.

Existing pilot names are used **verbatim** where needed: `MIT Mini Cheetah actuator` is reused in project relations without re-emitting its row. Text prerequisites reference `Electronics fundamentals for robots`, `Smart servos & serial actuator buses`, `BLDC motor control & field-oriented control (FOC)` and `Grasp mechanics`. Knowledge prerequisites are schema text, not relation arrays. Every actual relation name resolves inside this file or the two pilots. Ecosystem relations are empty; attributions remain in builder text to avoid dangling organizations.

## Discovery queries actually run

Search results selected pages; **snippets alone are not counted as opened sources**. Official URLs were also opened directly to avoid redundant product queries. Initial/targeted queries:

1. `robot mechanism design actuators syllabus MIT mechanical robotics transmission`
2. `Springer Handbook Robotics actuators mechanisms mechanical design contents`
3. `robot actuator mechanical design quasi direct drive series elastic variable stiffness hydraulic HASEL primary research`
4. `RSS 2025 robot actuator mechanism design tendon transmission`
5. `robot actuator mechanical design quasi direct drive series elastic variable stiffness hydraulic HASEL`
6. `MIT Cheetah actuator design proprioceptive actuator Wensing 2017 mechanical`
7. `series elastic variable stiffness actuator DLR official robotics`
8. `robot mechanism belt capstan drive cycloidal actuator ball screw design official`
9. `robot actuator sizing thermal torque speed maxon motor continuous torque official`
10. `MIT fab machine design transmissions capstans belts screws Jake Read`
11. `Prusa designing 3D printed mechanical parts orientation strength tolerances`
12. `Festo fluidic muscle DMSP pneumatic official`
13. `Stanford humanoid robot ToddlerBot 2025 open hardware actuator design`
14. `site.thk.com ball screw mechanism rolling motion official`
15. `site.nabtesco.com precision reduction gears RV mechanism cycloidal`
16. `site.bostondynamics.com atlas hydraulic electric 2024`

The RSS query was inadvertently repeated in a later batch; it is not counted as a separate saturation observation. The HASEL query was shortened after the first retrieval. Search metadata dates are not used to infer product release dates.

## Saturation stop

Unit: a **new knowledge node**, not a new paper, product or organization. Denominator: the 18-node taxonomy already committed in the WIP. The final three discovery queries were submitted as one batch, in the order below; each yielded **0/18 new nodes (0%, <10%)**. Saturation reached at this taxonomy granularity; no claim of literature exhaustiveness.

| Query | Results reviewed | New nodes / existing | Mapping |
|---|---:|---:|---|
| `robot mechanical actuation taxonomy gears tendons soft artificial muscles hydraulic variable stiffness` | 8 | 0/18 = 0% | Mechanical-actuation and soft-fluidic reviews map to motor architecture, soft actuators, artificial muscles and variable stiffness. AI Wiki was not treated as a primary source. |
| `robot actuator mechanism research 2025 2026 humanoid transmission thermal backdrivable` | 8 | 0/18 = 0% | Precision reducers, gear-ratio trade-offs, humanoid actuation, QDD knee prosthesis and differential/parallel transmissions map to sizing, backdrivability, reducers, linkages and joint co-design. Search snippets were used for taxonomy mapping only, not as established performance evidence. |
| `robot mechanism design frontier compliant origami magnetic piezoelectric shape memory actuators` | 8 | 0/18 = 0% | SMA, piezoelectric and magnetic origami map to artificial-muscle mechanisms, compliant structures and linkages. These are acknowledged subfamilies rather than invented new adoption trends. |

After this stop, direct openings of the **2025 SMA microactuator** and **2021 PNAS magnetic-origami** papers strengthened the already present artificial-muscle node; they added sources and a model-only project, not new taxonomy nodes. No further expansion queries were run.

## Opened-source ledger

All 33 URLs below returned readable page/PDF text through content retrieval. Each JSON row cites at least one of these URLs. Multiple URLs from one organization remain distinct documents, not independent corroboration. Primary means textbook/course publisher, original paper/author page, institutional record, official project repository or manufacturer documentation. The ledger records what was read, not external replication of its claims.

| # | Opened primary source | Evidence used / limits |
|---|---|---|
| 1 | https://link.springer.com/book/10.1007/978-3-319-32552-1 | Springer Handbook (2nd edition): publisher contents, Mechanism and Actuation chapter; not full chapter text |
| 2 | https://modernrobotics.northwestern.edu/nu-gm-book-resource/8-9-actuation-gearing-and-friction/ | Modern Robotics §8.9: gear ratios, reflected inertia and friction |
| 3 | https://ocw.mit.edu/courses/2-12-introduction-to-robotics-fall-2005/pages/lecture-notes/ | MIT 2.12 lecture-note index: actuators, mechanisms, statics and compliance |
| 4 | https://meche.mit.edu/featured-classes/introduction-robotics | MIT current featured-course description: drives, transmissions and fabrication |
| 5 | https://ocw.mit.edu/courses/2-12-introduction-to-robotics-fall-2005/9158f91fc935aae58345446fc110f6e7_chapter2.pdf | MIT 2.12 chapter 2 PDF: actuator and drive-system teaching text |
| 6 | https://ocw.mit.edu/courses/2-12-introduction-to-robotics-fall-2005/5c238d7e3445337ed40d4af83d9d2239_chapter3.pdf | MIT 2.12 chapter 3 PDF: joint primitives and serial/parallel mechanisms |
| 7 | https://www.freecad.org/features.php | FreeCAD official features: parametric mechanical design |
| 8 | https://onshape-to-robot.readthedocs.io/en/latest/ | onshape-to-robot official docs: export formats, joints and kinematic loops |
| 9 | https://www.harmonicdrive.net/technology | Harmonic Drive official technology: strain-wave and planetary mechanisms (vendor claims) |
| 10 | https://github.com/open-dynamic-robot-initiative/open_robot_actuator_hardware | ODRI hardware repository: assembly, pulleys, printed/machined parts and test stands |
| 11 | https://softroboticstoolkit.com/ | Soft Robotics Toolkit: fabrication, modeling and testing resource scope |
| 12 | https://softroboticstoolkit.com/book/pneunets-bending-actuator | PneuNets official toolkit section: elastomer bending actuators |
| 13 | https://www.roboticsproceedings.org/rss20/p099.html | RSS 2024 paper abstract: pneumatic-muscle tendon arm |
| 14 | https://roboticsproceedings.org/rss21/p131.html | RSS 2025 paper abstract: RUKA tendon/underactuation design |
| 15 | https://ruka-hand.github.io/ | RUKA author project page: hand design and assembly links |
| 16 | https://www.skf.com/group/products/rolling-bearings | SKF official catalogue overview: bearing families and load directions |
| 17 | https://www.dlr.de/en/rm/research/robotic-systems/humanoids/david/mechatronics-of-david | DLR David official mechatronics: antagonism, BAVS and Floating Spring Joint |
| 18 | https://elib.dlr.de/99795/ | DLR author repository abstract: variable-stiffness component/design trade-offs (full paper restricted) |
| 19 | https://dspace.mit.edu/entities/publication/8b15bcc8-c288-43aa-b923-69ce3c13b818 | MIT institutional repository: 2017 Cheetah actuator paper metadata/abstract |
| 20 | https://doi.org/10.1126/sciadv.adi9319 | HALVE 2024 primary paper: electrohydraulic actuator and voltage limitation |
| 21 | https://fab.cba.mit.edu/classes/865.24/topics/mechanical_design/mechanical_design/transmissions/ | MIT 865.24 machine-design notes: belts, capstans, screws and reducers |
| 22 | https://support.maxongroup.com/hc/en-us/articles/360013761160-Motor-data-and-simulation | maxon official support: torque/current, thermal and motor-data interpretation |
| 23 | https://www.festo.com/us/en/p/fluidic-muscle-id_DMSP | Festo official DMSP product page: pulling fluidic muscle |
| 24 | https://toddlerbot.github.io/ | ToddlerBot author project page: CoRL 2025 platform and design |
| 25 | https://github.com/hshi74/toddlerbot | ToddlerBot repository: release chronology, design notes and split licenses |
| 26 | https://help.prusa3d.com/article/modeling-with-3d-printing-in-mind_164135 | Prusa official print-aware modeling guide: orientation and fabrication constraints |
| 27 | https://www.nabtescoprecision.com/engineering/ | Nabtesco official RV engineering: two-stage reduction and bearing support (vendor claims) |
| 28 | https://bostondynamics.com/blog/electric-new-era-for-atlas/ | Boston Dynamics 2024 announcement: hydraulic Atlas retirement and electric successor |
| 29 | https://bostondynamics.com/blog/atlas-evolution-from-research-robot-to-industrial-humanoid/ | Boston Dynamics March 2026 platform retrospective: manufacturer context, not independent deployment evidence |
| 30 | https://arxiv.org/abs/2504.17736 | 2025 author preprint: tendon-driver torque, velocity, noise, thermal and endurance benchmarking |
| 31 | https://www.nature.com/articles/s41378-025-01026-x | 2025 original SMA microactuator paper: folding and magnetic latching |
| 32 | https://www.pnas.org/doi/full/10.1073/pnas.2110023118 | 2021 original PNAS paper: magnetically actuated Kresling origami mechanism |
| 33 | https://github.com/Rhoban/onshape-to-robot | Rhoban/onshape-to-robot repository: implementation and MIT license |

Failed/empty direct retrievals were **excluded**: the guessed `github.com/onshape-to-robot/onshape-to-robot` repository (replaced with official docs and Rhoban repository), HEBI robotics landing URL, guessed THK ball-screw paths, Nabtesco corporate precision path, the guessed CMU series-elastic PDF, Artimus HASEL path and guessed Prusa anisotropy page. Nabtesco's dedicated precision engineering page and MIT transmission notes supply the necessary reducer/screw evidence instead. Pinocchio's repository was also opened successfully during exploration but is not needed by any row and is not included in the 33-source delivery manifest. Thus 33 is the distinct **retained** opened-source count, not all network attempts.

## Project ladder and estimates

Each node has exactly three proposals: **offline onboarding**, **bounded bench or digital experiment**, and **integrative comparison/custom subsystem**. All 54 names were checked against both pilot candidate lists and `output/existing_projects.json`. No re-proposal of the custom SO-101 gripper or introductory servo drive. Project prerequisites form separate three-step chains within each node; final global chaining belongs to the Holygraph architect.

Complexity spans reproduce/adapt/combine and off-the-shelf virtual components through custom parts/subsystems. Autonomy stays **2 - Scripted** because mechanism validation should not pretend to be learned autonomy. No 5 - Beyond SOTA claims. An advanced mechanical project can remain low autonomy; the four axes are not a single difficulty slider. Integrative powered builds target **3+ months**, consistent with the lab's 4–6 month horizon; no full humanoid build is proposed.

All **node-level starter cost bands are €0 (sim only)** because they refer to CAD, data analysis or an offline mechanical model, not a complete usable actuator. Accessibility includes realistic skill barriers beyond merely opening software. Project-level bands distinguish zero-new-hardware studies, **<€500** hand-driven coupons/fixtures, and **€500–5k** integrative physical test stands. Bands, duration, wow, accessibility and work-hour splits are **planning judgements**, not vendor quotes or measured results. Shared printer/tools, workstation and competent supervision are assumed; delivered EU price/VAT/shipping remain unknown. CAD and mechanical analysis count as **Mechanical %** even without fabrication; an offline project can therefore be 70% Software / 30% Mechanical / 0% Electrical.

Each proposal includes nominal, unloaded/zero-input and bounded failure trials, repeatability and limitations. No build or visual demonstration has been performed. Pressure hardware requires rated parts, regulation, relief, guards and competent review. Electrohydraulic high-voltage work is explicitly **model-only**: HALVE's reported 1100 V must not be mistaken for safe hobby voltage. Springs are captive; loads supported; mechanisms guarded. Power removal alone need not retain gravity loads. No human-contact trials, suspended payloads or free-standing legged demos.

## Top three: qualitative benefit/cost

1. **CAD and design for manufacture of robot joints** — accessibility 5; immediately visible assemblies, reusable robot-description exports and manufacturability reviews. Zero-incremental-hardware start and direct usefulness for improving low-cost robots. Test the learning-on-low-cost-hardware wedge rather than assume it.
2. **Timing-belt and capstan transmissions** — accessibility 4; highly legible remote-drive demos and ODRI relevance, with a hand-driven belt fixture before powered procurement. Pretension and lost-motion measurement are reusable skills.
3. **Linkages, cams and parallel mechanism design** — accessibility 4; striking motion transformations from CAD/cardboard, cheap initial materials, relevance to humanoid packaging without buying an entire humanoid.

The requested `(accessibility × visual impact × ecosystem relevance) / cost` is a **qualitative ranking**, not a fabricated numeric ecosystem metric or division by zero simulation cost. Sizing and bearings are indispensable prerequisites even though they are less visually striking.

## Unknowns and representation decisions

- Unknown numerical release years are **null**, not a string in a numeric Notion field; human-readable unknowns remain in text. ToddlerBot and RUKA years come from opened release/proceedings evidence.
- The schema lacks an Actuator/Component kind: actuator modules, reducers, fabrication resources and commercial fluidic muscles use **Simulator/Tool**, **N/A** form/model fields, and descriptions identifying their real nature. Only complete hand/humanoid platforms use Robot.
- `Open source` is not a commercial-reuse guarantee. ToddlerBot is true for published implementation/design availability but explicitly records **MIT code / CC BY-NC-SA non-commercial hardware**. ODRI and onshape-to-robot license availability is documented. RUKA and PneuNets are conservatively false pending full license-scope checks, despite public design resources. A future syncer should not erase this nuance.
- No Unitree/Tesla-style internal actuator specs were guessed. Atlas is context in source text, not a newly invented purchasable actuator row.
- `_accessibility_reason` is deliberately retained per this discovery brief, despite pilot verification removing private keys for sync. It is **not a Notion field** and must be excluded by any later syncer. No deprecated Project ideas content, Used in projects reverse field, project Level formula or Mix check is emitted. Knowledge Level remains the required select.
- Remaining depth gaps: full fatigue/materials qualification, roll/roller-screw procurement specifics, quantitative FEM validation, comprehensive piezo/SMA/magnetic product coverage and late-2026 conference schedules. Those do not establish new taxonomy nodes at this granularity. Hiring research is out of scope.
- Independent verification and coverage review are subsequent pipeline steps; no claim that these discovery rows are Verified.

## Reusable validation

Adapted from the manipulation report: checked-in schema choices, exact row fields (plus the required private accessibility key), null release years, local/pilot relation resolution, duplicate names across both pilots/existing projects, counts, source membership, percentage totals and acyclic prerequisite chains. The validator establishes structural consistency, **not factual correctness or that a page was opened**; the research ledger above provides source-access evidence.

Run from the repository root:

```python
import json
import re
from pathlib import Path

data = json.loads(Path('output/knowledge_mechanisms_actuation.json').read_text())
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
assert data['branch'] == 'Mechanisms & actuation'
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
pilot_names = {k:set() for k in names}
for filename in ['knowledge_manipulation', 'knowledge_embedded_electronics']:
    pilot = json.loads(Path('output/' + filename + '.json').read_text())
    for group, _, title in groups:
        pilot_names[group].update(row[title] for row in pilot[group])
        assert not names[group] & pilot_names[group], ('pilot duplicate', group)
existing = json.loads(Path('output/existing_projects.json').read_text())
if isinstance(existing, dict):
    existing = existing.get('projects', existing.get('project_candidates', []))
assert not names['project_candidates'] & {r['Project'] for r in existing}
resolved = {k:names[k] | pilot_names[k] for k in names}
for node in data['nodes']:
    assert node['Branch'] == data['branch'] and node['Status'] == 'To verify'
    assert node['Project ideas'] == '' and node['_accessibility_reason']
for row in data['robots_models'] + data['project_candidates']:
    assert row['Knowledge nodes'] and set(row['Knowledge nodes']) <= resolved['nodes']
    if 'Robots & models' in row:
        assert row['Branch'] == data['branch']
        assert set(row['Robots & models']) <= resolved['robots_models']
        assert set(row['Prerequisites']) <= resolved['project_candidates']
        assert row['Project'] not in row['Prerequisites']
        assert all(isinstance(row[k], (int,float)) and 0 <= row[k] <= 100 for k in ['Software %','Mechanical %','Electrical %'])
        assert sum(row[k] for k in ['Software %','Mechanical %','Electrical %']) == 100
        assert row['Status'] == 'Idea' and not row['Relevant orgs']
    else:
        assert isinstance(row['Open source'], bool)
        assert isinstance(row['Release year'], int) or row['Release year'] is None
        assert not row['Built by'] and not row['Used by']
        assert row['Status'] == 'To verify'
assert 8 <= len(data['nodes']) <= 20
for node in names['nodes']:
    assert 3 <= sum(node in p['Knowledge nodes'] for p in data['project_candidates']) <= 6
assert len(data['top3']) == len({x['Node'] for x in data['top3']}) == 3
assert all(x['Node'] in names['nodes'] and x['justification'] for x in data['top3'])
graph = {p['Project']:p['Prerequisites'] for p in data['project_candidates']}
def visit(name, active, done):
    assert name not in active, ('cycle', name)
    if name in done or name not in graph:
        return
    active.add(name)
    for pre in graph[name]:
        visit(pre, active, done)
    active.remove(name)
    done.add(name)
done=set()
for name in graph:
    visit(name,set(),done)
print(f'PASS: {checks} select/multi-select/status values validated against schema')
print('PASS: exact row fields, unique names, 100% work splits, local/pilot relations and per-row source URLs')
print('PASS: 3 projects per node, To verify/Idea statuses, 3 top nodes; no formula or deprecated fields')
print('PASS: no pilot/existing-project name duplicates; project prerequisites are acyclic')
print(f"COUNTS: nodes={len(data['nodes'])}, robots_models={len(data['robots_models'])}, project_candidates={len(data['project_candidates'])}, distinct_sources={len(sources)}")
```

Validation output (executed directly from the Python block above):

```text
PASS: 751 select/multi-select/status values validated against schema
PASS: exact row fields, unique names, 100% work splits, local/pilot relations and per-row source URLs
PASS: 3 projects per node, To verify/Idea statuses, 3 top nodes; no formula or deprecated fields
PASS: no pilot/existing-project name duplicates; project prerequisites are acyclic
COUNTS: nodes=18, robots_models=10, project_candidates=54, distinct_sources=33
```

`git diff --check` completed without diagnostics. No existing executable test suite covers these research JSON files. No robot hardware, CAD tool installation or visual demo was tested; deliverables are research proposals, not working prototypes.
