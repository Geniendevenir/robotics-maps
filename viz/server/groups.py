import json
import re
import secrets
import threading
from datetime import datetime, timezone
from pathlib import Path


DEFAULT_GROUPS_PATH = Path(__file__).resolve().parents[1] / "state" / "groups.json"
DEFAULT_COLOR = "#e4572e"
COLOR_PATTERN = re.compile(r"^#(?:[0-9a-fA-F]{3}|[0-9a-fA-F]{6})$")


def timestamp():
    return datetime.now(timezone.utc).isoformat()


def validate_color(color):
    if not isinstance(color, str) or not COLOR_PATTERN.fullmatch(color):
        raise ValueError("color must be a 3- or 6-digit hex value")
    return color


class GroupStore:
    def __init__(self, path=DEFAULT_GROUPS_PATH):
        self.path = Path(path)
        self._lock = threading.RLock()
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self._groups = self._read()

    def _read(self):
        if not self.path.exists():
            return []
        return json.loads(self.path.read_text(encoding="utf-8"))

    def _persist(self):
        self.path.parent.mkdir(parents=True, exist_ok=True)
        temporary = self.path.with_suffix(".tmp")
        temporary.write_text(
            json.dumps(self._groups, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
        temporary.replace(self.path)

    def list(self):
        with self._lock:
            return json.loads(json.dumps(self._groups, ensure_ascii=False))

    def get(self, group_id):
        with self._lock:
            for group in self._groups:
                if group["id"] == group_id:
                    return json.loads(json.dumps(group, ensure_ascii=False))
        raise KeyError(group_id)

    def create(self, name, description="", color="#e4572e", node_ids=None, created_by="user"):
        color = DEFAULT_COLOR if color is None or color == "" else validate_color(color)
        now = timestamp()
        with self._lock:
            group_id = f"g_{secrets.token_hex(3)}"
            while any(group["id"] == group_id for group in self._groups):
                group_id = f"g_{secrets.token_hex(3)}"
            group = {
                "id": group_id,
                "name": name.strip(),
                "description": description or "",
                "color": color,
                "node_ids": list(dict.fromkeys(node_ids or [])),
                "created_by": created_by if created_by in ("user", "agent") else "user",
                "created_at": now,
                "updated_at": now,
            }
            self._groups.append(group)
            self._persist()
            return json.loads(json.dumps(group, ensure_ascii=False))

    def update(self, group_id, **fields):
        color = fields.get("color")
        if color is not None and color != "":
            validate_color(color)
        with self._lock:
            group = self._find(group_id)
            for key in ("name", "description", "color"):
                if key not in fields or fields[key] is None:
                    continue
                value = fields[key]
                if key == "name":
                    group[key] = value.strip()
                elif key == "color":
                    if value != "":
                        group[key] = value
                else:
                    group[key] = value
            group["updated_at"] = timestamp()
            self._persist()
            return json.loads(json.dumps(group, ensure_ascii=False))

    def add_nodes(self, group_id, node_ids):
        with self._lock:
            group = self._find(group_id)
            group["node_ids"] = list(dict.fromkeys(group["node_ids"] + list(node_ids)))
            group["updated_at"] = timestamp()
            self._persist()
            return json.loads(json.dumps(group, ensure_ascii=False))

    def remove_nodes(self, group_id, node_ids):
        remove = set(node_ids)
        with self._lock:
            group = self._find(group_id)
            group["node_ids"] = [node_id for node_id in group["node_ids"] if node_id not in remove]
            group["updated_at"] = timestamp()
            self._persist()
            return json.loads(json.dumps(group, ensure_ascii=False))

    def delete(self, group_id):
        with self._lock:
            before = len(self._groups)
            self._groups = [group for group in self._groups if group["id"] != group_id]
            if len(self._groups) == before:
                raise KeyError(group_id)
            self._persist()

    def _find(self, group_id):
        for group in self._groups:
            if group["id"] == group_id:
                return group
        raise KeyError(group_id)
