Documentation Methodology | design | DocMeth_Design@v3 | 2026-09-11

## Summary

Documentation Methodology defines the grammar of documents — how they are structured, how they identify themselves, how they are composed from typed building blocks, and the conventions that make them portable and machine-readable. It owns the structural primitives: doctypes, block types, the declaration, rendering conventions, identity and versioning, the definition contract for defining new types, and the writing rules that apply to every governed document. It does not own individual doctype or block-type definitions, and it does not own the binder concept or inclusion rules.

## Model

The grammar has six concerns: composition (how doctypes and blocks build documents), identity (how a document names and versions itself), format (which formats are supported and how blocks express themselves in each), writing (the language conventions that apply to all authored content), activation (the Declaration triggers DocMeth — a document with a Declaration is a governed document), and the definition contract (the grammar for defining new doctypes and block types so that any component can extend the vocabulary without modifying the methodology).

## The definition contract

The definition contract specifies what properties are available when defining a doctype or block type. It is primarily for machine consumption — structured where structure makes it deterministic, prose where judgement is needed, but always formally delineated.

The governing principle: the contract is the definition language, not a form to fill in. A minimal definition is a name and a purpose. A complex definition uses as many of the available properties as it needs. The contract facilitates; it does not mandate structure where structure adds no value.

### Doctype definition

A doctype is the root definition for a document. Name and purpose are the only required properties.

Available vocabulary, stated when needed:

- **Included blocktypes** — which blocks the doctype uses, with optionality per block (required, recommended, or optional for this doctype) and any density override.
- **Block positioning** — where a block goes if different from the block's own placement default, or to resolve ordering between blocks.
- **Dependency implications** — the standard(s) a document inherits by adopting this doctype. These populate the dependencies field in the document header automatically.
- **Format constraint** — narrows the permitted formats when the type requires it (e.g. standards must be markdown for session loading).
- **Owner and residence** — which component owns the definition and where it lives. Implicit from hosting location for most definitions; stated when not obvious.

A doctype includes a block as defined — it does not modify it. A doctype may not suppress a block's fields, add fields, or adjust a block's shape on inclusion. Where two doctypes need different shapes, those are two blocks, which may share a smaller common block. Composition, not inheritance.

Cut as over-engineered: multiple doctype inheritance, abstract doctypes, block self-assignment to doctypes (push model), collision precedence machinery. Residual collision rule: the doctype defines resolution if needed; otherwise flag to the user.

### Block-type definition

A block is a named set of fields with meaning, mapping to one or more sections in a document. Name and purpose are the only required properties.

Available vocabulary, stated when needed:

- **Fields** — the named set of fields with their meaning. Stated when the block has structured properties; omitted for content-only blocks.
- **Subheadings** — when the block spans multiple sections, declares them with optionality per subheading (required, recommended, or optional).
- **Density** — compact or expanded. No assumed default; stated when it matters, omitted when the content shape makes it obvious.
- **Recognition** — how this block is identified in a document. Three strategies: by subheading (a single heading or a group of adjacent subheadings), by placement (position identifies it), or by marker (an HTML comment, used only where heading or placement can't discriminate). Structure-first recognition; marker is the fallback.
- **Placement** — which container this block places into (header, body, footer, or a doctype-defined container) and any ordering hint against the boundary proximity principle.
- **Dependency implications** — the standard(s) a document inherits by using this block type.
- **Conditional behaviour** — rules the block owns about its own behaviour in context ("if the document also includes block X, then do Y"). The block owns its rules; the doctype cannot impose them on inclusion.
- **Container** — declares this block type as a placement destination for other blocks or content.
- **Owner and residence** — as for doctypes.

Blocks may include other blocks; composition recurses; no cycles. Hosting rules attach to the block, not the section: one authoritative instance per semantic scope, permitted hosts owner-defined, moves between hosts are structural not semantic. Contiguity of a block's sections is a default, not a rule.

Shared content across doctypes is a block that doctypes include — not inheritance. Content is defined in one place; ambiguity is flagged rather than resolved silently.

### Block-type recognition

A block type whose specification does not fix its position requires recognition — how a consumer identifies it. Three strategies, in preference order:

- **By subheading** — a single heading, or a group of adjacent/near subheadings that together carry the block. The default for most blocks.
- **By placement** — position identifies it (e.g. title at the top, description beneath title).
- **By marker** — a hidden HTML comment placed after the heading (not before, so it survives RAG chunking). Used only where heading or placement can't discriminate: variable subheading, or repeatable instances.

The marker's form and content are defined once in DocMeth's block-type standard, available to any definition that needs it.

## The common block catalogue

DocMeth holds blocks that are common across documents or usable by any document. Component-specific blocks are defined by their owning component and merge at the document level. No central repository of all blocks.

### The Declaration

The Declaration is a container block in the document header. Its presence is the conformance marker and the corpus recognition mechanism — a document with a Declaration is governed, and DocMeth applies. First block, fixed placement, not overridable.

The Declaration carries labelled fields: identity (name + @version), doctype, date, dependencies, and blocktypes. Dependencies and blocktypes use the grouping syntax for ownership tracking.

In markdown, the Declaration renders as a blockquote with labelled fields:

```
> identity: Name@vN | doctype: type | date: YYYY-MM-DD
> dependencies: StandardA@v1, ComponentName:[StandardB@v2, StandardC@v1]
> blocktypes: Declaration, Summary, ComponentName:[Brief, WorkRegister]
```

In structured formats (YAML, JSON), a reserved top-level `aide` key holds the Declaration fields as sub-properties (nested one level: `aide.identity`, not `aide_identity`). Presence of `aide` = governed.

The name "Declaration" lives in the methodology, not in the document; nothing emits the word.

### Self-describing blocks

Four blocks that make a document self-describing, ordered by depth, clustered at the top of the document in the header region:

- **Title** — what it's called. Recognised by placement (at the top, the way titles always do).
- **Description** — what it is, a line. Recognised by placement (text beneath the title).
- **Contents** — what's in it, the semantic map.
- **Summary** — what it establishes, the substance.

Title and description may be explicitly declared or inferred from ordinary document convention. In structured formats they are keyed because labelling is native; in prose/markdown they are positional because that is native to prose. Same block, expressed the way each format naturally expresses things. This is not special inference machinery — it follows the format rendering rule.

### Other common blocks

**Header and Footer.** Placement containers only, no semantics of their own. Blocks declare they place into them and may carry a hint. Ties resolved by doctype instruction or defined method. Containers are themselves blocks. No literal marker line in markdown; footer start is marked by a horizontal rule; body start is the first heading that is not Contents or Summary.

**Boundary proximity principle.** Value increases toward the file boundaries. Header runs high-to-low from the top; footer runs low-to-high to the end. Containers declare the gradient; blocks place against it.

**Dependencies.** Which standards a document depends on and at which version it was last brought into line. A flat list of `standard@version` pairs with optional grouping for ownership tracking. Direct and inherited entries undifferentiated, conformance stamp not constraint, no presence levels or exact pins. Own identity standard omitted. The currency check gates use, so a partial read from the top must answer "may I use this" without reading to the end.

Dependencies now renders within the Declaration blockquote rather than as a separate header line.

**Contents.** Optional. Lets a reader decide whether to read the document and what it covers, at lowest cost. Primary consumer is a file-scanning AI making a partial-read-and-stop decision.

- Earns its place when a reader could not decide from the Declaration alone whether to keep reading.
- Curated semantic map, grouped descriptive entries — not heading repetition.
- Stable heading or section-number locators, never line numbers.
- Density: compact (rendered inline / delimited, never a vertical list).
- The doctype owner sets the default for that type (on, off, or conditional) and defines depth.

**Summary.** Optional. States what the document establishes, absorbed quickly.

- Earns its place when the document's substance needs a compressed statement.
- States the key model, key points, and defining items — the substance, not a gesture at it.
- Stated, not explained. No expansion, reasoning, or qualification; that is the body's role.
- The body expands; it does not restate. Re-establishing what the Summary states is a defect.
- The doctype owner governs whether Summary is used for that type.

**Version note.** Metadata at the top of the footer (low-value end of the footer gradient). One line, current version only, never a list. Historical version notes do not accumulate; the decisions document holds what mattered.

**Parked.** Tags — Core owns the definition. Returns to the common catalogue only if DocMeth grammar needs to know about it specifically. References — no consumer has appeared; decide on its own merits when one does.

### The guide doctype

A guide is a human-facing output document, the counterpart to the standard. Standard for the machine, guide for the human. General-purpose — any component may produce one. Defined by DocMeth as a common doctype available to all. Ships with what it explains — a deployed standard, a capability, a tool. Published and versioned like a standard. Distinct from the internal design doctype: design is development-time reasoning, guide is use-time explanation for someone using the thing in the world.

### Aggregation model

One model, several output forms — index, navigation view, concatenated collation. Input is documents carrying self-describing blocks. Aggregation picks how deep it needs to go: a navigation index may need only title and description; a richer collation may pull summary too. The binder is deliberately kept separate; possible overlap reviewed later, only if it doesn't compromise the binder's role.

## Identity and versioning

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

## Lifecycle states

Three semantic states, independent of physical storage:

- **Current** — the issued authoritative version the corpus resolves for normal use.
- **Superseded** — an older issued version, or a document displaced or withdrawn without reaching an archival disposition of its own.
- **Archived** — a document whose type-specific lifecycle reaches a terminal disposition; the final record is frozen except through the type's permitted correction route.

Working Practices owns the physical handling — how storage represents these states, file movement, retention, and cleanup.

## Format and rendering

**Supported formats.** Markdown is the primary format. YAML and JSON are usable as document formats or embedded inside documents as defined by blocks. HTML is available for long human-facing artefacts when a document demonstrates the need. The declaration and block model work across all supported formats.

**Format fits the job.** Choose the format that best serves the document's primary consumer and content shape. Format is a considered choice, not a default.

**The format rendering rule.** A block is a named set of fields. Structured formats express fields as native properties; prose formats express them as a heading or delimited line. Each format's own existing standards provide a clear default mapping — no additional mapping tables are needed at this stage. If a gap appears where the format's conventions do not provide an unambiguous answer, DocMeth authors the mapping.

**Density axis.** Compact or expanded, per-block default, doctype override. How compact and expanded render is determined by the format in use.

**Portability flag.** Anything a block defines that would not port cleanly across formats is flagged for confirmation, not decided silently.

## File conventions

**File naming.** Recommended pattern: `{Prefix}_{DocType}_v{N}.md`. Applied by default, not enforced. Deviate and you manage your own file identification. The header is authoritative for identity and doctype; the filename mirrors for human readability.

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
- **Change management methodology** — how change actions are collated, distributed, and executed. Owned by Migration. DocMeth owns the document-level mechanics: the Dependencies field and the conformance stamp. Documents are living — they declare their schema dependencies and changes to definitions they use can be applied to them.
- **The cross-review process** — a collaboration convention owned by Working Practices.
- **Packaging and delivery** — how a standard becomes a skill or binder entry. Owned by Infrastructure and Deployment.
- **Rule-weight vocabulary** — the strength model (required, recommended, optional, information). Owned by Standards.

## Carries to other components

### PD-F1 — Design two-part structure

The design doctype has two recognised parts: the approach (model and architecture, tested by Check 1) and the detailed design (tested by Check 2). Approach belongs in design, not the brief, because it is solution space.

### PD-F2 — Doctype definitions needed

Once the definition contract exists, all components owning doctypes must define them using it. After DocMeth standards are defined, review all existing components and get them to apply DocMeth standards to their doctype definitions.

### PD-F3 — Schema placement guidance

Schema definition placement guidance is DocMeth-owned. PD's standard should reference it when advising components on their document sets.

### Standards — clarification block

The standard doctype has two parts: the standard itself (lean, stated rules) and clarification (reasoning, justification). Two blocks, joined when small, split by the split test when clarification would bloat the loaded standard. Term agreed: "clarification."

---

Version note: v3 — definition contract added (doctype and block-type contracts, governing principle, header format evolution, self-describing blocks, guide doctype, aggregation model, schema placement guidance). Carries restored. Ownership-designation rule softened to optional. Path-authority claim removed. 2026-09-11. Replaces v2.
