import re
import unicodedata


def norm(value):
    return re.sub(r"[\W_]+", "", (value or "").lower())


def strip_paren(value):
    return re.sub(r"\s*\([^)]*\)", "", value or "").strip()


ALIAS = {
    "SO-101 arm": "SO-101",
    "pi0": "π0 / π0.5",
    "pi0 (Physical Intelligence)": "π0 / π0.5",
    "pi0.5 (Physical Intelligence)": "π0 / π0.5",
    "GR00T N1": "Isaac GR00T",
    "Mirokaï (Miroki / Miroka)": "Miroki / Miroka",
    "Isaac Lab": "Isaac Sim / Isaac Lab",
    "NVIDIA Isaac Lab": "Isaac Sim / Isaac Lab",
    "NVIDIA Isaac Sim": "Isaac Sim / Isaac Lab",
    "NVIDIA Isaac Sim (in Comau controllers)": "Isaac Sim / Isaac Lab",
    "Franka Research 3": "Franka Research 3 (FR3)",
    "Genesis (physics simulator)": "Genesis",
    "AEON": "AEON (Hexagon Robotics)",
    "ACT (Action Chunking with Transformers)": "ACT (Action Chunking Transformer)",
    "AMI (Advanced Machine Intelligence)": "Advanced Machine Intelligence (AMI)",
    "AMI Labs (Advanced Machine Intelligence)": "Advanced Machine Intelligence (AMI)",
    "Hugging Face": "Hugging Face (LeRobot)",
    "Pollen Robotics": "Pollen Robotics (Hugging Face)",
    "ISIR (Institut des Systèmes Intelligents et de Robotique)": "ISIR (Sorbonne Université)",
    "automatica (Munich)": "automatica",
    "GdR Robotique (CNRS)": "GdR Robotique (CNRS research network)",
    "LIRMM (Robotics department)": "LIRMM",
    "ICube (Strasbourg)": "ICube",
    "Heudiasyc (UTC)": "Heudiasyc",
    "TIMC (Grenoble)": "TIMC",
    "I3S (Université Côte d'Azur)": "I3S",
}
ALIAS_N = {norm(key): value for key, value in ALIAS.items()}


def canon(name):
    return ALIAS_N.get(norm(name), name)


def slugify(name):
    value = unicodedata.normalize("NFKC", name or "").casefold()
    parts = []
    for char in value:
        if char.isalnum():
            parts.append(char)
        elif parts and parts[-1] != "-":
            parts.append("-")
    return "".join(parts).strip("-") or "unnamed"


def resolve_name(name, names):
    by_norm = {norm(candidate): candidate for candidate in names}
    by_strip = {}
    for candidate in names:
        by_strip.setdefault(norm(strip_paren(candidate)), set()).add(candidate)

    canonical = canon(name)
    if norm(canonical) in by_norm:
        return by_norm[norm(canonical)]
    matches = by_strip.get(norm(strip_paren(canonical)), set())
    if len(matches) == 1:
        return next(iter(matches))
    matches = by_strip.get(norm(canonical), set())
    if len(matches) == 1:
        return next(iter(matches))
    return None
