# AIDE_Documentation Binder

> **Generated Binder - do not edit directly.** Edit the individual master documents
> and regenerate the Binder.
> **Binder Version 8** (2026-09-08).

This Binder is a current-context consumption artefact; authoritative masters remain
individual files.

## Binder manifest

- `_rebuild/AIDE_Component_PurposeLines_v2.md` - sha256 `b1836489f28b`
- `_rebuild/AIDE_Rebuild_Guide_v1.md` - sha256 `01ceb45e507b`
- `_rebuild/AIDE_Rebuild_Overview_v1.md` - sha256 `5a65c44f5991`
- `_rebuild/AIDE_Rebuild_SettledDecisions_v1.md` - sha256 `33593102e982`
- `_rebuild/ProjectDesign_Decisions_Pending_v1.md` - sha256 `647aacf4c1ad`
- `_rebuild/ProjectDesign_Design_Pending_v1.md` - sha256 `587bc4c6165f`
- `_rebuild/ProjectDesign_StandardInputs_Pending_v1.md` - sha256 `710b74bb0958`
- `_rebuild/ProjectDesign_WorkRegister_Pending_v1.md` - sha256 `638ebbfb6eef`
- `Core/Core_Brief_v1.md` - sha256 `6c2e6280ea89`
- `Core/Core_Design_Documentation_Working_v1.md` - sha256 `b2999c523397`
- `Principles/Principles_Decisions_v4.md` - sha256 `2c31c26b5c66`
- `Principles/Principles_Design_v4.md` - sha256 `4bd5797d3d2e`

---

<!-- BEGIN SOURCE: _rebuild/AIDE_Component_PurposeLines_v2.md -->
# AIDE Component Purpose Lines

Version 2. 2026-09-08. Rewritten against the rebuild overview per finding F2. Supersedes the item 7 table in the WIP.

---

## Active components

| # | Component | Purpose line | Key boundaries |
|---|---|---|---|
| 1 | Principles | Give any AI the durable, portable reasoning and premises to think and act well — independent of platform or methodology. | Portability is the defining test. Includes verification as a premise and the base human-side behavioural premises. |
| 2 | Working Practices | Own the conventions and behaviours for how an AI and user actually work together across surfaces. | Includes the human working model as its own standard. May grow into a container with sub-components. |
| 3 | Documentation Methodology | Define how documents are structured and created — the generic mechanics. | Owns the grammar. Not a registry of types belonging to other components. Specific types live with whoever knows the most. |
| 4 | Project Design | Produce the design specification. | One scalable architecture. Owns both ends of the design-build loop: handoff, return, reconciliation, and the work register. |
| 5 | Build | Take the design specification and execute it — produce the outcome, report what was done. | Creates from the spec, thinking not transcribing. Owns how code is structured. Likely an umbrella with different build paths. |
| 6 | Standards | Make sure standards are applied, honoured and kept current across the environment. | As a capability, owns the definition of a standard and the authoring guidance including leanness. |
| 7 | Tools | Encapsulate a repeatable, named, invokable action so its mechanism does not have to be re-derived each time. | Owns the definition of a tool. Individual tools are owned by their consuming component. |
| 8 | Migration | Keep things current when something they depend on changes — collate, distribute and execute change actions. | Detection varies by consumer; the mechanism is generic. Documents against standards is the primary consumer. |
| 9 | Messaging | Carry a message across any boundary reliably, with a known envelope and delivery convention. | General-purpose transport. Any component or logic can use it. External AI and Code handoffs are consumers, not owners. |
| 10 | External AI | Bring another AI into your work — review, research, parallel solutioning, or consultation. | Modes, not separate components. Consumes Messaging. Mode is the contract; interaction pattern is a separate axis. |
| 11 | Deployment | Get the publishable capabilities live in a session, on whatever surface is in use. | Simple pipeline: build into a plugin, push to marketplace, account reloads. Includes the deployable-length weight gate. |
| 12 | Core | Hold whatever shared requirements have no natural home elsewhere. | Deferred by design, resolved last. Carries the settled Index, Domain and Bootstrap work forward. |

## Held — resolved by demonstrated need

| Candidate | Original rationale | Resolution trigger |
|---|---|---|
| Tags | Removed duplication of labelling behaviour across components. | Reappears if the new design shows the same duplication. |
| Scope | Removed duplication of applicability-decision logic. | Reappears if runtime applicability needs a shared definition. |
| Dependencies | Removed duplication of dependency-declaration behaviour. | Reappears if multiple components need a shared dependency methodology. |

## Deferred

| Concern | Reason | Trigger |
|---|---|---|
| Environment and platform concerns | Single platform, no current need. | Multi-platform deployment or a need to track deployed state. |
<!-- END SOURCE: _rebuild/AIDE_Component_PurposeLines_v2.md -->

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

<!-- BEGIN SOURCE: _rebuild/AIDE_Rebuild_Overview_v1.md -->
# AIDE Rebuild — Overview

Version 1. 2026-09-08.

---

## Purpose

AIDE makes the standards and behaviours that shape how AI works with you live in your sessions, on whatever surface is in use. Everything else in AIDE exists to produce, deliver and keep that content current.

---

## The model — what kind of thing AIDE is

AIDE is a set of components. Each component is a defined area of functionality with a declared purpose, scope and ownership. A component owns its own documents and decisions.

Some components produce capabilities — standards and tools that are delivered into the AI environment. A capability is a component whose purpose is providing a mechanism by which functionality is delivered to the AI environment. Producing capabilities is not a requirement; a component that exists solely to organise and govern a body of work is still a component.

There are two types of capability:

- A **standard** defines rules, expectations, guidance and context that shape decisions and behaviour while work is being done. It can include procedures, but those procedures are guidance within the operating context rather than a separately invoked operation.

- A **tool** encapsulates a repeatable, named, invokable action so its mechanism does not have to be re-derived each time. It normally defines its inputs, preconditions, ordered procedure, decision points, escalation conditions, outputs, and failure behaviour.

Standards and tools are defined platform-neutral — the what — and transformed into platform-specific delivery. On Claude, that means a skill in a plugin.

A third kind of repeatable operation exists outside the AI session: a **utility** encapsulates a repeatable operation that acts on the corpus, environment or infrastructure from outside the session. It does not load into session context or shape in-session decisions. Examples: the binder-builder, the file-update packager, version-cleanup scripts. Utilities are not capabilities.

**Leanness is a governing principle.** Everything deployable — standards, tools, anything that loads into a session — is written as lean as possible without compromising its purpose or outcomes. The cost of length is baked into authoring from the start: the standards for building standards and building tools carry the discriminating guidance on how to write lean. A weight gate at deployment checks the combined load of a plugin and flags if the total is getting too big.

---

## The components

Twelve components, listed by the work they do.

### Foundations

**Principles** gives any AI the durable, portable reasoning and premises to think and act well, independent of platform or methodology. Portability is the defining test — if a candidate principle only makes sense inside AIDE, it is not a principle. Verification lives here as a premise: where possible, build in mechanical verification so claims and outcomes can be checked against inspectable evidence. The base premises about how the system behaves on the human side also live here.

**Working Practices** owns the conventions and behaviours for how an AI and user actually work together across surfaces — work in progress, handoffs, preservation of active state. The human working model — tiering, per-item confidence, the assumptions and gap-fill report, drift detection, definition-of-done at commission time — is a standard within Working Practices. The per-user override model is a future direction only; single user for now.

**Documentation Methodology** owns how documents are structured and created — the generic mechanics. Naming, document types, lifecycle, the master-versus-generated distinction, the doctype and block model, format, versioning, language rules. It is the grammar everything else is written in.

### The design-and-build path

**Project Design** produces the design specification. One scalable architecture from simple single-document to complex multi-document structures. It owns both ends of the design-build loop: the handoff to Build and the return and reconciliation. It defines its own block types (objectives, requirements, considerations) and document types.

**Build** takes the design specification and executes it — produces the outcome and reports what was done. It creates from the specification, thinking rather than transcribing, and owns how the code is structured. Build is likely an umbrella with different build paths depending on what is being produced — code projects, standards, tools — each potentially its own path.

### Capabilities

**Standards** makes sure standards are applied, honoured and kept current across the environment. As a capability, it owns what a standard is and how one is authored — including the authoring guidance that enforces leanness.

**Tools** owns what a tool is — the definition, shape and authoring guidance. Individual tools are owned by the component that needs them.

### Shared mechanisms

**Migration** owns the generic mechanism for keeping things current when something they depend on changes. It collates and distributes change actions (the migration record, accumulation, shipping the fix with the thing it serves) and executes them (the three-part task shape, atomic transitions, user prompt, stamp management). Detection is the one part that varies by consumer; each consumer defines its own. Documents against standards is the primary consumer, but it also covers skills, bootstraps, binder definitions, project knowledge, code project structure, and platform configuration.

**Messaging** is a general-purpose transport component — a standard for creating and carrying messages that any component or logic can use to move something across a boundary. Cross-process, cross-session, cross-AI, cross-project. It owns the envelope and the delivery convention. It does not care who uses it or why.

### Collaboration

**External AI** owns how and when another AI is brought into your work. The former separate components — Review, Research, Parallel Solutioning and Consultation — are modes within it. Mode is the contract (what role the external AI plays); interaction pattern (one-shot, multi-round, conversational) is a separate axis. External AI consumes Messaging as its transport.

### Delivery

**Deployment** takes the publishable capabilities, builds them into a plugin, pushes it to the git marketplace, and the account reloads. Deploy as each component completes, so the framework is tested in use. This is also where the deployable-length weight gate lives, flagging if the combined load of a plugin is getting too big.

### Residual

**Core** is deferred by design and resolved last. It is defined by whatever shared requirements are left that no other component naturally owns. It holds the existing settled work on the Index, Domain and Bootstrap — those designs carry forward. Core's shape is not forced until everything else has declared what it needs.

---

## How the components wire together

Intent enters through Project Design, which produces a specification and hands it to Build. Build creates the outcome and returns it; Project Design reconciles.

Principles and Working Practices are loaded into every session and shape all of it. Documentation Methodology is the grammar everything is written in.

Standards and Tools define what capabilities are and how they are authored. Migration keeps documents and other consumers current when standards change. Messaging carries structured communication across any boundary.

External AI can be invoked at any point — review, research, parallel solutioning, consultation — consuming Messaging as its transport.

Deployment takes capabilities live. Core holds what has no other home.

---

## What every component consumes

Each component uses the shared constructs already settled in the rebuild:

- documents, decisions, knowledge and WIP (the doctype and block model)
- binders (the generated consumption artefact)
- versioning
- the work item and definition of done
- principles and working practices

These are the common grammar. A component does not re-derive them.

---

## The build sequence

Standards and Tools are worked first — they define what capabilities are and how they are authored, which is prerequisite to all other component output. Their standards also carry the leanness guidance.

Then a simple Deployment component, so capabilities can be shipped.

Then deploy-and-test as each subsequent component completes its design. The sequence after Deployment follows the per-component method in the rebuild guide: purpose and objectives; component overview; Check 1; design; Check 2; author the standard; deploy; old-material pass.

---

## Outside AIDE

Which binders exist and what they contain; project repositories and their lifecycles; platform behaviour, which is verified not assumed.

---

## Open items

These are recorded explicitly as unresolved. Each has a stated trigger for resolution.

**Component boundaries and structure.** What makes something a component, where the boundaries fall, and whether components can contain sub-components. At least Working Practices and Build show signs of wanting nesting. The three held candidates also feed into this discussion. Trigger: resolve before or during the Standards pass, because the definition of a component is foundational.

**Utilities and infrastructure placement.** Utilities are defined but where they and infrastructure sit organisationally in the framework is not settled — they are currently a tack-on. Trigger: resolve when a utility needs to be built or documented and there is nowhere to put it.

**The Capability-as-deployable-unit question.** The old model had an extensive Capability Definition contract — elements, releases, production checkpoints, build target profiles. In the simplified model, does anything still own what a capability looks like when packaged? Or is that just Deployment's concern? Trigger: resolve during the Standards or Deployment pass.

**Whether domains exist as a concept.** The old model said development domains consume AIDE; they are not components of it. Whether that concept carries forward has no demonstrated need yet. Trigger: resolve if and when the relationship between AIDE and consuming projects needs to be defined.

---

## Held and deferred

**Tags, Scope and Dependencies** are held, not resolved. They earned their place in the old model by removing duplication of similar behaviour across multiple components. They come back only if the new design shows the same duplication reappearing. Resolution is by demonstrated need during component design, not before.

**Environment and platform concerns** are deferred. The old Core design held runtime knowledge of surfaces, channels, models, access references and deployed state. Single platform for now; no requirement yet to track this. Trigger: multi-platform deployment or a need to track deployment state.
<!-- END SOURCE: _rebuild/AIDE_Rebuild_Overview_v1.md -->

---

<!-- BEGIN SOURCE: _rebuild/AIDE_Rebuild_SettledDecisions_v1.md -->
# AIDE Rebuild — Settled Decisions

> **Version 1** (2026-09-08). Extracted from AIDE_Rebuild_WIP_v23 per rebuild guide F9. Settled rebuild-wide content — doctype model, block catalogue, versioning, format rules, change management, decisions doctype, and generic constructs produced during component passes. To be mined when Documentation Methodology and Standards are worked.

---

## 2b. Process scaffolding dropped (2026-09-07)

Five overlapping frames were running at once, most of them Claude's, and the
director's time was going on working out what was happening rather than on
decisions. Collapsed to the two phases above.

| Frame | Origin | Disposition |
|---|---|---|
| Six-stage review procedure | Claude | **Silent checklist.** Still a reasonable prompt list for "have we actually confirmed the purpose", but no longer tracked, and findings are not labelled against it. |
| Two-part sweep (omissions / approach) | Agreed, a genuine distinction | **Collapsed to one sweep** under the single test. The split cost more than it returned: real findings did not sort cleanly into the two halves, and the sorting was load on the director. |
| Buckets A / B / C | Claude, invented mid-sweep | **Dropped entirely.** Findings are *carried, with the reason it earns its place* or *not carried*; parked only where something genuinely blocks. |
| Three-layer authoring model | Settled by the director | **Kept.** It describes the output — design, decisions, standard — not the process. |
| The four binder-editing items | Work arising | **A list, not a frame.** Calling it one made it sound structural. |

**No completed work needs redoing.** Principles and Project Design were worked in
this order regardless; only the labelling changes.

---

## 6a. Infrastructure — the payload boundary

Payload = Standards, Tools, guidance loaded into the AI to shape behaviour (Capabilities).
Infrastructure = machinery that acts on the corpus and is never loaded into an AI session.

### Tool work done (prior session, folded in here)

Two Infrastructure utilities exist as Python, each with a design doc:

- **VersionCleanup** (`VersionCleanup_Design_v2`) — carries the "a tool cleans up after itself"
  principle and the three-form path model.
- **BinderBuilder** (`BinderBuilder_Design_v1`) — captures format, manifest, the supersession rule
  as D7 with a rejected alternative, and the ratified three-form path model.

### Tool placement (settled)

- Masters for the utilities live in an **Infrastructure** folder under the documentation root.
- Running instances are copied into an **`_tools`** folder at the documentation root — master
  versus execution point.
- These are Infrastructure utilities, NOT capability Tools. Infrastructure is machinery acting on
  the corpus, never loaded into an AI session.

### Consequence from the versioning model (this session)

VersionCleanup must be revised to understand **draft state**, not just a trailing `_v<number>`:
- group `v27-draft1 ... v27-draftN` together;
- treat flat `v27` as a different, terminal, immutable thing — not merely the highest number in the
  group;
- parse the generic `-{key}{n}` suffix and validate the key against the defined set (one member
  today: `draft`).

---

## 6c. Rebuild-wide policy — demonstrated requirement

**Set aside anything without a demonstrated requirement.** If a need surfaces, it comes back with a
reason. Applied this session to the Internal section, Temporary owner-labelled state, Overview,
Type metadata, and (pending filter) Dependencies/Tags/References.

---

## 7. Decisions doctype — CLOSED

**Done criteria:** no valuable knowledge is lost. Design + Decisions together must allow the full
development path to be recreated and understood. Framing: other docs are a snapshot of the now;
Decisions and knowledge are everything else.

Eight agreed points:

1. **Purpose broadened.** Accumulated reasoning, alternatives, learnings and decision history
   valuable to a topic's past, present and future evolution — not only the direct path to the
   current position.
2. **Knowledge boundary.** Topic-scoped reasoning goes to Decisions; reasoning with no owning topic
   goes to Knowledge. Cross-topic reasoning lives where it most applies; single record + reference
   preferred over duplication; prompt the user if in doubt.
3. **Two new triggers.** (a) investigation/reasoning that shaped understanding whether or not it
   produced a decision; (b) content removed or replaced in any document — check it survives
   elsewhere, capture if valuable. Trigger (b) makes supersession an active checkpoint.
4. **Immutability relaxed.** Compaction allowed — consolidate duplicates, merge related reasoning —
   provided substance survives and temporal reference is retained where sequence affects
   interpretation. Changing a past decision's meaning is a new decision, not compaction. A
   cumulative log is not required.
5. **Authority tightened.** Design must be sufficient alone to produce the outcome; reasoning
   pertinent to current design choices belongs in Design. Decisions informs but does not override
   or supplement Design as executable authority. Design governs on conflict.
6. **Retention chain.** Conversation to WIP/Working to Decisions. Reasoning is persisted to WIP or
   Working when those update, then promoted to Decisions as Design is confirmed. Same-pass rule
   retained.
7. **Scope follows Design.** Absorbed into parent when Design merges; may split when Design splits
   and volume warrants. Split by closure state, not chronology.
8. **Exclusions unchanged.** Editorial, formatting, metadata, migration, mechanical maintenance
   alone do not create an entry.

Two variants drafted (in transcript): a fuller design-length definition, and a standard-length
version roughly half the length (rationale stripped, operative rules kept) for use inside a skill.

---

## 8. Doctype / block-type model — AGREED

Terminology change: "doctypes and sections" becomes "doctypes and block types." A block is a subset
of document content that may span one or more sections. Sections remain the unit of navigation,
storage and organisation.

Four rules:

- A **doctype** is the root definition for a document; states what it defines and which blocks it
  includes.
- A **block** is a named content definition mapping to one or more sections; blocks may include
  other blocks; composition recurses; no cycles.
- **Shared content is a block, not inheritance.** Universals live in a common block that doctypes
  include.
- **One source of truth.** Content defined in one place. Flag ambiguity rather than resolve
  silently.

Also: hosting rules attach to the block, not the section — one authoritative instance per semantic
scope, permitted hosts owner-defined, moves between hosts are structural not semantic. Contiguity
of a block's sections is a default, not a rule.

**A doctype includes a block as defined; it does not modify it.** A doctype may not suppress a
block's fields, add fields to it, or otherwise adjust its shape on inclusion. Defining a derived
block type that overrides a base is the same design in another form and is equally excluded. Where
two doctypes need different shapes, those are two blocks, which may share a smaller common block —
composition, not override. Added on review (v8): override-on-include is inheritance under another
name and brings back what the cuts below removed — precedence when two doctypes adjust the same
block differently, drift when the base changes underneath, and a reader unable to tell what shape a
block actually has here. The accepted cost is duplication between near-identical blocks, which is
visible; override chains are not. Revisit on a demonstrated case per §6c (the demonstrated-
requirement rule).

**Cut as over-engineered:** multiple doctype inheritance, abstract doctypes, block self-assignment
to doctypes (push model), collision precedence machinery (most-specific / last-declared). Residual
collision rule: doctype defines resolution if needed; otherwise flag to user.

DocMeth owns the doctype/block structure, how to use and apply it.

Catalogue scope: DocMeth holds only blocks common across documents or usable by any document.
Area/owner-specific blocks are defined in their topical area and merge at runtime. No central
repository.

### Catalogue preamble (rendering model)

- A block is a named set of **fields** with meaning.
- A block has a default **density**: compact or expanded. Doctype may override.
- Rendering follows the **format rendering rule**: structured formats express fields as native
  properties; prose formats express them as a heading or a delimited line.
- A block may use whatever structures suit its information (sections, tables, lists). Each maps to a
  native default in the format in use. **If anything a block defines would not port cleanly across
  formats, flag it for confirmation rather than deciding silently.**

---

## 9. Block catalogue

### Closed

**Declaration** (renamed from "preamble"). Mandatory in every governed document; its presence is
the DocMeth conformance marker and the corpus recognition mechanism. First block, fixed placement,
not overridable. Fields: title, doctype (root of the composition chain), identity, date. Density
compact. No separate version field — identity carries the version.
- Structured formats: a reserved top-level `aide` key holding the fields as sub-properties (nested,
  one level: `aide.identity`, not `aide_identity`). Presence of `aide` = governed.
- Markdown: a single delimited line, fixed field order (title, doctype, identity, date),
  delimiter ` | `. Pipe chosen over middot and semicolon: ASCII, no collision with title text, and
  it reads as structure rather than punctuation. Revisit only if a renderer treats the line as a
  table.
- The name "Declaration" lives in the methodology, not in the document; nothing emits the word.

**Header, Footer** — placement containers only, no semantics. Blocks declare they place into them
and may carry a hint. Ties resolved by doctype instruction or defined method. Containers are
themselves blocks. No literal marker line in markdown; footer start already marked by a horizontal
rule; body start is the first heading that is not Contents or Summary.

**Boundary proximity principle.** Value increases toward the file boundaries. Header runs
high-to-low from the top; footer runs low-to-high to the end (most important closest to file
start/end). Containers declare the gradient; blocks place against it.

**Version note** — metadata, top of footer (low-value end). One line, current version only, never
a list. Historical version notes do not accumulate anywhere; Decisions holds what mattered.

**Contents** — lets a reader decide whether to read the document and what it covers, at lowest cost.
Primary consumer is a file-scanning AI making a partial-read-and-stop decision; humans benefit too.
- Curated semantic map, grouped descriptive entries, not a heading repetition.
- Stable heading or section-number locators, never line numbers.
- Rendered inline / delimited, never a vertical list (expressed as density: compact).
- Placed immediately after the Declaration, before Summary.
- Included when a file-scanning agent could not decide whether to keep reading from the Declaration
  alone; doctype owners may set a per-type default.
- Doctype owner defines depth.

**Summary** — states what the document establishes, absorbed quickly.
- States the key model, key points and defining items — the substance, not a gesture at it.
- Stated, not explained. No expansion, reasoning or qualification; that is the body's role.
- The body expands, it does not restate. Re-establishing what the Summary states is a defect.
- Placed after Contents, before the body.
- Omitted only where the document is short enough that the Summary would substantially restate it.
- Doctype owner defines applicability and depth.
- Default exclusions: Decisions, WIP, WorkRegister, OpenItems, Index, structured data.

**Body** — the document's substance.
- Every governed document has a body; the only mandatory content block.
- Holds the authority; body governs on conflict with Summary.
- Expands what the Summary states; does not restate it.
- Structure is doctype-defined; the block model imposes no section shape.
- Everything not claimed by another block is body (default host).
- Density expanded.

**Dependencies** — the standards this document is built on, and the version of each it was last
brought into line with. Closed this session; resolved by the change-management work (§11a).
- Field form: a flat list of `standard@version` pairs, one entry per standard.
- Contents: direct and inherited standards alike, listed explicitly and not distinguished. Flat and
  self-contained so detection reads one field and needs no graph walk.
- The version is a **conformance stamp** — what the document reached — not a constraint. No presence
  levels (`!`, `!!`) and no exact pins (`@!vN`); those were runtime-availability concerns and belong
  to deployment currency, which the change-management work separated out.
- A document does not list its own identity's standard; identity carries that version.
- **Placement: header, immediately after Declaration, before Contents.** Moved from the footer
  position the old model used. The currency check gates use, so a partial read from the top must be
  able to answer "may I use this" without reading to the end — which is the boundary-proximity
  principle applied to the consumer that runs first.
- Kept a separate block rather than folded into the Declaration: Declaration is fixed, compact and
  not overridable, and a variable-length list would change its character.
- Name: `Dependencies` retained over `Implements`, `GovernedBy`, `Uses` and `Conformance`. The word
  carries the necessity — the standard must be present for the document to function — which is what
  CM-Q6 (no modification where standards are absent) turns on. The value's shape changed, so no
  reader will mistake it for the old field.
- Markdown: `Dependencies: A@vN, B@vN` — pipe separates Declaration fields, comma separates list
  members, so the two header lines are visibly different shapes.
- Structured formats: a `dependencies` key as a sibling of `aide`, holding the list.

Structural blocks total four: Declaration, Header, Body, Footer. Contents and Summary place into
Header. Body is between Header and Footer.

### Parked (need a case through the filter)

**Parking confirmed this session.** These blocks exist to serve downstream machinery — drift
detection, classification, citation. Until the components that consume them come through the filter
and demonstrate the need, there is nothing to anchor the decision to; deciding now would be deciding
ahead of requirement. They return when the component that needs them does. (Dependencies has since
been closed — see above and §11a.)

- **Tags** — footer property, AIDE_Tags-owned.
- **References** — footer, citation without conformance semantics; "related reading." Was to be
  decided with Dependencies; that dependency is now discharged, so References can be taken on its
  own merits when its consumer appears.
- **Overview** — returns as a discussion. Case to test is a topic-or-corpus-scale TLDR, not the old
  document-level one.

### Set aside

- **Internal section** — purpose overlaps Decisions; old spec already warned against using it as a
  hidden second body.
- **Temporary owner-labelled state** — no current user.

### Cut

- **Type metadata** — superseded by doctype in the Declaration.

---

## 10. Versioning model — CLOSED

Applies to versioning generally; the two-rhythm split applies at the publish boundary.

- **Identity** — authoritative, in the Declaration. Carries the contract version and draft state:
  `@v27-draft2` while working, `@v27` on publish. Absence of a draft marker means published and
  immutable.
- **Filename** — informative, mirrors the identity: `_v27-draft2.md` then `_v27.md`. Never
  authoritative.
- **Draft numbering** — filename and identity both carry the draft number and match; identity wins
  on conflict. Draft numbering is optional in the scheme, on by default. Self-describing is the
  better failure mode (a file pasted without its name still states what it is).
- **Reference forms** — `@v27` resolves to the published contract; `@v27-draft` resolves to the
  highest draft present.
- **Publish** — drops the draft marker in both identity and filename; creates the immutable
  contract. Published numbers are never reused.
- **Next cycle** — opens immediately at the next integer, `@v28-draft1`. No live drafts ever sit
  under a published version.
- **`.n`** — reserved, unused. Available for minor published releases later without colliding with
  draft counters.
- **Naming grammar** — `{name}_v{integer}-{key}{n}`. Exactly one key defined: `draft`. An undefined
  key is a conformance error, not a tolerated variant. Expressed as a named token, not a hardcoded
  literal, so adding a key later is a list addition, not a grammar reinterpretation.

Design documents (and other unpublished docs) run on a single rhythm — identity and file move
together. Only published outcomes (Standards, deployed contracts) use the two-rhythm split.

Every document has an identity in its Declaration regardless of publish state; filename is
informative only. This is a corpus-integrity requirement: the filename can be renamed and is
outside the content, so it cannot be authoritative.

Versioning documentation to revise: naming grammar, publish transition, published immutability,
reference forms, `.n` reservation, draft support.

---

## 11. Format and rendering model — CLOSED

- Governed documents today are Markdown. Filename grammar fixes `.md`.
- Escape hatches already in the corpus: **Assets** (filename/format fixed by consuming tool) and
  **Unmanaged files** (held but not governed).
- Future doctypes may use other formats: machine-readable / performance docs stay Markdown; Design,
  Brief, Overview, Guides could be HTML. YAML and JSON usable as document types or embedded inside
  docs as defined by blocks.

### HTML assessment (searched this session)

The pro-HTML position is a personal opinion piece by an Anthropic Claude Code engineer (Thariq
Shihipar, 9 May 2026), not Anthropic guidance. Its argument is human engagement with long
plans/audits/reports, not machine consumption. HTML is less token-efficient than Markdown; the
"more info per size" claim is expressiveness per screen line, not tokens. Markdown is still held to
win for chained agent handoffs, short content, and git repos where diffs matter — the exact profile
of this corpus. Recommendation: no change now. HTML earns a place only for long human-facing
artefacts, e.g. a topic-scale Overview if that returns.

### Rendering model

- **Format rendering rule** (DocMeth, stated once): a block is a named set of fields; structured
  formats express fields as native properties; prose formats express them as a heading or delimited
  line.
- **Density axis:** compact or expanded, per-block default, doctype override. Compact/expanded
  render per format (markdown inline vs headings; JSON flow vs pretty-print).
- **Per-format default mapping table:** each abstraction maps to one native construct by default, so
  any block renders with zero per-block, per-format instruction. HTML defaults: fields to a
  description list (`dl`, `dt`/`dd`); compact to inline; expanded to block; header/body/footer to
  their natural HTML equivalents. A correct document needs no per-block HTML; styling
  (colour, collapsibility, layout) is separate optional polish.
- **Renderers per format** are separate specs (Infrastructure), not DocMeth core and not block
  definitions. Markdown renderer trivial; HTML renderer substantial. Build none now.
- **Portability flag:** anything a block defines that would not port cleanly across formats is
  flagged for confirmation, not decided silently.

---

## 11a. Change management — SETTLED

Reworked from a blank page this session (2026-09-06), per the brief this section commissioned in
v4. The v4 content is superseded; what survives from it is noted inline.

### The split that unblocked it

The subject had been running as one problem and behaving like a spider's web. It is three:

- **A — Change definition.** What changed, in which version, and what the fix is.
- **B — Detection.** Which documents are behind, and how that is known.
- **C — Execution.** Who applies the fix, where, when, and with what authority.

Every attempt to settle one moved the other two. The old corpus fused them as well: the Dependencies
footer line carried both a conformance fact (B) and a runtime-presence level (C). Separated, each is
tractable. **All three are now settled** (see the SETTLED headers below).

### Scope

Change management is defined **for standards**. Reuse as a general framework for other item types is
a nice-to-have, not a constraint on this design. Standard granularity also resolves the
dependency-granularity question that v4 worked twice: a document depends on a standard, and the
standard's internal doctype and block structure is the standard's own business. Same conclusion as
v4, reached as a consequence rather than a choice.

---

### A. Change definition — SETTLED

> **Publishing a standard version requires a migration record for that version. The record is a set
> of condition-to-action tasks that take a document from the previous version to this one.
> Conditions are evaluated against definitions, not inferred from document content. "No action" is
> stated, not implied. One accumulating migration file per standard, held alongside it and shipped
> with it.**

Points, each settled this session:

- **Migration is created at publish, not after.** A version is not published until its migration
  record is written. This is enforceable as a publish gate rather than remembered as a discipline —
  which matters, because the recorded failure of the old model was not bad design but that nothing
  ever executed. **The gate is a presence check** — a record exists for the version being published,
  and it is either a set of tasks or an explicit "no action." Whether the tasks are *correct* is not
  checkable by anything, which is why the check is cheap and still worth having. It lives in the
  publish operation, not in a separate tool, and **has no override**: an override would be used
  exactly when someone is in a hurry, which is when the record is most likely to be forgotten, and a
  missing record is invisible afterwards because absence looks identical to "nothing to do." The
  accepted cost is that publishing is slightly heavier every time, including for the many versions
  whose honest answer is "no action" — the right trade, since fifty-three cheap records beat one
  silently missing one.
- **Every version has a record, including "no action."** Positive declaration. Absence is ambiguous
  (nothing changed, or the author forgot); presence is a fact. Retained from the old model's
  positive-posture rule.
- **A task has three parts: condition, action, success check.** Revised on review (v8); previously
  stated as condition-to-action only, which left "succeeded" undefined and made the atomic-write
  rule rest on nothing. A standard may publish several doctypes and block types; the **condition**
  decides applicability — *if the document's doctype is X*, *if the doctype uses block type Y* — so
  one migration covers a corpus of differently-shaped documents. The **action** states the work. The
  **success check** states what must be true of the document afterwards, in terms that can be tested
  against it: field present, field non-empty, block present, block absent, value matching a pattern.
- **The success check is authored, not self-assessed.** It is written before the work is done, by
  someone other than whoever applies it, which is why it is worth more than the applier's own
  verdict — the same reason a test written before the code is worth more than one written after.
  Nothing is written to the document until every applicable task's check passes.
- **A task whose success cannot be stated as a checkable outcome is not a migration task.** That is
  the same self-test as the one below: if the change cannot be expressed this way, it is a
  restructure and belongs with a human.
- **Form: structured conditions and success checks, prose actions.** Conditions and checks are
  evaluated mechanically and must be machine-readable. Actions are carried out by an AI, so prose is
  correct — forcing them into structure would amount to building a transformation language, which is
  the over-engineering to avoid.
- **Conditions resolve against the doctype definition, never against document content.** The doctype
  definition is the only source of truth for which block types a doctype currently uses. Inferring
  block usage from what a document looks like is guesswork and breaks the fail-visibly rule.
- **Held beside the definition, not inside it.** Definitions are payload and load into sessions;
  every token counts. Migration content is read only when migration is needed. Same seam as the
  payload/infrastructure boundary in §6a (what loads into an AI session versus what acts on the
  corpus from outside). The old model already did this as `migrations.md` alongside the standard.
- **Accumulates.** Every transition from the supported baseline to current is retained, so a
  document several versions behind can walk forward step by step. Pruning is possible only once
  nothing is proven to be sitting at the pruned version — which is the one job that requires a
  wide check.
- **Ships with the standard.** Without the fix present at the point the need is detected, all
  detection can do is stop work. Detection without remedy is a blocked session, which is the failure
  mode that causes a check to be disabled.

**Consequence worth noting.** The migration file is the portable asset and the executor is a
convenience built on top of it. Every consumption path — runtime check, another repo, a batch run,
or a human reading it — reads the same file. Nothing else has to be portable.

---

### B. Detection — SETTLED

**The question detection answers:** does this document need work under the current standards, and
what work.

**Runtime is the only complete picture.** A document loaded for use is loaded with the things it
depends on; that is the only moment where document, applicable standards, their versions and their
migration records all exist together. This was the premise of the original methodology and it is
correct. It also composes without tracking: a document in a repository untouched for eight months
is checked the moment it is next used, and nobody had to remember that repository existed.

**Read is use.** If a document is read, a currency check runs.

Six detection questions were worked (numbered CM-Q1 to CM-Q6 to avoid collision with the Q-series in
§14, the rebuild-wide open questions). All six are now closed.

**CM-Q1 — which standards apply to a document?** *Settled: declaration, repaired by migration.*
Derivation from doctype is truer; declaration is the practical compromise. The known risk of
declaration is a stale association — a doctype moves from standard A to standard B and the
document's declared dependency no longer reflects reality. That is repairable by an ordinary
condition-to-action task in A's migration: *if doctype is X, add standard B as a dependency*. So
declaration stops being lossy, at declaration cost. **A corpus-wide "global action" that all
documents check regardless of standard versioning was considered and rejected** as a second
mechanism sitting permanently in the check path; the demonstrated-requirement rule (§6c) applies.
Revisit only if a case forces it.

**CM-Q2 — what was the document last brought into line with?** *Settled: the Dependencies block, one
`standard@version` pair per standard.* The document must carry this; nothing else remembers. A
single whole-document value was ruled out by the cross-standard case, where each standard is used at
its own current available version independently — one value cannot express A at v4 while B is at v6.
Conformance version and dependency declaration are held in **one field**, not two: two lists over the
same set can diverge, and a conformance entry for a standard you do not depend on says nothing.
**The field is machine-findable** — fixed header position, predictable shape — so a named-scope
operation or any later wide scan can read it without parsing whole documents. Full block definition
in §9 (the block catalogue).

**CM-Q5 — where does the wrong/old severity live?** *Settled: on the task, not the version.* The
governing test:

> **Blocking = the old shape produces a *wrong* result. Non-blocking = the old shape produces an
> *old* result.**

The user's framing was discoverability — if a change alters whether a document can be found and
used, it must be applied before use. Widened slightly: a renamed field that now means something
else, or a consumer silently reading a moved block and getting nothing, are also wrong rather than
merely dated. A release can genuinely mix both kinds; version-level severity forces the whole
release up to its most severe member, so one wrong-making change makes three cosmetic ones blocking.
This restores the old model's original task-level classification, which a later decision had moved
to release level.

**CM-Q6 — can detection run without the standard present?** *Settled: no, and that is a safety rule.*
If the standards are not present the session is operating outside the methodology environment.
That is a legitimate choice, at the user's risk — but **documents must not be modified there.**

**CM-Q3 — is a wide corpus scan part of the model?** *Settled: no.* Worked from what a wide scan
would be *for*. Three candidate purposes: correctness, pruning, planning.

- **Correctness does not need it.** An unused document has no impact whether it is ahead or behind,
  and blocking work applies before use. Read-time observation is complete for every document at the
  moment that document matters.
- **Pruning does need it** — history can only be pruned once nothing is proven to sit behind the
  pruned version, and the documents you would need to hear from are exactly the ones nobody reads.
  **Pruning is deferred**, so this purpose is not live.
- **Planning is marginal** and never blocking.

With pruning deferred, no purpose remains. **No wide scan in the model.** What is retained is the
CM-Q2 constraint that the stamp stays machine-findable, which costs nothing now and keeps the
pruning option open without retro-fitting later. The named-scope operation in execution (E5) also
provides the means to bring a defined tree fully current on demand, should pruning ever be wanted.

**CM-Q4 — what does detection produce?** *Settled: a work list, per document, at read time.* Sorting
blocking from non-blocking requires knowing which tasks apply, which requires evaluating conditions
against definitions. A cheap summary carried alongside the tasks — *does any version in this range
contain a blocking task?* — answers the cheap question without evaluating the full set.

**Accepted consequence, recorded so it is seen as decided rather than missed.** Non-blocking work is
made visible at read time, but only to whoever is reading. If nobody reads a document, nobody learns
it is behind. This is the same shape as the old model's failure, and it is accepted here for a
reason the old model did not have: the old model deferred work *silently and indefinitely* with no
way to ask, whereas here the information is surfaced every time the document is used, and
`/migrations` (below) lets the user ask deliberately. The residual — documents nobody opens — is
accepted because an unread document has no consumer to harm.

### Cross-standard dependencies — SETTLED

The case: a block type owned by standard B is used by a doctype owned by standard A, and the block
type changes.

**Standards declare dependencies on standards. Documents inherit them.** A document implementing a
doctype from A declares A, and also A's declared dependencies, including B. A change to the block
type moves B's version and produces B's migration; the document is reached through the inherited
dependency. This reuses the standards-declare-their-own-dependencies cascade already noted in v4
rather than adding a construct.

**Each standard is used at its own current available version, independently.** Not "the newest
standard wins." If B is at v6 and A still declares B at v4, the document records B at the version it
actually read the block type from — v6. A stamp claiming v4 when the session used v6 would be a lie.

**Consequence: A can be behind its own dependency without A's version moving.** The document is
internally consistent; the standards are not. This is a standard-to-standard currency problem and it
is invisible to document-level detection.

Two solutions were considered and one rejected:

- **Rejected — publish multiple versions of a standard and let documents pull the matching one.**
  Compatibility-matrix machinery, and it creates retrieval ambiguity for an AI deciding which to
  use.
- **Rejected — halt all work whenever a standard is behind a standard it depends on.** Considered
  and argued down. Any standard update would block the environment until every dependent standard
  was republished, one at a time, creating a self-inflicted outage whose only lesson is to avoid
  updating standards. It also treats every mismatch as wrong when most are merely old, which
  contradicts the task-level severity settled at CM-Q5.
- **Adopted — apply the wrong/old test to the mismatch itself.** Halt on the consequence, not the
  condition. B's migration may carry tasks conditioned on a dependent standard's behaviour — *if you
  extend this block type's X field, do this* — so A becomes detectably behind through the ordinary
  mechanism. A document loading A then gets either "A is behind, nothing applies to you" (proceed,
  flagged) or "A is behind and it affects the block type you use" (block).

**Falls out of this, flagged now to avoid surprise at format-definition time:** the condition
vocabulary must be wider than "is this doctype X." It has to express conditions about another
standard's behaviour. Cross-standard coordination lives in migration instructions, because the
standard author is the only party who knows what needs coordinating.

---

### C. Execution — SETTLED

Detection has produced a work list on a document about to be used. Six questions, all closed.

**E1 — who may act?** *Settled: authority is a filesystem fact, not a construct.* A session modifies
documents that are in the tree it is working in and writable. If a document is not writable, the
session may request a writable copy. No ownership register is maintained. A standard delivered in a
plugin is reported, never modified — its migration belongs to whoever owns the plugin and runs in
their workflow.

**E2 — what happens at the moment of detection?** *Settled: notify, then offer the choice.* The user
is told, and chooses whether and where to migrate. If migration is deferred to another session, the
resuming session simply runs detection again — no new mechanism, no state carried.

**Where deferral is permitted, the split is by what the session is about to do:**

- **Reading — may proceed on authorisation.** The migration tasks are shown to the user, who judges
  whether they affect the work in hand. The wrongness affects only what comes out, the user has been
  told what it is, and nothing propagates.
- **Writing — may not proceed.** Saving a document known to be behind authors new content under old
  rules and entrenches it, and the stamp cannot advance because no migration ran. That is not a
  deferred problem but a manufactured one — the corpus is made worse by proceeding.

The proceed-anyway decision is **session-scoped and never recorded in the document**. A persisted
override is invisible and outlives its reason. The accepted cost, confirmed on review: a document
you have deliberately chosen to leave behind will re-prompt in every new session.

**Rejected — the executor evaluates whether the pending tasks affect the work in hand.** Considered
and discarded. It is a correctness call the executor cannot be accountable for, and getting it wrong
produces a document that looks right and is wrong — the silent failure the whole design exists to
prevent. It would also require a model of what the requested work touches, which would be the
largest new construct in the design for the thinnest benefit. The tasks are human-readable and
author-written; showing them to the user puts the decision with the party who can be accountable
for it, and keeps the executor dumb (R5).

**E5 — batch and binder loads.** *Settled: detect fully, then present one decision.* Detection is
read-only (R17), so nothing prevents it running across everything before any execution happens. The
single-document case is then a batch of one — same detection, same report, same decision point, no
special handling.

**Rejected — stop mid-load, migrate, continue.** Interleaves execution with a load already in
progress, consumes context exactly where R3 says not to, repeats per affected document, and needs
re-entrancy and partial-load state. It is the option that feels most helpful and behaves worst.

**Independent of binder methodology.** How binders are built and loaded is not yet defined in the new
system, so execution does not depend on knowing a load in advance. When a migration need is
detected, the user is prompted with two questions:

| | Here | Elsewhere |
|---|---|---|
| **This document** | update in this session | new session — in chat, offer cowork or code |
| **All docs in context** | update in this session | new session — in chat, offer cowork or code |

**Defaults (confirmed):** *this document / this session* for one; *all docs / new session* for
several. Context cost scales with document count, not with the size of any single fix.

**"Docs in context" means the same thing on every surface** — documents currently loaded, evaluated
at the moment of the prompt. No accumulation, no session ledger, no tracking. A document read an
hour ago and since dropped from context is not included; it is caught next time it is read.

**Rejected — a per-surface definition of scope** (chat: context; cowork: context; code: current
repo or wherever write access exists). Two faults. It makes the same phrase mean four documents in
chat and seven hundred in code, which is the corpus sweep re-entering through a prompt option. And
it folds write access into scope, when write access is E1 authority — a gate on whether you *may*
act, not a definition of what is *in* scope.

**Named-scope operation, code only.** Scanning and migrating a whole tree, repository, or other
defined scope is a **directed command, not a detection mode** — the user names the scope, the
executor acts. Nothing runs it automatically or on a schedule. Three constraints: **scope is
explicit and never defaulted** (no implicit "current repo"); it **reports before it acts** (counts
and blocking/non-blocking breakdown, then confirmation, using the same read-only detection); and
**the ordinary execution rules apply unchanged**. This is also what would make pruning possible
later, since a named tree can be brought fully current on demand.

**Migration is an AI task on every surface.** Established on review (v8), correcting an earlier
implication. Because actions are prose written for an AI to interpret, no script can be the thing
that applies them. On code, a script is a *launcher* only: it enumerates a named scope, reads
stamps, sequences the work, collects failures and resumes. The per-document work — evaluate
conditions, apply actions, verify success checks, write — is the AI's on every surface. There is no
verification-strength difference between surfaces; the difference is only how much un-intelligent
surrounding automation exists. This also means "the executor" is one actor, not a script directing an
AI, and the stamp is written by whoever did the work, after the checks pass, in the same operation
as the document.

**Commands.** `/migrations` reports and changes nothing; `/migrate` runs the same detection then
offers the same prompt and acts. In chat and cowork their scope is documents in context, identical
to a read-triggered check — the named-scope operation stays code-only. `/migrate` reuses the E5
prompt rather than replacing it: one path through execution, two entry points. Their value is that
the user can take the initiative rather than only being interrupted, which serves R2 better than
read-triggering alone. This restores the old model's diagnostic/destructive split, which was right.
Names may be revisited if collisions appear.

**E6 — failure partway.** *Settled: transition is atomic; the run banks what completed.* Two levels,
and the distinction matters because "migration" was doing double duty:

- A **transition** is one version step (v28 to v29) containing a set of tasks.
- A **run** is the whole walk (v26 to v29), which is three transitions in sequence.

**Within a transition: all tasks succeed or nothing is written.** There is no stamp value that
describes a half-applied transition — the document is no longer v28 and not yet v29, so any recorded
version is a lie. In practice the executor works on a copy and writes back only on complete success,
so "rollback" means nothing was written; a crash mid-transition is indistinguishable from a failure
mid-transition, and there is nothing to undo. No journal or rollback mechanism is needed.

**Across a run: each completed transition is kept and stamped.** A document at v26 whose third
transition fails ends cleanly at v28, with the failure reported and its reason recorded. Discarding
banked work because a later step failed would mean repeating it on every attempt and never making
progress past one bad transition. This is the old model's stepwise-durable rule, correctly scoped.

Both rules exist to protect one property: **the stamp only ever holds a version the document
genuinely reached.**

**The stamp is written in the same operation as the transition, atomically.** Written separately, a
crash between them leaves a converged document claiming the old version, which is then migrated
twice.

---

### The model in thirty seconds

> **Publishing a standard version requires a migration record for it — condition-to-action tasks
> that carry a document from the previous version to this one, shipped with the standard. When a
> document is read, it is checked: the standards it declares, what it was last brought into line
> with, what is current. Anything that makes the old shape *wrong* is applied before use; anything
> that merely makes it *old* can wait, but is shown every time. The user chooses whether to migrate
> this document or everything in context, here or in another session. Each version step succeeds
> whole or not at all, and the stamp only ever records a version the document actually reached.**

---

### Requirements schedule

Built to score models against; scored below.

**Knowns**

- **K1.** The full dependency-and-version picture for a document exists only at runtime, when it is
  loaded with what it depends on.
- **K2.** Multiple repositories with independent lifecycles; ~790 documents growing 10–30 a week.
- **K3.** A document is composed from several definitions; those definitions are published by
  standards.
- **K4.** Shape changes are rare; improvements are frequent.
- **K5.** Standards arrive via plugins/skills the consuming session does not own.
- **K6.** Runtime observability differs per surface; startup checks are best-effort in chat.
- **K7.** The doctype definition is the only source of truth for which block types a doctype
  currently uses.

**Requirements**

Scope
- **R0.** Change management is defined for standards; extensibility to other item types is a
  nice-to-have, not a constraint.

The migration record
- **R5.** The mechanism carries no standard-specific knowledge — everything specific to a standard
  lives in its migration record, so the mechanism never needs updating when a standard changes.
  *(Reworded on review; previously "the executor is dumb," which misdescribed it — see R23.)*
- **R23.** The action fully describes the work to be done. The executor carries out what the action
  states; it does not infer intent, fill gaps, or improve on the instruction. Reasoning is used in
  service of applying the action as written — resolving how to express the change in this document's
  format, or locating where the action's target sits — not in deciding what the work is. Where an
  action requires judgement, it must say so explicitly. This is the principle behind R10.
- **R6.** A version is not published until its migration record is written.
- **R7.** Migration content is held beside the definition, not inside it.
- **R8.** History accumulates; prunable only once nothing is proven to sit behind.
- **R13.** Every version has a migration record, including an explicit "no action."
- **R14.** A migration record is a set of condition-to-action tasks; conditions evaluate against
  definitions.
- **R15.** The migration record travels with the standard.
- **R22.** Conditions are read from the doctype definition and cover inclusion only — *is the
  doctype X*, *does the doctype use block type Y*. **Reduced on review (v8).** It previously required
  a wider vocabulary able to interrogate how a doctype modified an included block. With doctype
  modification of included blocks disallowed in §8, no such case arises and the requirement shrinks
  to what the settled conditions already do.

Detection
- **R4.** Wrong before old: a change making old shape produce a wrong result applies before use; an
  old-result change may wait.
- **R9.** "What is outstanding?" is answerable without opening every document.
- **R16.** Detection is bounded by what is observable where it runs, and states its own scope. A
  clean result means "nothing outstanding among what I could see."
- **R17.** Detection is read-only; it never modifies a document.
- **R18.** Where required standards are absent, documents are not modified.
- **R19.** Severity is per task, not per version.
- **R20.** A cheap summary answers "could blocking work apply here" without evaluating the full task
  set.
- **R21.** A standard behind its own declared dependencies is a detectable state.

Execution
- **R1.** A session modifies only what it has authority over; plugin-delivered content is reported,
  never modified.
- **R2.** Migration is raised in the workflow and automated — never silent, never hand-edited.
- **R3.** Execution never consumes the working session's context without the user choosing it.
- **R10.** Preserve unrelated content; fail visibly rather than guess.
- **R11.** Migration alone creates no Decisions entry.

Whole
- **R12.** The model is statable in thirty seconds.

---

### Schedule scored

Against the settled model. Amber means satisfied by discipline or convention rather than mechanism.

| | Requirement | |
|---|---|---|
| R0 | Scoped to standards | pass |
| R1 | Authority — modify only what you own | pass (E1) |
| R2 | Raised in workflow, automated, never silent | pass (E2, commands) |
| R3 | Never consumes working context unchosen | pass (E2, E5 defaults) |
| R4 | Wrong before old | pass (CM-Q5) |
| R5 | Mechanism carries no standard-specific knowledge | pass |
| R6 | No publish without a migration record | pass — presence check in the publish operation, no override |
| R7 | Held beside the definition | pass |
| R8 | History accumulates, prunable later | pass — pruning deferred, option preserved by CM-Q2 |
| R10 | Preserve unrelated content; fail visibly | pass — backed by R23 (the action is the whole scope of the work) and by per-task success checks |
| R11 | No Decisions entry for migration | pass |
| R12 | Statable in thirty seconds | pass |
| R13 | Every version has a record, including "no action" | pass |
| R14 | Condition-to-action; conditions on definitions | pass |
| R15 | Travels with the standard | pass |
| R16 | Detection states its own scope | pass |
| R17 | Detection is read-only | pass |
| R18 | No modification where standards absent | pass |
| R19 | Severity per task | pass |
| R20 | Cheap summary for the blocking question | pass |
| R21 | Standard behind its dependencies is detectable | pass — near-trivial once doctype modification of included blocks is disallowed; standards are governed documents and are checked on read like any other |
| R22 | Conditions read from the doctype definition, inclusion only | pass |
| R23 | Action fully describes the work | pass — stated as a principle; enforced in practice by the success check |

**R9 — "what is outstanding" answerable without opening every document — is withdrawn.** It was the
requirement the wide scan existed to serve, and it fell with it (CM-Q3). It is now a **stated
limitation**: corpus-wide currency cannot be answered. What can be answered is that every document
used is current, which under the settled model is the only claim that bears on correctness.

**No ambers remain after the v8 review.** Both cleared for reasons worth recording: R10 gained a
principle behind it (R23, the action is the whole scope of the work) and a mechanical backstop (the
per-task success check); R21 shrank once doctype modification of included blocks was disallowed,
since the stale-adjustment risk it guarded against can no longer arise.

**The one gap the review found was success.** The model said a transition writes only if all tasks
succeed, without saying what succeeding meant for an AI applying text instructions — atomic-on-
success with success undefined. The three-part task closes it. Three further review points shrank to
nothing once doctype modification was disallowed, which is the better outcome: the model got smaller
under review rather than larger.

**Standing, by choice: no reconciliation path.** Every comparable system that started lazy later
added a sweep. This one does not, and the correctness argument holds — an unused document harms
nobody. The operability cost is real: migration history can never be simplified, and corpus currency
cannot be stated. Mitigated by the machine-findable stamp (CM-Q2) and the code-side named-scope
command (E5). Debt with a repayment plan, not a hole.

---

### From the old methodology — keep unchanged

Assessed against the full decision chain in the Capabilities core binder. The user's suspicion that
this is an application problem more than a design one is largely borne out: the mechanism was
designed, declared fifty-five times, and never asked to do anything.

- **Owner authors the transition; the mechanism carries no standard-specific knowledge.** Right, and now R5. (The old wording was "the executor is dumb"; reworded on review — the applier reasons, it just does not decide what the work is.)
- **Transition shape** — version, statement of change, ordered items, success condition. Exactly
  what an executor needs. Keep unchanged.
- **Positive declaration; never infer deltas by diffing definition text.** Right and load-bearing.
- **The checkpoint records *proven* conformance, not the version that happens to be installed.**
  Subtle and right.
- **Stepwise durable, records partial progress.** Required for any batch execution.
- **Authority boundary** — mutate only what you own, report the rest. Already the correct answer to
  the plugin-ownership problem in C.
- **"Preserve unrelated content; do not rewrite merely to make the document look newer."** The
  single most important sentence in the old migration material, currently buried as one item inside
  one transition. **Promote to a standing rule.** An AI sweeping a document will want to violate it
  on every pass, because tidying always looks like improvement.
- **Fail visibly rather than guess** where declarations are contradictory.
- **Migration alone creates no Decisions entry.**

**What actually failed, stated plainly.** Not the runtime-observation premise, which is sound. Three
things: severity was moved from task level to release level; non-blocking work waited for a save
that frequently never came, with no way to ask how much was outstanding; and the result was declared
the designed steady state, which closed the question rather than answering it. Across the visible
binder set: roughly fifty-three transitions declared "no action," exactly one on-update, exactly one
required, and no evidence any document ever traversed either.

### Considered and withdrawn this session

Recorded so it is not re-proposed. A **change-time push model** was worked at length — sweep the
corpus when a definition changes, converge before commit, treat the stamp as evidence rather than
trigger. It was withdrawn on two grounds the user raised: it cannot reach documents in project
repositories with independent lifecycles without manual per-repository tracking, which is the
original problem wearing a different hat; and runtime observation gets that case right for free,
because the check costs nothing when the material is already loaded. What survives from it is the
audit use — a wide check is how you learn it is safe to prune migration history (R8) — and with
pruning deferred at CM-Q3 that purpose is not live. What survives is the code-side named-scope
operation (E5), which provides the same reach as a directed command rather than as a check.

### Owed next

Nothing outstanding in the model. Carried forward to the corpus build:

1. **Author the migration-format standard**, carrying the three-part task shape (condition, action,
   success check), the structured/prose form split, R23 (the action fully describes the work) and
   R10 (preserve unrelated content) as hard inputs. Authored with the doctype set, not before it.
2. Land the R6 publish gate wherever the publish operation is defined.

---

## 12. Filter rules

Unchanged from v2. The eight-question sieve; disposition per item is moves as-is / moves reshaped /
left behind. Owner = whoever knows the most. Live why stays with the current document; historical
why goes to Decisions.

---

## 13. Folder structure

Unchanged from v2. `AIDE/documentation/` holds all AIDE documentation; `_rebuild/` holds this
rebuild's working docs; `documentation_old/` is the previous corpus, source to mine not to edit.
`_rebuild` docs need not conform to full spec but use simple visible versioning.

Adds this session: an **Infrastructure** folder under the documentation root for tool masters, and
an **`_tools`** folder at the documentation root for running instances.

---

## From cross-session items

### Binder definition (raised 2026-09-07)

The binder is used constantly and defined nowhere in the rebuild. The binder
**doctype** — what a binder file looks like, how a consumer reads it, what the
manifest means — belongs to Documentation Methodology as a small definition. The
binder **builder tool** stays in Infrastructure. Which binders exist and what
they contain is a user decision, defined in the file system, outside AIDE's
scope.

Binder purpose (stated fresh): make management of many master files easy by
producing a single file containing the full contents of the masters it includes,
so one file can be removed from context and one added. A binder is a **complete
replacement** for the individual masters it contains — load the binder instead of
the masters, never both.

Builder configuration model: include paths, include file types, exclude patterns
and paths, destination path. The builder runs, detects file changes within its
scope and rebuilds if changes. Binders increment version each time they are built
due to new changes. Multiple binders can be defined for different context scopes
for different chat projects. For AIDE specifically, likely one binder for the
whole corpus.

### Durability test — binder-class versus working-class (from Claude-Code, 2026-09-08)

The rule for what belongs in the binder versus the working document is
**durability, not cadence**. Everything that outlives the session is
binder-class — it goes into a master document and therefore into the binder.
Open items are register-class (durable, belong in the binder, written at master
update); interim items live in the working document until then. Aligns with the
pending-content rule (v22): the working document holds current working state and
pending content destined for masters not yet written.

Settled with Claude-Code; recorded in BinderBuilder_Design v7 on their side.

### Binder-settings outcomes (from Claude-Code, 2026-09-08)

Five changes committed on Code's side (BinderBuilder_Design v7):

1. **JSON added** to recognised file types.
2. **Path-qualified file exclusions** now supported (not just filename patterns).
3. **`*_Working_*` exclusion removed** — working documents are not defined in the
   rebuild; premature to exclude by name convention.
4. **Empty-scope rule reversed** — an empty scope now writes an empty binder
   rather than preserving a potentially stale one.
5. **Binder file naming** now carries the binder name.

### Masters focus and no-binder-references rule (2026-09-08)

Two standing rules:

1. **Master files are the unit of work.** Binders are a delivery convenience — a
   concatenation of masters for context loading. Authoring attention stays on
   masters; binder rebuilds are downstream and automatic. Verification of
   content happens against masters, not binders.
2. **No document references binders except the binder definition itself.** Binders
   are a current mechanism for working around context-loading limitations; that
   mechanism may change. Coupling other documents to binders creates references
   that go stale when the mechanism does.

---

## Generic constructs settled during the Project Design pass

### Three-layer authoring model (applies to every component)

Settled 2026-09-07 while reviewing Principles; general to the rebuild.

1. **Design document** — elaborates each element: what it is, and the reasoning
   for why it exists. Depth and clarification live here.
2. **Decisions** — records the thinking and valuable knowledge worked through to
   get there, as normal.
3. **Standard** — the published artefact. Hard bar: extremely brief and
   concise, because it is loaded into memory and applied constantly alongside a
   stack of other standards. No bloat, no restating, nothing superfluous —
   **but brevity is never bought at the cost of what the standard is trying to
   achieve.** Lean and accurate, both. This authoring bar is itself an input to
   defining the Standards component.

**Standing step:** each authored standard is reviewed by a separate AI before
acceptance, to confirm it implements the design in a form that is usable and
lean.

**Sign-off rule that falls out of this:** a component's design pass being
complete does not sign the component off. Sign-off waits until its standard is
authored (which needs the Standards component defined) and cross-reviewed.

### Block-level portability convention (general, strong)

**Define logic as block types wherever possible, not doctypes.** The block is
the portable unit. Keep doctypes with the topic that owns them; when a block
turns out to have shared meaning, promote just that block to a generic context
and let topic-specific doctypes reference it.

This lowers the stakes on every ownership call — a wrong call costs a block
promotion, not a doctype migration.

**Exemplar:** definition of done started life as a brief element but is
principle-level, so it wants to be a generic block that the Project Design brief
consumes.

**Caution recorded:** promote because a block *has* shared meaning, not because
it *could*. Same demonstrated-need bar (§6c), or this drifts into the
interconnection web flagged during the migration work.

### Component project documentation — definition of done (general pattern)

Not a one-off for Project Design. This is the completion gate for **any**
component's project documentation, and it sits on top of whatever done criteria
that component already carries.

1. Its **doctypes and block types are defined** — including, per the ownership
   rule below, where each one lives.
2. Its **workflow, behaviour, methodology rules and guidance are recorded in the
   design**.
3. All **thinking and knowledge behind them are recorded in decisions and
   knowledge**.

**Consequence.** This reopened Principles, whose design pass was previously
recorded complete — a design pass is not done until all three hold.

### The work item — the base workflow entity (settled 2026-09-07)

**Owner: Working Practices.** It is about how work is conducted, not how
documents are shaped, so it fails the Documentation Methodology test and passes
the generic-operating-behaviour band. It is deliberately **cross-side** — design
raises work items, build raises work items, so does anything else.

**Definition.** A work item is an **encapsulated unit of something pending in a
workflow** — something that needs attention, or is being worked through. It is
raised from any source: the human, a build return, a session noticing a
consequence, another component handing something in. Its weight is **not decided
at the moment it is raised**.

**Two axes.** The item is the stable thing; what varies around it is:

- **Type** — what kind of thing it turned out to be, determined on judgement.
- **State** — open, current, closed. These are **views**, not different entities:
  "the open work items" is a filter, not a separate list.

**Naming.** "Work items" serves as both the singular noun and the collective term
for the set at any scope — a session, a project, whatever is meant. There is no
separate container doctype; the collection is just the plural. So: *add this to
work items*, *what are the open work items*, *remove that from work items*.

**Types — deliberately not enumerated yet. Moderate.** Capture-and-place is
expected to surface the real type list; enumerating now would be inventing.
Record the types as an **output** of that work, not an input to it.

**The fates.** What can become of a work item — chosen by the session on context,
not applied from a routing table:

- **dealt with in conversation**, leaving no trace, because it warranted none;
- **resolved and recorded as a decision**, where it settled something with
  reasoning worth keeping;
- **parked as an open item**, where it is live but unresolved;
- **captured into WIP**, where it is active thinking mid-flight;
- **become committed work**, landing in the work register.

**The one governing rule.** *No knowledge lost.* A work item may be dropped, but
only by a **decision** that it carries nothing worth keeping. Escalation is a
judgement; disappearance is not an accident.

**Defined concept, scalable implementation.** The work item and its collection
exist as a defined model; a session may realise them not at all, lightly, ad hoc,
or in full — chosen by scale, severity, importance and the nature of the
workflow. Same pattern as everything else in this rebuild: define the shape, let
the implementation flex.

**Precedent checked.** This is the mainstream architecture, arrived at
independently: Azure DevOps and agile use *work item* as a generic base with type
specialising it; Jira and GitHub use *issue* with type or labels doing the same
job; ITIL names its types hard (incident, problem, change, request) but shares
one state lifecycle; Kanban makes the card the unit and the column the state; and
GTD supplies the discipline that nothing leaves the intake un-judged — which is
no-knowledge-lost under another name. **Work item** was chosen as the base word
because it is plain, side-neutral, and already how the work is spoken about.

### Definition of done — the generic block (settled 2026-09-07)

**Promoted to a generic block type. Owner: Working Practices.**

**Why Working Practices and not Documentation Methodology.** A definition of done
is not a structural property of a document — a document cannot assess itself. It
is exercised in the *act* of judging whether something is complete, which is a
comparative judgement made during work. That is generic operating behaviour, so
it sits in band 2, alongside the workflow moments that invoke it: a brief closing
out, a build returning, a review concluding.

**Why generic rather than Project-Design-owned.** Shared meaning is
**demonstrated**, not merely possible — it is already recorded at principle
level, and Build needs a completion test of its own. That clears the
promote-only-on-demonstrated-shared-meaning bar.

**The block carries the invariant, not the content.** The invariant is a
**property**: a definition of done must be **testable or assessable** — a bar you
can actually check something against. That is what makes it a definition of done
rather than an aspiration, and it is true everywhere it is used.

**Consumers fill the content.** The brief's definition of done, Build's, a
review's — each consuming parent block or doctype expands what its done actually
contains, in its own context. **The generic block guarantees the shape; the
parent supplies the substance.** This is the block-versus-parent split applied,
and it is a better fit than a loose principle because it makes the requirement
structural and checkable.

### Ownership designation — a rule for Documentation Methodology

**Defining any doctype or block type must include naming its owner and
residence.** Part of being defined, not a separate later step.

**Home: Documentation Methodology**, because that is where doctypes and block
types are defined *as concepts* — the grammar. Clean separation: **Documentation
Methodology owns the requirement to designate a home; each definition states
which home.**

**Why it is worth a rule.** This has bitten repeatedly — a thing gets defined,
its residence gets deferred to "placement later", and placement then has to
re-derive a decision that was obvious at definition time. It is the routing rule
stated at the point of definition. **Strong.**

*Applied retroactively this pass: definition of done → Working Practices; work
item → Working Practices; work register → Project Design; the ownership rule
itself → Documentation Methodology.*
<!-- END SOURCE: _rebuild/AIDE_Rebuild_SettledDecisions_v1.md -->

---

<!-- BEGIN SOURCE: _rebuild/ProjectDesign_Decisions_Pending_v1.md -->
# Project Design — Decisions (Pending Content)

> **Version 1** (2026-09-08). Pending content extracted from AIDE_Rebuild_WIP_v23 per rebuild guide F9. Reasoning, rejected alternatives, corrections, and decisions from the Project Design pass. Ready to feed ProjectDesign_Decisions when masters are authored.

---

### The six-stage per-component review procedure (adopted, general)

Adopted 2026-09-07; applies to every component review from here. This procedure
is itself a working-practices artefact to capture when working practices is
worked.

1. Clarify purpose.
2. Clarify objectives, model approach.
3. Discuss and resolve key issues.
4. Review requirements, resolve changes.
5. Work through how the brief is delivered — the design.
6. Review design output — standards etc.

**Stages 4 and 6 author FORWARD first — amended 2026-09-07, general.** The
original legacy check anchored the work on the old material and then asked what
justified keeping it, which quietly gave the old corpus a default seat. Inverted:

1. **Author forward from the brief.** Derive requirements — and later the
   standard — from purpose and objectives, without reading the old design first.
2. **Then run a two-part sweep of the old corpus, as a resource, not a gate:**
   - **Omissions sweep** — is there a requirement the old design met that the
     forward design does not? Missing, not merely absent.
   - **Approach sweep** — how was it implemented before, and is there a learning
     or technique worth lifting?

The old corpus never gets a default seat. This is what makes the
demonstrated-requirement rule (§6c) actually bite. **Strong.**

### Stage 3 — Key issues resolved

- **Work register survives.** The gap it fills is **temporal, not
  interpersonal** — something must hold "design says X, build hasn't caught up
  yet." Not team scaffolding.
- **Live-state granularity by nomination.** A topic can nominate which WIP or
  work register it uses, so a cluster of topics can share one.
- **WIP is the staging buffer — current memory; the binder is persisted
  memory.** Register items ride the design-change binder update for free.
  Completion and acknowledgement also stage in WIP and flush on the next pass.
  This resolves the churn objection.
- **The live-state trio moves to working practices** — WIP, work register and
  open items all live there. *(Superseded later in this pass — the work register
  comes home to Project Design; WIP and open items stay generic. See the
  component-ownership boundary section.)*
- **Producer guarantee.** The obligation lives with Project Design at
  requirement weight — a design change is not complete until the register entry
  exists. Enforced by the producer, never by the receiver. *(The original split —
  obligation here, artefact in working practices — was withdrawn later in this
  pass; the register itself is now Project Design's.)*
- **Handoff artefact judged by sufficiency.** Primarily AI-written and AI-read.
  The test is whether it carries everything the executing side needs. Slight
  over-weight is acceptable; depth proportionate to the work. *(Amended later in
  this pass — the sufficiency test survives, but it now attaches to the
  design-build handoff rather than to a fixed work-package doctype.)*
- **Register default-on.** The register is the default. Non-use must be
  **explicitly stated** in the design or brief. Where the AI believes a project
  should not have one, it prompts, and the result is recorded. This is P5
  (authoritative evidence over incidental inference) and P10 (confirmed state
  over assumed state) applied.

### Findings from the existing binder (ProjectDesign_Binder_v6)

*(Early reconnaissance, taken during stage 3. Superseded in coverage by the full
two-part sweep recorded below — see **Binder sweep part 1 — omissions**. The five
findings here stand; the sweep is the complete pass.)*

1. **The seam already exists but points at the wrong owner.** D12 separates the
   producer rule (Project Design) from the admission boundary; §3 assigns
   general work-register type and admission semantics to Documentation
   Methodology. Item 7 already overruled that. The binder is **stale, not
   wrong-headed**. **D12 needs rewording to point at Working Practices**, and
   the work-package doctype (§7, `AIDE_WorkPackage@v3`) follows.
2. **Proportionate fill is already designed.** §6 lists six fields a register
   item carries "proportionately." Extend that to the work package rather than
   inventing a new rule.
3. **Default-on is a genuine strengthening.** §6 currently only forbids an
   implicit "implementation later" assumption; it does not require a
   declaration. Record as a change.
4. **§9 already answers part of the handover seam** — routine reversible detail
   goes to Build; objective, major scope, acceptance, ownership, architecture
   and policy return to Project Design. Confirm, do not reopen.
5. **§8 returned-pending state (D13) survives** on demonstrated need — losing
   the thread mid-reconcile is a real solo failure mode. **Moderate.**

### Doctype ownership — the clean line (settled)

**Documentation Methodology owns the methodology only** — what a doctype is,
what a block is, headers, footers, metadata, versioning, common structural
standards. **The grammar.** Individual doctype definitions live with the topic
that owns them.

*(The allocation originally recorded here was reworked later in the same pass —
Working Practices was accumulating other components' specifics. See
**component-ownership boundary — reworked** below for the governing test and the
final allocation. Summary: Project Design owns brief, design, overview and the
work register; WIP, open items, decisions and knowledge stay generic.)*
- Shaping behaviour — how brief and design get evolved — is defined in Working
  Practices for now; move later only if demonstrated.
- **The split test belongs to Documentation Methodology** as part of the
  grammar.

Decisions and Knowledge themselves are **already locked** (see §7) — objective
"no valuable knowledge lost," Decisions takes what is topic-scoped, Knowledge
takes what has no owning topic, Design governs on conflict. No reopening; the
only change here is who owns the doctype definition.

### No knowledge lost — the fundamental rule (to Working Practices)

Preserving knowledge outranks churn every time. The balance is real but **not
symmetric**. Claude carries responsibility for this and should push when it sees
loss happening. Three behaviours:

- **Session-close sweep** — before a chat ends, anything pending is written to
  WIP or to documents.
- **Session-start check** — a new chat looks back at recent previous chats to
  confirm nothing failed to make it in. Within Claude's actual capability; it
  can read recent conversations.
- **Periodic consolidation prompt** — when WIP gets heavy, suggest a pass to
  flush to documents and regenerate the binder.

Governing principle: do whatever the platform's capabilities and limits allow to
ensure nothing that needs recording is lost.

### Session-transition commands (to Working Practices, design later)

Commands marking work-session transitions, distinguished on two axes — how much
gets flushed, and whether there is a continuation. Names are Dave's to set;
working labels only.

- **Full stop** — session over; strongest sweep.
- **Checkpoint and continue** — a natural break to stop a chat bloating; flush
  plus a handoff of where we were and what is next.
- **Flush without closing** — commit to WIP, or push to masters plus binder,
  while the chat continues.

**Rationale — strong yes.** An explicit command removes Claude's need to *infer*
session end, which makes the no-knowledge-loss sweep reliable rather than
best-effort.

### Live-state set justified; elasticity and the split test

**The journey is as valuable as the conclusion.** Recorded knowledge is
intellectual property and knowledge capital regardless of team size. Retention
test: *if you had to rework or redo this, what would you want to know, and what
will have value for future evolution.* The solo-developer volume objection is
withdrawn — the cost is the work of recording, and that work is Claude's to
carry.

- **Elasticity model.** Same content, container chosen by scale. A block lives
  inside its host document for a small project and splits into its own doctype
  when it grows. Applies to open items, the register, even register-inside-design
  for a tiny project.
- **The split test — locked, strong.** Externalise a block into its own document
  **when keeping it in would compromise the primary role of its host** — for
  example when register or open-items volume degrades the ability to search,
  understand and use the design. Below that line, keep it in; file management is
  easier.
- **Open items defined:** the ongoing design task list, including future and
  next-stage items that extend design scope. Owned by Working Practices.

### Brief — mandatory, and a composite block

- **A brief is mandatory. Always.** Standalone or incorporated into another
  document, but never absent. Design is the *delivery* of the brief, so design
  cannot exist without one.
- **Brief is a composite block type containing its element blocks** — purpose,
  objectives, requirements, considerations, target/outcome, and definition of
  done. That composite unit can be the body of a standalone brief document, or
  sit at the head of a design document for a small project. **Strong.**
- **The brief's home is scale-dependent, and the split test governs it**
  (settled 2026-09-07). For a small project the brief block lives inline at the
  head of the design; as it grows it branches out into its own standalone brief
  doctype. The trigger is the split test already locked: externalise when
  keeping the block inline would compromise the primary role of its host — here,
  when the brief's bulk starts degrading the design's readability and use. Same
  content, container chosen by scale. **Brief and design are therefore not two
  mandatory separate documents** — they are one composite that is either joined
  or split. **Strong.**
- **Purpose and objectives are distinct and both earn their place** — purpose is
  why the thing exists; objectives are what it must achieve.
  **Moderate-to-strong.**

### Definition of done — a core pillar, at principle level

> **Amended 2026-09-07 — see "Definition of done — the generic block" below.**
> Definition of done is now a **generic block type owned by Working Practices**.
> The principle-level recording stands as the signal that pushed it there; the
> block is where it actually lives. The Principles consequence recorded at the
> foot of this subsection is superseded by that placement.

**Recorded at principle level, not merely as a Project Design rule.** It is
elementary, to be kept front of mind and carried through everything, and it is a
protection mechanism for effective working.

The brief largely defines done: purpose addressed, requirements met,
considerations factored in, plus any target criteria set. It governs how briefs
are written, how work packages are judged sufficient, and how build return is
reconciled. **Strong.**

**Consequence to action:** Principles' design pass is recorded above as complete
with nine premises. This adds a candidate premise. Principles must be revisited
to place definition-of-done before its standard is authored.

### Overview — SURVIVES as a Project Design doctype

Overview was **parked, not killed**, in the block-catalogue session, with the
discussion explicitly reserved for later. That discussion is this one. The
parked return condition was *topic-or-corpus scale*; the case made here
**corrects that** — the real return condition is **function**, at project scale.

Claude recommended cutting Overview and **withdrew the recommendation** on the
argument below.

**Purpose.** A single pane-of-glass snapshot of a whole project — an accurate,
concise snapshot that can be loaded into the head quickly. It solves the single
biggest problem in working with AI: **information overload**, when working
across five or ten topics and switching between build work and design work. It
gives context for anything discussed without re-reading the documentation set.
It is also a **deviation detector** — a concise snapshot surfaces anything that
does not align with the objective or the model.

**Content.** Key objective; the chosen approach or delivery method; the model at
top level; key defining principles.

**Register — statements, not explanation.** Where something can simply be
stated, it is stated. Short and brief. Brevity is a strong benefit because it
makes the Overview cheap to load — **but that drive for brevity must not
compromise the information the Overview needs to contain.**

**Recall-and-drill.** Each statement is a handle: it triggers memory recall, and
where more is needed it can be asked for, or the session or document where it is
fully defined can be read. An Overview entry carries an implicit "the detail
lives elsewhere."

**Elasticity.** Inline in the design or the brief for small projects; split out
into its own document per the split test.

**Owner:** Project Design. **Audience:** primarily human, primarily Dave — a
legitimate design driver.

### Design inbox — the inbound entry point (RETIRED as a named thing)

> **Superseded 2026-09-07 — see "The work item" below.** The inbox was never a
> place or a doctype; it was the lifecycle of things raised into a workflow, and
> "inbox" smuggled in a queue-and-processor flavour that does not apply. The
> mechanism survives in full as the **work item** and its fates. The word is
> retired. What follows is kept as the reasoning that produced the work item, not
> as a live definition.

Separated out from build return, which is the better cut: build return is
build answering a handoff; the inbox is anything arriving that design must
consider.

**A single inbound entry point for anything requiring design attention, from any
source.** Source is an attribute, not a separate mechanism:

- the human raises something;
- a review or collaborative session with another AI surfaces a design-relevant
  issue;
- build sends an unsolicited signal — including from work in another area that
  turns out to bear on this design scope.

**Defining property: flexible handling proportional to significance.** It is a
doorway with a routing rule, not a ledger — items disperse to their real homes:

- raised and resolved inside the session → a light note, possibly just a
  decisions entry recording that it was discussed and where it came from;
- still pending → an **open item**;
- active thinking attached → stages in **WIP**;
- carries or needs a document → a working document, tagged back to the entry.

A build return that "raises an issue" then **feeds** the design inbox — which is
how the two connect without being the same thing.

**Flag for later:** the design inbox smells generic — a build or review session
could want one too. Under the block-level portability convention this does not
need deciding now: define it here, promote it to a generic block only if shared
meaning is demonstrated. **Do not pre-solve.**

### The catalogue this design work will produce (settled 2026-09-07)

What the Project Design design pass is committed to defining, at note level.

**Doctypes owned by Project Design:**

| Doctype | What it covers |
|---|---|
| Brief | The problem space — purpose, objectives, requirements, considerations, scope and boundaries, target/outcome, definition of done. Composite; inline or split by scale. |
| Design | The confirmed model and approach, carrying its own live "why"; the primary source for the handoff. |
| Overview | The project-scale pane-of-glass snapshot; also a deviation detector. |
| Work register | The ledger of confirmed commitments build has not yet delivered. |

**Block types owned here and consumed by the brief:** purpose, objectives,
requirements, considerations, scope and boundaries, target/outcome — the six
brief element blocks.

**Definition of done** is the exception in that list: it wants to be a
**generic, principle-level block** that the brief consumes, not a
Project-Design-only block. Consistent with its recording at principle level, and
with the block-level portability convention. *(Resolved 2026-09-07 — promoted to a
generic block owned by Working Practices. See below.)*

**Owned mechanisms, deliberately not fixed doctypes:** the design-build handoff,
the build return, the design inbox. *(The design inbox was retired 2026-09-07 and
replaced by the work item, owned by Working Practices. The handoff and the build
return stand.)*

### Facilitate, not constrain — captured, home deferred

**The position.** AIDE exists to **facilitate and empower, not to constrain or be
a source of friction**. Documentation must facilitate, not inhibit, control, or
be draconian.

**Not new.** It was recorded in the 3 September session and has been sitting
inert in this document since. It surfaced again while defining the design doctype
and is the reason that doctype is criteria-plus-advice rather than a schema, and
the reason the superseded-after-handoff rule is a judgement rather than a
procedure.

**Not a Principles premise.** It fails the portability test that governs
Principles — it is about **AIDE's own character**, not a universal premise that
holds outside AIDE.

**Home deferred — a decision to make later.** It belongs to AIDE's **root
defining material**. Its form and its home are open until **Core** is worked
(Core is deferred to last) and until we know what else lives at the root. The
content is captured here so nothing is lost in the meantime.

### Binder sweep part 1 — omissions (complete 2026-09-07)

The first half of the two-part sweep of `ProjectDesign_Binder_v6` — the existing
Project Design binder (Index v7, Design v7, Decisions v5 with D1–D22, and the
published Standard v6). Read against the finished forward design. **This is
reading an existing document and producing edits, not open design conversation.**

The forward-to-binder direction is the whole design pass and needs no
enumeration: none of capture-and-place, the work item, the design doctype, the
work register, the handoff, the build return or the commitment-and-return loop
appears in the binder at all. That is the authoring job, not a finding. The
findings run the other way.

#### Bucket A — genuine omissions (the binder held something the forward design did not)

Eight candidates raised. Five carried, two dropped, one parked.

**Carried:**

1. **Build is never handed a choice between conflicting current designs.**
   Recovered from binder §11 and D16 (the many-to-many design-contribution rule).
   Material conflicts among current contributions are reconciled *before*
   handoff. **Strong.** Written up as the design doctype's ninth required
   property.
2. **State the model compactly before elaborating it.** Recovered from binder §4
   and D5 (the two-layer intent/system-then-model checkpoint), compressed to its
   operative test: if it will not state cleanly, the model is wrong, not the
   write-up. **Moderate.** Written up as design doctype advice.
3. **Handoff sufficiency has a ceiling.** Recovered from the old Standard's
   handoff clause — do not re-supply generic execution-platform knowledge the
   build environment already provides. **Moderate.** Written up on the
   design–build handoff.
4. **A requirement stays distinct from an implementation choice.** Recovered
   from binder §3. **Strong.** Written up as the brief's fifth boundary test, and
   goes into the brief standard as well as the design.
5. **The brief names the linked build project or build outcome.** *Not a binder
   finding — surfaced by the director while working item 6 below, and kept rather
   than dropped with it.* **Moderate-to-strong.** Written up in the brief
   section specification.

**Dropped:**

6. **Cross-topic reconciliation** (binder §12 and D18 — topic ownership fixes the
   destination but not where the work is physically done). **Absorbed by
   capture-and-place**, which already guarantees every settled piece reaches its
   right destination whatever topic that sits in. Claude's initial "strong" rating
   was withdrawn as wrong once the director explained the topic model.
7. **No generic top-level workflow owner** (binder §5 and D3). Half of it is
   already implied by §1's purpose-and-boundary statement, which is kept; the
   other half may be contradicted once Working Practices is worked. Dropped —
   see if a need arises later.

**Parked:**

8. **One authoritative instance per scope** (binder §11, the semantic-section
   hosting rule permitting brief/purpose/requirements to be hosted compactly
   inside a domain control document). Blocked: **the concept of *domains* has not
   been reviewed or decided**, and the rule is written entirely in domain
   language.

**Noted, not resolved:**

- **When independent design review fires** (binder §3, §8 and the old Standard's
  Review clause). The director's note: **design-review instructions and
  methodology will likely reside in Project Design**, but revisit after the
  Review component is confirmed.

#### Bucket B — superseded, retired or contradicted (the binder must give these up)

Raised and inventoried this pass; **the four binder-editing items ride here and
are not yet worked.**

- **The work-package doctype** (`AIDE_WorkPackage@v3`). Reaches much further than
  binder §7: the Index references, the §2 flow diagram, §3, §10's release
  lineage, the Standard's handoff clause, D4, D7, D8, D12, and the dependency
  footers of all four documents. Retired in favour of the design–build handoff.
- **Partial coverage** (binder §7 and D8 — a work package selects manageable
  *portions* of register obligations and identifies covered item IDs and
  portions). Dissolved: register items are written as logical blocks of work.
  Also drops the "partial/blocked" branch in §8 and D9.
- **Work-register ownership** (binder §3 and D12, which assign general register
  type and admission semantics to Documentation Methodology). The register comes
  home to Project Design outright. **Raises a live question rather than settling
  one:** D12 explicitly held the register is *not* exclusively design-generated.
  Under sole ownership, does it still admit confirmed non-design work? Keep it
  open; do not close it by omission.
- **The Overview escalation rule** (binder §13, D20 and D21), which makes Overview
  an overflow valve for a Summary that would bloat the design and requires the
  design Summary to survive in reduced form. **Direct contradiction** with the
  forward design, which makes Overview a purposeful pane-of-glass and deviation
  detector with its own required/advice content, and inverts the Summary rule.
  The forward design wins.
- **"Removed after reconciliation"** (D7). The forward register has *reconciled*
  as a state. Removal versus retention is an open call.
- **Binder §9's escalation framing** — superseded by the what/why-versus-how
  boundary with return-if-unsure, plus the cost-and-complexity flag. The §9
  authority list (objective, major scope, acceptance, ownership, architecture,
  policy) still holds as illustration.
- **Binder §2's core model flow** — replaced by intent → capture and place →
  brief → design → commitments → register → handoff → build → reconcile.
- **Binder §3's "Intent / Brief"** — thin, and permits a light brief. Superseded
  by mandatory-brief and the section specification.
- **Binder-local and lineage material** — D10 (container path), D11/D14/D19/D22
  (release issuance), §10's intended output and lineage note, and the
  `MigrationSummary` / `Transition` blocks. None carries forward.
- **Any surviving build-side "work package" is renamed *build package***, so it
  cannot collide with work item. **Strong.**

#### Bucket C — confirm and carry unchanged

Binder §1's purpose and boundary, including "does not own the physical container";
§6's ban on the implicit "implementation later" assumption, now strengthened by
register default-on; "build should not need Decisions history", which matches
design-is-sufficient-alone; §8's "execution evidence does not silently rewrite
Design" and "Build does not close the obligation"; D13's returned-pending state,
already re-adopted as the register state *returned-pending-reconciliation*; and
the old Standard's "apply proportionately" and "keep the model simple".

> **CORRECTED 2026-09-07 (v22).** This list also carried the old Index's binder
> boundary — *the live register loads separately from the stable binder* — on the
> grounds that it matched WIP-as-current-memory, binder-as-persisted-memory.
> **That carry was wrong and is withdrawn.** It was taken from the old binder
> without being tested against the new model, and confirm-and-carry is where
> scrutiny is thinnest. See the register/binder correction below.

#### Named rather than dropped — three homeless items

1. **Does AIDE use the concept of *domains*?** Undecided, never reviewed, and now
   blocking bucket A item 8. The binder uses the term throughout.
2. **"Design project" and "build project" are undefined terms.** Both were used
   as if they are units; neither is defined anywhere in the rebuild. The new brief
   property depends on *build project* meaning something specific. **Recommended
   to be worked before part 2 of the sweep, since the approach sweep hits the same
   terms. Moderate.**
3. **"A brief is the root of a design."** Stated tentatively. Sits close to what
   is settled (brief mandatory, design is the delivery of the brief, brief inline
   at the head of the design) but "root" adds a hierarchy claim those do not make.
   Restatement or small addition — not guessed either way.

#### Method note

A raised-once observation, recorded and not pressed: the four binder-editing
items are phrased as edits to the v6 binder, while the rebuild method holds that
a previous item is a source of knowledge only — author fresh. Claude's
recommendation was to treat all four as decisions recorded against the *new*
Project Design documents, with D12 superseded by a new decision rather than
reworded in place. **Moderate-to-strong.** The director's call either way.

### Binder sweep part 2 — approach (complete 2026-09-07); the sweep is closed

The second half of the sweep of `ProjectDesign_Binder_v6` — the existing Project
Design binder (Index v7, Design v7, Decisions v5 carrying D1–D22, and the
published Standard v6). Part 1 asked whether the binder held a requirement the
forward design had missed. **Part 2 asked whether the binder's structure and
framing still fit the design it now has to express.**

*(Recorded under the collapsed method — see the method restatement. The
part 1 / part 2 split and the A/B/C buckets are retained here only because that
is how the work was actually done; neither continues.)*

#### Reconciliation first — most of part 2 was application, not discovery

**Checked against already-settled material before being proposed, which is the
correction this pass produced.** On that check, most of part 2 turns out to apply
settled rules rather than decide anything.

*Already settled; part 2 only confirms or applies:*

- ~~The work register loading separately from the binder.~~ **WITHDRAWN in v22 —
  this was an untested carry, not settled material. See the correction below.**
- Brief and overview as conditional documents rather than fixed members of the
  set — the split test and the scale-dependent brief home already decide this.
- The four-group structure — this is the **design doctype's own advice** applied
  to Project Design's own document. Not a finding.
- Stating the model compactly — carried in part 1.
- **The whole of decisions maintenance** — see below. Zero new decisions.
- The proportionate field list — already in use as the required/advice field
  split on the work register and the overview.
- Contents as a grouped semantic map — already settled in the Contents block
  definition (curated semantic map, grouped descriptive entries, not heading
  repetition).
- No conflicting designs at handoff — carried in part 1.
- Design-is-the-default disposing of the zero-design permission — a settled rule
  applied, not a new call.
- The work-package doctype was **already withdrawn** on 7 September, so retiring
  it in the new documents is bookkeeping.
- The build-package rename was already agreed. **Strong.**

#### Genuinely new — adopted

1. **The Project Design document set is design, decisions, standard and work
   register. No Index.** *Deferred, not dropped:* whether an index doctype is
   needed at all gets worked once the other components have run and a need has
   either arisen or not. The old Index's five jobs are already split elsewhere —
   document register and container path to the repo configuration file and the
   binder builder configuration (user-level, outside AIDE); binder boundary and
   live state answered by the binder definition; local configuration was empty.
   What remains is topic identity plus the recorded direction that build-project
   identity lives at the topic root, and that depends on the unreviewed index
   doctype anyway. **Work register is a document in the set**, and **inside the
   binder** *(corrected in v22 — v21 wrongly recorded it as excluded)*. **Brief
   and overview are conditional**, governed by the split test. **Knowledge is
   created on demand**, not pre-created empty.
2. **The design document is authored in four groups, not a flat numbered run.
   Strong.** The old document is thirteen sections whose order is publication
   history rather than meaning — the original ten, then the many-to-many and
   cross-topic sections appended at one release, then the orientation section at
   the next, with nothing reorganised. The cost is scattering: the handoff
   appears in three separate sections, the work register in three, and overview
   does not surface until the thirteenth. The new order is **model** (purpose and
   boundary, then the flow — intent, capture and place, brief, design,
   commitments, register, handoff, build, reconcile — stated compactly);
   **definitions** (brief and its blocks, design, overview, work register, the
   design-build handoff, the build return, design project); **rules**
   (capture-and-place, the commitment rule, register invariants, handoff and
   return sufficiency, reconciliation, the cost-and-complexity flag, the
   what/why-versus-how boundary); **boundaries** (what Project Design does not
   own). Definitions sit second despite the settled ordering correction that
   elements come first, because the model section is a flow and a paragraph
   rather than elaboration — it orients and hands straight over. Both hold
   provided the model stays compact, which is also the part 1 carry.
3. **Rule weight markers are lifted. Strong.** The per-section `Weight:
   Requirement` and per-document `Default weight: Expectation` labels. This is
   exactly the needed-at-the-moment-of-application test: a lean memory-resident
   standard has to say which lines bind. **The vocabulary itself is flagged to
   Standards** — lift the technique, settle the home there. *Moderate on the
   home.*
4. **Fenced pseudo-flow blocks are lifted. Moderate-to-strong.** Compact
   statement of a model or a branch; directly serves state-the-model-compactly.
5. **The proportionate field list is named as a technique. Strong.** Required
   fields versus advice fields, applied proportionately. Already in use; naming
   it makes it reusable.
6. **All four binder-editing items resolve as decisions recorded against the new
   documents, not edits to the old ones. Strong.** This is the rebuild method
   applied — a previous item is a source of knowledge only. So work-register
   ownership is recorded by a **new decision that supersedes D12** (the old
   decision splitting register ownership between Documentation Methodology and
   Project Design), rather than D12 being reworded in place.
7. **The orientation section (§13 of the binder) is dropped entirely. Strong.**
   It makes Overview an overflow valve for a Summary that would bloat the design,
   and requires the design Summary to survive in reduced form. **Direct
   contradiction** with the forward design, which makes Overview a purposeful
   pane-of-glass and deviation detector and inverts the Summary rule. The one
   salvageable line — someone opening the design directly must still understand
   what it is — is already settled as design-is-sufficient-alone.
8. **The semantic-hosting park narrows. Moderate-to-strong.** Only the permission
   to host brief, purpose and requirements compactly inside a domain control
   document was ever blocked; the externalise-only-when-warranted half is already
   delivered by the split test. **And with domains now closed, the park falls
   away entirely** — see below.

#### The many-to-many and cross-topic sections (§11–§12 of the binder)

- **Many-to-many design contributions (§11):** split verdict. The
  reconcile-conflicts-before-handoff half is **already carried** from part 1. The
  "zero, one or several design documents, author directly to the outcome" half is
  **contradicted by design-is-the-default — dropped. Strong.**
- **Cross-topic reconciliation (§12):** dropped in part 1 as absorbed by
  capture-and-place. **Confirmed, no residue.**

#### Decisions maintenance — closed, no new decisions

The old decisions document shows three failure modes: superseded-in-substance
entries still reading as current; four entries (D11, D14, D19, D22) recording
nothing but "publish version 2 / 3 / 5 / 6"; and no way to tell current from
historical without reading all twenty-two.

**Claude proposed append-only. Withdrawn — it contradicts a settled rule.** The
locked Decisions and Knowledge rules already govern this under the immutability
clause: **compaction is allowed** — consolidate duplicates, merge related
reasoning — provided substance survives and temporal reference is kept where
sequence affects interpretation; **a cumulative log is not required**; and
**changing a past decision's meaning is a new decision, not compaction**.

Applied to the sprawl:

- **Compaction is the maintenance mechanism. Strong.** The register-as-ledger
  decision and the register-ownership-split decision (D7 and D12) are the case in
  point — same subject, one refining the other across two reviews, currently two
  entries with a "clarification of D7" paragraph buried inside the second. Those
  compact into one entry carrying the current position and the reasoning that
  reached it, temporal reference kept.
- **Meaning changes are new entries. Strong.** Hence the new decision superseding
  D12 rather than a reword.
- **Release-issuance entries never create entries at all. Strong.** The
  exclusions clause already keeps metadata and migration out.
- **No cumulative log**, so stable identifiers are a convenience rather than a
  guarantee, and the document is maintained for current usefulness.

**Nothing new to decide. The maintenance model was already settled; the
twenty-two-entry sprawl is what it looks like unapplied.**

#### Withdrawn — the dependency-footer lift

Claude proposed lifting the old dependency and reference footers, including the
`!` presence marker. **Wrong, and inconsistent with settled work.** The
**dependencies block** — the standards a document is built on and the version of
each it was last brought into line with — was closed by the change-management
work: a flat list of identity-and-version conformance stamps; **moved from the
footer to the header**, immediately after the Declaration, so a partial read from
the top can answer "may I use this"; and the presence markers `!` and `!!`
**explicitly removed** as deployment-currency concerns. The **references block**
(related reading, citation without conformance semantics) is **parked** awaiting a
consumer. Neither is available to lift. **Withdrawn.**

#### Domains — CLOSED. AIDE does not adopt the concept

**Decided 2026-09-07.** No case for domains has been raised by anyone, including
Claude, and the director held no preference either way — so it is closed as a
**considered no**, not an omission.

The old corpus uses "domain" for two jobs. **One** is asserting that Project
Design is not software-shaped — the domain-independence decision (D2) and the
purpose statement's list of software, documentation, capability, business and
creative work. That is a genericness claim: **it needs an adjective, not a
noun.** **The other** is naming an owner for production workflows that are
neither Project Design nor Build — the domain-owned-workflows section (§5 of the
binder). **Topics already do that**: they are hierarchical, they group documents,
and they own things. Domain would be a second ownership axis alongside topic with
no stated relationship between them, which is the shape of a term used before it
was defined.

**Where a real case could still appear:** if topics turn out to be purely a filing
hierarchy and something else is needed to name a field of practice carrying its
own conventions across topics. Nothing has demonstrated that, and Build and
Working Practices are unworked, so it would surface there. **Dropping under
demonstrated-need is reversible; adopting an undefined term across the corpus is
not.**

**Consequences.** The parked sweep finding (one authoritative instance per scope,
with domain-control-document hosting) **falls away rather than resolving** — it
has no referent. And **the claim survives, the word does not**: wherever the new
documents would have said "domain-independent" or "domain-owned", they say
*generic across kinds of work* and *topic-owned*. That is a vocabulary strip on
carried material, not a design change.

#### "A brief is the root of a design" — CLOSED as restatement

**No change. Moderate.** The brief is mandatory, the design is the delivery of the
brief, and the brief sits inline at the head of the design until scale splits it
out. "Root" adds a tree the flat model does not have. Recorded as restating
settled material rather than adding a hierarchy claim.

#### The work register lives inside the binder — CORRECTION (2026-09-07)

**Raised by the director against v21, and he is right.** v21 stated in three
places that the work register loads separately from the binder as live state.

**Provenance of the error.** The claim entered through sweep part 1's
confirm-and-carry-unchanged list, sourced from the **old** binder's Index. It was
carried because it rhymed with WIP-as-current-memory / binder-as-persisted-memory,
never tested against the new model, and then quoted back this session as settled.
**This is precisely the failure the reconcile-before-proposing standing rule was
added to catch**, and it slipped through because confirm-and-carry is the list
that gets the least scrutiny. *Lesson recorded: a carry-unchanged entry is a
proposal, not a settled fact, and gets the same test as any other.*

**The corrected position, in the director's terms:**

- **The work register is inside the binder**, updated in a pass.
- **Items may be written to the working document in the interim**, and are moved
  to the register when masters are updated.
- **The working document is checked for register items in addition to those in
  the register itself.**
- Rationale: **a limited number of working documents and a small number of
  binders to manage in context.**

**Why this is better, not merely different.** The old exclusion exists to stop
register churn forcing binder rebuilds. This cadence *removes* the problem rather
than working around it — the register is written at master update, and master
update is when the binder rebuilds anyway, so the two are already synchronised
and there is no churn to avoid. The old rule only makes sense if the register is
edited continuously, which under this model it is not.

**The decisive argument is context cost**, and it had been underweighted.
Separate loading means every session loads binder plus working document plus
register, multiplied by however many registers exist — and the design already
permits a cluster of topics to share one, so the count is real and unbounded.

**Nothing in the design breaks.** Handoff immutability is unaffected: build reads
the handoff, not the register. Return-driven state changes are design acts, so
they land in the working document and flush at master update like everything
else.

#### Pending content — the working document's second role (settled 2026-09-07)

**Generalised by the director from the register correction.** The register is not
a special case: *design, decisions, brief, open items — almost any document can
have pending content in the working document, and this must be checked.*

**This is not a new mechanism.** Capture-and-place already produces it: when
something is captured and its destination master is not being written this pass,
it has to go somewhere, and that somewhere is the working document. **Pending
content is placed content whose destination has not yet been written.** The
filing obligation that puts it there is the same one that keeps it accurate — no
new construct, no new obligation on the director, no bookkeeping that can rot.

**The rule, stated once:**

> The working document holds two things: **current working state**, and **pending
> content destined for master documents not yet written**. Pending content is held
> **under its destination document**, because capture-and-place already knows the
> destination at the moment of filing. A master document is therefore **not
> authoritative alone** between updates — the current position on any document is
> that document *plus* its pending content in the working document. At master
> update the pending content is written out and clears.

The destination-labelled organisation is load-bearing. An undifferentiated pending
pile puts the burden on the reader to work out what applies to them; content filed
under its destination makes the check a lookup.

**Two consequences recorded with it. Strong.**

- **The working document is always loaded with the topic.** There is no cheap way
  to know whether pending content exists without loading it, and it is small.
- **Reading a master in order to act on it means checking its pending section
  first.** A read-time gate, the same shape as the dependencies currency check.

**Where it does NOT go. Strong.** Not duplicated into each doctype — the
register, design, decisions, brief and open items all share the property, and
repeating it breaks one-source-of-truth and guarantees drift. It is a property of
the two-tier memory model, not of any one document type. And **not an index of
which masters have pending content**: that is a second source of truth about the
working document's own contents, it needs maintaining, and it rots.

**Ownership — flagged, not closed.** It sits in Working Practices as part of the
working document's definition, since Working Practices owns the live-state layer.
The *read obligation* is arguably a corpus-reading mechanic and so Documentation
Methodology's. **Recommendation: keep it whole in Working Practices rather than
split it. Moderate.** A rule half-defined in two places is worse than one placed
imperfectly. Revisit when Working Practices is worked — that pass will test it.

#### Still open after the sweep

- **Does the work register still admit confirmed non-design work?** Raised by
  part 1 when register ownership came home; the old D12 explicitly held that it
  did. **Open — not to be closed by omission.**
- **Stage 6** — design output and standards — **blocked on Standards.** *The
  sweep completing does not make Project Design finished.*
<!-- END SOURCE: _rebuild/ProjectDesign_Decisions_Pending_v1.md -->

---

<!-- BEGIN SOURCE: _rebuild/ProjectDesign_Design_Pending_v1.md -->
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
<!-- END SOURCE: _rebuild/ProjectDesign_Design_Pending_v1.md -->

---

<!-- BEGIN SOURCE: _rebuild/ProjectDesign_StandardInputs_Pending_v1.md -->
# Project Design — Standard Inputs (Pending Content)

> **Version 1** (2026-09-08). Pending content extracted from AIDE_Rebuild_WIP_v23 per rebuild guide F9. Items explicitly flagged as belonging in the Project Design standard. Feeds the standard when the Standards component unblocks stage 6.

---

## Items flagged for the brief standard

Five boundary tests, each with its definition, flagged for inclusion in the brief standard. Source flag: "By the Standards principle (needed at the moment of application), it goes into the brief standard as well as the design" and "the four brief boundary tests go into the brief standard, not only into the design."

1. **Objectives vs requirements.** An objective is what success looks like; a
   requirement is a condition the solution must meet to get there. "Fast" is an
   objective; "responds within two seconds" is a requirement.
2. **Considerations vs decisions.** A consideration is live input still bearing
   on the design; the moment it resolves into a choice it moves to decisions.
3. **Requirements vs scope.** A requirement is a condition the *solution* must
   satisfy; scope is the boundary of the *work* — what is in and deliberately
   out. "Must work offline" is a requirement; "the mobile client is out this
   phase" is scope. The tell for a confusable out-of-scope item: does it
   constrain the solution or the effort?
4. **Target/outcome vs definition of done.** Definition of done is the
   completion test — the short, checkable pass-or-fail bar. Target/outcome is the
   described end state, and may be qualitative or aspirational. If it is the
   condition you check to say "finished," it is definition of done; if it
   describes what you are trying to bring about, it is target/outcome.
5. **Requirement vs implementation choice.** A **requirement**
   states what the outcome must satisfy and stays **distinct from an implementation
   choice**. The classic failure is a requirement written as "use X" rather than
   "must achieve Y", which pre-decides the design inside the brief. That runs
   directly against Project Design's purpose — fluid in, precise out — because a
   solution smuggled into the brief closes the fluid space before it opens.
   **Strong.**

---

## The "needed at the moment of application" test

A Standards-wide principle, the director's own generalisation: what goes into a standard is decided by **"is this needed at the moment of application"**, not **"is this the definition of the thing."**

Placement, routing and other runtime judgements happen from whatever is memory-resident, so *discriminating* guidance — the tell that separates a thing from its confusable neighbour — belongs in the lean standard even though it reads like elaboration. This sharpens the three-layer authoring model rather than contradicting it.

**Immediate effect:** the four brief boundary tests go into the brief standard, not only into the design. **Moderate-to-strong.**

This is a Standards-wide principle and an input to the Standards component definition.

---

## The Contents/Summary edge

Contents and Summary both feed the read-decision from different angles — Contents maps *what is where* to judge relevance; Summary gives *what the document establishes*. Their edges need to stay distinct.

Flagged for Standards — the director's note is that "this will be a common issue."

---

## Rule weight markers

The per-section `Weight: Requirement` and per-document `Default weight: Expectation` labels. This is exactly the needed-at-the-moment-of-application test: a lean memory-resident standard has to say which lines bind.

**The vocabulary itself is flagged to Standards** — lift the technique, settle the home there. *Moderate on the home.*
<!-- END SOURCE: _rebuild/ProjectDesign_StandardInputs_Pending_v1.md -->

---

<!-- BEGIN SOURCE: _rebuild/ProjectDesign_WorkRegister_Pending_v1.md -->
# Project Design — Work Register (Pending Content)

> **Version 1** (2026-09-08). Pending content extracted from AIDE_Rebuild_WIP_v23 per rebuild guide F9. Work owed by Project Design and items carried to other components.

---

## Owed — Project Design

**The forward design pass is COMPLETE**, to the limit of the Standards block. All
six requirements are delivered. Closed this pass, and no longer owed:
capture-and-place (the filing obligation); the commitment-and-return loop
(delivering requirement 5); register grouping into areas (a flat optional label);
the interim-placement rule (closed by absorption into capture-and-place); and
sharpening the old binder's escalation section into an explicit cost-discovery
loop (delivered as the cost-and-complexity flag, which is more than a sharpened
sentence).

**The binder sweep is COMPLETE end to end** — part 1 (omissions) and part 2
(approach) both closed, and both open items with it. Closed since v20: **domains**
(AIDE does not adopt the concept), **brief-as-root** (restatement, no change), and
**all four binder-editing items** (resolved as decisions against the new
documents rather than edits to the old ones).

**Remaining:**

- **Stage 6** (design output and standards) — blocked on Standards. **This is the
  only remaining item.** *The sweep completing does not make Project Design
  finished.*
- **Does the work register still admit confirmed non-design work?** Raised by
  part 1 when register ownership came home. Open; not to be closed by omission.
- *(Resolved by part 2 — retained for the record.)* **The four binder-editing
  items**, inventoried by part 1.
  They are **not** design work:
  - Reword D12 (the decision on work-register ownership) and bring
    **work-register ownership home to Project Design** in the binder.
  - Retire the work-package doctype (binder §7, the handoff-to-build section, and
    its `AIDE_WorkPackage@v3` target) in favour of the design-build handoff.
  - Examine binder §11–§13 (design contributions many-to-many; semantic-section
    hosting; cross-topic reconciliation; and the Design/Brief/Overview
    orientation).
  - Rename any surviving build-side **work package** to **build package**, so it
    cannot collide with work item. **Strong.**
- **Facilitate, not constrain** — its form and home are deferred to Core.

**Then the completeness check** against the component definition of done set
earlier: doctypes and block types defined (done); workflow, behaviour and
methodology rules recorded in the design (done); all thinking routed to decisions
and knowledge (this WIP write, plus authoring).

---

## Carried to other components from this pass

- **To Principles:** definition of done as a candidate premise (reopens the
  Principles element list).
- **To Working Practices:** WIP and open items; decisions and knowledge doctype
  ownership (provisional — confirm when Working Practices is worked); the
  shaping behaviour for brief and design; the no-knowledge-lost rule and its
  three behaviours; the session-transition commands; the nomination model for
  live-state granularity; the six-stage review procedure and its forward-design
  amendment; P6 and the Guidance Profiles review (from Principles);
  **the work item** as the base workflow entity with its types, states and fates;
  **definition of done** as a generic block carrying the testable-or-assessable
  invariant.
- **To Build:** confirm that build's own learnings route correctly under the
  existing Decisions/Knowledge lock — a learning *about the design* passes up, a
  learning about *build technique* stays in build. A check, not new work.
  **Strong.** **Added this pass:** build must be able to **recognise it is
  holding a what/why question** rather than a how question, and must be able to
  **judge when cost has materially exceeded the design's apparent assumption**.
  Both are obligations the escalation boundary and the cost flag place on build;
  neither is designed here.
- **To Documentation Methodology:** the split test, as part of the grammar;
  **the ownership-designation rule** — defining any doctype or block type must
  name its owner and residence; **the binder doctype** — what a binder file is,
  how a consumer reads it, what the manifest means (small definition; builder
  tool and binder configuration are not Doc Methodology's).
- **To Standards:** the Contents/Summary edge. **Added this pass, and general —
  the director's note is that "this will be a common issue":** the test for what
  goes into a standard is **not** "is this the definition of the thing" but **"is
  this needed at the moment of application"**. Placement, routing and other
  runtime judgements happen from whatever is memory-resident, so *discriminating*
  guidance — the tell that separates a thing from its confusable neighbour —
  belongs in the lean standard even though it reads like elaboration. This
  sharpens the three-layer authoring model rather than contradicting it.
  **Immediate effect:** the four brief boundary tests go into the brief standard,
  not only into the design. **Moderate-to-strong.**
- **To Core:** **facilitate, not constrain** — content captured above; its form
  and its home at AIDE's root are an open decision, to be made when Core is
  worked.

---

## Open question

- **Does the work register still admit confirmed non-design work?** Raised by
  part 1 when register ownership came home; the old D12 explicitly held that it
  did. **Open — not to be closed by omission.**
<!-- END SOURCE: _rebuild/ProjectDesign_WorkRegister_Pending_v1.md -->

---

<!-- BEGIN SOURCE: Core/Core_Brief_v1.md -->
# Core — Brief

Version 1. 2026-09-08.

---

## Purpose

Core is the root entry to AIDE. It describes what AIDE is, how it is structured, and the framework-wide requirements and concepts that govern all components. A reader starting here should be able to understand AIDE's shape and navigate to any component from it.

---

## What AIDE is

AIDE makes the standards and behaviours that shape how AI works with you live in your sessions, on whatever surface is in use. Everything else in AIDE exists to produce, deliver and keep that content current.

It is a methodology-driven framework for a solo developer working with AI. It gives AI sessions consistent behaviour, accumulated knowledge, and standards defined by the owner — not by platform defaults.

---

## Objectives

O1. Provide a single, maintained description of what AIDE is and how it works — the framework's own self-description.

O2. Define the component model: what a component is, what a capability is, and how components relate to each other.

O3. Hold the framework-wide requirements that govern all components and cannot be owned by any single one.

O4. Serve as the entry point — a reader (human or AI) arriving at AIDE for the first time navigates from here.

---

## Requirements

R1. **Facilitate, not constrain.** AIDE exists to facilitate and empower, not to constrain or be a source of friction. This is AIDE's own character — distinct from the universal principles, which hold outside AIDE. Every framework-wide decision is tested against it.

R2. **Component model.** Every component has a declared purpose, scope and ownership. A component owns its own documents and decisions. The component definition, the capability definition (standards and tools), and the utility definition all live here.

R3. **Platform neutrality.** Capabilities are defined platform-neutral — the what — and transformed into platform-specific delivery. On Claude, that means skills in a plugin.

R4. **Leanness.** What loads into a session must justify its weight. Leanness is a governing principle at the framework level; the Standards component owns the authoring guidance that enforces it.

R5. **Design is the default.** A design almost always exists behind a standard. Authoring straight to standard is the exception, not the rule.

R6. **No knowledge lost.** The framework captures and places everything of value. This is the fundamental rule.

R7. **Entry-point completeness.** Core's design document must contain a summary of every active component — its purpose and key boundaries — sufficient for navigation. The design specification of each component lives in its own folder.

---

## Considerations

C1. Core absorbs the "facilitate not constrain" position that was deferred pending a home. It is now settled here.

C2. Core replaces the previous definition ("hold whatever shared requirements have no natural home elsewhere"). The new purpose is deliberate and first-class, not residual.

C3. The relationship between Core and Principles needs to stay clean. Principles owns universal premises (portability test). Core owns AIDE-specific character and governance. "Facilitate not constrain" fails the portability test — it is about AIDE, not about all AI work — and therefore lives here, not in Principles.

C4. Some requirements above (leanness, design-is-the-default, no-knowledge-lost) are also expressed or implied elsewhere. Core holds the framework-wide statement; the owning component holds the mechanism. No duplication of mechanism.

C5. The three held candidates (Tags, Scope, Dependencies) and the deferred concerns (environment, platform, domains) remain open and are not resolved by this brief.

---

## Scope and boundaries

**In scope:**
- The framework's self-description and conceptual model
- Framework-wide requirements and considerations
- The component, capability and utility definitions
- The component map — purpose lines and navigation to each component's own material
- AIDE's character statement (facilitate not constrain)

**Out of scope:**
- Individual component designs — each component owns its own folder
- Principles — universal premises live there, governed by the portability test
- Documentation Methodology — the grammar of how documents are written
- The rebuild process itself — that is a project, not a permanent part of the framework

---

## Target outcome

A reader arriving at AIDE — whether a new AI session, a reviewing AI, or the human owner returning after time away — can read Core and understand: what AIDE is, what a component is, what the framework expects of every component, and where to find any specific component's design. Core is the map and the constitution.

---

## Definition of done

1. Core's design document describes the component model, capability and utility definitions, and framework-wide requirements
2. Core's design document contains a current summary of every active component with purpose and key boundaries
3. "Facilitate not constrain" is placed and stated with its rationale
4. The distinction from Principles (portability test) is explicit
5. A reader unfamiliar with AIDE can navigate from Core to any component
<!-- END SOURCE: Core/Core_Brief_v1.md -->

---

<!-- BEGIN SOURCE: Core/Core_Design_Documentation_Working_v1.md -->
# Core — Design Documentation Working

Version 1. 2026-09-08. Working document — concept and principle, not placed.

---

## Status

Exploratory shaping session. Recording thoughts, knowledge, ideas and decisions as concept and principle. Residence of each piece not yet decided. When complete, consolidate and work out where each item belongs.

---

## The anchor — what AIDE is for

Core states AIDE's outcomes; components deliver them. The design use case is the lead outcome, delivered by the Project Design component.

AIDE is ambient until triggered by self-declaration. A document opts into AIDE's capabilities by carrying the information that maps it into scope. No declaration, no imposition — it is just a document. This is facilitate-not-constrain expressed as a mechanical principle.

---

## Forks abandoned

An earlier proposal split AIDE into two forks — Development (building the framework) and Framework (using it). Abandoned because it duplicates: every component would be described twice with most of the substance shared.

Instead, one project per component carries both concerns. The applied-behaviour lens — how the component operates once the framework is live — is included in each component's design where relevant, not as a fixed required element on every design.

---

## Structure — design projects and design areas

### Design project

A container grouping all design material for an area of work. "Project" is the term despite collision with Claude/chat projects — it is the natural word, and the collision is handled by context. "Design project" disambiguates when needed.

### Design area

A bounded part of the thing being designed. Areas are the groupings within a project — each is a section of the overall design. Terminology settled: **project** as the container, **area** as the grouping.

CMS is the reference example: areas include query, views, relationships, dependency system, keys, change log, localisation, pipeline, predicate engine, schema, tags, values — each a different part of the overall design.

### Folder structure

Folders are free organisation only. They carry no meaning the system depends on. A folder might hold one area, several areas, or areas might sit loose with no subfolders. Binders retire the old flatness constraint — a binder can carry a whole project or a segment, so subfolder hierarchies are now practical without paying a sync cost.

### Area identity and hierarchy

Areas are declared on the document, not by folder position. Expressed as a delimited **path** relative to a context-defined root. The path encodes the hierarchy — each segment is a level, shared prefixes show what is related.

Example: CMS / query / SQL — CMS is the project, query is the area, SQL is the sub-area.

Areas can be hierarchical. A sub-brief either opens a new area or sections an existing one — the brief itself declares which by carrying a different or the same area identity.

### Path — the general property

The property is **path**, not "design path." It is a general locating mechanism, not design-specific. Build documentation or anything else uses the same concept. The path is relative to a context-defined root; what the root represents depends on the domain. In a design project, the root is the project.

---

## Expand and collapse

The brief is always conceptually present. Big areas earn a separate brief and separate design documents. Small areas collapse the brief inline into the design document. Same methodology, scaled to the weight of the area.

A brief can branch to sub-briefs, to design documents, or both. The author decides per case and records it — flexible where it should be, explicit so the system knows.

---

## Document handling model

Three self-declared properties compose to give a document its behaviour:

1. **Path** — where it sits in the design structure, relative to a root.
2. **Doc type** — what it is. A known doc type inherits functionality and behaviour automatically. Declare the type and the behaviour comes with it.
3. **Blocks** — the granular unit of functionality. Known defined blocks bring their own logic whether or not the document has a doc type. Include a versioning block and versioning applies. Declare a dependency and the system knows what to do when that standard changes.

Path and doc type are independent and compose. Path is location, doc type is nature. Neither depends on the other.

### Partial application

Blocks work independently of doc type. A freeform document with no doc type can include known blocks, and each block gains its functionality — production guidance, navigation, extraction, and migration scope. Known parts get full support; the rest is carried inert. Functionality degrades gracefully, not all-or-nothing.

### The incentive model

"Define it and you get functionality; don't and it's inert." This is the design principle that lets AIDE be permissive without becoming chaos. You can extend freely — new doc types, modified structures — but you define what you create so the system knows how to handle it. Stay within known structures and you get support for free. Go your own way and you document your own information locally.

---

## Header and footer convention

### Header — triggers and identifies

The header holds what must be seen first because it switches on logic. A machine reading a document starts at the header, sees a doc type, and that fires the doc type skill, loads the rules and functionality, and loads the standard containing that type.

Header carries:
- Path
- Document identity
- Dependencies (change tracking / change management)
- Doc type
- Custom block types (delimited list, if the document includes blocks beyond what the doc type implies)

### Footer — elaborates

The footer holds structural detail needed only after the header has established what the document is. Accessed by jumping to the end, which is fast for both humans and machines.

Footer carries:
- Custom layout and block positioning within the document flow
- Document spec or structure definition for custom documents
- Custom doc type definition, if this document defines its own

### Principle

Header triggers, footer elaborates. Anything that must fire functionality goes up top and stays lean. Structural elaboration goes to the bottom, out of the way but findable. Metadata placement serves both machine navigation and human readability.

---

## AIDE activation model

AIDE is ambient until something triggers its behaviour. The presence of declarations in the header — the doc type above all — is what brings AIDE into play against a document. The header is not just describing the document, it is activating AIDE.

This is opt-in by self-description. No declaration, no imposition. The trigger model is the facilitate-not-constrain principle operating at the mechanical level.

---

## Stable triad

Most designs vary in their stages, but nearly all land on three document types: **brief** (the what — purpose, objectives, requirements, considerations, scope), **design** (the how — the confirmed model and approach), and **decisions** (the knowledge capital — how decisions were made, what was learned along the journey).

---

## Rapid evolution cycle

AIDE is a living, evolving system. Learn something while working, stop, design the component or standard or doc type needed, build it, deploy it — and use it almost immediately. This rapid application development cycle is why migration and change management are fundamental infrastructure, not bolted on.

---

## Open items

1. **Working document** — needs a proper definition as a concept. Flagged, not solved.
2. **Header/footer detail** — which exact properties at which end; the rule is clear but the full list needs pinning.
3. **Residence** — where each piece in this document eventually belongs across the AIDE components. To be consolidated when the shaping is complete.
4. **Path delimiter** — settled as a concept; the exact delimiter and any naming rules are design detail.
5. **Area boundary mechanism** — area boundaries are declared in documents, not by folders. The precise mechanism (property, marker block, doc type implication) is for the design.
6. **Core Brief v2** — drafted but needs rework to reflect this session. The fork structure is abandoned; Core's objectives now include stating AIDE's outcomes with components delivering them.
<!-- END SOURCE: Core/Core_Design_Documentation_Working_v1.md -->

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
