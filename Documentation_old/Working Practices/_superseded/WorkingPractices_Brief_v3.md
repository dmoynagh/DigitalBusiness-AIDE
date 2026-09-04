# Working Practices — Brief

> **Version 3** (2026-08-31). Consolidates Project Handoff, repository/Binder conventions and
> checkpoint-based batching of documentation/file output under the clarified Documentation
> Methodology ownership boundary.
>
> Created: 2026-08-31 | Last modified: 2026-08-31

## Purpose

Working Practices defines **how an AI and user practically work together** across chat, document,
code, Work, repository and other AI-assisted surfaces.

It covers cross-cutting conventions that are too operational to be Principles and too general to
belong to one work Domain or output methodology.

## Required model

Working Practices must be:

- a top-level AIDE concern;
- independently deployable;
- complementary to Principles;
- portable across software and non-software work;
- base guidance customisable through small Guidance Profile deltas;
- explicit about the distinction between generated intent and observed/applied state; and
- clear about the boundary between semantic ownership and practical workflow implementation.

## Demonstrated practices

- material multi-file output uses a Change Delivery Package;
- Change Delivery Packages use a defined staging/completion workflow where repository storage is
  available;
- cross-project master changes use the owning project's current Binder/current sources when
  available;
- material knowledge crossing AIDE project ownership boundaries uses a Project Handoff;
- structural/management folders are visually distinguished from substantive content using the
  current `_` prefix convention;
- generated project Binders are independently versioned, read-only consumption artefacts kept with
  the active masters for easy selection/context loading;
- confirmed file/document changes are normally queued and emitted in one consolidated pass at a
  significant work-unit, session or completion checkpoint rather than after every change;
- coded references are glossed on first use;
- externally held/current facts are checked rather than plausibly invented;
- material state-changing actions are not silently assumed complete;
- architecture-shaping choices are surfaced explicitly; and
- complex work proceeds in human-comprehensible layers.

## Outcome

```text
AIDE_WorkingPractices@v1
```

---
Dependencies: !AIDE_DocumentationMethodology@v20
References: WorkingPractices_Design_v4, Principles_Brief_v3
