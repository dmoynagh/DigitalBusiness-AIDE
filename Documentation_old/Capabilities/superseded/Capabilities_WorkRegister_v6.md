# Capabilities — Work Register

> **Version 6** (2026-08-28). Reconciled after the parent architecture rewrite. Retires or
> revises work based on superseded ownership, adds the five newly explicit component designs,
> and records child-design reconciliation and shared contract work.
>
> Created: 2026-08-27 | Last modified: 2026-08-28

---

## WR1 — DocMeth: Overview type and document metadata

**Status:** Closed — present in `DocumentationMethodology_Guide` v17
**Raised:** 2026-08-27
**Closed:** 2026-08-28 reconciliation

The uploaded DocMeth v17 already defines Overview as an established type and created/last-modified
metadata. No duplicate message or change is required. Whether these remain appropriately shared
is recorded as `DR5` in `Capabilities_DocMethReviewItems` v1.

---

## WR2 — Continue baseline re-admission

**Status:** Superseded by parent architecture rewrite
**Raised:** 2026-08-27

The new parent Brief, Design, and Overview restate Capabilities from the confirmed architecture
rather than continuing block-by-block re-admission. Older corpus remains available as design
history. Any later recovery of a specific requirement must be justified against the current
component boundaries.

---

## WR3 — Principles topic: produce a standard

**Status:** Moved outside Capabilities
**Raised:** 2026-08-27

Principles remains a separate top-level topic under `D8`. Its production work belongs in that
topic and is not tracked as active Capabilities work.

---

## WR4 — Standards outputs: Production and Usage standards

**Status:** Open — revised
**Raised:** 2026-08-27
**Revised:** 2026-08-28

Reconcile the Standards child Brief and Design with the parent architecture, then produce first
drafts of:

- the generic **Standards Production Standard**;
- the generic **Standards Usage Standard**.

The Production Standard governs standards, not Deployment. The Usage Standard owns runtime use
behaviour and is not AIDE-scoped. Both consume Scope, Dependencies, Migration, and Review rather
than redefining their shared mechanisms.

**Depends on:** `WR18`; enough of `WR14`–`WR17` to reference stable component contracts.

---

## WR5 — AIDE-scoped runtime standard

**Status:** Superseded by `D51`; absorbed into `WR4`
**Raised:** 2026-08-27

Do not produce an AIDE-scoped runtime standard. Produce the generic Standards Usage Standard.

---

## WR6 — Tools production standard decision

**Status:** Open — revised
**Raised:** 2026-08-27
**Revised:** 2026-08-28

During Tools child-design reconciliation, decide whether Tools publishes a standalone Tools
Production Standard. The decision must be based on what Tool authors need, not on the earlier
assumption that the Standards Standard governs both capability kinds. Include contributed
commands in the Tool model (`D52`).

**Depends on:** `WR19`.

---

## WR7 — Migration transition standard(s)

**Status:** Open — revised
**Raised:** 2026-08-28
**Revised:** 2026-08-28

Define how dependency owners author transition instructions, including identity, version range,
applicability, ordered steps, success/failure reporting, and judgment/escalation. Required
Migration and On-Update content must be separate artefacts or package members (`D47`).

Decide within Migration design whether one production standard can govern both distinct
artefacts without obscuring their postures.

**Depends on:** `WR16`, `Q12`.

---

## WR8 — Build `/migrations-check`

**Status:** Open — revised
**Raised:** 2026-08-28

Build the diagnostic Tool for pending Required Migrations. Platform enumeration and trigger
details must come from the relevant Scope/Migration platform design, not from the parent
architecture.

**Depends on:** `WR16`, `WR7`, `WR10` where the target platform requires the probe.

---

## WR9 — Build `/migrations-apply`

**Status:** Open — revised
**Raised:** 2026-08-28

Build the Tool that applies authorised Required Migrations in order. It must not absorb
On-Update behaviour, which belongs to `/update-doc` and the automatic modification path.

**Depends on:** `WR16`, `WR7`, `WR8`.

---

## WR10 — Probe platform metadata visibility

**Status:** Open — platform evidence
**Raised:** 2026-08-28

Test what installed plugin/capability identity and version data an AI can inspect on each target
platform. Record results in platform reference/design material. The older
`{key}_pendingmigrations` convention is one candidate for Claude, not a generic contract.

**Feeds:** `Q9`, Scope/Dependencies/Migration platform designs.

---

## WR11 — Package manifest document type

**Status:** Withdrawn from DocMeth batch; replaced by `WR20`
**Raised:** 2026-08-28

Define the package/manifest contract locally in Capabilities first. Consider promotion to a
shared DocMeth type only if reuse beyond Capabilities is demonstrated (`D53`, `DR4`).

---

## WR12 — Build record document type

**Status:** Withdrawn from DocMeth batch; folded into `WR20`
**Raised:** 2026-08-28

Define any build/deployment record locally with the production and Deployment contracts. Do not
promote it to DocMeth solely because the record is represented as a document (`D53`, `DR4`).

---

## WR13 — Deployment component design

**Status:** Open — revised
**Raised:** 2026-08-28
**Revised:** 2026-08-28

Design Deployment from the completed package boundary through platform preparation and
distribution/publication. Cover package validation, platform selection, divergence application
where it belongs, removals, partial failure, resumption, idempotency, and clear rejection of
defective packages.

Do not include capability build/package or host pickup as Deployment-owned stages.

**Depends on:** `D49`, `D50`, `WR20`.

---

## WR14 — Scope component design

**Status:** Open
**Raised:** 2026-08-28

Create the Scope Brief and Design. Preserve the mechanical/context model, define the logical
scope contract, and specify how platform designs render trigger and discovery cues. Produce the
revised trigger inventory from `Q10` without embedding platform techniques in the parent.

**Depends on:** `D43`, `D45`, `D50`.

---

## WR15 — Dependencies component design and Standard

**Status:** Open
**Raised:** 2026-08-28

Create the Dependencies Brief and Design, then define the Dependencies Standard. Cover identity,
declared version meaning, dependency/reference distinction, availability checks, version gaps,
declaration advancement, and document-footer rendering. Coordinate the DocMeth consequences via
`Capabilities_DocMethReviewItems` v1 without editing DocMeth in this work.

**Depends on:** `D43`, `D46`. Feeds `Q12` and `WR20`.

---

## WR16 — Migration component design and `/update-doc`

**Status:** Open
**Raised:** 2026-08-28

Create the Migration Brief and Design. Define separate Required Migration and On-Update
artefacts, transition ordering, author/executor boundaries, AI-oriented automatic triggering,
and the command set. Specify and then build idempotent `/update-doc`, including no-op reporting
and required-migration stop/defer behaviour.

**Depends on:** `D43`, `D47`, `D48`, `WR14`, `WR15`. Coordinates the version interface through
`Q12` and `WR20` without waiting for a final cross-component schema.

---

## WR17 — Review component design

**Status:** Open
**Raised:** 2026-08-28

Create the Review Brief and Design. Define lead/reviewer responsibilities, finding/remedy
separation, review profiles, evidence, dispositions, iteration, and the outcome/tool set. Resolve
`Q14` without coupling roles permanently to a model or domain.

**Depends on:** `D43`, `D44`.

---

## WR18 — Reconcile Standards child corpus

**Status:** Open
**Raised:** 2026-08-28

Rewrite `Capabilities_Standards_Brief` v1 and `Capabilities_Standards_Design` v3 against parent
Design v2. Remove AIDE-scoped Usage ownership, shared Scope machinery, and Deployment ownership;
retain still-current standard role, weights, guide/output, and conflict reasoning in the correct
production/use outcome.

**Depends on:** Overview architecture checkpoint; `WR14`–`WR17` may proceed alongside it.

---

## WR19 — Reconcile Tools child corpus

**Status:** Open
**Raised:** 2026-08-28

Rewrite `Capabilities_Tools_Brief` v1 and `Capabilities_Tools_Design` v1 against parent Design v2.
Move shared Scope and Migration mechanics to their components, add commands explicitly, correct
the production/Deployment boundary, and resolve `WR6`.

**Depends on:** Overview architecture checkpoint; component contracts from `WR14`–`WR16` as they
stabilise.

---

## WR20 — Define shared identity/version and package contracts

**Status:** Open
**Raised:** 2026-08-28

Resolve `Q12` and `Q13` at the smallest useful level. Define producer/consumer contracts without
creating new top-level components. Start package manifest and build/deployment record artefacts as
local Capabilities types. Revisit shared DocMeth status only during the separate DocMeth review.

**Depends on:** provisional interface drafts from Standards, Tools, Dependencies, Migration, and
Deployment; it may stabilise those interfaces iteratively rather than waiting for every component
design to finish.

---

## WR21 — DocMeth review handoff

**Status:** Open — intentionally deferred
**Raised:** 2026-08-28

When the separate Documentation Methodology review begins, use
`Capabilities_DocMethReviewItems` v1 as its input. Do not edit DocMeth piecemeal from this Work
Register. Record each review item's disposition in the DocMeth corpus.

---

**Depends on:** `Capabilities_Decisions` v8.

**References:** `Capabilities_OpenItems` v8, `Capabilities_DocMethReviewItems` v1.

**Methodology:** v17
