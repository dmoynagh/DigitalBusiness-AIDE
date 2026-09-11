# Documentation Methodology — Authoring Standard

> identity: DocumentationMethodology_Authoring_Standard@v4 | doctype: standard | date: 2026-09-12
> uses: DocumentationMethodology_Definitions_Standard@v4

Use when authoring, structuring, or versioning a governed document.

## What this standard is for

Information. This standard defines how to author and use governed documents — the Declaration, identity, versioning, format, and writing conventions. For defining new types, see the Schema Standard. For the common types DocMeth defines, see the Definitions Standard.

## The governed-document scaffold

Information. The methodology provides an implicit scaffold for every governed document:

- **Declaration** — the first block, fixed topmost. Every governed document has one.
- **Title** — recognised by placement, immediately after Declaration. The human-readable name.
- **Description** — recognised by placement, immediately after Title. What the document is, in a line.
- **Header, Body, Footer** — structural containers. Every governed document has them. Containers exist structurally even when they contain no explicitly declared blocks.

Information. A doctype adds content blocks beyond this scaffold. Contents, Summary, Version note, and all component-defined blocks are doctype choices, not methodology defaults.

## The Declaration — recognition and activation

Required. Every governed document has a Declaration. It is the first block, fixed topmost, not overridable. Its presence is what makes a document governed.

Required. The Declaration carries labelled fields:

- identity (required) — name + @version, the authoritative reference
- doctype (required) — the document's type
- date (required) — the date this version was produced, YYYY-MM-DD
- uses (optional) — standards this document depends on, as `standard@version` pairs. Populated automatically from the dependency implications of the document's doctype and included block types. Conformance stamp, not constraint. The grouping syntax `name:[item1, item2]` tracks ownership.
- blocks (optional) — non-scaffold typed blocks present in this document. The scaffold (Declaration, Title, Description, Header, Body, Footer) is not re-stated. The grouping syntax tracks ownership.

Information. In markdown, the Declaration renders as a blockquote with labelled fields:

```
> identity: Name@vN | doctype: type | date: YYYY-MM-DD
> uses: StandardA@v1, ComponentName:[StandardB@v2, StandardC@v1]
> blocks: Summary, ComponentName:[Brief, WorkRegister]
```

Information. In structured formats (YAML, JSON), a reserved top-level `aide` key holds the Declaration fields as sub-properties (nested one level: `aide.identity`, not `aide_identity`). Presence of `aide` = governed.

Information. The name "Declaration" is methodology vocabulary — nothing in the document emits the word.

## Self-describing blocks

Information. Four blocks make a document self-describing, ordered by depth in the header region: title (what it's called), description (what it is), contents (what's in it), summary (what it establishes).

Information. Title and description are inferred from natural document convention in prose formats (position and shape) and keyed in structured formats. This follows the format rendering rule.

## Identity and versioning

### Identity reference grammar

Required. The primary grammar for referencing a document's version:

`{Name}@v{integer}` — published, immutable.
`{Name}@v{integer}-draft{n}` — working draft.

Required. Every document has an identity in its Declaration. Identity is authoritative; the filename mirrors it. Identity wins on conflict.

Required. Absence of a draft marker means published and immutable. Published version numbers are never reused. Next cycle opens at the next integer.

Required. Every draft carries its sequence number.

Information. Reference forms: `@v27` resolves to the published contract; `@v27-draft` resolves to the highest draft present.

Information. `.n` is reserved, unused — available for minor published releases later.

### Filename mirror grammar

Recommended. The filename mirrors the identity for human readability. Never authoritative.

`{Name}_v{integer}.{ext}` — published.
`{Name}_v{integer}-draft{n}.{ext}` — working draft.

Information. Naming keys: `{name}_v{integer}-{key}{n}`. One key defined: `draft`. An undefined key is a conformance error.

### Two rhythms

Information. Design documents run on a single rhythm — identity and file move together. Published outcomes use a two-rhythm split at the publish boundary.

## Lifecycle states

Information. Three semantic states, independent of physical storage:

- **Current** — the issued authoritative version for normal use.
- **Superseded** — an older issued version, or a document displaced without reaching archival.
- **Archived** — terminal disposition; the record is frozen except through the type's permitted correction route.

Information. Working Practices owns physical handling.

## File conventions

Recommended. File naming pattern: `{Prefix}_{DocType}_v{N}.md`. Applied by default, not enforced. The Declaration is authoritative; the filename mirrors for readability.

Recommended. File prefixes identify the subject — the area, part, or component name.

## Format and rendering

Recommended. Choose the format that best serves the document's primary consumer and content shape. Format is a considered choice, not a default. Markdown is the primary format; YAML, JSON, and HTML are available where the content warrants them.

Required. A block is a named set of fields. Structured formats express fields as native properties; prose formats express them as a heading or delimited line. Each format's own standards provide the default mapping.

### Default markdown rendering

Information. Deterministic defaults for markdown. Block definitions override when needed.

- **Heading level** follows nesting: a top-level block uses `##`, a subheading within a block uses `###`. Deeper nesting adds levels.
- **Compact fields** render as a single delimited line, pipe-separated, labelled. A block definition may override this — the Declaration renders compact fields across multiple lines (one per field group).
- **Expanded fields** render as labelled list items: `- **FieldName:** value`.
- **Containers** have no literal rendering — structural only. Children render in sequence.
- **Title** is the markdown document heading (`#`).
- **Description** is the first paragraph beneath the title.

Required. Anything a block defines that would not port cleanly across formats is flagged for confirmation, not decided silently.

## The split test

Recommended. Externalise a block into its own document when keeping it in would compromise the primary role of its host. Below that line, keep it in — file management is easier.

## The Contents/Summary edge

Recommended. Contents maps what is where (navigation). Summary gives what the document establishes (substance). Their roles must stay distinct.

## Language and integrity

Required. Five rules applying to every governed document:

1. Plain English wherever it will do.
2. Meaning first, code second — name the thing before citing its identifier.
3. Use the terms already in use on the project.
4. Flag a new term rather than introducing it silently.
5. Do not compose plausible metadata, times, versions, paths, or delivery facts where the fact should be observed or read. Distinguish verified state, declared state, and unknown state.

---

Version note: v4 — round 3 corrections. Uses field propagation rule added. Blocks example corrected. Compact rendering override noted. 2026-09-12. Replaces v3.
