import argparse
import json
from pathlib import Path

try:
    from .build_data import RELATION_FIELDS
    from .data_common import DATA_DIR, read_json
    from .normalize import canon, norm
except ImportError:
    from build_data import RELATION_FIELDS
    from data_common import DATA_DIR, read_json
    from normalize import canon, norm


KINDS = (
    ("organizations", "ecosystem", "Organization"),
    ("robots_models", "robots", "Name"),
)


def _encode_props_and_rels(record, kind, name_key):
    props = {}
    rels = {}
    relation_fields = RELATION_FIELDS[kind]

    for field, value in record.items():
        if field == name_key or field.startswith("_"):
            continue
        if field in relation_fields:
            values = value if isinstance(value, list) else ([] if value is None or value == "" else [value])
            if values:
                rels[field] = values
            continue
        if isinstance(value, bool):
            value = "__YES__" if value else "__NO__"
        elif isinstance(value, list):
            value = json.dumps(value, ensure_ascii=False)
        props[field] = value

    return props, rels


def import_research(country, source_path, rows_path=None):
    source_path = Path(source_path)
    rows_path = Path(rows_path) if rows_path else DATA_DIR / "rows.json"
    source = json.loads(source_path.read_text(encoding="utf-8"))
    rows = read_json(rows_path)
    result = {}

    for source_kind, row_kind, name_key in KINDS:
        existing = rows.setdefault(row_kind, [])
        seen = {norm(canon(row["name"])) for row in existing}
        added = skipped = 0
        for record in source.get(source_kind, []):
            name = record[name_key]
            key = norm(canon(name))
            if key in seen:
                skipped += 1
                continue
            props, rels = _encode_props_and_rels(record, row_kind, name_key)
            row = {
                "name": name,
                "existing_url": None,
                "props": props,
                "rels": rels,
                "srcs": [source_path.name],
                "aliases": [name],
                "country": country,
            }
            existing.append(row)
            seen.add(key)
            added += 1
        result[row_kind] = {"added": added, "skipped": skipped}

    rows_path.write_text(
        json.dumps(rows, ensure_ascii=False, indent=1) + "\n",
        encoding="utf-8",
    )
    for kind, counts in result.items():
        print(f"{kind}: added {counts['added']}, skipped {counts['skipped']}")
    return result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--country", required=True)
    parser.add_argument("source", type=Path)
    args = parser.parse_args()
    import_research(args.country, args.source)


if __name__ == "__main__":
    main()
