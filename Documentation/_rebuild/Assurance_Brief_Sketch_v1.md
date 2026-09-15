# Assurance — Brief (sketch)

This is a sketch produced during the Working Practices design pass to hold the confirmed identity and scope of the Assurance component until its own design pass. It is not a full brief — purpose and content are confirmed; objectives and definition of done await the design pass.

---

## Purpose

Build justified trust in AI-assisted work by defining and evolving the conventions, structures, and detection mechanisms that ensure the human's intent is reliably delivered and that anomalies, drift, errors, and misunderstandings are visible when they occur.

## Role

Guidance. Sits alongside Principles, Standards, and Tools. Provides the trust and outcome conventions.

## Cross-cutting nature

Assurance is both a component and a framework-wide requirement. Every element in the framework contributes to assurance — the brief-required gate, cross-review, operations test, acceptance test, strength model, capture-and-place, the design-check skill, definition of done, Principles P7/P8/P10 all contribute. The component owns its specific mechanisms; the framework-wide requirement is the lens every component is designed through.

## Content (moved from WP's Human-AI Collaboration area)

**Proactive conventions** — help the AI deliver correctly in the first place:
- Human working model (tiering, confidence signalling, assumptions/gap-fill report)
- Overview-first discipline (consumed from WP's generic statement)

**Detective conventions** — help the human see when something has gone wrong:
- Verification behaviours (verify inspectable facts, distinguish generated intent from applied state — consuming Principles P7 and P10)
- Drift detection (recognising when work moves away from the agreed model — consuming P8)
- Anomalies channel (surfacing things that don't fit — behaviour with capture-and-place as destination)

**Evolution path** — new failure modes discovered in practice become new conventions or detection behaviours. The area is a living system, not a fixed specification.

## Key boundaries

- Assurance defines what to watch for and how to signal it
- WP defines how work is conducted (the substrate Assurance runs on)
- Principles provides the reasoning premises both consume
- Cross-review is likely an Orchestration concern that Assurance defines the criteria for

## Confirmed design decisions

- Named tiers for autonomy levels, small number, chosen by either side. AI judges default; human overrides
- Anomalies channel is a behaviour with capture-and-place as destination, not a separate mechanism
- Confidence vocabulary uses the framework's existing strength model (strong/moderate/etc.), not a new system
- These three decisions require review when the full design brief is produced

## Charter alignment

Directly delivers O1 (trust and integrity) — the framework's primary reason for existing.
Contributes to O4 (extensibility from learning) — conventions evolve as collaboration learns.

---

Version note: v1 — sketch from the WP design pass. To be replaced by a full brief when the Assurance design pass begins. 2026-09-15.
