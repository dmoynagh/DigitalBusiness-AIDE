# Project Design Binder

> **Generated Binder — do not edit directly.** Edit the individual master documents and regenerate the Binder.
> **Binder Version 6** (2026-09-03). Corrects the v4/v5 release-lineage explanation on top of the current Project Design v6 orientation model.

This Binder is a current-context consumption artefact; authoritative masters remain individual files.

## Binder manifest

- `ProjectDesign_Index_v7.md` — sha256 `3882d3bf560b`
- `ProjectDesign_Design_v7.md` — sha256 `a3772d6c0214`
- `ProjectDesign_Decisions_v5.md` — sha256 `ad7f2b358062`
- `AIDE_ProjectDesign_Standard_v6.md` — sha256 `b33781fa444d`

---

<!-- BEGIN SOURCE: ProjectDesign_Index_v7.md -->
# Project Design — Index

> **Version 7** (2026-09-03). Registers the corrected v4/v5 release-lineage explanation; canonical Project Design remains v6.
>
> Created: 2026-08-30 | Last modified: 2026-09-03

`{scope: "AIDE/Project Design", type: DocumentationTopic}`

## Contents

- **Project Design** — generic methodology for defining substantial work and reconciling committed
  Design with downstream delivery.  
  `{standard: AIDE_ProjectDesign@v6}`

## Documentation

### Top-level topic

| Name | Parent topic | Filename prefix | Inheritance | Mode |
|---|---|---|---|---|
| Project Design | AIDE | `ProjectDesign` | independent | expanded |

### Document register

| Document | Version | Type | Status |
|---|---:|---|---|
| `ProjectDesign_Index` | v7 | Index | Current |
| `ProjectDesign_Design` | v7 | Design | Current |
| `ProjectDesign_Decisions` | v5 | Decisions | Current |
| `AIDE_ProjectDesign_Standard` | v6 | Standard | Current; identity `AIDE_ProjectDesign@v6` |

### Binder boundary

One top-level Project Design Binder; live WorkRegister remains separate.

### Live state

- `ProjectDesign_WorkRegister` — WorkRegister live series; load separately from the stable Binder
  when current outstanding delivery obligations need to be managed.

### Container

Current repository-relative master folder:

```text
Documentation/Project Design/
```

The active AIDE repository supplies the repository root. Repository-relative placement remains
authoritative if a local checkout path changes.

### Local configuration

None.

---
Dependencies: !AIDE_DocumentationMethodology@v28, AIDE_Index@v2
References: ProjectDesign_Design_v7, AIDE_ProjectDesign@v6, AIDE_WorkPackage@v3
<!-- END SOURCE: ProjectDesign_Index_v7.md -->

---

<!-- BEGIN SOURCE: ProjectDesign_Design_v7.md -->
# Project Design — Design

> **Version 7** (2026-09-03). Corrects the release-lineage explanation for v4/v5 while preserving current Project Design v6 semantics.
>
> Created: 2026-08-30 | Last modified: 2026-09-03

## Contents

- **Purpose and operating model** — Project Design's boundary, lifecycle flow and principal concepts. §1–§3
- **Design quality and authority** — layered design, decision discipline, current authority and proportionate structure. §4–§7
- **Review, handoff and reconciliation** — independent assessment, WorkPackage handoff and Build return. §8–§10
- **Flexible contribution model** — many-to-many Design contributions, permitted section hosts and cross-Topic work. §11–§12
- **Document orientation** — Design/Brief Summary coverage and when to create or rely on Overview. §13

## Summary

Project Design establishes what substantial work is intended to achieve, why, under which
requirements and constraints, and what current model or approach has been confirmed before
execution. It separates design authority from Build execution: confirmed Design identifies any
undelivered downstream consequences, WorkRegister preserves those obligations, WorkPackage bounds
an executable slice, and the returned Outcome is reconciled by the owning design process.

Design is confirmed knowledge rather than a mandatory one-document-per-output pipeline. A work area
may use zero, one or several reconciled Design documents or semantic sections, and may author the
proper authoritative outcome directly when intermediate prose would only duplicate it. Current
contributions must not conflict materially, and Build must not choose among unresolved designs.

Substantial Design documents normally use a semantic Contents map and a genuine high-level Summary.
The Summary communicates the objective, model, major relationships, key logic and boundaries while
the body retains the detailed authority. If adequate high-level coverage would materially duplicate
or bloat the Design, an Overview should carry the fuller high-level representation. A current
Overview permits a smaller Design Summary but does not remove the Design's minimum self-orientation.

## §1 — Purpose and boundary

Project Design defines **what is to be achieved, why, under what requirements/constraints, and what
approach/outcome has been determined** before execution is handed to Build.

It is generic across software, documentation, capability development, business/process work,
creative production and other substantial work.

Project Design owns the reusable design method. It does not execute the work and does not own the
physical container in which the topic happens to be discussed.

## §2 — Core model

```text
Intent / need
    ↓
Brief / requirements / constraints
    ↓
Decisions + current model/approach
    ↓
Design (committed current state)
    ↓
identify downstream consequences
    ↓
fully delivered now? ── yes → reconciled
    │
    no
    ↓
WorkRegister
    ↓
select manageable work chunk(s)
    ↓
WorkPackage(s)
    ↓
Build
    ↓
Outcome
    ↓
reconcile WorkRegister
    ├── complete → remove item
    └── partial/blocked/design issue → retain/update or revise Design
```

## §3 — Principal concepts

### Intent / Brief

States the objective, need, scope, success conditions and important non-goals. Ceremony is
proportionate to stakes.

### Requirements and constraints

States what the outcome must satisfy. Requirements remain distinct from implementation choices.

### Decisions

Records material design choices, credible rejected alternatives, reasoning and consequences.
Decisions informs future Design; downstream delivery consumes the current Design/defined outcome.

### Design

The authoritative current model/approach, which may be represented by one or several reconciled Design contributions or directly in another authoritative semantic owner. Every consideration downstream work must honour is present in a current authoritative input.

### WorkRegister consequence

Documentation Methodology owns the general WorkRegister type/admission semantics: WorkRegister holds
confirmed work owed by the owning top-level topic and not yet fully delivered.

Project Design owns one mandatory producer rule into that general type. A confirmed Design change is
a **commitment** to the current model. If that commitment requires code, build, document,
deployment-input or another produced outcome to change and the consequence is not fully delivered in
the same pass, the owning top-level topic records the consequence in WorkRegister.

The consequence must be described in sufficient detail to determine later whether the production
outcome actually caught up with the Design.

Project Design does not define WorkRegister as exclusively Design-generated work and does not make it
a generic backlog. Other confirmed work may be valid there under its governing owner/type contract;
unresolved ideas, possible work and unconfirmed attention remain outside WorkRegister.

### WorkPackage

WorkPackage is a bounded execution contract built from some or all relevant WorkRegister
obligations (or directly defined work where no register item is needed).

### Review

Independent Review applies under `AIDE_Review` where required/configured/materially useful. Review
does not take design ownership.

## §4 — Layered design control

For substantial design, establish a compact two-layer checkpoint before deep mechanics:

1. **Intent/system** — purpose, premises, ownership/boundaries, inputs/outputs, surrounding
   relationships.
2. **Model** — principal concepts, responsibilities, relationships, lifecycle/flow, major rules.

If this cannot be made clear, reassess the model before adding machinery.

## §5 — Domain-owned workflows

A domain/top-level work concern owns the workflow that composes Project Design, Build, Review and
other AIDE services. Project Design supplies the generic design behaviour only.

## §6 — Consequence capture rule

After each substantive confirmed Design change:

1. identify downstream outcomes affected;
2. identify the concrete changes required in each outcome;
3. if all are delivered/verified in the same pass, no Design-generated WorkRegister obligation
   remains; and
4. otherwise create/update the owning top-level topic's WorkRegister with the undelivered
   consequence(s).

A Design-generated WorkRegister item should identify, proportionately:

- source Design/decision;
- committed change;
- required implementation/output changes;
- target outcome/location;
- current state; and
- later WorkPackage/result/remaining information.

Do not leave a confirmed Design change with an implicit “implementation later” assumption.

This rule is a Project Design producer guarantee. It does not redefine or limit other WorkRegister
admission permitted by Documentation Methodology.

## §7 — Handoff to Build

When execution is required, create/authorise a WorkPackage conforming to `AIDE_WorkPackage@v3`.

If sourced from WorkRegister, identify the covered register item IDs and the portion of each
obligation included in this manageable work chunk.

Build should not need Decisions history to reconstruct the intended result.

## §8 — Return and reconciliation

Build returns an Outcome stating actual work, produced/changed state, validation, deviations,
unresolved work and design feedback.

Project Design/director then:

- confirms acceptance where the defined result is satisfied;
- reconciles each mapped WorkRegister item;
- removes a fully delivered WorkRegister item;
- records returned result/remaining work on any item still outstanding;
- resolves design-shaping feedback and issues revised/further work; or
- explicitly accepts a residual difference/risk within authority.

If a mapped Outcome is received and reconciliation cannot be completed in the same uninterrupted
step, before leaving that context preserve a compact `Returned — reconciliation pending` state on
the owning WorkRegister item(s) with a pointer to the Outcome. Keep detailed execution evidence in
the Outcome rather than duplicating it into the register. Reconciliation is completed by Project
Design/the directing owner when work resumes; Build does not close the obligation.

Execution evidence is input to reconciliation; it does not silently rewrite Design.

## §9 — Simplicity and escalation

Routine reversible implementation detail belongs to Build authority. Changes to objective, major
scope, acceptance, ownership, architecture or policy return to Project Design.

When implementation accumulates compensating exceptions, test whether a simpler model/boundary/
requirement removes the complexity first.

## §10 — Intended output

```text
AIDE_ProjectDesign@v6
```

Migration posture is `None`: v6 adds prospective Design/Brief orientation and the Overview
escalation rule without requiring mass rewriting historical Design, Brief or Overview documents.

Release-lineage clarification: `AIDE_ProjectDesign@v4` was the WorkPackage preflight correction to
the current `AIDE_WorkPackage@v3` handoff target; `AIDE_ProjectDesign@v5` added flexible Design
contributions, semantic-section hosting and direct cross-Topic reconciliation; v6 then added the
current Design/Brief orientation model. This Design-document v7 corrects the explanation only and
does not create another semantic Project Design release.


## §11 — Design contributions and semantic-section hosting

Design is confirmed knowledge, not a mandatory one-document-per-output pipeline. A work area may
use zero, one or several Design documents/sections where the authoritative outcome can be written
directly to its proper owner without duplicative Design prose.

One Design contribution may affect several outputs; one output may aggregate several Design
contributions. Contributions may be whole documents or identified sections. Current contributions
must not conflict materially; reconcile conflict before Build rather than asking Build to choose.

Brief, Purpose, Requirements and Considerations are semantic sections. Their baseline Project
Design meaning remains stable while a domain Standard may permit them in a domain control document
such as Capability Definition. Keep one authoritative instance for each scope and externalise only
when size, lifecycle, retrieval, reuse or complexity warrants it.

## §12 — Cross-Topic reconciliation

Topic ownership identifies the baseline and durable destination. It does not require the work to be
performed in the owning Topic's physical context. A sufficiently sourced and authorised Working
Context may reconcile a coordinated design across Topics. Use Project Handoff only when a genuine
transfer boundary exists under Working Practices.

## §13 — Design, Brief and Overview orientation

Project Design consumes the generic Contents/Summary semantics from Documentation Methodology and
defines their use for its DocTypes.

A substantial **Design** should normally expose:

- Contents — a concise semantic map of significant design information and stable section locations;
  and
- Summary — enough high-level coverage for a reader to understand the objective, overall model or
  approach, principal components/relationships, important logic and boundaries without first
  reading the complete detailed sequence.

Summary depth is proportionate. The body remains the complete authoritative design and carries the
supporting reasoning, precise rules, exceptions and implementation detail. A current related
Overview may reduce the Design Summary to essential objective/model/boundary orientation plus a
clear Overview reference, but someone opening the Design directly must still understand what it is
and how its detail fits together.

If a useful high-level Design representation cannot be expressed proportionately without materially
duplicating or bloating the Design, create an **Overview** rather than continuing to enlarge the
Summary. An Overview may also be created directly on explicit user/work-owner instruction. It is a
purposeful independent document, not only an overflow artefact, and normally does not need its own
Summary because high-level explanation is its primary role.

A substantial **Brief** may use a shorter Summary covering objective/need, scope/boundaries, major
requirements/outcomes and intended result. Small Briefs or Designs whose whole content is already
immediately scannable may omit either section under the value/readability test.

---
Dependencies: !AIDE_DocumentationMethodology@v28, AIDE_Review@v4, AIDE_WorkPackage@v3
References: ProjectDesign_Decisions_v5, Build_Design_v9
<!-- END SOURCE: ProjectDesign_Design_v7.md -->

---

<!-- BEGIN SOURCE: ProjectDesign_Decisions_v5.md -->
# Project Design — Decisions

> **Version 5** (2026-09-02). Records Design/Brief Summary depth and the Summary-to-Overview escalation rule.
>
> Created: 2026-08-30 | Last modified: 2026-09-02

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


## D15 — Design is knowledge, not a mandatory document pipeline

A domain may use zero, one or many Design documents/sections. Direct authorship to the correct
authoritative outcome is valid where an intermediate Design would duplicate it.

## D16 — Design contributions are many-to-many

One contribution may affect several outcomes and one outcome may aggregate several contributions.
Build does not resolve material conflicts among current contributions.

## D17 — Brief and Requirements are semantic sections

Their Project Design meaning is stable while domain Standards may permit compact hosting inside a
domain control document. Each scope retains one authoritative instance.

## D18 — Topic ownership does not fix work location

Cross-Topic design may be reconciled directly in a sufficiently sourced/authorised Working Context;
Handoff is reserved for genuine transfer boundaries.

## D19 — Issue Project Design v5

Publish `AIDE_ProjectDesign@v5`, posture `None`. Existing valid Design documents remain valid; the
release removes mandatory duplication prospectively.

## D20 — Design Summary provides genuine high-level understanding

**Decision.** A substantial Design normally uses Documentation Methodology Contents and Summary.
Its Summary covers the objective, overall model/approach, principal relationships, key logic and
boundaries deeply enough to orient a reader without requiring the full detailed sequence. A
substantial Brief may use a shorter objective/scope/requirements/outcome Summary.

## D21 — Overview carries disproportionate high-level representation

**Decision.** If an adequate Design Summary would materially duplicate or bloat the Design, create
an Overview. A user/work owner may also instruct Overview creation directly. Where a current
Overview exists, the Design Summary may be smaller but retains minimum self-orientation and points
to the Overview for the fuller high-level model.

## D22 — Issue Project Design v6 prospectively

**Decision.** Publish `AIDE_ProjectDesign@v6` with transition posture `None`. Apply the new
orientation posture to new or substantively updated Design/Brief documents where it adds value; do
not mass-rewrite otherwise-current documents solely to insert sections.

---
Dependencies: !AIDE_DocumentationMethodology@v28, ProjectDesign_Design_v6
References: AIDE_WorkPackage@v3, Build_Decisions_v6
<!-- END SOURCE: ProjectDesign_Decisions_v5.md -->

---

<!-- BEGIN SOURCE: AIDE_ProjectDesign_Standard_v6.md -->
# AIDE Project Design — Standard

> **Identity:** `AIDE_ProjectDesign@v6`
> **Common name:** Project Design
> **Version 6** (2026-09-02). Defines Design/Brief orientation and the Summary-to-Overview escalation rule.
>
> **Default weight:** Expectation

---

## Contents

- **Establish and record the work** — proportional definition, layered checkpoints and authoritative state.
- **Delivery control** — WorkRegister consequences, Review, WorkPackage handoff and Outcome reconciliation.
- **Design contribution model** — flexible authoritative hosts and cross-Topic reconciliation.
- **Document orientation** — Design/Brief Contents and Summary, and when Overview is warranted.

## Summary

Project Design turns intent and requirements into a coherent current model before execution. It
keeps the Design owner responsible for confirmed meaning and downstream consequences while Build
executes only a bounded WorkPackage and reports evidence for owner reconciliation.

Design may be represented through one or several reconciled documents/sections or directly in the
proper authoritative outcome. Substantial Design documents normally provide a semantic Contents map
and a high-level Summary; if that representation would become disproportionate, a separate Overview
carries the fuller high-level model.

## Purpose

Define substantial work coherently before execution: establish intent and requirements, determine the current model/approach, review proportionately, and hand execution to Build through a complete WorkPackage where needed.

## Apply proportionately

Use the amount of structure justified by consequence, reach, reversibility and uncertainty. Small clear tasks do not require ceremony merely to imitate a large project.

## Establish the work

For work that needs design, establish enough of the following to remove material ambiguity:

- objective/need and intended outcome;
- authorised scope and non-goals;
- requirements and constraints;
- material assumptions/uncertainties;
- decisions and credible alternatives where consequential;
- the current design/model/approach; and
- defined deliverables or acceptance signals.

Do not allow detailed implementation to become the place where unresolved design is silently decided.

## Use a layered checkpoint for substantial design

Before descending into extensive mechanics, maintain a compact view of:

1. **Intent/system:** purpose, premises, ownership/boundaries, inputs/outputs and surrounding relationships.
2. **Model:** principal concepts, responsibilities, relationships, lifecycle/flow and major rules.

If this view is difficult to make clear, reassess the model before adding mechanisms.

## Record authoritative state

Design/Definition/Standards/Tools hold the applicable current confirmed position. Decisions retains material evolutionary reasoning and rejected alternatives. Downstream outcomes consume current authoritative inputs, not Decisions history.

Confirmed material must be written according to the governing Documentation Methodology rather than left only in conversation.

## Track undelivered Design consequences

**Weight: Requirement**

Documentation Methodology owns the general WorkRegister type/admission semantics. Project Design
owns the following mandatory producer guarantee.

Whenever the confirmed Design changes, identify the downstream outcomes that must change for
delivered reality to remain aligned.

For each material consequence:

```text
fully delivered in the same pass → no Design-generated standing obligation remains
not fully delivered               → record/update it in the owning top-level topic's WorkRegister
```

The WorkRegister entry must state the source Design change and required downstream code/build/
document/production changes in enough detail that later delivery can be reconciled.

This producer rule does **not** define WorkRegister as exclusively Design-generated work. Confirmed
non-Design work may also belong there under the governing WorkRegister/type contract. WorkRegister
is still not a generic backlog: unresolved ideas, possible work and unconfirmed attention remain
outside it.

## Review

Use `AIDE_Review` when required by the governing workflow/Standard/WorkPackage or when an independent reasoning path is expected to add material value. The Lead retains design ownership and Finding disposition.

## Handoff to Build

When execution is required, provide a WorkPackage conforming to `AIDE_WorkPackage@v3`.

A WorkPackage may be created directly from defined work or select manageable portions of one or
more WorkRegister obligations. Where it is sourced from WorkRegister, identify the source item IDs
and the portion of each obligation covered.

The package must make the required result, authority, work-specific inputs and acceptance clear.
WorkRegister references are traceability, not a substitute for a self-contained execution contract.
Do not embed generic execution-platform knowledge already supplied by the Build environment.

## Handle Build return

**Weight: Requirement**

On Build Outcome:

- reconcile returned evidence against each mapped WorkRegister obligation where applicable;
- remove a WorkRegister item only when its full confirmed obligation is actually delivered;
- retain partial/blocked items with returned result and remaining work;
- close/record completion when acceptance and the committed outcome are satisfied;
- resolve returned design questions before authorising changed execution; or
- record an authorised residual difference/risk.

If a mapped Outcome is received and reconciliation cannot be completed in the same uninterrupted
step, before leaving the context preserve a compact `Returned — reconciliation pending` state on
the owning mapped item(s) and point to the Outcome. Detailed evidence remains in Outcome rather
than being duplicated into WorkRegister.

Project Design/the directing owner reconciles and closes the obligation. Build reports evidence;
it does not silently close the owning WorkRegister.

Build may resolve implementation detail within authority; it does not silently change objectives,
major scope, acceptance or architecture.

## Keep the model simple

When implementation begins accumulating exceptions or compensating machinery, test whether a simpler model, boundary or requirement removes the complexity before adding another mechanism.

```yaml
MigrationSummary:
  CurrentVersion: v6
  LatestRequiredVersion: none
  LatestOnUpdateVersion: none

Transition:
  Version: v1
  Posture: None

Transition:
  Version: v2
  Posture: None

Transition:
  Version: v3
  Posture: None

Transition:
  Version: v4
  Posture: None
```


## Design contributions and hosts

Design is confirmed knowledge, not a required one-document-per-output chain. Use zero, one or many
Design documents/sections proportionately. Directly author the proper authoritative outcome when an
intermediate Design would only duplicate it.

One contribution may affect several outputs; one output may aggregate several contributions. If
current contributions conflict materially, reconcile them before Build. Build must not choose.

Brief/Purpose, Requirements and Considerations are semantic sections. A domain Standard may permit
compact hosting in a domain control document while retaining one authoritative instance per scope.
Externalise only when size, lifecycle, retrieval, reuse or complexity warrants it.

## Cross-Topic work

Topic ownership determines authoritative baseline and destination, not physical work location. A
sufficiently sourced and authorised Working Context may reconcile several Topics. Use Project
Handoff only where Working Practices identifies a real transfer boundary.

## Design and Brief orientation

Consume the generic Contents/Summary semantics from `AIDE_DocumentationMethodology`.

For a substantial Design, normally provide Contents plus a Summary covering the objective, overall
model/approach, principal relationships, important logic and boundaries. The Summary should provide
genuine high-level understanding while the body retains precise authority and implementation detail.

If useful coverage would materially duplicate or bloat the Design, create an Overview. Create one
also when the user/work owner explicitly instructs it. A current Overview may reduce the Design
Summary to essential self-orientation and a clear reference, but does not remove it entirely.

A substantial Brief may use a shorter Summary of objective/need, scope/boundaries, major
requirements/outcomes and intended result. Omit these sections for small/immediately scannable
documents or where they fail Documentation Methodology's value/readability test.

```yaml
Transition:
  Version: v5
  Posture: None

Transition:
  Version: v6
  Posture: None
```

---
Dependencies: !AIDE_DocumentationMethodology@v28, ProjectDesign_Design_v6, AIDE_Review@v4
References: AIDE_WorkPackage@v3
<!-- END SOURCE: AIDE_ProjectDesign_Standard_v6.md -->
