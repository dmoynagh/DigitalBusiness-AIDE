# Documentation Methodology — Standard

## Purpose

Make building, authoring, managing and maintaining documents easier in an AI-driven development environment.

## What it does

Provides content standards, structure and management to documentation. Extends AI platforms (standards) and provides human guides.

## Approach and key principles

1. **Facilitate, not enforce** — the methodology helps, it doesn't dictate
2. **Content-triggered** — documents activate functionality by their content; functionality applies because it's present, not because it's mandated
3. **Graceful degradation** — functionality can be applied in part or in full; enhance as best able, degrade gracefully
4. **Schema serves authoring and consumption** — helps authors shape and define content, helps consumers find and use it
5. **Consistency where wanted** — apply consistency where it's needed, not everywhere by default
6. **Default and override** — DocMeth defines default behaviour; defaults can be overridden by logic inherited by, applied to, or defined within the document

## Key functions

Documentation Methodology provides five functions:

- **Identity and Versioning** — unique identification, version tracking and management
- **Schema** — defined content structure, metadata, instructions and functionality applied through doctypes and blocktypes
- **Instructions** — rules, conventions and instructions applied to documents
- **Change Management** — dependency tracking and change identification

---

## Application and triggering

DocMeth applies to a document through its content.

The primary mechanism is the **Declaration** — described below. A document with a Declaration is the fullest expression of DocMeth's capability.

But the Declaration is not the only trigger. Individual features can also activate from defined elements or patterns elsewhere in a document — if what a feature needs to function is present, it can apply. Full adoption is not required for partial benefit.

---

## The Declaration

The Declaration is a block at the top of a document containing fields that DocMeth uses to determine what applies and how. A document with a Declaration is a governed document.

### Declaration fields

- **identity** (required) — the document's unique identifier: `documentname` or `documentname@v##` when versioned
- **doctype** (optional) — the document's type. Links the document to a doctype definition
- **blocks** (optional) — typed blocktypes present in the document, beyond any defined by the doctype. Comma-separated, with optional ownership grouping: `blocks: Brief, WorkRegister` or `blocks: pd:[Brief, WorkRegister]`. The grouping syntax (`prefix:[items]`) organises values by source or owner — groups are for organisation only; when applied, the list is flattened. This grouping syntax may be used by other fields (e.g. `uses`).
- **updated** (optional) — the date this version was produced
- **uses** (optional) — standards this document depends on, as `standard@version` references

### How it looks

In markdown, the Declaration renders as a blockquote with labelled, pipe-delimited fields:

```
> identity: MyDocument@v3 | doctype: standard | updated: 2026-09-14
```

Fields are included as needed — only identity is always present.

In structured formats (YAML, JSON), a reserved top-level `aide` key holds the Declaration fields as sub-properties (`aide.identity`, `aide.doctype`, etc.). The presence of the `aide` key is what makes the document governed in these formats.

---

## Identity and Versioning

### Identity

A document has an identity — a unique identifier within a given scope (at minimum, within a folder).

Identity is set in one of two ways:

- **Declared** — in the Declaration's `identity` field. Always takes precedence.
- **Inferred** — from the filename, when no Declaration is present. If a Declaration exists but the identity field is not set, the filename can be used as the source to populate it.

The identity value is a string. The document name uses no spaces; alphanumeric characters, hyphens and underscores are permitted.

### Versioning

Versioning is a feature DocMeth can add to documents. When a document is updated, its version is increased and a new version saved.

Versioning is triggered in two ways:

- **Declared** — the identity field includes a version part after the `@`: `documentname@v##` or `documentname@v##-draft#`
- **Inferred** — from a filename ending in `_v##` or `_v##-draft#`, when no Declaration is present.

**Default behaviour:**

- Version increments on save with changes.
- Version is written into the filename.

These are DocMeth defaults, subject to the default-and-override principle.

**Version format:**

- `documentname@v##` — published version, immutable
- `documentname@v##-draft#` — working draft

In filenames, the version mirrors using `_v##` and `_v##-draft#`.

**Draft and publish cycle:**

- Absence of a draft marker means published and immutable.
- Published version numbers are never reused.
- Every draft carries its sequence number.
- **Publish** — drops the draft marker in both identity and filename; creates the immutable version. The next cycle opens immediately at the next integer (`@v4-draft1` after publishing `@v3`).
- **Reference forms** — `@v3` resolves to the published version; `@v3-draft` resolves to the highest draft present.

---

## Schema

Schema applies defined content structure, metadata, instructions and functionality to documents through two building blocks: **blocktypes** and **doctypes**.

Blocktypes define reusable chunks of document content. Blocktypes can contain other blocktypes, allowing composition of complex content from simpler defined parts.

Doctypes are the primary method for applying blocktypes to a document. A doctype links a document to a defined composition of blocktypes, metadata, conventions and instructions. By declaring a doctype, a document inherits everything that doctype defines.

A document can also declare individual blocktypes directly, with or without a doctype.

**Key properties:**

- Extensible and scalable — new doctypes and blocktypes can be defined as needed, and existing ones can be adopted incrementally
- Specifications can be as simple or detailed as the owner wants
- Define once, apply where needed

### Blocktype specification

- **Name** — what the block is called
- **Purpose** — what it's for
- **Content** — what the block contains: headings, sections, general content, named fields with optionality. As specific or generic as the author deems necessary. Used for recognition, authoring and interpretation. Included blocktypes are defined here.
- **Placement** — (optional) where in the document the block belongs. Defaults to general document flow, or as defined by the including doctype
- **Recognition** — (optional) how to identify this block when its content definition alone is not sufficient
- **Instructions** — block-specific rules applied when authoring, reading or using this block

### Doctype specification

- **Name** — what the document type is called
- **Purpose** — what this type of document is for, its role and behaviour
- **Content** — what the doctype defines for its documents: blocktypes with optionality, ordering, metadata, conventions, and any other information that applies
- **Instructions** — doctype-specific rules applied when authoring, reading or using documents of this type

A doctype includes a blocktype as defined — it does not modify it. The block's own definition is authoritative for its content, fields and structure.

---

## Instructions

Instructions are rules, guidance and conventions applied to documents. They are the general mechanism for governing how documents are authored, read and used.

### DocMeth default instructions

These apply to all governed documents:

1. Plain English wherever it will do
2. Meaning first, code second — name the thing before citing its identifier
3. Use the terms already in use on the project
4. Flag a new term rather than introducing it silently
5. Do not compose plausible metadata, versions, paths or state — distinguish verified, declared and unknown

This set grows as the system evolves. Additional instructions can be defined by other sources — a doctype, a blocktype, or the document itself — at a more specific scope.

---

## Change Management

The `uses` field in the Declaration lists the standards and versions a document depends on. Its purpose is to maintain a clear record of what a document is built against, so that when any of those defining items change, the documents affected can be identified and updated.

---

## Operational instructions

How to apply DocMeth when working with a document.

### When opening a document

1. Read the Declaration. Identify the doctype, any declared blocks, and the `uses` references.
2. Load the doctype definition and all blocktype definitions that apply.
3. Combine instructions from all sources: DocMeth defaults, then doctype instructions, then block instructions, then document-level instructions. More specific scope takes precedence where they conflict.
4. Check `uses` references against current versions. If any dependency is not current, check for migration actions defined by the changed item and apply them before proceeding. Update `uses` to reflect current versions once applied.

### When authoring or updating a document

1. Apply the combined instructions when writing or editing content.
2. Use blocktype content definitions to guide structure, fields and content within each block.
3. Populate `uses` with the current versions of all standards the document's doctype and blocktypes are defined in. Trace from each type to the standard that defines it — those defining standards, at their current versions, are the `uses` entries.
4. Apply versioning: increment the version and update the filename.

### When a defining item changes

The migration methodology governs how change actions are defined and applied. DocMeth's responsibility is that the dependency information in `uses` is accurate and maintained.
