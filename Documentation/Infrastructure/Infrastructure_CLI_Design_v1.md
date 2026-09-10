Infrastructure — CLI Design | design | Infrastructure_CLI_Design@v1 | 2026-09-10

## Summary

The `aide` command is the single entry point to AIDE's infrastructure utilities. It is a Python package distributed via pip from a git repository, installed as a console entry point so that `aide` is available on PATH. On launch it scans for available utilities, applies settings, and presents an interactive menu. Each utility can also be invoked directly as a subcommand.

This document specifies four things: how utilities are discovered, how settings work, how the tool keeps itself current, and how individual utilities can be included or excluded. It is the handoff to a Code session for the build.

Infrastructure owns this design. The individual utility designs (the binder builder, the file-update packager, version cleanup) live with their owning area — File Operations in Working Practices.

---

## Distribution and entry point

The `aide` package is a standard Python package hosted in a git repository and installed with pip. A `console_scripts` entry point registers `aide` as a command, so it is available on PATH after installation.

No PyPI publication. The install source is the git repository directly.

---

## Utility registration

Utilities live as modules in a `utilities/` subpackage inside the `aide` package. The dispatcher scans this subpackage at startup and picks up every module that follows the standard shape:

- A `name` attribute — the display name shown in the menu and used as the subcommand.
- A `description` attribute — a short line shown alongside the name.
- A `run` function — the entry point the dispatcher calls.

Any module in the subpackage that exposes these three things is a utility. No separate registration step, no manifest, no decorator — presence in the subpackage and conformance to the shape is registration.

The three existing utilities each become a module in this subpackage following this shape: the binder builder, the file-update packager, and version cleanup. Their internal logic is unchanged; only the entry point is standardised.

**Consideration noted:** this dispatcher may grow into the full AIDE CLI later, but the design does not anticipate that. The registration model is simple enough to extend if that direction is taken, without needing to be redesigned for it now.

---

## Interactive menu and subcommand support

When invoked without arguments, `aide` presents an interactive menu listing every registered utility by name and description. The user selects one and it runs.

When invoked with a utility name as a subcommand (e.g. `aide binder`), the dispatcher calls that utility's `run` function directly, bypassing the menu. This supports both interactive use and scripting.

The auto-update check (described below) and the manual update command are also available through the menu and as subcommands.

---

## Per-project batch launcher

When invoked from within a project that has an `_aide/` folder, the dispatcher can run a defined sequence of utilities in order. The batch configuration lives in the project settings file. This supports common workflows — for example, running version cleanup, the binder builder, and a git commit in sequence.

---

## Settings

### Format

JSON. This matches the format already used by the existing utility settings files.

### Locations

Three levels, each overriding the one before:

- **Package defaults** live with the installed package. Immutable — shipped as part of the package and overwritten on every update. Never edited by the user.
- **User global** live at `~/.aide/settings.json` (on Windows, `C:\Users\<user>\.aide\`). The user's own global settings — their exclude list, repo URL, anything they want everywhere. Survives updates. Created on first use if absent; skipped silently if missing.
- **Per-project settings** live under `_aide/` at the documentation root of the project. These override both layers above for work in that project.

### Merge behaviour

Deep merge at each layer. Package defaults are merged with user-global settings, then the result is merged with per-project settings. A key present in a higher layer replaces the same key from the layer below; everything else is inherited.

This means each layer only declares what it changes. A user who wants a global exclude list sets it once in `~/.aide/settings.json`. A project that needs different exclude rules states those rules and inherits everything else.

---

## The `_aide` folder

Underscore-prefixed folder at the documentation root. It is the single home for machine-facing operational files in a project:

- Settings (the per-project settings file).
- Logs (if utilities produce them).
- Any other operational state the dispatcher or utilities need per-project.

The underscore prefix keeps it sorted to the top of the directory and signals that it is infrastructure, not content. It sits outside AIDE's document processing — consistent with the convention that underscore-prefixed folders are outside binder scope.

---

## Auto-update

### Automatic check

On launch, the dispatcher checks whether a newer version is available. It does this by comparing the installed version against git release tags in the source repository — no separate update server, no package index query.

The check runs at most once per day. The dispatcher records a "last checked" timestamp and skips the check if less than 24 hours have passed.

### Graceful offline behaviour

If the check fails (no network, repository unreachable), the dispatcher does not retry, does not block, and does not update the "last checked" timestamp. The next launch will try again naturally because the timestamp was not advanced. No retry loop, no error beyond a quiet log entry.

### Manual update

`aide update` forces an immediate update check and applies any available update. Available both as a subcommand and as an item in the interactive menu.

When a newer version is found (by either the automatic or manual check), the dispatcher reports what is available and applies it. The mechanism is a pip install from the git repository — the same command used for initial installation, pointed at the newer tag.

---

## Include and exclude

### Principle

Registration finds everything. Settings decide what is shown.

This is a settings concern, not a registration concern. The dispatcher scans the `utilities/` subpackage and discovers all conforming modules. The settings then filter which of those are presented in the menu and available as subcommands.

### Mechanism

A deny list in settings. Every discovered utility is available by default. To hide one, name it in the exclude list. There is no allow list — the default is "everything on."

### Scope

Both global and per-project, on the same deep-merge model as all other settings. A global exclude hides a utility everywhere. A per-project exclude hides it for that project only, without affecting global availability.

The merge means a project can exclude utilities that are globally available, or (by overriding the exclude list) restore utilities that are globally excluded. The same deep-merge rules apply.

---

## What this document does not cover

- The internal design of the three existing utilities — those are owned by File Operations in Working Practices.
- The broader question of whether utilities grow into a full AIDE CLI — that is a future direction, noted as a consideration, not designed for.
- The content of the global settings file beyond the structures needed for merge and exclude — each utility defines what settings it needs.

---

Version note: v1 — design document from voice session 2026-09-10. All four items were settled in conversation; this document records the design for handoff to a Code session.
