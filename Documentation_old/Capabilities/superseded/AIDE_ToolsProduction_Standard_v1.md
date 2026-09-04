# AIDE Tools Production — Standard

> **Identity:** `AIDE_ToolsProduction@v1`
> **Common name:** Tools Production
> **Version 1** (2026-09-01). First published Tools-owned contract for producing a canonical Tool
> from confirmed Tool/Capability Design.
>
> **Default weight:** Requirement

---

## Purpose

Produce a complete platform-independent canonical Tool from confirmed Tool/Capability Design without
inventing capability meaning during production or leaking generic platform implementation into the
canonical outcome.

## Applicability

Apply when confirmed Design declares a Tool outcome or when an existing canonical Tool is rebuilt
for a new capability release.

```yaml
Scope:
  Context: >
    Apply when producing or validating a canonical Tool from confirmed Tool/Capability Design.
```

## Required inputs

Resolve before production:

- confirmed Tool/Capability Design and declared Tool outcome;
- formal Tool identity, common name, logical actions and intended capability release version;
- applicable Scope, Dependencies and Migration contracts;
- capability-specific platform addenda confirmed by Design, if any;
- prior canonical release/transition history where this is not the first release; and
- current authority to produce or replace the outcome.

If substantive Tool behaviour, release identity/version or another authoritative input is materially
ambiguous, stop and return the gap to the work owner. Production does not repair Design by invention.

## Canonical Tool contract

A canonical Tool contains enough platform-independent information to implement the same logical
action contract on any supported platform:

1. stable identity/common name and logical actions;
2. trigger and `AIDE_Scope` applicability;
3. purpose;
4. inputs, defaults, resolution sources and confirmation posture;
5. preconditions;
6. ordered procedure;
7. explicit decision points and the rule/authority resolving them;
8. escalation conditions where the Tool must hand back rather than invent policy;
9. outputs/effects and persistent-state consequences;
10. reporting contract; and
11. failure, partial-completion, idempotency and resumption semantics.

A Tool may orchestrate bounded declared judgment. It does not acquire substantive authority absent
from its Design.

## Ask, infer and escalate

- infer where confidence is strong and cost of error is low;
- ask once, preferably batched, for genuinely missing required inputs; and
- escalate genuine conflicts, authority decisions or material uncertainty the Tool does not own.

Do not fail for information that can reasonably be requested, and do not convert a missing Design
decision into producer policy.

## Shared capability contracts

Use the shared owners rather than restating them:

- `AIDE_Scope` — applicability;
- `AIDE_Dependencies` — dependency/version/presence state;
- `AIDE_Migration` — release transitions affecting durable consumer state/configuration/contract.

Use versionless current executable capability identities by default. A specific version is valid
only where the instruction deliberately depends on or targets that release; validate such
specificity rather than mechanically advancing it.

## Production procedure

1. Read the confirmed Design and declared Tool outcome; Decisions are not downstream production
   input.
2. Resolve identity, common name, logical actions and intended release version.
3. Extract the complete confirmed Tool behaviour into the canonical Tool contract above.
4. Preserve capability terminology, ownership and authority boundaries exactly.
5. Add shared Scope/Dependencies/Migration declarations only as required by Design.
6. Carry supported transition history and update `MigrationSummary` for later releases.
7. Include only confirmed capability-specific platform addenda; exclude generic platform
   skill/plugin/command/UI mechanics.
8. Validate completeness, cross-action coherence, dependency identities, transition continuity,
   capability-reference specificity and idempotency/resumption behaviour.
9. Produce the canonical Tool or return the smallest actionable production-defect set.

## Validation failures

Fail visibly when, among other cases:

- Design does not determine required Tool behaviour;
- identity/release/logical actions are unresolved;
- a required input/precondition/decision/escalation/output/failure behaviour is missing;
- Scope/Dependency/Migration declarations contradict the Design;
- a current executable capability reference is unintentionally stale or unjustifiably
  version-specific;
- a later release lacks required transition continuity; or
- generic platform implementation has leaked into canonical Tool meaning.

## Output

The output is one canonical Tool for the declared capability release, ready for normal Build-side
platform realisation without reopening internal Tool Design.

```yaml
MigrationSummary:
  CurrentVersion: v1
  LatestRequiredVersion: none
  LatestOnUpdateVersion: none

Transition:
  Version: v1
  Posture: None
```

---
Dependencies: !AIDE_DocumentationMethodology@v26, Capabilities_Tools_Design_v3, AIDE_Scope@v2, AIDE_Dependencies@v3, AIDE_Migration@v2
References: AIDE_BuildCapabilityTool, AIDE_StandardsProduction
