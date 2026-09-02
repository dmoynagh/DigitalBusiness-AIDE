# Capabilities Architecture — Review — Core Substrate

> **Review record v2** (2026-09-01). Final durable result for Review A. Supersedes the R1-only
> checkpoint v1 while preserving the complete Review lifecycle, Findings/dispositions, remediation
> and final verification outcome.

Review: `AIDE-Architecture-Review-A-Core-Substrate`
State: Complete
Outcome: Complete
Final level: High
Mode: Full
Lead: GPT
Reviewer: Claude
Reviewer model: Claude Opus 5

## Subject

AIDE Core substrate:

- generic Index;
- Item / Item Type;
- runtime Item Type recognition;
- Domain authority and recognition;
- Domain Propagation Stop;
- Bootstrap/Profile/Contribution; and
- the Core/Documentation Methodology `DocumentationTopic` seam.

## Objective

Determine whether the Core substrate is conceptually sound, proportionate and operable; whether
authority and ownership compose cleanly; and whether a materially smaller/stronger design exists
before platform-specific Build/Deployment work proceeds.

## Review history

### Round 1

```text
Type: Robust
Level: High
Mode: Full
Reviewer: Claude
Actual reviewer model: Claude Opus 5
```

Authoritative material:

- `Core_Binder_v1.md`
- `DocumentationMethodology_Binder_v2.md` — seam testing

Messaging:

```text
Request:  aide-architecture-review-a-core-substrate/gpt/001 @ GPT_v1
Response: aide-architecture-review-a-core-substrate/claude/001 @ Claude_v1
Effective Lead disposition:
          aide-architecture-review-a-core-substrate/gpt/002 @ GPT_v2
```

R1 identified fourteen Findings. The Lead accepted/changed the architecture on F1–F12 and F14,
declined F13, and issued coordinated Core + Documentation Methodology remediation.

### Round 2

```text
Type: Inspect
Level: High
Mode: Full
Reviewer: Claude
Actual reviewer model: Claude Opus 5
```

Authoritative material:

- `Core_Binder_v2.md`
- `DocumentationMethodology_Binder_v4.md`

Messaging:

```text
Request:     aide-architecture-review-a-core-substrate/gpt/003 @ GPT_v1
Response:    aide-architecture-review-a-core-substrate/claude/002 @ Claude_v1
Disposition: aide-architecture-review-a-core-substrate/gpt/004 @ GPT_v1
```

R2 was a focused High-level remediation verification rather than another blank-sheet Robust review.

Claude assessed:

- RA-R1-F1 through RA-R1-F12 — Resolved;
- RA-R1-F13 — Superseded / Not Applicable under the Lead Decline;
- RA-R1-F14 — Resolved.

Claude found no remaining structural defect in the R1 architecture remediation and raised three
narrow R2 Findings.

## R1 Finding dispositions and final state

| Finding | Lead disposition | Final state |
|---|---|---|
| RA-R1-F1 — Domain-approved recognition set / Solution + Project ownership | Change | Resolved and verified in R2 |
| RA-R1-F2 — generic Index as Domain root | Change | Resolved and verified in R2 |
| RA-R1-F3 — Stop and independent Domain below | Change | Resolved and verified in R2 |
| RA-R1-F4 — Stop representation/traversal | Change | Resolved as dispositioned; R2 exposed boundary-membership ambiguity handled by RA-R2-F1 |
| RA-R1-F5 — duplicate registries / Domain authority | Change | Resolved and verified in R2 |
| RA-R1-F6 — registry production/provenance | Change | Resolved and verified in R2 |
| RA-R1-F7 — Contributions gated by Profile | Change | Resolved and verified in R2 |
| RA-R1-F8 — DocumentationTopic identity/subtopics | Change in part | Resolved and verified in R2 |
| RA-R1-F9 — explicit root recognition field | Change | Resolved and verified in R2 |
| RA-R1-F10 — Domain metadata/settings host | Change | Explicit case resolved; implicit-host residual handled by RA-R2-F2 |
| RA-R1-F11 — Bootstrap Profile `Why` | Change | Resolved and verified in R2 |
| RA-R1-F12 — Bootstrap ordering | Change | Resolved and verified in R2 |
| RA-R1-F13 — Document Register/current-version drift | Decline | Superseded / Not Applicable; Reviewer accepted the Decline in R2 |
| RA-R1-F14 — `{bootstrap}` vs Item Type recognition | Change — clarification | Resolved and verified in R2 |

## R2 Findings and Lead dispositions

### RA-R2-F1 — Stop boundary membership

**Disposition:** Change.

The inclusive interpretation was selected.

`Propagation: Stop` takes effect at the marked recognised/registered structural boundary itself.
The enclosing effective Domain is removed from:

- the marked boundary; and
- all content within/below that boundary.

The marked boundary and its contained region then resolve independently as one stopped region.

A parent Index may host the Domain-owned Stop property on that boundary's registration, but the
parent Index is only the property host and is not itself the stopped boundary.

**Final verification:** Applied in `Core_Binder_v3` / `AIDE_Domain@v4`.

### RA-R2-F2 — implicit Domain settings host

**Disposition:** Change.

Implicit Domain settings use unique-host eligibility rather than precedence:

- an Index is eligible only where it is the governing Index of an approved semantic recognised root
  establishing/participating in the Domain;
- parent/repository registration alone grants no settings-host authority;
- one unambiguous eligible authoritative host is required where settings are needed;
- if no unique eligible host exists, use explicit `AIDE_Domain.yaml`;
- native Solution/Project-only implicit Domains do not acquire arbitrary Index host authority; and
- competing eligible hosts fail visibly rather than merging/ranking/using discovery order.

**Final verification:** Applied in `Core_Binder_v3` / `AIDE_Domain@v4`.

### RA-R2-F3 — historical D6 Index example

**Disposition:** Decline.

The Reviewer described D6 as an unrefined pre-refactor example. The Lead found that current Domain
Decision D34 already explicitly refines D6 (together with D5/D8/D9/D10/D15/D19/D22) wherever the
historical wording/examples used Index as literal or potentially Domain-establishing.

D34 states the current rule that generic `Index` is outside the approved Domain recognition set.

D6 therefore remains preserved historical reasoning and D34 remains its explicit current
refinement. Rewriting D6 would erase useful decision evolution.

**Final verification:** `Core_Binder_v3` retains D34's explicit refinement and does not flatten the
historical record.

## Protected authority constraint

The Review's load-bearing authority constraint remains satisfied:

```text
External Item Type owner
    may define identity + Identify + Provides
    cannot declare/acquire Domain-capable or Domain-defining authority

AIDE_Index / optional ItemTypeRegistry
    provides Domain-neutral recognition/provision optimisation only

AIDE_Domain
    publishes the approved Domain recognition set
    exclusively determines which recognised semantic/native structures may establish or
    participate in Domain resolution
```

Final verification found no route in `Core_Binder_v3` by which an external Item Type owner, generic
Index or registry entry can self-elevate into Domain authority.

## Final authoritative verification

Final completion input:

`Core_Binder_v3.md`

Verified current outcomes include:

- `AIDE_Index@v2`
- `AIDE_Domain@v4`
- `AIDE_Bootstrap@v2`
- `Core_Domain_Design_v4`
- `Core_Domain_Decisions_v4`
- `Core_System_Design_v9`

The final Lead verification confirmed:

1. Stop applies to the marked boundary and its contained region.
2. Parent Index property hosting does not make the parent the stopped boundary.
3. Stop still creates no Domain inheritance/merge/precedence/parent-child model.
4. Implicit settings-host authority is unique and deterministic.
5. Parent/repository registration alone creates no settings-host authority.
6. Native-only implicit Domains use explicit Domain representation when AIDE Domain settings are
   required.
7. Competing eligible implicit settings hosts fail visibly.
8. D6 remains historical and D34 explicitly refines it.
9. The generic `ItemTypeRegistry` remains Domain-neutral.
10. Core/Domain remains the exclusive Domain eligibility authority.
11. Index and Bootstrap child contracts were not unnecessarily reissued.
12. `AIDE_Domain@v4` uses migration posture `None`.

## Out-of-scope observation

R2 noted a possible apparent cycle if Documentation Methodology conformance checkpoints are treated
identically to functional dependencies when `AIDE_Index` and Documentation Methodology reference
each other.

No Review A action was authorised.

Carry this observation into the later Capabilities/Dependencies review slice so the Dependencies
model can test whether cycle handling must distinguish documentation-conformance checkpoint
semantics from functional dependency semantics.

## Review Result

```yaml
ReviewResult:
  ReviewId: AIDE-Architecture-Review-A-Core-Substrate
  Subject: Core substrate
  Outcome: Complete
  FinalLevel: High
  Mode: Full
  Rounds:
    - R1:
        Type: Robust
        Reviewer: Claude
        ActualModel: Claude Opus 5
        Status: Complete
    - R2:
        Type: Inspect
        Reviewer: Claude
        ActualModel: Claude Opus 5
        Status: Complete
  ReReview:
    Required: true
    Completed: true
  InScopeFindingsRemaining: none
  ResidualRisk: none material identified inside Review A scope
  OutOfScope:
    - Dependency/conformance-cycle semantics observation reserved for later Capabilities review
  CompletionReason:
    - R1 remediation survived required High re-review
    - accepted R2 determinism corrections were applied and Lead-verified
    - remaining Reviewer observation RA-R2-F3 was declined with existing Decision refinement evidence
    - another full Review A round was judged unlikely to add material value
```

## Completion

**Review A is Complete at High.**

No Round 3 is required.

The peer architecture Review programme remains open under `WR17`; the next planned slice is
**Review B — Documentation/work-state model**.

---
Dependencies: !AIDE_DocumentationMethodology@v23, AIDE_Review@v2, AIDE_Messaging@v1
References: Core_Binder_v3, DocumentationMethodology_Binder_v4, Capabilities_WorkRegister_v15
