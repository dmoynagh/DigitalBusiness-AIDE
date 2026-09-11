Documentation Methodology — Standard | standard | DocumentationMethodology_Standard@v1 | 2026-09-11

Use when authoring, structuring, or versioning a governed document — doctypes, blocks, identity, naming, and writing rules.

## What Documentation Methodology is

Information. Documentation Methodology defines the grammar of documents — how they are structured, how they identify themselves, how they are composed from typed building blocks, and the conventions that make them portable and machine-readable. It owns the structural primitives. It does not own individual doctype or block-type definitions — those live with the component that knows the most about them.

## Applicability

Information. This standard applies whenever a governed document is being authored, structured, versioned, or read for structural compliance. It also applies when defining a new doctype or block type. It does not apply to unmanaged files or files outside the methodology.

## The Declaration — recognition and activation

Required. Every governed document has a Declaration. It is the first block, fixed placement, not overridable. Its presence is what makes a document governed — Documentation Methodology's grammar, standards, and behaviours apply to any document that carries one.

Required. Declaration fields: title, doctype, identity (name + @version), date. Density: compact. No separate version field — identity carries the version.

Information. In markdown, the Declaration is a single delimited line with fixed field order, delimiter `|`. In structured formats (YAML, JSON), a reserved top-level `aide` key holds the fields as sub-properties. Presence of `aide` = governed.

Information. The name "Declaration" is methodology vocabulary — nothing in the document emits the word.

## Doctypes and blocks

Required. A doctype is the root definition for a document — it states what the document defines and which blocks it includes. A doctype includes a block as defined and does not modify it. No field suppression, no field addition, no shape adjustment on inclusion.

Required. A block is a named set of fields with meaning, mapping to one or more sections. Blocks may include other blocks; composition recurses; no cycles.

Recommended. Shared content across doctypes is a block that doctypes include — composition, not inheritance. Where two doctypes need different shapes, those are two blocks, which may share a smaller common block.

Required. Content is defined in one place. Ambiguity is flagged rather than resolved silently.

### Block-type recognition

Recommended. A block type that is not inherited from its doctype and whose specification does not fix its position requires a marker. The marker is an HTML comment placed after the heading (not before) so it survives RAG chunking.

### Defining new types

Required. Defining any doctype or block type must include naming its owner and residence. This is part of being defined, not a later step.

## The common blocks

Information. These blocks are available to any document. Component-specific blocks are defined by their owning component.

**Dependencies.** Recommended. A flat list of `standard@version` pairs stating which standards a document depends on and at which version it was last brought into line. Conformance stamp, not constraint — no presence levels or exact pins. Placed in the header, immediately after the Declaration, before Contents.

**Header and Footer.** Information. Placement containers with no semantics of their own. Blocks declare they place into header or footer. The boundary proximity principle governs ordering: value increases toward the file boundaries — header runs high-to-low from the top, footer runs low-to-high to the end.

**Contents.** Optional. A curated semantic map letting a reader decide whether to read the document and what it covers. Earns its place when the Declaration alone is not enough to make that decision. Often not relevant for machine-focused or skill-delivered documents. Density: compact. Placed after Dependencies (or Declaration if no Dependencies), before Summary. The doctype owner sets the default for their type and defines depth.

**Summary.** Optional. States what the document establishes, absorbed quickly. Earns its place when the document's substance needs a compressed statement. States the key model, key points, and defining items — the substance, not a gesture at it. Stated, not explained — expansion is the body's role. The body does not restate what the Summary states. The doctype owner governs whether Summary is used.

Recommended. The Contents/Summary edge must stay distinct. Contents maps what is where (navigation). Summary gives what the document establishes (substance). Letting one drift into the other's territory defeats both.

**Version note.** Optional. One line at the top of the footer. Current version only — historical version notes do not accumulate; the decisions document holds what mattered.

## Identity and versioning

Required. Every document has an identity in its Declaration. Identity is authoritative; the filename is informative and mirrors it. Identity wins on conflict.

Required. Identity carries the contract version and draft state: `@v27-draft2` while working, `@v27` on publish. Absence of a draft marker means published and immutable.

Required. Published version numbers are never reused. Next cycle opens at the next integer.

Recommended. Draft numbering is optional in the scheme, on by default.

Information. Reference forms: `@v27` resolves to the published contract; `@v27-draft` resolves to the highest draft present.

Information. Naming grammar: `{name}_v{integer}-{key}{n}`. One key defined: `draft`. An undefined key is a conformance error.

Information. Design documents run on a single rhythm — identity and file move together. Published outcomes use a two-rhythm split at the publish boundary.

## Lifecycle states

Information. Three semantic states, independent of physical storage:

- **Current** — the issued authoritative version for normal use.
- **Superseded** — an older issued version, or a document displaced without reaching archival.
- **Archived** — terminal disposition; the record is frozen except through the type's permitted correction route.

Information. Working Practices owns physical handling — how storage represents these states.

## File conventions

Recommended. File naming pattern: `{Prefix}_{DocType}_v{N}.md`. Applied by default, not enforced. The header is authoritative; the filename mirrors for readability.

Recommended. File prefixes identify the subject — the area, part, or component name. A prefix makes a file distinguishable in search results, open-file lists, and folder listings.

## Format and rendering

Recommended. Choose the format that best serves the document's primary consumer and content shape. Format is a considered choice, not a default. Markdown is the primary format; YAML, JSON, and HTML are available where the content warrants them.

Required. A block is a named set of fields. Structured formats express fields as native properties; prose formats express them as a heading or delimited line. Each format's own standards provide the default mapping.

Recommended. Each block has a default density — compact or expanded — which the doctype may override.

Required. Anything a block defines that would not port cleanly across formats is flagged for confirmation, not decided silently.

## The split test

Recommended. Externalise a block into its own document when keeping it in would compromise the primary role of its host. Below that line, keep it in — file management is easier. Same content, container chosen by scale.

## The binder as a doctype

Information. The binder is a doctype defined by Documentation Methodology — its structure as a document, how a consumer reads it, what the manifest means. A binder assembles governed documents into a single file for AI platform delivery. The manifest records relative paths, preserving structure when documents enter flat context.

Information. Why the binder exists, how it is built, and what it includes are owned by Working Practices / Content Delivery.

## Language and integrity

Required. Five rules applying to every governed document:

1. Plain English wherever it will do.
2. Meaning first, code second — name the thing before citing its identifier.
3. Use the terms already in use on the project.
4. Flag a new term rather than introducing it silently.
5. Do not compose plausible metadata, times, versions, paths, or delivery facts where the fact should be observed or read. Distinguish verified state, declared state, and unknown state.

---

Version note: v1 — initial standard authored from DocumentationMethodology_Design_v2, 2026-09-11.
