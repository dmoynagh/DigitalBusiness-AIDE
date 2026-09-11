import importlib
import pkgutil
import subprocess
import sys
from pathlib import Path

from aide import utilities as utilities_pkg
from aide.settings import load_settings
from aide.updater import check_for_updates, force_update


class Context:
    """Passed to each utility's run function."""

    def __init__(self, settings, project_root):
        self.settings = settings
        self.project_root = project_root

    def git_commit(self, message, paths=None):
        """Stage paths and commit with a descriptive message."""
        if paths:
            for p in paths:
                subprocess.run(["git", "add", str(p)], check=True)
        subprocess.run(["git", "commit", "-m", message], check=True)


def discover_utilities():
    """Scan the utilities subpackage for modules with name, description, run."""
    found = {}
    for _importer, modname, _ispkg in pkgutil.iter_modules(utilities_pkg.__path__):
        mod = importlib.import_module(f"aide.utilities.{modname}")
        if hasattr(mod, "name") and hasattr(mod, "description") and hasattr(mod, "run"):
            found[mod.name] = mod
    return found


def filter_utilities(utilities, settings):
    exclude = settings.get("exclude", [])
    return {name: mod for name, mod in utilities.items() if name not in exclude}


def show_menu(utilities, settings, project_root):
    items = sorted(utilities.items())
    print("\nAIDE Utilities\n")
    for i, (_name, mod) in enumerate(items, 1):
        print(f"  {i}. {mod.name} — {mod.description}")

    extras = []
    if settings.get("batch"):
        extras.append(("batch", "Run configured batch sequence"))
    extras.append(("update", "Check for updates"))

    for i, (label, desc) in enumerate(extras, len(items) + 1):
        print(f"  {i}. {label} — {desc}")
    print(f"  0. Exit\n")

    choice = input("Select: ").strip()
    if choice == "0" or choice == "":
        return

    try:
        idx = int(choice)
    except ValueError:
        print("Invalid selection.")
        return

    if 1 <= idx <= len(items):
        name, mod = items[idx - 1]
        ctx = Context(settings.get(name, {}), project_root)
        mod.run(ctx)
    elif 1 <= idx - len(items) - 1 < len(extras):
        label = extras[idx - len(items) - 1][0]
        if label == "update":
            force_update(settings)
        elif label == "batch":
            run_batch(utilities, settings, project_root)
    else:
        print("Invalid selection.")


def run_batch(utilities, settings, project_root):
    sequence = settings.get("batch", [])
    if not sequence:
        print("No batch sequence configured.")
        return
    for name in sequence:
        if name in utilities:
            print(f"\n--- {utilities[name].name} ---")
            ctx = Context(settings.get(name, {}), project_root)
            utilities[name].run(ctx)
        else:
            print(f"Skipping '{name}' — not available.")


def main():
    settings, project_root = load_settings()
    check_for_updates(settings)

    all_utilities = discover_utilities()
    utilities = filter_utilities(all_utilities, settings)

    if len(sys.argv) > 1:
        command = sys.argv[1]
        if command == "update":
            force_update(settings)
        elif command == "batch":
            run_batch(utilities, settings, project_root)
        elif command in utilities:
            ctx = Context(settings.get(command, {}), project_root)
            utilities[command].run(ctx)
        else:
            print(f"Unknown command: {command}")
            print(f"Available: {', '.join(sorted(utilities))} | update | batch")
            sys.exit(1)
    else:
        show_menu(utilities, settings, project_root)
