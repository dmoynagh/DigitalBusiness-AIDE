# Capabilities Architecture — Review — Capabilities Semantic Architecture

> **Review record v1** (2026-09-01). Final durable result for Review C. Preserves the complete
> three-Round lifecycle, R1 architecture findings/dispositions, R2 remediation findings, bounded R3
> verification, final carries, and completion outcome.

Review: `AIDE-Architecture-Review-C-Capabilities`
State: Complete
Outcome: Complete
Final level: High
Mode: Full
Lead: GPT
Reviewer: Claude
Reviewer model: Claude Opus 5

## Subject

The integrated AIDE Capabilities semantic architecture:

- parent Capabilities ownership and eight-peer model;
- Standards and Tools production/usage;
- Tags and Scope;
- Dependencies and Migration;
- Review and Messaging;
- capability identity/release/conformance/reference semantics;
- generic Builder boundaries; and
- direct Bootstrap-facing seams needed to test semantic coherence.

## Objective

Determine whether the Capabilities peer set has one coherent semantic owner for each mechanism,
composes without hidden cycles or duplication, distinguishes release/conformance/reference roles
correctly, and can be materially simplified before design-to-production and platform implementation
work proceeds.

The Review explicitly carried forward:

1. Review A's apparent dependency/conformance-cycle observation; and
2. Review B's unresolved distinction between current executable capability references, saved
   dependency checkpoints and ordinary References.

## Review history

### Round 1

```text
Type: Robust
Level: High
Mode: Full
Reviewer: Claude
Actual reviewer model: Claude Opus 5
Assessment: Sound with targeted changes
```

Primary Capabilities material:

- `Capabilities_Binder_Core_v2.md`
- `Capabilities_Binder_StandardsTools.md`
- `Capabilities_Binder_Runtime.md`
- `Capabilities_Binder_Review_v2.md`
- `Capabilities_Binder_Messaging_v1.md`

Narrow seam authorities:

- `Core_Binder_v3.md`
- `DocumentationMethodology_Binder_v7.md`

Messaging:

```text
Request:     aide-architecture-review-c-capabilities/gpt/001 @ GPT_v1
Response:    aide-architecture-review-c-capabilities/claude/001 @ Claude_v1
Disposition: aide-architecture-review-c-capabilities/gpt/002 @ GPT_v1
```

R1 found eleven targeted issues. The Lead accepted all eleven, with refinements that deliberately
avoided a new dependency taxonomy, exact-version policy layer, generic Builder substrate or runtime
orchestration engine.

### Round 2

```text
Type: Inspect
Level: High
Mode: Full
Reviewer: Claude
Actual reviewer model: Claude Opus 5
Assessment: Architecture sound; targeted reach corrections remained
```

Remediated material:

- `Capabilities_Binder_Core_v3.md`
- `Capabilities_Binder_StandardsTools_v1.md`
- `Capabilities_Binder_Runtime_v1.md`
- `Capabilities_Binder_Review_v3.md`
- `Capabilities_Binder_Messaging_v2.md`

Messaging:

```text
Request:     aide-architecture-review-c-capabilities/gpt/003 @ GPT_v1
Response:    aide-architecture-review-c-capabilities/claude/002 @ Claude_v1
Disposition: aide-architecture-review-c-capabilities/gpt/004 @ GPT_v1
```

R2 verified eight R1 Findings fully resolved and three partially resolved. It raised four bounded
closing Findings concerning self-application of the versionless-reference rule, runtime propagation
into Standards Usage, Messaging Tool alignment, and the Index self-version row.

The Lead accepted all four and applied a bounded closing pass.

### Round 3

```text
Type: Check
Level: High
Mode: Full
Reviewer: Claude
Actual reviewer model: Claude Opus 5
Scope: RC-R2-F1..F4 plus accidental-scope-expansion check only
Assessment: All criteria passed
```

Verification material:

- `Capabilities_Binder_Core_v4.md`
- `Capabilities_Binder_StandardsTools_v2.md`
- `Capabilities_Binder_Messaging_v3.md`

Runtime and Review Binders were deliberately omitted because they were already verified in R2 and
were unchanged by the closing remediation.

Messaging:

```text
Request:     aide-architecture-review-c-capabilities/gpt/005 @ GPT_v1
Response:    aide-architecture-review-c-capabilities/claude/003 @ Claude_v1
Disposition: aide-architecture-review-c-capabilities/gpt/006 @ GPT_v1
```

R3 directly verified every closing criterion, found no new material Review C Finding, found no
scope expansion and recommended closure at High.

## R1 Finding dispositions and final state

| Finding | Lead disposition | Final state |
|---|---|---|
| RC-R1-F1 — capability-reference semantics | Accept with refinement | Resolved; syntactic role determines semantics; executable references versionless by default |
| RC-R1-F2 — conformance checkpoints create apparent ordering/cycles | Accept | Resolved; checkpoints are non-ordering saved evidence |
| RC-R1-F3 — legacy footer form in unchanged artefacts | Accept with confirmed migration fact | Resolved; no sweep; changed artefacts reconcile through current on qualifying save |
| RC-R1-F4 — Review Profiles current executable v1 references | Accept | Resolved; current executable Review references are versionless |
| RC-R1-F5 — exact-version constraint treatment | Accept with refinement | Resolved; unsatisfied exact constraint blocks affected use; no substitute/policy layer |
| RC-R1-F6 — missing published Tool production contract | Accept | Resolved through `AIDE_ToolsProduction@v1` |
| RC-R1-F7 — generated-tag freshness | Accept with refinement | Resolved semantically; concrete Build/platform realisation carried to Review D |
| RC-R1-F8 — Review/Messaging correlation disagreement | Accept | Resolved; Review identity authoritative, positive disagreement quarantined |
| RC-R1-F9 — Messaging STATE evidential limit | Accept as clarification | Resolved; evidence depends on retained state, explicit Ack when proof matters |
| RC-R1-F10 — dependency precedence versus Bootstrap peers | Accept | Resolved; precedence is local to dependencies of the processed artefact |
| RC-R1-F11 — behind-current checkpoints treated as decay | Accept | Resolved; lag is expected steady state, not automatic update trigger |

## R2 Finding dispositions and final state

| Finding | Lead disposition | R3 verification |
|---|---|---|
| RC-R2-F1 — reference-position rule not self-applied | Accept / bounded change | Resolved |
| RC-R2-F2 — Standards Usage runtime propagation missing | Accept / change | Resolved through `AIDE_StandardsUsage@v2` |
| RC-R2-F3 — Messaging Tool not aligned to current Messaging semantics | Accept / change | Resolved through Tool Design v2 and `AIDE_MessagingTool@v2` |
| RC-R2-F4 — Index self-row records wrong version | Accept / correction | Resolved in `Capabilities_Index_v18` and verified row-by-row |

## Final architecture outcomes

### Reference-position semantics

The final model does not add dependency categories.

```text
Dependencies: X@vN
  = dependent artefact's last saved/proven conformance checkpoint

Dependencies: X@!vN
  = hard present exact-version constraint

Dependencies: X
  = dependency relationship without version tracking

References:
  = reader/evidence pointer with no currency or conformance obligation

Current executable body reference
  = operational instruction; versionless by default
```

A specific executable version remains valid where the instruction deliberately depends on or
targets that release's contract. Production validates intentional specificity rather than forcing
all references to the newest release.

Conformance checkpoints create no resolution or execution order. Mutual checkpoints therefore do
not create an operational dependency cycle.

A newer available release does not by itself make an older saved checkpoint stale, defective or an
update trigger.

### Exact-version constraints

`X@!vN` is a hard present constraint. If exact vN is unavailable:

- the dependency is unsatisfied;
- affected use requiring it is blocked;
- another release may not silently substitute;
- the condition is not an ordinary Migration gap; and
- changing/removing the pin is an explicit validated dependent-artefact change.

No extra exact-pin policy mechanism was introduced.

### Tools production

Tools now publishes the canonical generic Tool production contract:

`AIDE_ToolsProduction@v1`

Build Capability consumes that contract by identity rather than duplicating the canonical Tool
shape or depending on internal Tools Design to recover it.

This preserves the ownership boundary:

```text
Tools
  owns generic canonical Tool production semantics

Build Capability
  applies the published production contract

Platform Build
  realises canonical Tools for target platforms
```

### Tags, Scope and runtime usage

Tags owns the generic freshness rule without owning a polling service or orchestration engine.

Where source state capable of changing generated tags changes, applicable builders run before the
artefact is published/saved as current where those tags are governed state. If freshness is
uncertain, rebuild before tag-dependent behaviour relies on them.

Machine Scope is deterministic only over current tag state.

`AIDE_StandardsUsage@v2` now carries this runtime precondition and also tells operating consumers
that a behind-current dependency checkpoint is expected steady state rather than a stale-state
condition. Applicable Required Migration remains the affected-use gate.

### Review and Messaging

Review/Round payload identity is authoritative for Review lifecycle semantics. Messaging
Thread/Message correlation is transport-level evidence. A positive disagreement between the two is
a quarantine condition.

Messaging remains register-free. STATE is best-effort evidence whose value depends on evidence the
constructing context actually retains. A genuinely stateless context may provide no positive
receipt evidence; explicit Ack/Acknowledge is used where positive proof matters.

`AIDE_MessagingTool@v2` now consumes those current STATE semantics directly.

### Preserved simplifications and boundaries

Review C explicitly did **not** introduce:

- a Tags/Scope merge;
- a generic Builder capability/framework;
- a Dependencies/Migration merge;
- a generic runtime orchestration engine;
- a Review/Messaging merge;
- Review-owned transport;
- release-number coupling between Review and Review Profiles;
- a new dependency relationship taxonomy; or
- a ninth Capabilities peer.

The final architecture remains eight peers:

```text
Standards
Tools
Tags
Scope
Dependencies
Migration
Review
Messaging
```

## Decision-record treatment

R3 observed that the bounded R2/R3 corrections are not repeated as new entries in
`Capabilities_Decisions_v16`.

**Lead disposition: no additional Capabilities Decisions entry is required.**

D96–D106 already preserve the substantive Review C architecture decisions and reasoning. The R2/R3
items are self-application, runtime propagation and record-truth corrections implementing those
accepted decisions; they do not establish a new architecture choice. The Review record owns Review
Finding/disposition/verification history. Duplicating that history in Decisions would create a
second owner for the same evidence.

A later change that introduces a genuinely new design choice should of course be recorded in
Decisions normally.

## Final verification

R3 verified directly that:

1. parent locator/current-outcome prose is versionless while dependency syntax, Index current-release
   data and historical Decisions remain correctly version-bearing;
2. `AIDE_StandardsUsage@v2` carries both Machine Scope freshness and expected checkpoint-lag runtime
   semantics;
3. `AIDE_MessagingTool@v2` and its Tool Design consume current retained-evidence/Acknowledge
   semantics and use versionless current executable Messaging references;
4. the Index self-row and all changed document/release rows are truthful;
5. the eight-peer architecture is unchanged;
6. no new Builder/orchestration/taxonomy mechanism was introduced;
7. Runtime and Review architecture remained unchanged from the R2-verified state; and
8. the work did not broaden into Review D.

R3 found no new material Review C Finding and judged another Round to have no material value.

Post-completion `Capabilities_Index_v19` / `Capabilities_Binder_Core_v5` update only the current
Review-programme state and priority after this successful verification; they do not alter the
reviewed semantic architecture.

## Carries

### Review D — design-to-production

Carry forward the concrete platform/Build realisation of generated-tag freshness and related
production/build sequencing. Review C owns only the semantic requirement and did not design the
platform execution mechanism.

### Review E — integrated coherence

Reconsider the deferred possible `OpenItems + WorkRegister` merge after Review D has tested the
remaining design-to-production architecture.

No merge is implied.

## Review Result

```yaml
ReviewResult:
  ReviewId: AIDE-Architecture-Review-C-Capabilities
  Subject: Capabilities semantic architecture
  Outcome: Complete
  FinalLevel: High
  Mode: Full
  Reviewer: Claude
  ActualModel: Claude Opus 5
  Rounds:
    - R1:
        Type: Robust
        Status: Complete
        Assessment: Sound with targeted changes
    - R2:
        Type: Inspect
        Status: Complete
        Assessment: Architecture sound; four bounded closing findings
    - R3:
        Type: Check
        Status: Complete
        Assessment: All bounded closing criteria resolved
  ReReview:
    Required: true
    Completed: true
  InScopeFindingsRemaining: none
  ResidualRisk:
    - concrete platform/build realisation of generated-tag freshness reserved for Review D
    - OpenItems/WorkRegister merge question reserved for Review E
  CompletionReason:
    - all eleven R1 Findings are resolved
    - all four R2 Findings are resolved and independently verified in R3
    - no material new R3 Finding was introduced
    - the eight-peer architecture and ownership boundaries remained intact
    - another Round was judged unlikely to add material value
```

## Completion

**Review C is Complete at High.**

No Round 4 is required.

Reviews A, B and C are now complete. The peer architecture Review programme remains open under
`WR17`; the next planned slice is **Review D — design-to-production**.

---
Dependencies: !AIDE_DocumentationMethodology@v26, AIDE_Review@v3, AIDE_Messaging@v2
References: Capabilities_Binder_Core_v4, Capabilities_Binder_StandardsTools_v2, Capabilities_Binder_Runtime_v1, Capabilities_Binder_Review_v3, Capabilities_Binder_Messaging_v3, Capabilities_WorkRegister
