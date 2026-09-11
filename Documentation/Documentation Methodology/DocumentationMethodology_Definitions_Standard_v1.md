Documentation Methodology — Definitions Standard | standard | DocumentationMethodology_Definitions_Standard@v1 | 2026-09-11

The doctypes and block types defined by Documentation Methodology, using its own definition contract.

## What this standard is for

Information. This standard contains DocMeth's own type definitions — the common block catalogue and the common doctypes. Component-specific types are defined by their owning component using the Schema Standard. For the definition grammar itself, see the Schema Standard. For authoring governed documents, see the Authoring Standard.

## Common block types

### Declaration

- **Purpose:** The machine-readable identity and activation block for a governed document. Its presence makes a document governed.
- **Fields:** identity (name + @version), doctype, date, dependencies (flat list with grouping syntax), blocktypes (flat list with grouping syntax).
- **Density:** compact.
- **Recognition:** by placement — first block, fixed position.
- **Placement:** header, topmost.
- **Container:** yes — dependencies and blocktypes place within it.

### Title

- **Purpose:** What the document is called. The human-readable name.
- **Recognition:** by placement — at the top of the document, above the Declaration in markdown.
- **Placement:** header, above Declaration.

### Description

- **Purpose:** What the document is, in a line.
- **Recognition:** by placement — text beneath the title.
- **Placement:** header, between title and Declaration.

### Header

- **Purpose:** Placement container for blocks that serve the read-decision. No semantics of its own.
- **Container:** yes.
- **Placement:** top of document.
- **Conditional behaviour:** boundary proximity principle — value increases toward the file boundary. Header runs high-to-low from the top.

### Footer

- **Purpose:** Placement container for metadata and low-priority blocks. No semantics of its own.
- **Container:** yes.
- **Placement:** bottom of document.
- **Recognition:** by marker — in markdown, a horizontal rule marks the footer start.
- **Conditional behaviour:** boundary proximity principle — footer runs low-to-high toward the end. Most important content closest to file end.

### Body

- **Purpose:** The document's substance. Every governed document has a body.
- **Container:** yes — default host for content not claimed by another block.
- **Placement:** between header and footer.
- **Recognition:** by placement — the first heading that is not Contents or Summary.

### Dependencies

- **Purpose:** Which standards this document depends on and at which version it was last brought into line.
- **Fields:** a flat list of `standard@version` pairs with optional grouping for ownership tracking.
- **Density:** compact.
- **Recognition:** by field label within the Declaration blockquote.
- **Placement:** Declaration (rendered within the Declaration blockquote).
- **Dependency implications:** this block is defined in the Documentation Methodology Definitions Standard.

### Contents

- **Purpose:** A curated semantic map letting a reader decide whether to read the document and what it covers.
- **Density:** compact (rendered inline / delimited, never a vertical list).
- **Recognition:** by subheading.
- **Placement:** header, after Declaration, before Summary.
- **Conditional behaviour:** earns its place when the Declaration alone is not enough for a reader to decide whether to keep reading. The doctype owner sets the default (on, off, or conditional) and defines depth.

### Summary

- **Purpose:** States what the document establishes, absorbed quickly. The substance, not a gesture at it.
- **Recognition:** by subheading.
- **Placement:** header, after Contents (or after Declaration if no Contents).
- **Conditional behaviour:** earns its place when the document's substance needs a compressed statement. Stated, not explained — expansion is the body's role. The body does not restate what the Summary states. The doctype owner governs whether Summary is used.

### Version note

- **Purpose:** Current version metadata. One line, current version only. Historical version notes do not accumulate; the decisions document holds what mattered.
- **Density:** compact.
- **Recognition:** by placement — top of footer.
- **Placement:** footer, topmost (low-value end of the footer gradient).

## Common doctypes

### Binder

- **Purpose:** Assembles governed documents into a single file for delivery to the AI platform.
- **Included blocktypes:** Declaration (required), a manifest recording relative paths for every included document, source documents concatenated with BEGIN/END markers.
- **Format constraint:** markdown.

Information. The binder concept — why it exists, how it is built, inclusion rules — is owned by Working Practices / Content Delivery. This definition covers the binder as a document: its structure and how a consumer reads it.

### Guide

- **Purpose:** A human-facing output document, the counterpart to the standard. Standard for the machine, guide for the human. Ships with what it explains.
- **Included blocktypes:** Declaration (required), Title (required), Description (recommended), Contents (recommended), Summary (optional), Body (required), Version note (optional).
- **Dependency implications:** DocumentationMethodology_Definitions_Standard.

Information. General-purpose — any component may produce one. Published and versioned like a standard. Distinct from the design doctype: design is development-time reasoning, guide is use-time explanation.

## Parked

**Tags** — Core owns the definition. Returns to the common catalogue only if DocMeth grammar needs to know about it specifically.

**References** — no consumer has appeared. Decide on its own merits when one does.

---

Version note: v1 — split from DocumentationMethodology_Standard@v1. Type definitions expressed using the definition contract from the Schema Standard. Title and Description added as common blocks. Guide added as common doctype. 2026-09-11.
