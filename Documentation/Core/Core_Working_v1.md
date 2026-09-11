Core | working | Core_Working@v1 | 2026-09-10

## Three pillars (confirmed 2026-09-09)

AIDE's components organise around three pillars — three kinds of thing that together make the framework work:

- **Building blocks** — the structural primitives. How documents are shaped (doctypes, block types, the declaration), how they identify themselves (identity, versioning), how they are organised (folders, paths, the AIDE document). Documentation Methodology owns this pillar.

- **Workflows** — the behavioural patterns. How a person works with AI across sessions and surfaces: the development lifecycle, capture-and-place, handoffs, work management, file operations. Working Practices owns this pillar, with Project Design and Build owning the design-and-build path within it.

- **Standards** — the guidance layer. Rules, expectations, and context that shape decisions and behaviour while work is being done. The Standards component owns what a standard is and how one is authored; individual standards are owned by the component that knows the most about their subject.

The overview sits in Core because it is a framework-level concept — it describes how AIDE's parts relate to each other. The individual pillars are owned by their respective components.

This is a framing concept, not a hierarchy. Components do not belong to pillars; they contribute to them. A component like Migration contributes to both workflows (how change actions are executed) and standards (what a migration record looks like).

---

Version note: v1 — initial working document from session 2026-09-09.
