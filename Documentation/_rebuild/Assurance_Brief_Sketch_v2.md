# Assurance — Brief (sketch)

This is a sketch produced during the Working Practices design pass and expanded during the Assurance scoping session. It is not a full brief — purpose, content, and scope direction are confirmed; formal objectives and definition of done await the design pass.

---

## Purpose

Build justified trust in AI-assisted work by defining and evolving the conventions, structures, and detection mechanisms that ensure the human's intent is reliably delivered and that anomalies, drift, errors, and misunderstandings are visible when they occur.

## Role

Guidance. Sits alongside Principles, Standards, and Tools. Provides the trust and outcome conventions.

## Scope — full lifecycle, not build-focused

Assurance runs the full length of work, from the first conversational concept through to delivery. The quality of the top two levels of design — the overview and the approach — carries a near one-to-one relationship with everything downstream: what's built, delivered, deployed, and managed. Assurance therefore protects the highest-leverage work first. It is not primarily a build-side or output-verification concern.

This means assurance conventions apply during the qualifying and shaping of intent, during the human-and-AI design of the model, through AI-driven detailed specification, into build, and through orchestration and review. The earliest stages are where assurance matters most, because a flaw at the top multiplies through every layer below.

## Cross-cutting nature

Assurance is both a component and a framework-wide requirement. Every element in the framework contributes to assurance — the brief-required gate, cross-review, operations test, acceptance test, strength model, capture-and-place, the design-check skill, definition of done, Principles P7/P8/P10 all contribute. The component owns its specific mechanisms; the framework-wide requirement is the lens every component is designed through.

## Content

Three connected areas of concern, following the lifecycle of the work.

### Proactive conventions — getting to the right outcome

Help the AI deliver correctly in the first place:

- **Human working model** — the AI's operational contract with the human: tiering (named autonomy levels, small number, chosen by either side, AI judges default, human overrides), confidence signalling (using the existing framework strength model), assumptions and gap-fill report (the AI discloses what it filled in versus what the human stated)
- **Overview-first discipline** (consumed from WP's generic statement) — the single most important assurance behaviour, because quality at the overview level is the primary determinant of downstream outcome

### Detective conventions — making deviation visible

Help the human see when something has gone wrong:

- **Verification behaviours** — verify inspectable facts, distinguish generated intent from applied state (consuming Principles P7: verified truth over plausible assertion, and P9: confirmed state over assumed state)
- **Drift detection** — recognising when work moves away from the agreed model, objective, or scope (consuming P7: loud failure over quiet absorption)
- **Anomalies channel** — surfacing things that don't fit. A behaviour with capture-and-place as the destination, not a separate mechanism

### Learning and feedback loop — improving from experience

Identify opportunities where work outcomes can teach the system to be better:

- **Measurable moments** — recognising situations where a clean A-B comparison exists: a known starting point, work done, an accepted end point. These are the recognition capability — Assurance has to know what a measurable moment looks like so it can catch one when it occurs.
- **Quick comparison and capture** — at a measurable moment, the AI does a comparison and makes a judgement call on whether a learning is significant or noise. If significant, it writes a short synopsis to the learnings queue. This is AI-initiated and runs in the background, not prompted by the human.
- **Learnings queue** — a distinct queue from the task/item queue. Holds raw observations written whenever a comparison throws one up. The threshold and frequency of comparisons need to be tunable, since each comparison costs thinking and consumption. Most entries sit and wait — their value is only visible in aggregate.
- **Two escalation triggers** — a single high-impact instance caught in the moment (significant enough to act on alone), or a pattern that emerges across many low-weight entries during periodic review. Minor-but-frequent is a category that only exists in aggregate, so the queue must preserve entries that looked small individually.
- **Interface to Improvement** — Assurance identifies and captures. The Improvement component (see boundary below) analyses, finds patterns, and decides what to act on. The learnings queue is the interface between them.

### Evolution path

New failure modes discovered in practice become new conventions or detection behaviours. The area is a living system, not a fixed specification. This is the charter's extensibility-from-learning objective (O4) showing up as a structural commitment.

## Key boundaries

- Assurance defines what to watch for and how to signal it — conventions and policy
- WP defines how work is conducted — the substrate Assurance runs on
- Principles provides the reasoning premises both consume
- Infrastructure owns the plumbing — the MCP that writes to the queue, the queue file format and location
- Orchestration provides the mechanism to run things on a schedule — transport, not business logic
- **Improvement** (new, identified but not yet scoped) — owns the pattern analysis, the periodic review of the learnings queue, and the decision about what to act on. Assurance identifies and captures; Improvement analyses and acts. The reviewer that periodically reads the learnings queue, spots candidate patterns, and escalates sits in Improvement, not Orchestration or Assurance.
- Cross-review is likely an Orchestration concern that Assurance defines the criteria for

## Confirmed design decisions

- Named tiers for autonomy levels, small number, chosen by either side. AI judges default; human overrides
- Anomalies channel is a behaviour with capture-and-place as destination, not a separate mechanism
- Confidence vocabulary uses the framework's existing strength model (strong/moderate/etc.), not a new system
- Learnings queue is distinct from the task/item queue — different lifecycle, different purpose
- Two escalation triggers: single high-impact instance, or accumulated pattern
- These decisions require review when the full design brief is produced

## Charter alignment

Directly delivers O1 (trust and integrity) — the framework's primary reason for existing.
Contributes to O4 (extensibility from learning) — conventions evolve as collaboration learns; the learning loop makes this concrete.

---

Version note: v2 — expanded from the WP-pass sketch. Added: full-lifecycle scope (not build-focused), learning and feedback loop (measurable moments, learnings queue, two escalation triggers), Improvement component boundary, Infrastructure and Orchestration boundary clarifications. 2026-09-15.
