> identity: DocumentationMethodology_SchemaAuthoring_Standard@v1 | doctype: standard | updated: 2026-09-14

# Documentation Methodology — Schema Authoring Standard

Use when defining new blocktypes or doctypes, or modifying existing ones.

This standard defines the rules for writing schema definitions — the definition contract. For the types DocMeth itself defines, see the Schema Definitions standard. For how schema is used in documents, see the main Documentation Methodology standard.

---

## The definition contract

The definition contract is the grammar for defining new blocktypes and doctypes. It facilitates — it does not mandate structure where structure adds no value. A minimal definition is a name and a purpose. A complex definition uses as many properties as it needs.

---

## Blocktype definition

A blocktype is defined with the following properties. Name and Purpose are always required. Other properties are stated when they add value.

- **Name** — what the block is called. The heading in the definition.
- **Purpose** — what it's for. Always the first property.
- **Content** — what the block contains: headings, sections, general content, named fields with optionality (required, recommended, optional). As specific or generic as the author deems necessary. Used for recognition, authoring and interpretation. Included blocktypes are defined here.
- **Placement** — (optional) where in the document the block belongs. Defaults to general document flow, or as defined by the including doctype.
- **Recognition** — (optional) how to identify this block when its content definition alone is not sufficient. Three strategies in preference order: by subheading, by placement, by marker.
- **Instructions** — block-specific rules applied when authoring, reading or using this block.

### Conditional completeness

A property becomes required when omitting it would leave the definition ambiguous. A block whose content and position do not identify it must state its recognition. A block with structured fields must declare them in its content. The test: would a consumer be unable to recognise, render or use the block without this property? If yes, include it.

### Composition

Blocktypes can include other blocktypes — defined in the content specification. Composition recurses but must not cycle. A blocktype may not include itself, directly or indirectly.

Shared content across doctypes is a block that doctypes include — not inheritance. Content is defined in one place.

### Recognition strategies

When a block cannot be identified by its content alone:

1. **By subheading** — the block is identified by a heading matching its blocktype name. The block's content extends from that heading to the next heading at the same or higher level. This is the default and preferred strategy for most blocks.
2. **By placement** — position in the document identifies it. Used for blocks with fixed positions (e.g. Title after Declaration).
3. **By marker** — an HTML comment placed after the heading. The fallback when subheading and placement cannot discriminate.

Marker syntax:
```
<!-- aide:block:TypeName -->
```

For repeated instances of the same block type:
```
<!-- aide:block:TypeName:instance-id -->
```

The `aide:block:` prefix is reserved. Markers are placed after the heading, not before, so they survive content chunking.

---

## Doctype definition

A doctype is defined with the following properties. Name and Purpose are always required.

- **Name** — what the document type is called. The heading in the definition.
- **Purpose** — what this type of document is for, its role and behaviour. Always the first property.
- **Content** — what the doctype defines for its documents: blocktypes with optionality (required, recommended, optional), ordering, metadata, conventions, and any other information that applies.
- **Instructions** — doctype-specific rules applied when authoring, reading or using documents of this type.

### The no-modification rule

A doctype includes a blocktype as defined — it does not modify it. No field suppression, no field addition, no shape adjustment on inclusion. The block's own definition is authoritative for its content, fields and structure.

Where two doctypes need different shapes for similar content, define two blocktypes. They may share a smaller common blocktype through composition. This is composition, not inheritance — visible duplication is preferred over hidden override chains.

### Doctype-level placement

A doctype may specify where each of its included blocktypes is placed in the document and their ordering relative to each other. This overrides the block's own default placement for documents of this type.

---

## Definition representation

A definition is written as a heading naming the type, followed by labelled properties as list items. Name is the heading. Purpose is the first property. Remaining properties follow in any order.

In structured formats (YAML, JSON), a definition is a keyed object with the same property names.

Example — a blocktype definition:

### Work register

- **Purpose:** The ledger of confirmed work owed and not yet delivered.
- **Content:** Entries listed under subheadings by status. Fields per entry: description (required), source (required), status (required), notes (optional).
- **Recognition:** by subheading.
- **Placement:** body.
- **Instructions:** Updated at the end of each session. Completed items are removed, not marked done.

---

## Dependency propagation

When a standard defines blocktypes or doctypes, it should specify which of its dependencies should propagate to the `uses` field of documents that consume those types. A standard that inherits other standards for its own internal behaviour, but where those inherited standards have no direct application to consuming documents, does not propagate them.

State the propagation rule in the standard itself, typically as a short section at the top (see the Schema Definitions standard for an example).

---

## Placement guidance

(Recommended) When a component defines blocktypes or doctypes, the default recommendation is a separate schema standard with its own version track, distinct from the component's operational standards. This keeps schema changes and operational changes on independent version paths and improves discoverability.

The override: if the schema definitions are small and change at the same rate as the operational content, keeping them together is acceptable. The component owner decides.

---

## The split test

(Recommended) Externalise a block into its own document when keeping it in would compromise the primary role of its host. Below that line, keep it in — file management is easier. This applies to blocks within documents and to definitions within standards.

---

## Checklist — before publishing a definition

1. Does it have a name and purpose?
2. Could a consumer recognise the block or apply the doctype from this definition alone?
3. Are all structured fields declared with optionality?
4. If the block's content and position do not identify it, is a recognition strategy stated?
5. Does the definition use the properties from the contract, or invent its own?
6. Is the dependency propagation rule stated in the hosting standard?
7. Does the definition follow the no-modification rule — no inherited block is adjusted on inclusion?

---

Version note: v1 — clean-sheet rebuild. Replaces DocumentationMethodology_Schema_Standard_v4. Definition contract simplified (6 blocktype properties, 4 doctype properties). Worked example and pre-publish checklist added. 2026-09-14.
