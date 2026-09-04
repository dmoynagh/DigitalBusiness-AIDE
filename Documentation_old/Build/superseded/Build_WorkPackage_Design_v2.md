# Build WorkPackage — Design

> **Version 2** (2026-08-31). Adds explicit WorkRegister source mapping and result return so a
> WorkPackage can deliver manageable portions of confirmed outstanding obligations.
>
> Created: 2026-08-30 | Last modified: 2026-08-31

## §1 — Purpose

A WorkPackage is a bounded executable unit of defined work handed to Build. It states what Build is
authorised to do, with what inputs, for what result and how completion is established.

A WorkPackage may be created directly from defined work or may select some/all of one or more
WorkRegister obligations.

## §2 — Required contract

Every executable WorkPackage resolves:

- **Objective** — required result;
- **Authorised Scope** — what may be changed/created and explicit exclusions;
- **Inputs** — work-specific authoritative inputs;
- **Required Outputs** — artefacts/state to produce/change;
- **Acceptance** — observable completion/evidence conditions;
- **Constraints** — limits/dependencies/targets/reserved decisions;
- **Review posture** — explicit plan/result Review where applicable;
- **Return** — outcome destination/record; and
- **WorkRegister mapping** — when sourced from WorkRegister, the item IDs and covered obligation
  portion(s).

Optional context may help execution, but the package should not become a dump of design history.

## §3 — WorkRegister mapping

Conceptual representation:

```yaml
WorkRegisterItems:
  - Id: WR12
    Covers: "Comparer implementation and tests"
  - Id: WR13
    Covers: "Documentation update"
```

Equivalent prose is valid.

Rules:

- one WorkPackage may cover multiple items;
- one item may appear in several WorkPackages where delivery is deliberately chunked;
- `Covers` states the portion currently authorised where the package does not satisfy the entire
  source obligation; and
- the mapping is traceability/reconciliation input, not authority to reinterpret the WorkRegister
  or Design.

## §4 — Self-containment boundary

Build must be able to understand required result/authority without reopening Decisions history.

WorkRegister references do not substitute for a complete WorkPackage. Include the actual
work-specific Design/inputs needed for execution.

If a material design choice remains unresolved, the package is NotReady.

## §5 — Review configuration

WorkPackage may configure `AIDE_Review` independently for planning and result review. Omitted
fields resolve through governing defaults.

## §6 — Execution contract

Build shall:

1. validate required inputs/authority;
2. validate WorkRegister mappings where supplied;
3. establish a proportionate plan;
4. perform required/recommended Review;
5. execute within scope;
6. validate against Acceptance;
7. perform result Review where applicable; and
8. return truthful Outcome evidence including mapped obligation results.

Build may decide ordinary implementation detail within contract but may not silently alter the
objective, major scope, acceptance or reserved Design decisions.

## §7 — WorkPackage Outcome

Return at least:

- terminal status `Complete | Partial | Blocked | Failed`;
- work actually performed;
- produced/changed artefacts/state;
- validation/acceptance evidence;
- Reviews and material dispositions;
- deviations/authorised exceptions;
- unresolved/remaining work;
- out-of-scope findings;
- design questions/follow-up; and
- **WorkRegisterResults** when the package carried WorkRegister mapping.

Conceptual result mapping:

```yaml
WorkRegisterResults:
  - Id: WR12
    Result: Complete
    Evidence: <what proves the covered obligation was delivered>
    Remaining: None
  - Id: WR13
    Result: Partial
    Evidence: <what was completed>
    Remaining: <what is still owed>
```

Build reports these results. The owning/directing process decides how they reconcile the source
WorkRegister.

## §8 — Lifecycle

```text
Defined → Ready → Executing → Returned → Reconciled/Archived
```

`Reconciled` includes consumption of Outcome and source WorkRegister reconciliation where mapping
exists.

A blocked/partial return does not erase safe successful work; the Outcome states actual resulting
state.

---
Dependencies: !AIDE_DocumentationMethodology@v21, Build_Design_v4, AIDE_Review@v1
References: ProjectDesign_Design_v2, AIDE_DocumentationMethodology@v21
