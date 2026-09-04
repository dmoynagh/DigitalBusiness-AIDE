# Capabilities — WIP

> **Version 8** (2026-09-01). Review B Round 1 is complete. Lead dispositions are settled and
> accepted remediation is being routed to Documentation Methodology, Working Practices,
> Project Design and Build/WorkPackage before High re-review.

## Current position

Programme:

`AIDE Architecture — Peer Review Programme`

WorkRegister:

`WR17 — Peer-review major Capabilities architecture slices`

Completed slice:

`Review A — Core substrate` — Complete at High.

Active slice:

`Review B — Documentation/work-state model`

Review identity:

`AIDE-Architecture-Review-B-Documentation-Work-State`

Current lifecycle state:

`Continuing — Round 1 complete; accepted remediation pending`

## Review B Round 1

```text
Type: Robust
Level: High
Mode: Full
Lead: GPT
Reviewer: Claude
Actual reviewer model: Claude Opus 5
Response status: Complete
```

Messaging:

```text
Request:
  aide-architecture-review-b-documentation-work-state/gpt/001 @ GPT_v1

Response:
  aide-architecture-review-b-documentation-work-state/claude/001 @ Claude_v1

Lead disposition prepared:
  aide-architecture-review-b-documentation-work-state/gpt/002 @ GPT_v1
```

The Claude response assessed the integrated model as:

`Coherent with targeted changes`

No Review A/Core reopening was proposed.

## Lead disposition summary

### Change / accepted

- **RB-R1-F1 — WorkRegister admission**
  - general rule: confirmed work owed by the owning top-level topic and not yet fully delivered;
  - excludes ideas/unconfirmed/unresolved possible work;
  - Project Design's Design→WorkRegister hard consequence rule remains mandatory but is a producer
    rule, not the whole admission boundary.
- **RB-R1-F2 — WIP per-thread exit**
  - routed active-thread sections are removed from subsequent WIP checkpoints;
  - whole WIP is withdrawn when no continuation thread remains.
- **RB-R1-F3 — Working discovery**
  - live Working series receive a version-agnostic Index `Live state` locator;
  - Working versions do not force Index churn and remain outside Binder.
- **RB-R1-F4 — DocMeth / Working Practices seam**
  - one normative owner per rule; semantic/lifecycle rules stay DocMeth, operational handling stays
    Working Practices.
- **RB-R1-F5 — Returned / not reconciled**
  - when reconciliation cannot complete in the same uninterrupted step, record compact
    `Returned — reconciliation pending` state before leaving context.
- **RB-R1-F6 — received Project Handoff**
  - if not reconciled in the same pass, destination creates one concise OpenItem until incorporated.

### Clarify / accepted

- **RB-R1-F7**
  - WorkRegister keeps compact result/reference/remaining state; detailed evidence remains Outcome.
- **RB-R1-F8**
  - split obligations use independently identifiable required changes and exact `Covers` mapping;
    no structured sub-obligation IDs.
- **RB-R1-F9**
  - material negative/no-change conclusions that could credibly be re-raised are preserved in
    Decisions/appropriate durable owner before OpenItem removal.

### Change in part / defer in part

- **RB-R1-F10**
  - correct concrete stale in-body contract references encountered during Review B remediation;
  - general versioned in-body reference policy is deferred to Review C / Dependencies.

## Simplification disposition

Preserve as separate:
- WIP and Working;
- WIP and OpenItems;
- WorkRegister and WorkPackage;
- WorkPackage Outcome;
- Working.

OpenItems + WorkRegister merge:

`Deferred to Review E — integrated coherence`

No separate work item is created; WR17 already owns Review E.

## Remediation ownership

Prepared Project Handoffs:

1. Documentation Methodology
   - F1, F2, F3, F4, F5, F7, F8 coordination, F9, concrete part of F10.
2. Working Practices
   - F4, F6, concrete stale-reference maintenance from F10.
3. Project Design
   - F1 producer-rule refinement; return/reconciliation alignment.
4. Build / WorkPackage
   - F8 mapping clarification; otherwise preserve Build/Outcome boundary.

These are transfer/reconciliation artefacts. No destination master is considered changed until the
owning project applies its handoff against its current authoritative baseline.

## Review C carried observations

Carry both into Review C / Dependencies:

1. Review A observation:
   documentation-conformance checkpoint versus functional dependency/cycle semantics.
2. Review B F10 general question:
   how versioned in-body capability references relate to dependency/conformance checkpoint
   semantics and whether current-instruction prose should normally use versionless identities.

Do not resolve either as part of Review B beyond concrete stale-reference correction.

## Round 2 posture

After accepted remediation is applied and current replacement Binders are available:

```text
Type: Inspect
Level: High
Mode: Full
Reviewer: Claude
Requested model: Claude Opus 5 if available
```

Round 2 should concentrate on:
- WorkRegister admission and OpenItems boundary;
- WIP per-thread exit + Working discovery together;
- Project Handoff receipt/reconciliation;
- Documentation Methodology / Working Practices owner-boundary cleanup;
- WorkRegister/WorkPackage return and split-coverage seams where remediated.

Do not re-run the full simplification challenge.

## Next action

1. Relay the prepared Lead disposition message `gpt/002` to the existing Claude Review B chat.
2. Apply the four Project Handoffs in their owning project chats against current authoritative
   Binders/masters.
3. Return/apply the resulting Change Delivery Packages.
4. Bring the new current Binders back to this Capabilities Review B Lead chat.
5. Construct and relay Round 2 Inspect / High / Full.
6. Do not begin Review C until Review B is Complete or explicitly escalated.

---
Dependencies: !AIDE_DocumentationMethodology@v23, AIDE_Review@v2, AIDE_Messaging@v1
References: Capabilities_WorkRegister_v15, Capabilities_OpenItems_v15, Capabilities_Architecture_Review_2026-08-31-1_CoreSubstrate_v2, DocumentationMethodology_Binder_v4, WorkingPractices_Binder_v2, ProjectDesign_Binder_v1, Build_Binder_v4
