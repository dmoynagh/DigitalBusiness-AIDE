> identity: DocumentationMethodology_Schema_Standard@v4 | doctype: standard | updated: 2026-09-12

# Documentation Methodology — Schema Standard

Use when defining a new doctype or block type.

## What this standard is for

Information. This standard defines the grammar for defining new doctypes and block types — the definition contract. It is for framework developers extending the type vocabulary. For authoring governed documents, see the Authoring Standard. For the common types DocMeth defines, see the Definitions Standard.

## The definition contract

Required. The definition contract is the grammar for defining new doctypes and block types. Name and purpose are the only always-required properties. All other properties are available vocabulary — stated when they add value, omitted when they do not.

Information. The contract is the definition language, not a form to fill in. A minimal definition is a name and a purpose.

### Conditional completeness

Required. A property becomes required when omitting it would leave the definition ambiguous: a block whose position does not identify it must state its recognition; a block with structured fields must declare them. A definition that would be broken without a property must include that property.

### Definition representation

Required. A definition is written as a heading naming the type, followed by labelled properties as list items. Name is the heading. Purpose is the first property. Remaining properties follow in any order. In structured formats, a definition is a keyed object with the same property names.

### Implicit dependency rule

Information. A type defined in a versioned standard implicitly carries that defining standard as its dependency implication. A definition only states dependency implications explicitly when they differ from the defining standard.

Required. Dependency implications from the document's doctype and included block types populate the Declaration's `uses` field automatically. The `uses` field is syntactically optional in the Declaration but is present whenever resolved dependencies exist.

Required. `uses` lists the standards whose change would specifically require review of this document. Universal dependencies — standards whose change triggers review of the entire governed corpus — are exempt because they carry no discrimination power. Three qualify as universal: the Authoring Standard (governs all governed documents), the common and scaffold block definitions in the Definitions Standard (present or available in all governed documents), and the standard doctype definition in the Standards Authoring Standard (every standard is one). A standard that defines its own doctype does not list itself.

Required. Nested included blocks participate in dependency propagation — a block that includes another block acquires that block's defining standard as a dependency implication, which propagates to the hosting document's `uses` field under the same rules as direct inclusions.

## Doctype definition

Required. A doctype definition states a name and a purpose.

Recommended. Available vocabulary for a doctype definition, each stated when needed:

- **Included blocktypes** — which blocks the doctype uses beyond the governed-document scaffold. For each: the optionality for this doctype (required, recommended, optional, or conditional) and any density override. A conditional entry states its condition — for example: "required when the design feeds a build, omitted otherwise."
- **Block positioning** — where a block goes if different from the block's own placement default, or to resolve ordering between blocks.
- **Dependency implications** — stated only when different from the implicit rule (defining standard).
- **Format constraint** — narrows the permitted formats when the type requires it.
- **Format conventions** — format-specific structural behaviour owned by the doctype. Stated when the type has rendering conventions beyond what block definitions and the default markdown rendering cover.
- **Owner and residence** — which component owns the definition. Implicit from hosting location for most definitions; stated when not obvious.

Required. A doctype includes a block as defined and does not modify it. No field suppression, no field addition, no shape adjustment on inclusion.

## Block-type definition

Required. A block-type definition states a name and a purpose.

Recommended. Available vocabulary for a block-type definition, each stated when needed:

- **Fields** — the named fields the block contains, with optionality per field (required, recommended, optional, or conditional) and any value constraints. Stated when the block has structured properties; omitted for content-only blocks.
- **Subheadings** — when the block spans multiple sections, declares them with optionality per subheading (required, recommended, optional, or conditional).
- **Density** — compact or expanded. Stated when it matters; omitted when the content shape makes it obvious.
- **Recognition** — how this block is identified. Three strategies: by subheading, by placement, or by marker. Required when position does not unambiguously identify the block.
- **Placement** — which container this block places into and any ordering hint.
- **Dependency implications** — stated only when different from the implicit rule (defining standard).
- **Conditional behaviour** — rules the block owns about its own behaviour in context. The block owns its rules; the doctype cannot impose them on inclusion.
- **Container** — declares this block as a placement destination for other blocks or content.
- **Owner and residence** — as for doctypes.
- **Included blocktypes** — which blocks this block includes. The same semantics as for doctypes: for each included block, the optionality for this parent block (required, recommended, optional, or conditional) and any density override. A block may not include itself; composition must not cycle (see Composition rules).

## Block-type recognition

Required. A block type whose position does not unambiguously identify it must state its recognition strategy. Three strategies, in preference order: by subheading (the default for most blocks), by placement (position identifies it), by marker (fallback only).

### Marker syntax

Information. The canonical marker is an HTML comment placed after the heading:

```
<!-- aide:block:TypeName -->
```

For repeated instances of the same block type:

```
<!-- aide:block:TypeName:instance-id -->
```

## Composition rules

Required. Blocks may include other blocks; composition recurses; no cycles. Shared content across doctypes is a block that doctypes include — composition, not inheritance. Where two doctypes need different shapes, those are two blocks.

Required. Content is defined in one place. Ambiguity is flagged rather than resolved silently.

Required. The `blocks` Declaration field lists only directly hosted non-scaffold typed blocks, not the recursive closure of blocks included by other blocks. A Brief instance lists `Brief` in `blocks`; it does not also list blocks that Brief itself includes.

## Type-reference resolution

Required. Type names must be unique within each kind in their owning component — a component may not define two doctypes with the same name, or two block types with the same name. The same name may intentionally exist as both a doctype and a block type within one component, distinguished by kind. Independently owned components may use the same name without coordination.

Recommended. Unqualified names are the default when the name is unique within the document's active `uses` scope. The dot-qualified form disambiguates on collision: `pd.brief`, where the prefix is the component's declared alias.

Information. Resolution path: a non-universal type's authoritative definition resolves through its defining standard in the document's `uses` field. Universal types — those whose defining standard is exempt from `uses` under the universal-dependency rule — resolve through the framework's universal standards without appearing in `uses`. The three universal standards are `DocumentationMethodology_Authoring_Standard` (governs all governed documents), `DocumentationMethodology_Definitions_Standard` (common and scaffold blocks), and `Standards_Authoring_Standard` (the standard doctype).

Required. Type references in Declaration fields (`doctype`, `blocks`) are serialized in lowercase. Definition headings are the display form; lowercase is the reference form. Type-name matching is case-insensitive. `uses` entries are document identity references and preserve the authoritative identity form, including version.

## Schema placement guidance

Recommended. When a component defines doctypes or block types, a separate schema standard with its own version track is preferred over embedding definitions in the component's operational standard. The split test is the override — if the definitions are small and change at the same rate, keeping them together is acceptable.

---

Version note: v4 — round 3 corrections. Dependency-to-uses propagation rule added. Format conventions added to doctype vocabulary. Type resolution wording corrected. 2026-09-12. Replaces v3.
