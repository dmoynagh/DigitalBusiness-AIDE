Project Design — Design | design | ProjectDesign_Design@v2 | 2026-09-11

## Brief

**Purpose.** Provide a fluid environment for design thinking, but produce an accurate, clear specification that build can act on. Fluid in, precise out. Project Design owns both ends of the design-build loop — not just the outbound specification, but the response from build as it pertains to design.

**Objectives.**

1. Stay fluid enough to think freely — support open design conversation across the full input set (purpose, stakeholders, outcomes, requirements, considerations, background, business case, prior research, methodology).
2. Stay structured enough to converge — the AI writes and places each piece into the right doctype and section, asks when unsure, and flags when there is nowhere for something to live.
3. Guarantee no confirmed design commitment goes silently undelivered — the producer rule into the work register.
4. Group owed work into areas at the design side; build decides units of work. The design-build handoff sits at that seam.
5. Scale from trivial to complex without changing method.

**Requirements.**

1. **Hold a fluid design space** — support open conversation across the full input set, with no ceremony blocking thinking.
2. **Converge into an accurate, actionable specification** — a guarantee of placement, not merely of capture.
3. **Never silently swallow a homeless piece** — ask, or flag that there is nowhere for it to live. Nothing is dropped because it did not fit.
4. **Guarantee no confirmed commitment goes undelivered** — the producer rule at requirement weight.
5. **Own the return from build** — reconcile the five return states; run cost discovery.
6. **Scale trivial to complex without changing method** — including at block level, with detail and language held proportional to scale. Judge the amount of structure by consequence, reach, reversibility and uncertainty.

**Definition of done.** The design specifies every element, mechanism and rule needed for a project design to flow from intent through to reconciliation. All six requirements are delivered, or explicitly deferred with a reason.

## The design shape

**One flow, three holding places, one seam.**

The flow: intent → capture and place → brief → design → commitments → register → handoff → build → reconcile.

The holding places: brief, design, overview — plus the work register, which is Project Design's own.

The seam: the design-build handoff — where responsibility crosses from design to build.

Three things to specify: the capture-and-place mechanism; brief-to-design delivery and elasticity; and the commitment-and-return loop. But the elements of a Project Design must be defined first — placement is routing, and each element's definition is the routing rule.

## The document set

**Owned doctypes:** brief (a composite block, mandatory), design, overview, and work register.

**The producer rule.** Whenever a confirmed design change creates downstream work that is not already represented in the register, that work must be entered as a register item in the same pass. An existing register item that already covers the obligation is not duplicated. This is the mechanism that delivers Requirement 4 — the guarantee that no confirmed commitment goes silently undelivered.

**Owned transition mechanisms:** the design-build handoff and the build return. These are mechanisms, not fixed doctypes — their shape varies with the scenario.

**Consumed generics:** decisions, knowledge, WIP, open items, work item, definition of done.

A **design project** is the scope of one design: a brief and the design that delivers it, together with the commitments entered into the work register. A naming convenience for a boundary that already exists, not a new entity. If it starts acquiring properties — a state, an owner, a lifecycle — that is the signal it was a mistake.

**Build project** is deferred under the demonstrated-requirement rule. The brief carries a plain identifier for its linked build project; the definition question waits until something demonstrates the need. Recorded direction: the build project's identity is documented at the root of the topic that holds its designs.

Cardinality: many-to-one is the common case (several design projects feed one build project). Many-to-many is allowed.

## Brief

### What the brief is

The brief fixes the problem and the bar for success before designing. The brief is the problem space; the design is the solution space. The brief must be complete enough that the design has everything it needs, without smuggling in solution decisions.

A brief is mandatory — always. Standalone or inline at the head of a design document, but never absent. Design is the delivery of the brief, so design cannot exist without one.

The brief is a composite block type containing its element blocks. The composite unit can be the body of a standalone brief document or sit at the head of a design document for a small project. The split test governs when it branches out: externalise when keeping the block inline would compromise the primary role of its host.

### Brief sections

**Required, always — the irreducible core:**

- **Purpose** — the problem or need, and why it is worth solving.
- **Objectives** — what success looks like.
- **Definition of done** — the completion bar. Short, accurate, concise — the primary success test. Definition of done is a generic block type owned by Working Practices; the brief consumes it.

**Required in substance, may be light:**

- **Requirements** — the conditions the solution must satisfy. May be a single line, but never absent: "no stated requirements" is a deliberate statement, not an omission.
- **Scope and boundaries** — what is in, and what is explicitly out. Split from considerations because out-of-scope is one of the highest-value things a brief carries and it gets lost when buried.
- **Linked build project or build outcome** — which build the design feeds. Absent only where the design produces no build.

**Optional, scale- and scenario-dependent:**

- **Considerations** — constraints, background, stakeholders, business case, prior research, methodology, assumptions, risks.
- **Target / outcome** — the intended end state and any acceptance criteria. Separate from definition of done: definition of done is the pass-or-fail test; target/outcome is the broader described end state.

The brief scales by which sections are present and how deep each runs.

### Brief boundary tests

Five tests settling where content belongs when the destination is not obvious. These are boundary tests involving brief content — some resolve placement within the brief, others resolve the boundary between the brief and a neighbouring destination (decisions, design).

1. **Objectives vs requirements.** An objective is what success looks like; a requirement is a condition the solution must meet to get there. "Fast" is an objective; "responds within two seconds" is a requirement.
2. **Considerations vs decisions.** A consideration is live input still bearing on the design; the moment it resolves into a choice it moves to decisions.
3. **Requirements vs scope.** A requirement constrains the solution; scope bounds the work. "Must work offline" is a requirement; "the mobile client is out this phase" is scope. The tell: does it constrain the solution or the effort?
4. **Target/outcome vs definition of done.** The condition you check to say "finished" is definition of done. What you are trying to bring about is target/outcome.
5. **Requirement vs implementation choice.** A requirement states what the outcome must satisfy. A requirement written as "use X" rather than "must achieve Y" pre-decides the design inside the brief, closing the fluid space before it opens. This runs directly against Project Design's purpose — fluid in, precise out.

## Design document

### What the design is

The design is the current confirmed model and approach — the authoritative delivery of the brief. A point-in-time snapshot of what is true now; it must be sufficient on its own to produce outcomes, and it governs on conflict. It is the primary source for the build handoff.

The design carries its own live reasoning inline. Duplication with decisions is accepted and expected: design holds the live why for the current approach; decisions holds the fuller why, including paths not taken and reasoning that no longer bears on the current snapshot. This makes the design genuinely self-sufficient for the handoff without requiring the reader to find the reasoning elsewhere.

The design document is the authoritative doctype — it governs on conflict with decisions or knowledge. Between master updates, the current position on the design is the master document plus any pending design content in the working document. Pending content has the same authority as the master it is destined for.

### Design criteria

The design is not done until all nine hold:

1. **It delivers the brief** — every requirement is addressed, or explicitly deferred or rejected with a reason.
2. **It is sufficient alone** to produce the outcome.
3. **Every element carries its why inline.**
4. **It states the model.**
5. **It states its boundaries** — what it does not cover, and where it hands off.
6. **Workflow, behaviour, methodology rules and guidance are recorded in it.**
7. **It is current state** — no superseded content left standing.
8. **Its thinking is routed to decisions and knowledge as produced** — the producer obligation, not a later sweep.
9. **Current design contributions do not conflict materially.** Where several current contributions bear on the same outcome, they are reconciled before handoff. Build is never handed a choice between unresolved designs.

### Design advice

- Group elements as model / rules / definitions / boundaries.
- Lead with the model before elaborating. State it compactly; if it will not state cleanly, the model is wrong, not the write-up.
- Link elements back to brief items where the connection is not obvious.
- Include a worked example where the rules are abstract.

### Reasoning routing

Because the design is only a snapshot, the reasoning behind each choice is lost unless captured as the design is worked. The routing is a producer obligation:

**Same-pass rule** — a design change and its reasoning are produced together; reasoning is never left to live only in conversation.

**Retention checkpoint** — every design-element change triggers a check: anything removed from the design must survive in decisions; if not, it is added before the removal stands. This is the locked content-removal trigger pointed at the document most likely to churn.

**Split** — topic-scoped reasoning to decisions; reasoning with no owning topic to knowledge.

**Authority** — decisions and knowledge inform; they never override or supplement the design as the executable authority. Design governs on conflict.

### Coverage check

A coverage check is run once, when the design is called done — walk the brief's requirements and confirm each is met, deferred, or rejected. Per-element traceability links were rejected: they rot on every edit and the maintenance cost buys little. The coverage check tests criterion 1 above.

## Overview

### What the overview is

A single pane-of-glass snapshot of a whole project — an accurate, concise snapshot that can be loaded into the head quickly. It solves the single biggest problem in working with AI: information overload when working across five or ten topics and switching between build and design work. It gives context for anything discussed without re-reading the documentation set, and serves as a deviation detector — a concise snapshot surfaces anything that does not align with the objective or the model.

**Owner:** Project Design. **Audience:** primarily human.

### Overview content

**Required:** key objective; the chosen approach or delivery method; the top-level model; key defining principles.

**Advice:** project-level scope and boundaries, where a reader would otherwise misjudge the edges.

**Register:** statements, not explanation. Each entry is a recall handle with the detail reachable on demand. Brevity is a strong benefit but never bought at the cost of what the overview must contain.

### Overview scaling

Inline in the design or the brief for small projects; split out into its own document per the split test. Where a project is a single document, the overview and that document's summary are the same artefact, not two.

**The summary suppression rule.** While an overview lives inline in a document, that document does not also carry a summary — the overview is already doing the orienting job at a superset level. The moment the overview branches out to its own document, the source document gets a summary back.

## Work register

### What the work register is

The ledger of confirmed work owed and not yet fully delivered. Not ideas, not maybes — those are work items and go to open items or stay in conversation. Default-on: non-use must be stated explicitly.

**Owner:** Project Design. The register is the one artefact where design is both source and target — the only thing Project Design both produces and consumes — which is why its states must reconcile against build return.

### Work register fields

**Required:** source (the design element or decision that committed it); the commitment (what was committed); what must change (the required output or implementation change); target (where the change lands); state.

**Advice:** handoff reference, return reference, area.

### Origin tagging

Each item tags its origin as design-generated or directly-entered. The register admits confirmed non-design-generated work. The discipline that real design work should not bypass design is a judgement at entry, not a mechanism.

### Writing rule — logical blocks of work

Items go to the register as logical blocks of work — coherent wholes that mean something on their own terms, each individually completable or completable together. Design does the chunking at the point of writing the entry, not afterwards when a partial return forces the question. The axis is coherence, not build-effort sizing.

There are no child items and no task tree — the register stays flat and every item is atomic: owed or discharged. Build may take items singly or swallow several in one handoff, since build owns units of work. If an item cannot be completed by one handoff, that is a sign design wrote it too coarse.

### Area — a flat optional label

An item may carry an area. An area is a label, not a container: areas do not own items, have no states, are never completed, and nothing rolls up. It exists so design can hand off a coherent bundle and so the register can be read by theme. Design does the labelling because design holds the coherence view that build does not.

### States

Four states:

1. **Owed**
2. **Handed off**
3. **Returned, pending reconciliation**
4. **Reconciled**

Build return states map to register consequences: confirmed → reconcile and close. Needs information or raises an issue → back to owed, the issue becomes a work item for design. Failed → back to owed. Done with deviation → returned-pending; design decides whether to accept.

**Invariant:** build never closes a register item. Design owns closure because design owns the commitment.

### Immutability after handoff

**Not yet handed off (owed):** the entry is mutable. Superseded → amend in place. No longer relevant → remove it; removal is a retention trigger, so the withdrawal and its reason go to decisions in the same pass.

**Already handed off:** the description of the work owed is immutable. It is the record of what crossed the responsibility boundary and nothing may rewrite it. Design determines the impact and the remedy, makes the call explicitly, and records it. The register carries the outcome; the reasoning goes to decisions.

Advice: a superseding commitment usually wants its own entry; telling build sooner is usually better than later.

## Capture and place

### What capture and place is

A Project Design conversation wanders — tangents, triggers, exploration alongside focused work. The AI's job is that nothing said gets left where it fell. Each thing that emerged gets put where it belongs.

The requirement: the director stays focused on the knowledge and on working the item, trusting the AI to file everything necessary in the appropriate place, with no valuable knowledge lost.

### Three obligations on the AI

1. **Continuous capture, silently.** The moment something in the conversation settles, shifts or is raised, it is noted against a destination — then, not at session end. Nothing is held on the strength of "I'll remember." A session-close sweep recovers only what is still visible; the early material in a long chat drifts out of reach.

2. **Placement by destination definitions.** Settled things go to a permanent home — the brief if problem-space, the design if solution-space, decisions if topic-scoped reasoning, knowledge if reasoning with no owning topic. Unsettled content goes to a holding place — WIP for live thinking, open items for a parked question. Confirmed but undelivered work goes to the work register — not unsettled, but not yet delivered. The brief boundary tests resolve placement involving brief content.

3. **Batched surfacing at natural breaks.** What was captured and where it is going is put in front of the director in plain language; he agrees or corrects; only then is it written.

The director may override any placement at any time but never has to. If he says nothing, it still lands.

### Placement rules

**Placement defers to the destination's own standard for content.** Capture and place routes to a destination; the destination's standard says what belongs in it. This mechanism holds no guidance of its own about what a decisions entry or a brief section should contain — that would be a second source of truth.

**Homeless pieces are named, not dropped.** Anything that cannot be placed is surfaced in the batch rather than quietly left out. Where there is genuinely nowhere proper, the interim-placement rule applies: place it sensibly for now and raise a review task.

**Err toward over-capture.** Cheap to delete in review, expensive to lose. Including tangents that went nowhere: the reason a line was abandoned is often the keepable part, and that is a knowledge entry.

**Batch triggers.** The session-transition commands (full stop, checkpoint and continue, flush without closing) are the batch triggers. When a topic closes mid-chat, the AI offers the batch unprompted rather than waiting for a command.

## The commitment-and-return loop

The circuit: a design change produces a commitment (register entry, owed) → handoff, responsibility crosses → build works → build return in one of five states → reconciliation → the item closes, or the return provokes a design change which produces fresh commitments.

### The escalation boundary

Design owns the what and why; build owns the how. The test: does what build encountered change what is being delivered or why, or only how it gets delivered? How is build's call. What or why comes back.

**Tiebreak:** if build cannot tell which side it is on, it returns. An unnecessary return costs a message. Silently absorbing a design change costs the design's authority and is exactly the silent-swallowing failure this component exists to prevent.

### The cost-and-complexity flag

Something that looks simple in design can turn out complex in build. Rather than build persevering and silently carrying that cost, it flags: this is looking more extensive and complicated than it probably seemed from the design side — do you want to review, or are you happy to proceed?

What is being protected is the value-versus-cost judgement, and that judgement is design's, because only design holds the why.

An obligation, not a threshold. When the real cost or complexity materially exceeds what the design appeared to assume, build surfaces it before proceeding. No number — just the duty to flag, and build's own judgement of "materially."

A flag with a default of proceed, not a return. If design does not intervene, build proceeds. The loop keeps moving.

### The design-build handoff

The handoff is where responsibility crosses from design to build. The work-package doctype is withdrawn — replaced by a transition point whose mechanism varies with the build context.

- **Design must not overreach into build — even in the same session.** The transition point exists to stop design running, controlling or managing build.
- **Shape varies with scenario** — a one-line message for trivial work, a full package for complex work; it may not physically move when design and build share a session.
- **Multiple builders.** One design may hand off to several builders for different components, each returning independently.
- **Sufficiency is the one firm requirement.** Whatever crosses must carry everything the build side needs to act without returning to the design conversation. Format free, sufficiency required.
- **Sufficiency has a ceiling as well as a floor.** Do not re-supply generic execution-platform knowledge the build environment already provides. The handoff carries what is specific to this work.

### Build return

Every build handoff expects a build return. A confirmation of the work is the default, because without it nothing can establish that a handoff completed. Fire-and-forget is allowed but must be explicitly declared.

A handoff and its return are a matched pair. An open handoff with no return is an incomplete transaction.

**Return states:** confirmed, needs information, raises an issue, failed, done with deviation.

**Return sufficiency:** the return must carry everything design needs to reconcile without going back to build. Sufficient out, sufficient in.

- **Never bare.** "Done" is not a return. Every return carries a real description of what was actually done, or what prevented it — accessible and comparable so design can hold it against the commitment.
- **Attribution on failure.** A failure has two possible origins and the return must say which: design-side (unbuildable, unclear, conflicting) or build-side (a configuration, environment, file or tooling fault). The response differs completely. Selectivity is allowed on deep internal build faults: build reports enough to establish it was build, not design, without exposing the whole internal cause.
- **Proportional to the task.** A trivial task earns a brief return; a high-impact task earns fuller reporting, because design has a heavier decision to make.
- **Review results ride in the return.** Where the work was reviewed, the return says so and carries the result.

### Reconciliation

Reconciliation is design's act of checking a return against its commitment and deciding the outcome — close it, accept a deviation, or send it back to owed. One act, three endings.

Who: design, always. Build reports; design decides.

Against what: the original commitment — what the register said was owed. Not "did build do something" but "did build do the thing that was promised."

It fires on two return states: confirmed (check and close) and done with deviation (design decides whether the deviation is acceptable; accepting is itself a design change and may spawn a fresh commitment; rejecting returns it to owed). The other three states deliver nothing to reconcile — the item stays owed and routes back into the design conversation.

### Loop visibility

An item that has been round the loop several times is a design smell worth surfacing — usually the design is wrong at a level above the item. Not blocked, not stopped, just visible. Every trip round the loop is provoked by something real; the goal is not the loop stopping but the register emptying.

## Design is the default

A design almost always exists behind a standard, and a standard almost always has a design behind it. Authoring straight to standard is the exception — justified only where everything worth recording fits the standard without compromising either document. The design holds the reasoning, alternatives and constraints; the standard holds the conclusion. Forcing everything into the standard alone either bloats it past the conciseness gate or leaves the reasoning unrecorded.

## Component-ownership boundary

The governing test — the provider-consumer test Documentation Methodology already uses: **does the thing exist and carry meaning outside Project Design?** Yes → it is generic and lives with the generic owner. No → it belongs to Project Design.

Applied: the work register comes home to Project Design (the temporal gap it fills only exists because Project Design owns both ends of the loop). WIP stays generic (any session stages thinking). Open items stay generic (build sessions accrue deferred sub-tasks). Decisions and knowledge stay generic (provisional home Working Practices).

**Three placement bands:**
1. Universal grammar → Documentation Methodology.
2. Generic operating behaviour and live state → Working Practices.
3. Component-specific → the component itself.

## Boundaries

Project Design does **not** own:

- **WIP, open items, decisions, knowledge** — generic doctypes, provisional home Working Practices.
- **The work item** — a generic workflow entity owned by Working Practices.
- **Definition of done** — a generic block type owned by Working Practices; the brief consumes it.
- **Document structure and block grammar** — Documentation Methodology.
- **Session-transition commands** — Working Practices.
- **The shaping behaviour for brief and design** — how they get evolved in conversation; Working Practices for now.

## Carries to other components

**To Principles:** definition of done as a candidate premise.

**To Working Practices:** WIP and open items; decisions and knowledge doctype ownership; the shaping behaviour for brief and design; the no-knowledge-lost rule; the session-transition commands; the nomination model for live-state granularity; the six-stage review procedure; the work item as the base workflow entity; definition of done as a generic block.

**To Build:** build must recognise it is holding a what/why question rather than a how question, and must judge when cost has materially exceeded the design's apparent assumption.

**To Documentation Methodology:** the split test; the ownership-designation rule; the binder doctype definition.

**To Standards:** the Contents/Summary edge.

**To Core:** facilitate, not constrain — its form and home at AIDE's root are deferred.

---

Version note: v2 — cross-review remediation: producer rule specified (PD-D1), boundary test framing corrected (PD-D2), capture-and-place three bands (PD-D3), proportionality factors added (PD-S8), model advice items merged (PD-DEC2), two-tier model acknowledged (PD-DEC4/D21). 2026-09-11.
