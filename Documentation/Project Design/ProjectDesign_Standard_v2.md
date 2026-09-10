Project Design — Standard | standard | ProjectDesign_Standard@v2 | 2026-09-11

## What Project Design is

Information. Project Design produces the design specification and manages the return from build. It owns both ends of the design-build loop — the outbound specification and reconciliation when build reports back. Purpose in two words: fluid in, precise out.

Information. The flow: intent → capture and place → brief → design → commitments → register → handoff → build → reconcile.

Recommended. **Proportionality test.** Judge the amount of structure by consequence, reach, reversibility and uncertainty. Small clear tasks do not require ceremony merely to imitate a large project.

## Design is the default

Recommended. A design almost always exists behind a standard, and a standard almost always has a design behind it. Authoring straight to standard is the exception — justified only where everything worth recording fits the standard without compromising either document.

## The document set

Information. Project Design owns four document types: brief, design, overview, and work register. It also owns two transition mechanisms — the design-build handoff and the build return — and the producer rule. It consumes generics: decisions, knowledge, WIP, open items, work item, and definition of done.

Information. A design project is the scope of one design: a brief and the design that delivers it, together with the commitments entered into the work register. A naming convenience for a boundary that already exists, not a new entity. If it starts acquiring properties — a state, an owner, a lifecycle — that is the signal it was a mistake.

## Brief

Information. The brief fixes the problem and the bar for success before designing. The brief is the problem space; the design is the solution space. The brief must be complete enough that the design has everything it needs, without smuggling in solution decisions.

### Brief sections

**Required, always:**

Required. **Purpose** — the problem or need, and why it is worth solving.

Required. **Objectives** — what success looks like.

Required. **Definition of done** — the completion bar. Short, accurate, concise — the primary success test.

**Required in substance, may be light:**

Recommended. **Requirements** — the conditions the solution must satisfy. May be a single line, but never absent: "no stated requirements" is a deliberate statement, not an omission.

Recommended. **Scope and boundaries** — what is in, and what is explicitly out.

Recommended. **Linked build project or build outcome** — which build the design feeds. Absent only where the design produces no build.

**Optional, scale-dependent:**

Optional. **Considerations** — constraints, background, stakeholders, business case, prior research, methodology, assumptions, risks.

Optional. **Target / outcome** — the intended end state and any acceptance criteria. Separate from definition of done: the definition of done is the pass-or-fail test, the target is the broader described end state.

Information. The brief scales by which sections are present and how deep each runs.

### Brief boundary tests

Required. These five tests settle where content belongs when the destination is not obvious. Apply them as tie-breakers during capture and placement.

1. **Objectives vs requirements.** An objective is what success looks like; a requirement is a condition the solution must meet to get there. "Fast" is an objective; "responds within two seconds" is a requirement.

2. **Considerations vs decisions.** A consideration is live input still bearing on the design; the moment it resolves into a choice it moves to decisions.

3. **Requirements vs scope.** A requirement constrains the *solution*; scope bounds the *work*. "Must work offline" is a requirement; "the mobile client is out this phase" is scope. The tell: does it constrain the solution or the effort?

4. **Target/outcome vs definition of done.** The condition you check to say "finished" is definition of done. What you are trying to bring about is target/outcome.

5. **Requirement vs implementation choice.** A requirement states what the outcome must satisfy. A requirement written as "use X" rather than "must achieve Y" pre-decides the design inside the brief, closing the fluid space before it opens.

## Design document

### What the design is

Information. The design is the current confirmed model and approach — the authoritative delivery of the brief. A point-in-time snapshot of what is true now. It must be sufficient on its own to produce outcomes, and it governs on conflict with any other document.

Required. The design carries its own live reasoning inline — the rationale for the current approach. Duplication with decisions is accepted and expected.

### Design criteria

Required. A design is not done until all nine hold:

1. It delivers the brief — every requirement addressed, or explicitly deferred or rejected with a reason.
2. It is sufficient alone to produce the outcome.
3. Every element carries its reasoning inline.
4. It states the model.
5. It states its boundaries — what it does not cover, and where it hands off.
6. Workflow, behaviour, methodology rules and guidance are recorded in it.
7. It is current state — no superseded content standing.
8. Its thinking is routed to decisions and knowledge as produced — the producer obligation, not a later sweep.
9. Current design contributions do not conflict materially — build is never handed a choice between unresolved designs.

### Design advice

Recommended. Group elements as model / rules / definitions / boundaries.

Recommended. Lead with the model before elaborating. If the model will not state compactly, the model is wrong, not the write-up.

Optional. Link elements back to brief items where the connection is not obvious.

Optional. Include a worked example where the rules are abstract.

### Reasoning routing

Required. A design change and its reasoning are produced together. Reasoning is never left to live only in conversation.

Required. Every design-element change is a retention checkpoint: anything removed from the design must survive in decisions. If not, add it before the removal stands.

Information. Topic-scoped reasoning goes to decisions; reasoning with no owning topic goes to knowledge. Decisions and knowledge inform but never override design.

### Coverage check

Required. When the design is called done, walk the brief's requirements and confirm each is met, deferred, or rejected.

## Overview

Information. The overview is the project-scale snapshot — a pane-of-glass view of the whole design project. Also a deviation detector: anything that cannot be placed against the overview is either a branch or evidence the overview is missing something.

Required. The overview carries: key objective, the chosen approach or delivery method, the top-level model, and key defining principles.

Recommended. Include project-level scope and boundaries where a reader would otherwise misjudge the edges.

Required. Overview entries are statements, not explanation — each is a recall handle with detail reachable on demand.

### Scaling and the summary suppression rule

Recommended. The overview sits inline in the design document for small projects. It splits to its own document when the project outgrows that.

Required. While an overview lives inline, the host document does not also carry a summary. When the overview splits out, the source document gets its summary back.

Information. A single-document project's overview and summary are the same thing.

## Work register

Information. The work register is the ledger of confirmed work owed and not yet delivered. Project Design owns it — the register is the one artefact where design is both source and target.

Required. The register is default-on. Non-use must be stated explicitly.

### Entries

Required. Each entry carries five fields: source (the design element or decision that committed it), the commitment, what must change, target (where the change lands), and state.

Recommended. Advice fields: handoff reference, return reference, area.

Required. Each entry tags its origin as design-generated or directly-entered. The register admits confirmed non-design-generated work. The discipline that real design work should not bypass design is a judgement at entry, not a mechanism.

### Writing rule

Required. Items enter the register as logical blocks of work — coherent wholes individually completable, chunked at the point of writing. The axis is coherence, not build-effort sizing. No child items, no task tree — the register stays flat and every item is atomic.

Optional. An item may carry an area label. An area is a label, not a container — areas do not own items, have no states, and nothing rolls up.

### States

Information. Four states: owed → handed off → returned, pending reconciliation → reconciled.

### Immutability after handoff

Required. Once handed off, an entry's description of the work owed is immutable — it is the record of what crossed the responsibility boundary.

Required. Build never closes a register item. Design owns closure because design owns the commitment.

Recommended. When a handed-off commitment is superseded, design determines the impact and remedy, makes the call explicitly, and records it.

## Capture and place

Information. Project Design conversations wander — tangents, triggers, exploration alongside focused work. The AI's job is that nothing said is left where it fell.

### Three obligations on the AI

Required. **Continuous capture, silently.** The moment something settles, shifts, or is raised, it is noted against a destination — then, not at session end. Nothing is held on the strength of "I'll remember."

Required. **Placement by destination definitions.** Settled content goes to a permanent home — brief if problem-space, design if solution-space, decisions if topic-scoped reasoning, knowledge if reasoning with no owning topic. Unsettled content goes to a holding place — WIP for live thinking, open items for a parked question, the work register for confirmed work owed.

Required. **Batched surfacing at natural breaks.** What was captured and where it is going is put in front of the user in plain language; agreed or corrected; only then written. When a topic closes mid-session, the AI offers the batch unprompted.

### Placement rules

Required. Placement defers to each destination's own standard for content. Capture and place holds no guidance of its own about what a decisions entry or a brief section should contain.

Required. Homeless pieces are named, not dropped. Where there is genuinely nowhere proper, place it sensibly and raise a review task.

Recommended. Err toward over-capture. Cheap to delete in review, expensive to lose.

## The commitment-and-return loop

Information. The circuit: a design change produces a commitment (register entry, owed) → handoff → build works → build return → reconciliation → the item closes, or the return provokes a design change producing fresh commitments.

### The escalation boundary

Required. Design owns the what and why; build owns the how. The test: does what build encountered change what is being delivered or why, or only how it gets delivered? How is build's call. What or why comes back.

Required. If build cannot tell which side of the boundary it is on, it returns. An unnecessary return costs a message; silently absorbing a design change costs the design's authority.

### The cost-and-complexity flag

Required. When real cost or complexity materially exceeds what the design appeared to assume, build surfaces it before proceeding.

Information. A flag with a default of proceed, not a return. If design does not intervene, build proceeds.

### Design-build handoff

Required. The handoff carries everything the build side needs to act without returning to the design conversation. Format free, sufficiency required.

Recommended. The handoff has a ceiling as well as a floor — do not re-supply generic execution-platform knowledge the build environment already provides. Carry what is specific to this work.

Required. Design must not overreach into build, even in the same session.

### Build return

Required. Every build handoff expects a build return. Fire-and-forget must be explicitly declared at the handoff.

Required. Never bare. Every return carries what was actually done or what prevented it — accessible and comparable against the commitment.

Required. A failure names its origin — design-side (unbuildable, unclear, conflicting) or build-side (environment, tooling). The response differs: a design fault re-enters design; a build fault means retry or fix, nothing for design to rework.

Recommended. Return is proportional to the task. Sufficiency is "enough for design to make this decision about this task."

Information. Five return states: confirmed, needs information, raises an issue, failed, done with deviation.

### Reconciliation

Required. Reconciliation is design's act of checking a return against its commitment and deciding the outcome — close it, accept a deviation, or send it back to owed.

Information. Reconciliation fires on two return states only. Confirmed — check and close. Done with deviation — design decides whether to accept; accepting is a design change that may spawn a fresh commitment. The other three states (needs information, raises an issue, failed) deliver nothing to reconcile — the item stays owed.

Information. An item that has been round the loop several times is a design smell worth surfacing — usually the design is wrong at a level above the item.
