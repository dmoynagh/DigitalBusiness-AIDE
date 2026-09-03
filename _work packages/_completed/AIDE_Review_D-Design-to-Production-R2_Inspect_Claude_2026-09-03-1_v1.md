# AIDE Architecture — Peer Review Programme — Review D — Round 2 — Inspect — Reviewer Response

> **Version 1** (2026-09-03). Remediation verification against the accepted R1 dispositions.

---

## 1. Overall assessment

**Resolved with minor clarification.**

All ten accepted dispositions (`RD-R1-1` through `RD-R1-10` — the Lead's remediation-verification
groupings) are applied in the current corpus, and in every case the rule reaches the executable
contract rather than stopping at Design prose. The two that mattered most in R1 — Deployment Set
membership authority and generated-Tag freshness at the producer freeze boundary — are closed
properly, including the runtime boundary that R1 identified as unenforceable.

Seven residuals remain. None is a design defect. Three are current-reference or current-state
contradictions of exactly the class `RD-R1-9` (the bounded current-reference and procedure
corrections) was accepted to sweep, and one of those three appears to have been introduced by this
remediation pass. The remaining four are wording, placement or one-sided-rule observations.

**Review D can complete at High** once `R2-1`, `R2-2` and `R2-3` are corrected. Those are text
corrections to three sentences in three documents. They do not require another Review Round.

---

## 2. Findings

Severity scale used here: *Minor* means a current executable or current-state contradiction that an
implementer could act on wrongly; *Clarification* means wording or placement that is currently
unambiguous in substance but would read better corrected at its next natural revision.

### R2-1 — Two current documents disagree about which Capability Build Tools are current

**Severity: Minor. Regression introduced by this remediation.**

`Capabilities_Tools_Design_v7` §10 (the current production/build Tool family list) states:

- `AIDE_BuildCapabilityTool@v5`
- `AIDE_CapabilityBuilderTool@v3`

`Capabilities_Tools_Definition_v5` — the single current Capability Definition, which is the
authoritative composition control — records:

- `Tools.BuildCapability` → `AIDE_BuildCapabilityTool@v6`, Element release v4
- `Tools.CapabilityBuilder` → `AIDE_CapabilityBuilderTool@v4`, Element release v4

`Capabilities_Index_v24` agrees with the Definition (`AIDE_BuildCapabilityTool@v6`,
`AIDE_CapabilityBuilderTool@v4`), and both Tools exist at those releases in
`Capabilities_Binder_StandardsTools_v7`.

Both Tools advanced in this remediation pass (v5→v6 and v3→v4). The Definition, Index and Tools
themselves were updated; the `Capabilities_Tools_Design_v7` §10 list was not.

**Why it matters.** An executor resolving "the current Capability Builder" gets v3 from the Design
and v4 from the Definition. The two releases differ materially: v4 carries the snapshot-relative Tag
validation step (`RD-R1-2`) and the post-Build workflow-state boundary (`RD-R1-8`). Following the
Design's list would run the pre-remediation executor.

**Source evidence.** `Capabilities_Binder_StandardsTools_v7`, `Capabilities_Tools_Design_v7` §10
versus `Capabilities_Tools_Definition_v5` Capability Elements table;
`Capabilities_Binder_Core_v10`, `Capabilities_Index_v24` subtopic ownership table.

**Remedy.** Update `Capabilities_Tools_Design_v7` §10 to `AIDE_BuildCapabilityTool@v6` and
`AIDE_CapabilityBuilderTool@v4`. The same paragraph's closing sentence — "its production role is not
silently interpreted as v3" — should also adopt the corrected v3-as-checkpoint wording already used
in `Capabilities_BuildCapability_Tool_Design_v6` and `AIDE_BuildCapabilityTool@v6`.

---

### R2-2 — AI Deployment Design points readers at the superseded Set Release contract

**Severity: Minor.**

`AIDeployment_Design_v7`, "Closed generic layer", states: detailed contracts are
`AIDeployment_SetRelease_Design_v1` and `AIDeployment_TargetAdapter_Design_v1`.

The current Set Release contract is `AIDeployment_SetRelease_Design_v2`. The same document's
`References:` footer cites v2 correctly, and the Layer 2 model section correctly cites
`AIDeployment_Registry_Design_v2`. Only this body sentence is wrong.

**Why it matters.** `AIDeployment_SetRelease_Design_v2` is precisely where the `RD-R1-1`
fixed-membership rule and the `RD-R1-3` required-presence separation live. v1 contains neither. A
reader following the body pointer from the current Design lands on the pre-remediation contract and
would implement the exact defects this Round is verifying as closed. This is a current directive,
not a historical citation and not a `References:` pointer, so it falls inside the `RD-R1-9`
boundary rather than the explicit non-findings.

**Source evidence.** `AIDeployment_Binder_v7`, `AIDeployment_Design_v7` "Closed generic layer"
versus its own `References:` line and `AIDeployment_SetRelease_Design_v2` header.

**Remedy.** Change the body reference to `AIDeployment_SetRelease_Design_v2`.

---

### R2-3 — Capability Standard points at the superseded Build Target Profile contract

**Severity: Minor.**

`AIDE_Capability_Standard_v3`, under "Platform Definition, Build Platforms and Build Targets",
instructs: use `Capabilities_BuildTargetProfile_Design_v1` for deployment-facing Build Target/Profile
semantics. The current contract is `Capabilities_BuildTargetProfile_Design_v2`, which the same
Standard's `References:` footer cites correctly.

**Why it matters.** v2 is where the `RD-R1-6` `RequiredReach` clarification lives. This is an
in-body directive in a Standard that was itself revised in this pass (v2→v3), so it is a current
executable instruction naming a superseded release.

**Source evidence.** `Capabilities_Binder_Core_v10`, `AIDE_Capability_Standard_v3` body versus its
`References:` line and `Capabilities_BuildTargetProfile_Design_v2` header.

**Remedy.** Change the body reference to `Capabilities_BuildTargetProfile_Design_v2`.

---

### R2-4 — Registry retains a tag-staleness obligation written before the snapshot model

**Severity: Clarification.**

`AIDeployment_Registry_Design_v2` §6 (Tags) still says Registry publication shall not knowingly
publish stale generated Tags where those Tags are part of governed package state. That sentence
predates the remediation and was one of R1's items of evidence that the Registry was being given an
obligation it could not discharge.

**Assessment.** This is **no longer a contradiction**. `AIDE_Deployment@v7` Major Rule 16 and
Decision D42 now state that Registry and Deployment consume frozen snapshot-relative Tags and do not
run producer-owned Tag Builders, and `AIDE_DeploymentRegistryTool@v2` Register step 4 preserves the
producer freshness evidence. The Registry can therefore now discharge a *check* on that evidence.
But "stale" is undefined against a frozen snapshot, and no Registry Tool step performs the check the
sentence implies.

Per the R2 boundary instruction, `AIDeployment_Registry_Design_v2` remains current; I am not
recommending a revision on this alone.

**Suggested wording at next natural revision.** Replace with an evidence-based condition — reject a
package whose required producer tag-freshness evidence is absent or failed — so the rule names
something the Registry actually holds.

---

### R2-5 — Tag-freeze ordering is filed under a post-Build heading

**Severity: Clarification.**

`AIDE_CapabilityBuild@v4` places the instruction "Before Package freeze, run/validate every
applicable Tag Builder against the resolved authoritative Build source snapshot" as the final
paragraph of the **Post-Build** section. Post-Build actions by definition run after validation and
freeze. The Standard's Preconditions list does not mention tag freshness.

**Assessment.** The instruction itself is unambiguous about ordering, and
`AIDE_CapabilityBuilderTool@v4` step 5 places the operation correctly — before package assembly at
step 6 and freeze at step 8 — so there is **no executable defect**. This is a readability point on
an ordering-critical rule: an executor reading the Standard section by section reaches it only after
the boundary it governs.

**Suggested remedy at next revision.** Move the paragraph to Preconditions or to its own
pre-assembly heading.

---

### R2-6 — The RequiredReach evidence-return path is stated only where it is received

**Severity: Clarification.**

`Capabilities_BuildTargetProfile_Design_v2` states that repeated or authoritative Deployment evidence
contradicting the producer reach assumption is returned as design/platform-evidence feedback for
reassessment. That satisfies the substance of `RD-R1-6`: `RequiredReach` is producer intent,
Deployment failure does not invalidate it, and Deployment does not rewrite it.

No AI Deployment contract names a corresponding obligation to *emit* that feedback. `AIDE_Deployment@v7`
and `AIDE_DeploymentTool@v7` record per-Target mismatches, verification status and assurance in
Deployment State, so the fact exists and is durable; nothing routes it back to the owning Profile.

**Assessment.** Non-blocking. The fact is recorded and the ordinary direction/Review loop can carry
it. Worth one sentence in the Deployment verification contract at some point, but the accepted
disposition was about meaning and ownership, and both are correct.

---

### R2-7 — Registry Tool v2 retains a v1 self-reference

**Severity: Clarification (nit).**

`AIDE_DeploymentRegistryTool@v2` "Failure and idempotency" closes with "physical purge is not a v1
action" in a Tool now published at v2. A reader could infer purge became a v2 action. Same class as
the accepted `RD-R1-9` corrections, but with no consequence beyond the sentence itself, since no
purge action appears in the Tool's `LogicalActions`.

**Remedy.** Reword to "physical purge is not a Registry Tool action" or name v2 explicitly.

---

### Standing observation — C5, Build Platforms selection

Per the Lead's instruction to carry this as a standing observation rather than a Finding.

**Not independently resolved by the remediated corpus.** All eight current Capability Definitions —
Standards v4, Tools v5, Tags v3, Scope v3, Dependencies v3, Migration v4, Review v4, Messaging v3 —
retain the same prose under "Platform Definition and Build Platforms": the Capability is
platform-neutral, current generic Working Surface evidence must be resolved before a Capability Build
request, and designer selection remains `Build: null` until explicitly decided.

`AIDE_Capability@v3` defines the `BuildPlatforms` structure and the blocking rules, and
`AIDE_BuildCapabilityTool@v6` step 2 requires at least one explicit `Build:true`. The architecture is
therefore correct and correctly blocking. No Capability presently asserts a resolved `Build:true`, so
no Capability is presently build-authorised, and no contract names the owner or step that supplies
that selection.

Status unchanged: non-blocking, operational rather than architectural, outside the accepted
remediation, and not a condition of Review D closure.

---

## 3. Disposition against each R1 item

| Item | Verdict | Where verified |
|---|---|---|
| **RD-R1-1** — fixed Set membership and supply selection | **Resolved** | `AIDeployment_SetRelease_Design_v2` separates fixed member list from supply selector and blocks candidate resolution on missing required supply; `AIDE_Deployment@v7` "Deployment Set and Target" and Decision D40 carry it; `AIDE_DeploymentTool@v7` Reconcile steps 2–3 make it executable; `AIDeployment_AIDECore_Reference_v2` instantiates `MembershipMode: Fixed` with eight `RequiredMembers` and a separate `SupplySelector`. The dynamic mode is permitted only when explicitly declared, as required. |
| **RD-R1-2** — generated Tag freshness at Package freeze | **Resolved, including the runtime boundary** | `AIDE_Tags@v3` and `Capabilities_Tags_Design_v3` §9 add the immutable-artefact boundary with a freeze sequence and state that downstream consumers do not rerun producer builders; `AIDE_CapabilityBuild@v4` and `Capabilities_CapabilityBuild_Decisions_v4` D12 place the obligation at the producer; `AIDE_CapabilityBuilderTool@v4` step 5 executes it before assembly and freeze and fails visibly if freshness cannot be established; `AIDE_Scope@v3` and `Capabilities_Scope_Design_v3` §5a close R1's runtime boundary by defining "current" for deployed material as the frozen snapshot; `AIDE_Deployment@v7` Rule 16 and D42 close the consumer side. No polling service or orchestration engine introduced, so the Review C constraint is preserved. |
| **RD-R1-3** — immutable Set facts, per-Target satisfaction | **Resolved** | `AIDeployment_SetRelease_Design_v2` makes preservation-and-interpretability the candidate condition and defers satisfaction to per-Target evaluation; `AIDE_Deployment@v7` Major Rule 8 and Decisions D41/D44; `AIDE_DeploymentTool@v7` steps 9 and 13. The R1 contradiction between candidate validity and Target reconciliation is gone: candidate validity now tests supply and assembly, not satisfaction. Mechanical assembly preservation is stated in `AIDeployment_SetRelease_Design_v2` Output Definitions, the Standard and the Tool. |
| **RD-R1-4** — exact evaluated-input vectors | **Resolved** | `AIDE_Capability@v3` requirement 7 requires exact version/revision or digest plus evaluation date/status and rules out generic prose; all eight Capability Definitions now carry structured `ElementProduction` blocks with `EvaluatedInputs`, `LastEvaluated` and `Result`. No Definition retains the old prose form. |
| **RD-R1-5** — specialised facts map into WorkPackage v3 | **Resolved** | `AIDE_CapabilityBuild@v4` "Capability Build WorkPackage mapping" gives the field-by-field mapping including the explicit default for absent force scope; `AIDE_BuildCapabilityTool@v6` step 8 makes it executable; `Capabilities_CapabilityBuild_Decisions_v4` D11 and `Build_Decisions_v9` D26 confirm `AIDE_WorkPackage@v3` is unchanged. No v4 or parallel schema introduced. |
| **RD-R1-6** — RequiredReach is producer intent | **Resolved**, with `R2-6` | `Capabilities_BuildTargetProfile_Design_v2` defines reach as required/intended support under satisfied conditions, states that Deployment failure does not by itself invalidate it, and routes contradictory evidence to reassessment; `Capabilities_Decisions_v21` D141. Nothing in AI Deployment rewrites reach. |
| **RD-R1-7** — one Open Release Batch for coordinated changes | **Resolved** | `Build_PostBuild_Design_v3` and `Build_Decisions_v9` D25 make coordination an owner-defined fact that Build carries but never infers; `Capabilities_CapabilityBuild_Decisions_v4` D13 and `AIDE_CapabilityBuild@v4` Post-Build make Batch use non-optional within an established coordinated change while preserving direct registration for an independent package; `AIDE_BuildCapabilityTool@v6` step 5 and `AIDE_CapabilityBuilderTool@v4` step 9 execute it. `AIDE_DeploymentRegistryTool@v2` BeginBatch retains the rule against inferring a batch from timing. |
| **RD-R1-8** — post-Build request/result are workflow state | **Resolved** | `AIDE_Capability@v3` requirement 13; `AIDE_CapabilityBuild@v4` Capability Package list no longer includes nominated post-Build intent; `AIDE_CapabilityBuilderTool@v4` step 8 forbids writing request, receipt or lifecycle state into frozen bytes; `Build_Design_v9` §13, `Build_Decisions_v9` D24 and `AIDeployment_Decisions_v7` D43 agree. The "Post-Build intent" section is removed from all eight Capability Definitions. |
| **RD-R1-9** — bounded current-reference and procedure corrections | **Resolved in part; three residuals** | Verified applied: Build Capability migration wording now treats v3 as the Required transition checkpoint and directs current invocations to the current release (`Capabilities_BuildCapability_Tool_Design_v6`, `AIDE_BuildCapabilityTool@v6`, `Capabilities_Design_v15` §7); Registry Tool is v2 and Register step 2 validates `AIDE_Deployment@v7`; `AIDE_DeploymentTool@v7` Reconcile numbering is coherent at 1–17 with the missing step restored; `ProjectDesign_Design_v7` §10 records the true lineage (v4 preflight correction, v5 flexible contributions and hosting, v6 orientation) and states that the v7 document corrects the explanation without creating another semantic release; Capability Definition dependency and reference drift is not reintroduced; mechanical assembly preservation is stated in three places. **Not fully swept:** `R2-1`, `R2-2` and `R2-3`. |
| **RD-R1-10** — Change Delivery application location | **Resolved against its stated disposition** | `WorkingPractices_Design_v9` WP1, `WorkingPractices_Decisions_v8` D43 and `AIDE_WorkingPractices@v8` WP1 all require the instructions to identify the target repository and application root, use a repository-relative destination for every file action, preserve the target tree, and treat absolute local paths as supplemental only, with an explicit prohibition on depending on a stale absolute path or an ambiguous working directory. Verified as a changed-item check only; this item has no R1 Reviewer-finding basis and is not presented as closure of one. |

---

## 4. Regressions introduced by remediation

**One, minor: `R2-1`.**

`Capabilities_Tools_Design_v7` §10 was left naming the pre-remediation Tool releases while the Tools
themselves, the Tools Capability Definition and the Capabilities Index all advanced. This is a
remediation-pass omission rather than a pre-existing defect, and it is the only place in the R2
baseline where two current documents assert different current state.

`R2-2` and `R2-3` are stale in-body pointers of the same class but in documents whose target
contracts also advanced in this pass, so I have not classified them as regressions in the strict
sense — either reading is defensible and the remedy is identical.

**No semantic regression found.** I specifically checked the seams most exposed to the remediation:

- removing post-Build intent from Capability Definitions does not leave the Definition unable to
  express anything it previously owned, because `AIDE_Capability@v3` requirement 13 relocates the
  authority to the Build request and WorkPackage rather than deleting it;
- the snapshot-relative Tag rule did not displace the ordinary publish-time freshness rule —
  `AIDE_Tags@v3` retains both and scopes the new clause to immutable Build packages and outputs;
- the fixed-membership rule did not eliminate selector-based Sets, which remain available under an
  explicit dynamic mode; and
- moving required-presence satisfaction to per-Target evaluation did not weaken it — the facts are
  preserved in the immutable release and the missing-material blocker is retained in Rule 8 and Tool
  step 13.

---

## 5. Would another round add material value?

**No.**

The three Minor residuals are single-sentence corrections in three documents. They do not require
design work, do not interact with each other, and would be verifiable by inspection of the corrected
sentences rather than by a Review Round. The four Clarifications are drafting improvements for the
next natural revision of their host documents.

Running a further Round would exercise the same Inspect posture against the same baseline and would
be very unlikely to surface anything the accepted dispositions did not already frame. If the Lead
wants additional assurance after correction, the useful next step is Review E — integrated coherence
— as already planned, not another Review D Round.

---

## 6. Can Review D complete at High?

**Yes, on correction of `R2-1`, `R2-2` and `R2-3`.**

The substantive architecture questions Review D was convened to answer are settled. The design-to-
production chain is coherent from confirmed design state through runtime-verified deployment,
ownership is correct at every layer tested, the identity and release model holds, and the two seam
defects that R1 identified as capable of producing a wrong-but-well-provenanced deployed release —
silent Set shrinkage and unenforceable tag freshness — are closed at the executable contract level.

The remaining residuals are current-reference corrections. My recommendation is that the Lead apply
them as a bounded correction pass and close Review D at High without a further Round, recording the
four Clarifications and the C5 standing observation as carried items rather than open findings.

---

## 7. Concise R2 result summary

```text
Review: Review D — design-to-production
Round: R2 | Type: Inspect | Level: High | Mode: Full
Reviewer: Claude (Opus 5, session-declared)
Baseline: 13 post-remediation current sources as supplied

Result: Resolved with minor clarification

Dispositions:  RD-R1-1  Resolved
               RD-R1-2  Resolved, incl. runtime boundary
               RD-R1-3  Resolved
               RD-R1-4  Resolved
               RD-R1-5  Resolved
               RD-R1-6  Resolved (see R2-6)
               RD-R1-7  Resolved
               RD-R1-8  Resolved
               RD-R1-9  Resolved in part — R2-1, R2-2, R2-3 outstanding
               RD-R1-10 Resolved against stated disposition

Residuals:     R2-1 Minor  Tools Design v7 §10 names superseded current Tool family
               R2-2 Minor  Deployment Design v7 points at SetRelease Design v1
               R2-3 Minor  Capability Standard v3 points at BuildTargetProfile Design v1
               R2-4 Clar.  Registry Design v2 §6 tag-staleness wording predates snapshot model
               R2-5 Clar.  CapabilityBuild v4 tag-freeze rule filed under Post-Build heading
               R2-6 Clar.  RequiredReach feedback path stated only on the receiving side
               R2-7 Clar.  Registry Tool v2 retains a v1 self-reference

Standing:      C5 — no Capability asserts a resolved Build:true; unchanged, non-blocking

Regressions:   one minor (R2-1); no semantic regression
Another round: no material value
Review D at High: yes, on correction of R2-1, R2-2, R2-3
```

---

*Prepared 2026-09-03. No changes were implemented. Assessment was bounded to the accepted
dispositions; Review C peer semantics, the Review/Messaging/live-state models and Core were not
reopened.*
