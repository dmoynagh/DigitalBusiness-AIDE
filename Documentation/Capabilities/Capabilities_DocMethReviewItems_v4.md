# Capabilities — DocMeth Review Items

> **Version 4** (2026-08-30). Closure record: DR1–DR12 are dispositioned by
> Documentation Methodology v18 and no longer constitute open Capabilities work.
> compact machine-content principle, and reconciles update behaviour with the completed Migration
> contract.
>
> Created: 2026-08-28 | Last modified: 2026-08-29

---

## Purpose

Preserve the Capabilities→Documentation Methodology handoff record after disposition. The items
below are historical inputs; Documentation Methodology v18 is now the receiving authority.

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

## DR7 — Integrate Migration with document update without turning every edit into a full rewrite

A local edit is a qualifying update event for declared transition instructions; it is not permission
to reinterpret every current Standard and rework the whole document.

`/update-doc` should point to `AIDE_Migration` rather than restating transition logic. Under the
completed Migration contract, an update does **not** stop merely because Required Migration exists:
the document is already being changed/saved, so applicable Required and pending OnUpdate work are
reconciled together as far as successfully possible.

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

## DR11 — Generic temporary document state container

Several capabilities need to attach temporary operational state to a document without making the
document methodology understand that state semantically. Examples include migration failure/defer,
validation errors, update errors, concurrency/conflict state, and incomplete processing.

DocMeth should define a generic compact location/structure/rendering for independently owned
temporary state entries. Each entry should require a human-readable title/name and a stable owner so
the owning capability can safely create, update, replace, or remove only its own entry.

Preferred human-facing shape:

```text
Title [Owner]
Message
```

The owner defines the meaning/lifecycle/content. DocMeth defines only placement, structure,
formatting, and coexistence of multiple owner entries.

---

## DR12 — Compact metadata and machine-generated content in human-readable documents

Adopt a general rendering principle for documents that may be read by humans:

> Metadata, derived state, and other machine-generated content should be as compact as practicable
> while remaining unambiguous and machine-usable.

This applies across Identity, Tags, Dependencies, migration summaries/state, validation state, and
future generated metadata. Prefer compact one-line/two-line forms over multi-line diagnostic blocks
inside the document; richer diagnostics belong in the active session/work record where appropriate.

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


## Closure disposition — 2026-08-30

**Status: Completed.**

Documentation Methodology v18 applies the handoff as follows:

- DR1/DR2 — dependency/conformance semantics use `AIDE_Dependencies` + `AIDE_Migration`;
- DR3/DR4 — local type boundaries retained; no premature type promotion;
- DR5/DR6 — existing shared types retained and generic behaviour delegated to owners;
- DR7 — document update consumes Migration rather than redefining it;
- DR8–DR10 — generic metadata hosting with Identity/Tags/Dependencies owner boundaries;
- DR11 — generic compact owner-labelled temporary state;
- DR12 — compact machine-generated metadata/state principle.

This document remains as evidence of the handoff; no item here is an open implementation request.

---
Dependencies: !AIDE_DocumentationMethodology@v18, Capabilities_Decisions_v14
References: DocumentationMethodology_Guide_v18
