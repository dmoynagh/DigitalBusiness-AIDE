# Capabilities Architecture — Review — Core Substrate

> **Review checkpoint v1** (2026-08-31). Records Review A Round 1 and Lead dispositions. Review is
> continuing; this is not the final Review Result.

Review: `AIDE-Architecture-Review-A-Core-Substrate`
Round checkpoint: R1 complete
State: Continuing
Type: Robust
Level: High
Mode: Full
Lead: GPT
Reviewer: Claude
Reviewer model: Claude Opus 5

## Subject

Current AIDE Core substrate after the 2026-08-31 Foundation consolidation:

- generic Index;
- Item / Item Type;
- runtime Item Type recognition;
- Domain authority and recognition;
- Domain propagation stop;
- Bootstrap/Profile/Contribution; and
- the Core/Documentation Methodology semantic Item Type seam.

## Objective

Determine whether the substrate is conceptually sound, proportionate and operable; whether authority
and ownership compose cleanly; and whether a materially smaller/stronger design exists before
platform-specific Build/Deployment work proceeds.

## Authoritative Round 1 material

- `Core_Binder_v1.md`
- `DocumentationMethodology_Binder_v2.md` — seam testing only

## Messaging correlation

Request:

```text
Thread: aide-architecture-review-a-core-substrate
Message-ID: aide-architecture-review-a-core-substrate/gpt/001
Version: GPT_v1
Round: R1
```

Reviewer response:

```text
Thread: aide-architecture-review-a-core-substrate
Message-ID: aide-architecture-review-a-core-substrate/claude/001
Version: Claude_v1
In-Reply-To: aide-architecture-review-a-core-substrate/gpt/001 @ GPT_v1
Reviewer model: Claude Opus 5
Review status: Complete
```

The complete reviewer response was received in the Review coordination chat and remains the
authoritative Reviewer-owned Round 1 Finding text. The Finding text is not rewritten by these Lead
dispositions.

## Reviewer overall assessment

Reviewer assessed the Index/Item/Item-Type/Domain decomposition as close to minimal and materially
stronger than the earlier architecture, especially:

- registration authority separated from item-internal authority;
- optional enumeration / self-describing delegation;
- restricted Domain authority;
- fail-visible Domain ambiguity;
- `No Domain` as valid;
- composable Item Types without inheritance.

The primary weakness was incomplete reconciliation of the Domain v2 move from literal structural
kinds to semantic recognition, plus duplicated/unowned runtime recognition projections and several
Bootstrap activation ambiguities.

## Round 1 Findings and Lead dispositions

| Finding | Disposition | Lead result |
|---|---|---|
| RA-R1-F1 — Domain-approved semantic type set absent; Solution/Project ownerless | Change | Publish Domain-owned approved recognition set in Domain Standard; use semantic Item Types where a genuine owner exists; Domain owns minimum native Solution/Project recognition. |
| RA-R1-F2 — generic Index reintroduced as Domain root | Change | Remove generic Index from Domain-defining examples/schema; use `DocumentationTopic` for documentation roots. |
| RA-R1-F3 — Propagation Stop can expose nested Domain | Change | State that Stop removes enclosing Domain and independent resolution may find another Domain; define no parent/child semantics. |
| RA-R1-F4 — Stop representation unavailable for unregistered boundary | Change | Limit v3 Stop to recognised/registered Domain-aware boundaries; no new generic marker file; specify upward discovery of parent-hosted Stop. |
| RA-R1-F5 — two derived runtime registries | Change | Remove separate DomainRecognitionRegistry; keep domain-neutral ItemTypeRegistry; Domain separately applies Domain-owned approved recognition set. |
| RA-R1-F6 — no registry production/freshness owner | Change | Treat compiled recognition as optional derived optimisation; direct authoritative recognition is supported fallback; persisted form uses normal Build provenance. |
| RA-R1-F7 — Contributions not gated by Profile | Change | Effective Profile defines startup set and gates Contributions; no Profile does not activate all deployed Contributions. |
| RA-R1-F8 — DocumentationTopic file/boundary ambiguity; subtopics | Change in part | Clarify Item as logical top-level-topic boundary declared by Index file; decline promotion of subtopics to DocumentationTopic. |
| RA-R1-F9 — explicit Domain root Type half-designed | Change | Keep expected-recognition assertion; independently validate observed recognition; mismatch fails. |
| RA-R1-F10 — two Domain metadata hosts | Change | Explicit Domain entry is sole Domain metadata/settings host where it governs/composes the Domain. |
| RA-R1-F11 — Bootstrap Why may become applicability | Change | `Why` is non-executable rationale; no second Scope system. |
| RA-R1-F12 — undefined Contribution ordering | Change | Contributions are order-independent; no startup ordering engine. |
| RA-R1-F13 — Document Register/current-version drift | Decline | Evidence did not establish register drift; dependency checkpoint/reference versions may be intentionally lower/specific. |
| RA-R1-F14 — bootstrap recognition vs Item Type recognition | Change (clarification) | `{bootstrap}` deliberately remains primitive pre-Index discovery; do not unify. |

## Protected constraint from Lead/user

Runtime-registry simplification must never weaken the Domain authority boundary.

Canonical intent:

```text
External Item Type owner
    may define Identify + Provides
    cannot declare itself Domain-capable

AIDE_Domain
    publishes the approved Domain recognition set
    exclusively determines which semantic types/native structures may establish or participate in
    Domain resolution
```

The shared `ItemTypeRegistry` is domain-neutral. Domain applies its approved set after semantic type
recognition.

## Remediation packages produced at this checkpoint

- `Core_ReviewA_R1_ChangeDelivery_Instructions_2026-08-31.md`
- `DocumentationMethodology_ReviewA_R1_ChangeDelivery_Instructions_2026-08-31.md`

The Documentation Methodology package also incorporates the previously confirmed queued root-WIP
rule because this is the next normal substantive Documentation Methodology pass.

## Current Review state

```yaml
ReviewState:
  ReviewId: AIDE-Architecture-Review-A-Core-Substrate
  State: Continuing
  Type: Robust
  Level: High
  Mode: Full
  Rounds:
    - R1:
        Reviewer: Claude
        Model: Claude Opus 5
        Status: Complete
        LeadDispositions: Complete
  Remediation:
    Definition: Complete
    AuthoritativeApplication: Pending
  ReReview:
    Required: true
    Reason: High-level substantive Review-driven changes
```

## Planned Round 2

After revised authoritative Binders exist:

- `Core_Binder_v2.md`
- `DocumentationMethodology_Binder_v3.md`

run focused Review A R2 against the changed material.

Recommended R2 posture:

```text
Type: Inspect
Level: High
Mode: Full
```

Objective: verify that the R1 remediation actually resolves the Findings without new contradictions,
with particular focus on Domain authority/recognition, removal of duplicate registry machinery,
Propagation Stop, and Bootstrap Profile gating.

Do not start Review B until Review A has completed or been explicitly escalated/accepted otherwise.

---
Dependencies: !AIDE_DocumentationMethodology@v21, AIDE_Review@v2, AIDE_Messaging@v1
References: Core_Binder_v1, DocumentationMethodology_Binder_v2, Capabilities_WorkRegister_v14
