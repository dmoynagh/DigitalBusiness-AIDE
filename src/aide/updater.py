import json
import subprocess
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

from aide import __version__

STATE_DIR = Path.home() / ".aide"
STATE_FILE = STATE_DIR / "state.json"
CHECK_INTERVAL = timedelta(hours=24)


def _read_state():
    if STATE_FILE.is_file():
        with open(STATE_FILE, "r", encoding="utf-8-sig") as f:
            return json.load(f)
    return {}


def _write_state(state):
    STATE_DIR.mkdir(parents=True, exist_ok=True)
    with open(STATE_FILE, "w", encoding="utf-8") as f:
        json.dump(state, f, indent=2)


def _parse_version(tag):
    """Parse a version tag like 'v0.1.0' or '0.1.0' into a comparable tuple."""
    tag = tag.lstrip("v")
    try:
        return tuple(int(x) for x in tag.split("."))
    except (ValueError, AttributeError):
        return None


def _current_version():
    return _parse_version(__version__)


_UNREACHABLE = "unreachable"


def _fetch_latest_tag(repo_url):
    """Query the remote repo for release tags.
    Returns (tag, version_tuple), _UNREACHABLE, or None (reachable but no tags)."""
    try:
        result = subprocess.run(
            ["git", "ls-remote", "--tags", repo_url],
            capture_output=True, text=True, timeout=15,
        )
        if result.returncode != 0:
            return _UNREACHABLE
    except (subprocess.TimeoutExpired, FileNotFoundError):
        return _UNREACHABLE

    best = None
    for line in result.stdout.strip().splitlines():
        parts = line.split("refs/tags/")
        if len(parts) != 2:
            continue
        tag = parts[1]
        if tag.endswith("^{}"):
            tag = tag[:-3]
        version = _parse_version(tag)
        if version and (best is None or version > best[1]):
            best = (tag, version)

    return best


def _apply_update(repo_url, tag):
    print(f"Installing aide {tag} ...")
    subprocess.run(
        [sys.executable, "-m", "pip", "install", "--upgrade",
         f"git+{repo_url}@{tag}"],
        check=True,
    )
    print("Update complete.")


def check_for_updates(settings):
    """Auto-check: runs at most once per day. Skips silently if offline."""
    repo_url = settings.get("update", {}).get("repo_url")
    if not repo_url:
        return

    state = _read_state()
    last_checked = state.get("last_checked")
    if last_checked:
        last_dt = datetime.fromisoformat(last_checked)
        if datetime.now(timezone.utc) - last_dt < CHECK_INTERVAL:
            return

    latest = _fetch_latest_tag(repo_url)
    if latest is _UNREACHABLE:
        return
    if latest is None:
        state["last_checked"] = datetime.now(timezone.utc).isoformat()
        _write_state(state)
        return

    tag, version = latest
    state["last_checked"] = datetime.now(timezone.utc).isoformat()
    _write_state(state)

    if version > _current_version():
        print(f"\nUpdate available: {__version__} -> {tag}")
        _apply_update(repo_url, tag)
        print()


def force_update(settings):
    """Manual update: always checks and applies if available."""
    repo_url = settings.get("update", {}).get("repo_url")
    if not repo_url:
        print("No update repository configured.")
        return

    print(f"Checking for updates (current: {__version__}) ...")
    latest = _fetch_latest_tag(repo_url)

    if latest is _UNREACHABLE:
        print("Could not reach the update repository.")
        return

    state = _read_state()
    state["last_checked"] = datetime.now(timezone.utc).isoformat()
    _write_state(state)

    if latest is None:
        print("Already up to date.")
        return

    tag, version = latest
    if version > _current_version():
        print(f"Update available: {__version__} -> {tag}")
        _apply_update(repo_url, tag)
    else:
        print("Already up to date.")
