#!/usr/bin/env python3
"""Validate the structure and links in robotics lesson JSON files."""

from __future__ import annotations

import argparse
from collections import defaultdict
import json
import re
import sys
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode, urlparse
from urllib.request import Request, urlopen


LESSON_HEADINGS = {
    "knowledge": [
        "## In one sentence",
        "## Why it matters for us",
        "## How it works",
        "## Key terms",
        "## Before / after",
        "## Try it in an afternoon",
    ],
    "robot": [
        "## In one sentence",
        "## Why it matters for us",
        "## What it is made of / how it works",
        "## Key terms",
        "## Getting started",
        "## Used in",
    ],
    "project": [
        "## In one sentence",
        "## What you will learn",
        "## What you need",
        "## Steps",
        "## Common pitfalls",
        "## When it's done",
    ],
    "org": [
        "## In one sentence",
        "## What they do in robotics",
        "## Why they matter for 42AI",
        "## How to engage",
    ],
}
GUIDE_INTRO_HEADINGS = [
    "## What is a robot?",
    "## The fields of robotics and how they fit together",
    "## Hardware vs software: what changes when code touches the real world",
    "## How to use these maps",
    "## Suggested order",
]
GUIDE_CHAPTER_HEADINGS = [
    "## What this field is about",
    "## Where it sits in the robot loop",
    "## The big ideas",
    "## What you'll be able to build",
]
BRANCHES = [
    "Mechanisms & actuation",
    "Embedded & electronics",
    "Sensing",
    "Kinematics & dynamics",
    "Control",
    "Simulation",
    "Perception",
    "State estimation & SLAM",
    "Planning",
    "Manipulation",
    "Locomotion",
    "Robot learning",
    "HRI & safety",
]
PILOT_IDS = {
    "k:feedback-control-pid",
    "k:rigid-body-motion-coordinate-frames",
    "k:kalman-filtering-multisensor-fusion",
    "k:imitation-learning-behavior-cloning",
    "k:fiducial-markers-apriltag-aruco",
    "r:so-101",
    "r:feetech-sts3215-servo",
    "r:lerobot",
    "r:smolvla",
    "r:nvidia-jetson-orin-nano-super-developer-kit",
    "p:assemble-teleoperate-an-so-101",
    "p:pid-tuning-playground-in-simulation",
    "p:intro-calibrate-a-webcam-and-track-apriltags",
    "p:autonomous-pick-and-place-with-act",
    "p:language-commanded-arm-with-smolvla",
    "o:hugging-face-lerobot",
    "o:pollen-robotics-hugging-face",
    "o:eth-zurich-robotic-systems-lab-rsl",
}
FORMATS = {"Video", "Course", "Docs", "Blog", "Article", "Paper", "Book", "Repo", "Interactive"}
LEVELS = {"Beginner", "Intermediate", "Advanced"}
WORD_RE = re.compile(r"\b[\w’'-]+\b", re.UNICODE)
URL_RE = re.compile(r"^https?://", re.IGNORECASE)
MERMAID_BLOCK_RE = re.compile(r"(?ms)^```mermaid[ \t]*\n.*?^```[ \t]*(?:\n|$)")
MARKDOWN_IMAGE_RE = re.compile(r"!\[(?P<alt>[^\]]*)\]\((?P<path>[^)]+)\)")
LESSON_IMAGE_PATH_RE = re.compile(r"^/img/lessons/(?P<name>[^/\s]+\.webp)$")
LESSON_IMAGE_DIR = Path(__file__).resolve().parents[1] / "web" / "public" / "img" / "lessons"
LESSON_CREDITS_PATH = LESSON_IMAGE_DIR / "credits.json"
VISUAL_STEP_HEADINGS = {
    "## Steps",
    "## Try it in an afternoon",
    "## Getting started",
}
HEADING_STOP_WORDS = {"a", "an", "and", "for", "in", "is", "it", "of", "the", "to", "us"}
GENERIC_LEAD_WORDS = {
    ("application",),
    ("how", "works"),
    ("why", "matters"),
}
BOLD_LEAD_FUNCTION_WORDS = {
    "a", "an", "the", "of", "to", "is", "are", "was", "on", "in", "for",
    "and", "or", "with", "that", "it", "as", "by", "at", "from", "its",
    "be", "can", "may", "will", "would", "should", "must", "if", "this",
    "their", "your", "one", "into", "than", "then", "also", "still", "only",
    "so",
}


def word_count(text: str) -> int:
    return len(WORD_RE.findall(MERMAID_BLOCK_RE.sub("", text)))


def _normalize(text: str) -> str:
    return " ".join(text.split())


def _section_text(markdown: str, heading: str) -> str:
    lines = markdown.splitlines()
    try:
        start = lines.index(heading) + 1
    except ValueError:
        return ""
    for end in range(start, len(lines)):
        if lines[end].startswith("## "):
            section = lines[start:end]
            break
    else:
        section = lines[start:]
    text = MARKDOWN_IMAGE_RE.sub("", "\n".join(section))
    text = "\n".join(
        line for line in text.splitlines()
        if not (line.strip().startswith("*") and "Source:" in line)
    )
    return _normalize(text)


def _check_headings(markdown: object, expected: list[str], label: str, errors: list[str],
                    optional: set[str] | None = None) -> None:
    if not isinstance(markdown, str):
        errors.append(f"{label}: markdown body must be a string")
        return
    headings = [line for line in markdown.splitlines() if line.startswith("## ")]
    allowed = [expected]
    for heading in optional or set():
        allowed.append([item for item in expected if item != heading])
    if headings not in allowed:
        expected_text = " or ".join(" -> ".join(items) for items in allowed)
        errors.append(
            f"{label}: headings are {headings!r}; expected exactly {expected_text}"
        )
    if any(line.startswith("# ") for line in markdown.splitlines()):
        errors.append(f"{label}: top-level '# ' heading is not allowed")


def _check_bullet_section(markdown: str, heading: str, minimum: int, maximum: int,
                          label: str, errors: list[str], term_format: bool = False) -> None:
    lines = markdown.splitlines()
    try:
        start = lines.index(heading) + 1
    except ValueError:
        return
    end = next(
        (index for index in range(start, len(lines)) if lines[index].startswith("## ")),
        len(lines),
    )
    section_lines = [line.strip() for line in lines[start:end] if line.strip()]
    bullets = [line for line in section_lines if line.startswith("- ")]
    if not minimum <= len(bullets) <= maximum:
        errors.append(
            f"{label} {heading}: has {len(bullets)} bullets; expected {minimum}-{maximum}"
        )
    if any(not line.startswith("- ") for line in section_lines):
        errors.append(f"{label} {heading}: section must contain only bullets")
    if term_format and any(
        not re.fullmatch(r"- \*\*[^*\n]+\*\*: .+", line) for line in bullets
    ):
        errors.append(
            f"{label} {heading}: bullets must use '- **term**: definition' format"
        )


def _check_word_count(text: str, minimum: int, maximum: int, label: str,
                      errors: list[str]) -> None:
    count = word_count(text)
    if count < minimum or count > maximum:
        errors.append(f"{label}: {count} words; expected {minimum}-{maximum}")


def _section_lines(markdown: str, heading: str) -> list[str]:
    lines = markdown.splitlines()
    try:
        start = lines.index(heading) + 1
    except ValueError:
        return []
    end = next(
        (index for index in range(start, len(lines)) if lines[index].startswith("## ")),
        len(lines),
    )
    return lines[start:end]


def _prose_paragraphs(markdown: str) -> list[str]:
    paragraphs: list[str] = []
    current: list[str] = []
    in_fence = False

    def flush() -> None:
        nonlocal current
        if current:
            block = "\n".join(current)
            first = current[0].strip()
            is_list = (
                first.startswith(("- ", "* ", "+ "))
                or re.match(r"^\d+[.)]\s", first) is not None
            )
            is_caption = first.startswith("*") and first.endswith("*")
            if not (
                first.startswith(("## ", "# ", ">", "|", "!["))
                or is_list
                or is_caption
                or re.fullmatch(r"[-*_]{3,}", first)
            ):
                paragraphs.append(block)
            current = []

    for line in markdown.splitlines():
        if line.strip().startswith("```"):
            flush()
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        if line.startswith(("## ", "# ")):
            flush()
            continue
        if not line.strip():
            flush()
        else:
            current.append(line)
    flush()
    return paragraphs


def _visual_list_items(markdown: str) -> list[tuple[str, str, str]]:
    items: list[tuple[str, str, str]] = []
    current_heading = ""
    current_marker: str | None = None
    current_text: list[str] = []
    in_fence = False

    def flush() -> None:
        nonlocal current_marker, current_text
        if current_marker is not None:
            items.append((current_heading, current_marker, " ".join(current_text)))
        current_marker = None
        current_text = []

    for line in markdown.splitlines():
        if line.strip().startswith("```"):
            flush()
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        if line.startswith("## "):
            flush()
            current_heading = line.strip()
            continue
        match = re.match(r"^\s*(?P<marker>[-*+]|\d+[.)])\s+(?P<text>.*)$", line)
        if match:
            flush()
            current_marker = match.group("marker")
            current_text = [match.group("text").strip()]
        elif current_marker is not None and line.startswith(("  ", "\t")) and line.strip():
            current_text.append(line.strip())
        else:
            flush()
    flush()
    return items


def _normalized_lead_words(text: str) -> tuple[str, ...]:
    return tuple(
        word.casefold()
        for word in WORD_RE.findall(text)
        if word.casefold() not in HEADING_STOP_WORDS
    )


def _check_visuals(markdown: object, label: str, kind: str,
                   errors: list[str]) -> None:
    if not isinstance(markdown, str):
        errors.append(f"{label}: markdown body must be a string")
        return

    lines = markdown.splitlines()
    visible_headings: set[str] = set()
    in_fence = False
    for line in lines:
        if line.strip().startswith("```"):
            in_fence = not in_fence
        elif not in_fence and line.startswith("## "):
            visible_headings.add(line.strip())

    list_items = _visual_list_items(markdown)
    for heading, marker, content in list_items:
        count = word_count(content)
        if count > 30:
            errors.append(f"{label}: list item has {count} words; maximum is 30")
        if content and content[0].islower():
            errors.append(f"{label}: list item starts with a lowercase letter")
        bold_lead = re.match(r"^\*\*([^*\n]+)\*\*", content)
        if bold_lead is not None:
            lead_text = bold_lead.group(1)
            normalized_lead = lead_text.rstrip(": ")
            if normalized_lead and normalized_lead[0].islower():
                errors.append(f"{label}: bold lead starts with a lowercase letter")
            if " ," in lead_text:
                errors.append(f"{label}: bold lead contains ' ,'")
            lead_words = WORD_RE.findall(normalized_lead)
            if lead_words and lead_words[-1].casefold() in BOLD_LEAD_FUNCTION_WORDS:
                errors.append(f"{label}: bold lead ends with a function word")
        if bold_lead is not None and heading != "## Before / after":
            lead_words = _normalized_lead_words(bold_lead.group(1))
            heading_words = _normalized_lead_words(heading)
            if lead_words and (
                lead_words in GENERIC_LEAD_WORDS
                or heading_words[:len(lead_words)] == lead_words
            ):
                errors.append(
                    f"{label}: bold lead {bold_lead.group(1)!r} uses a generic label "
                    "or repeats its section heading"
                )

    for heading in VISUAL_STEP_HEADINGS & visible_headings:
        section_items = [item for item in list_items if item[0] == heading]
        numbered_items = [
            item for item in section_items if re.fullmatch(r"\d+[.)]", item[1])
        ]
        if any(not re.fullmatch(r"\d+[.)]", item[1]) for item in section_items):
            errors.append(f"{label} {heading}: steps must use a numbered list")
        if not 3 <= len(numbered_items) <= 7:
            errors.append(
                f"{label} {heading}: has {len(numbered_items)} numbered steps; expected 3-7"
            )

    image_lines = [(index, line.strip()) for index, line in enumerate(lines) if "![" in line]
    if not 1 <= len(image_lines) <= 2:
        errors.append(f"{label}: has {len(image_lines)} images; expected 1-2")
    try:
        credits = json.loads(LESSON_CREDITS_PATH.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        errors.append(f"{label}: cannot read lesson image credits: {exc}")
        credits = {}
    if not isinstance(credits, dict):
        errors.append(f"{label}: lesson image credits must be a JSON object")
        credits = {}
    for index, line in image_lines:
        match = MARKDOWN_IMAGE_RE.fullmatch(line)
        if match is None:
            errors.append(
                f"{label}: image must use ![alt](/img/lessons/<file>.webp) on its own line"
            )
            continue
        if not match.group("alt").strip():
            errors.append(f"{label}: image alt text must not be empty")
        path_match = LESSON_IMAGE_PATH_RE.fullmatch(match.group("path"))
        if path_match is None:
            errors.append(f"{label}: image path must be /img/lessons/<file>.webp")
        else:
            name = path_match.group("name")
            if not (LESSON_IMAGE_DIR / name).is_file():
                errors.append(f"{label}: image file does not exist: {match.group('path')}")

        caption_index = next(
            (next_index for next_index in range(index + 1, len(lines) if lines else index + 1)
             if lines[next_index].strip()),
            None,
        )
        if caption_index is None:
            errors.append(f"{label}: image must be followed by a caption containing Source:")
        else:
            caption = lines[caption_index].strip()
            if not caption.startswith("*") or "Source:" not in caption:
                errors.append(f"{label}: image caption must start with '*' and contain 'Source:'")
            if "Original" in caption:
                errors.append(f"{label}: image caption must not contain 'Original'")

        if path_match is not None:
            name = path_match.group("name")
            credit = credits.get(name)
            if not isinstance(credit, dict):
                errors.append(f"{label}: missing image credit for {name}")
                continue
            urls: dict[str, str] = {}
            for field in ("page_url", "image_url"):
                value = credit.get(field)
                parsed = urlparse(value) if isinstance(value, str) else None
                if parsed is None or parsed.scheme not in {"http", "https"} or not parsed.netloc:
                    errors.append(f"{label}: {name} credit requires an HTTP(S) {field}")
                else:
                    urls[field] = value
            for field in ("license", "author"):
                if not isinstance(credit.get(field), str) or not credit[field].strip():
                    errors.append(f"{label}: {name} credit requires a non-empty {field}")
            if caption_index is not None and "page_url" in urls:
                caption = lines[caption_index].strip()
                linked_urls = re.findall(r"\[[^\]]+\]\(([^)]+)\)", caption)
                if urls["page_url"] not in linked_urls:
                    errors.append(f"{label}: image caption must link to its exact page_url")

    required_mermaid = kind in {"intro", "chapter", "knowledge", "project"}
    if required_mermaid and not any(
        re.fullmatch(r"```mermaid[ \t]*", line.strip()) for line in lines
    ):
        errors.append(f"{label}: requires a Mermaid flowchart")

    key_ideas = [line for line in lines if line.startswith("> **Key idea:**")]
    if len(key_ideas) != 1:
        errors.append(f"{label}: has {len(key_ideas)} Key idea callouts; expected exactly 1")
    watch_outs = [line for line in lines if line.startswith("> **Watch out:**")]
    if len(watch_outs) > 1:
        errors.append(f"{label}: has {len(watch_outs)} Watch out callouts; maximum is 1")

    bold_spans = re.findall(r"\*\*[^*\n]+\*\*", markdown)
    if len(bold_spans) < 5:
        errors.append(f"{label}: has {len(bold_spans)} bold spans; expected at least 5")

    for paragraph in _prose_paragraphs(markdown):
        count = word_count(paragraph)
        if count > 40:
            errors.append(
                f"{label}: prose paragraph has {count} words; maximum is 40"
            )

    paragraph_limit = 6 if kind == "intro" else 3
    prose_count = len(_prose_paragraphs(markdown))
    if prose_count > paragraph_limit:
        errors.append(
            f"{label}: has {prose_count} prose paragraphs; maximum is {paragraph_limit}"
        )

    if kind == "knowledge" and re.search(r"(?m)^## Before / after[ \t]*$", markdown):
        before_after = [line.strip() for line in _section_lines(markdown, "## Before / after")
                        if line.strip()]
        bullets = [line for line in before_after if line.startswith("- ")]
        if (len(bullets) != 2 or len(before_after) != 2
                or not bullets[0].startswith("- **Before:**")
                or not bullets[1].startswith("- **After:**")):
            errors.append(
                f"{label}: ## Before / after must contain exactly the Before and After bullets"
            )

    if kind in {"knowledge", "robot", "project", "org"} and len(key_ideas) == 1:
        sentence = _section_text(markdown, "## In one sentence")
        key_idea = key_ideas[0].partition(":**")[2].strip()
        normalize_idea = lambda text: re.sub(
            r"[.!?]+$", "", re.sub(r"[*_`]", "", _normalize(text))
        ).casefold()
        if sentence and normalize_idea(sentence) == normalize_idea(key_idea):
            errors.append(f"{label}: Key idea must differ from the In one sentence text")

    for block in re.findall(r"(?ms)^```[^\n]*\n(.*?)^```[ \t]*(?:\n|$)", markdown):
        content_lines = block.splitlines()
        if (len(content_lines) >= 4
                and sum(not line.strip() for line in content_lines) / len(content_lines) > 0.4):
            errors.append(f"{label}: code fence has excessive blank-line padding")

    if kind == "robot":
        table_lines = [
            line.strip() for line in _section_lines(
                markdown, "## What it is made of / how it works"
            )
            if line.strip().startswith("|")
        ]
        if not table_lines:
            errors.append(
                f"{label}: robot lessons require a spec table under "
                "'## What it is made of / how it works'"
            )
        else:
            rows: list[list[str]] = []
            for line in table_lines:
                cells = [cell.strip() for cell in line.strip("|").split("|")]
                if len(cells) != 2:
                    errors.append(f"{label}: robot spec table must have exactly 2 columns")
                    continue
                if not all(re.fullmatch(r":?-{3,}:?", cell) for cell in cells):
                    rows.append(cells)
            data_rows = rows[1:] if rows else []
            if not 4 <= len(data_rows) <= 8:
                errors.append(
                    f"{label}: robot spec table has {len(data_rows)} data rows; expected 4-8"
                )


def _check_resources(resources: object, label: str, minimum: int, maximum: int,
                     errors: list[str]) -> None:
    if not isinstance(resources, list):
        errors.append(f"{label}: resources must be a list")
        return
    if not minimum <= len(resources) <= maximum:
        errors.append(f"{label}: has {len(resources)} resources; expected {minimum}-{maximum}")
    formats: set[str] = set()
    seen_urls: set[str] = set()
    for index, resource in enumerate(resources, 1):
        resource_label = f"{label} resource {index}"
        if not isinstance(resource, dict):
            errors.append(f"{resource_label}: must be an object")
            continue
        for key in ("title", "url", "format", "level", "why"):
            if not isinstance(resource.get(key), str) or not resource[key].strip():
                errors.append(f"{resource_label}: {key} must be a non-empty string")
        fmt = resource.get("format")
        if not isinstance(fmt, str) or fmt not in FORMATS:
            errors.append(f"{resource_label}: invalid format {fmt!r}")
        else:
            formats.add(fmt)
        level = resource.get("level")
        if not isinstance(level, str) or level not in LEVELS:
            errors.append(f"{resource_label}: invalid level {level!r}")
        url = resource.get("url")
        if isinstance(url, str) and url:
            if not URL_RE.match(url):
                errors.append(f"{resource_label}: URL must use http or https")
            normalized = url.rstrip("/").casefold()
            if normalized in seen_urls:
                errors.append(f"{resource_label}: duplicate URL {url}")
            seen_urls.add(normalized)
    if len(formats) < 2:
        errors.append(f"{label}: resources must use at least 2 distinct formats")
    if "Video" not in formats:
        errors.append(f"{label}: requires at least one resource with format 'Video'")


def _check_sources(sources: object, label: str, errors: list[str]) -> None:
    if not isinstance(sources, list) or not sources:
        errors.append(f"{label}: sources must be a non-empty list")
        return
    for index, source in enumerate(sources, 1):
        if not isinstance(source, str) or not URL_RE.match(source):
            errors.append(f"{label} source {index}: must be an http or https URL")


def _check_node(node_id: object, node_type: object, name: object, label: str,
                graph_nodes: dict[str, dict[str, str]], errors: list[str]) -> None:
    if not isinstance(node_id, str) or not node_id:
        errors.append(f"{label}: node_id must be a non-empty string")
        return
    graph_node = graph_nodes.get(node_id)
    if graph_node is None:
        errors.append(f"{label}: unknown node_id {node_id!r}")
        return
    if node_type != graph_node["type"]:
        errors.append(
            f"{label}: type {node_type!r} does not match graph type {graph_node['type']!r}"
        )
    if name != graph_node["name"]:
        errors.append(
            f"{label}: name {name!r} does not match graph name {graph_node['name']!r}"
        )


def _check_lesson(lesson: object, index: int, graph_nodes: dict[str, dict[str, str]],
                  errors: list[str]) -> None:
    label = f"lesson {index}"
    if not isinstance(lesson, dict):
        errors.append(f"{label}: must be an object")
        return
    required = {"node_id", "type", "name", "summary", "lesson_md", "resources", "sources"}
    missing = required - lesson.keys()
    if missing:
        errors.append(f"{label}: missing fields {sorted(missing)}")
    node_id = lesson.get("node_id")
    _check_node(node_id, lesson.get("type"), lesson.get("name"), label, graph_nodes, errors)
    lesson_type = lesson.get("type")
    headings = (
        LESSON_HEADINGS.get(lesson_type)
        if isinstance(lesson_type, str)
        else None
    )
    markdown = lesson.get("lesson_md")
    if headings:
        optional = {"## Before / after"} if lesson_type == "knowledge" else (
            {"## Used in"} if lesson_type == "robot" else set()
        )
        _check_headings(markdown, headings, label, errors, optional)
        if isinstance(markdown, str):
            minimum, maximum = (150, 300) if lesson_type == "org" else (250, 500)
            _check_word_count(markdown, minimum, maximum, label, errors)
            _check_visuals(markdown, label, lesson_type, errors)
            if lesson_type in {"knowledge", "robot"}:
                _check_bullet_section(markdown, "## Key terms", 3, 6, label, errors,
                                      term_format=True)
    else:
        errors.append(f"{label}: unsupported type {lesson_type!r}")
    summary = lesson.get("summary")
    if not isinstance(summary, str) or not summary.strip():
        errors.append(f"{label}: summary must be a non-empty string")
    else:
        count = word_count(summary)
        if count > 30:
            errors.append(f"{label}: summary has {count} words; maximum is 30")
        if isinstance(markdown, str):
            first_sentence = _section_text(markdown, "## In one sentence")
            if _normalize(summary) != first_sentence:
                errors.append(f"{label}: summary must match the In one sentence section")
    _check_resources(lesson.get("resources"), label, 4, 6, errors)
    _check_sources(lesson.get("sources"), label, errors)


def _check_guide(data: dict, label: str, graph_nodes: dict[str, dict[str, str]],
                 errors: list[str]) -> None:
    if data.get("title") != "Robotics from zero":
        errors.append(f"{label}: title must be 'Robotics from zero'")
    intro = data.get("intro_md")
    _check_headings(intro, GUIDE_INTRO_HEADINGS, f"{label} intro", errors)
    if isinstance(intro, str):
        _check_word_count(intro, 500, 900, f"{label} intro", errors)
        _check_visuals(intro, f"{label} intro", "intro", errors)
    chapters = data.get("chapters")
    if not isinstance(chapters, list):
        errors.append(f"{label}: chapters must be a list")
        chapters = []
    expected_branches: list[str | None] = [*BRANCHES, None]
    if len(chapters) != len(expected_branches):
        errors.append(
            f"{label}: has {len(chapters)} chapters; expected {len(expected_branches)}"
        )
    seen_ids: set[str] = set()
    for index, chapter in enumerate(chapters, 1):
        chapter_label = f"{label} chapter {index}"
        if not isinstance(chapter, dict):
            errors.append(f"{chapter_label}: must be an object")
            continue
        for key in ("id", "title", "branch", "body_md", "start_here", "resources"):
            if key not in chapter:
                errors.append(f"{chapter_label}: missing field {key}")
        chapter_id = chapter.get("id")
        if isinstance(chapter_id, str):
            if chapter_id in seen_ids:
                errors.append(f"{chapter_label}: duplicate chapter id {chapter_id!r}")
            seen_ids.add(chapter_id)
        if index <= len(expected_branches):
            expected_branch = expected_branches[index - 1]
            if chapter.get("branch") != expected_branch:
                errors.append(
                    f"{chapter_label}: branch {chapter.get('branch')!r}; "
                    f"expected {expected_branch!r}"
                )
            if expected_branch is None and chapter.get("title") != "The robotics world":
                errors.append(f"{chapter_label}: final title must be 'The robotics world'")
        body = chapter.get("body_md")
        _check_headings(body, GUIDE_CHAPTER_HEADINGS, chapter_label, errors)
        if isinstance(body, str):
            _check_word_count(body, 250, 450, chapter_label, errors)
            _check_bullet_section(body, "## The big ideas", 3, 5, chapter_label, errors)
            _check_visuals(body, chapter_label, "chapter", errors)
        start_here = chapter.get("start_here")
        if not isinstance(start_here, list) or not 3 <= len(start_here) <= 6:
            errors.append(f"{chapter_label}: start_here must contain 3-6 node IDs")
        else:
            for node_id in start_here:
                if not isinstance(node_id, str) or node_id not in graph_nodes:
                    errors.append(f"{chapter_label}: unknown start_here node {node_id!r}")
        _check_resources(chapter.get("resources"), chapter_label, 3, 5, errors)
    _check_sources(data.get("sources"), label, errors)


def validate_payload(data: object, label: str,
                     graph_nodes: dict[str, dict[str, str]]) -> list[str]:
    errors: list[str] = []
    if not isinstance(data, dict):
        return [f"{label}: JSON root must be an object"]
    if "chapters" in data or "intro_md" in data:
        _check_guide(data, label, graph_nodes, errors)
    elif "lessons" in data:
        lessons = data.get("lessons")
        if not isinstance(lessons, list):
            errors.append(f"{label}: lessons must be a list")
            lessons = []
        lesson_ids: list[str] = []
        for index, lesson in enumerate(lessons, 1):
            _check_lesson(lesson, index, graph_nodes, errors)
            if isinstance(lesson, dict) and isinstance(lesson.get("node_id"), str):
                lesson_ids.append(lesson["node_id"])
        if len(lesson_ids) != len(set(lesson_ids)):
            errors.append(f"{label}: duplicate lesson node_id")
        if data.get("batch") == "pilot":
            actual = set(lesson_ids)
            if actual != PILOT_IDS:
                errors.append(
                    f"{label}: pilot IDs differ; missing={sorted(PILOT_IDS - actual)}, "
                    f"extra={sorted(actual - PILOT_IDS)}"
                )
    else:
        errors.append(f"{label}: expected a guide object or a lessons batch")
    return errors


def load_graph_nodes(graph_path: Path) -> dict[str, dict[str, str]]:
    graph = json.loads(graph_path.read_text(encoding="utf-8"))
    return {
        node["id"]: {"type": node["type"], "name": node["name"]}
        for node in graph["nodes"]
    }


def _collect_urls(data: object) -> set[str]:
    urls: set[str] = set()
    if not isinstance(data, dict):
        return urls
    if isinstance(data.get("sources"), list):
        urls.update(source for source in data["sources"] if isinstance(source, str))
    items = data.get("lessons", data.get("chapters", []))
    if isinstance(items, list):
        for item in items:
            if not isinstance(item, dict):
                continue
            sources = item.get("sources")
            if isinstance(sources, list):
                urls.update(source for source in sources if isinstance(source, str))
            resources = item.get("resources")
            if isinstance(resources, list):
                urls.update(
                    resource["url"]
                    for resource in resources
                    if isinstance(resource, dict) and isinstance(resource.get("url"), str)
                )
    return urls


def _collect_resource_metadata(
    documents: list[tuple[Path, object]],
) -> tuple[dict[str, set[str]], dict[str, set[str]]]:
    usages: dict[str, set[str]] = defaultdict(set)
    youtube_titles: dict[str, set[str]] = defaultdict(set)
    for path, data in documents:
        if not isinstance(data, dict):
            continue
        items = data.get("lessons", data.get("chapters", []))
        if not isinstance(items, list):
            continue
        for index, item in enumerate(items, 1):
            if not isinstance(item, dict):
                continue
            item_id = item.get("node_id") or item.get("id") or item.get("title")
            label = f"{path}:{item_id or index}"
            resources = item.get("resources")
            if not isinstance(resources, list):
                continue
            for resource in resources:
                if not isinstance(resource, dict):
                    continue
                url = resource.get("url")
                if not isinstance(url, str) or not url:
                    continue
                normalized = url.rstrip("/").casefold()
                usages[normalized].add(label)
                hostname = (urlparse(url).hostname or "").casefold()
                if hostname == "youtu.be" or hostname == "youtube.com" or hostname.endswith(".youtube.com"):
                    title = resource.get("title")
                    if isinstance(title, str) and title.strip():
                        youtube_titles[normalized].add(title.strip())
    return usages, youtube_titles


def url_reuse_warnings(documents: list[tuple[Path, object]], maximum: int = 3) -> list[str]:
    usages, _ = _collect_resource_metadata(documents)
    return [
        f"URL appears in {len(items)} items (maximum {maximum}): {url}"
        for url, items in sorted(usages.items())
        if len(items) > maximum
    ]


def check_urls(
    urls: set[str],
    timeout: float = 15.0,
    expected_titles: dict[str, set[str]] | None = None,
) -> tuple[list[str], list[str]]:
    failures: list[str] = []
    blocked: list[str] = []
    for url in sorted(urls):
        check_url = url
        hostname = (urlparse(url).hostname or "").casefold()
        is_youtube = (
            hostname == "youtu.be"
            or hostname == "youtube.com"
            or hostname.endswith(".youtube.com")
        )
        normalized = url.rstrip("/").casefold()
        if is_youtube:
            check_url = "https://www.youtube.com/oembed?" + urlencode(
                {"url": url, "format": "json"}
            )
        request = Request(
            check_url,
            headers={"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
                                   "(KHTML, like Gecko) Chrome/124.0 Safari/537.36"},
        )
        try:
            with urlopen(request, timeout=timeout) as response:
                status = response.status
                payload = response.read() if is_youtube and expected_titles and normalized in expected_titles else b""
        except HTTPError as exc:
            status = exc.code
            payload = b""
        except (URLError, TimeoutError, OSError) as exc:
            failures.append(f"FAIL {url}: {exc}")
            continue
        if status in (403, 429):
            blocked.append(f"BLOCKED {status} (verify manually): {url}")
        elif not 200 <= status < 400:
            failures.append(f"FAIL HTTP {status}: {url}")
        else:
            titles = (expected_titles or {}).get(normalized)
            if is_youtube and titles:
                try:
                    actual_title = json.loads(payload.decode("utf-8")).get("title")
                except (UnicodeDecodeError, json.JSONDecodeError, AttributeError):
                    actual_title = None
                if not isinstance(actual_title, str):
                    failures.append(f"FAIL YouTube oEmbed returned no title: {url}")
                    continue
                if len(titles) != 1 or actual_title not in titles:
                    failures.append(
                        f"FAIL YouTube title mismatch: {url}: got {actual_title!r}, "
                        f"expected {sorted(titles)!r}"
                    )
                    continue
            print(f"URL OK HTTP {status}: {url}")
    return failures, blocked


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check-urls", action="store_true",
                        help="GET each resource and source URL and report blocked pages")
    parser.add_argument("files", nargs="+", type=Path, help="lesson or guide JSON files")
    args = parser.parse_args(argv)
    graph_path = Path(__file__).resolve().parents[1] / "data" / "graph.json"
    try:
        graph_nodes = load_graph_nodes(graph_path)
    except (OSError, json.JSONDecodeError, KeyError, TypeError) as exc:
        print(f"ERROR: could not load graph {graph_path}: {exc}", file=sys.stderr)
        return 2
    problems: list[str] = []
    documents: list[tuple[Path, object]] = []
    for path in args.files:
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            problems.append(f"{path}: could not parse JSON: {exc}")
            continue
        documents.append((path, data))
        problems.extend(validate_payload(data, str(path), graph_nodes))
    for problem in problems:
        print(f"ERROR: {problem}", file=sys.stderr)
    if not problems:
        for path, data in documents:
            if isinstance(data, dict) and isinstance(data.get("lessons"), list):
                print(f"OK {path}: {len(data['lessons'])} lessons")
            elif isinstance(data, dict) and isinstance(data.get("chapters"), list):
                print(f"OK {path}: {len(data['chapters'])} chapters")
    for warning in url_reuse_warnings(documents):
        print(f"WARNING: {warning}", file=sys.stderr)
    if args.check_urls and documents:
        urls = set().union(*(_collect_urls(data) for _, data in documents))
        _, youtube_titles = _collect_resource_metadata(documents)
        failures, blocked = check_urls(urls, expected_titles=youtube_titles)
        for message in blocked:
            print(message, file=sys.stderr)
        for message in failures:
            print(message, file=sys.stderr)
        print(f"URL checks: {len(urls) - len(failures) - len(blocked)} passed, "
              f"{len(failures)} failed, {len(blocked)} blocked")
        if failures:
            problems.extend(failures)
    return 1 if problems else 0


if __name__ == "__main__":
    raise SystemExit(main())
