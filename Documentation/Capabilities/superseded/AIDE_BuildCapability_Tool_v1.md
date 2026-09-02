# AIDE Build Capability — Tool

> **Identity:** `AIDE_BuildCapabilityTool@v1`
> **Common name:** Build Capability
> **Version 1** (2026-08-30). Canonical design-side Tool for producing Standards/Tools from
> confirmed Capability Design.

---

## Purpose

Turn confirmed Capability Design into complete canonical Standard and/or Tool outcomes without
inventing new capability meaning and without crossing into platform Build or Deployment.

## Logical actions

```yaml
Tool:
  Identity: AIDE_BuildCapabilityTool@v1
  CommonName: Build Capability
  PrimaryInvocation: build-capability
  LogicalActions: [Build, Validate, Status]
```

## Trigger and inputs

Run when confirmed Capability Design is ready to produce/rebuild canonical outcomes, or when the
user/Lead asks whether that Design is production-ready.

Resolve the Design, its declared Standard/Tool outputs, formal identity/common name, intended
capability release version, applicable production contracts/shared Standards, previous release and
transition history where relevant, and current authority to produce the outcomes.

Do not infer a substantive design choice or semantic release version where the authoritative state
is ambiguous.

## Build

1. Read confirmed Capability Design and its declared outputs. Do not use Decisions as downstream
   production input.
2. Resolve each output kind, identity, and intended capability release version.
3. For each Standard, apply `AIDE_StandardsProduction@v1`.
4. For each Tool, produce the platform-independent Tool contract: identity/logical actions,
   trigger/Scope, purpose, inputs, preconditions, procedure, bounded decisions/escalation,
   outputs/effects, reporting, failure handling, and idempotency/resumption.
5. Preserve confirmed Scope, Dependencies, Migration, and Review semantics; do not restate their
   shared mechanisms inconsistently.
6. Exclude generic target-platform implementation. Include only capability-specific platform
   addenda explicitly confirmed by Design.
7. Validate each output and the sibling output set for completeness and contradiction.
8. Produce the canonical output set, or return a precise `DesignIncomplete`/production-defect result
   rather than repairing the Design by invention.

## Validate

Perform Build's readiness/completeness checks without replacing outputs. Return Ready/NotReady and
the smallest actionable set of missing/ambiguous inputs, shared-contract defects, or cross-output
contradictions.

## Status

Report target Design, declared outputs, resolved identities/releases, current canonical outcomes
where available, readiness, and next action.

## Boundary

Successful output is:

```text
canonical Standard / Tool outcome(s)
```

Build Capability stops there. Effective Build Config, WorkPackage, platform Build Standards/Tools,
Platform Contributions, Capability Package/Deployment Manifest, and Deployment are later stages.

## Failure and idempotency

- Missing design determination → stop and identify the unresolved point.
- Unresolved identity/release → ask/escalate; do not invent.
- Canonical/shared-contract contradiction → fail visibly.
- Re-running unchanged confirmed Design for the same release produces substantively equivalent
  canonical outcomes and does not create a new release solely because generation was repeated.

Normal reporting states outcomes produced/validated, identities/releases, and anything requiring
attention.

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

**Depends on:** `Capabilities_BuildCapability_Tool_Design_v1`, `AIDE_StandardsProduction@v1`,
`Capabilities_Tools_Design_v2`.

**References:** `AIDE_Scope@v1`, `AIDE_Dependencies@v2`, `AIDE_Migration@v1`.

**Type:** `Tool` — custom. Defined in `Capabilities_Index`, local configuration.

**Methodology:** v17
