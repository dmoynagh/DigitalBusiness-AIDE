> identity: Orchestration_InvestigationFindings@v1 | updated: 2026-09-15

# AIDE Orchestration — Investigation Findings

Version 1. 2026-09-15. Investigation against `AIDE_Orchestration_WIP_v1.md`.

---

## Area 1 — Claude Code Programmatic Invocation

### What was tested

The scoping document's "Agent SDK wrapper" maps to a specific, real product: the **Claude Agent SDK** — available as `@anthropic-ai/claude-agent-sdk` (TypeScript) and `claude-agent-sdk` (Python). Installed on this machine as Claude Code 2.1.270.

Investigated: official documentation at `code.claude.com/docs/en/agent-sdk`, the TypeScript API reference, the quickstart, and the headless/subprocess documentation. Also examined the Claude Code CLI's non-interactive mode (`claude -p`).

### What works

**Intent-level delegation is confirmed.** The SDK entry point is:

```typescript
import { query } from "@anthropic-ai/claude-agent-sdk";

for await (const message of query({
  prompt: "Apply this specification to the codebase",
  options: {
    allowedTools: ["Read", "Edit", "Bash", "Glob", "Grep"],
    permissionMode: "acceptEdits",
    cwd: "/path/to/project",
    maxBudgetUsd: 5.00,
    maxTurns: 20,
    outputFormat: {
      type: "json_schema",
      schema: { /* verification response schema */ }
    }
  }
})) {
  // Stream messages: assistant reasoning, tool calls, results
}
```

The agent loop owns file discovery, edit planning, and execution. The caller describes WHAT needs to change; the agent decides HOW. This is exactly the separation the scoping document assumed.

**Structured output is supported.** The `outputFormat` option accepts a JSON Schema. The agent's final response conforms to it. This means the verification response can be schema-constrained.

**Full local capability confirmed.** Built-in tools include Read, Write, Edit, Bash, Glob, Grep, WebSearch, WebFetch. The agent has access to the filesystem, git, and shell commands within the working directory (and any `additionalDirectories`).

**Session management exists.** Sessions persist to disk. Functions: `listSessions()`, `getSessionMessages()`, `getSessionInfo()`, `renameSession()`, `tagSession()`. Resume via `options.resume` (session ID) or `options.continue` (most recent).

**Subagent support exists.** Agents can be defined inline and spawned for subtasks:

```typescript
options: {
  agents: {
    reviewer: {
      instructions: "You are a code reviewer",
      maxTurns: 5,
      outputFormat: { type: "json_schema", schema: reviewSchema }
    }
  }
}
```

**Hooks system exists.** Custom code can run at lifecycle points (SessionStart, Setup, SessionEnd, etc.).

**Cost control exists.** `maxBudgetUsd` stops the agent when cost reaches a USD threshold. `maxTurns` limits complexity.

**MCP server support.** External tools can be connected via the `mcpServers` option — this means the orchestration layer could expose its own tools to the agent.

### CLI alternative — `claude -p`

For simpler invocations, the CLI works as a subprocess:

```bash
claude -p "Apply the FUP specification" \
  --output-format json \
  --json-schema '{"type":"object","properties":{"summary":{"type":"string"},"files_changed":{"type":"array","items":{"type":"string"}},"status":{"type":"string"}},"required":["summary","files_changed","status"]}' \
  --allowedTools "Read,Edit,Bash,Glob,Grep" \
  --permission-mode acceptEdits
```

The docs state: "To drive the same agent loop from another language, run the CLI as a subprocess with the `-p` flag and `--output-format json`."

The CLI supports session resume (`--continue`, `--resume <id>`), structured output, tool approval, and all the agent capabilities. The JSON output includes `session_id`, `result`, `total_cost_usd`, and metadata.

### Actual limits

| Constraint | Value |
|---|---|
| Context window | 1M tokens (Opus 5 default) |
| Max output tokens | 128K per response |
| Piped stdin | 10 MB cap |
| Timeout | Configurable; 10-minute default for background waits |
| Filesystem scope | Working directory + `additionalDirectories` |
| SDK packaging | Bundles a native Claude Code binary (~50MB) |

### What didn't work / caveats

- The SDK bundles a native binary. The npm/pip package is platform-specific (includes the Claude Code executable). This is not an issue for local use but affects deployment portability.
- The SDK spawns a child process — it is not an in-process library call. This has latency implications for rapid-fire invocations (though `startup()` provides a warm query path).
- No built-in "diff of changed regions" in the response format. The agent CAN report what it changed in free text, and the `outputFormat` can require structured fields, but you cannot get git-level diffs automatically. A post-invocation `git diff` is the correct way to capture diffs.

### Recommended design

**Use the TypeScript Agent SDK (`@anthropic-ai/claude-agent-sdk`) for the automated MCP transport.** It provides exactly the intent-level delegation the architecture assumed, with structured output, cost control, session management, and full local tool access.

For the manual transport (copy-paste), `claude -p` with `--output-format json --json-schema` is the CLI equivalent.

The `startup()` warm-query path should be used when the orchestration layer needs to submit multiple tasks in sequence — it keeps the Claude Code binary alive between invocations.

---

## Area 2 — OAuth / Subscription Authentication

### What was tested

Checked Claude Code auth status on this machine. Examined the Agent SDK documentation's authentication section. Reviewed the CLI's bare vs non-bare mode auth behaviour.

### What works

**Subscription auth is confirmed working.** Claude Code on this machine reports:

```json
{
  "loggedIn": true,
  "authMethod": "claude.ai",
  "apiProvider": "firstParty",
  "subscriptionType": "max",
  "email": "david@moynagh.co.nz"
}
```

**Non-bare mode uses subscription auth.** When the SDK runs in default (non-bare) mode, the Claude Code binary reads OAuth credentials from the system keychain. This is the logged-in Max subscription — no API key needed.

**Bare mode requires an API key.** The docs state: "In bare mode, Claude Code never reads OAuth credentials or the system keychain." Set `ANTHROPIC_API_KEY` or provide an `apiKeyHelper` in settings.

### The "third party" policy

The SDK docs contain this note:

> "Unless previously approved, Anthropic does not allow third party developers to offer claude.ai login or rate limits for their products, including agents built on the Claude Agent SDK."

**This is a distribution policy, not a technical block.** It restricts developers who build products for OTHER people using subscription auth. Dave is building AIDE for personal use — this is first-party use of his own subscription, not a product distributed to others. The technical mechanism (keychain-based OAuth) works regardless.

### Environment variable precedence (confirmed from docs)

1. Cloud credentials (Bedrock, Vertex, Foundry env vars)
2. `ANTHROPIC_AUTH_TOKEN`
3. `ANTHROPIC_API_KEY`
4. Logged-in OAuth profile (keychain)
5. Workload Identity Federation env vars
6. Default profile on disk

**Critical: if `ANTHROPIC_API_KEY` is set, it shadows the subscription login.** Ensure it is unset in the orchestration environment.

### Billing pool

Usage from non-bare SDK invocations draws from the **Max 5x subscription quota** — the same pool as interactive Claude Code sessions. This is usage-counted, not dollar-billed.

The SDK credit pool ($100/month at API rates for Max 5x) applies to **API-key-authenticated** calls only. It is a separate credit for programmatic use via `ANTHROPIC_API_KEY`. Its status on this account was not directly verifiable from this session.

### Recommended configuration

```
# Ensure no API key shadows subscription auth:
# ANTHROPIC_API_KEY must be UNSET

# No special environment variables needed.
# The Agent SDK in non-bare mode (the default) reads
# the logged-in session from the system keychain.
```

For the orchestration layer, the only requirement is that Dave is logged in to Claude Code (`claude auth login`). The SDK picks up the subscription automatically.

### What was hard

There is no programmatic way to query "which billing pool am I using" from the SDK. The `system/init` event in stream-json mode reports the model and auth method, but not the billing pool. Cost tracking is available via `total_cost_usd` in the response metadata, but this is a client-side estimate, not a billing-pool report.

---

## Area 3 — Desktop Extension Packaging (MCPB)

### What was tested

Researched the current Desktop Extension format, manifest schema, build workflow, developer experience, permissions, and the relationship between extensions and Claude Code's agent capabilities.

### What works

**The format is MCPB** (MCP Bundles, file extension `.mcpb`). Supersedes the earlier `.dxt` format. Manifest spec v0.3 (as of 2025-12-02).

An `.mcpb` file is a ZIP archive containing:
- `manifest.json` (required) — describes the extension, its server configuration, and user-configurable fields
- `server/` directory with implementation code
- Bundled dependencies

**Manifest schema (key fields):**

```json
{
  "manifest_version": "0.3",
  "name": "aide-orchestrator",
  "version": "1.0.0",
  "description": "AIDE orchestration work-package transport",
  "author": { "name": "David Moynagh" },
  "server": {
    "type": "node",
    "entry_point": "server/index.js",
    "mcp_config": {
      "command": "node",
      "args": ["${__dirname}/server/index.js"]
    }
  },
  "user_config": {
    "project_root": {
      "type": "directory",
      "title": "Project Root",
      "required": true
    }
  }
}
```

**Build workflow:**
```
npm install -g @anthropic-ai/mcpb
mcpb init          # generates manifest interactively
mcpb validate .    # validates manifest
mcpb pack .        # bundles into .mcpb
```
Install: double-click the `.mcpb` file or drag into Claude Desktop.

**Capabilities:**
- Full local filesystem/git/shell access (no sandbox)
- OS keychain for secrets via `sensitive: true` config fields
- Cross-platform (macOS, Windows) with platform-specific overrides
- Enterprise allowlisting for organizational control
- Node.js runtime bundled with Claude Desktop

### What didn't work — the architectural mismatch

**Desktop Extensions are the wrong mechanism for the core orchestration problem.**

A Desktop Extension is an MCP server. It exposes tools, resources, and prompts that Claude Desktop's chat can CALL. It is a passive tool provider. It cannot:

- Invoke Claude Code's agent loop
- Trigger a background agent session
- Drive multi-step execution
- Manage subagents or sessions

The orchestration architecture needs to INVOKE Claude's agent capabilities (via the Agent SDK), not EXPOSE tools for Claude to call. A Desktop Extension sits on the wrong side of the invocation: it gives chat new tools, but the expensive work (reasoning about files, planning edits) still happens in chat — exactly the `mcp serve` pattern the scoping document rejected.

### Recommended design

**Desktop Extensions have a role, but not the one originally scoped.**

They are suitable for:
1. **Manual transport enrichment** — a "Submit Work Package" tool in Claude Desktop's chat that formats and presents work packages for copy-paste to Code.
2. **Dashboard / status tools** — exposing orchestration status, session history, or verification results as resources in chat.
3. **Configuration UI** — using the `user_config` mechanism for orchestration settings (project root, transport preferences, etc.).

They are NOT suitable for:
1. Automated build delegation (that is the Agent SDK's job).
2. Cross-platform review submission (that is Codex/Gemini CLI's job).
3. The core task-transport mechanism.

If a Desktop Extension is built at all, it is a convenience layer on top of the SDK-based orchestration, not the orchestration itself. This is a refinement, not a contradiction of the architecture — the scoping document said "this is the deployment vehicle for the automated MCP transport," and the investigation shows the automated transport goes directly through the SDK, not through an MCP tool server.

---

## Area 4 — Cross-Platform Review Transport

### What was tested

Examined Codex CLI on this machine (installed and authenticated). Researched Gemini CLI capabilities via web search.

### Codex CLI — confirmed working

**Installation:** Installed at `C:\Users\david\AppData\Local\Programs\OpenAI\Codex\bin\codex.exe`.

**Authentication:** `codex login status` reports `Logged in using ChatGPT`. Uses the ChatGPT Plus subscription, not API tokens.

**Non-interactive execution:**

```bash
codex exec "Review this code for security vulnerabilities" \
  --json \
  --output-last-message output.json \
  --output-schema review-schema.json \
  --cd /path/to/project \
  --approve-for-me
```

Key flags:
| Flag | Purpose |
|---|---|
| `--json` | JSONL event stream to stdout |
| `--output-last-message <file>` | Write final agent message to file |
| `--output-schema <file>` | JSON Schema for structured final output |
| `-m <model>` | Select model (e.g., `o3`, `o4-mini`) |
| `--cd <dir>` | Working directory |
| `--approve-for-me` | Automated approval via workspace-write sandbox |
| `--ephemeral` | No session persistence |
| `-s read-only` | Sandbox mode for read-only review |

**Dedicated review mode:**

```bash
codex exec review "Focus on security and performance" \
  --json \
  --output-last-message review.json \
  --output-schema schema.json
```

Reviews against: `--uncommitted` (staged/unstaged/untracked), `--base <branch>` (vs branch), `--commit <SHA>` (specific commit).

**Session resume:**

```bash
codex exec resume --last          # resume most recent
codex exec resume <session-id>    # resume specific session
codex exec fork <session-id>      # fork into new session
```

**Structured output:** The `--output-schema` flag accepts a path to a JSON Schema file. The agent's final response conforms to it. This means the orchestration layer can receive review results in a predictable structure.

### Gemini CLI — deprecated, replaced by Antigravity CLI

Gemini CLI is not installed on this machine. Research uncovered a significant development:

**Deprecation (June 2026):** At Google I/O on May 19, 2026, Google announced consolidation under the **Antigravity** brand. Gemini CLI **stopped serving consumer/free-tier requests on June 18, 2026.** Consumer users were redirected to **Antigravity CLI** (`agy` command). Gemini CLI still works with an API key from Google AI Studio or Vertex AI / service account auth, but consumer subscription auth (Google One AI Premium) is defunct.

**Installation:** `npm install -g @google/gemini-cli` (package: `@google/gemini-cli`, Node.js 20+).

**Non-interactive mode:** `gemini -p "prompt"` for headless execution. Output modes: `--output-format text` (default), `json` (single object at end), `stream-json` (JSONL events).

**Structured output:** JSON output includes `response`, `stats` (tokens, tool calls, files), and `error`. However, there is no `--output-schema` equivalent — no schema-constrained structured output like Codex CLI or the Agent SDK provide.

**Session management:** Sessions auto-save with UUIDs. `gemini --resume <UUID>` or `gemini -r latest`. However, headless mode JSON output **does not currently include the session ID** (GitHub issue #14435, open as of Sept 2026). This is a gap: you cannot capture the session ID from a non-interactive run to resume later.

**Authentication for headless use:** Only `GEMINI_API_KEY` (from AI Studio), Vertex AI service accounts, or Application Default Credentials. Browser OAuth is removed.

### Antigravity CLI (Google successor)

The Gemini CLI successor for consumer users:

- **Command:** `agy`
- **Non-interactive:** `agy -p "prompt"` (same pattern)
- **Permissions:** Tool calls requiring approval are soft-denied by default in headless mode. `--dangerously-skip-permissions` auto-approves. Known issue: headless mode does not consult `permissions.allow` in settings (GitHub issue #548).
- **Maturity:** Early. Known permission bugs in headless mode. Not yet a reliable automation target.

### Capability comparison

| Capability | Codex CLI | Gemini CLI | Antigravity CLI |
|---|---|---|---|
| Non-interactive exec | `codex exec` (mature) | `gemini -p` (works) | `agy -p` (early) |
| Structured output | `--output-schema` (JSON Schema) | `--output-format json` (no schema constraint) | Unknown |
| Dedicated review | `codex exec review` | None | None |
| Session resume (headless) | `codex exec --last` (clean) | `--resume` exists but no session ID in JSON output | Unknown |
| Auth (subscription) | ChatGPT Plus (confirmed) | **Deprecated** (June 2026) | Unknown |
| Auth (API key) | `CODEX_API_KEY` | `GEMINI_API_KEY` | Likely `GEMINI_API_KEY` |
| JSONL streaming | `--json` flag | `--output-format stream-json` | Unknown |
| Working dir control | `--cd <dir>` | Equivalent exists | Likely supported |
| Sandbox modes | read-only / workspace-write / full | `--yolo` / `--approval-mode` | `--dangerously-skip-permissions` |
| Maturity for automation | High | Medium (deprecation risk) | Low |

### Recommended design

**Implement Codex CLI first.** It is installed, authenticated, has structured output via `--output-schema`, and has the cleanest non-interactive path. The dedicated `codex exec review` subcommand maps directly to the cross-platform review use case.

**Gemini CLI is deprecated for consumer use** as of June 2026. The successor is Antigravity CLI (`agy`), which is early and has known issues in headless mode. Neither Gemini CLI nor Antigravity CLI supports schema-constrained output (`--output-schema` equivalent). For Google model access in automation, an API key from Google AI Studio + Gemini CLI would work technically, but the tooling is less mature than Codex CLI. Defer until the Antigravity CLI stabilises or a genuine need for Google model review arises.

**Structured output parsing:** Codex CLI supports schema-constrained output via `--output-schema`. Gemini/Antigravity CLI provides JSON output but without schema enforcement — the orchestration layer would need to parse and validate the response against the schema itself. For the first implementation, Codex CLI's schema support is sufficient; schema validation for other transports can be added when needed.

---

## Area 5 — Work Package Contract

### Design approach

The schemas below are informed by what Areas 1–4 showed is actually available. The key constraints:

1. **Agent SDK `outputFormat`** accepts a JSON Schema and constrains the agent's final response to it. This means the verification response is schema-enforced, not parsed from free text.
2. **Codex CLI `--output-schema`** also accepts a JSON Schema. Same mechanism, different transport.
3. **Copy-paste transport** needs a human-readable representation. Markdown with a YAML/JSON front matter block provides both: the front matter is machine-parseable, the body is human-readable.
4. **Authorship independence** requires that both chat and Code can populate the same fields. No field should be easy to fill from one surface and awkward from the other.

### Work Package Schema (JSON)

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "properties": {
    "package_id": {
      "type": "string",
      "description": "Unique identifier for this work package (UUID or descriptive slug)"
    },
    "created": {
      "type": "string",
      "format": "date-time",
      "description": "ISO 8601 timestamp when the package was created"
    },
    "task_type": {
      "type": "string",
      "enum": ["build", "review", "search", "collaborate"],
      "description": "What kind of work this package requests"
    },
    "tier": {
      "type": "string",
      "enum": ["autonomous", "heavyweight"],
      "description": "autonomous: MCP delivers, Code executes, results return. heavyweight: file-drop, Dave drives interactively"
    },
    "specification": {
      "type": "object",
      "properties": {
        "intent": {
          "type": "string",
          "description": "What needs to change — the specification, not the instructions. Describes the desired outcome, not the steps."
        },
        "context": {
          "type": "string",
          "description": "Background information the agent needs to understand the intent. References to existing files, standards, or decisions."
        },
        "scope": {
          "type": "object",
          "properties": {
            "files": {
              "type": "array",
              "items": { "type": "string" },
              "description": "Files or patterns the work should touch. Empty means agent discovers scope."
            },
            "directories": {
              "type": "array",
              "items": { "type": "string" },
              "description": "Directories the agent should have access to beyond cwd."
            }
          }
        }
      },
      "required": ["intent"]
    },
    "acceptance": {
      "type": "object",
      "properties": {
        "criteria": {
          "type": "array",
          "items": { "type": "string" },
          "description": "What must be true when the work is done — testable statements."
        },
        "objective_checks": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "check": { "type": "string", "enum": ["compile", "test", "lint", "deploy", "custom"] },
              "command": { "type": "string", "description": "Shell command to run (for custom checks)" }
            },
            "required": ["check"]
          },
          "description": "Automated checks the agent should run after making changes."
        }
      }
    },
    "routing": {
      "type": "object",
      "properties": {
        "transport": {
          "type": "string",
          "enum": ["mcp", "copy-paste", "file-drop"],
          "description": "How this package travels. MCP = automated via SDK. copy-paste = manual. file-drop = heavyweight tier."
        },
        "target": {
          "type": "string",
          "enum": ["claude-code", "codex", "gemini", "other"],
          "description": "Which surface executes this work."
        },
        "model": {
          "type": "string",
          "description": "Model hint for the executing agent (e.g., 'claude-opus-5', 'o3')."
        },
        "budget_usd": {
          "type": "number",
          "description": "Maximum cost for this task in USD."
        }
      }
    }
  },
  "required": ["task_type", "tier", "specification"]
}
```

### Verification Response Schema (JSON)

This is the schema passed to `outputFormat` (Agent SDK) or `--output-schema` (Codex CLI) to constrain the agent's response:

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "properties": {
    "status": {
      "type": "string",
      "enum": ["success", "partial", "failed", "blocked"],
      "description": "Overall outcome of the work."
    },
    "summary": {
      "type": "string",
      "description": "One-paragraph description of what was done."
    },
    "files_changed": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "path": { "type": "string" },
          "action": { "type": "string", "enum": ["created", "modified", "deleted", "renamed"] },
          "description": { "type": "string", "description": "What changed in this file and why." }
        },
        "required": ["path", "action"]
      },
      "description": "List of files touched by the work."
    },
    "checks": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "check": { "type": "string" },
          "passed": { "type": "boolean" },
          "output": { "type": "string", "description": "Relevant output from the check (truncated if long)." }
        },
        "required": ["check", "passed"]
      },
      "description": "Results of objective checks (compile, test, lint, deploy)."
    },
    "criteria_met": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "criterion": { "type": "string" },
          "met": { "type": "boolean" },
          "evidence": { "type": "string" }
        },
        "required": ["criterion", "met"]
      },
      "description": "Assessment of each acceptance criterion."
    },
    "questions": {
      "type": "array",
      "items": { "type": "string" },
      "description": "Questions or ambiguities encountered during execution that need human input."
    },
    "blockers": {
      "type": "array",
      "items": { "type": "string" },
      "description": "Issues that prevented completion."
    }
  },
  "required": ["status", "summary", "files_changed"]
}
```

### Transport independence test

**JSON transport (MCP / SDK):** The work package is a JSON object. The specification's `intent` field is the prompt passed to `query()`. The verification response schema is passed as `outputFormat`. Lossless.

**Markdown transport (copy-paste):** The work package renders as:

```markdown
---
task_type: build
tier: autonomous
---

## Intent

Deploy the Principles FUP: update Principles_Design to v4 and
Principles_Decisions to v4, superseding the v3 files.

## Context

The FUP zip is at `_fileupdatepackages/Principles_2026-09-08.zip`.
The FUP deployer tool is at `_tools/file_update_package.py`.

## Acceptance criteria

- [ ] Principles_Design_v4.md exists at Principles/
- [ ] Principles_Decisions_v4.md exists at Principles/
- [ ] v3 files moved to _superseded
- [ ] Binder builder runs successfully after deploy

## Objective checks

- deploy: `python _tools/file_update_package.py`
```

This is readable, pasteable, and parseable (YAML front matter + structured body). The same fields are present in both representations.

**Authorship independence test:** Both surfaces can populate all fields naturally. In chat, the user describes the intent in natural language and Claude structures it. In Code, the user or agent populates the JSON directly. The `intent` field is natural language in both cases — it is the specification, not implementation instructions.

### Example: FUP validation scenario

```json
{
  "package_id": "fup-principles-2026-09-08",
  "created": "2026-09-15T14:00:00Z",
  "task_type": "build",
  "tier": "autonomous",
  "specification": {
    "intent": "Deploy the Principles FileUpdatePackage. The FUP at _fileupdatepackages/Principles_2026-09-08.zip contains updated Principles_Design_v4.md and Principles_Decisions_v4.md. Run the FUP deployer tool to deploy these files into the documentation tree, superseding the v3 versions.",
    "context": "The FUP deployer is a Python script at _tools/file_update_package.py. It reads _manifest.json from the zip, deploys files to their target paths, moves replaced files to _superseded folders, and triggers the binder builder. The documentation root is the parent of _tools/.",
    "scope": {
      "files": [
        "_fileupdatepackages/Principles_2026-09-08.zip",
        "_tools/file_update_package.py",
        "_tools/file_update_package_settings.json"
      ],
      "directories": [
        "Principles/"
      ]
    }
  },
  "acceptance": {
    "criteria": [
      "Principles/Principles_Design_v4.md exists and matches the zip content",
      "Principles/Principles_Decisions_v4.md exists and matches the zip content",
      "Previous v3 files are in Principles/_superseded/",
      "FUP deployer reports DEPLOYED (not CONFLICT or ERROR)",
      "The processed zip is moved to _fileupdatepackages/_superseded/"
    ],
    "objective_checks": [
      { "check": "custom", "command": "python _tools/file_update_package.py" }
    ]
  },
  "routing": {
    "transport": "mcp",
    "target": "claude-code",
    "budget_usd": 2.00
  }
}
```

### Heavyweight tier — file-drop convention

For Tier 2 (heavyweight), the work package is a file placed in the repo:

- **Location:** `_workpackages/` at the documentation root (or project root)
- **Filename:** `{package_id}.workpackage.md` (or `.json`)
- **Discovery:** Code scans `_workpackages/` for files matching the pattern. No automated file-watch — Dave points Code at the file manually (per clarification C2, this is the right first step).

The heavyweight tier uses the same schema as the autonomous tier but with `tier: "heavyweight"` and `transport: "file-drop"`. The file contains the full work package. Dave opens Code in the project directory and instructs it to process the work package.

---

## What Was Hard

### Area 1 — Easier than expected
The Agent SDK's API is clean and well-documented. The `query()` → async generator pattern maps directly to the orchestration architecture. The structured output via `outputFormat` eliminates the need for response parsing. The scoping document's architecture is confirmed almost exactly as assumed.

### Area 2 — Billing pool opacity
There is no programmatic "which pool am I using" check. The distinction between subscription quota, SDK credit pool, and API billing is documented but not queryable at runtime. Cost tracking is available via `total_cost_usd` in response metadata, but this is a client-side estimate. The recommendation is to monitor via the Anthropic usage dashboard and set `maxBudgetUsd` as a per-task safety net.

### Area 3 — Architectural mismatch
This was the biggest surprise. The scoping document assumed Desktop Extensions were "the deployment vehicle for the automated MCP transport." The investigation shows they are MCP tool servers — they give chat new tools, but cannot invoke Code's agent loop. The core delegation mechanism is the Agent SDK (or CLI subprocess), not an extension. This is not a flaw in the architecture — it is a refinement. The extension packaging is still useful for manual-transport enrichment, but the automated transport bypasses it entirely.

### Area 4 — Gemini CLI deprecated
Codex CLI is mature and well-suited. Gemini CLI has been deprecated for consumer users (June 2026) and its successor Antigravity CLI has known issues in headless mode. Neither supports schema-constrained output. The scoping document's plan to "add Gemini and potentially others" is architecturally sound (transport-independent work packages mean adding transports is additive), but the Google CLI ecosystem is in flux. The transport-independent architecture means this is not blocking — Codex CLI covers the cross-platform review case, and Google model access can be added when the tooling stabilises.

---

## Recommended Architecture (revised from findings)

The findings confirm the scoping document's architecture with one structural correction:

### What the scoping document got right

1. **Task creation separate from transport** — confirmed. The work package schema is transport-independent.
2. **Intent-level delegation** — confirmed. The Agent SDK's `query()` accepts specification-level prompts.
3. **Structured verification** — confirmed. `outputFormat` with JSON Schema constrains agent responses.
4. **Two tiers** — confirmed. Autonomous via SDK, heavyweight via file-drop.
5. **Cross-platform review via CLI** — confirmed. Codex CLI `exec` with `--output-schema`.
6. **Stateless first** — confirmed as the right call. No penalty in deferring multi-turn.

### What the scoping document assumed incorrectly

1. **Desktop Extensions as the deployment vehicle** — incorrect for the core transport. Extensions are passive tool servers. The Agent SDK IS the transport mechanism. A Desktop Extension could wrap a "submit work package" tool for manual-transport convenience, but the automated path goes SDK → agent loop directly.

### Revised component architecture

```
┌──────────────────────────────────────────────────────┐
│ Chat (Claude Desktop / claude.ai)                     │
│                                                       │
│  Work package authored here (or in Code)              │
│  Routing heuristic decides: stay in chat or delegate  │
└───────────┬───────────────────────────┬───────────────┘
            │ Automated (SDK)           │ Manual (copy-paste)
            ▼                           ▼
┌───────────────────────┐   ┌───────────────────────────┐
│ Agent SDK invocation   │   │ claude -p with work       │
│                        │   │ package as prompt          │
│ query({                │   │                            │
│   prompt: intent,      │   │ --output-format json       │
│   options: {           │   │ --json-schema <response>   │
│     outputFormat:      │   │ --allowedTools "..."       │
│       responseSchema,  │   │ --permission-mode ...      │
│     allowedTools,      │   │                            │
│     maxBudgetUsd,      │   │                            │
│     cwd: projectRoot   │   │                            │
│   }                    │   │                            │
│ })                     │   │                            │
└───────────┬────────────┘   └─────────────┬─────────────┘
            │                               │
            ▼                               ▼
┌──────────────────────────────────────────────────────┐
│ Claude Code agent loop                                │
│                                                       │
│ Owns: file discovery, edit planning, execution        │
│ Tools: Read, Write, Edit, Bash, Glob, Grep            │
│ Returns: structured verification response             │
└───────────┬───────────────────────────────────────────┘
            │
            ▼
┌──────────────────────────────────────────────────────┐
│ Verification response (schema-constrained)            │
│                                                       │
│ { status, summary, files_changed, checks,             │
│   criteria_met, questions, blockers }                  │
└──────────────────────────────────────────────────────┘
```

For cross-platform review:

```
┌──────────────────────────────────────────────────────┐
│ Orchestration layer                                   │
│                                                       │
│ Work package with task_type: "review"                 │
│ routing.target: "codex" or "gemini"                   │
└───────────┬───────────────────────────┬───────────────┘
            │                           │
            ▼                           ▼
   codex exec "prompt"          gemini -p "prompt"
   --output-schema schema       --json
   --json                       (structured output TBD)
   --output-last-message out
            │                           │
            ▼                           ▼
┌──────────────────────────────────────────────────────┐
│ Review response (parsed into verification schema)     │
└──────────────────────────────────────────────────────┘
```

---

## Open Questions

These are design decisions the investigation surfaced but could not resolve.

### O1. Orchestration layer location

Where does the orchestration code live — in Code (a skill/plugin), in a standalone Node.js script, or in a Desktop Extension's MCP server? The investigation showed the SDK is the invocation mechanism, but the orchestration logic (reading work packages, invoking the SDK, routing to Codex/Gemini, collecting responses) needs a home. Options:

- **A Claude Code skill** that reads work packages and invokes the SDK (recursive: Code invoking Code)
- **A standalone script** (Node.js/Python) that orchestrates from outside
- **A Desktop Extension MCP server** that exposes orchestration tools to chat (chat-driven orchestration)

Each has tradeoffs. The standalone script is simplest. The skill integrates tightest with Code's existing infrastructure. The extension gives chat control but adds the indirection layer the investigation showed is unnecessary for the core transport.

### O2. When to use `outputFormat` vs post-hoc parsing

The Agent SDK's `outputFormat` constrains the agent's FINAL response to a JSON Schema. But the agent may produce multiple assistant messages during execution (reasoning, tool calls, intermediate results). The verification response schema applies only to the final output. If intermediate status reporting is needed (e.g., "working on file 3 of 5"), that comes from the message stream, not from `outputFormat`. Is intermediate status needed for the autonomous tier?

### O3. FUP deployer invocation strategy

For the FUP validation scenario, should the work package tell the agent to run the Python deployer (`python _tools/file_update_package.py`), or should it tell the agent to perform the deployment itself (read the manifest, copy files, move superseded versions)? The deployer tool is the proven mechanism and provides its own verification (completion summary, event log). But it runs as a GUI-oriented script (holds the window open, waits for user input). The agent would need to handle its interactive prompts or the tool would need a `--batch` mode.

---

## Batched Questions for Dave

### Q1. SDK credit pool status (Area 2, blocking: none)

The Max 5x plan includes a $100/month SDK credit pool for API-key-authenticated calls. Is this currently active on your account? Check at `console.anthropic.com` → Billing → Usage. If it is active, API-key-authenticated invocations (bare mode, CI pipelines) draw from this pool before incurring pay-as-you-go charges. If not active, all API-key usage is pay-as-you-go.

**Why it matters:** For personal use (non-bare mode), the subscription quota applies regardless. The SDK credit pool matters only if you also need API-key-authenticated invocations (e.g., CI/CD pipelines, or `--bare` mode for deterministic builds).

### Q2. Desktop Extension role (Area 3, blocking: none)

The investigation found that Desktop Extensions cannot invoke Claude Code's agent loop — they are passive MCP tool servers. The automated transport goes through the Agent SDK directly. Do you still want a Desktop Extension as a convenience layer for the manual transport (a "Submit Work Package" tool in chat), or is the copy-paste path sufficient for now?

**Recommendation:** Defer the extension. The SDK transport is the primary path; the copy-paste path covers the manual case. An extension adds value only when the manual path becomes frequent enough to justify the packaging overhead.

### Q3. Orchestration layer home (Open question O1, blocking: design pass)

Where should the orchestration code live? The three options are: a standalone Node.js script, a Claude Code skill, or a Desktop Extension MCP server. The investigation provides enough information to choose, but the choice shapes the design.

**Recommendation:** Start with a standalone Node.js script. It is the simplest, most testable, and least coupled option. It can be evolved into a skill or extension later if the integration benefits justify it.

### Q4. FUP deployer batch mode (Area 5 / validation scenario, blocking: prototype)

The FUP deployer tool (`file_update_package.py`) is interactive — it holds the window open and may prompt for user instructions. For the autonomous tier, the agent needs to run it non-interactively. Options:
- Add a `--batch` or `--non-interactive` flag to the deployer
- Have the agent pipe input to handle any prompts
- Have the agent perform the deployment itself (bypassing the tool)

**Recommendation:** Add a `--batch` flag to the deployer. It is a small change to an existing tool, preserves the proven deployment logic, and makes the tool usable from both interactive and automated contexts.

### Q5. Work package naming (clarification C4, blocking: none)

The scoping document notes a pending rename from "work package" to "build package" for the build-side artefact. The schemas above use "work package" throughout. The orchestration artefact is a transport envelope — neither "work package" nor "build package" is quite right. "Task package" or "dispatch" might be more accurate. Settle the naming before the schemas harden.

### Q6. "Code's scan command" (clarification C2, confirmation)

The investigation treated the heavyweight file-drop as a manual step (Dave points Code at the file). This is the right first approach. If you had something specific in mind by "Code's scan command" — an existing feature or planned capability — let me know and I'll adjust. The file-drop path works without automation: place the file, tell Code to process it.

### Q7. Subscription auth for distributed use (Area 2, forward-looking)

The Agent SDK's restriction on subscription auth is a policy against third-party distribution, not a technical block. For personal use, subscription auth works. But if AIDE is ever distributed to other users (e.g., as a product or template), each user would need their own API key or subscription. Is distribution a future consideration, or is AIDE always personal?

**Why it matters:** If always personal, subscription auth (non-bare mode) is the right default. If distribution is possible, the orchestration layer should be designed to accept API keys from the start, even if you personally use subscription auth.

---

## Summary

| Area | Scoping assumption | Finding | Status |
|---|---|---|---|
| 1. Agent SDK | Intent-level delegation via SDK wrapper | Confirmed — `query()` with `outputFormat` is exactly this | ✓ Confirmed |
| 2. Auth | OAuth against Max subscription | Works in non-bare mode via keychain. API key for bare mode. | ✓ Confirmed with nuance |
| 3. Desktop Extensions | Deployment vehicle for automated transport | Wrong mechanism — extensions are passive tool servers, not orchestrators | ✗ Corrected |
| 4. Cross-platform CLIs | Codex/Gemini for non-interactive review | Codex confirmed. Gemini deprecated for consumer auth (June 2026); successor Antigravity CLI is early. | ✓ Codex confirmed; Gemini deferred |
| 5. Work package | Transport-independent, authorship-independent contract | Draft schemas designed and tested against FUP scenario | ✓ Designed |

The architecture is sound. The one structural correction — Desktop Extensions serving a different role than originally scoped — is a refinement, not a redesign. The Agent SDK provides exactly the intent-level delegation the architecture assumed, with better structured output support than expected.
