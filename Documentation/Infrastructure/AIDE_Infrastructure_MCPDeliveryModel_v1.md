# AIDE Infrastructure — MCP Server Delivery Model

Status: tested and confirmed, 2026-09-16. Not yet a formal Infrastructure design
document — Infrastructure's design pass has not been run. This records the empirical
findings and tested methodology so they are available when that pass happens, and so
other components (Orchestration first, then binder, FUP, future tooling) can build
against a grounded model rather than assumptions.

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

### One server codebase

Raw Node.js, CommonJS, newline-delimited JSON over stdio, zero external dependencies
(only Node.js builtins: `readline`, `crypto`). No MCP SDK required — the server
implements raw JSON-RPC directly. 87–88 lines for the tested proof-of-concept.

Newline-delimited JSON framing is required — Claude Desktop's stdio transport expects
`\n`-delimited JSON, not HTTP-style `Content-Length` headers. Using Content-Length
causes a silent 120-second timeout on every connection attempt. This is not
well-documented by Anthropic and was discovered during testing.

### One distribution unit

A marketplace plugin in a git repo. Contains the server code, `.mcp.json` (using
`${CLAUDE_PLUGIN_ROOT}`), skills, and `plugin.json`. The existing AIDE marketplace
repo is `dmoynagh/DigitalBusiness-AIDE-Marketplace`.

Plugin structure:

```
<plugin-name>/
  .claude-plugin/
    plugin.json          — name, version, description
  .mcp.json              — MCP server declaration
  server/
    index.js             — the MCP server
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

### Update path

1. Merge PR to marketplace repo.
2. Refresh the local marketplace clone (`git fetch origin && git reset --hard
   origin/main` in `~/.claude/plugins/marketplaces/<marketplace-name>/`).
3. Restart Claude Desktop.

All three surfaces pick up the new server code. No rebuild, no reinstall, no
separate artifact. Running sessions do not hot-reload — restart is required.

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

---

## Known platform issues (all workaroundable)

### 1. Marketplace clone does not auto-pull reliably

The local clone at `~/.claude/plugins/marketplaces/<name>/` does not automatically
fetch merged PRs. Requires manual `git fetch origin && git reset --hard origin/main`.
The "Update" button was removed from the UI in a recent Claude Desktop version.

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

### MSIX/Windows Store install of Claude Desktop

Dave's Claude Desktop was originally the MSIX/Windows Store build (confirmed via
`Get-AppxPackage`, package family `Claude_pzs8sxrjxfjjc`). This has a known bug
where Python-type Desktop Extensions fail because `${__dirname}` resolves inside the
MSIX virtual filesystem, which spawned `py.exe` processes can't see. Reinstalled to
standalone from `claude.ai/download` to sidestep this and other MSIX
path-virtualisation issues. The Node.js-based approach used here is not affected by
this specific bug, but the standalone install is recommended regardless.

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
