# Project Design — Design (Pending Content)

> **Version 1** (2026-09-08). Pending content extracted from AIDE_Rebuild_WIP_v23 per rebuild guide F9. Settled design elements — the model, definitions, and rules. Ready to feed ProjectDesign_Design when masters are authored.
>
> The forward design pass is complete to the Standards block. All six requirements delivered. The binder sweep is complete end to end. Stage 6 (design output and standards) remains, blocked on the Standards component.

---

## Purpose and objectives

### Stage 1 — Purpose (settled)

Original binder line confirmed, then extended: Project Design produces a
coherent specification for work of any size **and manages the response from
build as it pertains to design** — it owns both ends of the loop, not just the
outbound half.

**Sharpened final form:** provide a fluid environment, but produce an accurate,
clear specification that build can act on. Fluid in, precise out.

### Stage 2 — Objectives (settled)

1. Stay fluid enough to think freely — support open design conversation
   (purpose, stakeholders, outcomes, requirements, considerations, background,
   business case, prior research and methodology in the area, and more).
2. Stay structured enough to converge — scribe with a filing system. Claude
   writes and places each piece into the right doctype and section, asks when
   unsure, and flags when there is nowhere for something to live.
3. Guarantee no confirmed design commitment goes silently undelivered — the
   producer rule into the work register.
4. Group owed work into areas at the design side; build decides units of work.
   The design-build handoff sits at that seam. *(Amended later in this pass —
   "work package" as a fixed doctype was withdrawn; see the handoff section.)*
5. Scale from trivial to complex without changing method.

**"Domain-generic" demoted from objective to constraint** on how the objectives
are written — as an objective it was inviting creative-production reach.

**Build return states:** confirmed, needs information, raises an issue, failed,
and **done with deviation**.

**Cost-discovery loop — owed.** Build may flag that a design element is
unbuildable, unclear, or disproportionately expensive; design then resolves it.
Binder §9 (simplicity and escalation) partly covers this as scope-and-authority
but not as cost discovery. Sharpen. **Moderate.**

## Requirements

### Stage 4 — Requirements (forward-derived, accepted)

Derived forward from purpose and objectives, before reading the old design.
Written as what the component must provide or guarantee.

1. **Hold a fluid design space** — support open conversation across the full
   input set (purpose, stakeholders, outcomes, requirements, considerations,
   background, business case, prior research, methodology), with no ceremony
   blocking thinking.
2. **Converge into an accurate, actionable specification** — a guarantee of
   *placement*, not merely of capture.
3. **Never silently swallow a homeless piece** — ask, or flag that there is
   nowhere for it to live. Nothing is dropped because it did not fit.
4. **Guarantee no confirmed commitment goes undelivered** — the producer rule at
   requirement weight.
5. **Own the return from build** — reconcile the five return states; run cost
   discovery.
6. **Scale trivial to complex without changing method** — including at block
   level, with detail and language held proportional to scale.

**Deliberately excluded:** "domain-generic" (a constraint on wording, not a
requirement); "group owed work into areas / package at the seam" (a mechanism
serving requirements 4 and 5, not a requirement in itself).

## Design shape

### Stage 5 — Design shape (accepted)

**One flow, three holding places, one seam.**

- **Flow:** intent → capture and place → brief → design → commitments →
  register → handoff → build → reconcile.
- **Holding places:** brief, design, overview — plus the register, now Project
  Design's own.
- **Seam:** the design–build handoff.

Three things to specify: the **capture-and-place mechanism**; **brief-to-design
delivery and elasticity**; the **commitment-and-return loop**.

**Ordering correction (Dave, accepted — strong).** Define **the elements of a
Project Design first**. Placement is routing, and each element's definition *is*
the routing rule; capture-and-place cannot be specified without its
destinations.

## The elements of a Project Design

### The elements of a Project Design — the destination map

**Brief element blocks** (the finest-grained destinations): purpose, objectives,
requirements, considerations, scope and boundaries, target/outcome, definition
of done. Specified in the next section.

**Owned doctypes and mechanisms:** design (the current confirmed model and
approach — the delivery of the brief, authoritative, governs on conflict);
overview (project snapshot); work register (the ledger of confirmed commitments
build has not delivered); the design–build handoff and build return (transition
mechanisms, not fixed doctypes); the design inbox (entry point).

**Consumed generics:** decisions (topic-scoped reasoning), knowledge (reasoning
with no owning topic), WIP (current staging memory), open items (the ongoing
task list).

**Boundary tests — where capture-and-place has to decide.** Each brief section
now carries three fields: what it holds, its weight, and a boundary test where it
has a confusable neighbour. The four tests:

- **Objectives vs requirements.** An objective is what success looks like; a
  requirement is a condition the solution must meet to get there. "Fast" is an
  objective; "responds within two seconds" is a requirement.
- **Considerations vs decisions.** A consideration is live input still bearing
  on the design; the moment it resolves into a choice it moves to decisions.
- **Requirements vs scope.** A requirement is a condition the *solution* must
  satisfy; scope is the boundary of the *work* — what is in and deliberately
  out. "Must work offline" is a requirement; "the mobile client is out this
  phase" is scope. The tell for a confusable out-of-scope item: does it
  constrain the solution or the effort?
- **Target/outcome vs definition of done.** Definition of done is the
  completion test — the short, checkable pass-or-fail bar. Target/outcome is the
  described end state, and may be qualitative or aspirational. If it is the
  condition you check to say "finished," it is definition of done; if it
  describes what you are trying to bring about, it is target/outcome.

### Brief — section specification (settled)

The brief's job, consistent with established brief / PID / design-brief
practice: **fix the problem and the bar for success before designing.** The
failure mode all such practice guards against is solutioning too early. The
brief is the problem space; the design is the solution space. The brief must be
complete enough that the design has everything to meet, without smuggling in
solution decisions.

**Required, always — the irreducible core:**

- **Purpose** — the problem or need, and why it is worth solving. Never
  optional; without it there is nothing to design against.
- **Objectives** — what success looks like. The ends.
- **Definition of done** — the completion bar. Even trivial work needs to know
  when it is finished. **Short, accurate, concise — it is the primary success
  test.**

**Required in substance, may be light:**

- **Requirements** — the conditions the solution must satisfy. May be a single
  line, but never absent: "no stated requirements" must be a deliberate
  statement, not an omission. Register default-on logic applied to the brief.
- **Linked build project or build outcome** — which build the design feeds.
  *(Added by the binder sweep, 2026-09-07.)* Absent only where the design
  produces no build. The relationship is **many-to-one**: one build project may
  have several design projects, each managing a different area or part. It also
  gives the work register's target field something stable to point at.
  **Moderate-to-strong.** Depends on *design project* and *build project* being
  defined — a named open item.
- **Scope and boundaries** — what is in, and what is explicitly out.
  **Split out from considerations rather than folded into it —
  moderate-to-strong, accepted.** Out-of-scope / non-goals is one of the
  highest-value things a brief carries and it gets lost when buried.

**Optional, scale- and scenario-dependent:**

- **Considerations** — constraints, background, stakeholders, business case,
  prior research, methodology in the area, assumptions, risks. The context bag;
  flexes hugest with scale.
- **Target / outcome** — the intended end state and any acceptance criteria.
  **Kept separate from definition of done — accepted.** Rationale: definition of
  done is specific and focused, the primary success test; target/outcome is
  elaboration and broadening. Different jobs, so they do not collapse.

Seven sections: three hard-required, two required-in-substance, two optional.
*(Eight after the binder sweep added the linked build project/outcome, which is
required in substance. The linked build project property depends on "build
project" being defined — currently deferred, with topic-root documentation as the
direction. See the design-project and build-project section below.)* The brief scales by which sections are present and how
deep each runs — the block-level scaling rule doing its work inside the brief
itself.

**Fifth boundary test — added by the binder sweep, 2026-09-07.** A **requirement**
states what the outcome must satisfy and stays **distinct from an implementation
choice**. The classic failure is a requirement written as "use X" rather than
"must achieve Y", which pre-decides the design inside the brief. That runs
directly against Project Design's purpose — fluid in, precise out — because a
solution smuggled into the brief closes the fluid space before it opens.
**Strong.** By the Standards principle (needed at the moment of application), it
goes into the brief standard as well as the design.

### Design document — definition and reasoning routing (settled)

**Definition.** The Design is the current confirmed model and approach — the
authoritative *delivery* of the brief. A point-in-time snapshot of what is true
now; it must be **sufficient on its own** to produce outcomes, and it **governs
on conflict**. For Project Design specifically, that delivery *is* the tools and
standards that define and provide the AI-to-AI infrastructure — the Design is
not prose about a solution, it is the producer of the payload other components
run on. It is therefore the **primary source for the build handoff**, which is
built from it.

**Design carries its own live "why" inline (settled).** The Design holds not
just the what but the rationale for the approach chosen — the live slice of
reasoning relevant now. This gives context and makes Design genuinely
self-sufficient for the handoff. **Duplication with Decisions is accepted and
expected.** This honours the already-locked authority clause: "reasoning
pertinent to a current design choice belongs in Design."

- **Design holds the live why** — the rationale for the current approach.
- **Decisions holds the fuller why** — the evolutionary record, including paths
  not taken and reasoning that no longer bears on the current snapshot.

**Every design-element change is a retention checkpoint (settled).** When a
design element changes, anything removed from Design must be checked to survive
in Decisions; if not, it is added *before* the removal stands. This is the
locked content-removal trigger — the "moment of loss" — pointed at the document
most likely to churn.

**Decisions/knowledge routing is a producer obligation.** Because the Design is
only a snapshot, the reasoning behind each tool and standard choice is not in it
and is lost unless captured as the design is worked. The locked Decisions and
Knowledge rules (see §7) are *placed into* the design workflow — not changed:

- **Same-pass rule** — a design change and its reasoning are produced together;
  reasoning is never left to live only in conversation.
- **Retention chain** — conversation → WIP or Working → Decisions/Knowledge,
  promoted as the design is confirmed.
- **Triggers** — confirmed design position changes; a requirement established or
  materially revised; a credible alternative rejected; formative reasoning that
  shaped understanding; content removed or replaced (check it survives
  elsewhere, capture if valuable).
- **Split** — topic-scoped reasoning to Decisions; homeless reasoning to
  Knowledge.
- **Authority** — Decisions and Knowledge inform; they never override or
  supplement Design as the executable authority. Design governs on conflict.

The single thing this *adds* to the locked definition is placement, not change:
the producer of a design change owns producing its reasoning entry, the same
shape as the work-register producer rule. **Design and its reasoning are one
obligation, not two.**

### Overview — required and advice (settled 2026-09-07)

Refines the Overview section above into the same criteria-plus-advice shape as
the design doctype. The purpose, register and Summary-suppression material there
stands unchanged.

**Required:** key objective; the chosen approach or delivery method; the
top-level model; key defining principles.

**Advice:** project-level scope and boundaries, where a reader would otherwise
misjudge the edges.

**Register:** statements, not explanation. Each entry is a **recall handle** with
the detail reachable on demand. Brevity is a strong benefit but never bought at
the cost of what the Overview must contain.

**Elasticity:** inline for small projects, and while inline the host document
carries no Summary; when it splits out, the source document gets its Summary
back. For a single-document project, Overview and Summary are the same artefact.

### Overview and Summary — the relationship (locked)

They do not make each other redundant, but no document ever carries both.

- **Summary** — the document's TLDR, held inside the document it describes.
  Key model, key points, defining items; stated, not explained.
- **Overview** — the whole project's snapshot, standing above the document set.
  Typically somewhat larger than a Summary, because it carries the project
  rather than one document.

**The suppression rule — strong.** While an Overview lives inline in a document,
that document does **not** also carry a Summary; the Overview is already doing
the orienting job at a superset level. The moment the Overview branches out to
its own document, the source document **gets a Summary back** — a shorter,
document-only TLDR. One in, the other out.

**Small-scale collapse.** Where a project is a single document, the Overview and
that document's Summary are the same artefact, not two.
**Moderate-to-strong.**

**Edge to keep clean when Standards is worked (flagged, not resolved):** Contents
and Summary both feed the read-decision from different angles — Contents maps
*what is where* to judge relevance; Summary gives *what the document
establishes*. Their edges need to stay distinct. This does not affect Overview.

### Work item and work register — distinct in kind (settled 2026-09-07)

They were briefly collapsed — register entries treated as work items that had
reached a committed state — and that was **wrong and is not the model**. There is
**no subset relationship and none should be implied.**

- A **work item** is a generic entity flowing through a workflow: raised, judged,
  given a fate. Broad, any-source, any-side.
- A **work register entry** exists *because a design change had a downstream
  impact that has not yet been delivered.* It is produced by the
  consequence-capture rule, not by something being raised. Different origin,
  different purpose, different owner.

Collapsing them would erase exactly the meaning that makes the register worth
having.

**Name reviewed and kept.** With the meaning locked, the name was reopened and
tested — delivery register, obligations register, consequence register, impact
register, pending work register. *Obligations* was rejected as too amorphous to
state plainly what the thing is, which is Dave's own plain-language rule applied
to our own naming. **Work register** stands: concrete, side-neutral, and it reads
cleanly as *the register of work owed* now that work item and work register are
firmly separated. **Moderate-to-strong.**

**Consequence for the binder sweep.** Any surviving build-side "work package"
should be renamed **build package**, so the word "work" is left free and the two
never collide. The work-package doctype is being retired in that sweep anyway.
**Strong.**

### Work register — definition (settled 2026-09-07)

**Owner: Project Design.** The register is the one artefact where **design is
both source and target** — the only thing Project Design both produces and
consumes — which is why its states must reconcile against build return.

**What it holds.** Confirmed work owed and not yet fully delivered. **Not ideas,
not maybes** — those are work items and go to open items or stay in
conversation. **Default-on**; non-use must be stated explicitly.

**Entry — required fields:**

- **Source** — the design element or decision that committed it.
- **The commitment** — what was committed.
- **What must change** — the required output or implementation change.
- **Target** — where the change lands.
- **State.**

**Entry — advice fields:** handoff reference, return reference, **area**.

**Writing rule — logical blocks of work (settled 2026-09-07, strong).** Items go
to the register as **logical blocks of work** — coherent wholes that mean
something on their own terms, each individually completable or completable
together. Design does the chunking **at the point of writing the entry**, not
afterwards when a partial return forces the question. The axis is *coherence,
not build-effort sizing*; completability tends to follow from coherence rather
than needing to be aimed at separately.

This is what dissolves partial coverage. There are **no child items and no task
tree** — the register stays flat and every item is atomic: owed or discharged.
Build may take items singly or swallow several in one handoff, since build owns
units of work. If an item cannot be completed by one handoff, that is a sign
design wrote it too coarse, not a call for rollup machinery.

**Area — a flat optional label (settled 2026-09-07, strong).** An item may carry
an area. An **area is a label, not a container**: areas do not own items, have no
states, are never completed, and nothing rolls up. It exists so design can hand
off a coherent bundle and so the register can be read by theme rather than as one
long list. Design does the labelling because design holds the coherence view that
build does not. This delivers stage 2 objective 4 (design groups owed work into
areas; build decides units of work) at almost no cost and cannot grow into a
hierarchy.

**States — four:**

1. **owed**
2. **handed off**
3. **returned, pending reconciliation**
4. **reconciled**

**Mapping to the five build-return states:**

| Build return | Register consequence |
|---|---|
| Confirmed | Reconcile and close. |
| Needs information | Back to owed; the issue becomes a work item for design. |
| Raises an issue | Back to owed; the issue becomes a work item for design. |
| Failed | Back to owed. |
| Done with deviation | Returned-pending; design decides whether to accept. Accepting is itself a design change, which produces a new commitment. |

**Invariant — build never closes a register item. Strong.** Design owns closure
because design owns the commitment.

### Superseded register items — the handoff is the immutability boundary

**Not yet handed off (owed).** The entry is mutable. Superseded → amend in place.
No longer relevant → remove it; removal is a retention trigger, so the withdrawal
and its reason go to decisions in the same pass.

**Already handed off.** The entry's description of the work owed is
**immutable — absolutely.** It is the record of what crossed the responsibility
boundary and nothing may rewrite it.

**Everything else is a design judgement.** A fixed procedure was drafted here —
freeze the entry, raise a superseding entry, notify build, reconcile — and
**withdrawn**. The right answer genuinely varies: build might have finished the
work, not started it, or be halfway through, and the remedy might be stop work,
let it complete and amend after, or accept what lands and adjust the design. A
fixed rule would get most of those wrong.

**So the requirement is narrow and strong: design determines the impact and the
remedy, makes the call explicitly, and records it.** Not that it follows a set
path. The register carries the outcome of the call; the reasoning goes to
decisions.

**Advice, not procedure:** a superseding commitment usually wants its own entry;
telling build sooner is usually better than later.

*Noted: this is the first time facilitate-not-constrain changed a decision rather
than sitting inert in this document.*

## Mechanisms

### Design–build handoff — the bridgehead (settled)

**The work-package doctype is withdrawn as a fixed artefact.** It was designed
very early in the original AI-workflow implementation to meet a real
requirement, and has never been reviewed since. Replaced by the **design–build
handoff**: a transition point whose mechanism is deliberately *not* fully
defined and which varies by build context.

**The invariant is the responsibility boundary, not the artefact.** Project
Design owns through to the work register; the handoff is where responsibility
crosses to build.

- **Design must not overreach into build — even in the same session. Strong.**
  The transition point exists precisely to stop design running, controlling or
  managing build. Design produces what build needs; build works; build comes
  back if it needs to. Same session or not, the routing point is the same and
  the separation of responsibility holds.
- **Shape varies with scenario** — a one-line message for trivial work, a full
  package for complex work; it may not physically move at all when design and
  build share a session; it changes with the build product, the tooling and the
  environment (chat → Cowork or Code).
- **Multiple builders.** One design may hand off to several builders for
  different components or elements, each returning independently across the same
  bridgehead.
- **Sufficiency is the one firm requirement. Strong.** Whatever crosses must
  carry everything the build side needs to act without returning to the design
  conversation. **Format free, sufficiency required.**
- **Sufficiency has a ceiling as well as a floor.** *(Added by the binder sweep,
  2026-09-07. Moderate.)* Do **not** re-supply generic execution-platform
  knowledge the build environment already provides — the toolchain, the repo
  conventions, the language. The handoff carries what is specific to *this* work.
  A floor with no ceiling pushes toward bloated handoffs, which costs real
  context when they are AI-written and AI-read. Same shape as the Standards
  principle: what goes in is decided by what is needed at the moment of
  application.

### Build return — transactional by default (settled, strong)

**Every build handoff expects a build return.** A confirmation of the work is
the default, because without it there is no reliable transactional system —
nothing can establish that a handoff completed.

- **Fire-and-forget is allowed but must be explicitly declared** in that
  workflow, at the point the handoff is created. Same shape as register
  default-on: the safe state is expected-return, and the exception must be
  stated, never assumed.
- A handoff and its return are a **matched pair**. An open handoff with no
  return is an incomplete transaction the system should be able to see.
- **Return states** (from stage 2): confirmed, needs information, raises an
  issue, failed, done with deviation.
- **Naming — moderate-to-strong:** *build handoff* outbound, *build return*
  inbound. Both deliberately format-free.

### Capture-and-place — the filing obligation (settled 2026-09-07)

**Reframed at the outset of this pass.** An earlier framing treated this as a
workflow-entity question — capture as an act, placement as a fate, the work item
as its subject. That was wrong and was dropped. The real thing is narrower and
more useful: **a Project Design conversation wanders** — tangents, triggers,
exploration, alongside focused work on a topic — and the AI's job is that nothing
said gets left where it fell. Each thing that emerged gets put where it belongs.

**The requirement, in the director's words:** he stays focused on the knowledge
and on working the item, issue, idea or concept, trusting the AI to file
everything necessary in the appropriate place, with **no valuable knowledge
lost**.

**Three obligations on the AI. One on the director: none.**

1. **Continuous capture, silently.** The moment something in the conversation
   settles, shifts or is raised, it is noted against a destination — *then*, not
   at session end. Nothing is held on the strength of "I'll remember." This is
   the part that fails if left late: in a long chat the early material drifts out
   of reach and a session-close sweep recovers only what is still visible.
2. **Placement by the destination definitions.** Settled things go to a permanent
   home — the **brief** if problem-space, the **design** if solution-space,
   **decisions** if it is topic-scoped reasoning, **knowledge** if it is
   reasoning with no owning topic. Unsettled things go to a holding place — **WIP**
   for live thinking, **open items** for a parked question, the **work register**
   for confirmed work owed. The four brief boundary tests (objectives vs
   requirements; considerations vs decisions; requirements vs scope;
   target/outcome vs definition of done) are **tie-breakers inside the brief, not
   top-level choices**.
3. **Batched surfacing at natural breaks.** What was captured and where it is
   going is put in front of the director in plain language; he agrees or
   corrects; only then is it written. The existing no-output-until-agreed
   standing rule already does this job — no second mechanism is needed.

**The director may override any placement at any time — "that's a decision",
"don't keep that" — but never has to. If he says nothing, it still lands.**

**Two safety rules underneath:**

- **Homeless pieces are named, not dropped.** Anything that cannot be placed is
  surfaced in the batch rather than quietly left out. Where there is genuinely
  nowhere proper, the **interim-placement rule** applies: place it sensibly for
  now and raise a review task against Project Design. *(This closes the
  interim-placement item by absorption.)*
- **Err toward over-capture.** Cheap to delete in review, expensive to lose.
  Including tangents that went nowhere: the *reason* a line was abandoned is
  often the keepable part, and that is a knowledge entry rather than a deletion.

**Accepted weak point:** the AI's judgement of what counts as valuable. That is
the risk the director is knowingly accepting; over-capture is the mitigation.

**Batch triggers — inherited, not invented.** The three session-transition
commands already recorded (full stop; checkpoint and continue; flush without
closing) are the batch triggers. Capture-and-place does not need its own break
points. Each implies a different batch: full stop flushes everything including
loose ends, checkpoint flushes plus produces the handoff, flush-without-closing
writes and carries on. **Added:** when a topic closes mid-chat, the AI offers the
batch unprompted rather than waiting for a command — this keeps batches small
enough to review. **Strong.** *(Dependency, not a blocker: the commands themselves
are designed in Working Practices; capture-and-place works whatever they end up
called.)*

**Placement defers to the destination's own standard for content. Strong.**
Capture-and-place routes to a destination; the destination's standard says what
belongs in it. This mechanism holds **no guidance of its own** about what a
decisions entry or a brief section should contain — that would be a second source
of truth competing with the standard and rotting against it. Until the standards
exist, the definitions in this WIP serve; the standard supersedes once authored.

**Struck:** the expectation that this session would surface the **work item type
list**. That expectation came from the dropped framing. The type list stays with
Working Practices, to be surfaced when the work item is designed there, or left
unenumerated if nothing demands it (demonstrated-need rule). **Moderate-to-strong.**

### The commitment-and-return loop (settled 2026-09-07)

Delivers **requirement 5** — Project Design owns the return from build, including
cost discovery. The circuit: a design change produces a **commitment** (register
entry, *owed*) → **handoff**, responsibility crosses → build works → **build
return** in one of five states → **reconciliation** → the item closes, or the
return provokes a design change which produces fresh commitments.

**A. The escalation boundary — what comes back.**

Design owns the *what and why*; build owns the *how*. The test is one question:
**does what build encountered change what is being delivered or why, or only how
it gets delivered?** How is build's call. What or why comes back.

The old binder §6 of the Project Design binder (the section on simplicity and
escalation, numbered §9 there) enumerated instead: objective, major scope,
acceptance, ownership, architecture, policy. **That enumeration is demoted to
worked examples; the single test is the rule. Moderate-to-strong** — a list is
arguable at the margin and rots as the system grows; a test does not. Same move
as facilitate-not-constrain made on the design doctype and on superseded register
items.

**Tiebreak — if build cannot tell which side it is on, it returns. Strong.** An
unnecessary return costs a message. Silently absorbing a design change costs the
design's authority, and is exactly the silent-swallowing failure this component
exists to prevent. Cheap error one way, expensive the other, so the default is
deliberately asymmetric.

**B. The cost-and-complexity flag** *(this discharges the owed cost-discovery
item)*.

Something that looks simple in design can turn out complex in build. Rather than
build persevering and silently carrying that cost, it flags: *this is looking
more extensive and complicated than it probably seemed from the design side — do
you want to review the design elements, or are you happy to proceed?*

- **What is being protected** is the *value-versus-cost* judgement, and that
  judgement is design's, because only design holds the why.
- **An obligation, not a threshold. Strong.** When the real cost or complexity
  **materially exceeds what the design appeared to assume**, build surfaces it
  before proceeding. No number, no how-long-is-a-piece-of-string test — just the
  duty to flag, and build's own judgement of "materially". A rule with a number
  would be exactly the friction facilitate-not-constrain exists to remove.
- **A flag with a default of proceed, not a return. Strong.** If design does not
  intervene, build proceeds. The loop keeps moving; it does not choke waiting for
  permission on every bump.
- **Deliberately unshaped, with a review hook.** Demonstrated-need applied to
  itself: ship the obligation, watch how it behaves, and shape it only if the
  flags come too often (false positives) or too rarely (missed flags). Do not
  pre-engineer a threshold that is not yet known to be needed.

So build has **two distinct reasons to come back**, crossing the same bridgehead
at different weights: a **return** for a genuine what/why question it cannot
resolve, and a **flag** where it *can* proceed but the price has moved.

**C. Reconciliation — defined as an act.**

- **Who:** design, always. Build reports; design decides.
- **Against what:** the original commitment — what the register said was owed.
  Not "did build do something", but "did build do *the thing that was promised*".
- **What "reconciled" asserts:** the commitment is **discharged** — delivered
  reality now matches the design and nothing is left owed on this item. This is
  the word that makes the register trustworthy: if it meant "build said done",
  the register would be build's opinion; meaning "design confirmed the promise is
  kept", it is a reliable statement of what has actually been delivered.
- **Definition (strong):** reconciliation is design's act of checking a return
  against its commitment and deciding the outcome — **close it, accept a
  deviation, or send it back to owed**. One act, three endings.
- **It fires on two return states only.** *Confirmed* — check and close.
  *Done with deviation* — design must decide whether the deviation is acceptable;
  accepting is itself a design change and may spawn a fresh commitment; rejecting
  returns it to owed. *Needs information*, *raises an issue* and *failed* deliver
  nothing, so there is nothing to reconcile — the item stays owed and routes back
  into the design conversation.

**D. Return sufficiency — the mirror of handoff sufficiency.**

The handoff must carry everything build needs to act without returning to the
design conversation. The return must carry everything **design** needs to
reconcile without going back to build. **Sufficient out, sufficient in**, each
defined by what the *receiving* side must do without re-crossing. Insufficient
information is not a valid return — it collapses into *needs information* and
comes straight back.

- **Never bare. Strong.** "Done" is not a return. "An issue occurred" is not a
  return. Every return carries a real description of what was actually done, or
  what actually prevented it — **accessible and comparable** so design can hold
  it against the commitment.
- **Attribution on failure. Strong.** A failure has two possible origins and the
  return must say which: **design-side** (unbuildable, unclear, conflicting —
  design's to resolve) or **build-side** (a configuration, environment, file or
  tooling fault that has nothing to do with the design being wrong). The response
  differs completely: a design fault re-enters the design conversation; a
  build-side fault means the design is fine — retry or fix the environment,
  nothing for design to rework. **Selectivity is allowed** on deep internal build
  faults: build reports enough to establish *it was build, not you*, without
  necessarily exposing the whole internal cause.
- **Proportional to the task. Strong.** A trivial task delivered by a one-line
  message earns a brief return; a high-impact, high-risk, critical task earns
  fuller reporting, because design has a heavier decision to make. Sufficiency is
  never a fixed volume — it is "enough for design to make *this* decision about
  *this* task."
- **Review results ride in the return.** Where the work was reviewed, the return
  says so and carries the result. A review is evidence bearing directly on
  whether the commitment is genuinely met, so it belongs in the return rather
  than in a separate channel.

**E. Partial coverage — dissolved, not mechanised.** See the register writing
rule above: items are written as **logical blocks of work**, no children, no
tree. A return covering less than an item is not a partial-coverage case — it is
*done with deviation* or an issue, and reconciliation already handles it.

**F. Convergence — no mechanism. Moderate.** A return can provoke a design
change, which spawns commitments, which spawn handoffs, one of which raises
another issue. Nothing terminates this, and nothing should: **every trip round
the loop is provoked by something real**. If issues keep coming, the loop is not
failing — the design is being told something. The goal is not the loop stopping
but **the register emptying**, which happens when nothing is owed. The only
addition is **visibility**: an item that has been round the loop several times is
a design smell worth surfacing — usually the design is wrong at a level above the
item. Not blocked, not stopped, just visible.

## Rules and positions

### Design is the default (settled 2026-09-07)

**Authored forward, not derived from the old corpus.** Recorded per the rebuild
method: an old-corpus item is a *source of knowledge*, never a thing to modify
in place. The old decision D15 ("design is knowledge, not a mandatory document
pipeline") is reference material for reasoning already explored — it is not
carried forward, amended, or downgraded. If its reasoning holds anything not
captured here, it comes back through the omissions sweep.

**The position.** A design almost always exists, and a standard almost always
has a design behind it. Authoring straight to a standard with no design is the
**exception, and it has to justify itself** — taken only where genuinely
everything worth recording fits the standard without compromising either
document.

**The reason it holds.** The standard is deliberately lean and functional
because it is memory-resident and applied alongside many others. The design is
descriptive and complete. Force everything into the standard alone and one of
the two is compromised: either the standard bloats past the conciseness gate, or
the design's reasoning and elaboration are simply never recorded. There will be
very few cases where all the information worth recording could sit in the
standard alone. **Strong.**

### Design doctype — criteria and advice (settled 2026-09-07)

**The atomic unit.** A design element is a **two-part unit: the statement of what
is true, plus its inline why.** A separate reasoning block was considered and
rejected — the reading pattern demands the why *at* the element, and inline is
what makes the retention checkpoint (above) a natural act rather than a
bolted-on chore.

**Why this is criteria and not a schema.** Design composition varies a great deal
by project type and by the nature of the build outcome. So the doctype describes
a **base framework and methodology**, to be implemented as appropriate provided
it meets the published criteria and considers the recommendations. This is the
**facilitate-not-constrain** position doing its work: AIDE exists to facilitate
and empower, not to constrain or be a source of friction. **Strong.**

**Required — the design is not done until all eight hold:**

1. **It delivers the brief** — every requirement is addressed, or explicitly
   deferred or rejected with a reason.
2. **It is sufficient alone** to produce the outcome.
3. **Every element carries its why inline.**
4. **It states the model.**
5. **It states its boundaries** — what it does not cover, and where it hands off.
   This is what makes handoff sufficiency checkable rather than a matter of
   opinion.
6. **Workflow, behaviour, methodology rules and guidance are recorded in it.**
7. **It is current state** — no superseded content left standing.
8. **Its thinking is routed to decisions and knowledge as produced** — the
   producer obligation, not a later sweep.

**Added by the binder sweep, 2026-09-07 — a ninth required property. Strong.**

9. **Current design contributions do not conflict materially.** Where several
   current contributions bear on the same outcome, they are reconciled **before**
   handoff. **Build is never handed a choice between unresolved designs** — that
   is a design act and it does not cross the bridgehead. Recovered from the old
   binder's many-to-many contribution model, which the forward design had no
   equivalent for.

**Advice — considered, not imposed:**

- Group elements as model / rules / definitions / boundaries.
- Lead with the model before elaborating.
- **State the model compactly before elaborating it; if it will not state
  cleanly, the model is wrong, not the write-up.** *(Added by the binder sweep,
  2026-09-07 — the old binder's two-layer design checkpoint, compressed to its
  operative test. Moderate. The six-stage review procedure already builds this in
  for component work; this covers every other design.)*
- Link elements back to brief items where the connection is not obvious.
- Include a worked example where the rules are abstract.

**Traceability — the coverage check (strong).** Per-element links back to
requirements were rejected as overkill: the links rot on every edit and the
maintenance cost buys little. Replaced by a **coverage check run once, when the
design is called done** — walk the brief's requirements and confirm each is met,
deferred or rejected. Criterion 1 above is what that check tests.

### Component-ownership boundary — reworked (governing test)

The first allocation pushed too much into Working Practices, which was becoming
a dumping ground for other components' specifics. **Test adopted** (the
provider–consumer test Documentation Methodology already uses):

> **Does the thing exist and carry meaning outside Project Design?**

Yes → it is generic and lives with the generic owner. No → it belongs to Project
Design.

Applied:

- **Work register — comes HOME to Project Design. Strong.** The temporal gap it
  fills between design and build only exists *because* Project Design owns both
  ends of the loop. Splitting the producer rule from its own ledger was the
  mistake.
- **WIP — stays generic (Working Practices). Strong.** Any session stages
  thinking, including code and build sessions.
- **Open items — stays generic. Moderate-to-strong.** Build is the proof case:
  build sessions accrue deferred sub-tasks and follow-ups, which is an
  open-items list, not WIP staging.
- **Decisions and Knowledge — stay generic. Moderate.** Provisional home Working
  Practices; confirm when that component is worked.

**Three placement bands:**

1. **Universal grammar** → Documentation Methodology.
2. **Generic operating behaviour and live state** → Working Practices.
3. **Component-specific** → the component itself.

## Definitions

### Design project and build project — defined 2026-09-07

**Design project** is the scope of one design: a brief and the design that
delivers it, together with the commitments that design has entered into the work
register. **A naming convenience for a boundary that already exists**, not a new
entity, container or doctype; it owns nothing new. If it starts acquiring
properties — a state, an owner, a lifecycle — that is the signal it was a
mistake. One topic may hold several design projects; no conflict with the topic
hierarchy.

**Build project** — deferred under the demonstrated-requirement rule. The brief
carries a **plain identifier** for its linked build project; the definition
question waits until something demonstrates the need. **Recorded as the
direction** (not settled): the build project's identity is documented at the
**root of the topic** that holds its designs, which is where the old corpus put
it via the topic-root Index. That direction depends on the **Index doctype**,
which is unreviewed in the rebuild, and sits next to the parked **domains**
question.

**Finding behind the deferral:** the build project is defined *nowhere* in the
current corpus. Build's binder has **Build Target** (a producer-side output
requirement, explicitly not a repository or project) and pushes Target
Definitions out to "the specialised producer/domain". AI Deployment has
**Deployment Target** (the install realisation). The old model carried the
design-to-build linkage through the transient WorkPackage, so nothing durable
holds it.

**Cardinality:** many-to-one is the common case (several design projects feed one
build project). Many-to-many is allowed — a design handing off to several
builders is already in the model. The brief names the build project; the specific
outcome per handoff is what the work register's target field carries.

**Structural knowledge captured from the director (not yet placed as decisions):**
topics group documents and are hierarchical; a topic may hold several designs; a
build project may have several design projects, each managing a different area or
part; a brief is the root of a design (stated tentatively — sits close to what is
settled but "root" adds a hierarchy claim those do not make; open).

### Project Design doctype set as it now stands

**Owned:** brief (composite block, mandatory), design, overview, **work
register**, plus the producer rule. The **design-build handoff** and the **build
return** are owned transition mechanisms rather than fixed doctypes. *(The design
inbox is retired — replaced by the work item, a generic owned by Working
Practices.)*
**Consumed generics:** decisions, knowledge, WIP, open items, **work item**,
**definition of done**.
