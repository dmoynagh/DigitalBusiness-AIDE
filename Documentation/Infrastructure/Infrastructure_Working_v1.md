Infrastructure | working | Infrastructure_Working@v1 | 2026-09-10

## Confirmed direction — session 2026-09-10

### Utility distribution model

Utilities are distributed as a pip package installed from git. `pip install git+https://github.com/...` installs the package and registers the `aide` command on PATH. Updates via `pip install --upgrade` or a self-update command (`aide update`).

The design-to-distribution workflow: update the utility design → rebuild the utility → commit to the utilities repo → user runs `aide update` or is prompted when a new version is available.

This mirrors the AIDE framework's approach to deploying capabilities: design, build, publish, and the consumer installs and updates.

### The aide dispatcher

A single entry point command — `aide` — on PATH. Behaviour:

- **No arguments** — interactive text menu listing available utilities. User selects and runs.
- **With subcommand** — runs directly, e.g. `aide binder-build`, for users who know what they want.
- **Customisation** — allows configuring settings for utilities within the interactive interface.

The dispatcher also serves as the registration point for utilities — adding a utility means adding a module to the package and registering a subcommand. New utilities appear in the menu automatically.

### Per-project launcher

A simple batch file (or similar) placed in the project's documentation folder. Runs the `aide` dispatcher targeting the current folder. Provides right-click or double-click access from Explorer without requiring a terminal.

### Settings model

Global defaults with per-project overrides. Global settings live with the central utility installation. Per-project settings live in the project's documentation folder (in `_utilities/` or `_config/`). The dispatcher merges them — global provides defaults, per-project overrides where needed.

Log files can go to a subfolder under the per-project settings location.

When launching, the execution folder is passed to the utility. The utility probes for settings files relative to the execution location, loads and uses them. If settings are edited within the aide interactive interface, they are written back to the same location.

### Items needing further design

- Utility registration mechanism — how the dispatcher discovers available utilities (subdirectory scan, config file, or package entry points)
- Detailed settings file format and merging rules
- Auto-update behaviour — check on launch, prompt, or silent
- Include/exclude mechanism — option to manually include or exclude utilities, install by default or prompt for new ones

---

Version note: v1 — initial working document from session 2026-09-10. Confirmed direction, not complete design.
