# AIDE Standards Production — Standard

> **Identity:** `AIDE_StandardsProduction@v2`
> **Common name:** Standards Production
> **Version 2** (2026-09-01). Adds production-time capability-reference semantics from Review C while preserving the existing canonical Standard contract and weights.

---

## Purpose

Produce a canonical AI-facing Standard from confirmed Capability Design without introducing new
capability meaning during production.

This Standard governs the **canonical Standard outcome** only. Platform skill/plugin/bundle
realisation, packaging, WorkPackage execution, and Deployment are later concerns.

## Applicability

Apply when a confirmed Capability Design declares a Standard outcome or when an existing canonical
Standard is being rebuilt for a new capability release.

```yaml
Scope:
  Context: >
    Apply when producing or validating a canonical Standard from confirmed capability design.
```

## Required inputs

Resolve before production:

- the confirmed Capability Design and declared Standard output;
- formal capability identity and intended release version;
- applicable shared Standards, including Scope, Dependencies, Migration, and Review where used;
- any capability-specific platform addenda confirmed by the Design; and
- the previous canonical release/transition history where this is not the first release.

If capability meaning, release identity/version, or an authoritative input is materially ambiguous,
stop and return the gap to the work owner. Production does not fill design gaps by invention.

## Capability-reference semantics

During canonical production, distinguish reference roles rather than treating every version token as
a currency target:

- footer `Dependencies: X@vN` is a saved/proven conformance checkpoint owned by `AIDE_Dependencies`;
- footer `References:` is a reader/evidence pointer with no currency or conformance obligation; and
- a current executable in-body capability reference is an operational instruction.

Use a versionless identity for executable references by default. Name a specific capability release
only where the instruction deliberately depends on that release's contract or intentionally targets
it. Validate that any specific version is intentional and correct; do not mechanically advance every
body reference to the newest release.

## Canonical Standard contract

A canonical Standard contains only the capability meaning needed by its consumers and later Build.
Where applicable it carries:

- formal identity, common name, and capability release version;
- purpose and applicability;
- complete rules/guidance/context needed to operate under the capability;
- effective weight for every addressable/chunkable unit;
- `AIDE_Scope` declarations;
- `AIDE_Dependencies` declarations;
- `AIDE_Migration` summary and supported transition history;
- owner-defined Tag/Dependency Builder definitions;
- Review expectations/profile references where confirmed; and
- capability-specific platform addenda only.

Generic platform implementation metadata or mechanics do not belong in the canonical Standard.

## Weight production

Supported weights are:

```text
Requirement | Expectation | Guidance | Context
```

Every addressable unit must have an effective weight. Use the smallest clear representation:

1. an optional document default;
2. section/unit declaration where it differs or where no document default exists; and
3. statement/block override only where necessary.

Nearest declaration wins. A chunk with no effective weight is a production defect.

Weight meaning:

- `Requirement` — needed for the stated outcome/consumer to work; ordinary departure is not
  permitted.
- `Expectation` — default position; departure is allowed but must be made visible.
- `Guidance` — recommended/default practice; departure is allowed and its consequences are owned.
- `Context` — explanatory information with no obligation.

Requirements are expressed through consequence/value rather than bare authority.

## Production procedure

1. Read the confirmed Design and its declared outputs; do not use Decisions as an outcome input.
2. Resolve identity and intended capability release version.
3. Extract the complete confirmed Standard meaning, removing design-process reasoning that is not
   needed by consumers.
4. Preserve capability terminology and boundaries exactly; do not broaden ownership.
5. Apply the canonical Standard contract and effective weights.
6. Add shared Scope/Dependencies/Migration/Review declarations only where the Design requires them.
7. Carry forward supported transition history and update `MigrationSummary` for a later release.
8. Include only confirmed capability-specific platform addenda.
9. Validate completeness, internal coherence, dependency identities, transition continuity,
   capability-reference role/specificity, and chunk-level weight coverage.
10. Produce the canonical Standard and report any unresolved production defect rather than silently
    repairing the Design.

## First release and migration

A first release has no older consumer state to transform, but still declares positive transition
state so later tooling has an unambiguous history:

```yaml
MigrationSummary:
  CurrentVersion: v2
  LatestRequiredVersion: none
  LatestOnUpdateVersion: none

Transition:
  Version: v1
  Posture: None

Transition:
  Version: v2
  Posture: None
```

Later releases follow `AIDE_Migration` and retain the transition history required by the supported
baseline.

## Validation failures

Production fails visibly when, among other cases:

- Design does not determine required capability behaviour;
- declared output and Design disagree;
- identity/release version is unresolved;
- an addressable unit has no effective weight;
- Scope/Dependency/Migration declarations are contradictory or incomplete;
- a current executable capability reference is unintentionally stale or unjustifiably version-specific;
- a later release lacks required transition continuity; or
- platform-generic implementation has leaked into canonical capability meaning.

Return the smallest actionable defect set to the work owner. Do not create policy during repair.

## Output

The output is one canonical Standard for the declared capability release, ready for the normal
Build-side platform realisation flow.

---
Dependencies: !AIDE_DocumentationMethodology@v26, Capabilities_Standards_Design_v5, AIDE_Scope@v2, AIDE_Dependencies@v3, AIDE_Migration@v2
References: Capabilities_Tools_Design_v3, AIDE_BuildCapabilityTool
