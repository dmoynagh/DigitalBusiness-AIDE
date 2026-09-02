# Principles — Decisions

> **Version 3** (2026-08-31). Preserves the original top-level Principles decision and records the
> current separation, standalone/base-guidance model and Domain reconciliation.
>
> Created: 2026-08-27 | Last modified: 2026-08-31

## D1 — Principles established as a top-level topic

**Decision.** Principles is a cross-cutting concern applying to every project and scenario. It is
a top-level topic, not a subtopic of Workflow or Capabilities. It will produce a published Standard
as an outcome.

**Reason.** It was previously parked in Workflow because that was where the conversation happened.
Its scope is universal.

## D2 — Principles is independently deployable

**Decision.** `AIDE_Principles@v1` works both as part of AIDE and on its own.

**Reason.** Base reasoning guidance is useful in general AI sessions that are not doing software
development or other full-AIDE work.

## D3 — Principles is base guidance, not a personalised final configuration

**Decision.** The canonical Standard defines the portable default.

**Rejected alternative.** Put user/team preferences directly into the base Standard. Rejected
because the base would stop being portable and every consumer would inherit one party's local
choices.

## D4 — Guidance Profiles specialise the base by delta

**Decision.** Organisation/group/team/user Guidance Profiles may Add, Refine or explicitly Override
named base guidance.

**Reason.** Small deltas preserve a coherent common base and avoid copied forks.

**Consequence.** Unmentioned base guidance remains effective. Equal-specificity contradictions fail
visibly unless explicitly ordered.

## D5 — Do not create a generic profile subsystem yet

**Decision.** Principles and Working Practices share the same conceptual profile model, but no new
top-level profile component is created now.

**Reason.** These are the demonstrated consumers; wider generalisation should wait for further
evidence.

## D6 — Principles and Working Practices are sibling top-level concerns

**Decision.** Working Practices is not a child of Principles.

**Reason.** Principles owns judgement premises; Working Practices owns practical cross-surface
collaboration/operation conventions. Both can be independently useful.

## D7 — Replace declaration-over-inference wording with authoritative evidence

**Trigger / problem.** The original seed said “Domains are declared, not detected.” The confirmed
Core Domain model now permits implicit Domains resolved from recognised authoritative structures.

**Alternatives considered.**

- Keep the seed wording as a historical rule. Rejected because it directly contradicts
  `AIDE_Domain@v1`.
- Remove the principle entirely. Rejected because its deeper intent—rejecting accidental
  presence/proximity inference—remains valuable.

**Decision.** Replace it with **Authoritative evidence over incidental inference**.

**Consequence.** Model-defined inference from authoritative structure is permitted; casual
proximity/naming inference remains rejected.

## D8 — Operational seed behaviours move without loss

**Decision.** Concrete behaviours such as coded-reference glossing, verification before assertion
and no-silent-state-change behaviour are represented in Working Practices.

**Reason.** They remain valuable but are operational conventions rather than root reasoning
premises.

## D9 — Preserve the human-comprehensible working set

**Decision.** Principles continues to require layered modelling before detailed elaboration.

**Reason.** Human participation in architecture depends on being able to hold and challenge the
current model.

---
Dependencies: !AIDE_DocumentationMethodology@v19, Principles_Design_v3
References: WorkingPractices_Decisions_v2, Core_Domain_Decisions_v1
