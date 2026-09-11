Documentation Methodology — Schema Standard | standard | DocumentationMethodology_Schema_Standard@v1 | 2026-09-11

Use when defining a new doctype or block type.

## What this standard is for

Information. This standard defines the grammar for defining new doctypes and block types — the definition contract. It is for framework developers extending the type vocabulary. For authoring governed documents, see the Documentation Methodology Authoring Standard. For the common types DocMeth itself defines, see the Documentation Methodology Definitions Standard.

## The definition contract

Required. The definition contract is the grammar for defining new doctypes and block types. Name and purpose are the only required properties. All other properties are available vocabulary — stated when they add value, omitted when they do not.

Information. The contract is the definition language, not a form to fill in. A minimal definition is a name and a purpose. A complex definition uses as many of the available properties as it needs.

## Doctype definition

Required. A doctype definition states a name and a purpose.

Recommended. Available vocabulary for a doctype definition, each stated when needed:

- **Included blocktypes** — which blocks the doctype uses. For each: the optionality for this doctype (required, recommended, or optional) and any density override.
- **Block positioning** — where a block goes if different from the block's own placement default, or to resolve ordering between blocks.
- **Dependency implications** — the standard(s) a document inherits by adopting this doctype. These populate the dependencies field in the Declaration automatically.
- **Format constraint** — narrows the permitted formats when the type requires it.
- **Owner and residence** — which component owns the definition and where it lives. Implicit from hosting location for most definitions; stated when not obvious.

Required. A doctype includes a block as defined and does not modify it. No field suppression, no field addition, no shape adjustment on inclusion.

## Block-type definition

Required. A block-type definition states a name and a purpose.

Recommended. Available vocabulary for a block-type definition, each stated when needed:

- **Fields** — the named fields the block contains. Stated when the block has structured properties; omitted for content-only blocks.
- **Subheadings** — when the block spans multiple sections, declares them with optionality per subheading (required, recommended, or optional).
- **Density** — compact or expanded. Stated when it matters; omitted when the content shape makes the rendering obvious.
- **Recognition** — how this block is identified in a document. Three strategies: by subheading (a heading or group of adjacent subheadings), by placement (position identifies it), or by marker (an HTML comment placed after the heading, used only where subheading or placement can't discriminate).
- **Placement** — which container this block places into (header, body, footer, declaration, or a doctype-defined container) and any ordering hint.
- **Dependency implications** — the standard(s) a document inherits by using this block type.
- **Conditional behaviour** — rules the block owns about its own behaviour in context. The block owns its rules; the doctype cannot impose them on inclusion.
- **Container** — declares this block as a placement destination for other blocks or content.
- **Owner and residence** — as for doctypes.

## Block-type recognition

Recommended. A block type whose specification does not fix its position requires recognition — how a consumer identifies it. Three strategies, in preference order: by subheading (the default for most blocks), by placement (position identifies it), by marker (fallback only). The marker is an HTML comment placed after the heading (not before) so it survives RAG chunking.

## Composition rules

Required. Blocks may include other blocks; composition recurses; no cycles. Shared content across doctypes is a block that doctypes include — composition, not inheritance. Where two doctypes need different shapes, those are two blocks, which may share a smaller common block.

Required. Content is defined in one place. Ambiguity is flagged rather than resolved silently.

## Schema placement guidance

Recommended. When a component defines doctypes or block types, a separate schema standard with its own version track is preferred over embedding definitions in the component's operational standard. This keeps schema changes and operational changes on independent migration paths. The split test is the override — if the definitions are small and change at the same rate, keeping them together is acceptable.

---

Version note: v1 — split from DocumentationMethodology_Standard@v1. Definition contract added from DocMeth_Design@v3. 2026-09-11.
