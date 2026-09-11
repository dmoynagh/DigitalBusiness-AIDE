Documentation Methodology | design | DocMeth_Design@v4 | 2026-09-12

## Summary

Documentation Methodology defines the grammar of documents — how they are structured, how they identify themselves, how they are composed from typed building blocks, and the conventions that make them portable and machine-readable. It owns the structural primitives: doctypes, block types, the declaration, rendering conventions, identity and versioning, the definition contract for defining new types, type-reference resolution, and the writing rules that apply to every governed document. It does not own individual doctype or block-type definitions, and it does not own the binder concept or inclusion rules.

## Model

The grammar has six concerns: composition (how doctypes and blocks build documents), identity (how a document names and versions itself), format (which formats are supported and how blocks express themselves in each), writing (the language conventions that apply to all authored content), activation (the Declaration triggers DocMeth — a document with a Declaration is a governed document), and the definition contract (the grammar for defining new doctypes and block types so that any component can extend the vocabulary without modifying the methodology).

## The governed-document scaffold

The methodology implicitly provides a structural scaffold for every governed document. A doctype adds content blocks on top of this scaffold; it does not need to re-state what the methodology provides.

**Implicit structure:**

- **Declaration** — the first block, fixed topmost. Every governed document has one. The methodology provides it.
- **Title** — recognised by placement, immediately after the Declaration. The human-readable name.
- **Description** — recognised by placement, immediately after Title. What the document is, in a line.
- **Header, Body, Footer** — structural containers. Every governed document has them. Header runs from the top through the self-describing blocks. Body is the document's substance. Footer carries metadata. Containers exist structurally even when they contain no explicitly declared blocks.

**Doctype-added structure:** a doctype's included blocktypes declare the content blocks the document uses beyond the scaffold. Contents, Summary, Version note, and all component-defined blocks are doctype choices, not methodology defaults.

## The definition contract

The definition contract specifies what properties are available when defining a doctype or block type. It is primarily for machine consumption — structured where structure makes it deterministic, prose where judgement is needed, but always formally delineated.

The governing principle: the contract is the definition language, not a form to fill in. A minimal definition is a name and a purpose. A complex definition uses as many of the available properties as it needs. The contract facilitates; it does not mandate structure where structure adds no value.

### Conditional completeness

Name and purpose are always required. A property becomes required when omitting it would leave the definition ambiguous: a block whose position does not identify it must state its recognition; a block with structured fields must declare them. The contract remains facilitative — minimal definitions are still two lines — but a definition that would be broken without a property must include that property.

### Implicit dependency rule

A type defined in a versioned schema standard implicitly carries that hosting standard as its dependency implication. The document's `uses` field is populated automatically. A definition only states dependency implications explicitly when they differ from the hosting standard.

### Definition representation

A definition is written as a heading naming the type, followed by labelled properties as list items. Name is the heading. Purpose is the first property. Remaining properties follow in any order. In structured formats, a definition is a keyed object with the same property names.

### Type-reference resolution

Type names must be unique within their kind — doctype names unique among doctypes, block-type names unique among block types. Uniqueness is enforced at definition time.

Unqualified names are the default. When a name collides within the document's `uses` scope, the dot-qualified form disambiguates: `pd.brief`, where the prefix is the component's declared alias. The dot pattern extends to framework-level (`aide.pd.brief`) if needed, but the framework prefix is not defined until a collision demonstrates the need.

Resolution path: a type's authoritative definition is in the schema standard listed in the document's `uses` field. The consumer reads the type name from the Declaration, finds the defining standard in `uses`, reads the definition there.

### Doctype definition

A doctype is the root definition for a document. Name and purpose are the only required properties.

Available vocabulary, stated when needed:

- **Included blocktypes** — which blocks the doctype uses beyond the governed-document scaffold. For each: the optionality for this doctype (required, recommended, or optional) and any density override.
- **Block positioning** — where a block goes if different from the block's own placement default, or to resolve ordering between blocks.
- **Dependency implications** — stated only when different from the implicit rule (hosting standard).
- **Format constraint** — narrows the permitted formats when the type requires it (e.g. standards must be markdown for session loading).
- **Owner and residence** — which component owns the definition and where it lives. Implicit from hosting location for most definitions; stated when not obvious.

A doctype includes a block as defined — it does not modify it. A doctype may not suppress a block's fields, add fields, or adjust a block's shape on inclusion. Where two doctypes need different shapes, those are two blocks, which may share a smaller common block. Composition, not inheritance.

Cut as over-engineered: multiple doctype inheritance, abstract doctypes, block self-assignment to doctypes (push model), collision precedence machinery. Residual collision rule: the doctype defines resolution if needed; otherwise flag to the user.

### Block-type definition

A block is a named content definition mapping to one or more sections in a document. Name and purpose are the only required properties.

Available vocabulary, stated when needed:

- **Fields** — the named fields the block contains, with optionality per field (required, recommended, or optional) and any value constraints. Stated when the block has structured properties; omitted for content-only blocks.
- **Subheadings** — when the block spans multiple sections, declares them with optionality per subheading (required, recommended, or optional).
- **Density** — compact or expanded. Stated when it matters; omitted when the content shape makes the rendering obvious.
- **Recognition** — how this block is identified in a document. Three strategies: by subheading (a single heading or a group of adjacent subheadings), by placement (position identifies it), or by marker. Required when position does not unambiguously identify the block.
- **Placement** — which container this block places into (header, body, footer, declaration, or a doctype-defined container) and any ordering hint against the boundary proximity principle.
- **Dependency implications** — stated only when different from the implicit rule.
- **Conditional behaviour** — rules the block owns about its own behaviour in context ("if the document also includes block X, then do Y"). The block owns its rules; the doctype cannot impose them on inclusion.
- **Container** — declares this block type as a placement destination for other blocks or content.
- **Owner and residence** — as for doctypes.

Blocks may include other blocks; composition recurses; no cycles. Hosting rules attach to the block, not the section: one authoritative instance per semantic scope, permitted hosts owner-defined, moves between hosts are structural not semantic. Contiguity of a block's sections is a default, not a rule.

Shared content across doctypes is a block that doctypes include — not inheritance. Content is defined in one place; ambiguity is flagged rather than resolved silently.

### Block-type recognition

A block type whose specification does not fix its position requires recognition — how a consumer identifies it. Three strategies, in preference order:

- **By subheading** — a single heading, or a group of adjacent/near subheadings that together carry the block. The default for most blocks.
- **By placement** — position identifies it (e.g. title after Declaration, description after title).
- **By marker** — a hidden HTML comment placed after the heading (not before, so it survives RAG chunking). Used only where heading or placement can't discriminate.

### Marker syntax

The canonical marker is an HTML comment with the `aide:block:` prefix:

```
<!-- aide:block:TypeName -->
```

For repeated instances of the same block type:

```
<!-- aide:block:TypeName:instance-id -->
```

The `aide:` prefix namespaces the marker. The `block:` segment is extensible for future marker types. The type name is the plain name from the definition. Instance identifiers are free-form, used only when a block type appears more than once in the same document.

## Identity and versioning

Every document has an identity in its Declaration regardless of publish state. Identity is authoritative; the filename is informative and mirrors it. This is a corpus-integrity requirement: the filename can be renamed and is outside the content, so it cannot be authoritative.

### Identity reference grammar

The primary grammar for referencing a document's version:

`{Name}@v{integer}` — published, immutable.
`{Name}@v{integer}-draft{n}` — working draft.

Absence of a draft marker means published and immutable. Published numbers are never reused. Next cycle opens immediately at the next integer.

**Draft numbering** is optional in the scheme, on by default.

**Reference forms.** `@v27` resolves to the published contract; `@v27-draft` resolves to the highest draft present.

**`.n`** is reserved, unused — available for minor published releases later without colliding with draft counters.

### Filename mirror grammar

The filename mirrors the identity for human readability. Never authoritative. Identity wins on conflict.

`{Name}_v{integer}.{ext}` — published.
`{Name}_v{integer}-draft{n}.{ext}` — working draft.

**Naming keys.** `{name}_v{integer}-{key}{n}` — exactly one key defined: `draft`. An undefined key is a conformance error, not a tolerated variant. Expressed as a named token so adding a key later is a list addition, not a grammar reinterpretation.

### Two rhythms

Design documents and other unpublished documents run on a single rhythm — identity and file move together. Published outcomes (standards, deployed contracts) use a two-rhythm split at the publish boundary.

## Lifecycle states

Three semantic states, independent of physical storage:

- **Current** — the issued authoritative version the corpus resolves for normal use.
- **Superseded** — an older issued version, or a document displaced or withdrawn without reaching an archival disposition of its own.
- **Archived** — a document whose type-specific lifecycle reaches a terminal disposition; the final record is frozen except through the type's permitted correction route.

Working Practices owns the physical handling — how storage represents these states, file movement, retention, and cleanup.

## Format and rendering

**Supported formats.** Markdown is the primary format. YAML and JSON are usable as document formats or embedded inside documents as defined by blocks. HTML is available for long human-facing artefacts when a document demonstrates the need. The declaration and block model work across all supported formats.

**Format fits the job.** Choose the format that best serves the document's primary consumer and content shape. Format is a considered choice, not a default.

**The format rendering rule.** A block is a named set of fields. Structured formats express fields as native properties; prose formats express them as a heading or delimited line. Each format's own existing standards provide a clear default mapping. If a gap appears where the format's conventions do not provide an unambiguous answer, DocMeth authors the mapping.

### Default markdown rendering

A small set of deterministic defaults for markdown rendering. Block definitions override these when they need to.

- **Heading level** follows nesting: a top-level block uses `##`, a subheading within a block uses `###`. Deeper nesting adds levels.
- **Compact fields** render as a single delimited line, pipe-separated, labelled. The Declaration is the model.
- **Expanded fields** render as labelled list items under the block's heading: `- **FieldName:** value`.
- **Containers** have no literal rendering — they are structural. Their children render in sequence.
- **Title** is the markdown document heading (`#`).
- **Description** is the first paragraph beneath the title.

**Density axis.** Compact or expanded, per-block choice, doctype override. How compact and expanded render is determined by the format in use and the defaults above.

**Portability flag.** Anything a block defines that would not port cleanly across formats is flagged for confirmation, not decided silently.

## File conventions

**File naming.** Recommended pattern: `{Prefix}_{DocType}_v{N}.md`. Applied by default, not enforced. Deviate and you manage your own file identification. The Declaration is authoritative for identity and doctype; the filename mirrors for human readability.

**Prefix convention.** File prefixes identify the subject — typically the area, part, or component name. Recommended and applied by default. A prefix makes a file distinguishable in search results, open-file lists, and folder listings regardless of whether it sits in its own subfolder or flat alongside other files.

## The binder as a doctype

The binder is a doctype defined by Documentation Methodology — its structure as a document, how a consumer reads it, what the manifest means. A binder assembles governed documents into a single file for delivery to the AI platform. The manifest records relative paths for every included document, preserving structural relationships when documents leave the file system and enter flat AI context.

The concept of the binder — why it exists, how it is built, inclusion rules, how it delivers content — is owned by Working Practices / Content Delivery.

## Rules

### The split test

Externalise a block into its own document when keeping it in would compromise the primary role of its host — for example when register or open-items volume degrades the ability to search, understand, and use the host document. Below that line, keep it in; file management is easier. Same content, container chosen by scale.

### The Contents/Summary edge

Contents and Summary both feed the read-decision from different angles. Contents maps what is where — it lets the reader judge relevance. Summary gives what the document establishes — its substance in compressed form. Their roles must stay distinct: Contents is a navigation aid; Summary is a condensed statement of the document's contribution. Merging the two, or letting one drift into the other's territory, defeats both.

### Language and integrity rules

Five rules, applying to every governed document:

1. Plain English wherever it will do.
2. Meaning first, code second — name the thing before citing its identifier.
3. Use the terms already in use on the project.
4. Flag a new term rather than introducing it silently.
5. Do not compose plausible metadata, times, versions, paths, or delivery facts where the fact should be observed or read. Distinguish verified state, declared state, and unknown state. Where a value cannot be verified, represent that limitation explicitly rather than producing a plausible substitute.

### Schema placement guidance

When a component defines doctypes or block types, the default recommendation is a separate schema standard with its own version track, distinct from the component's operational standards. This keeps schema changes and operational changes on independent migration paths and improves discoverability for consumers defining new documents. The split test is the override — if the schema definitions are small and change at the same rate as the operational content, keeping them together is acceptable. DocMeth provides this as guidance; the component owner decides.

## Boundaries

Documentation Methodology does not own:

- **Individual doctype definitions** — each lives with the component that knows the most about its subject.
- **Individual block-type definitions** — same principle. DocMeth holds only the common catalogue.
- **The binder concept** — why it exists, how it is used, inclusion rules, how it delivers content. Owned by Working Practices / Content Delivery.
- **Change management methodology** — how change actions are collated, distributed, and executed. Owned by Migration. DocMeth owns the document-level mechanics: the `uses` field and the conformance stamp. Documents are living — they declare their schema dependencies and changes to definitions they use can be applied to them.
- **The cross-review process** — a collaboration convention owned by Working Practices.
- **Packaging and delivery** — how a standard becomes a skill or binder entry. Owned by Infrastructure and Deployment.
- **Rule-weight vocabulary** — the strength model (required, recommended, optional, information). Owned by Standards.
- **Component alias uniqueness** — Core Structure owns the rule that component names and aliases are unique.

## Carries to other components

### PD-F1 — Design two-part structure

The design doctype has two recognised parts: the approach (model and architecture, tested by Check 1) and the detailed design (tested by Check 2). Approach belongs in design, not the brief, because it is solution space.

### PD-F2 — Doctype definitions needed

Once the definition contract exists, all components owning doctypes must define them using it. After DocMeth standards are defined, review all existing components and get them to apply DocMeth standards to their doctype definitions.

### PD-F3 — Schema placement guidance

Schema definition placement guidance is DocMeth-owned. PD's standard should reference it when advising components on their document sets.

### Standards — clarification block

The standard doctype has two parts: the standard itself (lean, stated rules) and clarification (reasoning, justification). Two blocks, joined when small, split by the split test when clarification would bloat the loaded standard. Term agreed: "clarification."

### Core — component alias uniqueness

Component names and aliases must be unique within the framework. Core Structure owns this rule. Aliases are used as type-reference prefixes in the dot-qualified naming grammar.

---

Version note: v4 — cross-review findings F1-F14 applied. Governed-document scaffold, conditional completeness, implicit dependency rule, type-reference resolution, marker syntax, default markdown rendering, field-level optionality, definition representation, date semantics, identity/filename grammar separation added. Declaration field renames (blocks, uses). Dependencies resolved as Declaration field. Carries updated. 2026-09-12. Replaces v3.
