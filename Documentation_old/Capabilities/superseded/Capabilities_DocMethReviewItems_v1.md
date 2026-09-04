# Capabilities — DocMeth Review Items

> **Version 1** (2026-08-28). Records inputs identified during the Capabilities parent
> architecture rewrite for consideration in a separate Documentation Methodology review. This is
> not a DocMeth redesign and makes no change to `DocumentationMethodology_Guide` v17.
>
> Created: 2026-08-28 | Last modified: 2026-08-28

---

## Purpose

Keep Capabilities decisions that affect Documentation Methodology visible without resolving them
inside the Capabilities architecture pass. Each item below is a review input, not an instruction
to edit DocMeth in isolation.

---

## DR1 — Move dependency semantics to Dependencies

**Source decision:** `D46`

Review `DocumentationMethodology_Guide` v17 §3c, especially:

- the meaning of `Depends on` and `References`;
- dependent-side declaration;
- the statement that neither relationship creates automatic obligation;
- version history and footer-update behaviour.

The target boundary is:

- **DocMeth** owns the shared document footer as a component, its placement, and non-dependency
  document metadata;
- **Dependencies** owns dependency/reference semantics, dependency identity and version meaning,
  availability checks, and the dependency declaration within the footer;
- **Migration** owns consequences of a version gap: Required Migration, On-Update, or no
  transition.

The DocMeth review must decide how DocMeth references and consumes the Dependencies Standard
without duplicating it.

---

## DR2 — Reconcile the `Methodology` footer line with generic dependencies

`DocumentationMethodology_Guide` v17 treats `Methodology: v17` as a special per-document
conformance record governed at project level. Dependencies now provides a generic identity and
version model for artefacts.

Review whether Methodology remains a deliberately specialised footer field, becomes a normal
dependency declaration, or uses the Dependencies model with a DocMeth-specific rendering. Do
not assume all documents in a project must move together until the DocMeth review re-evaluates
that policy against Required Migration and On-Update.

---

## DR3 — Keep local document types local by default

**Source decision:** `D53`

The current custom-type mechanism in `DocumentationMethodology_Guide` v17 §4h already permits
local types and recognises promotion after recurrence. Review its surrounding language and any
other corpus statements against the confirmed boundary:

- a domain may define a document type needed for its own outcomes;
- local definition is normal, not provisional non-compliance;
- only genuinely shared document types and shared document components belong in DocMeth;
- recurrence across domains is evidence for promotion, not automatic promotion.

This specifically supersedes the earlier Capabilities decision that all document types are
single-source DocMeth.

---

## DR4 — Do not pre-promote package manifest and build record

The prior Work Register proposed **package manifest** and **build record** as new DocMeth document
types. Under `D53`, Capabilities may define them locally as package/production artefacts.

During the DocMeth review, consider them for shared status only if other domains demonstrate the
same semantic and lifecycle need. Their use by Capabilities alone is not sufficient.

---

## DR5 — Confirm existing shared types/components rather than re-adding them

`DocumentationMethodology_Guide` v17 already includes Overview as an established type and already
defines created/last-modified metadata. The old Capabilities work item proposing those additions
is therefore satisfied by the uploaded source and should not generate a duplicate change.

The separate DocMeth review should confirm whether these remain genuinely shared. Capabilities
continues using Overview as its critical architecture review surface in the meantime.

---

## DR6 — Audit generic behaviour accumulated in DocMeth

The creation of Scope, Dependencies, Migration, and Review as shared Capabilities components is
evidence that some behaviour may have accumulated in DocMeth because no generic owner existed.

Review candidate behaviour one concern at a time:

- applicability or trigger behaviour that belongs to Scope;
- dependency/version-gap behaviour that belongs to Dependencies;
- transition behaviour that belongs to Migration;
- reusable assessment and disposition behaviour that belongs to Review.

Do not slim DocMeth by category or word count. Move behaviour only where the receiving component
has a complete contract and DocMeth can consume it without losing document-specific semantics.

---

## DR7 — Integrate On-Update without turning every edit into a full rewrite

The DocMeth review should account for the AI-oriented On-Update trigger (`D48`) when documents
are modified. A local edit is a qualifying update event only for declared transition instructions;
it is not permission to reinterpret every current Standard and rework the whole document.

`/update-doc` is the forced reconciliation path. It is idempotent and stops on Required Migration.
DocMeth should point to this behaviour where document workflows need it rather than restating the
transition procedure.

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

**Depends on:** `Capabilities_Decisions` v8 (`D46`, `D48`, `D53`),
`DocumentationMethodology_Guide` v17.

**References:** `Capabilities_Design` v2, `Capabilities_WorkRegister` v6.

**Type definition:** `DocMethReviewItems` — review input. Holds consequences and questions for a
separate Documentation Methodology review without redesigning DocMeth in the originating pass.
Nearest established type: `Message`. Living until every item is dispositioned in the DocMeth
review. Internal.

**Methodology:** v17
