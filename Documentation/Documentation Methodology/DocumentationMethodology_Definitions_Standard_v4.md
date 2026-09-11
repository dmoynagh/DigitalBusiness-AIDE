# Documentation Methodology — Definitions Standard

> identity: DocumentationMethodology_Definitions_Standard@v4 | doctype: standard | date: 2026-09-12
> uses: DocumentationMethodology_Schema_Standard@v4

The doctypes and block types defined by Documentation Methodology, using its own definition contract.

## What this standard is for

Information. This standard contains DocMeth's own type definitions — the common block catalogue and the common doctypes. Component-specific types are defined by their owning component using the Schema Standard. For the definition grammar itself, see the Schema Standard. For authoring governed documents, see the Authoring Standard.

## Common block types

### Declaration

- **Purpose:** Machine-readable identity and activation block. Its presence makes a document governed.
- **Fields:**
  - identity (required) — name + @version, the authoritative reference
  - doctype (required) — the document's type
  - date (required) — date this version was produced, YYYY-MM-DD
  - uses (optional) — standards this document depends on, flat list with grouping syntax
  - blocks (optional) — non-scaffold typed blocks present in this document, flat list with grouping syntax
- **Density:** compact. Overrides the single-line compact default — renders across multiple lines (one per field group) because some fields are optional and variable-length.
- **Recognition:** by placement — first block, fixed topmost.
- **Placement:** header, topmost.
- **Container:** yes — a container for its labelled fields.

### Title

- **Purpose:** What the document is called. The human-readable name.
- **Recognition:** by placement — immediately after Declaration. In markdown, the `#` heading.
- **Placement:** header, after Declaration.

### Description

- **Purpose:** What the document is, in a line.
- **Recognition:** by placement — first paragraph after Title.
- **Placement:** header, after Title.

### Header

- **Purpose:** Placement container for blocks that serve the read-decision. No semantics of its own.
- **Container:** yes.
- **Placement:** top of document.
- **Conditional behaviour:** boundary proximity principle — value increases toward the file boundary. Header runs high-to-low from the top.

### Body

- **Purpose:** The document's substance. Default host for content not claimed by another container.
- **Container:** yes.
- **Placement:** between header and footer.
- **Recognition:** by placement — the first heading that is not Contents or Summary.

### Footer

- **Purpose:** Placement container for metadata and low-priority blocks. No semantics of its own.
- **Container:** yes.
- **Placement:** bottom of document.
- **Recognition:** by placement — everything after the boundary signal. In markdown, a horizontal rule marks the footer boundary.
- **Conditional behaviour:** boundary proximity principle — footer runs low-to-high toward the end.

### Contents

- **Purpose:** A curated semantic map letting a reader decide whether to read the document and what it covers.
- **Density:** compact (rendered inline / delimited, never a vertical list).
- **Recognition:** by subheading.
- **Placement:** header, after Description, before Summary.
- **Conditional behaviour:** earns its place when the Declaration alone is not enough for a reader to decide whether to keep reading. The doctype owner sets the default (on, off, or conditional) and defines depth.

### Summary

- **Purpose:** States what the document establishes, absorbed quickly. The substance, not a gesture at it.
- **Recognition:** by subheading.
- **Placement:** header, after Contents (or after Description if no Contents).
- **Conditional behaviour:** earns its place when the document's substance needs a compressed statement. Stated, not explained — expansion is the body's role. The body does not restate what the Summary states. The doctype owner governs whether Summary is used.

### Version note

- **Purpose:** Current version metadata. One line, current version only. Historical version notes do not accumulate; the decisions document holds what mattered.
- **Density:** compact.
- **Recognition:** by placement — top of footer.
- **Placement:** footer, topmost (low-value end of the footer gradient).

### Manifest

- **Purpose:** Records relative paths and structural metadata for every document included in a binder.
- **Fields:**
  - entries (required) — list of relative paths preserving structural relationships. Renders as a markdown table with columns for path and document identity.
- **Density:** compact.
- **Recognition:** by placement — first content block in the binder body.
- **Placement:** body, topmost.

## Common doctypes

### Binder

- **Purpose:** Assembles governed documents into a single file for delivery to the AI platform.
- **Included blocktypes:** Contents (required), Manifest (required).
- **Format constraint:** markdown.
- **Format conventions:** source documents are concatenated after the manifest. Each source document is delimited by `<!-- BEGIN SOURCE: relative/path.md -->` before and `<!-- END SOURCE: relative/path.md -->` after, where the path matches the manifest entry.

Information. The binder concept — why it exists, how it is built, inclusion rules — is owned by Working Practices / Content Delivery.

### Guide

- **Purpose:** A human-facing output document, the counterpart to the standard. Standard for the machine, guide for the human. Ships with what it explains.
- **Included blocktypes:** Contents (recommended), Summary (optional), Version note (optional).

Information. General-purpose — any component may produce one. Published and versioned like a standard. Distinct from the design doctype: design is development-time reasoning, guide is use-time explanation.

## Parked

**Tags** — Core owns the definition. Returns to the common catalogue only if DocMeth grammar needs to know about it specifically.

**References** — no consumer has appeared. Decide on its own merits when one does.

---

Version note: v4 — round 3 corrections. Manifest moved to common blocks. Binder BEGIN/END syntax defined. Manifest table rendering defined. Format conventions property used. 2026-09-12. Replaces v3.
