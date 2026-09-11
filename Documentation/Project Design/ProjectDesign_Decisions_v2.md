Project Design — Decisions | decisions | ProjectDesign_Decisions@v2 | 2026-09-11

## D1 — Work register survives and comes home to Project Design

The gap the register fills is temporal, not interpersonal — something must hold "design says X, build hasn't caught up yet." The register is the one artefact where design is both source and target, which is why its states must reconcile against build return. Splitting the producer rule from its own ledger was the original model's mistake. The provider-consumer test settles it: the temporal gap only exists because Project Design owns both ends of the loop — it does not carry meaning outside Project Design.

The alternative — register in Working Practices, producer obligation in Project Design — was tried and withdrawn during this pass.

## D2 — Work item and work register are distinct in kind

There is no subset relationship and none should be implied. A work item is a generic entity flowing through a workflow: raised, judged, given a fate. A design-generated work register entry exists because a design change had a downstream impact that has not yet been delivered. The register also admits directly-entered confirmed work (see D16). The distinction between work item and register entry is purpose and state, not exclusively origin — different purpose, different owner, different lifecycle. Collapsing them would erase exactly the meaning that makes the register worth having.

The name "work register" was reopened and tested against alternatives (delivery register, obligations register, consequence register, impact register, pending work register). "Obligations" was rejected as too amorphous. "Work register" stands: concrete, side-neutral, and reads cleanly as the register of work owed now that work item and work register are firmly separated.

## D3 — The design-build handoff replaces the work-package doctype

The work-package doctype was designed very early in the original implementation and never reviewed. It was a fixed artefact; the invariant it protected — the responsibility boundary — does not require one. Replaced by the design-build handoff: a transition point whose mechanism varies by build context.

The old doctype's reach was wide: Index references, the flow diagram, the handoff clause, the release lineage, and six decisions (D4, D7, D8, D12 and others). All of these either fall away or are re-grounded in the new mechanism.

Any surviving build-side "work package" is renamed build package so the word "work" is left free and the two never collide.

## D4 — The design doctype is criteria and advice, not a schema

Design composition varies a great deal by project type and build outcome. A schema would constrain composition; criteria describe what the design must achieve regardless of its shape. This is the facilitate-not-constrain position doing its work: AIDE exists to facilitate and empower, not to constrain or be a source of friction.

Nine required criteria, four advice items. The criteria tell the author what a good design must do; the advice tells how others have done it well.

## D5 — Design carries its own live reasoning inline

A design element is a two-part unit: the statement of what is true, plus its inline why. A separate reasoning block was considered and rejected — the reading pattern demands the why at the element, and inline is what makes the retention checkpoint a natural act rather than a bolted-on chore.

Duplication with decisions is accepted and expected: design holds the live why; decisions holds the fuller why, including paths not taken. The authority clause governs: reasoning pertinent to a current design choice belongs in the design.

## D6 — Overview survives as a Project Design doctype

Overview was parked in the block-catalogue session, with discussion reserved for the design pass. The parked return condition was topic-or-corpus scale; this pass corrects that — the real return condition is function, at project scale.

The overview is a purposeful pane-of-glass snapshot and deviation detector, not an overflow valve for a bloated summary. This directly contradicts the old binder's orientation section, which made overview an escalation from summary. The forward design wins; the old orientation section is dropped entirely.

## D7 — The summary suppression rule

Overview and summary do not make each other redundant, but no document ever carries both. While an overview lives inline, the host document does not also carry a summary. The moment the overview branches out to its own document, the source document gets a summary back. The rule prevents double-orienting, which wastes context and confuses consumers about which one governs.

## D8 — Capture and place reframed as a filing obligation, not a workflow entity

An earlier framing treated capture as an act, placement as a fate, and the work item as its subject. That was wrong. The real thing is narrower: a design conversation wanders, and the AI's job is that nothing said gets left where it fell. Each piece gets put where it belongs.

The work-item type list — expected in the earlier framing — does not belong here. It stays with Working Practices, to be surfaced when the work item is designed there, or left unenumerated if nothing demands it.

## D9 — The what/why vs how boundary replaces the old escalation list

The old binder enumerated what returns to design: objective, major scope, acceptance, ownership, architecture, policy. That enumeration is demoted to illustration; a single test replaces it: does what build encountered change what is being delivered or why, or only how it gets delivered? A list is arguable at the margin and rots as the system grows; a test does not.

The tiebreak — if build cannot tell which side it is on, it returns — makes the default deliberately asymmetric. An unnecessary return costs a message. Silently absorbing a design change costs the design's authority.

## D10 — The cost-and-complexity flag is an obligation, not a threshold

Rather than prescribe a numeric or percentage trigger, the flag is an obligation on build's judgement: when the real cost or complexity materially exceeds what the design appeared to assume, build surfaces it. No threshold, no how-long-is-a-piece-of-string test. A rule with a number would be exactly the friction facilitate-not-constrain exists to remove.

The flag defaults to proceed — if design does not intervene, build continues. This gives build two distinct reasons to come back, at different weights: a return for a genuine what/why question, and a flag where it can proceed but the price has moved.

## D11 — Superseded register items: judgement, not procedure

A fixed procedure was drafted for handling superseded items after handoff (freeze the entry, raise a superseding entry, notify build, reconcile) and withdrawn. The right answer genuinely varies — build might have finished, not started, or be halfway through. A fixed rule would get most cases wrong.

The requirement is narrow and strong: design determines the impact and the remedy, makes the call explicitly, and records it. Not that it follows a set path. This is the first instance in this design where facilitate-not-constrain changed a decision rather than sitting inert.

## D12 — Partial coverage dissolved by the register writing rule

Register items are written as logical blocks of work — no children, no task tree. A return covering less than an item is not a partial-coverage case; it is done with deviation or an issue, and reconciliation already handles it. This dissolves the old model's partial/blocked branch and the work-package coverage-ID mechanism.

## D13 — No convergence mechanism for the loop

A return can provoke a design change, which spawns commitments, which spawn handoffs. Nothing terminates this, and nothing should: every trip round the loop is provoked by something real. If issues keep coming, the loop is not failing — the design is being told something. The only addition is visibility: an item that has been round several times is a design smell worth surfacing.

## D14 — Domain-generic demoted from objective to constraint

"Domain-generic" invited creative-production reach when stated as an objective. Demoted to a constraint on how the objectives are written. The claim survives — the purpose and requirements are generic across kinds of work — but as a property of the specification, not a thing to pursue.

## D15 — Design is the default — authored forward, not derived from the old corpus

The old decision D15 ("design is knowledge, not a mandatory document pipeline") was reference material for reasoning already explored. It is not carried forward, amended, or downgraded. The position is restated from the new design: a design almost always exists, and a standard almost always has a design behind it. Authoring straight to standard is the exception. The design holds the reasoning; the standard holds the conclusion. Forcing everything into the standard alone compromises one or the other.

## D16 — Register admits non-design-generated work

The old D12 explicitly held the register is not exclusively design-generated. Under sole ownership by Project Design, the question was whether it still admits confirmed non-design work. Resolved: yes. Each item tags its origin as design-generated or directly-entered. The discipline that real design work should not bypass design is a judgement at entry, not a mechanism.

## D17 — The six-stage per-component review procedure

Adopted as a general procedure for every component review:

1. Clarify purpose.
2. Clarify objectives, model, approach.
3. Discuss and resolve key issues.
4. Review requirements, resolve changes.
5. Work through how the brief is delivered — the design.
6. Review design output — standards etc.

Stages 4 and 6 author forward first: derive requirements from purpose and objectives without reading the old design, then run a two-part sweep of the old corpus as a resource (omissions sweep, approach sweep). The old corpus never gets a default seat.

## D18 — Domains closed as a considered no

No case for domains was raised by anyone. The old corpus used "domain" for two jobs: asserting Project Design is not software-shaped (a genericness claim needing an adjective, not a noun) and naming an owner for production workflows (which topics already do). Domain would be a second ownership axis alongside topic with no stated relationship. The claim survives; the word does not.

## D19 — The binder sweep findings

### Omissions (part 1) — five carried, two dropped, one parked

**Carried:** (1) build is never handed conflicting current designs — ninth design criterion; (2) state the model compactly — design advice; (3) handoff sufficiency has a ceiling — handoff mechanism; (4) requirement distinct from implementation choice — fifth boundary test; (5) linked build project or build outcome — brief section.

**Dropped:** (6) cross-topic reconciliation — absorbed by capture and place; (7) no generic top-level workflow owner — partly implied by purpose, rest may contradict Working Practices.

**Parked then fallen away:** (8) one authoritative instance per scope — blocked on domains, which are now closed.

### Approach (part 2) — eight items adopted

(1) The document set is design, decisions, standard and work register — no index (deferred, not dropped). (2) Four-group design structure (model / definitions / rules / boundaries). (3) Rule weight markers lifted — vocabulary flagged to Standards. (4) Fenced pseudo-flow blocks lifted. (5) Proportionate field list named as a technique. (6) All binder-editing items resolve as decisions against the new documents. (7) The orientation section dropped entirely — direct contradiction with the forward design. (8) The semantic-hosting park falls away with domains.

### Decisions maintenance — no new mechanism needed

The locked decisions/knowledge rules already govern compaction, immutability, and maintenance. The old decisions document's sprawl (22 entries with superseded material reading as current, release-issuance entries recording nothing) is what the settled rules look like unapplied. Compaction is the maintenance mechanism; meaning changes are new entries; release-issuance entries never create entries at all.

## D20 — The work register lives inside the binder

The register is placed inside the binder rather than loaded separately. The old exclusion was carried from the old binder without being tested against the new model. The decisive argument is context cost: separate loading means every session loads binder plus working document plus register, multiplied by however many registers exist. The register is written at master update, which is when the binder rebuilds anyway — the two are already synchronised and there is no churn to avoid.

This is a placement decision. The register's operational semantics (fields, states, writing rule, immutability) are defined in the Design; how it is stored and when it is physically written are Documentation Methodology and Working Practices concerns that this decision informs.

## D21 — Pending content carries the authority of its destination

The working document holds pending content destined for master documents not yet updated. The two-tier model means a master document is not the complete current truth between updates — the current position is the master plus its pending content.

This does not conflict with doctype authority. The design document governs on conflict with decisions or knowledge — that is about the relationship between doctypes. Pending design content in the working document has the same authority as the design master it is destined for, because it is design content, not because it is in the working document. Pending decisions content has decisions-level authority. The tier changes where content lives, not what authority it carries.

Two consequences: the working document is always loaded with the topic; reading a master in order to act on it means checking its pending section first.

Not duplicated into each doctype — the property belongs to the two-tier memory model, not any one document type.

---

Version note: v2 — cross-review remediation: D2 origin qualified against D16 (PD-DEC1), D20 reframed as placement decision (PD-DEC3), D21 resolved against design authority model (PD-DEC4). 2026-09-11.
