import json
from pathlib import Path

from viz.scripts.check_lessons import (
    BRANCHES,
    GUIDE_INTRO_HEADINGS,
    _check_resources,
    _check_word_count,
    check_urls,
    load_graph_nodes,
    url_reuse_warnings,
    validate_payload,
)


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
    intro = "\n\n".join(GUIDE_INTRO_HEADINGS) + (
        "\n\nRobots sense, estimate, plan, act, and observe each result. " * 60
    )
    details = "Robots sense, estimate, plan, act, and observe each result. " * 8
    body = (
        "## What this field is about\n"
        f"{details}\n\n"
        "## Where it sits in the robot loop\n"
        f"{details}\n\n"
        "## The big ideas\n"
        "- Ideas use a measured position.\n"
        "- Plans respect joint limits.\n"
        "- Evaluation checks physical behavior.\n\n"
        "## Key terms\n"
        "- **Robot**: a system that senses and acts.\n"
        "- **State**: values describing the system.\n"
        "- **Loop**: repeated sensing and action.\n\n"
        "## What you'll be able to build\n"
        f"{details}"
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


def test_check_lesson_valid_and_broken_fixtures(tmp_path):
    summary = "A test concept explains a small robot idea."
    body = (
        "## In one sentence\n"
        f"{summary}\n\n"
        "## Why it matters for us\n"
        "This section explains why the concept is useful. "
        + " ".join(["A robot reads a measurement and updates its state."] * 12)
        + "\n\n## How it works\n"
        "This section gives a simple explanation and a software analogy. "
        + " ".join(["A loop compares the target with the current value."] * 6)
        + "\n\n## Key terms\n"
        "- **Robot**: a machine that can sense and act.\n"
        "- **State**: values describing the system.\n"
        "- **Loop**: repeated execution of a program.\n\n"
        "## Try it in an afternoon\n"
        "Try a small simulation and record the result. "
        + " ".join(["Change one input and observe the output."] * 6)
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
    graph_nodes, valid_data = _fixture(tmp_path, valid_lesson)
    assert validate_payload(valid_data, "valid fixture", graph_nodes) == []

    broken_lesson = {
        **valid_lesson,
        "node_id": "k:missing",
        "name": "Wrong name",
        "summary": "This summary does not match the lesson.",
        "lesson_md": "# Not allowed\n## Wrong heading\nToo short.",
        "resources": [{**resources[0], "format": []}],
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


def test_guide_chapters_require_bullet_lists():
    graph_nodes = {"k:test": {"type": "knowledge", "name": "Test concept"}}
    guide = _valid_guide_payload()
    assert validate_payload(guide, "valid guide fixture", graph_nodes) == []

    too_few_ideas = _valid_guide_payload()
    too_few_ideas["chapters"][0]["body_md"] = (
        too_few_ideas["chapters"][0]["body_md"]
        .replace("- Evaluation checks physical behavior.\n", "", 1)
    )
    problems = validate_payload(too_few_ideas, "short bullet fixture", graph_nodes)
    assert any("The big ideas: has 2 bullets; expected 3-5" in problem for problem in problems)

    malformed_term = _valid_guide_payload()
    malformed_term["chapters"][0]["body_md"] = (
        malformed_term["chapters"][0]["body_md"]
        .replace("- **Robot**: a system that senses and acts.",
                 "- Robot: a system that senses and acts.", 1)
    )
    problems = validate_payload(malformed_term, "term format fixture", graph_nodes)
    assert any("Key terms: bullets must use" in problem for problem in problems)


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
