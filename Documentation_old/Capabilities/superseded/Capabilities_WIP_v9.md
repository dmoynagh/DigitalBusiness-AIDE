# Capabilities — WIP

> **Version 9** (2026-09-01). Review B R1 remediation and pre-Round-2 corrections are applied.
> The focused Round 2 Inspect / High / Full request is prepared for relay against the remediated
> current source set; relay has not yet been confirmed.

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

`Continuing — Round 2 request prepared; relay not yet confirmed`

## Review B Round 1

```text
Type: Robust
Level: High
Mode: Full
Lead: GPT
Reviewer: Claude
Actual reviewer model: Claude Opus 5
Response status: Complete
Assessment: Coherent with targeted changes
```

Messaging:

```text
R1 request:
  aide-architecture-review-b-documentation-work-state/gpt/001 @ GPT_v1

R1 response:
  aide-architecture-review-b-documentation-work-state/claude/001 @ Claude_v1

R1 Lead disposition:
  aide-architecture-review-b-documentation-work-state/gpt/002 @ GPT_v1
```

Accepted R1 remediation was routed to Documentation Methodology, Working Practices, Project Design
and Build/WorkPackage.

## Remediation now applied

Current Round 2 owner sources:

1. `DocumentationMethodology_Binder_v6.md`
   - current Documentation Methodology v25;
   - implements WorkRegister admission, WIP thread exit, Working discovery, owner-seam cleanup,
     returned-pending reconciliation, compact Outcome referencing, split-obligation treatment and
     negative OpenItem closure;
   - pre-Round-2 correction aligns the coordinated split-obligation seam to
     `AIDE_WorkPackage@v3`.

2. `WorkingPractices_Binder_v3.md`
   - implements operational/semantic ownership cleanup;
   - deferred Project Handoff incorporation is held by one concise destination OpenItem.

3. `ProjectDesign_Binder_v3.md`
   - current Project Design v4;
   - Design→WorkRegister remains a mandatory producer rule rather than the whole WorkRegister
     admission definition;
   - current Build handoff targets `AIDE_WorkPackage@v3`;
   - returned-but-unreconciled mapped Outcomes preserve compact
     `Returned — reconciliation pending`.

4. `Build_Binder_v5.md`
   - current `AIDE_Build@v5` / `AIDE_WorkPackage@v3`;
   - deliberately split WorkRegister obligations require independently identifiable required changes
     and exact `Covers` mapping without structured sub-obligation IDs.

The substantive R1 remediation has therefore been applied across all four semantic owners.

## R1 disposition preserved

### Accepted changes

- RB-R1-F1 — WorkRegister admission clarified.
- RB-R1-F2 — WIP per-thread exit added.
- RB-R1-F3 — Working live-series discovery added.
- RB-R1-F4 — Documentation Methodology / Working Practices ownership seam cleaned up.
- RB-R1-F5 — returned-but-unreconciled state made explicit.
- RB-R1-F6 — deferred Project Handoff continuity uses one destination OpenItem.

### Accepted clarifications

- RB-R1-F7 — WorkRegister keeps compact reconciliation state; Outcome owns detailed evidence.
- RB-R1-F8 — split obligations use independently identifiable portions + exact WorkPackage `Covers`.
- RB-R1-F9 — material reusable negative conclusions are preserved before OpenItem removal.

### Partial/deferred

- RB-R1-F10 — concrete active WorkPackage references affected by R1 were corrected.
- General in-body version-reference versus dependency/conformance semantics remains deferred to
  Review C / Dependencies.

## Review C carried observations

Keep outside Review B:

1. Review A:
   documentation-conformance checkpoint versus functional dependency/cycle semantics.
2. Review B F10:
   general relationship between in-body versioned capability references and dependency/conformance
   checkpoints.

## Round 2 posture

```text
Type: Inspect
Level: High
Mode: Full
Lead: GPT
Reviewer: Claude
Requested reviewer model: Claude Opus 5 if available
```

Purpose:

Verify the applied R1 remediation against the current artefacts and determine whether Review B can
complete at High.

Do not repeat the full R1 simplification challenge.

Primary Round 2 focus:

- WorkRegister admission and OpenItems boundary;
- WIP per-thread exit + Working discovery;
- Project Handoff receipt/reconciliation continuity;
- Documentation Methodology / Working Practices owner-boundary cleanup;
- WorkRegister / WorkPackage / Outcome returned-pending and evidence boundary;
- split-obligation `Covers` mapping;
- negative OpenItem closure/history sufficiency;
- multiple top-level topics sharing one container.

## Outbound Round 2 message

Prepared identity:

```text
Thread: aide-architecture-review-b-documentation-work-state
Message-ID: aide-architecture-review-b-documentation-work-state/gpt/003
Version: GPT_v1
```

Status:

`Prepared — not yet confirmed relayed`

## Current Review B source set for Claude

Send:

1. `DocumentationMethodology_Binder_v6.md`
2. `WorkingPractices_Binder_v3.md`
3. `ProjectDesign_Binder_v3.md`
4. `Build_Binder_v5.md`
5. `Capabilities_WIP_v9.md`
6. `Capabilities_OpenItems_v15.md`
7. `Capabilities_WorkRegister_v15.md`

Use the existing Claude Review B chat so the R1 exchange remains available.

Do not send the temporary Standards/Tools Bundle as Review B authority.

## Next action

1. Replace `Capabilities_WIP_v8` with this v9 checkpoint in current Capabilities live context.
2. In the existing Claude Review B chat, attach/supply the seven current Round 2 sources.
3. Relay `aide-architecture-review-b-documentation-work-state/gpt/003 @ GPT_v1`.
4. Do not mark `Awaiting Response` until relay is actually confirmed.
5. On Claude return:
   - correlate exact Review/Round/message identity;
   - preserve reviewer findings unchanged;
   - disposition any R2 findings as Lead;
   - if remediation survives High re-review and no material in-scope finding remains, complete
     Review B and issue its durable Review record;
   - otherwise continue only with the smallest focused remediation/round justified.
6. Do not begin Review C until Review B is Complete or explicitly escalated.

---
Dependencies: !AIDE_DocumentationMethodology@v25, AIDE_Review@v2, AIDE_Messaging@v1
References: Capabilities_WorkRegister_v15, Capabilities_OpenItems_v15, Capabilities_Architecture_Review_2026-08-31-1_CoreSubstrate_v2, DocumentationMethodology_Binder_v6, WorkingPractices_Binder_v3, ProjectDesign_Binder_v3, Build_Binder_v5
