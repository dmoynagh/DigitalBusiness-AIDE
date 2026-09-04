# Project Design — Decisions

> **Version 2** (2026-08-31). Preserves the initial Project Design decisions and records the
> WorkRegister consequence/reconciliation contract plus the physical naming correction.
>
> Created: 2026-08-30 | Last modified: 2026-08-31

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

---
Dependencies: !AIDE_DocumentationMethodology@v21, ProjectDesign_Design_v2
References: AIDE_WorkPackage@v2, Build_Decisions_v4
