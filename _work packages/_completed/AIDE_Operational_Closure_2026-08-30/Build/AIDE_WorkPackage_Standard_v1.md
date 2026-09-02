# AIDE WorkPackage — Standard

> **Identity:** `AIDE_WorkPackage@v1`
> **Common name:** WorkPackage
> **Version 1** (2026-08-30). Initial generic Design-to-Build handoff and Build Outcome contract.
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
```

Equivalent clear prose/sections are valid; the semantic fields matter, not this physical rendering.

If a material field is unresolved and cannot safely be inferred from authoritative inputs, the WorkPackage is NotReady.

## Handoff rule

Build should not need Decisions/design-history material to reconstruct the required result. Include work-specific authoritative artefacts needed for execution; do not duplicate generic execution/platform knowledge already supplied by the Build environment.

## Build authority

Build may choose ordinary implementation detail within Authorised Scope. It must return rather than silently change Objective, major scope, Acceptance, architecture/policy, or a decision explicitly reserved to the work owner.

## Review

Where the WorkPackage specifies plan/result Review, execute it under `AIDE_Review`; do not invent a WorkPackage-specific review method.

An omitted Review field does not disable governing Review requirements supplied by another applicable Standard/workflow.

## Execution

1. Validate inputs and authority.
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
```

The persisted record may use concise document sections rather than YAML.

## Partial/failure behaviour

Preserve successful work only where the resulting state is safe and accurately reportable. Do not hide partial completion. A retry/resumption starts from the actual returned state and must avoid duplicate side effects where practical.

## Lifecycle

`Defined → Ready → Executing → Returned → Reconciled/Archived`.

Documentation Methodology owns the file naming/archive mechanics; this Standard owns the WorkPackage execution semantics.

---
Dependencies: !AIDE_DocumentationMethodology@v18, Build_WorkPackage_Design_v1, AIDE_Review@v1
References: AIDE_Build@v1, AIDE_ProjectDesign@v1
