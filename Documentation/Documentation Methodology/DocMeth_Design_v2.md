Documentation Methodology | design | DocMeth_Design@v2 | 2026-09-11

## Summary

Documentation Methodology defines the grammar of documents — how they are structured, how they identify themselves, how they are composed from typed building blocks, and the conventions that make them portable and machine-readable. It owns the structural primitives: doctypes, block types, the declaration, rendering conventions, identity and versioning, and the writing rules that apply to every governed document. It does not own individual doctype or block-type definitions, and it does not own the binder concept or inclusion rules.

## Model

The grammar has five concerns: composition (how doctypes and blocks build documents), identity (how a document names and versions itself), format (which formats are supported and how blocks express themselves in each), writing (the language conventions that apply to all authored content), and activation (the Declaration triggers DocMeth — a document with a Declaration is a governed document, and DocMeth's grammar, standards, and behaviours apply to it).

## Definitions

### The doctype

A doctype is the root definition for a document. It states what the document defines and which blocks it includes. A doctype includes a block as defined — it does not modify it. A doctype may not suppress a block's fields, add fields, or adjust a block's shape on inclusion. Where two doctypes need different shapes, those are two blocks, which may share a smaller common block. Composition, not inheritance.

Cut as over-engineered: multiple doctype inheritance, abstract doctypes, block self-assignment to doctypes (push model), collision precedence machinery. Residual collision rule: the doctype defines resolution if needed; otherwise flag to the user.

### The block type

A block is a named set of fields with meaning, mapping to one or more sections in a document. Blocks may include other blocks; composition recurses; no cycles. A block has a default density — compact or expanded — which the doctype may override.

Hosting rules attach to the block, not the section: one authoritative instance per semantic scope, permitted hosts owner-defined, moves between hosts are structural not semantic. Contiguity of a block's sections is a default, not a rule.

Shared content across doctypes is a block that doctypes include — not inheritance. Content is defined in one place; ambiguity is flagged rather than resolved silently.

### Block-type recognition

A block type that is not inherited from its doctype and whose specification does not fix its position requires a marker for recognition. The marker is an HTML comment placed after the heading, not before, so it survives RAG chunking — a chunker that splits on headings keeps the marker with the content it labels rather than orphaning it at the tail of the preceding chunk.

### The common block catalogue

DocMeth holds blocks that are common across documents or usable by any document. Component-specific blocks are defined by their owning component and merge at the document level. No central repository of all blocks.

**Declaration.** Mandatory in every governed document. Its presence is the conformance marker and the corpus recognition mechanism — a document with a Declaration is governed, and DocMeth applies. First block, fixed placement, not overridable. Fields: title, doctype (root of the composition chain), identity, date. Density: compact. No separate version field — identity carries the version. The name "Declaration" lives in the methodology, not in the document; nothing emits the word.

- Markdown: a single delimited line, fixed field order, delimiter `|`.
- Structured formats: a reserved top-level `aide` key with fields as sub-properties (nested one level: `aide.identity`, not `aide_identity`). Presence of `aide` = governed.

**Dependencies.** Which standards a document depends on and at which version it was last brought into line. A flat list of `standard@version` pairs — direct and inherited entries undifferentiated, conformance stamp not constraint, no presence levels or exact pins. Own identity standard omitted. Separate block rather than a Declaration field — Declaration is fixed and compact, and a variable-length list would change its character. Placement: header, immediately after Declaration, before Contents. The currency check gates use, so a partial read from the top must answer "may I use this" without reading to the end.

- Markdown: `Dependencies: A@vN, B@vN` — pipe separates Declaration fields, comma separates list members, so the two header lines are visibly different shapes.
- Structured formats: a `dependencies` key as a sibling of `aide`.

**Header and Footer.** Placement containers only, no semantics of their own. Blocks declare they place into them and may carry a hint. Ties resolved by doctype instruction or defined method. Containers are themselves blocks. No literal marker line in markdown; footer start is marked by a horizontal rule; body start is the first heading that is not Contents or Summary.

**Boundary proximity principle.** Value increases toward the file boundaries. Header runs high-to-low from the top; footer runs low-to-high to the end. Containers declare the gradient; blocks place against it.

**Contents.** Optional. Lets a reader decide whether to read the document and what it covers, at lowest cost. Primary consumer is a file-scanning AI making a partial-read-and-stop decision.

- Earns its place when a reader could not decide from the Declaration alone whether to keep reading. Often not relevant for standards, tools, and other machine-focused or skill-delivered documents unless it adds to discovery or usability.
- Curated semantic map, grouped descriptive entries — not heading repetition.
- Stable heading or section-number locators, never line numbers.
- Density: compact (rendered inline / delimited, never a vertical list).
- Placed immediately after Declaration (or after Dependencies if present), before Summary.
- The doctype owner sets the default for that type (on, off, or conditional) and defines depth.

**Summary.** Optional. States what the document establishes, absorbed quickly.

- Earns its place when the document's substance needs a compressed statement for quick absorption. Often not relevant for machine-focused or skill-delivered documents where the Declaration and body are sufficient.
- States the key model, key points, and defining items — the substance, not a gesture at it.
- Stated, not explained. No expansion, reasoning, or qualification; that is the body's role.
- The body expands; it does not restate. Re-establishing what the Summary states is a defect.
- Density: compact by default; doctype may override to expanded.
- The doctype owner governs whether Summary is used for that type.

**Version note.** Metadata at the top of the footer (low-value end of the footer gradient). One line, current version only, never a list. Historical version notes do not accumulate; the decisions document holds what mattered.

**Parked.** Tags — Core owns the definition; returns to the catalogue only if DocMeth grammar needs to know about it specifically. References — no consumer has appeared; decide on its own merits when one does.

### Identity and versioning

Every document has an identity in its Declaration regardless of publish state. Identity is authoritative; the filename is informative and mirrors it. This is a corpus-integrity requirement: the filename can be renamed and is outside the content, so it cannot be authoritative.

**Identity** carries the contract version and draft state: `@v27-draft2` while working, `@v27` on publish. Absence of a draft marker means published and immutable.

**Filename** mirrors the identity: `_v27-draft2.md` then `_v27.md`. Never authoritative. Identity wins on conflict.

**Draft numbering** is optional in the scheme, on by default.

**Reference forms.** `@v27` resolves to the published contract; `@v27-draft` resolves to the highest draft present.

**Publish** drops the draft marker in both identity and filename; creates the immutable contract. Published numbers are never reused.

**Next cycle** opens immediately at the next integer (`@v28-draft1`). No live drafts sit under a published version.

**`.n`** is reserved, unused — available for minor published releases later without colliding with draft counters.

**Naming grammar.** `{name}_v{integer}-{key}{n}`. Exactly one key defined: `draft`. An undefined key is a conformance error, not a tolerated variant. Expressed as a named token so adding a key later is a list addition, not a grammar reinterpretation.

**Two rhythms.** Design documents and other unpublished documents run on a single rhythm — identity and file move together. Published outcomes (standards, deployed contracts) use a two-rhythm split at the publish boundary.

### Format and rendering

**Supported formats.** Markdown is the primary format. YAML and JSON are usable as document formats or embedded inside documents as defined by blocks. HTML is available for long human-facing artefacts when a document demonstrates the need. The declaration and block model work across all supported formats.

**Format fits the job.** Choose the format that best serves the document's primary consumer and content shape. Format is a considered choice, not a default.

**The format rendering rule.** A block is a named set of fields. Structured formats express fields as native properties; prose formats express them as a heading or delimited line. Each format's own existing standards provide a clear default mapping — no additional mapping tables are needed at this stage. If a gap appears where the format's conventions do not provide an unambiguous answer, DocMeth authors the mapping.

**Density axis.** Compact or expanded, per-block default, doctype override. How compact and expanded render is determined by the format in use.

**Portability flag.** Anything a block defines that would not port cleanly across formats is flagged for confirmation, not decided silently.

### File conventions

**File naming.** Recommended pattern: `{Prefix}_{DocType}_v{N}.md`. Applied by default, not enforced. Deviate and you manage your own file identification. The header is authoritative for identity, doctype, and path; the filename mirrors for human readability.

**Prefix convention.** File prefixes identify the subject — typically the area, part, or component name. Recommended and applied by default. A prefix makes a file distinguishable in search results, open-file lists, and folder listings regardless of whether it sits in its own subfolder or flat alongside other files.

### The binder as a doctype

The binder is a doctype defined by Documentation Methodology — its structure as a document, how a consumer reads it, what the manifest means. A binder assembles governed documents into a single file for delivery to the AI platform. The manifest records relative paths for every included document, preserving structural relationships when documents leave the file system and enter flat AI context.

The concept of the binder — why it exists, how it is built, inclusion rules, how it delivers content — is owned by Working Practices / Content Delivery.

## Rules

### The ownership-designation rule

Defining any doctype or block type must include naming its owner and residence. Part of being defined, not a separate later step. DocMeth owns the requirement to designate a home; each definition states which home.

### The split test

Externalise a block into its own document when keeping it in would compromise the primary role of its host — for example when register or open-items volume degrades the ability to search, understand, and use the host document. Below that line, keep it in; file management is easier. Same content, container chosen by scale.

### The Contents/Summary edge

Contents and Summary both feed the read-decision from different angles. Contents maps what is where — it lets the reader judge relevance. Summary gives what the document establishes — its substance in compressed form. Their roles must stay distinct: Contents is a navigation aid; Summary is a condensed statement of the document's contribution. Merging the two, or letting one drift into the other's territory, defeats both.

### Language rules

Four rules, applying to every governed document:

1. Plain English wherever it will do.
2. Meaning first, code second — name the thing before citing its identifier.
3. Use the terms already in use on the project.
4. Flag a new term rather than introducing it silently.

## Boundaries

Documentation Methodology does not own:

- **Individual doctype definitions** — each lives with the component that knows the most about its subject.
- **Individual block-type definitions** — same principle. DocMeth holds only the common catalogue.
- **The binder concept** — why it exists, how it is used, inclusion rules, how it delivers content. Owned by Working Practices / Content Delivery.
- **Change management methodology** — how change actions are collated, distributed, and executed. Owned by Migration. DocMeth owns the document-level mechanics consumed by that methodology: the Dependencies block and the conformance stamp.
- **The cross-review process** — a collaboration convention owned by Working Practices.
- **Packaging and delivery** — how a standard becomes a skill or binder entry. Owned by Infrastructure and Deployment.
- **Rule-weight vocabulary** — the strength model (required, recommended, optional, information). Owned by Standards.

## Carries to other components

None at this time. All carries received from Project Design, Standards, and Core shaping have been absorbed into this design.

---

Version note: v2 — design pass complete, 2026-09-11. Replaces the v1 shell.
