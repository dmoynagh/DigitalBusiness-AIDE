# Capabilities Tools — Design

> **Version 4** (2026-09-02). Separates Element update, Build Capability orchestration and Capability Builder execution.

---

## §1 — Role and purpose

A Tool encapsulates a repeatable invokable action so its mechanism and safety checks are not
re-derived every time it is used.

Its value remains determinism of the action contract, encapsulation, lower repeated reasoning cost,
and completeness.

A Tool may contain bounded judgment where its contract explicitly defines how to infer, ask,
select, continue, or escalate. Genuine substantive authority remains with the work owner or the
capability that owns that judgment.

### Published production contract

This Design produces `AIDE_ToolsProduction@v1`, the published generic contract for producing and
validating canonical Tools from confirmed Tool/Capability Design. The structure below remains the
Tools-owned semantic source; downstream producers consume the published contract rather than
copying this internal Design.

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
Tool / Capability Design
   ↓
AIDE_ToolsProduction
   ↓
canonical Tool
   ↓
Build WorkPackage
   ↓
platform Build Standards/Tools
   ↓
platform contribution
```

`AIDE_UpdateCapabilityElementsTool` invokes `AIDE_ToolsProduction@v2` where documented production is required; directly authored Tool Elements and other authorised producers may consume the same contract. The
canonical Tool carries platform-independent action semantics plus capability-specific platform
addenda only. Generic skill/plugin/command-file/UI mechanics belong Build side.

## §7 — Version/release/package boundary

A Tool Element release is distinct from the DocMeth version of its sources and from the containing Capability release/composition. Package identity/integrity identifies a Build instance; Deployment state records what is installed. Neither is another Tool Element release.

## §8 — Reporting preferences

The four narration levels remain minimal, summary, detailed, verbose, defaulting to summary where
no stronger environment/user preference is available. The long-term storage home for account/
environment preferences remains external architecture work; Tools only consumes the resolved
preference.

## §9 — Ownership boundary

Tools owns the generic Tool/action contract and canonical Tool semantics. Shared peer components own
Scope, Dependencies, Migration, Review, Deployment, and platform implementation/build knowledge.


## §8 — Current production/build Tool family

- `AIDE_UpdateCapabilityElementsTool@v1` — design-side Element evaluation/production.
- `AIDE_BuildCapabilityTool@v3` — Build request/readiness/WorkPackage orchestration.
- `AIDE_CapabilityBuilderTool@v1` — Build-side specialised executor.

`AIDE_BuildCapabilityTool@v2` remains historical and requires explicit migration; its production
role is not silently interpreted as v3. Tool Element production uses `AIDE_ToolsProduction@v2`.

---
Dependencies: !AIDE_DocumentationMethodology@v27, Capabilities_Design_v12, Capabilities_Decisions_v17
References: Capabilities_Tools_Brief_v4, Capabilities_Standards_Design_v7, AIDE_Scope@v2, AIDE_Dependencies@v3, AIDE_Migration@v2
