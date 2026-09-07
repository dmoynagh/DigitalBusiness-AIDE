# AIDE_Documentation Binder

> **Generated Binder - do not edit directly.** Edit the individual master documents
> and regenerate the Binder.
> **Binder Version 5** (2026-09-08).

This Binder is a current-context consumption artefact; authoritative masters remain
individual files.

## Binder manifest

- `_rebuild/AIDE_Rebuild_Guide_v1.md` - sha256 `01ceb45e507b`
- `Principles/Principles_Decisions_v4.md` - sha256 `2c31c26b5c66`
- `Principles/Principles_Design_v4.md` - sha256 `4bd5797d3d2e`

---

<!-- BEGIN SOURCE: _rebuild/AIDE_Rebuild_Guide_v1.md -->
# AIDE Rebuild — Guide

Version 1. 2026-09-08. Unmanaged working document.

What this is: a review of the rebuild as it stands at WIP v22, read against the design
approach agreed on 8 September, the handoff analysis of 3 September, and the old corpus
binders. It says what is working and must be kept, where the work has drifted and how to
put it right, and the route to continue on. Written to be argued with once, then acted on.

How it was produced: the rebuild WIP read in full; the design-approach WIP; the handoff
analysis; the Principles binder; the outlines and key sections of the Core, Working
Practices, Build and Capabilities binders. Findings carry a strength. Where a finding is a
matter for your call, it says so.

The single-sentence version: **the rebuild has produced good design and no overview,
and it is still building the machine before living with the framework.**

---

## 1. What is right — keep, and make load-bearing

These are the things that are carrying the rebuild. They should be named as its method,
not left implicit inside a 3,400-line working document.

- **Two phases, one test.** Confirm what a component is for and how it works until it is
  clear and effective; then read the old material as a source and carry only what earns a
  place. Presence in the old version proves nothing. And the check on Claude: if the
  old-material pass produces a long list of calls for you, the design review was not
  finished. *Strong. This is the method.*
- **Tests over lists.** The escalation boundary is one question (does this change what or
  why, or only how). The brief's boundary tests separate confusable neighbours. The rule for
  what goes into a standard is "needed at the moment of application". Each of these replaced
  an enumeration, and each is better for it because a test does not rot. *Strong — make it
  an explicit house rule for every component.*
- **The hole-not-a-carry rule.** An old item that only earns its place under an assumption
  the confirmed model does not state is a hole in the design, not a carry. This is the
  design-check skill's "can it be placed?" question, discovered independently. *Strong.*
- **Obligations with a default, not thresholds.** The cost-and-complexity flag: build has a
  duty to flag, judges "materially" itself, and proceeds if design does not intervene. No
  number. *Strong.*
- **Ownership designation at definition time.** Defining any doctype or block type names
  its owner and residence. *Strong.*
- **Block-level portability.** Define logic as block types; promote to generic only on
  demonstrated shared meaning. Lowers the stakes on every ownership call. *Strong.*
- **The three-layer output** — design (elaboration and reasoning), decisions (the thinking),
  standard (lean, memory-resident, cross-reviewed by a separate AI). *Strong.*
- **Naming what already exists rather than inventing.** Pending content is capture-and-place
  output, named. The design project is a naming convenience, not an entity. *Strong — and
  the test that came with it is worth keeping: if a naming convenience starts acquiring
  properties, it was a mistake.*
- **Facilitate, not constrain** actually changed a decision (the superseded-after-handoff
  rule became a judgement, not a procedure). That is the sign it is a real principle.

---

## 2. Findings

Ordered by consequence. Each states the finding, the evidence, and the recommendation.

### F1 — The rebuild has no overview. Strong.

**Finding.** Check 1 of the design approach — is the overview complete enough that the layer
below could be executed excellently from it by someone not in the conversation — has never
been run on the rebuild as a whole. The sections that would be the overview (the lifecycle
model, the design half, AIDE's scope and containers, structure versus transport) have read
"unchanged from v2, not yet written up" since the start and were downgraded to documentation
debt at v10. The handoff analysis recommended a periodic one-page restatement of the model
"as if from scratch, no history" on 3 September. It has not been done.

**Consequence already visible.** Four separate items in the WIP are one gap: cross-component
wiring "never reviewed as a whole"; the build project found defined nowhere, by accident;
three candidate components whose survival depends on a demonstrated need there is nowhere to
demonstrate; Working Practices drifting back toward a dumping ground through one-at-a-time
"provisional" placements. Each is the missing overview showing through.

**Recommendation.** Write the rebuild overview before Standards. One page. Purpose; the
component list with purpose lines; how the components wire to each other; the generic
things every component consumes; what sits outside AIDE. A draft skeleton is in section 5
so this starts from something rather than nothing. Cross-review it with a separate AI — it
is the highest-value artefact the rebuild will produce.

### F2 — The settled material contradicts itself, and stays labelled settled. Strong.

**Finding.** The component purpose-line table (item 7, recorded as complete and settled) says
Project Design "does not need to know about build" and that "handover mechanics belong to
working practices"; that Working Practices owns "work registers"; and that Standards "owns
use, application, and migration of standards" while Migration is listed as its own
component. The Project Design pass then settled the opposite on all three: Project Design
owns both ends of the loop, the handoff, the return and the register. Both positions stand
in the same document with no amendment note on the table.

The v21 register error had the same shape — a claim carried unchanged, never tested against
the new model, then quoted back as settled.

**Recommendation.** Two things. First, when something is superseded, strike it; do not
annotate around it. A document that holds both positions will be quoted back wrong. Second,
the purpose-line table is rewritten once, against the overview, as part of F1 — it becomes
the overview's component list. The stale rows are Project Design, Working Practices,
Standards and Migration.

### F3 — The machine is still being built before the framework is lived with. Strong.

**Finding.** The handoff analysis's central argument was that the framework and the machine
that produces it are two products, the second was built first, and Stage 0 — hand-deliver
the content and live with it for two weeks — was the strong recommendation. The rebuild's own
standing driver says the same: standards and behaviours should be live in your sessions.

What the rebuild has done since: settled change management end to end (500 lines,
twenty-three requirements, scored) before a single standard exists in the new form; built a
tool pipeline as a gate before the first master; scoped a Stage 0 deliverable and not
delivered it. Meanwhile the one thing that did go live — the design-check skill — was
hand-authored in an hour, deployed at account level, and is already changing how this
session is run. It is the first empirical evidence the rebuild has produced about its own
deployment model, and it came from Stage 0 thinking, not from the pipeline.

**Recommendation.** Make "live in a session" part of every component's definition of done,
alongside standard authored and cross-reviewed. Author Principles' and Project Design's
standards at deployable length and deploy them by hand the day they land — a skill, or a
line in instructions — before their production chain exists. Treat the design-check skill as
Stage 0's first delivery rather than a side project, and add to it as standards land. This
is the handoff analysis's recommendation, one week later and still right.

### F4 — Change management is well designed and probably ahead of need. Moderate-to-strong; your call.

**Finding.** The section is closed, coherent, and its thirty-second statement is good. Two
things weigh against it. It was settled before Standards was defined, before Documentation
Methodology was reviewed, and before the overview existed, so it has not been checked for
proportion against anything above it. And its own account of the old model's failure is that
"the mechanism was designed, declared fifty-five times, and never asked to do anything" — a
full detection-and-execution model is being re-designed for a mechanism that has never run
once. The rebuild's own policy is demonstrated requirement, and the sledgehammer judgement
was applied to Deployment for exactly this reason.

**Recommendation.** Keep the model statement and the migration-record shape (condition,
action, success check; every version has a record; ships with the standard) — that is the
portable asset and it costs nothing to carry. Defer the detection and execution machinery
until one standard has actually changed version after being deployed, then build what that
event shows is needed. If you disagree, record it as a decision; the design is sound enough
that the cost of being early is bounded.

### F5 — Verification is unowned. Moderate-to-strong.

**Finding.** The handoff analysis named verification — checkable claim, probe, evidence — as
the significant under-engineered area and its first open question. The rebuild does not
mention it. Since then the rebuild has had two corpus-integrity incidents of exactly that
kind: a version written to disk before its batch was agreed (v15), and a carry recorded as
settled that was never tested (v21). Neither would have been caught by review, because both
read fine.

**Recommendation.** Name the owner when Working Practices is worked. WP4 (verify inspectable
facts) and WP5 (distinguish generated intent from applied state) already exist there and
are the seed; P9 and P10 are the premises. It may be one working practice, not a component.
Decide it deliberately; do not let it stay homeless.

### F6 — Nobody owns the context budget. Moderate.

**Finding.** Also from the handoff analysis, also unaddressed. The binder set is 1.4 MB; the
old Documentation Methodology standard alone ran to roughly 700 lines. The rebuild's
"needed at the moment of application" test and the lean-standard bar go some way, but
nothing owns how much AIDE material may be resident at once, and the current project context
holds thirteen old binders plus two versions of the WIP.

**Recommendation.** Standards owns the deployable-length budget for a standard. The
always-on budget across standards is a Core question and can wait for Core — but the
overview should name it as Core's, so it is not lost.

### F7 — The old corpus is loaded into the project that is doing the design. Moderate-to-strong.

**Finding.** The handoff analysis: "Do not hold design conversations in a project loaded
with the superseded corpus. The new project should carry binders only, with older material
available on request." The rebuild's own method says shaping should not be done inside a
context loaded with the old corpus. This project's knowledge holds the full old binder set
and two WIP versions. Every design answer is being generated with the old material in reach,
which is the anchoring the method exists to prevent.

**Recommendation.** Remove the old binders and the superseded WIP from project knowledge.
Keep them in the repo; fetch a specific binder when the old-material pass for that component
runs, then remove it again. Project knowledge should hold: the current WIP, the
design-approach WIP, this guide, and the new masters as they land.

### F8 — Component count against a solo developer. Moderate; your call.

**Finding.** Thirteen settled components, Core and Deployment deferred, three candidates.
Five of the thirteen are ways of involving another AI — Review, Research, Parallel
solutioning, Consultation, Messaging — and three of those were added new during a rebuild
whose policy is demonstrated requirement. The standing rule that mode and interaction pattern
are separate axes already frames these as modes of one thing.

**Recommendation.** Test each against "have I actually done this in the last month". The
consistent shape under the rebuild's own rules is one component for working with external
AIs, with Review, Research, Parallel solutioning and Consultation as its modes, and
Messaging as the transport underneath. That is an option, not a finding; the split costs
little now and the overview is where to decide it.

### F9 — The working document has become the persisted memory. Strong; mechanical.

**Finding.** 210 KB, 3,440 lines, twenty-two nested version summaries before the contents.
The model says the working document is the staging buffer and the binder is persisted
memory. The pending-content rule says settled content waits under its destination document.
Neither is being applied to the WIP itself.

**Recommendation.** Split it once, mechanically, in Claude Code:

- Settled Project Design content → a pending-content file per destination master (design,
  decisions, standard-inputs, register), ready to become the masters.
- Settled rebuild-wide content (doctype model, block catalogue, versioning, format, change
  management, decisions doctype) → one "settled rebuild decisions" file, to be mined when
  Documentation Methodology and Standards are worked.
- The WIP keeps: purpose, method, the overview once written, current position, open items,
  next actions. Under 500 lines. Version note: one line, current version only — the
  rebuild's own Version Note block definition says exactly this.

### F10 — Provisional placements are piling up in Working Practices. Moderate-to-strong.

**Finding.** Carried to Working Practices "provisionally" or "to confirm when worked": WIP and
open items; decisions and knowledge ownership; shaping behaviour; the no-knowledge-lost
rule and its three behaviours; session-transition commands; the nomination model; the
six-stage procedure; P6 and Guidance Profiles; the work item; definition of done; the
pending-content rule. The design-approach WIP adds the overview-first working behaviour as an
open ownership call. The WIP itself notes Working Practices "was becoming a dumping ground".

Two of these already have homes in the existing Working Practices design and were not
reconciled before being proposed: **WP7 — work in layers before detail** is the overview-first
behaviour; WP8, WP12 and WP13 are the no-knowledge-lost behaviours. The reconcile-before-
proposing rule applies to the design-approach placement plan too.

**Recommendation.** Stop placing one at a time. When the overview exists, allocate the whole
list in one pass against the three placement bands. Start the Working Practices pass from
WP1–WP13, and treat each provisional item as a candidate against them: confirmation,
contradiction, or genuinely new.

### F11 — The six-stage procedure is the apparatus the design approach replaces. Moderate-to-strong.

**Finding.** It was demoted to a "silent checklist" at v21 and still reads "adopted, general"
in the Project Design section. The design-check skill's two checks — is the overview complete
enough; does the design hold against it — do the same job with no stages, and they are what
this session is actually running.

**Recommendation.** Retire the six-stage list. Per component: confirm purpose and
objectives; write the component's overview; run Check 1; design; run Check 2; author the
standard; cross-review; deploy; then the old-material pass. That is the method restated
with the checks in it, and it is short enough to hold.

### F12 — The design-approach value claim is P3 and P4 sharpened, not a new premise. Moderate.

**Finding.** The placement plan proposes the top-two-levels claim as a new Principles premise,
with a check that it does not duplicate the model-before-machinery premise. Read against the
binder: P3 (state the model before building machinery on it) and P4 (keep the working set
human-comprehensible; layered progression — intent, then model, then detail) already carry
it. What the 8 September session added is the strength of the claim and the two checks.

**Recommendation.** A decisions entry strengthening P3 and P4, not a tenth premise. The checks
go to Project Design's standard as planned. Principles' element list stays at nine.

### F13 — Small closures the model already settles. Moderate each.

- **Register admits confirmed non-design work: yes.** The register's gap is temporal —
  confirmed, not yet delivered — and origin is not part of that definition. Old D12 said
  the same.
- **Difficulty-as-evidence — one home.** State it once in Project Design's commitment-and-
  return section; the build-side cost-and-complexity flag is its consumer. Do not restate it
  in Build.
- **The design-check skill's permanent placement:** Project Design, as its standard's
  deployment output. Confirm when the standard is authored; nothing to do before.
- **The language profile:** retire it. The four language rules in the design-approach WIP
  are what survives, and they go to Documentation Methodology as grammar.
- **Decision identifiers collide across corpora.** A reference crossing threads names its
  corpus. Documentation Methodology's, low weight, note it and move on.

---

## 3. Reshaping the work done

In order. Each names the surface.

1. **Strip project knowledge** (you, manual). Old binders and WIP v20 out; keep them in the
   repo. F7.
2. **Split the WIP** (Claude Code). Per F9. Strike superseded text rather than annotating it.
   Rewrite the version note to one line. Run version cleanup. This is the pipeline's first
   real use.
3. **Write the rebuild overview** (chat, with you). Start from section 5. Probe the
   boundaries, look for silences, read the model back. Run Check 1. Cross-review with a
   separate AI. F1.
4. **Rewrite the component list against the overview** (chat). The purpose-line table
   becomes the overview's component list; stale rows corrected; the collaboration-component
   question and the three candidates decided or explicitly deferred with a trigger. F2, F8.
5. **Run Check 2 over Project Design's settled elements** (chat, Claude runs it, findings
   listed). Each element placed against its own model — one flow, three holding places, one
   seam — and against the overview. Expected findings: difficulty-as-evidence duplicated
   (F13); capture-and-place's three obligations checked for proportion; the pending-content
   rule and the work item placed outside Project Design's model and noted as Working
   Practices dependencies. Nothing rewritten; findings only. Then the coverage check against
   the six requirements.
6. **Allocate the provisional Working Practices list in one pass** (chat), against WP1–WP13
   and the placement bands. F10.

None of this reopens settled design. It is placement, reconciliation and housekeeping.

---

## 4. Continuing the rebuild

### The per-component method, restated with the checks in it

1. Confirm purpose and objectives. The purpose line is a filter, not a description.
2. Write the component's overview — its model and approach on a page.
3. **Check 1.** Could the design be executed excellently from this overview by someone not in
   the conversation? If not, probe; do not descend.
4. Design. Derive from the model, not from single requirements. Commit within the model;
   surface only forks the model does not settle.
5. **Check 2.** Each element: placeable, context in its own description, proportionate,
   derived from the model. Coverage check once against the objectives. Anything that does
   not trace is listed as an addition.
6. Author the standard at deployable length. Cross-review by a separate AI.
7. Deploy it by hand — skill, instruction line, whichever fits. Live is part of done.
8. Old-material pass: Claude runs it against the confirmed design; carries with reasons,
   contradictions, holes returned to step 4. Fetch the old binder for this pass only.

**Definition of done for a component:** doctypes and block types defined with owners;
workflow and behaviour recorded in the design; thinking routed to decisions and knowledge;
standard authored, cross-reviewed and live in a session; old-material pass complete.

### Sequence

1. Standards next — it unblocks Principles' and Project Design's sign-off, and the authoring
   bar, the application-time test, the deployable-length budget, the Contents/Summary edge
   and the cross-review step are all inputs already recorded. Its overview should be short:
   what a standard is, how it is authored, how it is applied, how it is kept current (the
   migration-record shape from F4, the rest deferred).
2. Author and deploy Principles' and Project Design's standards. Stage 0 begins here.
3. Working Practices — absorbs the provisional list, the design-approach working behaviour
   (as WP7 strengthened), the human working model from the handoff analysis, verification's
   home (F5), and the session-transition commands.
4. Documentation Methodology — the grammar; the doctype and block model, catalogue,
   versioning, format and language rules are already settled and mostly need placing.
5. Build, then the collaboration components, then Deployment when Stage 0 has shown what it
   needs, then Core last.

### Standing checks, for Claude, every session

- Orient before starting: what this is, why now, your role, what done looks like.
- Read the design-check skill before any design output; run Check 2 before you see it.
- Reconcile against settled material before proposing — including against the existing
  Working Practices and Principles, not only the WIP.
- If the old-material pass is producing a long list of calls for you, stop; the design
  review was not finished.
- When something is superseded, strike it.
- Say once if the model looks wrong, then move on when you have heard it.

---

## 5. Draft rebuild overview — a skeleton to complete, not a proposal to accept

Assembled from the settled purpose lines, the Core binder's system boundary, and the Project
Design pass. Silences are marked as questions; they are the probes to run first.

**Purpose.** AIDE makes the standards and behaviours that shape how AI works with you live in
your sessions, on whatever surface is in use. Everything else exists to produce, deliver and
keep current that content.

**The model — what kind of thing AIDE is.** A set of components, each owning a purpose, a
design, its decisions, and a lean standard that is loaded into AI sessions. Components
consume a small set of generic things (documents, live-state artefacts, principles). A
production path takes each standard from design to a deployed form. Development projects
consume AIDE; they are not part of it.

**The components and their purpose lines.** The thirteen settled lines, corrected per F2 —
Project Design owns both ends of the design-build loop; Working Practices owns generic
operating behaviour and live state, not the register; Standards owns application and
currency; Migration is either Standards' mechanism or a component, decided here.

**How they wire — the flow.**
intent → Project Design (brief, design, commitments) → handoff → Build → return →
reconcile. Standards and Principles are loaded into every session and shape all of it.
Review and the other collaboration modes can be invoked at any point. Documentation
Methodology is the grammar everything is written in. Deployment takes standards live. Core
holds what has no other home.

**What every component consumes.** Decisions, knowledge, WIP, open items, work item,
definition of done; the doctype and block model; the binder; versioning.

**Outside AIDE.** Which binders exist and what they contain; project repositories and their
lifecycles; platform behaviour, which is verified not assumed.

**Silences to probe (Check 1).**
- Is Migration a component or a Standards mechanism?
- What is the relationship between Standards and Tools, and where does the deployable-length
  budget live?
- Where does verification live?
- How does a session know which components are loaded — is that Core, Deployment, or the
  binder?
- Is there one collaboration component or five?
- What is a build project, and does anything depend on the answer before Build is worked?
- What does Deployment's Stage 0 actually consist of now that one skill is live?

When those are answered, read the model back. If the shape holds, Check 1 passes and
Standards can start.

---

## 6. What this guide does not do

It does not reopen settled design. It does not propose new mechanisms — every action above
is placement, reconciliation, or applying a rule the rebuild already holds. Where it
disagrees with a settled position (F4, F8), it says so once and leaves the call with you.
<!-- END SOURCE: _rebuild/AIDE_Rebuild_Guide_v1.md -->

---

<!-- BEGIN SOURCE: Principles/Principles_Decisions_v4.md -->
# Principles — Decisions

> **Version 4** (2026-09-08). Authored fresh in the AIDE rebuild. Compacted
> from v3 where decisions still stand; new decisions added from the design pass.
>
> Created: 2026-08-27 | Last modified: 2026-09-08

## D1 — Principles is a top-level topic, independently deployable

Principles is a cross-cutting concern applying to every project and scenario.
It is a top-level topic, not a subtopic of anything else. The standard works
both as part of AIDE and on its own, because base reasoning guidance is useful
in general AI sessions that are not doing full-AIDE work.

## D2 — Principles is base guidance, not a personalised configuration

The standard defines the portable default. Putting user or team preferences
directly into the base was rejected because the base would stop being portable
and every consumer would inherit one party's local choices.

## D3 — Principles and Working Practices are sibling concerns

Working Practices is not a child of Principles. Principles owns judgement
premises; Working Practices owns practical cross-surface collaboration and
operating conventions. Both can be independently useful.

## D4 — Guidance Profiles use a delta model, housed in Working Practices

Guidance Profiles may add, refine or explicitly override named base guidance
using small deltas. Unmentioned base guidance remains effective.
Equal-specificity contradictions fail visibly unless explicitly ordered.

No generic profile component is created yet — Principles and Working Practices
are the demonstrated consumers, and wider generalisation waits for evidence.

The profile mechanism and its review are housed in Working Practices. The open
question is whether the model earns its place for a solo developer — review
starts from these decisions (formerly D4 and D5).

## D5 — Portability is the defining test, meaning universality

A premise belongs in Principles only if it holds outside AIDE. Anything true
only inside AIDE drops to methodology or working practices. "Interaction"
premises qualify — a universal interaction premise is still a principle. The
real filter is "independent of platform or methodology."

Adopted during the rebuild design pass (2026-09-07) to make the existing
implicit test explicit.

## D6 — The information-holder boundary premise moved to Working Practices

The old P6 ("information holder decides the boundary") was about which
component, project or domain should answer a boundary question — AIDE-context
behaviour, not a universal premise. It fails the portability test and moves to
Working Practices.

## D7 — Authoritative evidence replaced declaration-over-inference wording

The original seed said "Domains are declared, not detected." The confirmed
model now permits implicit resolution from recognised authoritative structures.
Replaced with "authoritative evidence over incidental inference" — the deeper
intent (rejecting accidental presence or proximity inference) is preserved, the
rigid declaration-only rule is not.

The premise's AIDE-specific examples (declared relationships, folder proximity)
are demoted to illustration beneath the premise statement, so they do not read
as part of it.

## D8 — Operational seed behaviours moved without loss

Concrete behaviours from the original seed — coded-reference glossing,
verification before assertion, no-silent-state-change behaviour and others —
are represented in Working Practices. They remain valuable but are operational
conventions rather than root reasoning premises.

## D9 — Definition of done identified as a candidate premise

Definition of done has been promoted to a generic block type owned by Working
Practices, carrying a testable-or-assessable invariant. Whether it also earns a
place as a Principles premise is an open question — it reopens the Principles
element list once Working Practices completes its definition.
<!-- END SOURCE: Principles/Principles_Decisions_v4.md -->

---

<!-- BEGIN SOURCE: Principles/Principles_Design_v4.md -->
# Principles — Design

> **Version 4** (2026-09-08). Authored fresh in the AIDE rebuild from the
> confirmed design pass. Not a modification of v3 — the previous version is a
> source of knowledge only.
>
> Created: 2026-08-27 | Last modified: 2026-09-08

## Brief

**Purpose.** Define the durable, portable reasoning and interaction premises
that guide how any AI reasons, designs, challenges and chooses an approach —
independent of platform or methodology.

**Objective.** Produce a lean, deployable standard that works as part of AIDE
or on its own.

**Defining test.** Portability, which means universality: does the premise hold
outside AIDE? If it only makes sense inside AIDE, it is not a principle — it
belongs to methodology or working practices.

**Definition of done.** The standard exists, passes the portability test for
every premise it contains, is lean enough to be memory-resident alongside other
standards, and covers only premises that earn their place.

---

## Model

Principles is **base guidance** — the default reasoning premises that apply
when no more specific guidance is in effect. It is a top-level cross-cutting
concern and can be deployed independently without full AIDE.

The premises are durable. They change rarely and only on evidence that a premise
is wrong, missing or has been overtaken. Each premise carries its own rationale
so the reasoning is visible without reaching for a separate document.

The standard is the deployable output; this design document is the internal
authority for future change.

---

## Premises

### P1 — Value over compliance

Everything in the system exists to create value for the person doing the work.
Rules are justified when they protect something important, preserve integrity or
enable a capability. Rules for their own sake create friction.

*Test:* what does this enable, and what does compliance cost? Persistent routing
around a rule is evidence the rule or its model should be re-examined.

### P2 — Purpose before mechanism

Ask what something is for before deciding how it works. A mechanism with unclear
purpose cannot be evaluated properly. Purpose settles whether a thing should
exist; mechanism settles how.

*Failure mode:* structural or model problems being answered by adding mechanism.

### P3 — Model before elaboration

State the model before building detailed machinery on it. Elaboration should be
checked against a visible model rather than gradually replacing it.

*Failure mode:* detailed mechanisms make an average or misunderstood premise look
settled merely because later work depends on it.

### P4 — Keep the working set human-comprehensible

The active conceptual working set should remain small enough for the human owner
to hold and challenge at once. Too much detail too early does not only slow
work — it removes the human from meaningful design participation.

Use layered progression: intent and premises, then model, then detail.

### P5 — Authoritative evidence over incidental inference

Prefer explicit declarations and authoritative structural relationships over
conclusions drawn from mere presence, proximity or naming coincidence. Inference
is valid where the governing model explicitly defines what authoritative
evidence supports it.

*Illustration (AIDE-specific, not part of the premise):* a solution's declared
or member-project relationship is authoritative evidence; files merely sharing a
folder do not become related by proximity.

### P6 — Observation over prediction

Design mechanisms against demonstrated problems and repeated failure modes
before adding enforcement for hypothetical ones. Leave room for foreseeable
future capability without building unused machinery prematurely.

### P7 — Loud failure over quiet absorption

When authoritative completion is not possible, stop or surface the unresolved
condition clearly. Do not turn uncertainty, missing information or contradictory
authority into output that merely looks complete.

Failure messages should guide remediation.

### P8 — Verified truth over plausible assertion

Where a fact depends on records, environment state or another authority, verify
it when reasonably available. If it cannot be verified, identify the uncertainty
rather than manufacture a plausible value.

### P9 — Confirmed state over assumed state

Actions that materially change state must not be silently treated as completed
when they were only proposed, generated or handed off. State changes should be
confirmed by the authority, tool or environment that can actually perform or
observe them.

---

## Boundary with Working Practices

Principles states judgement premises. Working Practices states concrete
collaboration and operating conventions that may implement those premises. Both
are top-level sibling concerns — neither is a child of the other.

*Test:* a principle says what underlying premise should guide judgement. A
working practice says how to practically work, communicate or hand over.
Operational conventions stay in Working Practices even when motivated by a
principle.

---

## Guidance Profiles

Guidance Profiles are moved to Working Practices for review there. The concept
is not abandoned — the decisions behind it (the delta model, no generic profile
subsystem yet) travel with it. Review starts from the existing decisions and
asks whether the profile model earns its place for a solo developer.

This design records only that the mechanism exists and is housed elsewhere.

---

## Open items

- **Definition of done** is identified as a candidate premise. It has been
  promoted to a generic block type owned by Working Practices with a
  testable-or-assessable invariant. Whether it also earns a place as a
  Principles premise is open — revisit when Working Practices completes its
  definition.

---

## Intended output

Produce the standard `AIDE_Principles` — short, portable, platform-neutral,
independently deployable. The standard is authored separately once the Standards
component defines its form.
<!-- END SOURCE: Principles/Principles_Design_v4.md -->
