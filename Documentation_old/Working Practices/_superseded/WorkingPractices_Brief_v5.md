# Working Practices — Brief

> **Version 5** (2026-09-01). Clarifies semantic/operational ownership and records deferred
> Project Handoff continuity handling.
>
> Created: 2026-08-31 | Last modified: 2026-09-01

## Purpose

Working Practices defines **how an AI and user practically work together** across chat, documents,
code, repositories, Work-style environments and other AI-assisted surfaces.

## Required model

Working Practices must be:

- cross-cutting and independently deployable;
- complementary to Principles;
- portable across software and non-software work;
- explicit about generated/proposed versus applied/verified state;
- protective of valuable thinking across context/session/platform boundaries; and
- clear that practical containers are not automatically semantic top-level topics.

## Demonstrated practices

- material multi-file output uses a Change Delivery Package;
- cross-project ownership changes use Project Handoff and the destination's current baseline;
- a received Handoff that cannot be reconciled in the same pass is held by one concise destination
  OpenItem until reconciliation completes;
- generated Binders are independently versioned read-only consumption artefacts;
- confirmed output is batched at meaningful checkpoints rather than after every edit;
- **valuable active thinking is checkpointed to WIP when loss of current context would materially
  impair continuation**;
- WIP versioning is used as a visible currency signal when context files are swapped/synced across
  chats/platforms;
- routine low-risk choices are handled autonomously while architecture decisions are surfaced;
- externally held/current facts are checked rather than plausibly invented; and
- material state-changing actions are not silently assumed complete.

## Outcome

```text
AIDE_WorkingPractices@v1
```

---
Dependencies: !AIDE_DocumentationMethodology@v21
References: WorkingPractices_Design_v6, Principles_Design_v3
