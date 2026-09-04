# AIDE WorkPackage — Standard

> **Identity:** `AIDE_WorkPackage@v3`
> **Common name:** WorkPackage
> **Version 3** (2026-09-01). Clarifies deterministic-enough coverage when one WorkRegister obligation is deliberately split across multiple WorkPackages.
>
> **Default weight:** Requirement

---

## Purpose

Provide Build with one bounded executable contract that states the required result, authority, work-specific inputs and acceptance, and returns enough evidence for the director of work to reconcile execution.

## Required WorkPackage content

Resolve before execution:

```yaml
WorkPackage:
  Objective: <required result>
  AuthorisedScope: <allowed work and material exclusions>
  Inputs: <work-specific authoritative inputs>
  RequiredOutputs: <artefacts/state to produce or change>
  Acceptance: <observable completion/evidence conditions>
  Constraints: <applicable limits/dependencies/targets/reserved decisions>
  Review: <optional explicit plan/result Review posture>
  Return: <required outcome destination/record>
  WorkRegisterItems: <optional source item IDs and covered portions>
```

Equivalent clear prose/sections are valid; the semantic fields matter, not this physical rendering.

If a material field is unresolved and cannot safely be inferred from authoritative inputs, the WorkPackage is NotReady.

## WorkRegister mapping

A WorkPackage may be created directly from defined work or may cover some/all of one or more
WorkRegister obligations. Where mapped, record each source item ID and the portion covered by this
package.

```yaml
WorkRegisterItems:
  - Id: WR12
    Covers: comparer implementation and tests
  - Id: WR13
    Covers: documentation update
```

One WorkRegister item may be delivered through several WorkPackages; one WorkPackage may cover
several items.

Where one source obligation is deliberately split across multiple WorkPackages:

- the source obligation's required changes must be independently identifiable, normally as an
  owner-supplied enumerated/bulleted set;
- each WorkPackage `Covers` must identify the exact required changes/portion it claims;
- equivalent clear prose is valid when unambiguous; and
- do not introduce structured sub-obligation identifiers merely to support the split unless later
  evidence establishes that they are needed.

Mapping is traceability and does not grant authority to reinterpret the source Design/WorkRegister.

## Handoff rule

Build should not need Decisions/design-history material to reconstruct the required result. Include work-specific authoritative artefacts needed for execution; do not duplicate generic execution/platform knowledge already supplied by the Build environment.

## Build authority

Build may choose ordinary implementation detail within Authorised Scope. It must return rather than silently change Objective, major scope, Acceptance, architecture/policy, or a decision explicitly reserved to the work owner.

## Review

Where the WorkPackage specifies plan/result Review, execute it under `AIDE_Review`; do not invent a WorkPackage-specific review method.

An omitted Review field does not disable governing Review requirements supplied by another applicable Standard/workflow.

## Execution

1. Validate inputs, authority, and any supplied WorkRegister mapping; for a deliberately split source obligation, require independently identifiable required changes and unambiguous `Covers`.
2. Establish a proportionate plan.
3. Complete applicable pre-execution Review.
4. Execute within scope.
5. Validate against Acceptance.
6. Complete applicable result Review.
7. Return a truthful Outcome.

Do not claim completion solely because an artefact was produced.

## Out-of-scope discovery

Report useful out-of-scope findings; do not action them under the current authority without explicit re-scope/new work.

## Outcome

Return:

```yaml
Outcome:
  Status: Complete | Partial | Blocked | Failed
  WorkPerformed: <summary>
  Outputs: <produced/changed artefacts or state>
  Validation: <acceptance evidence/results>
  Reviews: <where applicable>
  Deviations: <authorised exceptions/differences>
  Remaining: <unresolved/remaining work>
  OutOfScope: <reported findings>
  DesignFeedback: <questions/follow-up>
  WorkRegisterResults: <per mapped item/portion result, evidence and remaining work where applicable>
```

The persisted record may use concise document sections rather than YAML. For mapped WorkRegister work, report each item/covered portion as `Complete | Partial | Blocked | Failed`, with enough evidence and remaining-work detail for the owning/directing process to reconcile the source register. Build does not silently close the register.

## Partial/failure behaviour

Preserve successful work only where the resulting state is safe and accurately reportable. Do not hide partial completion. A retry/resumption starts from the actual returned state and must avoid duplicate side effects where practical.

## Lifecycle

`Defined → Ready → Executing → Returned → Reconciled/Archived`. `Reconciled` includes source WorkRegister reconciliation where mapping exists.

Documentation Methodology owns the file naming/archive mechanics; this Standard owns the WorkPackage execution semantics.

```yaml
MigrationSummary:
  CurrentVersion: v3
  LatestRequiredVersion: none
  LatestOnUpdateVersion: none

Transition:
  Version: v1
  Posture: None

Transition:
  Version: v2
  Posture: None

Transition:
  Version: v3
  Posture: None
```

---
Dependencies: !AIDE_DocumentationMethodology@v21, Build_WorkPackage_Design_v3, AIDE_Review@v1
References: AIDE_Build@v5, AIDE_ProjectDesign@v2
