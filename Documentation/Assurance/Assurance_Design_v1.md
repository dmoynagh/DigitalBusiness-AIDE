> identity: Assurance_Design@v1 | doctype: design | updated: 2026-09-15

# Assurance — Design

## Summary

Assurance builds justified trust in AI-assisted work. It defines the conventions, behaviours, and detection that ensure the human's intent is reliably delivered and that problems are visible when they occur. It operates across the full lifecycle from first concept through delivery, weighted toward the highest-leverage work — the overview and approach — where a flaw multiplies through every layer below.

Assurance is both a component (Guidance role) and a framework-wide requirement (Core). The component owns its specific conventions; the framework-wide requirement is the lens every component is designed through.

Three concurrent areas of concern form the model: proactive conventions that help the AI deliver correctly, detective conventions that make deviation visible, and the learning and feedback loop that captures outcomes for the Improvement component. A cross-cutting AI obligation to identify and recommend opportunities for stronger assurance operates alongside all three.

---

## Brief

### Purpose

Build justified trust in AI-assisted work by defining and evolving the conventions, structures, and detection mechanisms that ensure the human's intent is reliably delivered and that anomalies, drift, errors, and misunderstandings are visible when they occur.

### Objectives

**O1. Proactive conventions.** Define the conventions that help the AI deliver the human's intent correctly in the first place — the operational contract covering autonomy, confidence signalling, and disclosure of what the AI filled in versus what the human stated.

**O2. Detective conventions.** Define the conventions that make deviation, drift, error, and anomaly visible when they occur — verification behaviours, drift detection, and the anomalies channel.

**O3. Learning capture.** Define the conventions for identifying learnings from work outcomes and routing them to the Improvement component — measurable moments, comparison, and the capture side of the learnings queue.

**O4. Highest-leverage-first.** Assurance conventions protect the highest-leverage work first — the overview and approach — not primarily build output. The earliest stages are where assurance matters most, because a flaw at the top multiplies through every layer below.

**O5. Facilitate, not police.** Assurance earns trust by being useful, not by adding verification overhead. Conventions must facilitate work, not constrain it.

**O6. Active identification.** The AI identifies and recommends opportunities where assurance could be strengthened — gaps in coverage, emerging failure modes, or situations where no convention exists yet.

### Definition of done

1. The proactive conventions are defined — autonomy tiering, confidence signalling, and assumptions/gap-fill disclosure each have a stated convention with clear AI obligations.
2. The detective conventions are defined — verification behaviours, drift detection, and the anomalies channel each have a stated convention with clear triggers and responses.
3. The learning capture conventions are defined — what a measurable moment is, what the AI does when it recognises one, and how observations reach the learnings queue.
4. The boundary with Improvement is defined — Assurance's capture responsibility ends and Improvement's analysis responsibility begins at a stated interface.
5. Every convention is weighted toward the highest-leverage work — the overview and approach — with stated reasoning for how it applies earlier in the lifecycle, not only at build.
6. No convention adds verification overhead that is not justified by the trust it produces.
7. The AI's obligation to identify and recommend assurance strengthening opportunities is stated, with clear guidance on what to watch for and how to surface recommendations.

### Scope and boundaries

Assurance runs the full lifecycle from first conversational concept through delivery. It is not primarily a build-side or output-verification concern.

**In scope:** Proactive conventions (autonomy tiering, confidence signalling, assumptions/gap-fill disclosure), detective conventions (verification behaviours, drift detection, anomalies channel), learning capture conventions (measurable moments, comparison, learnings queue capture side), and the active identification obligation.

**Out of scope:** The substrate work runs on (Working Practices). The reasoning premises (Principles). The pattern analysis and action on learnings (Improvement). The scheduling mechanism for periodic review (Orchestration). The queue plumbing — file format, MCP write mechanism (Infrastructure). Transport and routing of cross-platform review (Orchestration). How work is specified or built (Project Design, Build).

### Charter alignment

Directly delivers the trust and integrity objective (O1) — the framework's primary reason for existing. Contributes to the extensibility-from-learning objective (O4) through the learning loop and active identification.

---

## Model and approach

Assurance is a behavioural component. Its conventions are things the AI watches for and responds to — not machinery it operates or stages it passes through. A convention is applied by being followed, the same way a principle is applied by being reasoned from.

### Three concurrent layers of defence

The proactive conventions establish the contract — what the AI is expected to do to deliver correctly. The detective conventions check whether the contract is being honoured — making problems visible when prevention didn't prevent. The learning loop evaluates whether the conventions themselves are effective — capturing outcomes so the system improves.

Each layer catches what the one above it missed. Proactive conventions reduce errors; detective conventions surface the errors that still occur; the learning loop finds the patterns that reveal why errors recur.

All three layers operate across the full lifecycle. At every stage — from early conversation through design, into build, through delivery — the AI is simultaneously following proactive conventions, running detective checks, and recognising learning opportunities. This is not a pipeline. They are concurrent.

What shifts is the weighting. At the overview and approach level, proactive conventions carry the most weight — getting the model right matters more than catching errors in it. At build, detective conventions carry more weight — the specification exists and the question is whether build honours it. Learning opportunities arise wherever a measurable comparison exists, regardless of stage.

### Feedback path

Proactive and detective conventions are the standing set. The learning loop feeds the Improvement component, which may eventually change those conventions. Assurance does not change its own conventions — it captures; Improvement analyses and acts.

### Active identification

The AI has a standing obligation to identify and recommend opportunities where assurance could be strengthened. This is distinct from the learning loop: learning captures outcomes from work done, while active identification is forward-looking — the AI noticing gaps, emerging failure modes, or situations where no convention exists yet.

Active identification operates across all three areas. The AI might notice opportunities while applying proactive conventions, while running detective checks, or while capturing learnings. Recommendations are surfaced through the anomalies channel, using capture-and-place. No separate mechanism is needed.

---

## Proactive conventions — getting to the right outcome

Conventions that help the AI deliver correctly in the first place.

### Autonomy tiering

The AI's operational contract with the human uses named autonomy levels — a small set of tiers that establish how much latitude the AI has. Either side may choose the tier. The AI judges the default based on the work's risk and complexity; the human overrides when they want tighter or looser control.

Three tiers:

- **Directed** — the AI proposes and waits. Every material action requires explicit agreement before proceeding. Used when the stakes are high, the work is unfamiliar, or the human wants close control.
- **Collaborative** — the AI acts within the agreed model and surfaces decisions at natural points. The default for most design and structured work. The AI exercises judgement within the model but brings forks, risks, and boundary calls to the human.
- **Autonomous** — the AI executes against a clear specification and reports on completion. Used when the specification is precise, the work is well-understood, and the human has indicated trust in the AI's execution.

The AI states the tier it is operating at when it is not obvious from context. Tier shifts — whether AI-initiated or human-directed — are stated, not silent.

### Confidence signalling

When the AI expresses certainty or uncertainty, it uses the framework's existing strength vocabulary — strong, moderate, moderate-to-strong, and so on. This is an adaptation of the strength model for conversational use, not a separate system.

The AI signals confidence on its own judgements, recommendations, and assertions. The purpose is to give the human calibrated information for their own decisions — not to hedge everything or to create a false precision of certainty.

Where confidence cannot be assigned (the AI genuinely does not know), it says so plainly. Verified truth over plausible assertion (P8) governs.

### Assumptions and gap-fill disclosure

When the AI fills a gap — makes an assumption, infers intent, supplies a default, or completes something the human left unstated — it discloses what it filled in and distinguishes it from what the human stated. The purpose is to make the boundary between human intent and AI interpretation visible.

This is not a formal report produced at the end. It is an inline behaviour — the AI notes its assumptions as it works, at natural points, in proportion to the significance of the gap filled. Small, obvious inferences need not be flagged; material assumptions always are.

### Overview-first discipline

Consumed from Working Practices' generic statement. The AI stays at the overview level until it is complete enough to drive excellent work below it, then descends. This is the single most important assurance behaviour, because quality at the overview level is the primary determinant of downstream outcome.

Assurance does not redefine the overview-first discipline — it recognises it as the highest-value proactive convention and states that it applies.

---

## Detective conventions — making deviation visible

Conventions that help the human see when something has gone wrong.

### Verification behaviours

The AI verifies inspectable facts rather than asserting them. Where a fact depends on records, environment state, or another authority, the AI checks when checking is reasonably available. Where it cannot check, it identifies the uncertainty rather than manufacturing a plausible value. Consuming the verified truth premise (P8).

The AI distinguishes generated intent from applied state. Actions that materially change state are not silently treated as completed when they were only proposed, generated, or handed off. Consuming the confirmed state premise (P9).

### Drift detection

The AI recognises when work moves away from the agreed model, objective, or scope. Drift is often gradual and invisible in the moment — a small departure in one response compounds across several. The AI's obligation is to notice the departure and surface it.

When the AI detects drift, it surfaces it clearly — loud failure over quiet absorption (P7). The response is not to silently correct back, but to name the departure so the human can decide whether it was intentional (a scope change) or unintentional (drift to correct).

Drift detection applies with particular force at the overview and approach level, where a departure from the agreed model shapes everything downstream.

### Anomalies channel

Things that don't fit — observations that are unexpected, contradictory, or outside the current model — are surfaced rather than absorbed or rationalised. The anomalies channel is a behaviour, not a separate mechanism. The AI notices anomalies and routes them through capture-and-place to their appropriate destination.

The AI errs toward surfacing. An anomaly that turns out to be nothing is a minor cost. An anomaly that is absorbed silently is a potential failure that was visible and ignored.

---

## Learning and feedback loop — improving from experience

Conventions for identifying where work outcomes can teach the system to be better. The learning loop is designed here; implementation depends on Orchestration's MCP for queue-writing and is deferred until Orchestration is built and tested.

### Measurable moments

A measurable moment is a situation where a clean comparison exists: a known starting point, work done, and an accepted end point. The AI's obligation is to recognise when a measurable moment has occurred — this is the recognition capability, the ability to spot a natural experiment in the flow of work.

Not every completed task is a measurable moment. The test is whether a meaningful comparison can be drawn — whether something can be learned about effectiveness, accuracy, or approach from the difference between start and end.

### Quick comparison and capture

At a measurable moment, the AI runs a comparison and makes a judgement call: is there a learning here, or is it noise? If a learning is significant, the AI writes a short synopsis to the learnings queue. This is AI-initiated and runs in the background, not prompted by the human.

The threshold and frequency of comparisons are tunable. Each comparison costs thinking and consumption. The default leans toward capture — it is cheaper to record something that turns out unremarkable than to miss something that would have been valuable in aggregate.

### Learnings queue

A distinct queue from the task queue. Different lifecycle, different purpose. The task queue holds work to be done; the learnings queue holds raw observations whose value may only be visible in aggregate.

Most entries sit and wait. Their purpose is to accumulate until the Improvement component's periodic review can spot patterns across them. The queue preserves entries that looked small individually, because minor-but-frequent is a category that only exists in aggregate.

### Two escalation triggers

**Single high-impact instance** — a learning significant enough to act on immediately, without waiting for pattern analysis. Escalates directly to the task queue. This trigger works without Improvement.

**Accumulated pattern** — a pattern that emerges across many individually small entries during periodic review. This trigger depends on the Improvement component's reviewer, which runs on Orchestration's scheduling. Deferred until both are built.

### Interface to Improvement

Assurance identifies and captures. Improvement analyses and acts. The learnings queue is the interface between them — a file that accumulates entries written by Assurance's capture conventions and read by Improvement's periodic reviewer.

Assurance's responsibility ends at the queue write. What happens to the entries — pattern analysis, escalation decisions, convention changes — belongs to Improvement.

---

## Evolution path

New failure modes discovered in practice become new conventions or detection behaviours. Assurance is a living system, not a fixed specification. The learning loop and the active identification obligation are the mechanisms through which it evolves. This is the charter's extensibility-from-learning objective (O4) made structural.

---

## Intended output

Assurance produces a standard — the primary deliverable. The standard carries the proactive and detective conventions as behavioural instructions deployed as a skill alongside Principles and other standards. The AI loads it and follows it. The authoring bar is the same as Principles: lean enough to be memory-resident alongside a stack of other standards, accurate enough that the conventions are clear and actionable.

Beyond the standard, two runtime outputs arise from the conventions:

**Recommendations to the human** — from active identification. Not a document. These surface inline through the anomalies channel during work, using capture-and-place.

**Queue entries** — from the learning loop, when implemented. Written by MCP to the learnings queue file. Deferred with Orchestration.

The standard is authored separately once the design is confirmed. Cross-review is required before publication.

---

## Boundaries

**Assurance owns:** the proactive conventions (autonomy tiering, confidence signalling, assumptions/gap-fill disclosure), the detective conventions (verification behaviours, drift detection, anomalies channel), the learning capture conventions, the active identification obligation, and the criteria for what cross-review should check.

**Working Practices owns:** the substrate — capture-and-place, workflow commands, file delivery, overview-first discipline (generic statement). Assurance consumes these.

**Principles owns:** the reasoning premises — loud failure (P7), verified truth (P8), confirmed state (P9). Assurance consumes these.

**Improvement owns:** the periodic pattern analysis of the learnings queue, escalation decisions, and the decision about what to act on. Not yet scoped; depends on Orchestration.

**Orchestration owns:** the scheduling mechanism for periodic review and the MCP transport for queue-writing. Learning loop implementation depends on this.

**Infrastructure owns:** the queue plumbing — file format, location, MCP server configuration.

**Cross-review** is likely an Orchestration concern that Assurance defines the criteria for. This boundary is noted, not settled — it resolves when Orchestration is designed.

---

Version note: v1 — initial design from the Assurance design pass. 2026-09-15.
