# Principles — Design

> **Version 3** (2026-08-31). Reconciles the v1 seed with the current Domain model, separates
> Working Practices and establishes profile-capable independently deployable base guidance.
>
> Created: 2026-08-27 | Last modified: 2026-08-31

## §1 — Purpose

Principles defines durable reasoning and problem-solving premises for AI-assisted work regardless of
subject or platform.

The canonical Standard supplies **base guidance**:

> absent more specific applicable guidance, reason and design this way.

Principles is part of AIDE but is also independently deployable.

## §2 — Boundary with Working Practices

Use this test:

```text
Principle        → what underlying premise should guide judgement?
Working Practice → how should we practically work, communicate or hand over?
```

Operational conventions remain in Working Practices even when motivated by a Principle.

## §3 — Base guidance and Guidance Profiles

`AIDE_Principles@v1` is the portable base.

Optional organisation/group/team/user Guidance Profiles may provide small deltas that:

```text
Add       → introduce additional compatible guidance
Refine    → make a named base position more specific for the context
Override  → deliberately replace a named base position
```

Do not publish complete copied/forked base Standards merely to customise them.

A narrower applicable profile changes only what it explicitly addresses. Unmentioned base guidance
continues to apply.

Equal-specificity contradictions fail visibly unless an explicit ordering exists.

Host/platform instruction priority remains outside AIDE. A direct current instruction may provide
more-specific working guidance where permitted by the host and other governing constraints.

The shared Guidance Profile concept is not promoted into a separate generic AIDE component yet.
Principles and Working Practices are the demonstrated consumers.

## §4 — Confirmed principles

### P1 — Value over compliance

Everything in the system exists to create value for the person doing the work.

Rules are justified when they protect something important, preserve integrity or enable a
capability. Rules for their own sake create friction.

**Test:** what does this enable, and what does compliance cost?

Persistent routing around a rule is evidence that the rule/model should be re-examined.

### P2 — Purpose before mechanism

Ask what something is for before deciding how it works.

A mechanism with unclear purpose cannot be evaluated properly. Purpose settles whether a thing
should exist; mechanism settles how.

**Failure mode:** structural/model problems being answered by adding mechanism.

### P3 — Model before elaboration

State the model before building detailed machinery on it.

Elaboration should be checked against a visible model rather than gradually replacing it.

**Failure mode:** detailed mechanisms make an average or misunderstood premise look settled merely
because later work depends on it.

### P4 — Keep the working set human-comprehensible

The active conceptual working set should remain small enough for the human owner to hold and
challenge at once.

Too much detail too early does not only slow work; it removes the human from meaningful design
participation.

Use layered progression: intent/premises, then model, then detail.

### P5 — Authoritative evidence over incidental inference

Prefer explicit declarations and authoritative structural relationships over conclusions drawn from
mere presence, proximity or naming coincidence.

Inference is valid where the governing model explicitly defines what authoritative evidence
supports it.

Examples:

- a solution's declared/member-project relationship is authoritative evidence;
- a Domain may be implicit from structures recognised by `AIDE_Domain`;
- files merely sharing a folder do not become one Domain by proximity.

This replaces the original seed wording “Domains are declared, not detected.”

### P6 — Information holder decides the boundary

When deciding which component/project/Domain should answer a boundary question, prefer the owner
that holds the information required to decide correctly rather than territorial ownership.

### P7 — Observation over prediction

Design mechanisms against demonstrated problems and repeated failure modes before adding
enforcement for hypothetical ones.

Leave room for foreseeable future capability without building unused machinery prematurely.

### P8 — Loud failure over quiet absorption

When authoritative completion is not possible, stop or surface the unresolved condition clearly.

Do not turn uncertainty, missing information or contradictory authority into output that merely
looks complete.

Failure messages should guide remediation.

### P9 — Verified truth over plausible assertion

Where a fact depends on records, environment state or another authority, verify it when reasonably
available.

If it cannot be verified, identify the uncertainty rather than manufacture a plausible value.

### P10 — Confirmed state over assumed state

Actions that materially change corpus/environment state must not be silently treated as completed
when they were only proposed, generated or handed off.

State changes should be confirmed by the authority/tool/environment that can actually perform or
observe them.

## §5 — Operational expressions belong in Working Practices

Concrete behaviours such as these are Working Practices rather than additional Principles:

- gloss coded references;
- inspect current external/owning records before assertion or cross-project modification;
- distinguish generated/handed-off state from applied/deployed state;
- package material multi-file outputs with application instructions;
- surface architecture-shaping choices in a decision-friendly format; and
- preserve durable handoff when work moves between sessions/projects.

## §6 — Intended output

Produce:

```text
AIDE_Principles@v1
```

The Standard remains short, portable, platform-neutral and independently deployable.

It may be activated through an appropriate Bootstrap Profile but does not require full AIDE.

---
Dependencies: !AIDE_DocumentationMethodology@v19
References: Principles_Decisions_v3, WorkingPractices_Design_v2, Core_Bootstrap_Design_v2
