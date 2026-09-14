> identity: Core_Schema_Standard@v1 | doctype: standard | updated: 2026-09-12 | uses: DocumentationMethodology_Schema_Standard@v4

# Core — Schema Standard

The doctypes and block types defined by Core, using the Documentation Methodology definition contract.

## What this standard is for

Information. This standard defines Core's types. These definitions are provisional pending Core's design pass.

## Doctypes

### Index

- **Purpose:** The identity, entry point, and root source for a component or topic. Carries folder metadata, the component name, role, aliases, document listing, and parts declaration. One per scope.
- **Format constraint:** markdown.
- **Format conventions:** the filename is `_index.md`. The leading underscore sorts it to the top of a directory listing.

Information. The index document's content and structural role are defined in the Core component once that design pass is complete. This definition is provisional.

## Block types

### Tags

- **Purpose:** Classification labels for a governed document.
- **Placement:** footer.
- **Fields:**
  - tags (optional) — a flat list of classification labels.

Deferred under the demonstrated-requirement rule (D21). Defined so the concept is not lost. Returns when a consumer demonstrates need.

---

Version note: v1 — initial schema standard. Provisional pending Core's design pass. 2026-09-12.
