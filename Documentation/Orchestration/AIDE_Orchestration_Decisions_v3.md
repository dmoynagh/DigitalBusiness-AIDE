# AIDE Orchestration — Decisions v3

> identity: Orchestration_Decisions@v3 | doctype: decisions | updated: 2026-09-17

Two cross-review rounds completed (independent AI). Round 1: F1–F15, resolved in v2
(D20–D34). Round 2: R2-F1–R2-F7, resolved in v3 (D35–D41). D1–D34 unchanged except
where noted.

---

## v1 decisions

**D1 — Dispatch replaces the universal Work Package as Orchestration's artefact.**
Unchanged.

**D2 — Orchestration ownership narrowed.** Owns: dispatch acceptance and dispatch_id
creation, invocation, target-native invocation mechanics, target adapters, model-level
resolution (model capability settings only), execution-endpoint interaction, dispatch
correlation, transport/invocation failure, returning results to the caller. Does not
own: work-package/build-package structure, task types, verification policy, acceptance
criteria, review semantics, Build's return semantics, generic response semantics,
human/autonomy policy, model-mapping content, routing/target-selection decisions, or
message/thread correlation.

*v3 change (R2-F1):* "dispatch acceptance and dispatch_id creation" replaces "dispatch"
to clarify that Orchestration creates the correlation identifier, not the caller.

**D3 — Core's current wording needs correction.** Proposed replacement wording in
Design v3. Unchanged from v2.

**D4 — Transport outcome and task outcome are distinct fields.** Unchanged.

**D5 — `response_schema` is an adapter capability, not a mandatory contract.**
Unchanged in principle.

*v3 change (R2-F2):* behaviour when adapter doesn't support it changed from silent
degradation to invocation failure. See D36.

**D6 — Model capability is caller-selected, not classifier-selected.** Unchanged.

**D7 — Model-capability mapping content belongs to Core (Framework Resources), not
Orchestration.** Unchanged.

**D8 — Availability is discovered, not configured.** Unchanged.

**D9 — Capability availability and execution-endpoint availability are different
things.** Unchanged.

**D10 — Orchestration requires a local execution endpoint.** Unchanged from v2.

**D11 — First adapters: `claude-code` and `codex` only.** Unchanged.

**D12 — Stateless first.** Unchanged.

**D13 — No semantic intermediate-progress protocol in v1.** Unchanged.

**D14 — FUP remains the validation scenario.** Unchanged.

**D15 — No second generic messaging envelope.** Unchanged.

**D16 — Tier is caller-owned.** Unchanged.

**D17 — Routing is caller-owned.** Unchanged.

**D18 — Plugin delivery is Infrastructure's direction.** Unchanged.

**D19 — Assurance's D14 wording needs correcting.** Unchanged.

---

## v2 decisions (round 1 remediation)

**D20 — `response_schema` added as optional top-level dispatch field (F1).** Unchanged
in placement.

*v3 change (R2-F2):* silent-ignore behaviour replaced by invocation failure. See D36.

**D21 — Payload is UTF-8 text for v1 (F2).** Unchanged.

**D22 — Dispatch correlation is Orchestration-owned; message/thread correlation is
Messaging-owned (F4).** Unchanged.

**D23 — "Transport/channel selection" replaced by "target-native invocation mechanics"
(F5).** Unchanged.

**D24 — Model-level resolution narrowed to model capability settings only (F6).**
Unchanged.

**D25 — Dispatch field cardinality and omission behaviour defined (F7).**

*v3 change (R2-F1):* `dispatch_id` removed from the dispatch request fields — it
appears only in the dispatch (Orchestration-created) and the transport result.

*v3 change (R2-F6):* workspace omission behaviour tightened — if the target/adapter
requires a workspace and none was supplied, the dispatch fails before execution rather
than using an unspecified native default.

**D26 — Transport failure contract defined (F3).**

*v3 change (R2-F2):* `unsupported_capability` added as a failure category for
invocation-capability mismatches (e.g. response_schema on an adapter that doesn't
support it).

**D27 — Provenance is required on completed transport results (F13).**

*v3 change (R2-F3):* `requested_level` replaced by `requested_model`, which
symmetrically represents both `{ level: high }` and `{ exact: provider-model }`.
`resources_version` is `null` for the exact-model path, which bypasses Resources
resolution.

**D28 — Charter alignment corrected (F14).** Unchanged.

**D29 — Proposed Core wording updated (F15).** Unchanged from v2.

**D30 — Implementation home split (F11).** Unchanged.

**D31 — Use cases 5/6 reworded (F12).** Unchanged.

**D32 — Target discovery noted as implementation concern (F8).**

*v3 change (R2-F5):* upgraded from implementation note to explicit endpoint operation.
See D39.

**D33 — Capability level names are pre-deployment, not indefinitely deferred (F9).**

*v3 change (R2-F7):* timing language corrected. See D41.

**D34 — Framework Resources consumer contract stated (F10).**

*v3 change (R2-F4):* consumer contract expanded. See D40.

---

## v3 decisions (round 2 remediation)

**D35 — Dispatch request separated from dispatch (remediates R2-F1).** The v2 contract
conflated what the caller sends with what Orchestration creates. `dispatch_id` appeared
as a "required" field in the dispatch, but Orchestration creates it — a caller cannot be
required to provide a value it doesn't own. v3 separates: the **dispatch request** is
what the caller sends (target, payload, optional workspace/model/response_schema); the
**dispatch** is the accepted request plus the Orchestration-created `dispatch_id`. The
transport result echoes that `dispatch_id`. This is not a new artefact model — it is the
minimal distinction needed for an implementable API boundary.

**D36 — Unsupported `response_schema` fails the invocation, not silent degradation
(remediates R2-F2).** v2 said the adapter silently ignores an unsupported
`response_schema` and the dispatch proceeds without schema constraint. This is unsafe:
the caller explicitly requested constrained output and may treat the response as
constrained when it was not. v3 changes the behaviour: when the selected adapter does
not support schema-constrained invocation, the dispatch fails before invocation with
category `unsupported_capability`. The caller can retry without the schema if they want
unconstrained output. Orchestration still does not own or validate the schema's meaning
— it only ensures the requested invocation capability was applied or honestly reported
as unavailable.

**D37 — Provenance represents the requested model symmetrically (remediates R2-F3).**
v2 provenance required `requested_level`, which cannot represent a dispatch using
`model.exact`. v3 replaces this with `requested_model`, which carries either
`{ level: high }` or `{ exact: provider-model }` matching the form the caller used.
For the exact-model path: no Resources resolution is involved, the adapter uses the
specified model directly and records the native settings it applied, and
`resources_version` is `null`. This makes the dispatch contract and the result contract
mutually consistent across both model-selection forms.

**D38 — Workspace omission fails when the target requires a workspace (remediates
R2-F6).** v2 said an omitted workspace could fall back to the target's native default.
This is dangerous: operating against an unspecified working directory can cause
otherwise valid work to execute against the wrong location, with `completed` transport
status, which is worse than a transport failure. v3 tightens: if the target/adapter
requires a workspace and none was supplied, the dispatch fails before execution. If the
target supports genuinely workspace-free invocation (e.g. a review prompt fully
self-contained in payload), no workspace is passed. Orchestration does not substitute an
unspecified native default for the caller's routing decision.

**D39 — Target discovery is an explicit endpoint operation (remediates R2-F5, upgrades
D32).** v2 downgraded target discovery to an implementation note. The round 2 review
correctly identified that the design requires callers to choose a valid target (D17) but
provides no defined way to learn which targets are currently valid. This is the discovery
half of the endpoint contract already required by the detection-before-configuration
principle (D8/D9). v3 adds `available_targets()` as an explicit endpoint operation
returning the effective target set with unavailability reasons. This is a very small
addition — not a capability-negotiation framework — and closes the gap between
caller-owned routing and the information callers need to exercise it.

**D40 — Framework Resources consumer contract expanded to three behaviours (remediates
R2-F4).** v2's consumer contract was `resolve(target, logical_level) → native settings +
version`. Two behaviours the design already requires were missing: determining the
target's default logical level (used when the caller omits `model`), and determining
whether a target is currently supported by Resources (used in availability calculation).
v3 states all three as required behaviours without prescribing Core's API: (1) resolve a
logical level to native settings; (2) obtain a target's default level; (3) check target
support. Core may satisfy them however it chooses.

**D41 — Capability level naming timing corrected (remediates R2-F7).** v2 said the
proposed names are "not deferrable beyond design acceptance" and then listed them as a
pre-deployment decision. These statements are contradictory. v3 settles: final
capability-level names may remain provisional at design acceptance and must be settled
before the dispatch contract is frozen (pre-deployment). The substantive point —
renaming after deployment is an interface migration — is unchanged.

---

## Deferred

1. Framework Resources schema and deployment mechanism — Core's design pass.
2. Portable user/account settings mechanism.
3. Genuine machine-specific settings beyond environment discovery.
4. Remote execution endpoints for web-hosted sessions.
5. Stateful/multi-turn orchestration.
6. Semantic intermediate-progress protocol.
7. Broader Gemini/Google execution support.
8. Adapter-capability metadata beyond what the first two adapters demonstrate.

## Pre-deployment decisions

1. Final naming of model capability levels (`basic/standard/high/maximum` proposed).
   May remain provisional at design acceptance; must be settled before interface freeze.
