Documentation Methodology — Authoring Standard | standard | DocumentationMethodology_Authoring_Standard@v1 | 2026-09-11

Use when authoring, structuring, or versioning a governed document.

## What this standard is for

Information. This standard defines how to author and use governed documents — the Declaration, identity, versioning, format, and writing conventions. It is for framework users authoring documents. For defining new types, see the Documentation Methodology Schema Standard. For the common types DocMeth defines, see the Documentation Methodology Definitions Standard.

## The Declaration — recognition and activation

Required. Every governed document has a Declaration. It is a container block at the top of the document, fixed placement, not overridable. Its presence is what makes a document governed — Documentation Methodology's grammar, standards, and behaviours apply to any document that carries one.

Required. The Declaration carries labelled fields: identity (name + @version), doctype, date. It also carries dependencies and blocktypes when present.

Required. Dependencies is a flat list of `standard@version` pairs stating which standards a document depends on and at which version it was last brought into line. Conformance stamp, not constraint. The grouping syntax `name:[item1, item2]` tracks which owner contributed each dependency.

Information. In markdown, the Declaration renders as a blockquote with labelled fields:

```
> identity: Name@vN | doctype: type | date: YYYY-MM-DD
> dependencies: StandardA@v1, ComponentName:[StandardB@v2, StandardC@v1]
> blocktypes: Declaration, Summary, ComponentName:[Brief, WorkRegister]
```

Information. In structured formats (YAML, JSON), a reserved top-level `aide` key holds the Declaration fields as sub-properties (nested one level: `aide.identity`, not `aide_identity`). Presence of `aide` = governed.

Information. The name "Declaration" is methodology vocabulary — nothing in the document emits the word.

## Self-describing blocks

Information. Four blocks make a document self-describing, ordered by depth in the header region: title (what it's called), description (what it is), contents (what's in it), summary (what it establishes). Title and description are inferred from natural document convention in prose formats and keyed in structured formats.

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

Required. Anything a block defines that would not port cleanly across formats is flagged for confirmation, not decided silently.

## The split test

Recommended. Externalise a block into its own document when keeping it in would compromise the primary role of its host. Below that line, keep it in — file management is easier. Same content, container chosen by scale.

## The Contents/Summary edge

Recommended. Contents maps what is where (navigation). Summary gives what the document establishes (substance). Their roles must stay distinct. Letting one drift into the other's territory defeats both.

## Language and integrity

Required. Five rules applying to every governed document:

1. Plain English wherever it will do.
2. Meaning first, code second — name the thing before citing its identifier.
3. Use the terms already in use on the project.
4. Flag a new term rather than introducing it silently.
5. Do not compose plausible metadata, times, versions, paths, or delivery facts where the fact should be observed or read. Distinguish verified state, declared state, and unknown state.

---

Version note: v1 — split from DocumentationMethodology_Standard@v1. Declaration format updated to labelled blockquote. Self-describing blocks added. 2026-09-11.
