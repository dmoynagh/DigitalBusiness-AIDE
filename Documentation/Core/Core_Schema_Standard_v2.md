> identity: Core_Schema_Standard@v2 | doctype: standard | updated: 2026-09-14 | uses: DocumentationMethodology_SchemaAuthoring_Standard@v1

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

---

Version note: v2 — Tags block type removed (no operational consumer; concept retained in Core_Tags_Working_v1). `uses` updated to DocumentationMethodology_SchemaAuthoring_Standard@v1. 2026-09-14. Replaces v1.
