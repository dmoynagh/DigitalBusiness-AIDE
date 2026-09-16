# AIDE Orchestration — Design v1 (DRAFT — for review)

Status: proposed, not deployed. Awaiting Dave's read-through and decision batch before
this becomes an accepted design. Cross-review not yet run.

Input: `AIDE_Orchestration_WIP_v1.md` (original scoping), the Claude Code investigation
findings (2026-09-15), and a design-shaping pass done in another AI session (2026-09-15,
reconciled below). The investigation is treated as technical evidence; the design-shaping
pass is treated as the model correction that resolves it against AIDE's component
boundaries.

Dependency note: the work queue places Orchestration after Build. Build has not yet had
its design pass. This design does not depend on Build's internal structure — it treats
anything Build hands it as opaque, caller-owned payload — so it can proceed, but the gap
is worth naming rather than stepping over silently.

---

## Purpose

Orchestration coordinates execution across AI surfaces and platforms. It moves work
that another component already owns — its intent, its acceptance criteria, its
verification policy — to an execution target capable of doing it, and brings the result
back. It owns the crossing, not the work.

## Objectives

- **O1 — Cross-platform reach.** Let work defined in one AI surface (chat, Code) be
  carried out on another (Claude Code's agent loop, Codex, other platforms) without the
  originating surface needing to know the target's native invocation mechanics.
- **O2 — Strict ownership boundary.** Never absorb task semantics, verification policy,
  or response meaning from the components that use it. Orchestration is a Delivery-role
  component; the Work-role components it serves keep authority over what "done" means.
- **O3 — Reduce burden.** Delegating build and review work to Code and to external AI
  reduces Dave's manual load as AIDE matures, in proportion to what's actually delegated
  — not by building capacity ahead of demonstrated use.
- **O4 — Evidence over assumption.** Design choices here are grounded in what was
  actually tested (Agent SDK, Codex CLI), not in what documentation implied should work.

## Charter alignment

Serves the cross-platform applicability objective directly (O7 in Core Charter terms),
contributes to trust and integrity (transport-level outcomes are honestly distinguished
from task outcomes, so nothing is silently claimed as done that only completed transport),
and to reduce-burden. The Charter's development principles govern throughout: build the
smallest thing the objective demonstrably needs; do not add apparatus a principle didn't
ask for; difficulty in implementation is a signal about the model, not a cue for
cleverness.

---

## Model and approach

### Central model — dispatch, not orchestration-of-work

Orchestration does not describe or own the work being performed. It takes work already
defined by its caller (the owning component or the human), dispatches it to an
execution target through an adapter, and returns the result.

```
caller-owned work
      │
      ▼
Orchestration (dispatch, adapter selection, invocation, correlation)
      │
      ▼
target adapter
      │
      ▼
execution target (Claude Code / Codex / other)
      │
      ▼
result
      │
      ▼
Orchestration
      │
      ▼
caller
```

The caller retains ownership of: task semantics, specification/intent, acceptance
criteria, work-package or build-package structure, verification policy, and the semantic
meaning of the returned result.

### What Orchestration owns

Dispatch; invocation; transport/channel selection; target adapters; target-specific
invocation mechanics; model-capability-level resolution; execution-endpoint interaction;
correlation; transport/invocation failure; returning the recipient's result to the
caller.

### What Orchestration explicitly does not own

Work-package structure; Build packages or other workflow artefacts; task types/work
modes; verification policy; acceptance criteria; review semantics; Build's return
semantics; generic response semantics; human/autonomy policy; model-capability-mapping
*content* (owned by Core, see Resources below — Orchestration consumes it, doesn't own
it).

This narrows the wording currently carried in Core, which assigns Orchestration
ownership of "work package structure, verification, and capability profiles." That
wording needs correcting as part of accepting this design — flagged as a decision
against Core, not silently absorbed here.

### Dispatch, not Work Package

The original scoping and the investigation both reached for a universal Work Package
with a mandatory Verification Response shape. Under the ownership boundary above, that
would make Orchestration own task semantics — which it explicitly must not. A dispatch
is the thinner artefact that respects the boundary:

```yaml
dispatch_id: ...
target: claude-code
workspace: C:/dev/repos/example
model:
  level: high
payload: ...
```

`payload` is opaque to Orchestration. It may be a Build handoff, a review request, a
structured message, a plain instruction, or any other caller-owned artefact.

### `workspace`

The immediate requirement is the repository/project location the target should act on
— the value that becomes `cwd`, `--cd`, or the equivalent on the target side. A single
string field, not a broader execution-context object. A richer execution-context
abstraction is only introduced if multiple genuinely related properties demonstrate the
need (per the apparatus-avoidance principle) — not speculatively.

### Response handling

No universal Verification Response. Different callers own different return semantics —
Build, review, and other external-AI interactions may need materially different
response shapes. Orchestration returns the target's response to the caller without
redefining what success means.

**Transport outcome and task outcome are kept distinct:**

```yaml
dispatch_id: ...
target: claude-code
transport_status: completed
response: ...
```

`transport_status: completed` means the invocation completed and returned a response.
It does not mean the requested task succeeded — that judgement belongs to whichever
component owns the work.

### `response_schema` as adapter capability, not contract

The Claude Agent SDK's `outputFormat` and Codex's `--output-schema` both support
schema-constrained final output — this was confirmed technically by the investigation.
It is not, on that account, an Orchestration objective. Structured output is a useful
capability some adapters expose; if a caller owns a response contract and wants it
enforced, Orchestration may pass that contract through to a target that supports it.
It is never a mandatory part of the Orchestration contract itself.

### Model capability selection

The caller — human or AI — decides the required capability level; Orchestration does
not run a classifier to infer it. Automatic model-selection is parked, not designed.

A small, provider-independent vocabulary is used:

```
basic | standard | high | maximum
```

```yaml
model:
  level: high
```

An escape hatch allows requesting an exact provider model directly, for testing,
comparison, or reproduction:

```yaml
model:
  exact: provider-specific-model
```

`level` and `exact` are normally mutually exclusive.

### Model-level resolution

Orchestration maps a logical level to target-specific invocation settings — which may
involve more than model identity (reasoning effort, execution mode, other
provider-specific parameters). Two logical levels may legitimately resolve to the same
native configuration where a provider doesn't currently expose a meaningful distinction.
**The mapping content itself is not owned by Orchestration — see Framework Resources,
below.**

Execution results should retain the requested level, the resolved provider model, the
resolved execution settings, and the resource/profile version used — so a past
execution stays interpretable even after mappings later change.

---

## Framework Resources — a Core dependency, not an Orchestration artefact

This model-mapping need exposed a pattern broader than Orchestration: the distinction
between AIDE's durable behaviour/model and the volatile current knowledge that behaviour
consumes (current platform list, current model-capability mappings, current defaults).

**This belongs to Core, as a cross-cutting framework pattern — confirmed in this
session's review, not decided here.** Orchestration is a consumer of Framework
Resources, not its owner. This design records the dependency and the shape of what
Orchestration needs from it; the Resources mechanism itself (naming, deployment cadence,
contract) is Core's design pass to run, separately, and is out of scope for Orchestration
v1.

What Orchestration needs Resources to provide, indicatively:

```yaml
orchestration:
  platforms:
    claude-code:
      defaultModelLevel: standard
      models: { basic: ..., standard: ..., high: ..., maximum: ... }
    codex:
      defaultModelLevel: standard
      models:
        basic: { model: ..., reasoningEffort: low }
        standard: { model: ..., reasoningEffort: medium }
        high: { model: ..., reasoningEffort: high }
        maximum: { model: ..., reasoningEffort: ... }
```

The actual schema is Core's to settle, kept as small as demonstrated need allows.

**Settings vs Resources (also a Core-level distinction, noted here because
Orchestration is a consumer of both):** Resources describe the default/current AIDE
world (which platforms are supported); a portable user setting customises it for one
person (e.g. `disabledOrchestrationPlatforms: [Gemini]`). Not critical to Orchestration
v1 — noted so the boundary isn't invented ad hoc later inside Orchestration.

---

## Machine and execution-endpoint availability

### Detection before configuration

Availability of an execution target should normally be discovered, not configured. A
local AIDE execution endpoint can determine whether `claude` exists, whether `codex`
exists, whether required runtimes are installed, and whether auth appears usable.
Effective availability is:

```
supported by Resources ∩ detected on this endpoint ∩ not explicitly disabled
```

Machine-specific configuration is only introduced where detection genuinely cannot
represent a real requirement — not to describe facts that discovery already gives.

### Capability availability is not execution-endpoint availability

An AI session having the Orchestration capability does not imply it has access to a
local execution endpoint. A web-only chat session may have none; one machine may have
Claude Code and Codex both available, another only Claude Code. The execution endpoint
exposes its own effective target list; the calling session queries it rather than
inferring the environment itself:

```yaml
endpoint: david-laptop
targets:
  claude-code: { available: true }
  codex: { available: true }
  gemini: { available: false, reason: disabled }
```

Orchestration does not depend on a chat session discovering machine hostname,
desktop-vs-web mode, installed executables, or environment variables directly. Where
local machine state matters, the local AIDE runtime/endpoint is authoritative for it.

### Local execution endpoint

The local MCP/CLI bridge is an execution endpoint, not the Orchestration design itself.
A future remote endpoint reachable from web-hosted sessions is conceivable but
introduces networking, authentication, and security concerns well beyond v1's scope —
explicitly deferred, not designed against.

---

## Implementation home

Orchestration's dispatch mechanism lives in a **local MCP server, delivered as a
marketplace plugin** — not inside the `aide` CLI as originally proposed.

This follows the broader direction confirmed by empirical testing on 2026-09-16: AIDE
functionality is delivered via marketplace plugins that bundle local MCP servers. The
delivery model itself belongs to Infrastructure, not Orchestration — Orchestration is
the first consumer, not the owner, and the same model applies to binder, FUP, and
future tooling.

Orchestration owns the dispatch behaviour, adapters, model-level resolution, and
invocation semantics inside the MCP server. Infrastructure owns how that server gets
packaged, distributed, updated, and made available across surfaces.

### Surface coverage (tested, all three confirmed)

| Surface | Mechanism | Server file |
|---|---|---|
| Code | Marketplace plugin `.mcp.json` | Marketplace clone |
| Cowork | Marketplace plugin `.mcp.json` | Marketplace clone |
| Chat | `claude_desktop_config.json` entry | Same file in marketplace clone |

All three surfaces read the same physical server file. The `claude_desktop_config.json`
entry for Chat is a one-time bootstrap that points at the marketplace clone's server
path. Plugin updates (merged PR → clone refresh → restart) propagate to all three
surfaces automatically — no rebuild, no reinstall.

Chat's requirement for a separate config entry is due to a current Claude Desktop
platform bug (plugin-delivered `.mcp.json` tools don't reliably reach the Chat model,
despite Anthropic's documentation saying they should). Multiple independent
reproductions exist. When Anthropic fixes this, the config entry becomes redundant and
can be removed — a removal, not a rework. See Infrastructure's MCP delivery model
documentation for the full tested methodology and known platform issues.

### What was superseded

The original investigation considered three options: standalone script, Claude Code
skill, or Desktop Extension. The design-shaping pass selected `aide dispatch` inside
the CLI as a fourth option. The plugin-delivered MCP server supersedes all four —
it avoids standing up new infrastructure, integrates with the existing marketplace
update path, and reaches all three surfaces from a single server codebase.

## Target adapters

First implementation stays small: `claude-code` and `codex`. An adapter converts stable
dispatch semantics into native invocation details — e.g. for Codex, `model.level: high`
resolves via current Resources to a native model plus `reasoning_effort: high`, then
invokes `codex exec`.

Gemini/Google support is additive, added when there's a sufficiently stable execution
path — not required to block the first implementation. (The investigation found Gemini
CLI's consumer/subscription auth path discontinued in June 2026, replaced by the early
and less mature Antigravity CLI — this is a live reason for deferring rather than an
arbitrary one.)

## Statelessness

Each dispatch is independently executable. Provider session IDs may be preserved as
returned metadata where useful, but no AIDE session-management abstraction is built
until a demonstrated workflow requires one. This was the investigation's own
stateless-first position and is carried forward unchanged.

## Intermediate progress

No semantic progress protocol in v1. Provider event streams may be surfaced or logged
opportunistically; the stable contract only needs to distinguish transport completion
from transport failure. A richer progress model is added only if real usage demonstrates
the need.

---

## FUP validation scenario

Still the end-to-end transport test:

```
caller supplies work → Orchestration dispatches to Claude Code
    → Claude Code runs `aide fup` → result returns
```

Exercises invocation, authentication, workspace passing, local tooling, execution,
correlation, and return handling — the whole transport, without needing to prove
anything about sophisticated build delegation at the same time.

Do not reproduce FUP deployment logic inside Orchestration or inside the invoked agent.
Use the existing `aide fup` unchanged. The investigation's proposed `--batch` flag for
non-interactive deployment is not assumed necessary — current `aide fup` behaviour
already avoids interactive waiting when no interactive console is present. Test the
actual orchestrated invocation first; only change `aide fup` if a real failure
demonstrates the need. This is the apparatus-avoidance principle applied directly: don't
build the accommodation before the evidence that it's needed.

## Messaging boundary

Orchestration does not define a second generic messaging envelope. Messaging already
owns structured communication and correlation semantics for cross-boundary
communication. Where work needs to cross as structured text, Messaging's envelope
carries the caller-owned request; Orchestration owns moving and invoking it. For direct
programmatic execution, a dispatch is passed directly — no Markdown work-package doctype
is invented to duplicate what Messaging already does.

---

## Two boundary confirmations carried forward from the design-shaping pass

These were open in the original scoping and are treated as settled by this design,
named explicitly per AIDE's own discipline (commit within the model; only surface a fork
that genuinely isn't settled and materially shapes the design):

- **Tier (autonomous vs heavyweight) is caller-owned, not Orchestration-owned.**
  Orchestration dispatches; whether the surrounding workflow is autonomous or
  Dave-driven-interactive is a property of the caller's process, not something
  Orchestration decides or tracks. Risk-flagged external review for heavyweight work is
  the caller's workflow calling Orchestration twice (plan review, build review), not a
  special Orchestration mode.
- **Routing (which tasks even get delegated, and to what threshold) is caller-owned.**
  The original scoping had Orchestration holding a crude size/complexity threshold.
  Under the narrowed ownership, the caller decides the target explicitly
  (`dispatch.target: claude-code`). Orchestration doesn't run a router; it executes the
  caller's routing decision.

---

## Proposed Core boundary wording (for Core's design pass, not adopted here)

> **Orchestration — Coordinate execution across AI surfaces and platforms. Own
> invocation, dispatch, transport/channel routing, execution-target adapters,
> model-level resolution, correlation, and transport-level outcomes. Carry work defined
> by other components without redefining its task, verification, or response
> semantics.**

This replaces the current Core wording that assigns Orchestration ownership of "work
package structure, verification, and capability profiles" — that phrase needs to be
corrected as a Core decision, tracked here as a dependency, not applied by this document.

---

## Deferred — not solved in this design, per demonstrated-requirement discipline

1. Final naming of model capability levels (`basic/standard/high/maximum` proposed).
2. Framework Resources schema and deployment mechanism — Core's design pass.
3. Portable user/account settings mechanism and deployment.
4. Any genuine machine-specific settings beyond environment discovery.
5. Remote execution endpoints reachable from web-hosted sessions.
6. Stateful/multi-turn orchestration.
7. A semantic intermediate-progress protocol.
8. Broader Google/Gemini execution support.
9. Additional target-capability metadata beyond what the first two adapters demonstrate.

---

## Short-form model

> Orchestration moves caller-owned work to another AI execution target and brings the
> result back. The caller chooses the target and required logical model capability.
> Orchestration resolves that request through current Framework Resources into
> target-native invocation settings and executes it through an available endpoint.
> Orchestration owns the crossing, not the work, its verification policy, or the
> semantic meaning of the response.
