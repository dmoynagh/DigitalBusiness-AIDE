Documentation Methodology | working | DocumentationMethodology_Working@v2 | 2026-09-11

## Confirmed items — session 2026-09-10

### File naming convention

Recommended pattern: `{Prefix}_{DocType}_v{N}.md`. Applied by default, not enforced. Deviate and you manage your own file identification. The header is authoritative for identity, doctype, and path; the filename mirrors for human readability.

### Format fits the job

Choose the format that best serves the document's primary consumer and content shape. Markdown for prose-heavy documents. Yaml or json for structured data. Html where appropriate. The declaration header and block model work across formats — this is already settled in the block catalogue rendering rules. Format is a considered choice, not a default.

### Prefix convention

File prefixes identify the subject — typically the area, part, or component name. Recommended and applied by default. A prefix makes a file distinguishable in search results, open-file lists, and folder listings regardless of whether it sits in its own subfolder or flat alongside other files.

### Binder as a doctype

The binder is owned as a doctype definition by Documentation Methodology — its structure as a document, how to read it, what a binder contains. The concept of the binder — why it exists, how it is built, inclusion rules, how it delivers content to the platform — is owned by Working Practices / Content Delivery.

## Confirmed items — design pass 2026-09-11

### Carries received and absorbed

All carries to DocMeth from other component passes have been absorbed into the design document (DocumentationMethodology_Design@v2):

- **The split test** (from Project Design) — when to externalise a block into its own document. Placed as a grammar rule.
- **The ownership-designation rule** (from Project Design) — defining any doctype or block type must name its owner and residence. Placed as a grammar rule.
- **The binder doctype definition** (from Project Design) — what a binder file is, how a consumer reads it, what the manifest means. Placed as a definition in the design.
- **The Contents/Summary edge** (from Standards) — their roles must stay distinct. Placed as a grammar rule.
- **Block-type recognition** (from Core shaping) — two-part test and HTML-comment marker placement. Placed as a definition.
- **Identity and versioning** (from Core shaping) — name + @version, path. Placed as a definition.

### Common block catalogue confirmed

Seven blocks in the common catalogue: Declaration, Dependencies, Header, Footer, Contents, Summary, Version note. Tags stays out (Core-owned). References stays parked (no consumer).

### Rendering model confirmed

DocMeth owns the rendering model end to end — the format rendering rule, the density axis, the portability flag, and which formats the system supports. No explicit mapping tables at this stage — each format's own standards provide unambiguous defaults. No Infrastructure link for rendering unless a utility demonstrates the need.

### Language rules confirmed

Four language rules placed in DocMeth as grammar: plain English, meaning first / code second, use existing terms, flag new terms. Carried from the design-approach work. The aide-design-check skill consumes these; DocMeth's standard is their proper home.

### Declaration as activation trigger

The Declaration's presence is the trigger that causes DocMeth's grammar, standards, and behaviours to apply. A document with a Declaration is a governed document. Added to the model as the fifth concern (activation).

### Contents and Summary optionality

Both blocks are optional. They earn their place by function — Contents when a reader couldn't decide from the Declaration alone whether to keep reading, Summary when the document's substance needs a compressed statement. Often not relevant for machine-focused or skill-delivered documents. The doctype owner sets the default for their type.

## Old-material pass — 2026-09-11

Legacy binder (DocumentationMethodology_Binder_v9, five documents) reviewed against the new design. Two items earned their place:

- **Lifecycle states** (Current, Superseded, Archived) — semantic states independent of physical storage, common across all documents. Added to the design as a definition, placed alongside identity and versioning.
- **The claimed-versus-verified rule** — do not compose plausible metadata where the fact should be observed or read. Added to the design as a fifth language/integrity rule.

One item noted for awareness, no action taken:

- **Assets and Unmanaged files** — the legacy binder defined categories for files outside governed behaviour. The three-tier file model handles the inclusion question. Revisit only if a utility or tool demonstrates the need for a formal distinction.

Everything else in the legacy binder either already exists in the new design, belongs to another component (Working Practices, Project Design, Build, Migration), or was cut/parked during the rebuild.

## Open items

- **DocMeth standard** — blocked on Standards component (now complete). Can be authored.

---

Version note: v2 — updated with design-pass confirmations and old-material pass results, 2026-09-11.
