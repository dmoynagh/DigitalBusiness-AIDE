# Capabilities — WIP

> **Version 7** (2026-09-01). Review B preflight is complete: current cross-project sources are
> resolved, the Round 1 posture is set to Robust / High / Full, and the Claude request is prepared
> for manual relay. Relay has not yet been confirmed.

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

`Initiated — Round 1 request prepared; relay not yet confirmed`

Do not mark the Review `Awaiting Response` until the request is actually relayed.

## Review B Round 1 posture

```text
Type: Robust
Level: High
Mode: Full
Lead: GPT
Reviewer: Claude
Requested reviewer model: Claude Opus 5 if available
Actual reviewer model: record from returned response
```

Rationale: Review B is explicitly testing whether the current state taxonomy and ownership model
is the right design and whether materially simpler designs preserve the same guarantees. The
architecture has broad downstream reach and state-loss/duplication mistakes are difficult to
reverse once embedded in normal work, so High remains proportionate.

## Resolved authoritative Review inputs

Primary Review subject material:

1. `DocumentationMethodology_Binder_v4.md`
   - current Documentation Methodology v23 corpus;
   - owner of document/work-state type semantics, lifecycle, topic anchoring and Binder/live-state
     distinction.
2. `WorkingPractices_Binder_v2.md`
   - current practical persistence, checkpoint, cross-project Handoff and repository/context
     handling conventions.
3. `ProjectDesign_Binder_v1.md`
   - current Design commitment → WorkRegister consequence and return/reconciliation semantics.
4. `Build_Binder_v4.md`
   - current WorkPackage v2 / Build v4 mapping, Outcome evidence and source-WorkRegister return
     semantics.
5. `Capabilities_WIP_v7.md`
   - current volatile programme/continuation state and Review B checkpoint; live, non-authoritative
     architecture state.
6. `Capabilities_OpenItems_v15.md`
   - current concrete live-attention example.
7. `Capabilities_WorkRegister_v15.md`
   - current concrete WorkRegister example and WR17 programme ownership.

Core seam verification uses current `Core_Binder_v3.md` only for these settled facts:

- `DocumentationTopic` is the logical top-level-topic documentation boundary/scope; its governing
  Index declares/describes it.
- chat project/master folder/workspace boundaries are context/storage containers rather than
  semantic ownership boundaries and may host one or several top-level topics.
- standing workflow registers anchor to the top-level topic by default unless their owner defines
  a justified narrower scope.

The full Core substrate is not a Review B subject and Review A is not reopened without a concrete
material cross-slice contradiction.

## Governing Review/transport contracts

Use the current contracts represented by:

- `Capabilities_Binder_Review_v2.md` — `AIDE_Review@v2`, Review Profiles v1 and Review Tool v2;
- `Capabilities_Binder_Messaging_v1.md` — `AIDE_Messaging@v1` and Messaging Tool v1.

These govern the Review exchange; they are not themselves Review B architecture subjects except
where the Review/work-state persistence seam directly requires them.

## Excluded/stale material

Do not use as current Review B semantic authority:

- temporary `AIDE_Bundle_StandardsTools_v5` where the current Binders above establish newer state;
- older Documentation Methodology, Working Practices, Project Design, Build or Core Binders;
- the former normal `Capabilities_Binder_Work` route for live state;
- superseded WIP checkpoints.

Keep the Review A observation about Documentation Methodology conformance checkpoints versus
functional dependency/cycle semantics reserved for Review C — Dependencies.

## Lead preflight attack points

Review B should particularly test:

- whether the Documentation Methodology / Working Practices semantic-versus-operational ownership
  split composes cleanly or requires duplicated rules;
- whether WIP versus Working has an operationally reliable threshold rather than merely a conceptual
  distinction;
- whether WIP versus OpenItems permits safe promotion without durable duplicate truth;
- whether OpenItems versus WorkRegister has a crisp enough boundary between unresolved attention and
  confirmed undelivered Design obligation;
- whether WorkRegister many-to-many WorkPackage mapping preserves obligation truth without copying
  the same contract into both layers;
- whether WorkPackage Outcome evidence and the open WorkRegister row duplicate returned state more
  than necessary;
- whether removing completed WorkRegister/OpenItems rows still leaves sufficient durable history in
  Design/Decisions/WorkPackage Outcome and other authoritative evidence;
- whether stable Binders plus separately loaded live files form a proportionate resume/currentness
  contract when a top-level topic has several active threads;
- whether Project Handoff cleanly transfers knowledge into the owning project without becoming
  another competing work-state ledger; and
- what materially simpler state model, if any, preserves the same continuity, traceability,
  authority and reconciliation guarantees.

## Outbound Round 1 message

Prepared identity:

```text
Thread: aide-architecture-review-b-documentation-work-state
Message-ID: aide-architecture-review-b-documentation-work-state/gpt/001
Version: GPT_v1
```

Status:

`Prepared — not yet confirmed relayed`

## Next action

Relay the prepared Round 1 AI-MESSAGE and the resolved primary Review inputs to Claude.

On return:

1. correlate the response to the exact Review/Round/Message identity;
2. record actual Reviewer model and response status;
3. disposition material Findings as Lead before any owner-project master changes;
4. route accepted findings through Project Handoff / Change Delivery to their semantic owners;
5. update this WIP with confirmed relay/response/continuation state; and
6. because Level is High, return substantive Review-driven remediation for re-review before
   completing Review B.

Do not begin Review C until Review B is Complete or explicitly escalated.

---
Dependencies: !AIDE_DocumentationMethodology@v23, AIDE_Review@v2, AIDE_Messaging@v1
References: Capabilities_WorkRegister_v15, Capabilities_OpenItems_v15, Capabilities_Architecture_Review_2026-08-31-1_CoreSubstrate_v2, DocumentationMethodology_Binder_v4, WorkingPractices_Binder_v2, ProjectDesign_Binder_v1, Build_Binder_v4, Core_Binder_v3
