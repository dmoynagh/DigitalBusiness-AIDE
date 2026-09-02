# Capabilities Architecture — Review — Documentation / Work-State Model

> **Review record v1** (2026-09-01). Final durable result for Review B. Preserves the complete
> two-Round Review lifecycle, R1 findings/dispositions, coordinated remediation, R2 verification,
> accepted closing corrections and final completion outcome.

Review: `AIDE-Architecture-Review-B-Documentation-Work-State`
State: Complete
Outcome: Complete
Final level: High
Mode: Full
Lead: GPT
Reviewer: Claude
Reviewer model: Claude Opus 5

## Subject

AIDE documentation/work-state architecture and the seams between:

- Documentation Methodology and Working Practices;
- WIP;
- Working;
- OpenItems;
- WorkRegister;
- Design and Decisions;
- Project Handoff;
- WorkPackage and WorkPackage Outcome;
- Binder/current-context handling;
- live state versus durable history; and
- top-level-topic ownership versus practical containers.

## Objective

Determine whether the documentation/work-state model puts the correct information at the correct
durability under the correct owner, preserves safe continuation across context loss, supports
Design→WorkRegister→WorkPackage→Outcome reconciliation without duplicate live state, and can be
materially simplified without losing continuity, traceability or governance.

## Review history

### Round 1

```text
Type: Robust
Level: High
Mode: Full
Lead: GPT
Reviewer: Claude
Actual reviewer model: Claude Opus 5
Assessment: Coherent with targeted changes
```

Primary authoritative material:

- `DocumentationMethodology_Binder_v4.md`
- `WorkingPractices_Binder_v2.md`
- `ProjectDesign_Binder_v1.md`
- `Build_Binder_v4.md`
- `Capabilities_WIP_v7.md`
- `Capabilities_OpenItems_v15.md`
- `Capabilities_WorkRegister_v15.md`

Messaging:

```text
Request:
  aide-architecture-review-b-documentation-work-state/gpt/001 @ GPT_v1

Response:
  aide-architecture-review-b-documentation-work-state/claude/001 @ Claude_v1

Lead disposition:
  aide-architecture-review-b-documentation-work-state/gpt/002 @ GPT_v1
```

R1 found ten targeted defects/clarifications. The Lead accepted the architectural direction while
refining several remedies to preserve one-owner boundaries and avoid new mechanisms.

Coordinated remediation was routed to:

- Documentation Methodology;
- Working Practices;
- Project Design; and
- Build / WorkPackage.

### Round 2

```text
Type: Inspect
Level: High
Mode: Full
Lead: GPT
Reviewer: Claude
Actual reviewer model: Claude Opus 5
Assessment: Resolved with minor clarification
Continuation recommendation: Complete Review B
```

Remediated authoritative material:

- `DocumentationMethodology_Binder_v6.md`
- `WorkingPractices_Binder_v3.md`
- `ProjectDesign_Binder_v3.md`
- `Build_Binder_v5.md`
- `Capabilities_WIP_v9.md`
- `Capabilities_OpenItems_v15.md`
- `Capabilities_WorkRegister_v15.md`

Messaging:

```text
Request:
  aide-architecture-review-b-documentation-work-state/gpt/003 @ GPT_v1

Response:
  aide-architecture-review-b-documentation-work-state/claude/002 @ Claude_v1

Lead disposition:
  aide-architecture-review-b-documentation-work-state/gpt/004 @ GPT_v1
```

R2 verified the remediated artefacts directly, tested ten integrated scenarios, and found no
remaining material architectural defect. It raised two narrow closing findings. The Lead accepted
both as non-substantive corrections and declined another Round as verification-of-verification.

## R1 Finding dispositions and final state

| Finding | Lead disposition | Final state |
|---|---|---|
| RB-R1-F1 — WorkRegister admission too narrowly described as Design consequences | Change with refinement | Resolved and verified in R2 |
| RB-R1-F2 — one topic-wide WIP lacked per-thread exit/pruning | Change | Resolved and verified in R2 |
| RB-R1-F3 — Working series could become undiscoverable outside Binder | Change | Resolved and verified in R2 |
| RB-R1-F4 — DocMeth / Working Practices duplicated normative rules | Change with owner refinement | Resolved and verified in R2 |
| RB-R1-F5 — returned-but-unreconciled WorkPackage state was invisible | Change with refinement | Resolved and verified in R2 |
| RB-R1-F6 — deferred Project Handoff had no durable continuity holder | Change proportionately | Resolved and verified in R2 |
| RB-R1-F7 — returned-result depth could duplicate Outcome evidence | Clarify | Resolved and verified in R2 |
| RB-R1-F8 — split WorkRegister obligations could map ambiguously to WorkPackages | Clarify/change proportionately | Resolved and verified in R2 |
| RB-R1-F9 — material negative OpenItem conclusions could be lost | Clarify | Resolved and verified in R2 |
| RB-R1-F10 — stale current in-body capability references / broader version policy | Change concrete Review-B references; defer general policy | Concrete Review-B portion resolved; general policy carried to Review C |

## R1 final architectural outcomes

### WorkRegister admission is general but bounded

Final rule:

> WorkRegister holds confirmed work owed by the owning top-level topic and not yet fully delivered.

This is broader than Design consequences and narrower than a generic backlog.

Include genuinely confirmed/committed/owed work whose delivery remains incomplete.

Exclude:

- ideas;
- possible future work;
- unconfirmed Reviewer findings; and
- unresolved matters still requiring judgment.

Those remain OpenItems, Working or another appropriate state.

Project Design retains a mandatory producer guarantee:

> every confirmed Design change with an undelivered downstream consequence must create/update
> WorkRegister.

That producer rule is a guaranteed subset, not the complete WorkRegister admission definition.

This makes `WR17` legitimate even though the peer Review programme was directly committed rather
than created by a Design consequence.

### WIP has topic-wide identity and per-thread exit

There remains one current WIP series per top-level topic:

```text
{TopLevelTopic}_WIP_vN.md
```

Concurrent subtopics/threads live inside that WIP.

Once an `Active thread — ...` section has safely routed its useful material, remove that thread from
the next checkpoint. Withdraw the whole WIP only when no active continuation thread remains.

WIP remains temporary, high-churn and non-authoritative.

### Working remains distinct and discoverable

Working remains the substantial exploratory/formative state, distinct from short-lived WIP.

When a new Working series is issued, the topic Index carries one version-agnostic locator in
`Live state`. Later versions in the same series do not churn the Index. Remove the locator when the
series ceases to be live.

This is a targeted Working-series rule, not a general live-state manifest.

### Documentation Methodology / Working Practices owner seam

Documentation Methodology owns:

- semantic document/work-state meanings;
- lifecycle/routing meanings;
- authority/non-authority boundaries;
- Binder/live-state semantic treatment; and
- documentation-specific discoverability.

Working Practices owns:

- practical checkpoint timing;
- transfer/sync;
- currency verification;
- repository/file handling; and
- other operational collaboration conventions.

Duplicated normative restatements were removed or reduced to references/non-normative summaries.

### Returned does not mean reconciled

Where a mapped WorkPackage Outcome has arrived but owner reconciliation cannot complete in the same
uninterrupted step, the WorkRegister mapping records:

`Returned — reconciliation pending`

If reconciliation is immediate, no ceremonial intermediate write is required.

Build returns evidence; the owning/directing process reconciles the WorkRegister.

### Project Handoff continuity uses existing OpenItems

Project Handoff remains transfer material, not a DocType/register/archive.

- same-pass reconciliation → no extra live entry;
- deferred reconciliation → one concise destination OpenItem;
- after incorporation, any confirmed-but-undelivered consequence is routed to WorkRegister before
  that OpenItem is removed.

No separate Handoff lifecycle or ledger was introduced.

### WorkRegister stores reconciliation state, Outcome stores evidence

An open WorkRegister item retains only compact reconciliation facts:

- current/terminal package status;
- stable WorkPackage/Outcome reference;
- concise returned result where useful; and
- remaining obligation/blocker.

Detailed execution/validation evidence remains in the Outcome and is referenced rather than copied.

### Split obligations stay simple

Where one WorkRegister obligation is deliberately split:

- required changes are independently identifiable, normally through bullets/enumeration;
- each WorkPackage `Covers` identifies the exact portions claimed;
- equivalent unambiguous prose is acceptable; and
- no structured sub-obligation identifier system is required.

`AIDE_WorkPackage@v3` carries this deterministic-enough mapping rule while preserving WorkRegister
ownership outside Build.

### Negative OpenItem closure remains live-only

Resolved OpenItems leave no tombstone merely because they existed.

If a no-change/negative conclusion and its reasoning are material and credibly likely to be
re-raised, preserve that conclusion in Decisions or another proper durable owner before removing
the OpenItem. Otherwise remove it with no history.

## Simplification dispositions

R1 explicitly challenged whether the state model could be materially reduced.

Final Review B disposition:

- WIP + Working merge — **Declined**
- WIP + OpenItems merge — **Declined**
- WorkRegister + WorkPackage merge — **Declined**
- remove Working — **Declined**
- remove/fold WorkPackage Outcome — **Declined**
- OpenItems + WorkRegister merge — **Deferred to Review E integrated coherence**

The first five distinctions survived the targeted remediation and R2 integrated tests.

The OpenItems/WorkRegister merge remains a legitimate integrated-coherence question because both
are live registers, but Review B did not find evidence sufficient to collapse them before Reviews C
and D test the wider architecture.

## R2 integrated tests

Claude explicitly tested the remediated model against:

1. WR17 legitimacy outside the Design-producer path;
2. Q9/Q12 remaining OpenItems rather than WorkRegister items;
3. one WIP thread completing while another remains active;
4. a multi-version Working series outside the Binder and later withdrawal;
5. a deferred Project Handoff across context loss;
6. a returned Outcome interrupted before owner reconciliation;
7. one four-part WorkRegister obligation split over three WorkPackages including a Partial result;
8. trivial versus materially reusable negative OpenItem conclusions;
9. durable history after live-row deletion; and
10. multiple top-level topics sharing one physical/chat container.

All ten tests passed. The only caveats produced the two narrow R2 closing findings below.

## R2 findings and Lead dispositions

### RB-R2-F1 — D41 overclaimed completion of the current-reference sweep

**Disposition:** Accept / Change — non-substantive closing correction.

R2 found two current executable references in the Documentation Methodology Standard that remained
stale:

- `AIDE_Build@v4` where current Build is `AIDE_Build@v5`;
- `AIDE_Review@v1` where current Review is `AIDE_Review@v2`.

It also found that Documentation Methodology Decision D41 recorded the earlier check too broadly as
a complete five-master sweep.

**Applied correction:**

Final `DocumentationMethodology_Binder_v7.md` / `AIDE_DocumentationMethodology@v26`:

- corrects the two active instructions to `AIDE_Build@v5` and `AIDE_Review@v2`;
- preserves D41 unchanged as historical R1 evidence;
- adds D42, explicitly refining D41's overbroad verification claim;
- states that the R1 preflight check covered current references directly identified/affected by the
  coordinated remediation rather than proving a general corpus-wide version sweep; and
- deliberately does not establish general footer/current-reference/dependency-checkpoint policy.

**Final verification:** Applied and Lead-verified.

### RB-R2-F2 — Project Handoff closure omitted the existing WorkRegister routing step

**Disposition:** Accept / Clarify — non-substantive closing correction.

The general Documentation Methodology OpenItems closure rule already required confirmed remaining
delivery to be routed to WorkRegister, but the practical Project Handoff section did not state that
step at the point a destination OpenItem is removed.

**Applied correction:**

Final `WorkingPractices_Binder_v4.md` states that a deferred Project Handoff OpenItem is removed only
after:

1. reconciliation/incorporation is complete; and
2. any confirmed-but-undelivered consequence produced by that reconciliation has been routed to the
   destination WorkRegister under Documentation Methodology.

No new Handoff mechanism/state/lifecycle/register was introduced.

**Final verification:** Applied and Lead-verified.

## Final authoritative verification

Final closing inputs:

- `DocumentationMethodology_Binder_v7.md`
- `WorkingPractices_Binder_v4.md`
- `ProjectDesign_Binder_v3.md`
- `Build_Binder_v5.md`

Concrete live-state test inputs:

- `Capabilities_OpenItems_v15.md`
- `Capabilities_WorkRegister_v15.md`

The Lead verified:

1. `AIDE_DocumentationMethodology@v26` contains the accepted R1 work-state architecture.
2. Current Documentation Methodology WorkPackage integration targets `AIDE_WorkPackage@v3` and
   `AIDE_Build@v5`.
3. Current Documentation Methodology Review integration targets `AIDE_Review@v2`.
4. D41 remains unchanged as historical R1 evidence.
5. D42 explicitly corrects/bounds D41 without asserting a general version-reference policy.
6. Working Practices Project Handoff closure now routes any confirmed-but-undelivered consequence
   to WorkRegister before its continuity OpenItem is removed.
7. Project Handoff remains transfer material rather than a new document type/register/lifecycle.
8. Documentation Methodology remains the semantic owner of OpenItems/WorkRegister.
9. Project Design retains the mandatory Design→WorkRegister producer rule without narrowing the
   general WorkRegister definition.
10. Build/WorkPackage retains evidence/authorisation ownership without gaining WorkRegister closure
    authority.
11. `AIDE_WorkPackage@v3` supplies deterministic-enough split-obligation `Covers` mapping without
    structured sub-obligation identifiers.
12. No material Review B architectural issue remains requiring another Reviewer Round.

## Carried observations

### Review C — Dependencies / conformance

Carry together:

1. Review A's observation that a documentation-conformance checkpoint can appear cyclic if treated
   identically to a functional dependency when Index and Documentation Methodology refer to each
   other.
2. Review B RB-R1-F10 / RB-R2-F1's broader unresolved question about how current in-body versioned
   capability references relate to dependency/conformance checkpoints and footer currency.

Review B corrected concrete current executable references that materially affected its remediation.
It did **not** establish the general policy.

### Review E — integrated coherence

Reconsider whether OpenItems and WorkRegister remain worth keeping as separate live registers after
Reviews C and D have tested the wider system.

No merge is implied.

## Review Result

```yaml
ReviewResult:
  ReviewId: AIDE-Architecture-Review-B-Documentation-Work-State
  Subject: Documentation/work-state model
  Outcome: Complete
  FinalLevel: High
  Mode: Full
  Rounds:
    - R1:
        Type: Robust
        Reviewer: Claude
        ActualModel: Claude Opus 5
        Status: Complete
        Assessment: Coherent with targeted changes
    - R2:
        Type: Inspect
        Reviewer: Claude
        ActualModel: Claude Opus 5
        Status: Complete
        Assessment: Resolved with minor clarification
  ReReview:
    Required: true
    Completed: true
  InScopeFindingsRemaining: none
  ResidualRisk:
    - general capability-reference versus dependency/conformance policy reserved for Review C
    - OpenItems/WorkRegister merge question reserved for Review E
  CompletionReason:
    - substantive R1 remediation survived required High re-review
    - all ten R1 findings were resolved for Review B scope
    - all ten focused R2 integrated tests passed
    - both R2 closing findings were non-substantive and were applied and Lead-verified
    - another Round would be verification-of-verification rather than material independent assurance
```

## Completion

**Review B is Complete at High.**

No Round 3 is required.

The peer architecture Review programme remains open under `WR17`; the next planned slice is
**Review C — Capabilities**.

---
Dependencies: !AIDE_DocumentationMethodology@v26, AIDE_Review@v2, AIDE_Messaging@v1
References: DocumentationMethodology_Binder_v7, WorkingPractices_Binder_v4, ProjectDesign_Binder_v3, Build_Binder_v5, Capabilities_WorkRegister_v15, Capabilities_OpenItems_v15, Capabilities_Architecture_Review_2026-08-31-1_CoreSubstrate_v2
