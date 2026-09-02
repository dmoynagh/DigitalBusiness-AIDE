# Capabilities — DocMeth Review Items

> **Version 2** (2026-08-28). Adds the generic header/footer metadata-container boundary, Tags
> footer integration, and shared Identity header implications discovered during the Tags/Scope/
> Dependencies design pass.
>
> Created: 2026-08-28 | Last modified: 2026-08-28

---

## Purpose

Keep Capabilities decisions that affect Documentation Methodology visible without resolving them
inside the Capabilities architecture pass. Each item below is a review input, not an instruction
to edit DocMeth in isolation.

---

## DR1 — Move dependency semantics to Dependencies and generalise footer hosting

**Source decisions:** `Capabilities_Decisions` v10 (`D46`, `D65`–`D68`),
`Core_System_Decisions` v2 (`D10`)

Review `DocumentationMethodology_Guide` v17 §3c, especially:

- the meaning/rendering of `Depends on` and `References`;
- dependent-side declaration;
- version history/footer-update behaviour;
- the fixed three-line footer shape.

Target boundary:

- **DocMeth** owns generic document header/footer metadata containers, placement, and block-hosting
  rules;
- **Dependencies** owns the `Dependencies:` property content, compact grammar, required/startup
  posture, identity resolution, conformance-version meaning, and advancement rules;
- **Migration** owns consequences of a version gap;
- **References** remain non-dependency citations and should be retained/reworked only where their
  document-specific value remains demonstrated.

The DocMeth review should make it possible for future components to add metadata blocks without
DocMeth enumerating or semantically owning them.

---

## DR2 — Reconcile the `Methodology` footer line with generic Dependencies

`DocumentationMethodology_Guide` v17 treats `Methodology: v17` as a special per-document
conformance record. Dependencies now provides a generic conformance-checkpoint model.

Review whether Methodology remains specialised, becomes a normal generated dependency (for
example on `AIDE_DocumentationMethodology`), or uses the Dependencies semantics with a
DocMeth-specific rendering.

Do not assume all documents in a project must move together until this is re-evaluated against
Required Migration and On-Update.

---

## DR3 — Keep local document types local by default

**Source decision:** `D53`

Retain the confirmed boundary that domains may define the types needed for their own outcomes;
DocMeth owns genuinely shared document types/components. Cross-domain recurrence is evidence for
promotion, not automatic promotion.

This pass has introduced a Capabilities-local `Standard` managed type for generated Standard
outputs. Treat that as another candidate to evaluate later, not as an instruction to promote it
now.

---

## DR4 — Do not pre-promote package manifest and build record

Package/Deployment Manifest remains a Capabilities production/deployment contract. Do not create
shared DocMeth types unless reuse outside Capabilities demonstrates the same semantic/lifecycle
need.

---

## DR5 — Confirm existing shared types/components rather than re-adding them

`DocumentationMethodology_Guide` v17 already includes Overview and created/last-modified metadata.
Do not duplicate them from older Capabilities work items.

---

## DR6 — Audit generic behaviour accumulated in DocMeth

The creation of Tags, Scope, Dependencies, Migration, and Review as shared Capabilities
components is evidence that some behaviour may have accumulated in DocMeth because no generic
owner existed.

Review candidate behaviour one concern at a time:

- tag/classification generation or matching that belongs to Tags;
- applicability or trigger behaviour that belongs to Scope;
- dependency/version-gap behaviour that belongs to Dependencies;
- transition behaviour that belongs to Migration;
- reusable assessment and disposition behaviour that belongs to Review.

Move behaviour only where the receiving component has a complete contract and DocMeth can consume
it without losing document-specific semantics.

---

## DR7 — Integrate On-Update without turning every edit into a full rewrite

A local edit is a qualifying update event only for declared transition instructions; it is not
permission to reinterpret every current Standard and rework the whole document.

`/update-doc` remains the explicit idempotent reconciliation path and stops on Required Migration.
DocMeth should point to shared Migration behaviour rather than restating it.

---

## DR8 — General header/footer metadata containers

**Source decision:** `Core_System_Decisions` v2 `D10`

Introduce or reconcile a generic document metadata-container model:

```text
Header metadata container
Body
Footer metadata container
```

DocMeth decides where these containers appear and how independently owned metadata blocks/properties
are added and formatted. The owner of each block decides its internal content and behaviour.

This prevents DocMeth from needing explicit knowledge of every capability that later contributes
machine metadata.

Current known consumers are:

- Identity → header metadata;
- Tags → footer metadata;
- Dependencies → footer metadata.

These examples must not become a closed list.

---

## DR9 — Tags footer property

`AIDE_Tags` defines compact document storage such as:

```text
Tags: design, release-ready, doctype:[design, platformdesign]
```

DocMeth should host the property in the footer metadata container without owning Tag Builder,
group, generation, cleanup, or query semantics.

Review how this interacts with the current mandatory footer shape and the `Internal` section.

---

## DR10 — Identity header metadata

**Source decision:** `Core_System_Decisions` v2 `D9`

A referenceable governed document may expose compact header metadata:

```text
Identity: primary-id@v2, alternate-id@v7, included-id
```

The first identity is primary; later entries are alternate/exposed identities. Version belongs to
an identity entry, and identity matching ignores version.

Review the physical header placement, relationship to filename/document version, and whether the
existing Index identity/topic mechanisms need any reconciliation. Do not collapse canonical
identity into filename merely because filenames are currently the primary document locator.

---

## Review disposition

For each item, the later DocMeth review should record one of:

- retained in DocMeth as document-specific;
- moved to and consumed from a Capabilities component;
- split across a shared component and DocMeth rendering;
- deferred pending a component design;
- rejected, with reason.

No item in this document is considered applied until that review updates DocMeth and records its
own decisions.

---

**Depends on:** `Capabilities_Decisions` v10, `Core_System_Decisions` v2,
`DocumentationMethodology_Guide` v17.

**References:** `Capabilities_Design` v4, `Capabilities_WorkRegister` v8,
`Capabilities_Tags_Design` v1, `Capabilities_Dependencies_Design` v1.

**Type definition:** `DocMethReviewItems` — review input. Holds consequences and questions for a
separate Documentation Methodology review without redesigning DocMeth in the originating pass.
Nearest established type: `Message`. Living until every item is dispositioned in the DocMeth
review. Internal.

**Methodology:** v17
