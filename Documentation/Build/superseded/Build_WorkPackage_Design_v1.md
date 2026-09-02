# Build WorkPackage — Design

> **Version 1** (2026-08-30). Defines the generic Design-to-Build handoff, execution authority, acceptance and return contract required for operational AIDE Build work.
>
> Created: 2026-08-30 | Last modified: 2026-08-30

---

## §1 — Purpose

A WorkPackage is a bounded, executable unit of defined work handed to Build. It answers what Build is authorised to do, with what inputs, for what result, and how completion is established.

The WorkPackage is an outcome of Project Design/work direction and is not itself the place to rediscover the project's design.

## §2 — Required contract

Every executable WorkPackage resolves:

- **Objective** — the outcome the work is intended to achieve.
- **Authorised Scope** — what may be changed/created and important explicit exclusions.
- **Inputs** — work-specific authoritative artefacts/information required for execution.
- **Required Outputs** — artefacts/state the package must produce or change.
- **Acceptance** — observable conditions/evidence used to judge completion.
- **Constraints** — applicable limits, dependencies, environment/target requirements, or reserved decisions.
- **Review posture** — any required/recommended plan or result Review; otherwise the normal Build/Review defaults apply.
- **Return** — where/how the WorkPackage Outcome is to be delivered or recorded.

Optional context may be included where it materially helps execution, but the WorkPackage should not become a dump of design history.

## §3 — Self-containment boundary

A WorkPackage is complete when Build can understand the required result and authority without reopening Decisions or other design-history material.

Self-containment does **not** require copying generic platform/toolchain knowledge already available to the Build environment through applicable Standards, Tools or references.

If a material design choice is unresolved, the package is NotReady rather than granting Build authority to invent it.

## §4 — Review configuration

WorkPackage may configure Review separately for planning and completed execution using `AIDE_Review`:

```yaml
Review:
  Plan:
    Posture: Required | Recommended | Optional | None
    Type: <profile where specified>
    Level: <level where specified>
    Mode: <mode where specified>
  Result:
    Posture: Required | Recommended | Optional | None
    Type: <profile where specified>
    Level: <level where specified>
    Mode: <mode where specified>
```

Omitted Type/Level/Mode values resolve through the governing Review defaults. WorkPackage does not define another Type/Level system.

A domain may use a higher-level tier to generate this explicit posture, but tier semantics are domain/workflow policy unless separately standardised.

## §5 — Execution contract

Build must:

1. validate that required WorkPackage inputs are available and mutually coherent;
2. identify any material ambiguity before consequential execution;
3. establish a proportionate execution plan;
4. perform required/recommended Review according to governing posture;
5. execute within authorised scope using applicable Standards/Tools;
6. validate the actual result against Acceptance;
7. perform result Review where required/recommended; and
8. return the Outcome truthfully.

Build may resolve implementation details inside the contract. It may not silently alter Objective, Authorised Scope, Acceptance or a reserved design decision.

## §6 — Out-of-scope discoveries

Useful issues discovered outside Authorised Scope are reported in the Outcome and not executed under the current WorkPackage unless the work owner explicitly re-scopes the package or creates separate work.

## §7 — WorkPackage Outcome

The Outcome records at least:

- terminal status: `Complete | Partial | Blocked | Failed`;
- summary of work actually performed;
- produced/changed artefacts or state;
- acceptance/validation evidence and failures;
- Reviews performed and material resulting dispositions where applicable;
- deviations/authorised exceptions;
- unresolved items and remaining work;
- out-of-scope findings; and
- design questions/follow-up required.

The Outcome may be held in the active WorkPackage and folded into it on archival under Documentation Methodology v17.

## §8 — Lifecycle

```text
Defined → Ready → Executing → Returned → Reconciled/Archived
```

- **Defined** — work is being authored; not yet executable.
- **Ready** — required contract is resolved and execution is authorised.
- **Executing** — Build owns active execution within scope.
- **Returned** — an Outcome has been produced.
- **Reconciled/Archived** — the director of work has consumed the Outcome; further work, if any, is a new/revised WorkPackage.

A blocked package may return without being complete. Re-authorisation after a design change produces a new executable state rather than silently pretending the original contract never changed.

---
Dependencies: !AIDE_DocumentationMethodology@v18, Build_Design_v1, AIDE_Review@v1
References: ProjectDesign_Design_v1
