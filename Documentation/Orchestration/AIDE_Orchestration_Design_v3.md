# AIDE Orchestration — Design v3

> identity: Orchestration_Design@v3 | doctype: design | updated: 2026-09-17

Two cross-review rounds completed (independent AI). Round 1: fifteen findings (F1–F15),
all resolved in v2 (D20–D34). Round 2: seven findings (R2-F1–R2-F7), all resolved in
v3 (D35–D41). Reviewer accepted the model; remaining work was contract tightening.

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

Serves the Charter's cross-platform applicability objective (O7) directly — one
coordinated dispatch model rather than platform-specific ad hoc mechanisms. Contributes
to trust and integrity (O1) by cleanly separating transport success from caller-owned
task success, so nothing is silently claimed as done that only completed transport.
Supports reduced human burden (O6) by replacing manual handoff with automated dispatch.
Serves coordinated framework (O2) by providing a single mechanism rather than
accumulating per-target patterns. Consistent with extensibility from learning (O4) and
the facilitation objective (O5) — no speculative machinery, no unnecessary caller
friction.

The Principles component's apparatus-avoidance premise and the difficulty-as-evidence
premise govern throughout: build the smallest thing the objective demonstrably needs;
difficulty in implementation is a signal about the model, not a cue for cleverness.
These are Principles premises, not Charter statements — the Charter provides the
objectives they serve.

---

## Model and approach

### Central model — dispatch, not orchestration-of-work

Orchestration does not describe or own the work being performed. It takes work already
defined by its caller (the owning component or the human), dispatches it to an
execution target through an adapter, and returns the result.

```
caller-owned dispatch request
      │
      ▼
Orchestration (accept, assign dispatch_id, adapter selection, invocation, dispatch correlation)
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

Dispatch acceptance and dispatch_id creation; invocation; target-native invocation
mechanics; target adapters; model-capability-level resolution; execution-endpoint
interaction; dispatch correlation (tying a dispatch_id to its transport result);
transport/invocation failure; returning the target's result to the caller.

Orchestration owns **dispatch correlation** — the lifecycle of `dispatch_id`, created by
Orchestration when it accepts a dispatch request and echoed in every transport outcome.
This is distinct from **message/thread correlation**, which is owned by Messaging.

### What Orchestration explicitly does not own

Work-package structure; Build packages or other workflow artefacts; task types/work
modes; verification policy; acceptance criteria; review semantics; Build's return
semantics; generic response semantics; human/autonomy policy; model-capability-mapping
*content* (owned by Core — Orchestration consumes it, doesn't own it); the
routing/target-selection decision (caller-owned); message/thread correlation
(Messaging-owned).

This narrows the wording currently carried in Core, which assigns Orchestration
ownership of "work package structure, verification, and capability profiles." That
wording needs correcting as part of accepting this design — flagged as a decision
against Core, not silently absorbed here.

### The dispatch request and the dispatch

The caller sends a **dispatch request** — the fields the caller owns and provides.
Orchestration accepts the request, creates a `dispatch_id`, and produces the
**dispatch** — the accepted request plus the Orchestration-generated identifier that
correlates it with its transport result.

**Dispatch request** (what the caller sends):

```yaml
target: claude-code         # required — caller-selected
payload: "..."              # required — UTF-8 text, caller-owned
workspace: /path/to/repo    # optional — see omission rules below
model:                      # optional — see omission rules below
  level: high               #   OR exact: provider-specific-model (mutually exclusive)
response_schema: { ... }    # optional — see invocation-capability rules below
```

**Dispatch** (what Orchestration creates from the request):

```yaml
dispatch_id: abc-123        # created by Orchestration
target: claude-code
payload: "..."
workspace: /path/to/repo
model:
  level: high
response_schema: { ... }
```

`dispatch_id` never appears in the caller's request. It is Orchestration's contribution
and the key for dispatch correlation.

**Field semantics:**

- **`target`** — Required. The caller's explicit routing decision (D17). Orchestration
  executes it; it does not make or override it. Must be a currently available target
  (see endpoint operations below).
- **`payload`** — Required. A UTF-8 text value. Orchestration does not interpret it.
  Callers serialise their own artefacts (Build packages, review prompts, Messaging
  envelopes) into this text. Richer payload representations (structured objects, file
  references) are added only when a demonstrated use case requires them.
- **`workspace`** — Optional. The repository/project location passed to the target as
  `cwd`, `--cd`, or equivalent. Omit for dispatches that don't operate against a
  specific location (e.g. cross-platform review with the prompt self-contained in
  payload). If the target/adapter requires a workspace and none was supplied, the
  dispatch fails before execution — Orchestration does not fall back to an unspecified
  native working directory.
- **`model`** — Optional. When provided, `level` and `exact` are mutually exclusive.
  When omitted, the target's default logical level from Framework Resources is used.
  The caller is still the owner of the selection — omission is an explicit delegation
  to the configured default, not a transfer of authority.
- **`response_schema`** — Optional. A caller-supplied schema requesting
  schema-constrained output from the target. If the selected adapter supports
  schema-constrained invocation (Agent SDK `outputFormat`, Codex `--output-schema`),
  the schema is passed through. If the adapter does not support it, the dispatch
  **fails before invocation** with category `unsupported_capability` — Orchestration
  does not silently degrade to unconstrained invocation. The caller can retry without
  the schema if they want unconstrained output.

### The transport result contract

Every dispatch produces a transport result, keyed by the `dispatch_id` Orchestration
created:

```yaml
# Success — target returned a response
dispatch_id: abc-123
target: claude-code
transport_status: completed
provenance:
  requested_model: { level: high }
  resolved_model: claude-sonnet-4-20260514
  resolved_settings: { reasoningEffort: high }
  resources_version: "2026-09-17"
response: "..."

# Success — exact model path (no Resources resolution)
dispatch_id: def-456
target: codex
transport_status: completed
provenance:
  requested_model: { exact: o3 }
  resolved_model: o3
  resolved_settings: { reasoningEffort: high }
  resources_version: null
response: "..."

# Failure — target did not return a response
dispatch_id: ghi-789
target: codex
transport_status: failed
failure:
  category: timeout
  detail: "Codex exec did not return within 300s"
```

**`transport_status`** is either `completed` or `failed`:

- **`completed`** means the invocation reached the target, the target executed, and a
  response was returned. It does **not** mean the requested task succeeded — that
  judgement belongs to whichever component owns the work.
- **`failed`** means no target response was obtained. The `failure` object carries a
  category and human-readable detail.

**Failure categories** (transport-owned — they describe what went wrong in invocation,
not whether the task's objectives were met):

- `invocation_error` — the adapter could not start the target process
- `timeout` — invocation started but did not return within the allowed time
- `target_unavailable` — the target is not currently available on this endpoint
- `auth_failure` — authentication/authorisation failed for the target
- `adapter_error` — the adapter encountered an internal error
- `unsupported_capability` — an explicitly requested invocation capability (e.g.
  `response_schema`) cannot be honoured by the selected adapter

The boundary: if the target's agent loop ran and returned output saying "I could not
complete this task," that is `transport_status: completed` with the target's response.
Transport failure means the target was never successfully reached or did not return.

**Provenance** is required on `completed` results. It records:

- **`requested_model`** — the caller's model selection, represented symmetrically:
  `{ level: high }` for logical-level requests, `{ exact: provider-model }` for exact
  requests. Matches the form the caller used.
- **`resolved_model`** — the native model identity actually used.
- **`resolved_settings`** — the native invocation settings applied (reasoning effort,
  etc.).
- **`resources_version`** — the Framework Resources version used for resolution. `null`
  for the exact-model path, which bypasses Resources resolution — the adapter uses the
  exact model directly, recording the native settings it applied.

Provenance ensures past executions stay interpretable after mappings change.

### Model capability selection

The caller — human or AI — decides the required capability level; Orchestration does
not run a classifier to infer it. Automatic model-selection is parked, not designed.

A small, provider-independent vocabulary is used:

```
basic | standard | high | maximum
```

These are the proposed v1 names. Final naming is a pre-deployment decision — the names
must be settled before the v1 dispatch contract is frozen, because renaming after
deployment is an interface migration. They may remain provisional at design acceptance.

An escape hatch allows requesting an exact provider model directly, for testing,
comparison, or reproduction:

```yaml
model:
  exact: provider-specific-model
```

`level` and `exact` are mutually exclusive.

When `model` is omitted from a dispatch request, the target's default logical level
from Framework Resources is used. The caller is still the owner of the selection —
omission is an explicit delegation to the configured default, not a transfer of
authority.

### Model-level resolution

Orchestration maps a logical level to target-specific invocation settings. Resolution
produces native model identity and reasoning effort — settings that express model
capability. It does not include sandbox mode, permission/approval mode, tool access, or
other execution-policy settings that belong to the caller's workflow.

The **exact-model path** bypasses logical-level resolution. The adapter uses the
specified model directly and records the native settings it applied. No Resources
resolution is involved; `resources_version` in provenance is `null`.

Two logical levels may legitimately resolve to the same native configuration where a
provider doesn't currently expose a meaningful distinction. **The mapping content itself
is not owned by Orchestration — see Framework Resources, below.**

### `response_schema` as invocation capability, not contract

The Claude Agent SDK's `outputFormat` and Codex's `--output-schema` both support
schema-constrained final output — confirmed technically by the investigation. This is a
useful capability some adapters expose; it is never a mandatory part of the
Orchestration contract itself. Orchestration transports a caller-supplied schema to
a target that supports it; it does not enforce or validate the schema's content.

When an adapter does not support schema-constrained invocation, the dispatch fails with
`unsupported_capability` rather than silently proceeding without the constraint. The
caller explicitly requested constrained output; silently delivering unconstrained output
would undermine the trust and integrity rationale.

---

## Framework Resources — a Core dependency, not an Orchestration artefact

This model-mapping need exposed a pattern broader than Orchestration: the distinction
between AIDE's durable behaviour/model and the volatile current knowledge that behaviour
consumes (current platform list, current model-capability mappings, current defaults).

**This belongs to Core, as a cross-cutting framework pattern.** Orchestration is a
consumer of Framework Resources, not its owner. Core is free to design the Resources
mechanism (naming, deployment cadence, storage) however it sees fit.

**Orchestration's consumer contract:** Orchestration requires Core to enable it to:

1. **Resolve a logical level** — given a target and a logical capability level, obtain
   the native invocation settings and the Resources version used.
2. **Obtain a target's default level** — when the caller omits `model`, determine the
   configured default logical level for the specified target.
3. **Determine target support** — check whether a target is currently supported by
   Resources, for use in availability calculation.

These are stated as required behaviours, not as a prescribed API. Core may satisfy them
through one operation, several operations, a loaded resource document, or another
mechanism entirely.

What Orchestration needs Resources to contain, indicatively:

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

The actual schema is Core's to settle.

**Settings vs Resources:** Resources describe the default/current AIDE world (which
platforms are supported); a portable user setting customises it for one person (e.g.
`disabledOrchestrationPlatforms: [Gemini]`). Not critical to Orchestration v1 — noted
so the boundary isn't invented ad hoc later inside Orchestration.

---

## Machine and execution-endpoint availability

### Detection before configuration

Availability of an execution target should normally be discovered, not configured.
Effective availability is:

```
supported by Resources ∩ detected on this endpoint ∩ not explicitly disabled
```

Machine-specific configuration is only introduced where detection genuinely cannot
represent a real requirement.

### Capability availability is not execution-endpoint availability

An AI session having the Orchestration capability does not imply it has access to a
local execution endpoint. A web-only chat session may have none; one machine may have
Claude Code and Codex both available, another only Claude Code.

### Endpoint operations

The local execution endpoint exposes two operations:

1. **`available_targets()`** — returns the effective target set: which targets are
   currently available and, for unavailable targets, the reason. This is how a caller
   determines which target choices are valid before dispatching.

   ```yaml
   endpoint: david-laptop
   targets:
     claude-code: { available: true }
     codex: { available: true }
     gemini: { available: false, reason: "consumer auth discontinued" }
   ```

2. **`dispatch(request)`** — accepts a dispatch request (target, payload, optional
   workspace/model/response_schema), creates a dispatch_id, invokes the target through
   its adapter, and returns the transport result.

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

Orchestration requires a **local execution endpoint** that exposes dispatch
functionality and target availability. The current implementation is a local MCP server.

The delivery mechanism — how this server is packaged, distributed, installed, updated,
and made available across surfaces — belongs to Infrastructure, not Orchestration.
Orchestration owns the dispatch behaviour, adapters, model-level resolution, and
invocation semantics inside the server. Infrastructure owns the packaging.

The empirical testing on 2026-09-16 confirmed a marketplace-plugin delivery model
reaching all three surfaces (Code, Cowork, Chat) from a single server file. That
evidence is input to Infrastructure's design pass as a proven approach — it is not an
Orchestration design decision.

### What was superseded

The original investigation considered standalone script, Claude Code skill, Desktop
Extension, and `aide dispatch` inside the CLI. The plugin-delivered MCP server
supersedes all four.

## Target adapters

First implementation stays small: `claude-code` and `codex`. An adapter converts stable
dispatch semantics into native invocation details — e.g. for Codex, `model.level: high`
resolves via current Resources to a native model plus `reasoning_effort: high`, then
invokes `codex exec`.

Gemini/Google support is additive, added when there's a sufficiently stable execution
path — not required to block the first implementation.

## Statelessness

Each dispatch is independently executable. Provider session IDs may be preserved as
returned metadata where useful, but no AIDE session-management abstraction is built
until a demonstrated workflow requires one.

## Intermediate progress

No semantic progress protocol in v1. Provider event streams may be surfaced or logged
opportunistically; the stable contract only needs to distinguish transport completion
from transport failure.

---

## FUP validation scenario

Still the end-to-end transport test:

```
caller supplies dispatch request → Orchestration creates dispatch, invokes Claude Code
    → Claude Code runs `aide fup` → transport result returns
```

Exercises invocation, authentication, workspace passing, local tooling, execution,
dispatch correlation, and return handling — the whole transport, without needing to
prove anything about sophisticated build delegation at the same time.

Do not reproduce FUP deployment logic inside Orchestration or inside the invoked agent.
Use the existing `aide fup` unchanged.

## Messaging boundary

Orchestration does not define a second generic messaging envelope. Messaging already
owns structured communication and message/thread correlation semantics for
cross-boundary communication. Where work needs to cross as structured text, Messaging's
envelope carries the caller-owned request; Orchestration owns moving and invoking it.

---

## Two boundary confirmations

- **Tier (autonomous vs heavyweight) is caller-owned, not Orchestration-owned.**
  Orchestration dispatches; whether the surrounding workflow is autonomous or
  Dave-driven-interactive is a property of the caller's process.
- **Routing is caller-owned.** The caller decides the target explicitly per dispatch;
  Orchestration executes the routing decision.

---

## Proposed Core boundary wording (for Core's design pass, not adopted here)

> **Orchestration — Coordinate invocation across AI execution targets. Accept
> caller-selected targets and caller-owned work, resolve requested logical model
> capability using Core-owned Framework Resources, invoke target adapters/endpoints,
> correlate each dispatch with its transport outcome, and return the target response.
> Orchestration does not define the task, verification policy, routing decision, or
> semantic meaning of the response.**

---

## Deferred

1. Framework Resources schema and deployment mechanism — Core's design pass.
2. Portable user/account settings mechanism and deployment.
3. Any genuine machine-specific settings beyond environment discovery.
4. Remote execution endpoints reachable from web-hosted sessions.
5. Stateful/multi-turn orchestration.
6. A semantic intermediate-progress protocol.
7. Broader Google/Gemini execution support.
8. Additional target-capability metadata beyond what the first two adapters demonstrate.

## Pre-deployment decisions

1. Final naming of model capability levels (`basic/standard/high/maximum` proposed).
   May remain provisional at design acceptance; must be settled before the dispatch
   contract is frozen.

---

## Short-form model

> Orchestration moves caller-owned work to another AI execution target and brings the
> result back. The caller chooses the target and required logical model capability.
> Orchestration resolves that request through Core-owned Framework Resources into
> target-native invocation settings and executes it through an available endpoint.
> Orchestration owns the crossing — dispatch correlation, invocation, and transport
> outcome — not the work, its verification policy, or the semantic meaning of the
> response.
