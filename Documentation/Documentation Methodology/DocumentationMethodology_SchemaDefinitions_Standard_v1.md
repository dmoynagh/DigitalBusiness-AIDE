> identity: DocumentationMethodology_SchemaDefinitions_Standard@v1 | doctype: standard | updated: 2026-09-14 | uses: DocumentationMethodology_SchemaAuthoring_Standard@v1

# Documentation Methodology — Schema Definitions Standard

The blocktypes and doctypes defined by Documentation Methodology.

Component-specific types are defined by their owning component. This standard defines only the common types that DocMeth provides to all governed documents.

## Dependency propagation

Documents using these types should add `DocumentationMethodology_SchemaDefinitions_Standard@v1` to their `uses` field.

---

## Common blocktypes

### Declaration

- **Purpose:** Identity and activation block. Its presence makes a document governed.
- **Content:** Labelled fields — identity (required), doctype (optional), blocks (optional), updated (optional), uses (optional). Renders as a blockquote with pipe-delimited fields in markdown.
- **Placement:** first block, fixed topmost.

### Title

- **Purpose:** The document's human-readable name.
- **Content:** A single heading. In markdown, the `#` heading.
- **Placement:** immediately after Declaration.
- **Recognition:** by placement.

### Description

- **Purpose:** What the document is, in a line.
- **Content:** A single paragraph.
- **Placement:** immediately after Title.
- **Recognition:** by placement.

### Body

- **Purpose:** The document's substance. Default host for content not placed elsewhere.
- **Placement:** between the header elements and the footer.

### Footer

- **Purpose:** Metadata and low-priority content at the bottom of the document.
- **Content:** In markdown, a horizontal rule marks the footer boundary. Content below the rule is footer content.
- **Placement:** bottom of document.
- **Recognition:** by placement — everything after the boundary signal.

### Contents

- **Purpose:** A curated map letting a reader decide whether to read the document and what it covers. Navigation, not substance.
- **Content:** Compact, rendered inline — never a vertical list.
- **Placement:** after Description, before Summary.
- **Recognition:** by subheading.
- **Instructions:** (Recommended) Earns its place when the Declaration alone is not enough for a reader to decide whether to keep reading. The doctype owner sets the default. Contents maps what is where; Summary gives what the document establishes — keep these roles distinct.

### Summary

- **Purpose:** States what the document establishes, absorbed quickly. The substance, not a gesture at it.
- **Content:** Stated, not explained — expansion is the body's role. The body does not restate what Summary states.
- **Placement:** after Contents (or after Description if no Contents).
- **Recognition:** by subheading.
- **Instructions:** (Recommended) Earns its place when the document's substance needs a compressed statement. The doctype owner governs whether Summary is used.

### Version note

- **Purpose:** Current version metadata. One line, current version only.
- **Content:** A single compact line. Historical version notes do not accumulate.
- **Placement:** footer, topmost.
- **Recognition:** by placement — top of footer.

### Manifest

- **Purpose:** Records relative paths and structural metadata for every document included in a binder.
- **Content:** Entries as a markdown table with columns for path and document identity.
- **Placement:** body, topmost.
- **Recognition:** by placement — first content block in the binder body.

---

## Common doctypes

### Binder

- **Purpose:** Assembles governed documents into a single file for delivery to the AI platform.
- **Content:** Contents (required), Manifest (required). Source documents are concatenated after the manifest, each delimited by `<!-- BEGIN SOURCE: relative/path.md -->` and `<!-- END SOURCE: relative/path.md -->`.
- **Instructions:** Format is markdown. The binder concept, tooling and inclusion rules are owned by Working Practices.

### Guide

- **Purpose:** A human-facing document, the counterpart to the standard. Standard for the machine, guide for the human. Ships with what it explains.
- **Content:** Contents (recommended), Summary (optional), Version note (optional).
- **Instructions:** General-purpose — any component may produce one. Published and versioned like a standard.

---

Version note: v1 — clean-sheet rebuild. Replaces the definitions portion of DocumentationMethodology_Definitions_Standard_v4. Manifest blocktype added. 2026-09-14.
