> identity: Core_Decisions@v1 | doctype: decisions | updated: 2026-09-15

# Core — Decisions

## Summary

Reasoning and resolutions from the Core design pass. Seven decisions covering the structural frame, component renaming, boundary separations, and disposition of working documents.

---

## D1. Three pillars replaced by four roles

The original three pillars (building blocks, workflows, standards) were a useful framing concept during the rebuild but mapped unevenly — Documentation Methodology sat alone in one pillar, six components spread awkwardly across the other two, and components like Migration and Messaging crossed pillar boundaries.

Replaced by four roles (Foundation, Guidance, Work, Delivery) drawn around what a component provides to the system rather than what mechanisms it uses internally. Every component maps without strain. The roles are a conceptual frame for terminology and placement decisions, not a hierarchy — components contribute to roles, they don't belong to them.

The original aim — a conceptual division of component roles and the functionality a component provides — is preserved. The four categories distribute more evenly and produce cleaner placement vocabulary: "is this a guidance concern or a delivery concern?" is a sharper question than "is this a building-block concern?"

## D2. External AI renamed to Orchestration

The component's scope grew beyond external AI during scoping work — it covers build delegation (chat → Claude Code) as well as cross-platform review and collaboration. "External AI" implied only outbound work with other AI platforms. "Orchestration" fits both scopes and aligns with the established industry term for the coordination layer that manages how multiple AI agents, tools, and human checkpoints work together.

Industry alignment confirmed: the term is used consistently for the conductor role — coordinating AI components to work together for complex tasks no single component can handle alone. AIDE's usage is well aligned with this core meaning.

## D3. Orchestration scoped as mechanics, not modes

Orchestration owns the channels, transport, routing, work package structure, verification machinery, and capability profiles — the coordination mechanics. Review, collaboration, research, parallel solutioning, and consultation are work modes that consume orchestration but are not owned by it. They are behaviours owned by their consuming components or by Working Practices.

This follows the same ownership pattern used throughout AIDE: Messaging defines the envelope but doesn't own what's in it; Documentation Methodology defines the grammar but doesn't own the doctypes; Standards defines what a standard is but individual standards live with their consuming component. The separation is a deliberate design choice — the conductor doesn't decide what music to play.

AIDE's separation of mechanics from work modes is arguably cleaner than the industry norm, where orchestration platforms commonly bundle task definitions with coordination mechanics. The separation is a design choice, not a distortion.

## D4. Messaging is format and methodology, not transport

Messaging defines the envelope — format, structure, addressing, acknowledgment conventions. It does not carry anything; it defines what is carried. Messages travel by Orchestration transport (automated) or by copy-paste (manual, always available). The transport is irrelevant to the message format.

This makes Messaging structurally equivalent to Documentation Methodology — a grammar, not plumbing. Foundation becomes three grammars: framework structure (Core), document structure (Documentation Methodology), communication structure (Messaging).

Consequence: Messaging moves from a Delivery role to Foundation.

## D5. Orchestration as a likely umbrella

Noted as a likely umbrella component that will have areas, parts, or sub-components within it. Two scopes already identified (build delegation, cross-platform review) with a shared shape (task creation separate from transport). Not designed further in Core — the umbrella structure is resolved when Orchestration gets its own design pass.

## D6. Tags stays held

No consumer has demonstrated need. The no-consumer-no-rule principle keeps it out of the design. The working document (Core_Tags_Working_v1) remains available if a consumer appears. A considered deferral, not a forgotten item.

## D7. Design Documentation Working swept and retired

Content reviewed against the current design: fork structure superseded, stable triad embodied in individual component designs, "Core Brief v2" open item overtaken by the charter, design projects and areas placed in the Structure design. No surviving content that isn't already placed elsewhere. Core_Working_v1 (three pillars) also retired — superseded by the four roles in D1.

---

Version note: v1 — initial decisions from the Core design pass. 2026-09-15.
