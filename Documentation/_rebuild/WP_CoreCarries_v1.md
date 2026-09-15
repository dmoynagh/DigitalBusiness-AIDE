# Carries to Core from the Working Practices design pass

Working document. Items confirmed during the WP design pass that require updates to Core documents. To be applied at next Core update or via FUP.

---

## Framework-wide requirements (additions to Core_Design)

### Definition of done

Every component, every piece of work, defines when it is done. The invariant: the completion bar must be testable or assessable. Core states the requirement; WP owns the block type definition (the mechanism consumers use); consumers fill it with their own content.

Source: settled WIP v22 (promoted from WP generic block to framework-wide requirement during WP design pass, D4).

### Assurance

Every component contributes to assurance — the justified confidence that the human's intent is reliably delivered and that anomalies, drift, errors, and misunderstandings are visible when they occur. The Assurance component owns the specific conventions and detection mechanisms; this requirement is the lens every component is designed through.

Source: WP design pass, D16.

## Ownership rules (addition to Core_Design)

### P6 — information holder decides the boundary

When a boundary question arises, the component that holds the information decides. This is a framework governance rule governing how components relate to each other — a sixth ownership rule alongside the existing five.

Source: moved from Principles to WP during the Principles design pass; moved from WP to Core during the WP design pass, D5.

## Component map updates

### New component: Assurance

| Component | Purpose | Key boundaries |
|---|---|---|
| Assurance | Build justified trust in AI-assisted work by defining and evolving the conventions, structures, and detection mechanisms that ensure the human's intent is reliably delivered and that anomalies, drift, errors, and misunderstandings are visible when they occur. | Guidance role. Cross-cutting — every component contributes. Owns the human working model, verification behaviours, drift detection, anomalies channel. Does not own the substrate (WP) or the premises (Principles). |

Placed in the Guidance role alongside Principles, Standards, and Tools.

Component count: 13 → 14.

---

Version note: v1 — carries from the WP design pass. 2026-09-15.
