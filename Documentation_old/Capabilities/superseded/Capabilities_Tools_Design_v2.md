# Capabilities Tools — Design

> **Version 2** (2026-08-29). Reconciles Tools with shared Scope, Dependencies, Migration and
> Build-side platform realisation; retains the input/decision/reporting/idempotency model and
> permits bounded contract-defined judgment such as that used by the Review Tool.
>
> Created: 2026-08-27 | Last modified: 2026-08-29

---

## §1 — Role and purpose

A Tool encapsulates a repeatable invokable action so its mechanism and safety checks are not
re-derived every time it is used.

Its value remains determinism of the action contract, encapsulation, lower repeated reasoning cost,
and completeness.

A Tool may contain bounded judgment where its contract explicitly defines how to infer, ask,
select, continue, or escalate. Genuine substantive authority remains with the work owner or the
capability that owns that judgment.

## §2 — Canonical Tool structure

A Tool Design defines, in this order where applicable:

### Identity and logical actions

Stable Tool identity/common name and the logical actions/commands it contributes. Platform names
and invocation syntax are later renderings.

### Trigger and Scope

Explicit invocation plus contextual circumstances where the Tool should be selected proactively.
Applicability is declared through `AIDE_Scope`, not a Tools-local model.

### Purpose

A dense selection/retrieval statement describing the action/outcome.

### Inputs

For each input: requirement/default, resolution sources, and confirmation posture.

### Preconditions

Facts that must hold before changing state.

### Procedure

Ordered operational steps.

### Decision points

Visible branches and the rule/authority that resolves them. Do not hide substantive decisions in
procedure prose.

### Escalation conditions

Conditions where the Tool must hand back rather than invent policy/authority.

### Outputs and effects

Produced artefacts, changed state, persistent records.

### Reporting

Minimal/summary/detailed/verbose narration as appropriate; failures/deviations always surface.
Narration verbosity does not reduce the persisted record.

### Failure handling and idempotency

Partial-completion semantics, resumability/retry behaviour, and explicit idempotency declaration.

## §3 — Ask, infer, escalate

- infer and state where confidence is strong and cost of error low;
- ask once, preferably batched, for genuinely missing required inputs;
- escalate genuine conflicts, authority decisions, or material uncertainty the Tool does not own.

Never fail for want of information that could reasonably have been requested.

## §4 — Standards boundary

A Standard shapes behaviour/decision context. A Tool exposes a named invokable action.

A Standard may describe a procedure until a Tool exists; once an authoritative Tool owns the
action, the Standard points to it rather than duplicating the executable mechanism.

One Capability Design may produce sibling Standards and Tools from the same confirmed meaning.

## §5 — Scope, dependencies and migration

Tools consumes the shared contracts:

- Scope → whether the Tool/action applies;
- Dependencies → identities/version state the Tool relies on;
- Migration → release transitions affecting durable consumer state/configuration/contract.

Tools are **not categorically excluded from Migration**. If a Tool release has no existing durable
consumer state to transition, it declares `None`; if a real transition exists, it uses the same
Required/OnUpdate/None model as Standards.

## §6 — Canonical production and platform realisation

```text
Tool Design
   ↓
Build Capability
   ↓
canonical Tool
   ↓
Build WorkPackage
   ↓
platform Build Standards/Tools
   ↓
platform contribution
```

The canonical Tool carries platform-independent action semantics plus capability-specific platform
addenda only. Generic skill/plugin/command-file/UI mechanics belong Build side.

## §7 — Version/release/package boundary

A Tool's formal capability release version is distinct from the DocMeth version of its Design.
Dependencies may track consumer conformance to the Tool capability version where relevant.

Package identity/integrity identifies a produced package of that release; Deployment state records
what package/release is installed. Neither is another Tool semantic version.

## §8 — Reporting preferences

The four narration levels remain minimal, summary, detailed, verbose, defaulting to summary where
no stronger environment/user preference is available. The long-term storage home for account/
environment preferences remains external architecture work; Tools only consumes the resolved
preference.

## §9 — Ownership boundary

Tools owns the generic Tool/action contract and canonical Tool semantics. Shared peer components own
Scope, Dependencies, Migration, Review, Deployment, and platform implementation/build knowledge.

---

**Depends on:** `Capabilities_Design_v6`, `Capabilities_Decisions_v12`.

**References:** `Capabilities_Tools_Brief_v2`, `Capabilities_Standards_Design_v4`,
`AIDE_Scope@v1`, `AIDE_Dependencies@v2`, `AIDE_Migration@v1`.

**Methodology:** v17
