import json

from viz.scripts.data_common import place_for_org
from viz.scripts.import_research import import_research


def test_import_research_encodes_rows_and_is_idempotent(tmp_path):
    source = tmp_path / "ecosystem_switzerland_all.json"
    rows_path = tmp_path / "rows.json"
    source.write_text(
        json.dumps(
            {
                "organizations": [
                    {
                        "Organization": "Test Zürich Lab",
                        "Type": "Research lab",
                        "City": "Zürich",
                        "Sector": ["Research", "AI"],
                        "Open source": True,
                        "Team size": 12,
                        "Builds": ["Test robot"],
                        "Uses": [],
                        "Related projects": ["Demo project"],
                        "_internal": "discard",
                    }
                ],
                "robots_models": [
                    {
                        "Name": "Test robot",
                        "Kind": "Robot",
                        "Built by": ["Test Zürich Lab"],
                        "Used by": [],
                        "Knowledge nodes": ["Control"],
                        "Open source": False,
                        "_private": True,
                    }
                ],
            },
            ensure_ascii=False,
        ),
        encoding="utf-8",
    )
    rows_path.write_text(
        json.dumps({"ecosystem": [], "robots": []}, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )

    first = import_research("Switzerland", source, rows_path)
    imported = json.loads(rows_path.read_text(encoding="utf-8"))
    org = imported["ecosystem"][0]
    robot = imported["robots"][0]

    assert first == {
        "ecosystem": {"added": 1, "skipped": 0},
        "robots": {"added": 1, "skipped": 0},
    }
    assert org == {
        "name": "Test Zürich Lab",
        "existing_url": None,
        "props": {
            "Type": "Research lab",
            "City": "Zürich",
            "Sector": '["Research", "AI"]',
            "Open source": "__YES__",
            "Team size": 12,
        },
        "rels": {"Builds": ["Test robot"], "Related projects": ["Demo project"]},
        "srcs": ["ecosystem_switzerland_all.json"],
        "aliases": ["Test Zürich Lab"],
        "country": "Switzerland",
    }
    assert robot == {
        "name": "Test robot",
        "existing_url": None,
        "props": {
            "Kind": "Robot",
            "Open source": "__NO__",
        },
        "rels": {
            "Built by": ["Test Zürich Lab"],
            "Knowledge nodes": ["Control"],
        },
        "srcs": ["ecosystem_switzerland_all.json"],
        "aliases": ["Test robot"],
        "country": "Switzerland",
    }

    second = import_research("Switzerland", source, rows_path)
    assert second == {
        "ecosystem": {"added": 0, "skipped": 1},
        "robots": {"added": 0, "skipped": 1},
    }
    reread = json.loads(rows_path.read_text(encoding="utf-8"))
    assert len(reread["ecosystem"]) == len(reread["robots"]) == 1


def test_place_for_org_adds_country_only_when_requested():
    fields = {"City": "Zurich", "Region": "Europe"}
    assert place_for_org(fields) == "Zurich"
    assert place_for_org(fields, "Switzerland") == "Zurich, Switzerland"
    assert place_for_org({"City": "Zurich, Switzerland"}, "Switzerland") == "Zurich, Switzerland"
    assert place_for_org({"City": "unknown", "Region": "Europe"}, "Germany") == "Germany"
