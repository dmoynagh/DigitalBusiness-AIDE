# Project Design — Decisions

> **Version 3** (2026-09-01). Preserves the v2 reasoning/history and records the Review B refinement
> of the WorkRegister ownership boundary plus return-pending reconciliation preservation.
>
> Created: 2026-08-30 | Last modified: 2026-09-01

## D1 — Use Project Design rather than Design or Solution Design

**Decision.** The top-level methodology is named **Project Design**. `Design` remains a valid
artefact/stage within it.

**Reason.** Bare `Design` is overloaded while `Solution Design` is unnecessarily software-shaped.

## D2 — Project Design is domain-independent

**Decision.** Project Design defines reusable behaviour for determining substantial work, not a
software-development lifecycle or product-specific process.

## D3 — Domain production workflows remain domain-owned

**Decision.** Do not introduce a generic top-level Workflow owner for all production scenarios. The
substantive domain/top-level concern composes Project Design, Build and other AIDE services.

## D4 — Project Design and Build form an iterative loop

**Decision.** The generic handoff is Design Outcome → WorkPackage → Build → Outcome, with the return
reconciled by the design/work owner.

## D5 — Layered overviews are a design-control mechanism

**Decision.** For substantial design, establish compact intent/system and model layers before deep
mechanics.

## D6 — Confirmed Design creates an explicit delivery obligation where outcomes must change

**Trigger / problem.** Once Design is changed, the committed current position can diverge from code,
built artefacts or other production outcomes. Without an explicit record, later readers cannot tell
which design changes have actually been implemented.

**Alternatives considered.** Put implementation status in Design; rely on WorkPackage history;
leave consequences to memory/current chat.

**Decision.** After a substantive Design change, identify every material downstream consequence.
If a consequence is not fully delivered in the same pass, record it in the owning top-level topic's
WorkRegister with enough detail to verify eventual delivery.

**Reason.** Design should remain the clean current model while WorkRegister truthfully represents
the gap between commitment and delivered reality.

## D7 — WorkRegister is not merely a backlog

**Decision.** Treat WorkRegister as the live undelivered-design-consequence ledger. A row records the
committed change, required downstream change(s), target outcome, delivery state, WorkPackage mapping,
returned result when still open and remaining work.

**Consequence.** Completed rows are removed after reconciliation; durable reasoning/evidence remains
with Design/Decisions/Outcome where it belongs.

## D8 — WorkPackages select manageable portions of WorkRegister obligations

**Decision.** One WorkPackage may group all/part of several WorkRegister items, and one large item
may require several WorkPackages.

**Reason.** The register should represent obligations at the useful design-consequence level while
Build execution can be chunked for safe/manageable delivery.

## D9 — Build return is reconciled against the source obligations

**Decision.** On Outcome return, the director reconciles mapped WorkRegister items. Complete items
are removed; partial/blocked items retain returned evidence and remaining work; design-level
feedback returns to Project Design.

**Boundary.** Build does not silently close WorkRegister state owned by the top-level topic.

## D10 — Correct the Project Design container path

**Decision.** The current physical/master folder is `AIDE/Project Design/`. Earlier
`AIDE/Design Project/` references were factual documentation/configuration errors, not a historical
rename.

## D11 — Issue Project Design v2

**Decision.** Publish the strengthened contract as `AIDE_ProjectDesign@v2`, migration posture
`None`.

**Reason.** The release changes future design/delivery behaviour but does not require rewriting
historical WorkPackages or Design documents.


## D12 — Project Design owns the Design→WorkRegister producer rule, not the whole admission boundary

**Trigger / problem.** Review B identified that D7's phrase “live undelivered-design-consequence
ledger” correctly described Project Design's use of WorkRegister but was too narrow if read as the
general WorkRegister type/admission boundary.

**Alternatives considered.** Keep WorkRegister exclusively Design-generated; move all WorkRegister
semantics into Project Design; weaken the consequence guarantee to avoid overlap.

**Decision.** Documentation Methodology owns the general WorkRegister type/admission semantics:
WorkRegister holds confirmed work owed by the owning top-level topic and not yet fully delivered.
Project Design owns a mandatory producer rule: after every substantive confirmed Design change,
identify material downstream consequences and either fully deliver each consequence in the same
pass or create/update the owning top-level topic's WorkRegister.

**Clarification of D7.** D7 remains historical and its “undelivered-design-consequence ledger”
wording remains valid for the Design-produced subset, but it is no longer the exclusive definition
of what may be admitted to WorkRegister.

**Boundary.** WorkRegister is still not a generic backlog. Unresolved ideas/possible work remain
outside it. Confirmed non-Design work is not invalid merely because its producer is not Project
Design. A WorkPackage may still be defined directly where no register item is needed.

## D13 — Preserve a returned-pending state before leaving unreconciled Outcome context

**Trigger / problem.** A mapped Build Outcome can be received at a point where the directing owner
cannot finish WorkRegister reconciliation in the same uninterrupted step. Without a compact state
change, the register may still look as though execution has not returned.

**Decision.** Before leaving that context, set/update the owning mapped item(s) to
`Returned — reconciliation pending` and point to the Outcome. Keep detailed evidence in Outcome.
Project Design/the directing owner later reconciles and closes/removes the obligation; Build does
not close it.

**Reason.** This preserves truthful live state without duplicating Outcome evidence or adding a new
mechanism.

## D14 — Issue Project Design v3

**Decision.** Publish the Review B refinement as `AIDE_ProjectDesign@v3`, migration posture `None`.

**Reason.** The release clarifies ownership/admission semantics and return-state preservation while
retaining the existing Design consequence guarantee, many-to-many WorkRegister→WorkPackage mapping,
and reconciliation model.

---
Dependencies: !AIDE_DocumentationMethodology@v21, ProjectDesign_Design_v3
References: AIDE_WorkPackage@v2, Build_Decisions_v4
