# Capabilities — Open Items

> **Version 8** (2026-08-28). Reconciled to the seven-component parent architecture. Historical
> questions remain visible with their current disposition; open work is narrowed to component
> contracts, platform evidence, and schemas not needed to settle the parent boundaries.
>
> Created: 2026-08-27 | Last modified: 2026-08-28

---

## Q1 — Domain carrier files

**Status:** Moved to `AIDE-Q3`
**Raised:** 2026-08-27

Moved to AIDE following `AIDE-D3` (Domain is an AIDE concern). No longer part of the Capabilities
architecture.

---

## Q2 — Platform-specific design re-admission

**Status:** Resolved — `D41`, clarified by `D50`
**Raised:** 2026-08-27
**Resolved:** Recorded in source v7; current convention recorded in v8

Old Claude-specific content is not re-admitted to the parent. The generic convention is now
`Generic Design → base outcome → apply Design_Platform_{Name} → platform outcome`, with platform
design containing divergence only.

---

## Q3 — Separate standards versus embedded blocks in the AIDE standard

**Status:** Resolved — `D26`, then reframed by `D51`
**Raised:** 2026-08-27

Standard blocks remain removed. Standards publishes a generic Standards Usage Standard; it is
not embedded in or scoped to AIDE.

---

## Q4 — Actions boundary

**Status:** Resolved — `D24`, extended by `D52`
**Raised:** 2026-08-27

A Standard may describe a procedure but may not define a named invokable action. A Tool defines
the logical commands it contributes.

---

## Q5 — Audience per weight

**Status:** Resolved — `D39`, ownership clarified by `D45`
**Raised:** 2026-08-27
**Resolved:** Recorded in source v7

Audience is carried by Scope, not by a per-weight marker.

---

## Q6 — Tone enforcement

**Status:** Resolved — `D40`, ownership clarified by `D44`
**Raised:** 2026-08-27
**Resolved:** Recorded in source v7

Tone and justification quality are assessed through Review, using a Standards-specific review
profile rather than a mechanical publish gate.

---

## Q7 — Versioning, currency, and drift

**Status:** Parent question resolved; detailed contracts reopened as `Q12` and `Q13`
**Raised:** 2026-08-27

The parent responsibilities are now clear:

- Dependencies owns declared dependency version meaning and availability checks (`D46`).
- Migration owns Required Migration and On-Update transitions (`D47`, `D48`).
- Deployment owns distribution from a completed package (`D49`).
- Host pickup/currency remains a host responsibility by default (`D38`).

The exact shared identity/version and package-manifest schemas were deliberately not settled by
the parent rewrite.

---

## Q8 — Account preferences: surface reach

**Status:** Open — empirical and component-design input
**Raised:** 2026-08-27

Tools identifies account-level preferences for reporting verbosity and prompting style. Determine
which supported platform surfaces actually expose those preferences. Record generic intent in
Tools and concrete reach in the appropriate platform design; do not assume parity across chat,
desktop coding, or other surfaces.

**Feeds into:** `WR19` (Tools reconciliation) and platform Tool designs.

---

## Q9 — Plugin metadata visibility

**Status:** Open — platform probe; no longer a parent-architecture dependency
**Raised:** 2026-08-28

Determine what installed capability/plugin identity and version information an AI session can
actually inspect on each supported platform. The older `{key}_pendingmigrations` naming
convention (`D32`) is historical platform-design input, not a generic architecture decision.

**Feeds into:** Scope, Dependencies, and Migration platform designs; `WR10`.

---

## Q10 — Trigger inventory for migration and On-Update

**Status:** Open — revised by `D45` and `D48`
**Raised:** 2026-08-28

Create an inspectable trigger inventory that separates:

- generic semantic trigger: an older dependent artefact is undergoing a qualifying update;
- Required Migration blocking checks;
- explicit command triggers (`/migrations-check`, `/migrations-apply`, `/update-doc`);
- platform-specific retrieval, discovery, or always-resident cues;
- evidence that purportedly independent platform triggers really fail independently.

The generic intent belongs in Migration. Concrete realisation belongs in Scope and the relevant
platform design.

**Feeds into:** `WR14` and `WR16`.

---

## Q11 — Production-chain re-runnability

**Status:** Earlier five-stage answer superseded in form; requirement remains under `D49`
**Raised:** 2026-08-28

`D42` settled re-runnability for the former five-stage chain. `D49` replaces that chain with
capability production and capability deployment flows. Each component design must now state
idempotency/resumption at its own side of the package boundary. No new parent mechanism is
currently required.

**Feeds into:** Standards, Tools, and Deployment component designs.

---

## Q12 — Shared identity and version contract

**Status:** Open
**Raised:** 2026-08-28

Define the minimum identity/version contract shared by produced artefacts, dependency
declarations, transition ranges, packages, and Deployment. It must distinguish:

- source-document version;
- produced artefact/deployment version;
- dependency version last conformed against;
- transition source and target versions.

Do not assume semantic versioning. Preserve `D36`'s useful separation between document and
deployed artefact versions unless component design finds a concrete contradiction.

**Feeds into:** `WR15`, `WR16`, `WR20`, and revised Standards/Tools designs.

---

## Q13 — Package and manifest contract

**Status:** Open
**Raised:** 2026-08-28

Define the smallest producer-to-Deployment contract: package identity, contents, platform
applicability, versions, transition artefacts, removals, integrity, and any resumption data.

The schema must remain generic across Standards and Tools without requiring Deployment to
understand their meaning. Package manifest and build record begin as local Capabilities artefacts;
their promotion to shared DocMeth types is deferred to the separate DocMeth review.

**Feeds into:** `WR20` and `WR13`.

---

## Q14 — Review component outcome and integration model

**Status:** Open
**Raised:** 2026-08-28

Define the reusable Review component closely enough to answer:

- what artefact records a review and its findings;
- how findings distinguish evidence, risk, and proposed remedy;
- how the lead records disposition;
- how component-specific review profiles attach without duplicating the common method;
- what, if anything, becomes a published standard or tool.

**Feeds into:** `WR17`.

---

**Depends on:** `Capabilities_Decisions` v8.

**References:** `Capabilities_Design` v2, `Capabilities_WorkRegister` v6.

**Methodology:** v17
