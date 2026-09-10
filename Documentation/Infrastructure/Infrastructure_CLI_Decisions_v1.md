Infrastructure — CLI Decisions | decisions | Infrastructure_CLI_Decisions@v1 | 2026-09-10

## Utility registration — convention scanning over alternatives

Three options were on the table: convention-based scanning of a subpackage, a registry file listing available utilities, and decorator-based registration.

Convention scanning was chosen (strong recommendation, agreed). There are three utilities now and likely only a handful more over time. A registry file is a second artefact to maintain for no benefit at this scale — every time a utility is added, the registry must also be updated, which is exactly the kind of coordination step that adds friction without adding value. Decorators add a layer of indirection that buys nothing when everything lives in one package. Convention scanning is the simplest thing that works: drop a module in the folder following the agreed shape, and it appears.

The CLI-growth consideration was raised by Dave: this dispatcher may become the full AIDE CLI. The response was that convention scanning does not paint the design into a corner — a folder of utilities following a shared shape is exactly the foundation a bigger CLI would want. The temptation to pre-build grouping, categories, or a richer interface was explicitly named as the apparatus trap. The consideration is logged but does not drive the current design.

## Settings format — JSON over YAML

The three existing utilities already use JSON settings files. YAML is friendlier to hand-edit but would be a new format to introduce for no demonstrated gain. Matching what is already in use on the project costs nothing and avoids a format split between existing utility settings and the new dispatcher settings.

## Settings merge — deep merge over full replacement

Deep merge means a per-project settings file overrides individual values without needing to restate the surrounding structure. The alternative — full replacement per key — would force a project to copy an entire settings block just to change one value inside it. That is more brittle and harder to keep in step with the global defaults as they evolve.

## Three-layer settings — package defaults separated from user global

The original design had two layers: global settings with the installed package, and per-project overrides. This missed a problem: pip overwrites the package directory on every update, so any user-edited global settings (a custom exclude list, a repo URL override) would be lost on the next `aide update`.

The fix separates immutable package defaults (shipped with the package, never edited) from user-global settings (`~/.aide/settings.json`, survives updates). Per-project remains the third layer. The auto-update state file already lived at `~/.aide/state.json`, so the convention was already established — settings just needed to follow it.

## The `_aide` folder — Dave's initiative

The original proposal placed per-project settings under `_utilities`. Dave pushed back: he wanted the number of root-level operational folders kept lean and preferred one generic home for machine-facing files rather than several purpose-specific ones. The folder would hold settings, logs, and utilities as a subfolder only if needed.

The name `_aide` was chosen over `_system` because it matches the framework name and the existing underscore-prefix convention already established for operational folders (`_index`, `_archived`, `_binders`, `_fileupdatepackages`). The underscore sorts it to the top of the directory listing and signals that it is infrastructure, not content.

## Auto-update frequency — daily over every-launch

Checking on every launch adds a network call and a slight delay each time the dispatcher runs, which gets annoying with frequent use. Once a day catches updates promptly without that friction. The manual `aide update` command is always available for an on-demand check, so the daily cadence never blocks a user who wants to check sooner.

## Auto-update version detection — git tags over commit hashes

The package is installed from a git repository, so git tags are the natural version signal. Commit hashes do not indicate whether a change is meaningful — a documentation-only commit and a breaking change look the same. Release tags carry explicit version semantics.

## Auto-update offline behaviour — graceful skip over retry

Dave asked specifically about the retry model. The decision was: no retry loop, no background process, no machinery. If the daily check fails because the network is unreachable, the dispatcher does not update the "last checked" timestamp. The next launch sees the check is still due and tries again naturally. Offline means "still due," not "retry now." This keeps the auto-update behaviour proportionate — a single quiet check, never a blocker.

## Include/exclude form — deny list over allow list

By default, every utility the dispatcher discovers is available. To hide one, name it in an exclude list. The alternative — an allow list where every utility must be explicitly enabled — means that adding a new utility requires updating every project's settings to make it visible. That contradicts the low-fuss spirit of convention scanning: a new module in the subpackage should just work everywhere unless deliberately turned off.

## Include/exclude as a settings concern, not a registration concern

Registration discovers everything that exists in the subpackage. Settings decide what is shown. Mixing the two — having registration itself honour include/exclude rules — would mean the dispatcher's scanning logic needs to know about settings before it has finished loading them. Keeping the concerns separate is both simpler and more predictable: scan first, filter second.

## Include/exclude scope — both global and per-project

This rides on the deep-merge settings model already settled. A global exclude hides a utility everywhere. A per-project exclude hides it for that project only. A per-project override can also restore a globally excluded utility. No new mechanism — it is just another setting following the same merge rules.

## Project root detection — walk up to repo boundary

Three options were considered: hardcoding the documentation root path in settings, using the git repo root directly, or walking up from the current directory. Walk-up was chosen. A hardcoded path is brittle and forces per-project configuration for something that should just work. Using the git root directly would require knowing the documentation folder's name within the repo, which is also configuration. Walking up and looking for `_aide/` is self-discovering — the folder's presence is both the marker and the configuration. The git repo boundary is the natural stop point, since `_aide/` above the repo root would belong to a different project.

## Multi-binder — run all definitions found, not just one

The original design assumed one binder settings file per project. In practice, the AIDE documentation already has two binders with different scopes and different file type rules — one for the full documentation set and one for the AI-facing subset. Erroring on multiple files forced the user to choose one, which defeated the purpose of having both. The utility now discovers all settings files in its subfolder and runs each. No configuration needed — presence is registration, the same principle as utility discovery in the dispatcher.

---

Version note: v1 — reasoning from voice session 2026-09-10. All four items were settled in conversation; this document records the alternatives considered and the reasons for each choice.
