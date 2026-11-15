import json
import re
from pathlib import Path

import pytest

from viz.scripts.check_lessons import (
    BRANCHES,
    GUIDE_INTRO_HEADINGS,
    _check_visuals,
    _check_resources,
    _check_word_count,
    check_urls,
    load_graph_nodes,
    url_reuse_warnings,
    validate_payload,
    word_count,
)


IMAGE_MD = (
    "![A diagram](/img/lessons/test.webp)\n"
    "*A test diagram. Source: [Fixture](https://example.org/source), CC BY 4.0.*"
)
MERMAID_MD = (
    "```mermaid\n"
    "flowchart LR\n"
    "  A[\"Measure\"] --> B[\"Act\"]\n"
    "  B --> A[\"Measure\"]\n"
    "```"
)


def _prepare_image_dir(tmp_path, monkeypatch):
    image_dir = tmp_path / "lesson-images"
    image_dir.mkdir(exist_ok=True)
    (image_dir / "test.webp").write_bytes(b"fixture")
    monkeypatch.setattr("viz.scripts.check_lessons.LESSON_IMAGE_DIR", image_dir)
    credits_path = tmp_path / "credits.json"
    credits_path.write_text(
        json.dumps({
            "test.webp": {
                "page_url": "https://example.org/source",
                "image_url": "https://example.org/test.webp",
                "license": "CC BY 4.0",
                "author": "Fixture author",
            }
        }),
        encoding="utf-8",
    )
    monkeypatch.setattr("viz.scripts.check_lessons.LESSON_CREDITS_PATH", credits_path)


def _fixture(tmp_path, lesson):
    graph_path = tmp_path / "graph.json"
    graph_path.write_text(
        json.dumps(
            {
                "nodes": [
                    {
                        "id": "k:test",
                        "type": "knowledge",
                        "name": "Test concept",
                    }
                ]
            }
        ),
        encoding="utf-8",
    )
    data_path = tmp_path / "lessons.json"
    data_path.write_text(
        json.dumps({"batch": "test", "lessons": [lesson]}),
        encoding="utf-8",
    )
    return load_graph_nodes(graph_path), json.loads(data_path.read_text(encoding="utf-8"))


def _valid_guide_payload():
    intro_sections = [
        "\n".join(
            [
                GUIDE_INTRO_HEADINGS[0],
                "",
                "> **Key idea:** Robots sense, estimate, decide, act, and check.",
                "",
                "- **Sensors read change:** cameras, encoders, and other devices report information about the robot or its surroundings.",
                "- **Actuators create effects:** motors, grippers, wheels, and legs turn commands into physical motion.",
                "- **Software runs a loop:** sensing and action repeat as the robot and environment change.",
                "- **Feedback checks progress:** new measurements show whether an action moved toward the goal.",
                "- **State changes over time:** joint positions and object locations can shift after every command.",
                "- **Goals guide behavior:** the same sensor readings can lead to different actions for different tasks.",
                "- **People define success:** robot behavior should fit task goals and remain safe to interact with.",
                "",
                IMAGE_MD,
            ]
        ),
        "\n".join(
            [
                GUIDE_INTRO_HEADINGS[1],
                "",
                "- **Mechanics constrain motion:** joints and links determine which positions an arm can reach.",
                "- **Electronics carry signals:** processors and buses connect software to sensors and motors.",
                "- **Control shapes behavior:** feedback turns a target into repeated actuator commands.",
                "- **Perception gives context:** vision and other sensors help interpret objects and scenes.",
                "- **Planning selects actions:** a robot chooses routes or motions under goals and limits.",
                "- **Learning uses examples:** demonstrations can teach a policy which actions fit a task.",
                "- **State estimation combines signals:** filters use noisy readings to track a more useful estimate of motion.",
                "- **Motion planning respects constraints:** routes must fit the robot's shape and reachable space.",
                "",
                MERMAID_MD,
            ]
        ),
        "\n".join(
            [
                GUIDE_INTRO_HEADINGS[2],
                "",
                "- **Hardware has tolerances:** backlash, friction, delay, and load affect physical results.",
                "- **Software sees samples:** programs receive sensor values at discrete times, not continuously.",
                "- **Timing becomes visible:** missed updates can make commands stale or unstable.",
                "- **Safety needs boundaries:** limits, stops, and cautious tests protect people and equipment.",
                "- **Simulation supports practice:** virtual models expose behavior before hardware trials.",
                "- **Real motors saturate:** actuator output has physical limits that software must respect.",
                "- **Power affects performance:** battery voltage and current limits can change actuator response.",
                "- **Tests reveal mismatch:** simulated and measured results differ when models simplify the world.",
            ]
        ),
        "\n".join(
            [
                GUIDE_INTRO_HEADINGS[3],
                "",
                "- **Start with a concept:** learn a field's vocabulary before choosing a tool or project.",
                "- **Follow prerequisites:** linked nodes show knowledge that supports later work.",
                "- **Compare resources:** begin with an accessible guide, then consult primary documentation.",
                "- **Build small tests:** verify one behavior at a time and record its outcome.",
                "- **Return to the graph:** revisit neighboring topics when a project reveals a knowledge gap.",
                "- **Treat links as paths:** use related nodes to connect theory, hardware, and projects.",
            ]
        ),
        "\n".join(
            [
                GUIDE_INTRO_HEADINGS[4],
                "",
                "1. **Build a safe tabletop arm** and identify its sensors, actuators, and communication ports.",
                "2. **Calibrate joints and cameras** before collecting demonstrations or evaluating motion.",
                "3. **Use simulation** to compare control settings and debug a simple manipulation task.",
                "4. **Record consistent demonstrations,** then train and evaluate a small learning baseline.",
                "5. **Share results with the community** and report limitations, failures, and setup details.",
                "6. **Use new tasks to find gaps** and revisit concepts that need more practice.",
            ]
        ),
    ]
    intro = "\n\n".join(intro_sections)
    body = (
        "## What this field is about\n"
        "> **Key idea:** Measure the system before deciding what to change.\n\n"
        "Control compares a requested state with sensor feedback, then changes actuator effort to reduce the difference.\n\n"
        "The plant includes mechanics, motors, and surroundings; friction, load, sampling time, and output limits shape the result.\n\n"
        f"{IMAGE_MD}\n\n"
        "## Where it sits in the robot loop\n"
        "- **Sensor feedback repeats the loop:** every cycle reads the plant before choosing another actuator command.\n"
        "- **The controller compares target and measurement:** their difference forms an error that guides the next output.\n"
        "- **The actuator moves the plant:** the next position becomes a new reading, closing the loop.\n\n"
        f"{MERMAID_MD}\n\n"
        "## The big ideas\n"
        "- **Measured position reflects sensor values:** a command alone does not show where the joint stopped.\n"
        "- **PID combines distinct responses:** P reacts to current error, I accumulates it, and D follows its rate of change.\n"
        "- **Sampling sets update timing:** a controller designed for 10 ms behaves differently at 100 ms.\n"
        "- **Saturation limits output:** integral windup continues while the motor command is capped.\n"
        "- **Load changes the response:** mass, gearing, and friction affect the gains that work in practice.\n\n"
        "## What you'll be able to build\n"
        "- **A simulation position loop** can test a 10-unit target before connecting a motor.\n"
        "- **A repeatable evaluation** can compare overshoot and settling time after changing one gain.\n"
        "- **A cautious hardware extension** can add output limits and check behavior under a small load.\n"
        "- **A final validation step** can compare commanded positions with encoder readings under load."
    )
    resources = [
        {
            "title": "Video",
            "url": "https://example.org/video",
            "format": "Video",
            "level": "Beginner",
            "why": "A visual introduction.",
        },
        {
            "title": "Article",
            "url": "https://example.org/article",
            "format": "Article",
            "level": "Intermediate",
            "why": "A focused explanation.",
        },
        {
            "title": "Reference",
            "url": "https://example.org/reference",
            "format": "Docs",
            "level": "Advanced",
            "why": "A technical reference.",
        },
    ]
    chapters = [
        {
            "id": f"chapter-{index}",
            "title": branch or "The robotics world",
            "branch": branch,
            "body_md": body,
            "start_here": ["k:test", "k:test", "k:test"],
            "resources": resources,
        }
        for index, branch in enumerate([*BRANCHES, None], 1)
    ]
    return {
        "title": "Robotics from zero",
        "intro_md": intro,
        "chapters": chapters,
        "sources": ["https://example.org/source"],
    }


def _valid_knowledge_lesson():
    summary = "A test concept explains how a robot uses measurements to choose its next action."
    body = (
        "## In one sentence\n"
        f"{summary}\n\n"
        + IMAGE_MD
        + "\n\n## Why it matters for us\n"
        + "> **Key idea:** A useful estimate changes the robot's next action.\n"
        + "- **Measurements reveal motion:** sensors show whether the robot moved as expected.\n"
        + "- **Feedback prevents blind commands:** the next action can respond to the latest state.\n"
        + "- **Simulation supports safe practice:** students can compare behavior before using hardware.\n\n"
        + "- **Robot errors accumulate:** a missed grasp can expose a mismatch between target and measured state.\n\n"
        + "## How it works\n"
        + "- **A sensor estimates position:** its reading describes part of the robot's current state.\n"
        + "- **The controller compares values:** target and measurement produce an error for correction.\n"
        + "- **A motor applies the output:** the next sensor reading closes the loop.\n\n"
        + MERMAID_MD
        + "\n\n## Key terms\n"
        + "- **Robot**: a machine that can sense and act.\n"
        + "- **State**: values describing the system.\n"
        + "- **Loop**: repeated execution of a program.\n"
        + "- **Target**: the value the controller wants the robot to reach.\n\n"
        + "## Before / after\n"
        + "- **Before:** The program acts without checking the current measurement.\n"
        + "- **After:** The program uses the measurement to adjust its next action.\n"
        + "\n\n## Try it in an afternoon\n"
        + "1. **Record a starting position** and write down the sensor reading.\n"
        + "2. **Change one command** and measure the result after the next update.\n"
        + "3. **Compare target and state** to decide whether the action moved in the right direction.\n"
        + "4. **Repeat with a small disturbance** and note how feedback changes the next command.\n"
        + "5. **Try another target** and check whether the corrections remain stable."
    )
    resources = [
        {
            "title": "Intro",
            "url": "https://example.org/intro",
            "format": "Article",
            "level": "Beginner",
            "why": "A first explanation.",
        },
        {
            "title": "Guide",
            "url": "https://example.org/guide",
            "format": "Docs",
            "level": "Intermediate",
            "why": "A practical guide.",
        },
        {
            "title": "Source",
            "url": "https://example.org/source",
            "format": "Book",
            "level": "Advanced",
            "why": "A deeper reference.",
        },
        {
            "title": "Video",
            "url": "https://example.org/video",
            "format": "Video",
            "level": "Beginner",
            "why": "A visual demonstration.",
        },
    ]
    valid_lesson = {
        "node_id": "k:test",
        "type": "knowledge",
        "name": "Test concept",
        "summary": summary,
        "lesson_md": body,
        "resources": resources,
        "sources": ["https://example.org/intro"],
    }
    return valid_lesson


def test_check_lesson_valid_and_broken_fixtures(tmp_path, monkeypatch):
    _prepare_image_dir(tmp_path, monkeypatch)
    valid_lesson = _valid_knowledge_lesson()
    graph_nodes, valid_data = _fixture(tmp_path, valid_lesson)
    assert validate_payload(valid_data, "valid fixture", graph_nodes) == []

    broken_lesson = {
        **valid_lesson,
        "node_id": "k:missing",
        "name": "Wrong name",
        "summary": "This summary does not match the lesson.",
        "lesson_md": "# Not allowed\n## Wrong heading\nToo short.",
        "resources": [{**valid_lesson["resources"][0], "format": []}],
        "sources": [],
    }
    _, broken_data = _fixture(tmp_path, broken_lesson)
    problems = validate_payload(broken_data, "broken fixture", graph_nodes)
    assert any("unknown node_id" in problem for problem in problems)
    assert any("headings" in problem for problem in problems)
    assert any("resources" in problem or "format" in problem for problem in problems)
    assert any("expected 4-6" in problem for problem in problems)
    assert any("sources" in problem for problem in problems)
    malformed_lesson = {**valid_lesson, "type": []}
    _, malformed_data = _fixture(tmp_path, malformed_lesson)
    malformed_problems = validate_payload(malformed_data, "malformed fixture", graph_nodes)
    assert any("unsupported type" in problem for problem in malformed_problems)


def test_knowledge_lesson_key_terms_must_be_bullets(tmp_path, monkeypatch):
    _prepare_image_dir(tmp_path, monkeypatch)
    lesson = _valid_knowledge_lesson()
    lesson["lesson_md"] = lesson["lesson_md"].replace(
        "- **Robot**: a machine that can sense and act.\n"
        "- **State**: values describing the system.\n"
        "- **Loop**: repeated execution of a program.\n"
        "- **Target**: the value the controller wants the robot to reach.",
        "Robot is a machine that can sense and act. "
        "State means values describing the system. "
        "Loop is repeated execution of a program. "
        "Target is the value the controller wants the robot to reach.",
        1,
    )
    graph_nodes, data = _fixture(tmp_path, lesson)

    problems = validate_payload(data, "prose terms fixture", graph_nodes)

    assert any("Key terms: has 0 bullets; expected 3-6" in problem for problem in problems)


def test_guide_chapters_require_bullet_lists(tmp_path, monkeypatch):
    _prepare_image_dir(tmp_path, monkeypatch)
    graph_nodes = {"k:test": {"type": "knowledge", "name": "Test concept"}}
    guide = _valid_guide_payload()
    assert validate_payload(guide, "valid guide fixture", graph_nodes) == []

    too_few_ideas = _valid_guide_payload()
    too_few_ideas["chapters"][0]["body_md"] = (
        too_few_ideas["chapters"][0]["body_md"]
        .replace(
            "- **Sampling sets update timing:** a controller designed for 10 ms behaves differently at 100 ms.\n"
            "- **Saturation limits output:** integral windup continues while the motor command is capped.\n"
            "- **Load changes the response:** mass, gearing, and friction affect the gains that work in practice.\n",
            "",
            1,
        )
    )
    problems = validate_payload(too_few_ideas, "short bullet fixture", graph_nodes)
    assert any("The big ideas: has 2 bullets; expected 3-5" in problem for problem in problems)


def _visual_fixture(robot_table=False):
    body = (
        "## In one sentence\n"
        "A measurement helps the robot choose its next action.\n\n"
        f"{IMAGE_MD}\n\n"
        "## Why it matters for us\n"
        "> **Key idea:** Keep a clear measurement loop.\n\n"
        "## How it works\n"
        "- **Measure** **estimate** **plan** **act** **check**\n\n"
        f"{MERMAID_MD}\n\n"
        "A short paragraph describes the robot system.\n\n"
        "## Key terms\n"
        "- **Encoder**: A sensor reports joint position.\n\n"
        "## Before / after\n"
        "- **Before:** The robot acts without using a measurement.\n"
        "- **After:** The robot adjusts its action from the measurement.\n\n"
        "## Try it in an afternoon\n"
        "1. Measure the current position.\n"
        "2. Change one input and record the output.\n"
        "3. Compare the result after a disturbance."
    )
    if robot_table:
        body += (
            "\n\n## What it is made of / how it works\n"
            "The device combines a motor, gears, and feedback.\n\n"
            "| Specification | Value |\n"
            "| --- | --- |\n"
            "| **Voltage** | 6-7.4 V |\n"
            "| **Encoder** | 12-bit magnetic |\n"
            "| **Bus** | Half-duplex serial |\n"
            "| **Joints** | Six |\n"
            "\n## Getting started\n"
            "1. Connect the device.\n"
            "2. Calibrate the sensor.\n"
            "3. Test a slow movement.\n"
        )
    return body


def _visual_errors(markdown, kind="knowledge"):
    errors = []
    _check_visuals(markdown, "visual fixture", kind, errors)
    return errors


def test_visuals_accept_complete_fixture(tmp_path, monkeypatch):
    _prepare_image_dir(tmp_path, monkeypatch)
    assert _visual_errors(_visual_fixture()) == []


@pytest.mark.parametrize(
    ("changed", "message"),
    [
        (lambda body: body.replace(IMAGE_MD + "\n\n", ""), "has 0 images"),
        (lambda body: body.replace(IMAGE_MD, IMAGE_MD + "\n\n" + IMAGE_MD + "\n\n" + IMAGE_MD),
         "has 3 images"),
        (lambda body: body.replace("![A diagram]", "![]"), "alt text"),
        (lambda body: body.replace("/img/lessons/test.webp", "https://example.org/image.webp"),
         "image path must be"),
        (lambda body: body.replace("test.webp", "test.png"), "image path must be"),
        (lambda body: body.replace("test.webp", "missing.webp"), "image file does not exist"),
        (lambda body: body.replace(IMAGE_MD, "![A diagram](/img/lessons/test.webp)\nCaption without source."),
         "caption must start with '*' and contain 'Source:'"),
        (lambda body: body.replace(
            "*A test diagram. Source: [Fixture](https://example.org/source), CC BY 4.0.*",
            "Caption. Source: [Fixture](https://example.org/source).",
        ), "caption must start with '*' and contain 'Source:'"),
        (lambda body: body.replace(
            "https://example.org/source", "https://wrong.example/source"
        ), "caption must link to its exact page_url"),
        (lambda body: body.replace(
            "A test diagram.", "Original test diagram."
        ), "must not contain 'Original'"),
        (lambda body: body.replace(IMAGE_MD, "Diagram: " + IMAGE_MD),
         "image must use ![alt]"),
    ],
)
def test_visual_image_rules(tmp_path, monkeypatch, changed, message):
    _prepare_image_dir(tmp_path, monkeypatch)
    errors = _visual_errors(changed(_visual_fixture()))
    assert any(message in error for error in errors)


@pytest.mark.parametrize("kind", ["intro", "chapter", "knowledge", "project"])
def test_visuals_require_mermaid_for_guide_and_concept_lessons(
    tmp_path, monkeypatch, kind
):
    _prepare_image_dir(tmp_path, monkeypatch)
    body = _visual_fixture()
    assert _visual_errors(body, kind) == []
    assert any(
        "requires a Mermaid flowchart" in error
        for error in _visual_errors(body.replace("\n\n" + MERMAID_MD, ""), kind)
    )


def test_visuals_enforce_key_idea_and_watch_out_counts(tmp_path, monkeypatch):
    _prepare_image_dir(tmp_path, monkeypatch)
    body = _visual_fixture()
    missing = body.replace("> **Key idea:** Keep a clear measurement loop.\n", "")
    assert any("Key idea callouts; expected exactly 1" in error
               for error in _visual_errors(missing))
    repeated = body.replace(
        "- **Measure** **estimate** **plan** **act** **check**",
        "> **Watch out:** Test with the motor unloaded.\n\n"
        "> **Watch out:** Keep hands clear.\n\n**measure** **estimate**",
    )
    assert any("Watch out callouts; maximum is 1" in error
               for error in _visual_errors(repeated))


def test_visuals_require_five_bold_spans(tmp_path, monkeypatch):
    _prepare_image_dir(tmp_path, monkeypatch)
    body = re.sub(r"\*\*([^*\n]+)\*\*", r"\1", _visual_fixture())
    assert any("bold spans; expected at least 5" in error
               for error in _visual_errors(body))


@pytest.mark.parametrize("item_kind", ["bullet", "step"])
def test_visuals_limit_list_items_to_thirty_words(tmp_path, monkeypatch, item_kind):
    _prepare_image_dir(tmp_path, monkeypatch)
    body = _visual_fixture()
    if item_kind == "bullet":
        body = body.replace(
            "- **Encoder**: A sensor reports joint position.",
            "- **Encoder**: " + "measurement " * 30,
        )
    else:
        body = body.replace(
            "1. Measure the current position.",
            "1. " + "measurement " * 31,
        )

    assert any("list item has 31 words; maximum is 30" in error
               for error in _visual_errors(body))


@pytest.mark.parametrize(
    ("item", "message"),
    [
        ("- lowercase text is not a complete label.", "list item starts with a lowercase letter"),
        ("- **lowercase lead:** This label starts lowercase.", "bold lead starts with a lowercase letter"),
        ("- **A label , with bad spacing:** This point is malformed.", "bold lead contains ' ,'"),
        ("- **A label with a:** This lead ends with a function word.", "bold lead ends with a function word"),
    ],
)
def test_visuals_reject_lowercase_and_malformed_bold_leads(
    tmp_path, monkeypatch, item, message
):
    _prepare_image_dir(tmp_path, monkeypatch)
    body = _visual_fixture().replace(
        "## How it works\n",
        "## How it works\n" + item + "\n",
    )
    assert any(message in error for error in _visual_errors(body))


def test_visuals_allow_complete_labels_and_inline_code_leads(tmp_path, monkeypatch):
    _prepare_image_dir(tmp_path, monkeypatch)
    body = _visual_fixture().replace(
        "## How it works\n",
        "## How it works\n"
        "- **Setpoint**: The requested value.\n"
        "- **Label:** A concise lead may keep its colon in bold.\n"
        "- `lerobot-record` saves the episode.\n",
    ).replace(
        "3. Compare the result after a disturbance.",
        "3. Compare the result after a disturbance.\n"
        "4. **Set a 10° target** for the simulated joint.",
    )
    assert _visual_errors(body) == []


def test_visuals_reject_bold_leads_that_repeat_section_headings(tmp_path, monkeypatch):
    _prepare_image_dir(tmp_path, monkeypatch)
    bodies = [
        _visual_fixture().replace(
            "## Why it matters for us\n",
            "## Why it matters for us\n"
            "- **Why it matters:** The label repeats the heading.\n",
        ),
        _visual_fixture().replace(
            "## How it works\n"
            "- **Measure** **estimate** **plan** **act** **check**",
            "## Application\n"
            "- **Application:** The label repeats the heading.",
        ),
    ]

    for body in bodies:
        assert any(
            "uses a generic label or repeats its section heading" in error
            for error in _visual_errors(body)
        )


@pytest.mark.parametrize(
    ("heading", "kind", "body", "third_step"),
    [
        (
            "## Try it in an afternoon",
            "knowledge",
            None,
            "3. Compare the result after a disturbance.",
        ),
        (
            "## Steps",
            "project",
            "## Steps\n1. Inspect the device.\n2. Run one test.\n3. Record the result.",
            "3. Record the result.",
        ),
        (
            "## Getting started",
            "robot",
            None,
            "3. Test a slow movement.",
        ),
    ],
)
def test_visuals_require_three_to_seven_numbered_steps(
    tmp_path, monkeypatch, heading, kind, body, third_step
):
    _prepare_image_dir(tmp_path, monkeypatch)
    fixture = _visual_fixture(robot_table=heading == "## Getting started")
    if body is not None:
        fixture = fixture.replace(
            "\n\n" + MERMAID_MD,
            "\n\n" + body + "\n\n" + MERMAID_MD,
        )
    assert _visual_errors(fixture, kind) == []

    too_few = fixture.replace(third_step, "", 1)
    assert any(f"{heading}: has 2 numbered steps; expected 3-7" in error
               for error in _visual_errors(too_few, kind))

    too_many = fixture.replace(
        third_step,
        third_step
        + "\n4. Repeat the test."
        + "\n5. Save the measurements."
        + "\n6. Check the result."
        + "\n7. Change one setting."
        + "\n8. Record the next result.",
    )
    assert any(f"{heading}: has 8 numbered steps; expected 3-7" in error
               for error in _visual_errors(too_many, kind))

    as_bullets = fixture.replace(
        third_step, third_step.replace("3. ", "- ", 1)
    )
    assert any(f"{heading}: steps must use a numbered list" in error
               for error in _visual_errors(as_bullets, kind))


def test_visual_credits_require_valid_metadata(tmp_path, monkeypatch):
    _prepare_image_dir(tmp_path, monkeypatch)
    credits_path = tmp_path / "credits.json"
    credits_path.write_text(
        json.dumps({
            "test.webp": {
                "page_url": "file:///source",
                "image_url": "not-a-url",
                "license": " ",
                "author": "",
            }
        }),
        encoding="utf-8",
    )

    errors = _visual_errors(_visual_fixture())

    assert any("HTTP(S) page_url" in error for error in errors)
    assert any("HTTP(S) image_url" in error for error in errors)
    assert any("non-empty license" in error for error in errors)
    assert any("non-empty author" in error for error in errors)


def test_visuals_require_a_matching_credit_entry(tmp_path, monkeypatch):
    _prepare_image_dir(tmp_path, monkeypatch)
    (tmp_path / "credits.json").write_text("{}", encoding="utf-8")

    errors = _visual_errors(_visual_fixture())

    assert any("missing image credit for test.webp" in error for error in errors)


def test_visuals_limit_prose_paragraphs_and_allow_intro_exception(tmp_path, monkeypatch):
    _prepare_image_dir(tmp_path, monkeypatch)
    body = _visual_fixture()
    intro_with_six = body + "\n\n" + "\n\n".join(
        f"Intro paragraph {index}." for index in range(4)
    )
    assert not any("prose paragraphs" in error
                   for error in _visual_errors(intro_with_six, "intro"))

    too_many = body + "\n\n" + "\n\n".join(
        f"Additional prose paragraph {index}." for index in range(5)
    )
    assert any("prose paragraphs; maximum is 3" in error
               for error in _visual_errors(too_many))
    assert any("prose paragraphs; maximum is 6" in error
               for error in _visual_errors(too_many, "intro"))


def test_visuals_require_exact_before_after_bullets(tmp_path, monkeypatch):
    _prepare_image_dir(tmp_path, monkeypatch)
    body = _visual_fixture().replace(
        "- **After:** The robot adjusts its action from the measurement.",
        "After the change, the robot adjusts its action from the measurement.",
    )

    assert any("must contain exactly the Before and After bullets" in error
               for error in _visual_errors(body))


def test_visuals_reject_key_idea_repeating_summary(tmp_path, monkeypatch):
    _prepare_image_dir(tmp_path, monkeypatch)
    body = _visual_fixture().replace(
        "> **Key idea:** Keep a clear measurement loop.",
        "> **Key idea:** A measurement helps the robot choose its next action.",
    )

    assert any("Key idea must differ from the In one sentence text" in error
               for error in _visual_errors(body))


def test_visuals_reject_blank_line_padded_fences(tmp_path, monkeypatch):
    _prepare_image_dir(tmp_path, monkeypatch)
    body = _visual_fixture() + (
        "\n\n```python\n\nfirst = 1\n\nsecond = 2\n\nthird = 3\n```"
    )

    assert any("excessive blank-line padding" in error
               for error in _visual_errors(body))


def test_visuals_limit_prose_paragraphs_to_forty_words(tmp_path, monkeypatch):
    _prepare_image_dir(tmp_path, monkeypatch)
    body = _visual_fixture() + "\n\n" + " ".join(["robot"] * 41)
    assert any("prose paragraph has 41 words; maximum is 40" in error
               for error in _visual_errors(body))


def test_robot_visuals_require_four_to_eight_table_rows_inside_section(
    tmp_path, monkeypatch
):
    _prepare_image_dir(tmp_path, monkeypatch)
    body = _visual_fixture(robot_table=True)
    assert _visual_errors(body, "robot") == []

    no_table = body.replace(
        "\n\n## What it is made of / how it works\n"
        "The device combines a motor, gears, and feedback.\n\n"
        "| Specification | Value |\n"
        "| --- | --- |\n"
        "| **Voltage** | 6-7.4 V |\n"
        "| **Encoder** | 12-bit magnetic |\n"
        "| **Bus** | Half-duplex serial |\n"
        "| **Joints** | Six |\n"
        "\n## Getting started\n",
        "\n\n## Getting started\n",
    )
    assert any("spec table under" in error for error in _visual_errors(no_table, "robot"))

    too_few = body.replace("| **Joints** | Six |\n", "")
    assert any("has 3 data rows; expected 4-8" in error
               for error in _visual_errors(too_few, "robot"))

    wrong_columns = body.replace(
        "| **Voltage** | 6-7.4 V |",
        "| **Voltage** | 6-7.4 V | extra |",
    )
    assert any("exactly 2 columns" in error
               for error in _visual_errors(wrong_columns, "robot"))


def test_word_count_excludes_mermaid_fences():
    markdown = (
        "Outside count\n\n"
        "```mermaid\n"
        "flowchart LR\n"
        "  A[\"many words inside this label\"] --> B[\"more words\"]\n"
        "```\n"
    )
    assert word_count(markdown) == 2


def test_resources_require_a_video():
    resources = [
        {
            "title": f"Resource {index}",
            "url": f"https://example.org/resource-{index}",
            "format": resource_format,
            "level": "Beginner",
            "why": "A focused explanation.",
        }
        for index, resource_format in enumerate(["Article", "Blog", "Docs", "Repo"], 1)
    ]
    errors = []

    _check_resources(resources, "lesson fixture", 4, 6, errors)

    assert errors == ["lesson fixture: requires at least one resource with format 'Video'"]


def test_word_count_bounds_are_strict():
    for count in (250, 500):
        errors = []
        _check_word_count("word " * count, 250, 500, "lesson fixture", errors)
        assert errors == []

    for count in (249, 501):
        errors = []
        _check_word_count("word " * count, 250, 500, "lesson fixture", errors)
        assert errors == [
            f"lesson fixture: {count} words; expected 250-500"
        ]


def test_url_reuse_warns_across_guide_and_pilot_items():
    url = "https://example.org/shared"
    resource = {"url": url, "title": "Shared resource"}
    guide = (
        Path("guide.json"),
        {"chapters": [{"id": f"chapter-{i}", "resources": [resource]} for i in range(3)]},
    )
    pilot = (
        Path("pilot.json"),
        {"lessons": [{"node_id": "k:test", "resources": [resource]}]},
    )

    warnings = url_reuse_warnings([guide, pilot])

    assert len(warnings) == 1
    assert "appears in 4 items" in warnings[0]
    assert url in warnings[0]
    pilot_without_reuse = (Path("pilot.json"), {"lessons": []})
    assert url_reuse_warnings([guide, pilot_without_reuse]) == []


def test_youtube_oembed_title_must_match_resource_title(monkeypatch, capsys):
    url = "https://www.youtube.com/watch?v=example123"

    class Response:
        status = 200

        def __enter__(self):
            return self

        def __exit__(self, *args):
            return False

        def read(self):
            return b'{"title":"Verified video title"}'

    monkeypatch.setattr("viz.scripts.check_lessons.urlopen", lambda *args, **kwargs: Response())
    failures, blocked = check_urls(
        {url},
        expected_titles={url: {"Verified video title"}},
    )
    assert failures == []
    assert blocked == []
    assert "URL OK HTTP 200" in capsys.readouterr().out

    failures, blocked = check_urls(
        {url},
        expected_titles={url: {"Different title"}},
    )
    assert blocked == []
    assert len(failures) == 1
    assert "YouTube title mismatch" in failures[0]
