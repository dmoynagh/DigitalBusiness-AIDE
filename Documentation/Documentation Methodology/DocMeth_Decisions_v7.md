> identity: DocMeth_Decisions@v7 | doctype: decisions | updated: 2026-09-14

# Documentation Methodology — Decisions

All settled items. v7 reflects the clean-sheet rebuild of 2026-09-14. Decisions from v6 that still hold are carried; decisions superseded by the rebuild are marked. New decisions from the rebuild session are added.

## D1 — DocMeth owns grammar only, not individual definitions

Carried from v6. Individual doctype and block-type definitions live with the component that knows the most about them. DocMeth defines what a doctype is, what a block is, how they compose, and the common catalogue of blocks usable by any document.

## D2 — Composition, not inheritance

Carried from v6. Doctypes compose blocks by inclusion. A doctype includes a block as defined and does not modify it. Where two doctypes need different shapes, those are two blocks. Override-on-include is inheritance under another name. Also cut: multiple doctype inheritance, abstract doctypes, block self-assignment, collision precedence machinery.

## D3 — Declaration as conformance marker and activation trigger

Carried from v6. The Declaration's presence is both the recognition mechanism (is this a governed document?) and the activation trigger (DocMeth applies). A document with a Declaration is a governed document.

## D4 — Dependencies as a Declaration field

Carried from v6. Dependencies (`uses`) is a labelled field within the Declaration, not a separate block. The grouping syntax `name:[item1, item2]` tracks which owner contributed each dependency.

## D5 — Common catalogue scope

Updated from v6. The common catalogue holds: Declaration, Title, Description, Body, Footer, Contents, Summary, Version note, Manifest. Nine blocks. Header removed as a named element (D26).

## D6 — Contents and Summary are optional

Carried from v6. Both blocks earn their place by function, not by rule. The doctype owner decides the default for their type.

## D7 — The Contents/Summary edge as a grammar rule

Carried from v6. Contents maps what is where; Summary gives what the document establishes. DocMeth owns the edge definition because it defines both blocks.

## D8 — The split test as grammar

Carried from v6. Externalise a block when keeping it in would compromise the primary role of its host.

## D9 — Identity and versioning as a single function

Carried from v6 in substance, merged. Identity owns the name. Versioning owns the version format and behaviour. Both use the Declaration and filename inference. Combined into one section to eliminate cross-referencing.

## D10 — Declaration labelled blockquote format

Carried from v6 (was D16). Multi-line blockquote with labelled, pipe-delimited fields. Structured formats use an `aide` container key.

## D11 — Title and Description as self-describing blocks after Declaration

Carried from v6 (was D17). Recognised by placement, following the Declaration.

## D12 — The claimed-versus-verified rule

Carried from v6 (was D14). Do not compose plausible metadata where the fact should be observed. Fifth writing/integrity rule.

## D13 — Lifecycle states dropped

**Supersedes v6 D13.** Lifecycle states (Current, Superseded, Archived) were introduced without a demonstrated consumer and no operational behaviour was defined for them. Dropped. Add when something needs them with the behaviour attached.

## D14 — The definition contract is facilitative, not prescriptive

Carried from v6 (was D15). Name and purpose are the only always-required properties. Everything else is available vocabulary.

## D15 — Density absorbed into Content

**New.** The separate Density property was absorbed into the blocktype Content property. Content now describes the full shape of a block — headings, sections, fields, density — in one place.

## D16 — Conditional behaviour replaced by Instructions

**New.** The Conditional behaviour property was replaced by Instructions — a clearer name that covers the same ground and extends to doctype-level and document-level instructions.

## D17 — Container property dropped

**New.** Footer is the only element that functions as a container in practice, and it is defined by its boundary signal. A generic Container property added formalism without function.

## D18 — Owner and residence property dropped

**New.** Implicit from where the definition lives. The existing standard acknowledged this but kept the property anyway.

## D19 — Header dropped as a named structural element

**New.** The elements that sit in the header area (Declaration, Title, Description) are defined individually by placement. Naming the container added formalism without function.

## D20 — Three-standard split by load profile

**New.** DocMeth splits into three standards based on load profile, not topic:
- **DocumentationMethodology_Standard** (main, always-on) — what DocMeth is, how it works, what to do with it
- **DocumentationMethodology_SchemaDefinitions_Standard** (always-on) — the type definitions DocMeth owns
- **DocumentationMethodology_SchemaAuthoring_Standard** (on-demand) — how to define new types

A fourth standard (DocumentationMethodology_Authoring_Standard) is planned for when authoring guidance grows enough to justify its own load. Currently in the main standard.

## D21 — Content-triggered application with graceful degradation

**New.** DocMeth can add value to a document that isn't formally governed. Individual features activate from defined elements or patterns in a document — if what a feature needs is present, it can apply. The Declaration is the primary trigger but not the only one.

## D22 — Instructions as a composable scoped mechanism

**New.** Instructions are rules applied to documents, scoped from general to specific: DocMeth defaults → doctype → block → document. More specific scope takes precedence. Document-level instructions must be stated under a heading recognised as instructions, or in a doctype-defined blocktype. Body prose without either is content, not instructions.

## D23 — Source-defined dependency propagation, one-level only

**New.** Each standard defines which of its dependencies should propagate to the `uses` field of consuming documents. Propagation is one level — the consuming document applies propagation rules for the standards it directly lists, not recursively. The defining standard itself always belongs in `uses`. Universal standards (the main DocMeth standard) are exempt.

This replaces the universal-exemption list approach from the existing standards, where three named standards were exempt by identity.

## D24 — Blocktype spec simplified to six properties

**New.** Name, Purpose, Content, Placement (optional), Recognition (optional), Instructions. Fields, Subheadings, and Density merged into Content. Container, Owner/residence, Dependency implications, and Conditional behaviour dropped.

## D25 — Doctype spec simplified to four properties

**New.** Name, Purpose, Content, Instructions. Content carries blocktypes with optionality, ordering, metadata, conventions. Format constraint and Format conventions sit in Instructions where needed.

## D26 — Default and override as a governing principle

**New.** DocMeth defines default behaviour; defaults can be overridden by logic inherited by, applied to, or defined within the document. This is a principle, not a per-feature rule.

## D27 — Grouping syntax is organisational only

**New.** The grouping syntax (`prefix:[items]`) flattens to type names — the prefix is not part of the type name. Dot-qualified disambiguation (`pd.Brief`) is separate from grouping and used only to resolve collisions.

## D28 — Version increment behaviour

**New.** Saving a draft increments the draft number. Publishing increments the published version number. A new versioned document starts at `v1-draft1`.

## D29 — Type resolution path

**New.** Type definitions are found by loading the standards referenced in `uses`, then resolving type names against the definitions in those standards. Unqualified names must resolve to exactly one definition; ambiguous names use dot-qualified form.

---

Version note: v7 — clean-sheet rebuild. Twenty-nine decisions; thirteen carried from v6, sixteen new or superseded. 2026-09-14. Replaces v6.
