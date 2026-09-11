import json
from pathlib import Path


def deep_merge(base, override):
    """Deep-merge override into base. Keys in override replace the same key in base;
    dicts are merged recursively; everything else is inherited."""
    merged = dict(base)
    for key, value in override.items():
        if key in merged and isinstance(merged[key], dict) and isinstance(value, dict):
            merged[key] = deep_merge(merged[key], value)
        else:
            merged[key] = value
    return merged


def _strip_comments(obj):
    """Remove keys starting with _comment from a parsed JSON object."""
    if isinstance(obj, dict):
        return {k: _strip_comments(v) for k, v in obj.items() if not k.startswith("_comment")}
    if isinstance(obj, list):
        return [_strip_comments(item) for item in obj]
    return obj


def load_json(path):
    with open(path, "r", encoding="utf-8-sig") as f:
        return _strip_comments(json.load(f))


def find_project_root():
    """Walk up from cwd looking for an _aide/ directory."""
    current = Path.cwd()
    for candidate in [current, *current.parents]:
        if (candidate / "_aide").is_dir():
            return candidate
    return None


def load_settings():
    """Load global defaults, then deep-merge per-project settings over them.
    Returns (merged_settings, project_root_or_None)."""
    defaults_path = Path(__file__).parent / "defaults.json"
    settings = load_json(defaults_path)

    project_root = find_project_root()
    if project_root:
        project_settings_path = project_root / "_aide" / "settings.json"
        if project_settings_path.is_file():
            project_settings = load_json(project_settings_path)
            settings = deep_merge(settings, project_settings)

    return settings, project_root
