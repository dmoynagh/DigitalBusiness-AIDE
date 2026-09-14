> identity: ProjectDesign_Standard@v4 | doctype: standard | updated: 2026-09-14 | uses: ProjectDesign_Schema_Standard@v1

# Project Design — Standard

Rules for briefs, design documents, work registers, capture-and-place, and the design-build handoff-return loop.

## Applicability

Information. Apply this standard when doing design work (writing or evolving a brief, design, or overview), managing the work register, performing capture and place during a design conversation, handing off to build, processing a build return, or reconciling a return against a commitment.

## What Project Design is

Information. Project Design produces the design specification and manages the return from build. It owns both ends of the design-build loop — the outbound specification and reconciliation when build reports back. Purpose in two words: fluid in, precise out.

Information. The flow: intent → capture and place → brief → design → commitments → register → handoff → build → reconcile.

**Proportionality test.** Judge the amount of structure by consequence, reach, reversibility and uncertainty. Small clear tasks do not require ceremony merely to imitate a large project.

## Default methodology

A brief is required before design starts. Design without a brief is the exception and requires explicit override.

Recommended. A design almost always exists behind a standard, and a standard almost always has a design behind it. Authoring straight to standard is the exception — justified only where everything worth recording fits the standard without compromising either document.

## The document set

Information. Project Design owns four document types: brief, design, overview, and work register. It also owns two transition mechanisms — the design-build handoff and the build return — and the producer rule. It consumes generics: decisions, knowledge, WIP, open items, work item, and definition of done.

**The producer rule.** Whenever a confirmed design change creates downstream work that is not already represented in the register, that work must be entered as a register item in the same pass. An existing item that already covers the obligation is not duplicated.

Information. A design project is the scope of one design: a brief and the design that delivers it, together with the commitments entered into the work register. A naming convenience for a boundary that already exists, not a new entity. If it starts acquiring properties — a state, an owner, a lifecycle — that is the signal it was a mistake.

Information. Components owning doctypes or block types must define them using the Documentation Methodology definition contract. The Project Design Schema Standard defines this component's types. For guidance on schema placement — when definitions belong in their own standard versus inline — see the Documentation Methodology Schema Authoring Standard.

## Brief

Information. The brief fixes the problem and the bar for success before designing. The brief is the problem space; the design is the solution space. The brief must be complete enough that the design has everything it needs, without smuggling in solution decisions.

A brief is required — standalone or inline at the head of a design document. Omission requires explicit override.

### Brief sections

**Required, always:**

**Purpose** — the problem or need, and why it is worth solving.

**Objectives** — what success looks like.

**Definition of done** — the completion bar. Short, accurate, concise — the primary success test.

**Required in substance, may be light:**

**Requirements** — the conditions the solution must satisfy. May be a single line, but never absent: "no stated requirements" is a deliberate statement, not an omission.

**Scope and boundaries** — what is in, and what is explicitly out. May be light for small projects.

**Linked build project or build outcome** — which build the design feeds. Absent only where the design produces no build.

**Optional, scale-dependent:**

Optional. **Considerations** — constraints, background, stakeholders, business case, prior research, methodology, assumptions, risks.

Optional. **Target / outcome** — the intended end state and any acceptance criteria. Separate from definition of done: the definition of done is the pass-or-fail test, the target is the broader described end state.

Information. The brief scales by which sections are present and how deep each runs.

### Brief boundary tests

These five boundary tests involving brief content settle where content belongs when the destination is not obvious — some resolve placement within the brief, others resolve the boundary between the brief and a neighbouring destination.

1. **Objectives vs requirements.** An objective is what success looks like; a requirement is a condition the solution must meet to get there. "Fast" is an objective; "responds within two seconds" is a requirement.

2. **Considerations vs decisions.** A consideration is live input still bearing on the design; the moment it resolves into a choice it moves to decisions.

3. **Requirements vs scope.** A requirement constrains the *solution*; scope bounds the *work*. "Must work offline" is a requirement; "the mobile client is out this phase" is scope. The tell: does it constrain the solution or the effort?

4. **Target/outcome vs definition of done.** The condition you check to say "finished" is definition of done. What you are trying to bring about is target/outcome.

5. **Requirement vs implementation choice.** A requirement states what the outcome must satisfy. A requirement written as "use X" rather than "must achieve Y" pre-decides the design inside the brief, closing the fluid space before it opens.

## Design document

### What the design is

Information. The design is the current confirmed model and approach — the authoritative delivery of the brief. A point-in-time snapshot of what is true now. It must be sufficient on its own to produce outcomes, and it governs on conflict with decisions or knowledge.

The design carries its own live reasoning inline — the rationale for the current approach. Duplication with decisions is accepted and expected.

Information. A design has two recognised parts. The first part — the approach — states the model, the key principles, and the framework: what the design is and why it is shaped that way. The second part — the detailed design — elaborates each element within that framework. The approach is tested by the approach completeness check; the detailed design is tested by the element quality check. Both checks are defined below.

### Design criteria

A design is not done until all nine hold:

1. It delivers the brief — every requirement addressed, or explicitly deferred or rejected with a reason.
2. It is sufficient alone to produce the outcome.
3. Every element carries its reasoning inline.
4. It states the model.
5. It states its boundaries — what it does not cover, and where it hands off.
6. Workflow, behaviour, methodology rules and guidance are recorded in it.
7. It is current state — no superseded content standing.
8. Its thinking is routed to decisions and knowledge as produced — the producer obligation, not a later sweep.
9. Current design contributions do not conflict materially — build is never handed a choice between unresolved designs.

### Operations test

For every significant objective, determine what a consumer must be able to do when the objective is met. Test whether the design specifies enough for that operation to be performed deterministically. If the consumer would have to invent a convention, the design is incomplete.

### Design advice

Recommended. Group elements as model / rules / definitions / boundaries.

Recommended. Lead with the model before elaborating. If the model will not state compactly, the model is wrong, not the write-up.

**Derive from the model, not from a single requirement.** Understand what the model is, why it is shaped that way, and what it implies before designing against it. A solution derived from one requirement in isolation tends to be broader than needed or inconsistent with what surrounds it.

**Context rule.** Every design element's place in the model must be visible, carried in the element's own description. The model is part tree, part web, part horizontal — an element may relate to several things above it, or span everything as a cross-cutting concern. State context explicitly only where it cannot be implied or inferred. Context that requires separate wiring, references or notation is ceremony the design should not need.

Optional. Link elements back to brief items where the connection is not obvious.

Optional. Include a worked example where the rules are abstract.

### Approach completeness check

Run before descending from the approach into detailed design.

**The test:** could the detailed design be executed excellently from this approach, by someone who has the brief and was not part of the conversation?

If no, the approach is not finished. Do not descend. Complete it instead — test the boundaries and the silences, check coherence, and resolve gaps at the cheapest possible moment.

### Element quality check

Run over any design element before it is accepted. Four questions per element:

**1. Can it be placed?** Which part of the overview does it relate to, where does it sit in the model? An element that cannot be placed is either a branch, or evidence the overview is missing something. Both are findings. Neither is silently kept.

**2. Is its context clear in its own description?** Context is carried in the element's description, not in separate wiring. State it explicitly only where it cannot be implied or inferred.

**3. Is it proportionate to the intent above it?** Output markedly more elaborate than the intent it serves means either the intent was more complex than it looked, or it has been over-built.

**4. Was it derived from the model, or from a single requirement?** Anchoring to one point produces work that is broader than needed or inconsistent with what surrounds it.

**Coverage:** when the design is called done, check once that every objective in the brief is delivered. Anything present that does not trace to the brief is listed separately as an addition, not woven in.

### Reasoning routing

A design change and its reasoning are produced together. Reasoning is never left to live only in conversation.

Every design-element change is a retention checkpoint: anything removed from the design must survive in decisions. If not, add it before the removal stands.

Information. Topic-scoped reasoning goes to decisions; reasoning with no owning topic goes to knowledge. Decisions and knowledge inform but never override design.

## Overview

Information. The overview is the project-scale snapshot — a pane-of-glass view of the whole design project. Also a deviation detector: anything that cannot be placed against the overview is either a branch or evidence the overview is missing something.

The overview holds the shape of the model. Any element should be placeable against it quickly — which part does this relate to, where does it sit in the model. This gives the overview structural work to do, not decorative work, and is why the overview must be genuinely complete at the top.

The overview carries: key objective, the chosen approach or delivery method, the top-level model, and key defining principles.

Recommended. Include project-level scope and boundaries where a reader would otherwise misjudge the edges.

Overview entries are statements, not explanation — each is a recall handle with detail reachable on demand.

### Scaling and the summary suppression rule

Recommended. The overview sits inline in the design document or the brief for small projects. It splits to its own document per the split test — externalise when keeping it inline would compromise the primary role of its host.

While an overview lives inline, the host document does not also carry a summary. When the overview splits out, the source document gets its summary back.

Information. A single-document project's overview and summary are the same thing.

## Work register

Information. The work register is the ledger of confirmed work owed and not yet delivered. Project Design owns it — the register is the one artefact where design is both source and target.

The register is default-on. Non-use must be stated explicitly.

### Entries

Each entry carries six fields: source (the design element or decision that committed it), the commitment, what must change, target (where the change lands), state, and origin tag.

Recommended. Advice fields: handoff reference, return reference, area.

Each entry tags its origin as design-generated or directly-entered. The register admits confirmed non-design-generated work. The discipline that real design work should not bypass design is a judgement at entry, not a mechanism.

### Writing rule

Items enter the register as logical blocks of work — coherent wholes individually completable, chunked at the point of writing. The axis is coherence, not build-effort sizing. No child items, no task tree — the register stays flat and every item is atomic.

Optional. An item may carry an area label. An area is a label, not a container — areas do not own items, have no states, and nothing rolls up.

### States

Information. Four states: owed → handed off → returned, pending reconciliation → reconciled.

### Register maintenance

While an item is owed and not yet handed off, it may be amended in place when superseded, or removed when no longer relevant. Removal is a retention trigger — the withdrawal and its reason go to decisions in the same pass.

### Immutability after handoff

Once handed off, an entry's description of the work owed is immutable — it is the record of what crossed the responsibility boundary.

Build never closes a register item. Design owns closure because design owns the commitment.

When a handed-off commitment is superseded, design determines the impact and remedy, makes the call explicitly, and records it.

## Capture and place

Information. Project Design conversations wander — tangents, triggers, exploration alongside focused work. The AI's job is that nothing said is left where it fell.

### Three obligations on the AI

**Continuous capture, silently.** The moment something settles, shifts, or is raised, it is noted against a destination — then, not at session end. Nothing is held on the strength of "I'll remember."

**Placement by destination definitions.** Settled content goes to a permanent home — brief if problem-space, design if solution-space, decisions if topic-scoped reasoning, knowledge if reasoning with no owning topic. Unsettled content goes to a holding place — WIP for live thinking, open items for a parked question. Confirmed but undelivered work goes to the work register.

**Batched surfacing at natural breaks.** What was captured and where it is going is put in front of the user in plain language, providing an opportunity to correct placement. If no correction is given, the placement stands — silence does not block persistence. When a topic closes mid-session, the AI offers the batch unprompted.

### Placement rules

Placement defers to each destination's own standard for content. Capture and place holds no guidance of its own about what a decisions entry or a brief section should contain.

Homeless pieces are named, not dropped. Where there is genuinely nowhere proper, place it sensibly and raise a review task.

Recommended. Err toward over-capture. Cheap to delete in review, expensive to lose.

## The commitment-and-return loop

Information. The circuit: a design change produces a commitment (register entry, owed) → handoff → build works → build return → reconciliation → the item closes, or the return provokes a design change producing fresh commitments.

### The escalation boundary

Design owns the what and why; build owns the how. The test: does what build encountered change what is being delivered or why, or only how it gets delivered? How is build's call. What or why comes back.

If build cannot tell which side of the boundary it is on, it returns. An unnecessary return costs a message; silently absorbing a design change costs the design's authority.

### The cost-and-complexity flag

When real cost or complexity materially exceeds what the design appeared to assume, build surfaces it before proceeding.

Information. A flag with a default of proceed, not a return. If design does not intervene, build proceeds.

### Difficulty as evidence

When something is becoming hard, expensive or elaborate to implement, that is evidence the model or approach may need review — not that the implementation needs more cleverness. At each implementation decision, ask whether a change in the model would make this better, easier, more robust or more comprehensive.

Recommended. A single small accommodation is usually absorbed. The same accommodation recurring across several elements is the strongest signal to raise it, however small each instance looks. Recurrence is visible from across the work in a way it is not from any single element.

### Design-build handoff

The handoff carries everything the build side needs to act without returning to the design conversation. Format free, sufficiency required.

Recommended. The handoff has a ceiling as well as a floor — do not re-supply generic execution-platform knowledge the build environment already provides. Carry what is specific to this work.

Design must not overreach into build, even in the same session.

### Build return

Every build handoff expects a build return. Fire-and-forget must be explicitly declared at the handoff.

Never bare. Every return carries what was actually done or what prevented it — accessible and comparable against the commitment.

A failure names its origin — design-side (unbuildable, unclear, conflicting) or build-side (environment, tooling). The response differs: a design fault re-enters design; a build fault means retry or fix, nothing for design to rework.

The return carries everything design needs to reconcile without going back to build. Sufficiency is symmetrical with handoff sufficiency.

Recommended. Return detail is proportional to the task — a trivial task earns a brief return, a high-impact task earns fuller reporting.

Where the work was reviewed, the return identifies that a review was performed and carries the result.

Information. Five return states: confirmed, needs information, raises an issue, failed, done with deviation.

### Reconciliation

Reconciliation is design's act of checking a return against its commitment and deciding the outcome — close it, accept a deviation, or send it back to owed.

Information. Reconciliation fires on two return states only. Confirmed — check and close. Done with deviation — design decides whether to accept; accepting is a design change that may spawn a fresh commitment. The other three states (needs information, raises an issue, failed) deliver nothing to reconcile — the item stays owed.

Information. An item that has been round the loop several times is a design smell worth surfacing — usually the design is wrong at a level above the item.

---

Version note: v4 — design-approach content folded in: two-part design structure (PD-F1), approach completeness check and element quality check as application-time guidance, operations test, context rule and derive-from-model, difficulty-as-evidence in the commitment-and-return loop. Brief-required gate made explicit with override. Overview section strengthened with structural/map role. DocMeth definition-contract and schema-placement pointers added (PD-F2, PD-F3). "Design is the default" renamed to "Default methodology" and expanded. Black-box acceptance test carried to Standards Authoring Standard. Cross-review remediation: authority scope restored to decisions/knowledge (F7), "overview" naming collision resolved — check renamed to approach completeness check (F3), conversational how-to removed from checks per WP ownership boundary (F4), strength inconsistencies corrected (F6). 2026-09-14. Replaces v3.
