> identity: Infrastructure_MCPDeliveryModel@v2 | updated: 2026-09-17

# AIDE Infrastructure — MCP Server Delivery Model

Status: tested and confirmed, 2026-09-16; updated 2026-09-17 with skill-delivery
findings and registration-path corrections; updated 2026-09-23 with marketplace
refresh corrections (CLI command is the only working path — restart, remove/re-add
do not pull), Python server encoding fix, multi-server plugin structure, and
confirmed MSIX config path. Not yet a formal Infrastructure design document —
Infrastructure's design pass has not been run. This records the empirical findings
and tested methodology so they are available when that pass happens, and so other
components (Orchestration first, then binder, FUP, future tooling) can build against
a grounded model rather than assumptions.

---

## What this is

A tested, proven model for delivering AIDE functionality as local MCP servers via
Claude Code marketplace plugins, reaching all three Claude Desktop surfaces (Code,
Cowork, Chat) from a single server codebase with automatic update propagation.

This is Infrastructure-owned delivery plumbing — the same kind of thing as the `aide`
CLI host, settings loading, and packaging, extended to cover plugin-based delivery.
Individual components (Orchestration, Build, etc.) are consumers of this model,
not its owners.

---

## The model

### Server codebase

A plugin can contain multiple MCP servers in different languages. The `.mcp.json`
declares each server with its command and args. Two patterns are proven:

- **Node.js** — raw CommonJS, newline-delimited JSON over stdio, zero external
  dependencies. Used by the dispatch server (`server/index.js`).
- **Python** — raw JSON-RPC over stdio, stdlib only (no SDK). Used by the document
  management server (`server/docmgmt/main.py`). On Windows, the config entry must
  use the absolute path to a real Python interpreter — the WindowsApps Store stub
  does not work.

Both implement raw JSON-RPC directly with no MCP SDK dependency.

Newline-delimited JSON framing is required — Claude Desktop's stdio transport expects
`\n`-delimited JSON, not HTTP-style `Content-Length` headers. Using Content-Length
causes a silent 120-second timeout on every connection attempt. This is not
well-documented by Anthropic and was discovered during testing.

**Encoding on Windows:** Python servers must set `sys.stdin.reconfigure(encoding=
"utf-8")` at startup. Without it, stdin defaults to the Windows system codepage
(cp1252), which mangles non-ASCII characters in JSON-RPC requests — including file
content sent to write/patch operations, not just commit messages. Discovered and
fixed in PR #12 (2026-09-23).

### One distribution unit

A marketplace plugin in a git repo. Contains the server code, `.mcp.json` (using
`${CLAUDE_PLUGIN_ROOT}`), skills, and `plugin.json`. The production AIDE marketplace
repo is `dmoynagh/DigitalBusiness-AIDE-Deploy`. The earlier testing repo
`dmoynagh/DigitalBusiness-AIDE-Marketplace` is retained for experiments only.

Plugin structure:

```
<plugin-name>/
  .claude-plugin/
    plugin.json          — name, version, description
  .mcp.json              — MCP server declarations (one or more)
  server/
    index.js             — Node.js MCP server (e.g. dispatch)
    docmgmt/
      main.py            — Python MCP server (e.g. document management)
      config.py, ...     — supporting modules
  skills/<skill-name>/
    SKILL.md             — skill(s) that trigger tools
```

Key detail: `.mcp.json` must use `${CLAUDE_PLUGIN_ROOT}` for paths, not relative
paths. Relative paths fail because the plugin host runs commands with the user's
project directory as CWD, not the plugin's cache directory. This variable is not
prominently documented but is the pattern used by all working marketplace plugins.

### Two config entries, one server file

| Surface | Mechanism | Config location |
|---|---|---|
| Code | Marketplace plugin `.mcp.json` | `enabledPlugins` in `~/.claude/settings.json` |
| Cowork | Marketplace plugin `.mcp.json` | `enabledPlugins` in `~/.claude/settings.json` |
| Chat | `claude_desktop_config.json` entry | `mcpServers` in `%APPDATA%/Claude/claude_desktop_config.json` |

All three surfaces read the **same physical server file** in the marketplace clone.

#### settings.json (Code and Cowork)

```json
"enabledPlugins": {
  "<plugin-name>@<marketplace-name>": true
}
```

#### claude_desktop_config.json (Chat)

```json
"mcpServers": {
  "<plugin-name>-desktop": {
    "command": "node",
    "args": ["~/.claude/plugins/marketplaces/<marketplace-name>/<plugin-name>/server/index.js"]
  }
}
```

The Chat config entry is a **one-time bootstrap**. It points at the same file the
plugin uses, so plugin updates are picked up automatically on restart. No need to
re-run the bootstrap after updates.

### Skill delivery to chat (separate from MCP tools)

Plugin-delivered skills (SKILL.md files) reach claude.ai chat through a different
mechanism from MCP tools. Skills are mounted server-side at `/mnt/skills/plugins/`
based on **account-level** plugin registration, not local Desktop config. This
mechanism is independent of `claude_desktop_config.json` and `settings.json`.

**The registration path matters.** Two different "Add marketplace" paths exist, and
they register at different levels:

| Registration path | Where it registers | What it delivers |
|---|---|---|
| claude.ai web UI → Settings → Plugins | Account level | Skills to chat (server-side mount) |
| Claude Desktop app → Settings → Plugins → Discover | Code tab | MCP tools to Code and Cowork only |

**Both registrations are needed for full three-surface coverage:** the web UI
registration for chat skills, and the Desktop/`settings.json` registration for MCP
tools on Code and Cowork. They are not interchangeable and neither implies the other.

This distinction was discovered on 2026-09-17 when the `aide` plugin's `design-check`
and `messaging` skills were confirmed present in the Deploy repo and correctly merged,
but invisible in chat. The Desktop "Add marketplace" had registered the Deploy repo
under the Code tab only. Re-registering via the web UI at account level made both
skills visible in chat immediately (after starting a fresh session — skills are
frozen at session start).

**Marketplace short form works:** `dmoynagh/DigitalBusiness-AIDE-Deploy` in the web
UI resolves to the full GitHub URL. This is the form used for the original testing
and the production registration.

**Earlier testing (2026-09-04/05) used the web path without realising it.** The test
probes (reach-probe, currency-probe) were registered at account level via the web UI
and worked in chat. When the production marketplace was later added via Desktop, it
went to the wrong level. The distinction was not documented at the time because both
registrations appeared to happen through the same "Add marketplace" action.

### Update path

1. Merge PR to marketplace repo.
2. `claude plugin marketplace update <marketplace-name>` (terminal command — this
   is the platform's mechanism for refreshing the local clone).
3. Restart Claude Desktop.

All three surfaces pick up the new server code. No rebuild, no reinstall, no
separate artifact. Running sessions do not hot-reload — restart is required.

**The merge-PR step is mandatory.** Direct commits to `main` do not trigger plugin
updates. This is a hard build/deployment requirement, not a workflow preference.

**Step 2 requires a terminal.** Claude Desktop's UI does not provide a working
path to refresh marketplace clones — neither restart, nor remove-and-re-add, nor
the Update button triggers a pull from origin. The CLI command is the only
reliable method. See known issues #1 and #9.

**Quit Claude Desktop before running step 2** if the marketplace contains a
running server — the process holds a lock on the clone directory, and the CLI
command fails with EPERM. The aide-desktop dispatch server, when running, is a
common cause.

### Why Chat needs a separate entry

Anthropic's documentation says marketplace-plugin MCP servers should be available in
Chat natively via the plugin's `.mcp.json`. This does not currently work reliably.
Multiple independent reproductions exist (GitHub issues #70397, #77388, #85623,
#86154). In at least one case the MCP server started, completed `initialize` and
`tools/list` successfully, but the tools never reached the Chat model — the break is
inside Claude Desktop's tool-exposure bridge, not in the server or protocol.

The `claude_desktop_config.json` entry is a workaround: same server, different
registration path, works reliably in Chat. When Anthropic fixes the platform bug,
the config entry becomes redundant and can be removed — a removal, not a rework.

---

## What was tested (the evidence base)

Three probes were run on 2026-09-16 across multiple Code sessions:

### Probe 1 — dispatch-probe (v1.0.4)

Plugin with one MCP server, one tool (`test_dispatch`) that invokes Claude Code CLI
and Codex CLI. Confirmed Code works; Cowork appeared negative (later attributed to
UI/local-sync bug, not a real platform limit); Chat not tested in this probe.

### Probe 2 — mcp-ping-test (v1.0.0 → v1.0.2)

Minimal plugin with one `ping` tool returning proof-of-life data (marketplace origin
string, runtime UTC timestamp, runtime UUID). Confirmed Code and Cowork both work.
Chat tested via `.mcpb` Desktop Extension — worked, but bundles a separate copy of
the server that doesn't receive plugin updates.

### Probe 3 — mcp-ping-test (v1.0.3, update propagation)

Added `update-test` field to ping payload, merged via PR, refreshed clone, restarted.
Confirmed all three surfaces return the updated payload from the same server file —
Code via plugin, Chat via `claude_desktop_config.json` entry, Cowork via plugin.
Confirmed the Chat config entry survives plugin updates without re-running bootstrap.

### Probe 4 — orchestration-probe (cross-tool invocation)

Fresh plugin, built applying the proven methodology from the start rather than
rediscovering it. Two tools: `test_python` (spawns a bundled Python script as a
subprocess, returns timestamped JSON with a UUID) and `test_dispatch(target, prompt)`
(invokes `claude -p` or the standalone Codex executable, returns the response).

Confirms an MCP server running inside Claude Desktop can shell out to both Python
tooling and external AI CLIs — the building block for wrapping AIDE's existing Python
utilities (binder builder, FUP deployer) and for cross-platform dispatch, from the same
mechanism, without modification to the underlying scripts.

Both tools pass on all three surfaces. Python on this machine resolves cleanly to the
real interpreter (`Python313\python.exe`) — no Microsoft Store stub, no equivalent of
the Codex PATH-shim problem. Chat was the last surface to pass; getting there required
debugging a config issue, not a code issue — see known issue 6, below.

---

## Known platform issues (all workaroundable)

### 1. Marketplace clone does not auto-refresh

The local clone at `~/.claude/plugins/marketplaces/<name>/` does not automatically
fetch merged PRs on restart, remove-and-re-add, or any Desktop UI action. The
platform's own mechanism is `claude plugin marketplace update <name>` from a
terminal — confirmed 2026-09-23 to force-pull the clone. Neither restart nor
remove-and-re-add triggers a pull from origin. Multiple independent reproductions
exist (GitHub issues #36317, #37252, #38271, #54276, #94516).

### 2. UI plugin install does not persist to local config

Clicking Install in Settings → Plugins → Discover succeeds server-side (account
plugin count increments) but does not write to `enabledPlugins` in `settings.json`
or to `installed_plugins.json`. The "Your plugins" page reads local files and shows
nothing. Workaround: manually add the `enabledPlugins` entry.

### 3. Stale clone causes silent "inline" fallback

When the clone is behind and the plugin directory doesn't exist locally, the installer
falls back to an "inline" mode, creating a data directory with a different naming
pattern. This doesn't register properly and blocks subsequent installs.

### 4. Plugin cache path is inconsistent

`installed_plugins.json` records a cache path that may not exist on disk. The server
actually runs from the marketplace clone. Does not affect the mechanism, but is
confusing during debugging.

### 5. Chat tool-exposure bug (the reason for the config-entry workaround)

Plugin-delivered `.mcp.json` tools don't reliably reach the Chat model despite the
server starting and responding to `initialize` and `tools/list`. Multiple
reproductions across GitHub issues. Workaround: `claude_desktop_config.json` entry.

### 6. A fresh or Extensions-only install may have no `mcpServers` key at all

Don't assume the `mcpServers` block exists in `claude_desktop_config.json` — if the
install has only ever used Desktop Extensions (`.mcpb`), the key may be entirely
absent, not just empty. Check before assuming a "add an entry next to the existing
one" instruction applies; the block itself may need creating first.

**Two parallel mechanisms confirmed to coexist:** the `mcpServers` config block
(Settings → Developer) and installed `.mcpb` Desktop Extensions (Settings →
Extensions, internally called "dxt" — evidenced by `dxt:allowlistEnabled` /
`dxt:allowlistCache` keys in the config). Both can be present on the same install
simultaneously with no conflict.

**`%APPDATA%\Claude` may be an NTFS junction, not MSIX virtualization.** On at least
one tested machine, this path is a plain filesystem junction pointing at
`%LOCALAPPDATA%\Packages\<PackageFamilyName>\LocalCache\Roaming\Claude` — meaning any
process, packaged or not, editing the `%APPDATA%\Claude` path gets transparently
redirected to the real file the app reads. This looks superficially like MSIX
filesystem virtualization (which *would* shadow edits) but isn't the same mechanism —
worth checking (`Get-Item` on the folder, look for `LinkType: Junction`) before
assuming a config edit didn't take effect. Also worth checking `SignatureKind` via
`Get-AppxPackage` — a sideloaded package (`Developer`) behaves differently from a true
Store-distributed one, and the two are easy to conflate.

**Multiple Start Menu "Claude" entries may exist and be indistinguishable.** One
tested machine had two identically-labelled Start Menu entries for Claude Desktop,
same binary version, sharing config via the junction above. Harmless when they share
config, but worth knowing this can happen before treating "wrong instance launched" as
an explanation for unexpected behaviour.

### 7. Desktop "Add marketplace" registers under Code tab, not account level

**This is the highest-impact issue in this list.** Adding a marketplace via Claude
Desktop's Settings → Plugins → Discover registers it under the Code tab only. This
delivers MCP tools to Code and Cowork, but does **not** register at the account level
that feeds skills to chat. The web UI at claude.ai → Settings → Plugins is the only
path to account-level registration.

Symptom: plugin skills appear in Code and Cowork but are absent from the chat
`available_skills` listing and `/mnt/skills/plugins/` mount. MCP tools may or may not
work in chat depending on whether the `claude_desktop_config.json` bootstrap entry
exists (a separate mechanism).

Workaround: register the marketplace via the web UI as well. Both registrations are
needed. The short form (`dmoynagh/DigitalBusiness-AIDE-Deploy`) works in the web UI.

This was not caught during original testing (2026-09-04/05) because the test probes
happened to be registered via the web path. The production marketplace was later added
via Desktop, which went to the wrong level.

### 8. `%APPDATA%\Claude` may not be browsable — use the MSIX-redirected path

On MSIX installs, `%APPDATA%\Claude` may not be visible in File Explorer despite
the config file existing on disk. The real location is the MSIX-redirected path:
`%LOCALAPPDATA%\Packages\<PackageFamilyName>\LocalCache\Roaming\Claude\`. On the
tested machine (package family `Claude_pzs8sxrjxfjjc`), both paths resolve to the
same file — confirmed 2026-09-23 by reading identical content from both via
subprocess. Edit at the MSIX-redirected path if `%APPDATA%\Claude` is not visible.

### 9. Desktop remove-and-re-add reuses the stale clone

Removing a marketplace via Desktop and re-adding it does not clone fresh from
origin — it reuses the existing on-disk clone at `~/.claude/plugins/marketplaces/
<name>/`. Confirmed 2026-09-23: after merging PR #11 (adding a Python MCP server),
remove-and-re-add still showed the clone at PR #5. Only the CLI command
`claude plugin marketplace update <name>` triggers a pull. This matches the
independent reproduction in GitHub issue #54276.

---

## What was also tested and deprioritised

### .mcpb Desktop Extension

Packaging: `manifest.json` (manifest_version 0.3) + bundled server code, built with
`mcpb pack` CLI v2.1.2 into a zip archive. Install: drag into Settings → Extensions.

Works in Chat, but bundles its own copy of the server — plugin updates do not
propagate. Requires rebuilding the `.mcpb` and reinstalling manually to update.
**Deprioritised** in favour of the `claude_desktop_config.json` approach, which
shares the same server file as the plugin and gets updates automatically.

Retained as known-working fallback knowledge, not as part of the active methodology.

Key differences from the plugin path:

| Aspect | Plugin `.mcp.json` | `.mcpb` Extension |
|---|---|---|
| Path variable | `${CLAUDE_PLUGIN_ROOT}` | `${__dirname}` |
| Server code | Shared — marketplace clone | Bundled copy, frozen at build |
| Update path | Merge PR → refresh clone | Rebuild `.mcpb` → reinstall |
| Surfaces | Code, Cowork | Chat |

### MSIX is the only Windows install (no standalone)

As of 2026-09-17, `claude.ai/download` serves only the MSIX package. The
`ClaudeSetup.exe` bootstrapper installs an MSIX sideloaded package
(`SignatureKind: Developer`). The earlier Squirrel-based standalone `.exe` installer
is no longer distributed. Reinstalling from `claude.ai/download` replaces one MSIX
with another — it does not produce a standalone install.

Current install: `C:\Program Files\WindowsApps\Claude_2.110.0.0_x64__pzs8sxrjxfjjc`,
package family `Claude_pzs8sxrjxfjjc`.

The MSIX build has a known bug where Python-type Desktop Extensions fail because
`${__dirname}` resolves inside the MSIX virtual filesystem, which spawned `py.exe`
processes can't see. The Node.js-based approach used here is not affected by this
specific bug.

---

## Broader direction

The tested delivery model applies beyond Orchestration. Any AIDE functionality that
currently lives in the `aide` CLI (binder builder, FUP deployer, cleanup) or that
will be built as new tooling can follow the same pattern: one Node.js MCP server
per tool (or per tool group), delivered as a marketplace plugin, with a Chat bootstrap
entry pointing at the same server file.

This makes the marketplace repo the single distribution point for AIDE's operational
tooling, with git-push-to-PR-merge as the update mechanism and restart as the
propagation step.

The `aide` CLI is not replaced — it remains available for terminal-only use and for
the git-tag auto-update path. But the plugin-delivered MCP server is the primary
delivery surface going forward, because it reaches all three Claude Desktop surfaces
from a single codebase without per-machine CLI installation.

Infrastructure's design pass (not yet run) should formalise this as the standard
delivery model, including: the bootstrap step (potentially automated as an
`aide mcp-register` command or equivalent), the marketplace clone refresh issue
(manual vs automated), and the relationship between CLI-delivered and
plugin-delivered tooling.
