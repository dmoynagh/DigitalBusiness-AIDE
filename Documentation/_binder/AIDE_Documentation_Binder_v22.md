# AIDE_Documentation Binder

> **Generated Binder - do not edit directly.** Edit the individual master documents
> and regenerate the Binder.
> **Binder Version 22** (2026-09-11).

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
- `Core/_index.md` - sha256 `8e58c5e0026b`
- `Core/Core_AIDEMap.md` - sha256 `e3b0c44298fc`
- `Core/Core_AIDEMap.yaml` - sha256 `a3f651bdb590`
- `Core/Core_AIDEPrinciples_Decisions_v1.md` - sha256 `655de3e64709`
- `Core/Core_AIDEPrinciples_Design_v1.md` - sha256 `60e20e8d0b9d`
- `Core/Core_Brief_v1.md` - sha256 `6c2e6280ea89`
- `Core/Core_Design_Documentation_Working_v1.md` - sha256 `b2999c523397`
- `Core/Core_Structure_Decisions_v1.md` - sha256 `2217f6768b89`
- `Core/Core_Structure_Design_v1.md` - sha256 `f464dc43de50`
- `Core/Core_Tags_Working_v1.md` - sha256 `ae6557378adf`
- `Core/Core_Working_v1.md` - sha256 `9808a331b339`
- `Documentation Methodology/_index.md` - sha256 `dd54608243d5`
- `Documentation Methodology/DocMeth_Decisions_v1.md` - sha256 `b349e5ec403e`
- `Documentation Methodology/DocMeth_Design_v1.md` - sha256 `e747f8b0f5e2`
- `Documentation Methodology/DocMeth_Working_v1.md` - sha256 `1af58d615fd8`
- `Infrastructure/_index.md` - sha256 `fb736219786c`
- `Infrastructure/binder-builder/binder_builder_Documentation_settings.json` - sha256 `b9b89306305b`
- `Infrastructure/binder-builder/BinderBuilder_Design_v10.md` - sha256 `e6573d80384e`
- `Infrastructure/binder-builder/README.md` - sha256 `3ec5dab12e67`
- `Infrastructure/file-update-package/file_update_package_settings.json` - sha256 `fce12837157e`
- `Infrastructure/file-update-package/FileUpdatePackage_Design_v1.md` - sha256 `11ad3a9f4c94`
- `Infrastructure/file-update-package/README.md` - sha256 `203b6f20f7ce`
- `Infrastructure/Infrastructure_CLI_Decisions_v1.md` - sha256 `7a16726b5162`
- `Infrastructure/Infrastructure_CLI_Design_v1.md` - sha256 `12e05744ff4a`
- `Infrastructure/Infrastructure_Working_v1.md` - sha256 `1d7a11e25a57`
- `Infrastructure/version-cleanup/README.md` - sha256 `a978d666e85a`
- `Infrastructure/version-cleanup/version_cleanup_settings.json` - sha256 `c17e9142e485`
- `Infrastructure/version-cleanup/VersionCleanup_Design_v3.md` - sha256 `e6d1eb38aba5`
- `Principles/Principles_Decisions_v4.md` - sha256 `2c31c26b5c66`
- `Principles/Principles_Design_v4.md` - sha256 `4bd5797d3d2e`
- `Project Design/_index.md` - sha256 `3002bcf578cc`
- `Project Design/ProjectDesign_Decisions_v1.md` - sha256 `0fc2d790dc5f`
- `Project Design/ProjectDesign_Design_v1.md` - sha256 `c4a80e5fa894`
- `Project Design/ProjectDesign_Standard_v1.md` - sha256 `453aaeb09fb9`
- `Project Design/ProjectDesign_Standard_v2.md` - sha256 `36d4c7c83bdd`
- `Standards/_index.md` - sha256 `3bd4678a60c0`
- `Standards/Standards_Authoring_Standard_v2.md` - sha256 `efd5f36981a2`
- `Standards/Standards_Decisions_v1.md` - sha256 `fb153d3db6bc`
- `Standards/Standards_Design_v1.md` - sha256 `60cebe0ab9f1`
- `Standards/Standards_Working_v1.md` - sha256 `9677537477ab`
- `Tools/Tools_Decisions_v1.md` - sha256 `266576979e50`
- `Tools/Tools_Design_v1.md` - sha256 `d6c8195c6fb9`
- `Working Practices/_index.md` - sha256 `f1d40d14c547`
- `Working Practices/FileOps/WP_FileOps_Working_v1.md` - sha256 `f2ffcdd7c76f`
- `Working Practices/WP_Capture_Working_v1.md` - sha256 `54171d4dea8b`
- `Working Practices/WP_ContentDelivery_Working_v1.md` - sha256 `6b858ff04f50`
- `Working Practices/WP_WorkManagement_Working_v1.md` - sha256 `59a0bba2401c`

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

<!-- BEGIN SOURCE: Core/_index.md -->
# Core

Role: component design

Core is the root entry to AIDE — the framework's self-description, component model, framework-wide requirements, and the map to all components. A reader arriving at AIDE reads Core to understand what AIDE is, what a component is, what the framework expects, and where to find any specific component's design.

## Key definitions at this level

**Component.** A defined area of functionality with a declared purpose, scope, and ownership. It owns its own documents and decisions. It may produce capabilities but need not. It is the functional unit independent of where it lives.

**Capabilities.** A term covering output definitions — Standards, Tools, Utilities. Components that define things delivering and adding functionality.

## Parts

**Structure** (prefix `Core_Structure_`)
How AIDE documentation is physically and logically organised — folder conventions, container labels, the AIDE document concept, path authority, and naming.

**AIDEPrinciples** (prefix `Core_AIDEPrinciples_`)
The operating principles specific to AIDE as a framework — facilitate not constrain, opt-in behaviour, strength model, aliases. Produces a standard for deployment. Distinct from the Principles component, which owns universal, portable premises.
<!-- END SOURCE: Core/_index.md -->

---

<!-- BEGIN SOURCE: Core/Core_AIDEMap.md -->
<!-- END SOURCE: Core/Core_AIDEMap.md -->

---

<!-- BEGIN SOURCE: Core/Core_AIDEMap.yaml -->
AIDEBrowser:
- name: Core
  type: Component
  description: ""
  folder: "~\Core"
  items: 
    - name: ""
      version: 1
      type: "file"
      filename: ""      
      doctype: ""
      description: ""
    
- name: Document Methodology
  type: Component
  description: 
  folder:"~\Document Methodology"  
- name: Workflow
  type: Component
  description: 
  folder:"~\Workflow"
- name: Capabilities
  type: Container
  description: 
  folder:"~\Core"
<!-- END SOURCE: Core/Core_AIDEMap.yaml -->

---

<!-- BEGIN SOURCE: Core/Core_AIDEPrinciples_Decisions_v1.md -->
Core AIDEPrinciples | decisions | Core_AIDEPrinciples_Decisions@v1 | 2026-09-10

## Summary

Reasoning behind the AIDE-specific principles, the strength model, and the aliases mechanism.

## Facilitate not constrain — placement

"Facilitate not constrain" was deferred during the Core brief (2026-09-08) pending a home. It was tested against the Principles component and failed the portability test — it is about AIDE specifically, not about all AI work. Placed in Core as an AIDE-specific operating principle.

The principle was then reworded to "facilitate and extend, not create friction or restrict" during the voice session (2026-09-09) to better express the active posture — AIDE does not just avoid constraining, it actively empowers.

## The design pattern it produces

Dave articulated the principle's mechanical consequence: functionality is attached to the structure and data it needs. The framework does not gate features behind compliance — it looks for the data a feature needs and applies the feature when that data is present. This is the "define it and you get functionality" incentive model operating at the principle level.

Examples: add a version tag to a document's identity and versioning applies. Add a doctype declaration and doctype logic fires. Add a dependency block and change management tracks it. Each feature activates from its own trigger data, not from a global compliance flag.

## Strength model — the fourth level

The original model had three levels (must/should/could, or required/recommended/optional). The fourth level — information — was added during the voice session (2026-09-09) when the reference document type was discussed.

The case: reference knowledge sometimes needs to reach the AI platform but carries no compliance expectation. A reference document is authored into a standard for delivery, not for governance. Without a fourth level, reference-origin content would carry "optional" strength, implying it is a choice to be made. "Information" correctly signals that the content is there to inform, with no decision or compliance attached.

## Aliases — why they matter

Arose during the session (2026-09-10) from the practical problem of referring to Documentation Methodology repeatedly in conversation and documents. The full name is precise but costly to type and read. Dave already uses "DocMeth" and "WP" (for Working Practices) naturally.

Rather than treating this as informal shorthand, aliases are declared alongside the thing they name. This makes them discoverable, unambiguous, and usable by both humans and AI — an AI seeing "DocMeth" can resolve it to Documentation Methodology because the alias is recorded.

Aliases are placed in the `_index.md` for the thing they name. This keeps them with the authoritative description rather than in a central registry.

---

Version note: v1 — initial decisions from sessions 2026-09-09 and 2026-09-10.
<!-- END SOURCE: Core/Core_AIDEPrinciples_Decisions_v1.md -->

---

<!-- BEGIN SOURCE: Core/Core_AIDEPrinciples_Design_v1.md -->
Core AIDEPrinciples | design | Core_AIDEPrinciples_Design@v1 | 2026-09-10

## Brief

**Purpose.** Produce a standard that delivers the operating principles specific to AIDE as a framework.

**Scope.** AIDE-specific tenets that shape how the framework behaves and how its features are adopted. Distinct from the Principles component, which owns universal, portable premises governed by the portability test. Content that fails the portability test — it is about AIDE, not about all AI work — lives here.

**Target outcome.** A deployed standard carrying these principles, the strength model, and the aliases mechanism, so that any AIDE-governed session applies them.

## Facilitate and extend, not create friction or restrict

AIDE empowers. It adds functionality where needed but does not do so from a position of control or dictation. If a user wants to add AIDE's features to a document or project, in full or in part, AIDE applies them where it can. If the user chooses not to, they manage those items on their own.

This leads to a design pattern: functionality is attached to the structure and data it needs to function. Add a particular block type to a document which has the data needed for a component feature to function, and it will be applied.

## Opt-in for benefit, opt-out loses the benefit only

Adopting an AIDE convention activates the functionality it provides. Not adopting it means managing that concern yourself — nothing breaks, nothing is imposed. The cost of opting out is losing the benefit, not gaining a penalty.

AIDE is ambient until something triggers its behaviour. The presence of declarations in the header — the doc type above all — is what brings AIDE into play. This is opt-in by self-description.

## Strength model

Items in standards carry strength — four levels defining how strongly they apply:

- **Required** — must be followed
- **Recommended** — should be followed; deviation needs a reason
- **Optional** — available for use; adoption is a choice
- **Information** — reference-origin content provided for awareness; no compliance expectation

The fourth level (information) exists for content that originated as reference knowledge and was authored into a standard for delivery to the platform. It carries no compliance weight — it informs, it does not direct.

## Aliases

Named things in AIDE — components, areas, parts — may have aliases: shorter or alternative names used for convenience. An alias is an equivalent reference to the same thing.

Aliases are declared where the named thing is described. For a component, that is the `_index.md` in its folder. For example, Documentation Methodology carries the aliases DocMeth and DM.

The purpose is practical — reducing typing and making conversation easier without losing precision. An alias resolves to exactly one thing; where ambiguity exists, the full name is used.

---

Version note: v1 — initial design. Principles from voice session 2026-09-09; aliases from session 2026-09-10.
<!-- END SOURCE: Core/Core_AIDEPrinciples_Design_v1.md -->

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

<!-- BEGIN SOURCE: Core/Core_Structure_Decisions_v1.md -->
Core Structure | decisions | Core_Structure_Decisions@v1 | 2026-09-10

## Summary

Reasoning and alternatives considered for the structural design decisions in the core structure design.

## Physical folders over logical overlays

Explored whether documents needed a logical path structure separate from the physical folder tree. The case for logical paths: documents loaded into flat AI context lose their folder position, so something must carry "where do I sit." Two mechanisms already solve this — the binder manifest carries relative paths for bulk loading, and the document header carries its own path for individual files. A logical overlay on top of the physical structure would duplicate what both already do.

Also explored whether multiple root scopes could share a folder, with documents associating to a specific root by reference. This was the logical-vs-physical separation at its most complex. Dave's direction: drop logical overlays entirely, keep it physical. If two areas need separation, make two folders.

## Root scope parked

Root scope was designed as a block type declaring a folder as a root of a particular kind — design project, component design, etc. The concept went through several iterations: separate block types per root scope kind, then a single block with a type name pointing at a standard.

Parked because no consumer could be identified. Every purpose root scope was supposed to serve is already handled:
- Path anchoring → physical folders plus header paths
- Structure preservation in context → binder manifest
- Container description → the AIDE document
- Classification ("this is a design project") → the role field in the AIDE document

Root scope was compensating for a problem (context flattening) that binders already solve. Identified during discussion as the likely origin of the concept — when files were in flat folders for context loading, logical structure needed to be declared. With binders carrying relative paths, the need disappeared.

## Container labels — vocabulary not types

Considered whether folder roles should be a formal type system with defined nesting rules (solution design contains project designs, project designs contain component designs, etc). Decided against: the labels describe what something is, not what it is allowed to contain. Nesting rules would impose structure the facilitate-not-constrain principle argues against, and no current functionality depends on knowing what's inside what.

Four labels chosen from existing vocabulary Dave already uses:
- Solution design — mirrors .NET solution concept
- Project design — mirrors .NET project concept, aligns with the Project Design component name
- Component design — matches the component definition
- Area / part — both used naturally, synonyms until a distinction is demonstrated

## AIDE document naming

Explored several options for the file name:
- `_AIDE.md` — sorts to top but brands every folder with the framework name
- Named after the container (e.g. `Principles_AIDE.md`) — self-describing but doesn't stand out
- `_folder.md` — generic but describes the container, not the function
- `_index.md` — generic, familiar concept, describes the function (indexing), room to grow

Chose `_index.md`. The underscore sorts it to the top. "Index" describes what it does rather than what it is about. The name is generic enough to work for any project whether using AIDE fully or partially. The concept retains the name "AIDE document" within framework terminology; the file on disk uses a name that doesn't advertise.

## Path authority chain

Applied the same pattern as identity and filename: header is authoritative, file system mirrors. This was a deliberate alignment — both follow the principle that a document should be self-describing and survive being detached from its context. A file pasted without its folder still states where it belongs.

Considered whether the physical-folders-as-structure decision created tension with header-as-authority. It does not — the physical structure is the expected organisation, the header is what the document says about itself. They agree in the normal case; the header wins on conflict.

## Three-tier file model

Arose from the question of what the binder should include. Initially framed as "governed documents only" versus "everything." Dave's test was sharper: does it need to be there for thinking and reasoning? A utility script that is the project's deliverable needs to be in context when working on that utility. A log file never does.

The three tiers:
1. In the binder — needed for thinking and reasoning in the AI session
2. Known to the framework — listed in the `_index`, not loaded into context. The framework knows it exists
3. Just present — incidental files AIDE has no opinion about

This is recorded as a decisions entry because it affects binder design (owned by Working Practices / Content Delivery) and will be referenced from there. The structural implication — the `_index` as the awareness mechanism for tier 2 — belongs here.

## Design and output separation

Design documents and the outputs they produce are separate. The design folder holds the specification; what gets built from it lives where it is consumed. This arose from Infrastructure where utility design docs sat alongside the Python scripts they specified. The scripts are outputs, not design — they belong where they run (_utilities), not where they were designed.

The principle applies broadly: utilities to _utilities, skills to the skills deployment location, standards to capabilities, plugins to the marketplace. The design folder is always "why and how"; the output is always elsewhere.

---

Version note: v1 — initial decisions from session 2026-09-10.
<!-- END SOURCE: Core/Core_Structure_Decisions_v1.md -->

---

<!-- BEGIN SOURCE: Core/Core_Structure_Design_v1.md -->
Core Structure | design | Core_Structure_Design@v1 | 2026-09-10

## Summary

Defines how AIDE documentation is physically organised and navigated. Physical folders are the structure. Documents self-declare their identity and path in their headers, which is authoritative — the file system mirrors it. An optional file named `_index.md` describes a folder and indexes its contents for both human and AI readers. Four container labels provide shared vocabulary for describing what a folder holds. There is no logical overlay, no root scope mechanism, and no formal folder-type system — the conventions empower organisation without imposing it.

## Physical folders are the structure

Folder hierarchy on disk is the organisational structure. There is no separate logical layer. Documents live where the folders put them, and paths resolve from the physical tree.

This decision followed from the removal of root scope (see below) and the recognition that the binder manifest preserves relative paths when documents are loaded into flat AI context. The need to reconstruct structure from declarations disappears when the binder already carries it.

## Path authority

The path declared in a document's header is authoritative. The file's position on disk mirrors it. If they disagree, the header is what the document says it is and the file is in the wrong place. This is the same relationship as identity and filename — header wins, filename mirrors.

A mismatch between header path and physical location is a detectable signal AIDE can flag.

### Path maintenance

To change a document's path: update the path in the header. The FileUpdatePackage carries the move to the file system via a move action. For files updated outside an update package in chat, instruct the user where to save based on the header path. For Code or Cowork working directly on files, check the file's physical location against the header path and move if they disagree.

## Container labels

Four labels provide shared vocabulary for describing what a folder contains. Declared in the `_index.md` file via a `role` field. Plain string value.

Known labels:

- **solution design** — umbrella container; holds component designs, project designs, and areas
- **project design** — contains the design docs for a project
- **component design** — contains the design for a component
- **area / part** — a segment or grouping within a design; two labels for the same concept

Using a known label gives AIDE inference — it recognises what the folder is for. Using a custom label works, it just is not one AIDE knows about. The list grows as new kinds demonstrate the need. No nesting rules are defined — the labels describe what something is, not what it is allowed to contain.

## The AIDE document — `_index.md`

A file named `_index.md` placed in a folder serves as the container's description and index. The concept is called the AIDE document within the framework; the file on disk uses a generic name with no framework branding.

The underscore prefix sorts it to the top of any folder listing. The name "index" describes its function and has scope for including additional logic in future.

### Purpose

Describes what this folder is (via the role field) and indexes what it contains. In a mixed folder holding multiple parts, the body carries a parts list. Each entry in the parts list has a name, a short description, and optionally an entry point file. The parts list also records the file prefix associated with each part.

### When it earns its place

The AIDE document is optional. It earns its place when a folder's contents are not obvious from the files alone — typically when a folder holds multiple parts or when a reader needs orientation. Single-part folders with a handful of clearly-named files do not need one.

### Format

Markdown is the natural choice when the content mixes structured fields (role, parts list) and descriptive prose. If a future `_index` is primarily machine-consumed structured data, yaml or json would be the right format. Format fits the job.

## Root scope — parked

Root scope was explored as a mechanism for declaring a folder as a root of a design project, component design, or similar container. It was parked: no consumer exists. Physical folder structure provides organisation, the binder manifest preserves paths for context loading, and the path in document headers provides self-description. Root scope was compensating for context flattening, which the binder already solves.

Root scope returns if a feature demonstrates it needs a formal root declaration.

## Binder as structure preservation

The binder manifest records relative paths for every document it includes. When documents leave the file system and enter flat AI context, the manifest is what preserves their structural relationships. This is not a new mechanism — binders already do this. It is documented here because it is the reason root scope is unnecessary and physical folders are sufficient.

---

Version note: v1 — initial design from session 2026-09-10.
<!-- END SOURCE: Core/Core_Structure_Design_v1.md -->

---

<!-- BEGIN SOURCE: Core/Core_Tags_Working_v1.md -->
Core — Tags | working | Core_Tags_Working@v1 | 2026-09-10

## Status

Tags resurrected from the held candidates list during the 2026-09-09 voice session. Confirmed as a Core capability with its own area (prefix Core_Tags). Four items identified for design; standard as output, tools deferred.

## Confirmed design (2026-09-09)

### What tags are

A flat list of string keys placed in a document's header. Tags label a document for classification, discovery, and feature activation. They are a Core capability because they serve any component — not owned by a single consumer.

### Named groups

Tags may be organised into named groups for ownership purposes. A group declares which component or area owns a set of tag definitions. Groups are an authoring-time concept only — they are invisible to consumers.

**Collapse behaviour.** When tags are consumed (by search, by a tool, by any logic reading a document), groups collapse to a single flat list of distinct keys. A consumer never sees group boundaries. This keeps the consumer interface simple regardless of how many groups or owners contribute tags.

### Producer/consumer model

Any component can define tags (producer). Any logic can read tags (consumer). The openness is deliberate — tags are a shared vocabulary, not a controlled namespace. Collision between independently-defined tags sharing a key is possible and is resolved by the tag definition, not by the framework.

## Items for design

1. **Tag definition** — what a tag definition looks like, where it lives, what it must state
2. **Group-ownership model** — how groups are declared, how ownership is expressed
3. **Collapse behaviour** — the precise rule for flattening groups to a distinct list
4. **Producer/consumer openness** — any constraints on who can define or read tags, or fully open

## Output

A standard. Tools deferred — no demonstrated need for tag-manipulation tooling yet.

---

Version note: v1 — initial working document from session 2026-09-09.
<!-- END SOURCE: Core/Core_Tags_Working_v1.md -->

---

<!-- BEGIN SOURCE: Core/Core_Working_v1.md -->
Core | working | Core_Working@v1 | 2026-09-10

## Three pillars (confirmed 2026-09-09)

AIDE's components organise around three pillars — three kinds of thing that together make the framework work:

- **Building blocks** — the structural primitives. How documents are shaped (doctypes, block types, the declaration), how they identify themselves (identity, versioning), how they are organised (folders, paths, the AIDE document). Documentation Methodology owns this pillar.

- **Workflows** — the behavioural patterns. How a person works with AI across sessions and surfaces: the development lifecycle, capture-and-place, handoffs, work management, file operations. Working Practices owns this pillar, with Project Design and Build owning the design-and-build path within it.

- **Standards** — the guidance layer. Rules, expectations, and context that shape decisions and behaviour while work is being done. The Standards component owns what a standard is and how one is authored; individual standards are owned by the component that knows the most about their subject.

The overview sits in Core because it is a framework-level concept — it describes how AIDE's parts relate to each other. The individual pillars are owned by their respective components.

This is a framing concept, not a hierarchy. Components do not belong to pillars; they contribute to them. A component like Migration contributes to both workflows (how change actions are executed) and standards (what a migration record looks like).

---

Version note: v1 — initial working document from session 2026-09-09.
<!-- END SOURCE: Core/Core_Working_v1.md -->

---

<!-- BEGIN SOURCE: Documentation Methodology/_index.md -->
# Documentation Methodology

Role: component design
Aliases: DocMeth, DM

Documentation Methodology defines how documents are structured and created — the generic mechanics. It owns the grammar of documents: doctypes, block types, the declaration, rendering rules, and the structural conventions that make documents portable and machine-readable. It is not a registry of types belonging to other components — specific doctypes and block types live with whoever knows the most about them.
<!-- END SOURCE: Documentation Methodology/_index.md -->

---

<!-- BEGIN SOURCE: Documentation Methodology/DocMeth_Decisions_v1.md -->
Documentation Methodology | decisions | DocMeth_Decisions@v1 | 2026-09-10

## Status

Awaiting the full design pass. Reasoning from the rebuild sessions covering doctypes, block types, versioning, and format rules will be consolidated here from the settled rebuild decisions and session transcripts.
<!-- END SOURCE: Documentation Methodology/DocMeth_Decisions_v1.md -->

---

<!-- BEGIN SOURCE: Documentation Methodology/DocMeth_Design_v1.md -->
Documentation Methodology | design | DocMeth_Design@v1 | 2026-09-10

## Status

Awaiting the full design pass. Substantial content exists in the settled rebuild decisions (extracted from WIP v22) covering the doctype/block-type model, the block catalogue, the versioning model, format rules, and the decisions doctype. This document will be populated when that material is worked through.
<!-- END SOURCE: Documentation Methodology/DocMeth_Design_v1.md -->

---

<!-- BEGIN SOURCE: Documentation Methodology/DocMeth_Working_v1.md -->
Documentation Methodology | working | DocMeth_Working@v1 | 2026-09-10

## Confirmed items — session 2026-09-10

### File naming convention

Recommended pattern: `{Prefix}_{DocType}_v{N}.md`. Applied by default, not enforced. Deviate and you manage your own file identification. The header is authoritative for identity, doctype, and path; the filename mirrors for human readability.

### Format fits the job

Choose the format that best serves the document's primary consumer and content shape. Markdown for prose-heavy documents. Yaml or json for structured data. Html where appropriate. The declaration header and block model work across formats — this is already settled in the block catalogue rendering rules. Format is a considered choice, not a default.

### Prefix convention

File prefixes identify the subject — typically the area, part, or component name. Recommended and applied by default. A prefix makes a file distinguishable in search results, open-file lists, and folder listings regardless of whether it sits in its own subfolder or flat alongside other files.

### Binder as a doctype

The binder is owned as a doctype definition by Documentation Methodology — its structure as a document, how to read it, what a binder contains. The concept of the binder — why it exists, how it is built, inclusion rules, how it delivers content to the platform — is owned by Working Practices / Content Delivery.

---

Version note: v1 — initial working document from session 2026-09-10.
<!-- END SOURCE: Documentation Methodology/DocMeth_Working_v1.md -->

---

<!-- BEGIN SOURCE: Infrastructure/_index.md -->
# Infrastructure

Role: component design

Infrastructure defines how to build and deploy utilities, and owns the design of the delivery mechanism (the `aide` dispatcher). It is a methodological component — it does not hold all utility designs. Individual utility designs live with the component or area that knows the most about them, under the what-knows-most-about-it principle.

Infrastructure is machinery that acts on the corpus and environment from outside the AI session. It is never loaded into session context and does not shape in-session decisions.

## Key distinction

Infrastructure utilities are not capability Tools. Capabilities (Standards, Tools) are loaded into the AI session to shape behaviour. Utilities run outside the session, acting on files, folders, and the environment.
<!-- END SOURCE: Infrastructure/_index.md -->

---

<!-- BEGIN SOURCE: Infrastructure/binder-builder/binder_builder_Documentation_settings.json -->
{
  "_comment": "Settings for the binder builder. This file IS the binder definition - it declares what the binder contains. One binder per copy of the tool: a second binder means a second folder with its own copy of the script and its own settings, not a second entry here. Any key starting with _comment is ignored by the tool - JSON has no comment syntax, so notes live in keys like this one.",

  "_comment_name": "The binder's name. Used in the heading (\"<name> Binder\"), in the binder filename (\"<name>_Binder_v<number>.md\"), and in this settings file's own name (\"binder_builder_<name>_settings.json\") and log (\"binder_builder_<name>.log\"). It also identifies this binder on the command line, and no two definitions in one folder may share it.",
  "name": "Documentation",

  "_comment_root": "The folder the binder is built from, including everything beneath it unless subfolders is false. A relative path is resolved against the folder this script lives in, so \"..\" means the parent folder. Give a full path such as \"C:/Users/you/Documents\" to point somewhere else. Forward slashes are safe on Windows.",
  "root": "..",

  "_comment_subfolders": "true walks the whole tree from root. false collects from root only.",
  "subfolders": true,

  "_comment_paths": "include and exclude accept three kinds of path. ABSOLUTE - \"C:/Docs/_binder\" - names one exact folder. ROOT-ANCHORED - \"~/_binder\" - names one exact folder, measured from the root above. RELATIVE - \"_binder\" - is a pattern rather than a place: it matches every folder in the tree whose path ends with those segments, so one entry covers a _binder subfolder wherever it appears. Note that ~ means the root of the tree here, never your home folder.",

  "_comment_defaults": "The tool skips two kinds of folder by default, without any entry in exclude. (1) Any folder whose name starts with an underscore. (2) The asset folders: assets, images, img and media. Use include to override a default skip for a specific folder. include does not include a default-skipped folder's own default-skipped children, so including _rebuild does not include _rebuild/_superseded.",

  "_comment_include": "Folders skipped by default that should be collected from anyway. See _comment_defaults above for what is skipped, and why including one folder does not include its underscore-prefixed children.",
  "include": [],

  "_comment_exclude": "Folders to skip entirely, along with everything inside them. Exclude always wins over include. A relative entry here is powerful: \"_superseded\" would skip every _superseded folder in the tree.",
  "exclude": [],

  "_comment_file_types": "File extensions to collect, without the dot.",
  "file_types": ["md", "yaml", "yml", "json", "txt", "py"],

  "_comment_exclude_files": "Files to skip. Applied AFTER file_types has chosen what to collect, so this setting only ever removes, and it is the last word. Three forms, the same convention include and exclude use for folders. FILENAME - \"*_WIP_*\" - matched against the name wherever the file appears. ROOT-ANCHORED - \"~/_rebuild/*.json\" - one exact path, measured from the root. TRAILING - \"_rebuild/*.json\" - a pattern rather than a place: any file whose path ends with those segments, so one entry covers a _rebuild folder wherever it appears.",

  "_comment_exclude_files_wildcards": "? matches one character. In the two path forms * stops at a folder separator and ** crosses them: \"~/_rebuild/*.json\" is JSON directly in _rebuild, while \"~/_rebuild/**/*.json\" is JSON in _rebuild and everything beneath it. The filename form has no separators to stop at.",

  "_comment_exclude_files_convention": "The working document - work in progress, working notes - is what belongs here: it is loaded separately when active state is needed. The test is durability, not cadence. Work registers and open-items documents outlive the session and belong IN the binder, so never exclude them here. Example: [\"*_WIP_*\", \"*_WIP.*\"]",
  "exclude_files": [],

  "_comment_order": "Optional. Filenames pulled to the front of the binder, in the order listed. Everything not named here follows, sorted by path. A name that matches nothing in scope is reported, not silently ignored.",
  "order": [],

  "_comment_output": "The folder the binder is written to. Absolute, or \"~/\" for root-anchored, or relative to the script folder. The default \"~/_binder\" is an underscore folder inside the root, so it is skipped by the walk and a binder can never contain itself.",
  "output": "~/_binder",

  "_comment_log_file": "Where the run log is appended. One entry per run, never overwritten. Absolute, or \"~/\" for root-anchored, or relative to the script folder. Leave this out entirely and the log is named for the binder - binder_builder_<name>.log - which is what keeps four definitions in one folder from interleaving four runs in one file. Set it explicitly to point several binders at one log on purpose.",
  "log_file": "binder_builder_Documentation.log"
}
<!-- END SOURCE: Infrastructure/binder-builder/binder_builder_Documentation_settings.json -->

---

<!-- BEGIN SOURCE: Infrastructure/binder-builder/BinderBuilder_Design_v10.md -->
# Binder Builder — Design

> **Version 10** (2026-09-08). **Reverses §5a's empty-scope rule.** An empty scope now writes an
> empty binder, stamped as empty on its own face, instead of writing nothing and leaving the
> previous binder in place. The old rule protected a good binder from being replaced by an empty
> one; what it actually produced was a binder that went on asserting content the scope no longer
> held. See D18.
>
> v9 (2026-09-08) named a settings file and its log for the binder they belong to —
> `binder_builder_{name}_settings.json` and `binder_builder_{name}.log` — so a folder holding
> four definitions can be read without opening any of them. Older filenames still work: the
> discovery glob was widened, not replaced.
>
> v8 (2026-09-08) gave `exclude_files` the same three path forms as `include` and
> `exclude`, so an exclusion can name where a file is and not only what it is called. Added §4c, the
> scope resolution order as five layers, requested in `binder-settings/aide-rebuild-chat/001`. Added
> a `_comment_defaults` key to the shipped settings so the invisible default skips are visible to a
> reader of the settings file. Existing settings files were unaffected: an entry with no `/` in it
> behaves exactly as it always did.
>
> v7 (2026-09-08) replaced the live-state convention with the durability test. v6 corrected v5's
> claim that registers are excluded. v5 (2026-09-07) added several binder definitions per folder —
> see §4b and BinderBuilder D13.

**Master/source folder:** `Documentation/Infrastructure/binder-builder`
**Run from:** a copied instance folder with its own settings and log, e.g. `Documentation/_tools`

---

## Contents

- **Objective and boundary** — what it does and what it deliberately doesn't.
- **Inputs** — settings file: root, folder scope, file scope, output.
- **Path logic** — absolute, folder-relative and root-relative forms.
- **Path forms for `exclude_files`** — the same three, applied to files.
- **Processing model** — walk, collect, order, assemble.
- **Change detection** — when a rebuild is skipped, and when it never is.
- **Several definitions in one folder** — many binders, one run.
- **Scope resolution, as layers** — the five layers, and what each can do.
- **Binder output format** — header, manifest, source delimiters.
- **Versioning and output placement.**
- **Execution behaviour** — live by default, dry run, double-click.
- **Definition of done.**
- **Decisions** — with reasons.

---

## 1. Objective and boundary

**Objective.** Gather the current documents of a defined scope into a single file that can be
dropped into an AI session's context, so a whole topic loads as one artefact rather than many.

**Boundary — hard.** It collects and assembles. It does **not** resolve versions (that is version
cleanup's job, run first) and it does **not** deploy. It is Infrastructure: it acts on the corpus
and is never loaded into an AI session itself.

**Shape.** A single-action tool, sibling to version cleanup. No actions framework, no shared base
class, no plugin system. One instance folder may define several binders (§4b); each is still one
settings file, one scope, one output.

**Pipeline position.** `version cleanup` → `binder builder`. Version cleanup leaves only current
documents in the live tree, so the binder builder can take what it finds without version reasoning.

---

## 2. Inputs — the settings file

JSON, read on launch. A settings file **is** a binder definition: it declares one binder's scope.
An instance folder may hold several of them — see §4b.

| Setting | Purpose |
|---|---|
| `root` | The path the binder is built from. Anchor for root-relative paths. |
| `subfolders` | `true` — walk the tree from root. `false` — process `root` only. |
| `include` | Folders to process that would otherwise be skipped. |
| `exclude` | Folders to skip. |
| `file_types` | Extensions to include. Default: `md`, `yaml`, `yml`, `json`, `txt`, `py`. |
| `exclude_files` | Files to skip. Filename patterns, or path-qualified patterns — see §3a. Applied after `file_types`; see §4c. |
| `order` | Optional. Filenames pulled to the front of the binder, in the order listed. |
| `output` | Folder the binder is written to. |
| `name` | The binder's name. Used in both the `# <name> Binder` heading and the `<name>_Binder_v<N>.md` filename. Must contain no path separator. |
| `log_file` | Log file location. Named to match version cleanup; the two tools must not disagree on the name of the same setting. |

The script writes a commented default settings file if none is present, rather than failing.

### Default folder exclusions

Skipped unless explicitly included:

- Folders with a leading underscore — this keeps the tool out of `_superseded` and out of its own
  `_binder` output.
- Asset folders by name: `assets`, `images`, `img`, `media`.

---

## 3. Path logic

Three forms, resolved as follows. **This supersedes the script-relative behaviour built into
version cleanup v1**; both tools should share this rule.

| Form | Example | Meaning |
|---|---|---|
| **Absolute** | `C:/…/Documentation/_binder` | Exact folder. Survives the instance being moved. |
| **Folder-relative** | `_binder` | A **pattern**, tested against every folder the walk reaches: matches any folder whose path **ends with those segments**. Multi-segment works — `_binder/current` matches any `…/_binder/current`, and the walk passes through the underscore parent to reach it without processing that parent. |
| **Root-relative** | `~/_binder` | Anchored to the `root` setting. One exact folder. |

**Ratified as the Infrastructure-wide convention** (version-cleanup/claude-code/001, 2026-09-04).

**Rejected as errors, not silently tolerated:** `..` inside a relative entry (a pattern has no
anchor for it), bare `~`, `~name`, and `~/` in the `root` setting.

**Consequence, deliberate:** `~` no longer means home directory anywhere in these settings. Home
expansion is dropped for include and exclude paths.

**Consequence, deliberate:** a short exclude entry is powerful. `"exclude": ["_superseded"]` removes
every such folder in the tree. That is the intent, but it means an innocuous-looking entry can take
out a whole class of folders. Prefer absolute or root-relative for anything non-obvious.

**Including a folder does not include its underscore children.** `_binder` included still skips
`_binder/_superseded`.

---

## 3a. Path forms for `exclude_files`

`exclude_files` takes the same three forms §3 gives `include` and `exclude`, read as files rather
than folders:

| Form | Example | Meaning |
|---|---|---|
| **Filename** | `*_WIP_*` | Matched against the name alone, wherever the file appears. |
| **Root-anchored** | `~/_rebuild/*.json` | One exact path, measured from `root`. |
| **Trailing** | `_rebuild/*.json` | A **pattern**: any file whose path ends with those segments, so one entry covers a `_rebuild` folder at any depth. |

**An entry with no `/` in it is the filename form and behaves exactly as it always did.** That is
what makes this change invisible to every settings file written before it.

### Wildcards

`?` matches one character. `*` and `**` differ between the forms, and the difference is the point:

| Pattern | `_rebuild/notes.json` | `_rebuild/sub/notes.json` |
|---|---|---|
| `~/_rebuild/*.json` | matches | **no** |
| `~/_rebuild/*/*.json` | **no** | matches |
| `~/_rebuild/**/*.json` | matches | matches |

In a path form **`*` stops at a folder separator and `**` crosses them**, `**` standing for zero or
more whole segments. In the filename form there are no separators to stop at, so `*` is
unrestricted as before.

**This is glob's rule, not `fnmatch`'s, and the substitution is deliberate.** `fnmatch`'s `*`
matches `/` as well as everything else, so `~/_rebuild/*.json` under `fnmatch` would also match
`_rebuild/anything/deep/x.json` and the qualification would mean nothing at all. See D15.

**Refused, not tolerated:** a bare `~`, `~name`, and `..` anywhere in a path form — the same
rejections §3 makes, for the same reason. A pattern that cannot mean anything is a settings error,
not a pattern that quietly matches nothing.

Matching is case-folded the way the local filesystem folds names, and paths are spelled with
forward slashes on every platform, so one settings file behaves the same everywhere.

**The report names the pattern that dropped a file** — `SKIPPED  x.json: matches exclude_files
pattern "~/_rebuild/*.json"` — which is the question anyone with four entries in a settings file
actually has.

---

## 4. Processing model

1. Resolve settings; resolve `root`.
2. Walk from `root` (or process `root` alone if `subfolders` is false), applying folder scope rules
   at each step.
3. Collect files matching `file_types` and not matching `exclude_files`.
4. Order: files named in `order` first, in that order; everything else alphabetically by path.
5. Assemble the binder.
6. Write it to `output`, append to the log, report on screen.

**Descend and process are two separate questions.** Reaching a folder nested inside an excluded
parent means walking *through* that parent without collecting from it — which is how a
`_binder/current` include pattern traverses the underscore-prefixed parent and collects only from
`current`. Fusing the two questions would make multi-segment include patterns unreachable.

**Live state is excluded by convention, not by rule.** The tool holds no opinion about which
filenames are live state and never has: it applies the `exclude_files` patterns a binder's own
settings give it, and hard-coding names into the tool is what this sentence exists to forbid.

The convention itself belongs to the corpus, not to this tool, and is stated here only so that a
settings file can be read against it. The test is one line:

> **The test is durability, not cadence.**
>
> The working document holds what is current-and-transient, plus pending content destined for
> masters not yet written. Everything that outlives the session is binder-class.

| Class | In the binder? |
|---|---|
| **The working document** — work in progress, working notes | **No.** Loaded separately when active state is needed. |
| **Work registers** | **Yes.** |
| **Open-items documents** | **Yes.** A parked question outlives the session by definition — that is what parking means. |

**Cadence is not the test, and mistaking it for one is the trap.** Registers and open-items
documents both churn at session cadence in raw terms. The discipline that makes them binder-safe is
that they are *written at master update*, and that discipline is available to any document. What
cannot be made binder-safe is content that is meaningless outside the session that produced it.

Items accumulate in the working document between master updates and move across when masters
update, so a reader wanting current register or open items checks the working document **as well
as** the register or open-items document.

**History, because both corrections were made against this tool's settings and both mattered.** v5
and earlier listed registers among the excluded, which was wrong (corrected v6, from
`tool-pipeline/aide-rebuild-chat/002`). v6 admitted registers on a cadence argument, which reached
the right answer by the wrong route and left open-items documents excluded; the owner replaced it
with the durability test in `tool-pipeline/aide-rebuild-chat/003`.

In both cases the running instance's `exclude_files` carried the pattern in question, invisible
only because no such document existed yet. Each would have dropped a document out of the binder the
moment the first masters landed — a binder that looks complete and quietly is not, which is the
failure §5a exists to make loud. A convention error in this table is not a documentation matter; it
is a defect waiting for its first input.

---

## 4a. Change detection

A binder is a derived artefact. If every in-scope file is byte-for-byte what it was when the last
binder was written, rebuilding produces the same content under a new version number and pushes a
perfectly good binder into `_superseded` for nothing. Untidy when someone runs the tool by hand;
wasteful once the FileUpdatePackage deployer runs it after every deploy.

**The comparison needs no new state.** The answer is already in the binder: §5's manifest lists
every file it contains with a digest of that file's content. Reading that manifest back and
comparing it against the digests this run computed answers "has anything in scope changed" exactly
— additions and removals included, because the comparison is over the *set* of files as well as
over the digests.

1. Assemble as normal, computing a digest per file. Nothing is written yet.
2. Parse the manifest of the current binder into filename → digest pairs.
3. Same set of labels, same digests → report `NO CHANGES`, write nothing, supersede nothing,
   consume no version number. Otherwise rebuild as normal.

**Every uncertainty resolves towards rebuilding.** The tool always builds when:

| Case | Why |
|---|---|
| No previous binder | First run. Nothing to compare against. |
| The previous binder cannot be read, or is not UTF-8 | No baseline. |
| Its manifest heading is absent, or any entry will not parse | The contents of that binder cannot be established, and guessing at the rest would be worse than rebuilding. |
| The previous binder is stamped `INCOMPLETE` | It is missing files by definition, so "nothing changed" measured against it would hold the hole open indefinitely. |
| A source could not be read *this* run | The run is already incomplete; §5a governs it, not this section. |
| `--force` | The stated override. |

The asymmetry is deliberate. An unnecessary rebuild costs a version number. A wrongly skipped one
leaves a binder that misrepresents the tree, which is the failure this tool exists to prevent.

**Report.** `NO CHANGES` live, `WOULD CHECK` in a dry run. Both name the binder compared against.
Every run — skipped or not — also carries a `change detection:` line in the report header stating
what the comparison found, so a log entry that rebuilt says why it rebuilt and not only that it did.

**The check is placed before the `INCLUDED` events are raised**, not after: a run that rebuilds
nothing must not claim to have included anything.

**The comparison reads the format §5 writes.** The manifest reader and the manifest writer are two
halves of one contract and have to change together. The reader is deliberately lenient about the
separator between the filename and the digest and strict about everything else, so a hand-tidied
binder still parses while an unrecognisable one falls back to rebuilding.

---

## 4b. Several definitions in one folder

Every `binder_builder_settings*.json` in the script's own folder is a binder definition. So a folder
holds `binder_builder_settings.json`, and beside it `binder_builder_settings_projectdesign.json`,
`binder_builder_settings_infrastructure.json`, and as many more as the corpus needs. **One run
builds all of them**, in file order — the plain name first, then the rest alphabetically.

**A binder is identified by its `name` setting.** That was already required to be unique: it names
the output file and drives the version scan, so two definitions sharing a name would supersede each
other's binder on alternate runs. Sharing is refused before anything runs, naming both files.

### File naming

The name goes in the filenames too, so a folder of four definitions can be read without opening any
of them:

| File | Form | Example |
|---|---|---|
| Settings | `binder_builder_{name}_settings.json` | `binder_builder_AIDE_Documentation_settings.json` |
| Log | `binder_builder_{name}.log` | `binder_builder_AIDE_Documentation.log` |

**The log name is derived, not required.** A definition that says nothing about `log_file` gets a
log named for itself, which is what keeps four definitions from interleaving four runs in one file.
Setting `log_file` explicitly still points several binders at one log, deliberately, and that
remains a legitimate choice — one file per folder in run order is exactly what someone auditing a
whole folder wants.

**The filename is a convention, not an input.** The tool reads the `name` *setting*, never the
filename, so the two can in principle disagree — nothing breaks if they do, and `--list` prints
them side by side, which is where a disagreement shows up. Enforcing agreement was considered and
rejected: it would break the two older spellings below for no gain beyond tidiness.

**Older filenames still work.** The discovery glob is `binder_builder*settings*.json`, deliberately
wider than the convention, and matches all three of:

- `binder_builder_{name}_settings.json` — the convention.
- `binder_builder_settings.json` — the original single-definition name. Sorts first when present.
- `binder_builder_settings_{x}.json` — the spelling this document recommended between v5 and v8.

A convention tidied after publication must not break the files written while the old one stood. See
D17.

### Selection

| Command | Effect |
|---|---|
| `python binder_builder.py` | Every definition in the folder. |
| `python binder_builder.py ProjectDesign Infrastructure` | Just those two. |
| `python binder_builder.py --list` | What is defined here. Builds nothing. |

A selector matches a binder's `name`, or the filename of its settings file with or without the
extension, case-insensitively. **A selector that matches nothing stops the whole run** and prints
what is available: "build these four", three-quarters done, is worse than not started.

`--dry-run` and `--force` apply to whatever was selected.

### Isolation

One definition failing must not take the others down — the entire point of the feature is that four
binders stay current, and one mistyped settings file is not a reason for three good binders to go
stale. So a settings file that cannot be read, or one whose `root` does not exist, is reported as
its own `SETTINGS PROBLEM` block and the run carries on with the rest. The run exits `1`.

An unreadable settings file is reported **whether or not the run was narrowed to other binders**. It
is a fact about the folder rather than about the selection.

### The roll-up

When more than one binder ran — or when a settings file could not be read — the run ends with one
line for the folder as a whole:

```text
========================================================================
Result: 4 binder(s) - 1 rebuilt, 2 unchanged, 1 with problems
========================================================================
```

It is **not** printed when a single definition ran cleanly. A folder holding one binder therefore
produces exactly the output it always did, and anything reading the last `Result:` line of this
tool's output — the FileUpdatePackage deployer does — keeps working in both cases, reading the
per-binder line when there is one binder and the roll-up when there are several.

The roll-up is not written to any log: definitions may have different `log_file` settings, and a
folder-level line has no single log to belong to. Every binder's own report is logged as always.

### What makes this safe

A build reads no global state. Every path, every scope, every digest and every log in a build comes
out of one definition, so building four is building one, four times. The `_binder` output folder can
be shared because the version scan, the self-inclusion guard and supersession all match on the
binder's own `<name>_Binder_v<N>.md` class (§6, D9) — `ProjectDesign_Binder_v3.md` and
`Infrastructure_Binder_v7.md` sit side by side without either touching the other.

**The exception, stated:** if an output folder is deliberately brought *into* a binder's scope with
an `include`, that binder's self-inclusion guard will skip its own binders and swallow its
neighbours'. The default `_binder` is underscore-prefixed and therefore outside every walk, so this
cannot happen by accident.

**Change detection is what makes it cheap** (§4a). Four definitions where nothing has changed cost
four manifest comparisons and no writes at all.

---

## 4c. Scope resolution, as layers

Scope is decided in five layers. **Each layer can only narrow what the previous one admitted**, and
at any level an exclusion beats an inclusion.

| Layer | Rule |
|---|---|
| **1 — Defaults** | Underscore folders and the asset folders `assets`, `images`, `img`, `media` are skipped unless overridden. |
| **2 — Include** | Overrides a default skip for named folders. Including a folder does not include its own default-skipped children. |
| **3 — Folder exclude** | Wins over include, always, along with everything beneath. |
| **4 — File types** | Only the listed extensions are collected from in-scope folders. |
| **5 — File exclude** | `exclude_files` drops matching files from what layer 4 admitted. The last word. |

**Layers 4 and 5 are sequential, not independent** — `exclude_files` is applied to what `file_types`
already selected. Confirmed against the build, and it has one observable consequence worth stating:
a file whose extension is not in `file_types` is dropped at layer 4 and never reaches layer 5, so it
produces no `SKIPPED` event. Only files that were genuinely in scope and then excluded are reported.
That is deliberate — §7 explains why unlisted extensions are silent — but it means the report shows
layer 5's decisions and not layer 4's.

Because layer 5 can only remove, a path-qualified pattern there **cannot conflict with a folder-level
include or exclude.** It can make an included folder contribute less; it can never make an excluded
folder contribute anything. That is what makes adding path qualification at layer 5 safe rather than
a second, competing scope language.

**The layers are stated in a settings file too, not only here.** `_comment_defaults` in the shipped
settings names layer 1 in plain language, because layer 1 is the only one with no entry anywhere to
show for it — a reader who has never seen this document would otherwise have to infer the underscore
and asset-folder rules from behaviour. See D16.

---

## 5. Binder output format

```markdown
# <Name> Binder

> **Generated Binder — do not edit directly.** Edit the individual master documents
> and regenerate the Binder.
> **Binder Version <N>** (<date>).

This Binder is a current-context consumption artefact; authoritative masters remain
individual files.

## Binder manifest

- `<filename>` — sha256 `<12-char digest>`
- `<filename>` — sha256 `<12-char digest>`

---

<!-- BEGIN SOURCE: <filename> -->
<full file content, unmodified>
<!-- END SOURCE: <filename> -->

---

<!-- BEGIN SOURCE: <next filename> -->
…
```

- Source content is copied **unmodified**, with exactly two stated exceptions:
  - A trailing newline is added where a source lacks one, so the closing delimiter sits on its own
    line.
  - A leading byte-order mark is stripped. A BOM is a start-of-file marker; one left embedded
    halfway down a binder puts a stray `U+FEFF` in the middle of the text.
- **Encoding.** Read bytes and decode `utf-8-sig`. Write UTF-8 without BOM, **in binary mode** —
  text mode on Windows rewrites every `\n` as `\r\n` and would silently alter every source line
  ending in the binder.
- Manifest lists files in binder order.
- Digests are truncated sha256, twelve characters, computed over **the source content as read**,
  not the section as written. D3's purpose is answering "does this binder match the masters"; a
  digest including the tool's own added newline answers a different question.
- **No hand-written change note** in the header — see Decision D2.
- Where assembly is incomplete, a block near the top of the binder lists every missing file.

---

## 5a. Incomplete and empty runs

The two cases look alike and are opposite. **An incomplete binder is defective; an empty binder is
correct.** A binder missing files it should contain cannot be trusted about anything. A binder
containing nothing, because nothing was in scope, is an accurate statement about the tree.

| Case | Behaviour |
|---|---|
| **Empty scope** — no in-scope files found | **Write the binder.** It carries an `EMPTY BINDER` block in its header and a manifest reading `(no files)`. The previous binder is superseded as usual. Report `EMPTY`. |
| **Incomplete** — a source cannot be read or decoded | Write the binder, but do **not** supersede the previous one, so the last good binder stays available beside the holed one. Report `ERROR` naming the file, plus `INCOMPLETE`, and list the missing files in the binder's own header block and the log. |

The rule for the incomplete case is unchanged: **a defective binder never displaces a good one.**

**Change detection covers the empty case** (§4a), which is what stops it churning. An empty scope
whose current binder is already empty compares equal — nothing added, nothing removed — and reports
`NO CHANGES`. Only a transition into or out of empty writes anything.

**`EMPTY` is reported even when nothing is written**, because an empty scope is far more often a
mistake in the settings than a true statement about the tree, and nobody should have to infer it
from a binder with nothing in it.

---

## 6. Versioning and output placement

**Name:** `<name>_Binder_v<N>.md`, with its own counter independent of the documents inside.

**Version resolution:** scan the output folder for existing binders of that name, take the highest
`N`, write `N+1`. Self-managing; no version recorded in settings.

**Placement:** the output folder is declared in settings. Default `_binder` beside the masters — an
underscore folder, therefore excluded from the walk by default.

**Self-inclusion guard.** Skip any file in the output folder matching `<name>_Binder_v<N>.md`.

This is stated against the **artefact class**, not the artefact. A guard written against "the file
I am about to write" defends nothing, because that file does not exist when the guard runs — but
*last* run's binder does, and would be swallowed as an ordinary source, doubling the corpus on
every build. See Decision D9.

**Supersession:** on a successful and complete write, the binder builder moves the previous binder
of that name into `_superseded` inside the output folder. See Decision D7.

---

## 7. Execution behaviour

Matches version cleanup, so the tools behave alike:

- Python, standard library only, single readable script.
- Runs **live by default**; `--dry-run` reports what would be assembled and writes nothing.
- `--force` rebuilds even when §4a finds nothing changed. It is the only way to consume a version
  number deliberately.
- Naming one or more binders builds only those; `--list` shows what is defined. See §4b.
- Reads settings on launch — no arguments required, so **double-click works on Windows**, and a
  double-click builds every binder defined in the folder.
- Prints a clear report; **pauses for a keypress before exiting** so the console doesn't vanish.
- Appends one entry per run to the log: binder written, version, files included, any skipped.
- Cross-platform; Windows primary.

### Report vocabulary

`INCLUDED` / `WOULD INCLUDE` · `SKIPPED` · `UNMATCHED` · `NO CHANGES` / `WOULD CHECK` ·
`WRITTEN` / `WOULD WRITE` · `SUPERSEDED` / `WOULD SUPERSEDE` · `CONFLICT` · `EMPTY` ·
`INCOMPLETE` · `ERROR`

`NO CHANGES` is §4a: nothing in scope has changed, so no binder was written and the previous one
remains current. `WOULD CHECK` is the dry-run twin — the same comparison, reported rather than
acted on. Neither is a failure; both exit `0`.

`CONFLICT` and `ERROR` carry version cleanup's meanings exactly. `UNMATCHED` is an `order` entry
naming a file not in scope — a binder assembled in an order its author did not get is a quiet
defect, so it is reported. Files whose extension is simply not in `file_types` are **not** reported;
a document tree is full of them and listing each would bury the report.

**Exit code `0` unless an `ERROR` occurred**, matching version cleanup. An `EMPTY` run exits `0`:
it wrote a binder, and the binder is correct. See §10.

---

## 8. Definition of done

Point an instance at a scope and it produces a single, correctly-versioned binder containing every
in-scope current document, with a manifest matching its contents, source files copied unmodified,
a readable on-screen report and a log entry. Dry run produces the same report and writes nothing.

An `exclude_files` entry naming a path — `~/_rebuild/*.json` — drops exactly the files at that
path and no others; the same entry written without a `~/` prefix drops them under a folder of that
name at any depth; an entry with no `/` behaves as it always did. A pattern that cannot mean
anything stops that binder with an explanation rather than matching nothing quietly. The report
names the pattern that dropped each file.

A folder of four definitions can be read from its file listing alone: each settings file and each
log carries its binder's name. A settings file written under either older spelling is still
discovered and built.

Put four settings files in one folder and one run keeps all four binders current, each reported
separately and the folder summarised in one line. Name one on the command line and only that one is
built. Name something that is not defined and nothing is built at all. Break one settings file and
the other three still build.

Point it at a scope that is empty and it writes a binder saying so, stamped `EMPTY BINDER` in its
own header, rather than leaving a binder that asserts content the scope no longer holds. Run it
again with the scope still empty and it writes nothing further.

Run it a second time with the tree untouched and it writes nothing, supersedes nothing, consumes no
version number, and says `NO CHANGES` naming the binder it compared against. Change, add or remove
any in-scope file and the next run rebuilds. `--force` rebuilds regardless. A run that cannot
establish a baseline — no previous binder, an unreadable one, an unparseable manifest, a previous
build stamped `INCOMPLETE` — rebuilds rather than skipping.

---

## 9. Decisions

**D1 — The settings file is the binder definition.** No separate definition document. The scope
declaration and the run configuration are the same information; splitting them would create two
things to keep in step. *The second half of this decision — one instance folder per binder — is
reversed by D13; the first half stands and is what makes D13 work.*

**D2 — Drop the hand-written change note from the binder header.** The old format carried an
authored line describing what changed in that issue. A generator cannot write it, and the binder is
a disposable regenerated artefact — a changelog on it duplicates the version lines the masters
already carry. *Reversible if a real need appears: add a `note` setting.*

**D3 — Keep the sha256 manifest digests.** Weak keep. They cost nothing to generate and answer
"does this binder match the masters" if a verification tool ever wants them.

**D4 — No partitioned binder sets.** The old corpus split one topic across five binders plus a set
index because of volume. Real problem, not today's problem. Build one binder per instance; revisit
if a topic genuinely exceeds a usable context.

**D5 — Version resolution by scanning output, not by settings.** A version number in settings is
state that drifts from reality. The folder is the truth.

**D6 — Path logic is shared with version cleanup.** Folder-relative evaluated per walk step,
root-relative via `~/`, absolute exact; home expansion dropped. Two Infrastructure tools with
different path semantics would be a trap.

**D7 — The binder builder supersedes its own previous output.** On a successful write it moves the
prior binder of that name into `_superseded` within the output folder.

*Considered and rejected:* leaving it for version cleanup. Rejected because the default output
folder is `_binder`, which version cleanup skips by the underscore rule — it would have to be
explicitly included purely to tidy up after every build. And this is not general supersession: the
tool knows exactly which single file it just replaced, so there is no scanning, grouping or version
reasoning to duplicate.

**Principle:** a tool cleans up after itself. Version cleanup handles supersession it didn't cause.

**D8 — `output` and `name` are two settings.** v1 gave one key described as carrying both the
folder and the binder's name. One key cannot do both jobs; the heading and the filename need the
name, the write needs the folder. Split, with `name` rejecting any path separator.

**D9 — Guards are written against the artefact class, not the artefact.** v1's self-inclusion check
("if a resolved input file is the output path, skip") is a no-op: the output file does not exist
when the guard runs. The previous run's binder does, and was swallowed as a source in test — six
files became seven, and the corpus would double on every build. The rule is to match the class
`<name>_Binder_v<N>.md`.

*Generalisable:* any Infrastructure tool that both reads and writes inside one tree needs its guard
written this way. This belongs to the Infrastructure container definition when that is written.

**D10 — Digests cover source content, not the written section.** They differ by one byte where a
source lacks a trailing newline. D3's stated purpose is comparison against the masters, so the
digest must describe the master.

**D11 — BOM stripping is a stated exception to byte-for-byte copying.** Accepted deliberately, and
named here so it is not later read as a defect.

**D13 — Several definitions in one folder, discovered by glob.** v1 to v4 said one binder means one
instance folder. That was right for what the tool then was and is wrong for what it now is.

*What changed underneath it.* The original reasoning was that a second binder in one settings file
would mean a settings schema with a list of binders in it, and every setting then having to say
which binder it belonged to — a configuration format growing a dimension. That objection still
holds, and this is not that: **one file is still exactly one binder**, with the schema untouched.
What is new is that the folder, not the file, is the unit of "everything here".

*What made it worth doing.* Change detection (D12). Before it, running four definitions meant
writing four binders and consuming four version numbers on every run, so the cost of "keep them all
current" scaled with the number of binders and running them separately was no worse. With it, three
unchanged binders cost three manifest comparisons. "Rebuild whatever needs rebuilding" became a
single cheap act, and the tool should let someone do it in one command.

*Considered and rejected:* a `--settings` argument naming a file. It solves nothing on its own — the
user still runs the tool four times, and now has to remember four filenames — and it makes
double-click, which is how this tool is actually used, the one mode that cannot reach the other
binders.

*Considered and rejected:* a separate list file naming the definitions. A second thing to keep in
step with the folder, which is the same objection as D5 to version numbers in settings. The folder
is the truth.

*Identity is the `name` setting*, not the filename, because `name` already had to be unique — it
decides the output filename. A duplicate is refused before anything runs rather than resolved,
because both plausible resolutions (first wins, last wins) silently give someone a binder they did
not ask for.

**D18 — An empty scope writes an empty binder.** Reverses the rule v1 to v9 held, that an empty
scope writes nothing and leaves the previous binder alone.

*The original reasoning, and why it was wrong.* The old rule called an empty binder replacing a good
one "a loss of information dressed up as a successful build". That framing has a false premise: the
previous binder is **superseded, not deleted** — it moves to `_superseded` beside the new one, and
recovering it is a file move. Almost nothing is lost. What the rule produced instead was worse: a
binder sitting in the output folder, presenting as current, asserting content the scope no longer
held. A stale binder that looks authoritative is precisely the failure this tool exists to prevent,
and the old rule manufactured one deliberately.

*The case that exposed it.* Exclusions are tightened until everything in scope is excluded. The tool
reported `EMPTY`, wrote nothing, and left a binder that still contained every excluded file. The
report said the scope was empty; the binder said otherwise; the binder is what gets loaded into a
session.

*What replaces the guard.* Three things, none of which the old rule provided. The binder says
`EMPTY BINDER` in its own header, so a reader who never sees a report cannot mistake it. The run
reports `EMPTY` whether or not it wrote, so a misconfigured scope stays loud. And the previous
binder is in `_superseded`, one move from being restored.

*Consequence, accepted:* a typo in `root` now supersedes a good binder with an empty one. That is a
real regression in one narrow case, recoverable by moving a file, and it is preferred to the
alternative — a stale binder that nothing announces at all.

*Generalisable:* refusing to record an unwelcome state does not prevent the state, it only removes
the record. This tool's job is to describe the tree, including when the tree is empty.

**D17 — Settings and log are named for the binder; the glob is widened rather than replaced.**
`binder_builder_{name}_settings.json` and `binder_builder_{name}.log`. The reason is the one D13
created: once a folder can hold four definitions, four files called some variation of "settings"
have to be told apart, and opening each one to find out which binder it defines is exactly the
friction D13 was meant to remove.

*The glob is `binder_builder*settings*.json`, not the convention itself.* Three spellings now exist
in the wild — this document recommended `binder_builder_settings_{x}.json` between v5 and v8, and
`binder_builder_settings.json` predates definitions entirely. Narrowing the glob to the new
convention would have silently stopped discovering files written on this document's own advice, and
a binder that stops being built without saying so is the failure mode this tool most needs to avoid.
The cost of the wider glob is that it also matches names nobody intends to write; that costs
nothing, because an unintended match is a settings file that either parses or is reported.

*The log name is derived rather than mandated.* A definition may still name its log explicitly and
share one, which is the right answer for a folder someone audits as a whole.

*The filename is not read.* Identity stays in the `name` setting, per D13. The filename is a
convenience for humans reading a folder listing, and `--list` shows both so drift is visible.

**D15 — Path-qualified `exclude_files` uses glob's wildcards, not `fnmatch`'s.** In a path form
`*` stops at a folder separator and `**` crosses them.

*Why it cannot be `fnmatch`.* `fnmatch`'s `*` matches `/`, so `~/_rebuild/*.json` would also match
`_rebuild/deep/nested/x.json`. Every path-qualified pattern would then be silently recursive, the
qualification would carry no information, and there would be no way to express "this folder only" at
all. The one thing the feature exists to do could not be said.

*Consequence, accepted:* two wildcard dialects in one settings file — `fnmatch` for the filename
form, glob for the path forms. Considered and rejected: moving the filename form to glob as well.
Under glob, `*_WIP_*` still behaves identically because a filename contains no separators, so the
change would be invisible in every case anyone has written — but it would be a behaviour change to
existing settings for no benefit, and this design has consistently refused those.

*Consequence, accepted:* `~/_rebuild/*/*.json` means "exactly one folder below `_rebuild`", not
"`_rebuild` and everything under it". The recursive form is `~/_rebuild/**/*.json`. The request that
prompted this feature described the `*/` spelling as recursive; that reading is not available
without giving `*` `fnmatch` semantics and losing the non-recursive form entirely. Raised with the
requester rather than resolved silently.

**D16 — Defaults are documented in the settings file, not only in the design.** Layers 2 to 5 of
§4c each have a key in the settings file, so a reader sees them. Layer 1 has none: the underscore
rule and the asset-folder list are enforced by the tool with nothing in the settings to show for
them, and a reader who has never opened this document can only infer them from behaviour — usually
after being surprised. `_comment_defaults` states them where that reader is already looking.

*Generalisable:* any tool in this family whose behaviour includes a rule with no corresponding
setting should state that rule in the settings file. Silent defaults are the ones that get
rediscovered by accident.

**D14 — One bad definition does not stop the good ones.** A settings file that will not parse is
reported and skipped; the rest build. The feature exists so that four binders stay current, and
"three went stale because the fourth had a trailing comma" would defeat it. The run still exits `1`.

*Consequence, accepted:* a run can be partly successful, which neither sibling tool can be. The
roll-up line exists to make that legible in one line rather than requiring the reader to scan four
report blocks.

**D12 — Change detection compares against the binder's own manifest, and keeps no state of its
own.** The alternatives were a sidecar state file recording what the last run saw, and timestamp
comparison against the binder's modification time.

*A sidecar file was rejected* because it is a second source of truth that drifts the first time a
binder is moved, restored or hand-edited — the same reasoning as D5, which put the version number
in the folder rather than in settings. The binder already carries a digest per file; that manifest
*is* the record of what the last build saw, and it cannot drift from the binder because it is part
of it.

*Timestamps were rejected* because they answer a different question. A file touched but not
changed, a checkout that rewrites every modification time, a copy across a filesystem — all move
timestamps without moving content. D3 kept the digests for exactly this purpose and this is the
verification tool it anticipated.

*Consequence, accepted:* the reader in §4a is coupled to the writer in §5. They are two halves of
one contract and are marked as such in both places.

*Consequence, accepted:* a change that leaves every digest identical — a file renamed to a name that
sorts to the same place, then back — is invisible. A digest comparison is a content comparison, and
that is the question worth answering.

---

## 10. Open

- **`EMPTY` and `NO CHANGES` exit codes.** Both are `0`, consistent with treating expected outcomes
  as non-failures. A caller therefore cannot distinguish "binder rebuilt" from "nothing written"
  by exit code alone. The FileUpdatePackage deployer, which now chains this tool, does not need to:
  it reports the binder builder's outcome by reading its report, and a skipped rebuild is a correct
  outcome for it rather than a condition to handle. Prefer a distinct exit code for "nothing
  written" over overloading the failure code if a caller ever does need to branch on it. **Not
  now.**
- **Per-definition scheduling.** Every definition is built on every run. A binder whose scope is
  expensive to walk and rarely changes still gets walked. Not a problem at four definitions over a
  corpus this size; the shape of a fix, if it is ever needed, is a `skip_unless` or an interval in
  the settings — state in a settings file, which D5 warns about. **Not now.**
- **Path-logic duplication.** The three path forms now exist in two implementations. The trigger for
  extracting shared code is a **third tool needing it**, not a third mention. The logic is pure
  functions over paths with no state, which is what has kept copying cheap.
- **The `_superceded` misspelling** at the Documentation root remains, alongside correctly-spelled
  folders. Both are underscore-prefixed so both are skipped. A human act to reconcile.
<!-- END SOURCE: Infrastructure/binder-builder/BinderBuilder_Design_v10.md -->

---

<!-- BEGIN SOURCE: Infrastructure/binder-builder/README.md -->
# binder builder

Gathers the current documents of a defined scope into a single file, so a whole
topic can be dropped into an AI session's context as one artefact rather than
as many.

This folder is the **master copy**. To use the tool, copy `binder_builder.py`
and the settings file to wherever it should run from, then edit that copy's
settings — including renaming it for the binder it defines. Each instance keeps
its own settings and its own log beside the script, so instances never
interfere with each other.

**A settings file is a binder definition.** It declares the scope. To define a
second binder, put a second settings file beside the first — one run builds them
all. See *Several binders in one folder* below.

**Run version cleanup first.** It leaves only current documents in the tree, so
the binder builder can take what it finds without any version reasoning of its
own.

**It will not rebuild for nothing.** If no in-scope file has changed since the
last binder was written, the run reports `NO CHANGES` and writes nothing. See
*Change detection* below.

---

## What it produces

```markdown
# <Name> Binder

> **Generated Binder - do not edit directly.** Edit the individual master documents
> and regenerate the Binder.
> **Binder Version 3** (2026-09-04).

This Binder is a current-context consumption artefact; authoritative masters remain
individual files.

## Binder manifest

- `Alpha/Alpha_Design_v3.md` - sha256 `06f6435c91ff`
- `Beta/beta.yaml` - sha256 `75d068ad343e`

---

<!-- BEGIN SOURCE: Alpha/Alpha_Design_v3.md -->
…the file, exactly as it is on disk…
<!-- END SOURCE: Alpha/Alpha_Design_v3.md -->

---

<!-- BEGIN SOURCE: Beta/beta.yaml -->
…
```

Source content is copied **unmodified** — no reformatting, no heading demotion,
no trimming. The manifest lists the files in binder order, with a truncated
sha256 of each source, so a binder can be checked against its masters.

The one adjustment: a newline is added after a source that does not end with
one, so the closing delimiter starts on its own line.

---

## Installing Python on Windows

Only needed once per machine. The tool uses nothing beyond the Python standard
library, so there is nothing else to install.

1. Go to <https://www.python.org/downloads/windows/> and download the latest
   **Windows installer (64-bit)**. Python 3.8 or newer is required; any current
   release is fine.
2. Run the installer. On the first screen, **tick "Add python.exe to PATH"**
   before clicking Install. This is easy to miss and is the usual reason a
   `.py` file will not run afterwards.
3. Choose **Install Now**.
4. To check it worked, open PowerShell and run:

   ```
   python --version
   ```

   It should print something like `Python 3.13.1`.

### Making double-click work

The standard installer associates `.py` files with the Python launcher, so
double-clicking `binder_builder.py` in File Explorer should just run it. If it
instead opens in Notepad or asks which app to use:

1. Right-click `binder_builder.py` → **Open with** → **Choose another app**.
2. Pick **Python** (or browse to `C:\Windows\py.exe`).
3. Tick **Always use this app to open .py files**.

The script pauses with *"Press Enter to close..."* when it finishes, so the
console window stays open long enough to read the report.

### Running it from a terminal instead

```
python "C:\path\to\binder_builder.py"
```

---

## Settings

The script reads every `binder_builder*settings*.json` in **its own folder** —
not from wherever the terminal happens to be pointing. Each one is a binder. If
the folder holds none at all, the script writes a fresh
`binder_builder_Documentation_settings.json` with default values and
explanatory notes, then tells you to check it. Since a settings file is a binder
definition, a fresh one almost always needs editing — starting with its `name`,
and then its own filename to match.

```json
{
  "name": "Documentation",
  "root": "..",
  "subfolders": true,
  "include": [],
  "exclude": [],
  "file_types": ["md", "yaml", "yml", "json", "txt", "py"],
  "exclude_files": [],
  "order": [],
  "output": "~/_binder",
  "log_file": "binder_builder.log"
}
```

| Setting | Meaning |
| --- | --- |
| `name` | The binder's name — used in the heading and in the filename. |
| `root` | The folder the binder is built from. |
| `subfolders` | `true` walks the whole tree; `false` collects from `root` only. |
| `include` | Folders to collect from that would otherwise be skipped. |
| `exclude` | Folders to skip entirely, along with everything inside them. |
| `file_types` | Extensions to collect, without the dot. |
| `exclude_files` | Files to skip — by name, or by path. Applied after `file_types`. |
| `order` | Filenames pulled to the front of the binder, in the order listed. |
| `output` | The folder the binder is written to. |
| `log_file` | Where the run log is appended. |

### Which folders are skipped by default

- Any folder whose name starts with an underscore. This is what keeps the tool
  out of `_superseded` and out of its own `_binder` output — it is the
  mechanism that makes it impossible for a binder to contain a binder.
- The asset folders `assets`, `images`, `img` and `media`, by name.

List a folder in `include` to collect from it anyway. Including a folder does
**not** include its underscore-prefixed children: `_binder` included still skips
`_binder/_superseded`.

### The three path forms

**`root`, `output` and `log_file`** take a full path, a `~/` path measured from
`root`, or a path measured from the folder the script lives in — so `".."`
means "the folder above me", and an instance sitting in `Documentation/_tools`
builds from `Documentation` by default. (`root` itself cannot use `~/`, since it
is what defines the root.)

**`include` and `exclude`** take the same three forms, but the relative one
means something different:

| Form | Example | Means |
| --- | --- | --- |
| Absolute | `"C:/Docs/_binder"` | that one exact folder |
| Root-anchored | `"~/_binder"` | that one exact folder, measured from `root` |
| Relative | `"_binder"` | a **pattern**: every folder in the tree whose path ends with those segments |

**`exclude_files` takes the same three forms**, applied to files — see
*Excluding files by path* below.

The relative form is the useful one for a corpus. `"_binder"` is not a place,
it is a shape — it matches a `_binder` subfolder wherever one appears, at any
depth. Several segments work too: `"_binder/current"` matches any
`.../_binder/current`, and the walk passes *through* the underscore parent to
reach it without collecting that parent's own files.

Two consequences worth holding on to:

- `"~"` here means **the root of the tree**, never your home folder. The tool
  never expands `~` the way a shell would.
- A relative entry in `exclude` is powerful in the same way. `"_superseded"`
  would skip every `_superseded` folder in the tree, not one of them. Prefer
  absolute or root-anchored for anything non-obvious.

This is the same path model as version cleanup, deliberately. Two Infrastructure
tools with different path semantics would be a trap.

**Writing paths in JSON.** Use forward slashes (`"C:/Users/you/Documents"`) or
doubled backslashes (`"C:\\Users\\you"`); a single backslash is an escape
character in JSON and will break the file.

**Comments.** JSON has no comment syntax, so the notes in the shipped settings
file are carried as keys beginning with `_comment`. They are ordinary JSON and
the tool ignores them. Leave them, edit them, or delete them as you prefer.

### Excluding live state

The working document — work in progress, working notes — is loaded separately
when active state is actually needed, so it is normally kept out of the binder.
Do that through `exclude_files` in the binder's own settings rather than
expecting the tool to know the names:

```json
"exclude_files": ["*_WIP_*", "*_Working_*"]
```

**Work registers and open-items documents are a different case: they belong
*in* the binder.** The test is **durability, not cadence** — everything that
outlives the session is binder-class, and a parked question outlives the
session by definition. Both churn at session cadence in raw terms; what makes
them binder-safe is that they are written at master update. Do not add a
`*_WorkRegister_*` or `*_OpenItems_*` pattern here.

Items accumulate in the working document between master updates, so a reader
wanting current register or open items checks the working document as well.

`*` matches any run of characters and `?` matches one, matched
case-insensitively on Windows and case-sensitively elsewhere — the same way the
filesystem does.

### Excluding files by path

An `exclude_files` entry containing a `/` is matched against the file's **path**
rather than its name, using the same three forms as `include` and `exclude`:

| Form | Example | Means |
| --- | --- | --- |
| Filename | `"*_WIP_*"` | the name, wherever the file is |
| Root-anchored | `"~/_rebuild/*.json"` | that exact path, measured from `root` |
| Trailing | `"_rebuild/*.json"` | a **pattern**: any file whose path ends with those segments, so it covers a `_rebuild` folder at any depth |

**An entry with no `/` in it behaves exactly as it always did**, so nothing you
have already written changes.

In the two path forms, `*` stops at a folder separator and `**` crosses them:

| Pattern | `_rebuild/notes.json` | `_rebuild/sub/notes.json` |
| --- | --- | --- |
| `~/_rebuild/*.json` | matches | no |
| `~/_rebuild/*/*.json` | no | matches |
| `~/_rebuild/**/*.json` | matches | matches |

So `*/` is "exactly one folder down" and `**/` is "here and anything below".
Use `**` when you mean recursive.

A bare `~`, a `~name`, or a `..` anywhere in a path pattern is refused with an
explanation rather than quietly matching nothing.

The report names the pattern that dropped each file:

```
SKIPPED  tool_settings.json: matches exclude_files pattern "~/_rebuild/*.json"
```

### Ordering

Files named in `order` come first, in the order listed. Everything else follows,
sorted by path. Matching is on the filename alone, so an `order` entry catches
that file wherever it lives.

An `order` entry that matches nothing in scope is reported as `UNMATCHED` rather
than passed over, because a binder assembled in an order its author did not get
is a quiet defect.

---

## Several binders in one folder

Each settings file in the script's folder is one binder, and both the settings
and the log are named for the binder they belong to:

```
_tools/
├── binder_builder.py
├── binder_builder_AIDE_Documentation_settings.json
├── binder_builder_ProjectDesign_settings.json
├── binder_builder_Infrastructure_settings.json
├── binder_builder_Methodology_settings.json
├── binder_builder_AIDE_Documentation.log
├── binder_builder_ProjectDesign.log
├── binder_builder_Infrastructure.log
└── binder_builder_Methodology.log
```

So a folder of four binders can be read from the listing without opening
anything.

To add one, copy an existing settings file to
`binder_builder_<name>_settings.json`, edit it, and set its `name` to match.

**The filename is a convention, not an input.** The tool reads the `name`
*setting*, never the filename, so nothing breaks if they disagree — but
`--list` prints them side by side, which is where you will notice.

**The log name is derived.** Leave `log_file` out and each binder gets
`binder_builder_<name>.log` automatically, so four definitions do not interleave
four runs in one file. Set `log_file` explicitly if you would rather several
binders shared one — one file per folder in run order is exactly what someone
auditing a whole folder wants.

**Older filenames still work.** `binder_builder_settings.json`, and the
`binder_builder_settings_<something>.json` spelling this README recommended
earlier, are both still discovered and built. Rename them when convenient;
nothing forces it.

**Give each one a different `name`.** The name decides the output filename, so
two binders sharing one would take turns superseding each other's file. The tool
refuses to run at all if it finds a duplicate, and tells you which two files
clash.

They can share an output folder. `ProjectDesign_Binder_v3.md` and
`Infrastructure_Binder_v7.md` sit happily side by side in one `_binder`: each
definition only ever scans, supersedes and skips binders of its own name.

They can share a log too — that is what happens if you leave `log_file` alone,
and it gives you one file with every build in it, in order. Give a definition a
different `log_file` if you would rather it kept its own.

### Running them

```
python binder_builder.py
```

builds every binder defined in the folder — which is also what double-clicking
does. Each one gets its own report, and the run ends with a line for the folder:

```
========================================================================
Result: 4 binder(s) - 1 rebuilt, 3 unchanged
========================================================================
```

To build only some of them, name them:

```
python binder_builder.py ProjectDesign Infrastructure
```

The name is the `name` from the settings file, or the settings filename itself
if that is easier to remember; either way it is matched case-insensitively. Name
something that is not defined and **nothing** is built — the tool lists what is
available instead, on the grounds that "build these four", three-quarters done,
is worse than not started.

To see what is defined without building anything:

```
python binder_builder.py --list
```

`--dry-run` and `--force` apply to whatever you selected.

### If one definition is broken

It is reported on its own and the others still build. Four binders staying
current is the point of keeping them in one folder; three of them going stale
because the fourth has a trailing comma would defeat it. The run still exits `1`,
and the roll-up counts it:

```
Result: 4 binder(s) - 4 unchanged, 1 unreadable
```

### Why this is cheap

Change detection. Four definitions where nothing has changed cost four manifest
comparisons and no writes at all, so running the lot after every edit is a
sensible habit rather than an expensive one.

---

## Versioning and output

The binder is written as `<Name>_Binder_v<N>.md`, with a counter of its own,
independent of the versions of the documents inside it.

The version is worked out by **scanning the output folder** — highest `N` found,
write `N+1`. Nothing is recorded in settings, because a number kept in settings
drifts from reality the first time a file is moved by hand.

A run that finds nothing changed does not consume a version number — see
*Change detection* below.

On a successful write, the previous binder of that name is moved into
`_superseded` inside the output folder. A tool cleans up after itself; version
cleanup handles supersession it did not cause. Nothing is ever overwritten — if
the `_superseded` slot is taken, the run reports `CONFLICT` and leaves the file
alone.

---

## Change detection

The binder is a derived file. Rebuilding it when nothing has changed produces
the same content under a new version number and pushes a perfectly good binder
into `_superseded` for nothing.

So before writing, the tool compares what it just assembled against the
**manifest of the current binder** — the list of filenames and digests in that
binder's own header. Same files, same digests, and there is nothing to do:

```
change detection: Documentation_Binder_v7.md: 24 file(s) in scope, all matching the manifest - binder not rebuilt

[_binder]
  NO CHANGES       no changes detected since Documentation_Binder_v7.md; binder not rebuilt
```

Nothing is written, nothing is superseded, and no version number is used up.
The previous binder is still the current one.

Change, add or remove any in-scope file and the next run rebuilds, saying what
it noticed:

```
change detection: Documentation_Binder_v7.md: 1 changed, 1 added (Project Design/ProjectDesign_Design_v8.md, Project Design/ProjectDesign_Index_v8.md) - rebuilding
```

There is no state file. The comparison uses the digests the binder already
carries, so there is nothing that can drift out of step with it — and nothing
to clean up if a binder is moved or restored by hand.

**It builds whenever it cannot be sure.** No previous binder, a previous binder
it cannot read, a manifest it cannot parse, a previous build stamped
`INCOMPLETE`, or a source it could not read this time: all rebuild. An
unnecessary rebuild costs a version number; a wrongly skipped one leaves a
binder that misrepresents the tree.

**Timestamps are not used.** A file touched but not changed, or a checkout that
rewrites every modification time, would both trigger a pointless rebuild. The
comparison is over content.

To rebuild anyway:

```
python binder_builder.py --force
```

A dry run reports the same comparison as `WOULD CHECK` and writes nothing
either way.

---

## Running it

Live by default — there is no confirmation prompt. With no arguments it builds
every binder defined in the folder:

```
python binder_builder.py
```

One binder only:

```
python binder_builder.py ProjectDesign
```

Report only, writes nothing:

```
python binder_builder.py --dry-run
```

Rebuild even if nothing has changed:

```
python binder_builder.py --force
```

List the binder definitions in this folder and build nothing:

```
python binder_builder.py --list
```

The dry run takes exactly the same decisions as a live run — it reads every
source and computes every digest — and reports them with `WOULD INCLUDE` and
`WOULD WRITE` in place of `INCLUDED` and `WRITTEN`. It is the safe way to check
a new scope before letting the tool write anything.

---

## The report

| Kind | Meaning |
| --- | --- |
| `INCLUDED` | File placed in the binder, with its digest. |
| `WOULD INCLUDE` | Dry run — the same file, nothing written. |
| `SKIPPED` | In a collected folder, deliberately left out — an `exclude_files` match, or the tool's own output. |
| `UNMATCHED` | An `order` entry naming a file that is not in scope. |
| `NO CHANGES` | Nothing in scope has changed since the last binder. Nothing written, nothing superseded. |
| `WOULD CHECK` | Dry run — the same comparison, reported rather than acted on. |
| `WRITTEN` / `WOULD WRITE` | The binder itself. |
| `SUPERSEDED` / `WOULD SUPERSEDE` | The previous binder moved into `_superseded`. |
| `CONFLICT` | A destination name is already taken; nothing overwritten. |
| `EMPTY` | Nothing in scope. An empty binder is written, saying so. |
| `INCOMPLETE` | A source could not be read. The binder has a hole in it. |
| `ERROR` | A filesystem refusal — a locked file, permissions, an unreadable folder. |

Events are grouped by folder. The exit code is `0` unless at least one `ERROR`
occurred.

### Two cases worth understanding

**`EMPTY` — nothing was in scope.** The binder is still written, and says so on
its own first screenful:

```
> **EMPTY BINDER - nothing was in scope when this was built.**
>
> This is a statement about the tree, not a failure: the scope genuinely
> contained no files. If that is unexpected, the scope settings are where
> to look.
```

The previous binder is superseded as usual, so it is in `_superseded` and one
move from being restored if this was not what you wanted.

This is deliberate, and it is the opposite of what the tool used to do. Writing
nothing sounds safer, but it leaves a binder in the output folder presenting as
current while asserting content the scope no longer holds — and that binder is
what gets loaded into a session. A stale binder that looks authoritative is the
worst thing this tool could produce. An empty one that says it is empty is
merely surprising.

`EMPTY` is reported whether or not anything was written, because an empty scope
is far more often a settings mistake than a true statement. If you see it and
did not expect it, check `include`, `exclude_files` and `file_types` first.

Running again with the scope still empty writes nothing further — change
detection sees an empty binder and an empty scope and reports `NO CHANGES`.

**`INCOMPLETE` — a source could not be read.** The binder is written, but it has
a hole in it, so it is stamped as incomplete in three places: the report, the
log, and a block near the top of the binder itself naming every missing file.
The previous binder is **not** superseded, so the last good one stays available.
A plausible-looking binder that is quietly missing a document is the worst thing
this tool could produce, so it is made loud in every place someone might look.

---

## Text encoding

Stated explicitly rather than left to the platform:

- **Read** as UTF-8, with a byte-order mark removed if one is present. That BOM
  removal is the only deviation from byte-for-byte copying, and it is
  deliberate: a BOM is a start-of-file marker, and leaving one embedded halfway
  down a binder puts a stray character in the middle of the text.
- **Write** as UTF-8 without a BOM, in binary mode so that no line-ending
  translation can happen. Line endings pass through exactly as they were in the
  source.

A file that is not valid UTF-8 cannot go into the binder. It is reported as an
`ERROR`, and the binder it would have gone into is stamped `INCOMPLETE`.

---

## The log

Every run appends one entry to the log file, live and dry-run alike, each
stamped with the date, the mode and the root it was pointed at. The log is never
rewritten or trimmed. If it grows unwieldy, archive or delete it by hand; the
tool will start a fresh one.

---

## Scope

It collects and assembles. It does not resolve versions — that is version
cleanup's job, run first — and it does not deploy. It is Infrastructure: it acts
on the corpus and is never loaded into an AI session itself.
<!-- END SOURCE: Infrastructure/binder-builder/README.md -->

---

<!-- BEGIN SOURCE: Infrastructure/file-update-package/file_update_package_settings.json -->
{
  "_comment": "Settings for the file update package deployer. Edit the values below. Any key starting with _comment is ignored by the tool - JSON has no comment syntax, so notes live in keys like this one.",

  "_comment_documentation_root": "The root of the document tree packages are deployed into. Manifest paths are measured from here. A relative path is resolved against the folder this script lives in, so \"..\" means the parent folder - which is what an instance sitting in _tools wants. Give a full path such as \"C:/Users/you/Documents\" to point somewhere else. Forward slashes are safe on Windows. This setting cannot use \"~/\", because \"~/\" means \"measured from the documentation root\" and this is the setting that defines it.",
  "documentation_root": "..",

  "_comment_paths": "The three settings below accept three kinds of path. ABSOLUTE - \"C:/Docs/_fileupdatepackages\". ROOT-ANCHORED - \"~/_fileupdatepackages\" - measured from the documentation root above. RELATIVE - \"_fileupdatepackages\" - measured from the folder this script lives in. Note that ~ means the documentation root here, never your home folder.",

  "_comment_drop_folder": "Where packages are put to be deployed. The newest unprocessed .zip in this folder is the one that gets processed; the rest wait. Processed packages are moved into a _superseded subfolder of it.",
  "drop_folder": "~/_fileupdatepackages",

  "_comment_binder_builder": "The binder builder script to run after a deploy. Point this at the running instance, not at the master copy, so it uses that instance's settings. Set it to \"\" to skip the trigger entirely.",
  "binder_builder": "~/_tools/binder_builder.py",

  "_comment_log_file": "Where the run log is appended. One entry per run, never overwritten. Absolute, or \"~/\" for root-anchored, or relative to the script folder.",
  "log_file": "file_update_package.log"
}
<!-- END SOURCE: Infrastructure/file-update-package/file_update_package_settings.json -->

---

<!-- BEGIN SOURCE: Infrastructure/file-update-package/FileUpdatePackage_Design_v1.md -->
# FileUpdatePackage Deployer — Design

> **Version 1** (2026-09-07). First issue. Third tool in the Infrastructure family, after version
> cleanup and the binder builder, and the one that closes the loop: it takes the output of a Chat or
> Cowork session and puts it into the master tree.

**Master/source folder:** `Documentation/Infrastructure/file-update-package`
**Run from:** a copied instance folder with its own settings and log, e.g. `Documentation/_tools`

---

## Contents

- **Objective and boundary** — what it does and what it deliberately doesn't.
- **Inputs** — the settings file, and the package format.
- **Path logic** — absolute, root-anchored and script-relative forms.
- **Processing model** — find, validate, gate, deploy, trigger, file away.
- **Execution behaviour** — live by default, dry run, double-click, the completion summary.
- **Folder naming check** — advisory, and why it is here.
- **Definition of done.**
- **Decisions** — with reasons.

---

## 1. Objective and boundary

**Objective.** Deploy a FileUpdatePackage — a zip of updated documents produced by a Chat or Cowork
session — into the master document tree, superseding what it replaces, and leave the user in no
doubt about what happened.

**Boundary — hard.** It places whole files. It does **not** merge, patch or edit content, it does
not decide what belongs in a package, and it does not do general version resolution — it moves the
single document each manifest entry names, and nothing else. It is Infrastructure: it acts on the
corpus and is never loaded into an AI session itself.

**It never overwrites.** A file already sitting where a package wants to write, and not named as
the one being replaced, is a `CONFLICT`: reported, skipped, left exactly as it was.

**Shape.** A single-action tool, sibling to version cleanup and the binder builder. No actions
framework, no shared base class, no plugin system.

**Pipeline position.**

```text
(a session produces a package)
        ↓
file update package  →  binder builder
```

The deployer triggers the binder builder itself, so a deploy leaves the binder current. Version
cleanup remains a separate, human-run pass over the tree: the deployer supersedes only what a
manifest names.

---

## 2. Inputs

### 2.1 The settings file

JSON, read on launch, from the script's own folder.

| Setting | Purpose |
|---|---|
| `documentation_root` | The root of the tree packages deploy into. Manifest paths are measured from here, and it is the anchor for `~/` in the other settings. |
| `drop_folder` | Where packages are put to be deployed. Default `~/_fileupdatepackages`. |
| `binder_builder` | The binder builder script to run after a deploy. Point it at the **running instance**, not the master, so it uses that instance's settings. Empty string skips the trigger. |
| `log_file` | Log file location. Named to match both siblings. |

The script writes a commented default settings file if none is present, rather than failing.

### 2.2 The package

A zip file carrying documents at their paths relative to the documentation root, plus a manifest at
the zip root:

```json
{
  "created": "2026-09-07T10:00:00Z",
  "description": "Project Design master files — binder sweep complete",
  "files": [
    {
      "path": "Project Design/ProjectDesign_Design_v8.md",
      "action": "update",
      "replaces": "ProjectDesign_Design_v7.md"
    },
    { "path": "Project Design/ProjectDesign_Index_v8.md", "action": "create" }
  ],
  "user_instructions": "Review the new Overview document before publishing."
}
```

| Field | Meaning |
|---|---|
| `path` | Where the file goes, relative to the documentation root, forward slashes. |
| `action` | `create` — the file is new. `update` — it replaces an existing document. |
| `replaces` | *Update only, optional.* The **filename** of the document being superseded. The tool finds it and moves it to `_superseded`. Omitted, an update supersedes the file at its own `path` — see D4. |
| `description` | Optional. Shown in the report header and the completion summary. |
| `user_instructions` | Optional. Shown to the user, who must acknowledge before the deploy proceeds. |
| `created` | Optional, informational. The tool orders packages by filesystem modification time, not by this field. |

**`Documentation/_config/repo_config.json`** maps topic names to folder paths for whoever is
*building* a package. The tools do not read it; they have their own settings.

---

## 3. Path logic

The same three forms as the sibling tools, ratified as the Infrastructure-wide convention
(version-cleanup/claude-code/001, 2026-09-04):

| Form | Example | Meaning |
|---|---|---|
| **Absolute** | `C:/…/Documentation/_fileupdatepackages` | Exact folder. |
| **Root-anchored** | `~/_fileupdatepackages` | Measured from `documentation_root`. |
| **Script-relative** | `..` | Measured from the folder holding the script. |

`documentation_root` itself cannot use `~/`, because it is what `~/` means — the same rule and the
same error message as `root` in both siblings. See D2.

**The folder-relative *pattern* form does not appear here.** In the siblings it exists for `include`
and `exclude`, which describe *classes* of folder across a tree. This tool has no such setting:
every path names one place. Nothing is missing — there is nowhere for a pattern to apply.

`~` never means the home folder. Home expansion is not performed anywhere in these settings.

**Manifest paths are not settings paths.** They come from an untrusted zip and are checked
separately and harder — see §4.2.

---

## 4. Processing model

1. Resolve settings; resolve `documentation_root`.
2. Run the folder naming check over the tree (§6).
3. Find every `.zip` in the top level of the drop folder. None → `SKIPPED`, exit `0`.
4. Take the **newest by modification time**. Report the rest as `SKIPPED` — waiting, not processed.
5. Validate the package as a whole (§4.1). Any problem → `INVALID`, nothing is deployed.
6. If the manifest carries `user_instructions`: show them and wait for acknowledgement (§4.3).
7. For each manifest entry in order (§4.4): supersede what it replaces, then write the new file.
8. Trigger the binder builder (§4.5), unless nothing was written.
9. Move the package into `_superseded` inside the drop folder — **only if the deploy was complete**.
10. Report, log, print the completion summary, hold the window open.

### 4.1 Validation is a gate, not a filter

A package deploys as a whole or is rejected as a whole. Rejected for: not a zip; no `_manifest.json`;
a manifest that is not valid JSON or not an object; no `files` list; an entry with no usable `path`;
an `action` that is not `create` or `update`; `replaces` on a create; `replaces` containing a folder
separator; the same destination listed twice; and — the important one — **a manifest naming a file
the zip does not contain**.

A package that is wrong in one place is not deployed in the places it happens to be right. Deploying
the good half of a badly-built package leaves the tree in a state nobody designed, and leaves the
session that built it believing its work landed.

### 4.2 Package paths are untrusted input

Every manifest `path` is checked before it is used: no absolute paths, no drive letters, no `..`
segment, no trailing separator, not empty. The resolved destination is then checked again to be
inside the documentation root, which catches the case a purely textual check cannot — a symbolic
link in the tree carrying a well-formed relative path somewhere else entirely.

Files are written from `zipfile.read()` into a validated destination rather than with
`ZipFile.extract()`, which derives the destination from the member name.

### 4.3 The user instructions gate

If the manifest carries `user_instructions`, they are printed in a banner and the tool waits for
Enter **before anything is written**. Stopping there — Ctrl+C — stops a deploy that has not started,
rather than one that is half done.

The wait is skipped, and the summary says so in those words, when there is no interactive console.
A run triggered by another tool must not block forever on a keypress nobody is there to press. This
is the same reasoning as the exit pause in both siblings.

### 4.4 One entry, in order

| Step | Behaviour |
|---|---|
| **Find what it replaces** | Beside the new file first — v7 and v8 of one document live in the same folder — then the rest of the tree, skipping `_superseded` folders throughout. |
| **Found once** | Move it into `_superseded` beside itself. `SUPERSEDED`. |
| **Not found** | `SKIPPED`, naming it. The new file still deploys. |
| **Found more than once** | `CONFLICT`, naming every place. **Nothing is moved** — see D5. The new file still deploys. |
| **Destination taken** | `CONFLICT`. Nothing is written and nothing is overwritten, ever. |
| **Otherwise** | Write the file. `DEPLOYED` for an update, `CREATED` for a create. |

An update whose predecessor sits at the destination itself clears its own way: the supersession
moves it, and the never-overwrite check that follows is then a genuine test rather than a formality.
A dry run reports this correctly rather than reporting a conflict against a file it would itself
have moved.

### 4.5 The binder builder trigger

Run unconditionally after any deploy that wrote something, with no arguments, in live mode. The
binder builder's own change detection (BinderBuilder_Design_v4 §4a) decides whether a rebuild is
actually needed, so this tool does not have to know or care.

`stdin` is closed rather than inherited, which is what stops the binder builder pausing for a
keypress at the end of its own run. Its `Result:` line is carried up into this report; its full
report is in its own log.

**Best-effort.** The deploy has already happened by the time this runs. A binder builder that is
missing, that will not start, that exits non-zero or that runs past its timeout is reported as an
`ERROR` on that step and the deploy stands — including the package being filed away, because the
files did land.

### 4.6 Partial deploys keep their package

A run with any `CONFLICT` or file-level `ERROR` leaves the package in the drop folder. Whoever sorts
the conflict out needs the package still to hand, and a package sitting under `_superseded` reads as
one that was fully applied. The report says which files landed and which did not.

---

## 5. Execution behaviour

Matches both siblings, so the three tools behave alike:

- Python, standard library only, single readable script.
- Runs **live by default**; `--dry-run` reports what would be deployed and changes nothing.
- Reads settings on launch — no arguments required, so **double-click works on Windows**.
- Appends one entry per run to the log, dry runs included and marked.
- Cross-platform; Windows primary.

### Report vocabulary

`DEPLOYED` / `WOULD DEPLOY` · `CREATED` / `WOULD CREATE` · `SUPERSEDED` / `WOULD SUPERSEDE` ·
`CONFLICT` · `SKIPPED` · `INVALID` · `BINDER` · `PROCESSED` / `WOULD PROCESS` · `ERROR`

`CONFLICT` and `ERROR` carry version cleanup's meanings exactly. `SKIPPED` covers both nothing-to-do
cases: no packages at all, a package waiting its turn, and a `replaces` that names nothing in the
tree. `INVALID` is §4.1 — the package was rejected and nothing in it was deployed.

**Events are reported in the order they happened**, not sorted, unlike both siblings. A deploy is a
sequence: a supersession and the write that depended on it read as one story. The folder heading
still changes as the run moves through the tree.

### The completion summary

The primary output, not an afterthought. Every run ends with it, whatever happened, and the window
stays open until it has been read:

```text
========================================================================
COMPLETION SUMMARY
------------------------------------------------------------------------
  package:              good.zip
                        Project Design master files - binder sweep complete
  files updated:        1
  files created:        1
  files superseded:     1
  conflicts:            0
  errors:               0
  user instructions:    present, shown and acknowledged
  binder builder:       triggered - 24 included, 1 written, 1 superseded
  the package is now:   moved to _superseded/
  folder naming:        1 folder(s) close to a convention name but not matching it
    - _superceded  (expected "_superseded")
------------------------------------------------------------------------
COMPLETED SUCCESSFULLY
========================================================================
```

Every conflict and every error is listed individually with its filename and reason. The final line
is one of:

| Status | When |
|---|---|
| `COMPLETED SUCCESSFULLY` | No conflicts, no errors. Also the "nothing to do" case, and a clean dry run. |
| `COMPLETED WITH ERRORS - every file was deployed, but a later step failed` | The files landed; something after them did not — in practice, the binder builder. |
| `COMPLETED WITH ERRORS - the deploy is incomplete` | Some files landed and some did not. |
| `FAILED - nothing was deployed` | An `INVALID` package, or every entry conflicted. |

**Exit code `0` unless an `ERROR` occurred**, matching both siblings. Note the consequence, stated
so it is not later read as a defect: a `CONFLICT` and an `INVALID` package both exit `0`, because
nothing failed — the tool did exactly what it should with what it was given. See §8.

---

## 6. Folder naming check

Every run, before anything else, walks the documentation root and reports any folder whose name is a
near-miss of a convention name — `_superseded`, `_fileupdatepackages`, `_binder`, `_tools`,
`_config`, `_rebuild` — using a similarity threshold rather than a fixed list of misspellings.

**Only underscore folders are candidates.** Every convention name is one, and the restriction is
what keeps the check honest: `Infrastructure/file-update-package`, the master folder of this very
tool, scores above the threshold against `_fileupdatepackages` on similarity alone and is plainly
not a misspelling of it. A summary that cries wolf stops being read.

**It is advisory.** It never renames anything, never blocks a deploy, and never changes the exit
code. It speaks in the completion summary and nowhere else.

It is here because a misspelled underscore folder is invisible to every tool in this family: they
all skip underscore folders, so `_superceded` does no damage and produces no complaint — it just
quietly splits a convention in two, and stays split until something says so. The known instance is
`Documentation/_superceded`, recorded in BinderBuilder_Design_v3 §10 and deliberately left alone;
reconciling it is a human act. Naming it on every run is how it stops being forgotten. See D7.

---

## 7. Definition of done

Drop a well-formed package into the drop folder and run the tool. Each `update` supersedes the
document it names and lands in its place; each `create` lands where it should; nothing anywhere is
overwritten. Instructions in the package are shown and acknowledged before any file is touched. The
binder builder runs afterwards and its outcome is reported. The package is moved to `_superseded`.
The completion summary states, without the user having to interpret anything, how many files were
updated, created and superseded, every conflict and error with its filename and reason, whether the
binder was rebuilt, and a final status line — and the window stays open until it is read.

A dry run reports all of that and changes nothing.

An empty drop folder reports `SKIPPED` and exits `0`. A package that is not a zip, has no manifest,
has an unparseable manifest, or names a file it does not contain, is rejected whole — `INVALID`,
nothing deployed, the package left where it is. A path containing `..` never writes outside the
documentation root. A partial deploy names what landed and what did not, and keeps its package. A
misspelled convention folder anywhere in the tree is named in the summary.

---

## 8. Decisions

**D1 — A third tool, not a mode of an existing one.** Deploying is a different job from tidying
versions and from assembling a binder, and it is the only one of the three that takes an external
input. The three run in sequence and share nothing but conventions.

*Consequence, accepted:* the path logic now exists in three implementations. The trigger for
extracting shared code was stated in BinderBuilder_Design_v3 §10 as "a third tool needing it" — and
this is that third tool. It is still not extracted: this tool needs only the one-place resolver,
about forty lines of pure functions over paths with no state, and not the pattern matching that
makes up the bulk of the siblings' path code. A shared module carrying two thirds dead weight for
each importer is worse than the copy. **Re-examine when a fourth tool arrives, or when any tool needs
the pattern form changed.**

**D2 — `documentation_root` cannot use `~/`.** The tool-pipeline brief proposed
`"documentation_root": "~/"`. Rejected as circular: `~/` means "measured from the documentation
root", so it cannot appear in the setting that defines that root. Both siblings reject `~/` in
`root` for exactly this reason and say so in an error message. The shipped default is `".."`, which
is what an instance sitting in `_tools` wants, and the setting comment says why.

**D3 — Newest package only; the rest wait.** Batching would mean deciding what to do when the third
of five packages conflicts, and the honest answer is "a person looks at the report". One package per
run keeps the completion summary about one deploy. Waiting packages are reported by name, so nothing
is silently held back.

Ordering is by filesystem modification time rather than by the manifest's `created` field: the field
is written by whatever produced the package and cannot be relied on, and the file's own timestamp is
the fact the drop folder actually carries.

**D4 — `replaces` is optional on an update.** Where it is absent, the entry supersedes the file at
its own `path`. This is the natural reading of "update" for a document whose filename does not carry
a version, and it never overwrites: the existing file is moved to `_superseded` exactly as a named
one would be.

*Considered and rejected:* treating a missing `replaces` as `INVALID`. Rejected because the
resulting behaviour would be worse — a package that plainly means "here is the new version of this
file" would be refused for a field that adds nothing in that case.

**D5 — An ambiguous `replaces` moves nothing.** A filename found in three folders is a question this
tool must not answer by guessing. All three are named in a `CONFLICT`, none is moved, and the new
file still deploys — so the outcome is visible in the tree as well as in the report, and version
cleanup will surface it again on its next pass.

This is version cleanup's `AMBIGUOUS` shape, reported here as `CONFLICT` because the vocabulary for
this tool was fixed at seven words and a near-duplicate would have to earn its place.

**D6 — The binder builder trigger is best-effort, and it is unconditional.** Unconditional because
the binder builder now decides for itself whether a rebuild is needed (v4 §4a); a deployer that
tried to predict that would duplicate the judgement and eventually disagree with it. Best-effort
because the deploy has already happened: a binder that could not be rebuilt is a stale binder, not a
lost document. It is reported as an `ERROR` and the run exits `1`, but the deploy stands and the
package is still filed away.

**D7 — The folder naming check is advisory and lives here.** It could sit in any of the three tools.
It is here because this is the tool that writes *into* the tree at paths a session composed, which
is exactly where a split convention would first do harm — a package built against `_superceded`
would file documents somewhere no tool looks.

It never renames. Renaming a folder is a decision with consequences the tool cannot see, and the
misspelling it will find most often is a known one that has already been left deliberately.

**D8 — `CONFLICT` and `INVALID` exit `0`.** Consistent with both siblings, where the exit code
reports whether the tool failed rather than whether the outcome was the desired one. The completion
summary is the human channel and it says `FAILED` in plain words. Recorded here because the two
channels disagreeing looks like a defect if it is not written down as a choice. See §9.

---

## 9. Open

- **Exit codes for expected-but-unwanted outcomes.** `EMPTY` in the binder builder, and `CONFLICT`
  and `INVALID` here, all exit `0`. A future orchestrator chaining these tools would want to
  distinguish "did nothing" from "did what was asked". Prefer distinct codes over overloading the
  failure code. **Not now** — the only chaining that exists is this tool calling the binder builder,
  and it reads the report rather than the exit code.
- **Package provenance.** The manifest's `created` field is carried but not used, and there is no
  record in the deployed tree of which package a document arrived in. The log has it. Whether that
  is enough is a question for the first time someone asks "where did this file come from".
- **Path-logic duplication.** Three implementations now. See D1 for the trigger to revisit.
- **The `_superceded` misspelling** at the Documentation root remains, and is now reported on every
  deploy rather than only in a design document. Still a human act to reconcile.
<!-- END SOURCE: Infrastructure/file-update-package/FileUpdatePackage_Design_v1.md -->

---

<!-- BEGIN SOURCE: Infrastructure/file-update-package/README.md -->
# file update package

Deploys a **FileUpdatePackage** — a zip of updated documents produced by a Chat
or Cowork session — into the master document tree, superseding what it replaces
and rebuilding the binder afterwards.

This folder is the **master copy**. To use the tool, copy
`file_update_package.py` and `file_update_package_settings.json` to wherever it
should run from, then edit that copy's settings. Each instance keeps its own
settings file and its own log beside the script, so instances never interfere
with each other.

**It never overwrites.** A file already sitting where a package wants to write,
and not named as the one being replaced, is reported as a `CONFLICT` and left
exactly where it is.

---

## What a package looks like

A zip file containing the documents at their paths relative to the
documentation root, plus a manifest called `_manifest.json` at the zip root:

```
ProjectDesign_2026-09-07.zip
├── _manifest.json
└── Project Design/
    ├── ProjectDesign_Design_v8.md
    └── ProjectDesign_Index_v8.md
```

```json
{
  "created": "2026-09-07T10:00:00Z",
  "description": "Project Design master files - binder sweep complete",
  "files": [
    {
      "path": "Project Design/ProjectDesign_Design_v8.md",
      "action": "update",
      "replaces": "ProjectDesign_Design_v7.md"
    },
    {
      "path": "Project Design/ProjectDesign_Index_v8.md",
      "action": "create"
    }
  ],
  "user_instructions": "Review the new Overview document before publishing."
}
```

| Field | Meaning |
| --- | --- |
| `path` | Where the file goes, measured from the documentation root. Forward slashes. |
| `action` | `create` for a new file, `update` for one that replaces an existing document. |
| `replaces` | Update only, optional. The **filename** — not a path — of the document being superseded. The tool finds it and moves it into `_superseded`. |
| `description` | Optional. Shown in the report and the completion summary. |
| `user_instructions` | Optional. Shown to you, and the tool waits for you to acknowledge them before it touches anything. |
| `created` | Optional, informational. Packages are ordered by file modification time, not by this. |

**Leaving `replaces` out of an update** means "this replaces the file already at
this path" — that file is moved into `_superseded` and the new one written in
its place. Use it for documents whose filenames do not carry a version.

`Documentation/_config/repo_config.json` maps topic names to folder paths, for
whoever is *building* a package. The tool does not read it; it has its own
settings.

---

## What it does

1. Finds the newest unprocessed `.zip` in the drop folder. Any others wait their
   turn and are reported by name.
2. Validates the package — a zip, with a manifest, that names files it actually
   contains. Anything wrong and the whole package is rejected: `INVALID`, and
   nothing at all is deployed.
3. Shows the package's instructions, if it has any, and waits for you.
4. For each file: moves the document it replaces into `_superseded`, then writes
   the new one.
5. Runs the binder builder. It decides for itself whether a rebuild is needed.
6. Moves the package into `_superseded` inside the drop folder — but only if the
   deploy was complete.
7. Prints a completion summary and holds the window open until you have read it.

---

## Installing Python on Windows

Only needed once per machine. The tool uses nothing beyond the Python standard
library, so there is nothing else to install.

1. Go to <https://www.python.org/downloads/windows/> and download the latest
   **Windows installer (64-bit)**. Python 3.8 or newer is required; any current
   release is fine.
2. Run the installer. On the first screen, **tick "Add python.exe to PATH"**
   before clicking Install. This is easy to miss and is the usual reason a
   `.py` file will not run afterwards.
3. Choose **Install Now**.

Double-clicking `file_update_package.py` in File Explorer runs it. If it opens
in Notepad instead, right-click it → **Open with** → **Choose another app** →
pick **Python**, and tick **Always use this app to open .py files**.

Or from a terminal:

```
python "C:\path\to\file_update_package.py"
```

---

## Settings

The script reads `file_update_package_settings.json` from **its own folder** —
not from wherever the terminal happens to be pointing. If that file is missing,
the script writes a fresh one with default values and explanatory notes, then
tells you to check it.

```json
{
  "documentation_root": "..",
  "drop_folder": "~/_fileupdatepackages",
  "binder_builder": "~/_tools/binder_builder.py",
  "log_file": "file_update_package.log"
}
```

| Setting | Meaning |
| --- | --- |
| `documentation_root` | The root of the tree packages deploy into. Manifest paths are measured from here. |
| `drop_folder` | Where packages are put to be deployed. |
| `binder_builder` | The binder builder to run afterwards. Point it at the **running instance**, so it uses that instance's settings. Set it to `""` to skip the trigger. |
| `log_file` | Where the run log is appended. |

### The three path forms

| Form | Example | Means |
| --- | --- | --- |
| Absolute | `"C:/Docs/_fileupdatepackages"` | that exact folder |
| Root-anchored | `"~/_fileupdatepackages"` | measured from `documentation_root` |
| Script-relative | `".."` | measured from the folder holding the script |

`"~"` here means **the documentation root**, never your home folder. The tool
never expands `~` the way a shell would.

`documentation_root` cannot itself use `"~/"` — it is what `"~/"` means. Use
`".."`, which is what an instance sitting in a `_tools` folder wants, or a full
path.

This is the same path model as version cleanup and the binder builder,
deliberately. Three Infrastructure tools with different path semantics would be
a trap. (The *pattern* form those two accept in `include` and `exclude` has no
equivalent here: every setting in this tool names one place.)

**Writing paths in JSON.** Use forward slashes (`"C:/Users/you/Documents"`) or
doubled backslashes; a single backslash is an escape character in JSON and will
break the file.

---

## Running it

Live by default — the only prompt is the package's own instructions, if it has
any:

```
python file_update_package.py
```

Report only, changes nothing:

```
python file_update_package.py --dry-run
```

The dry run takes the same decisions as a live run — it validates the package,
works out what would be superseded and what would conflict — and reports them
with `WOULD DEPLOY`, `WOULD CREATE` and `WOULD SUPERSEDE`. It is the safe way to
look at a package you did not build yourself.

---

## The completion summary

This is the point of the run. It is printed whatever happened, and the window
stays open until you have read it:

```
========================================================================
COMPLETION SUMMARY
------------------------------------------------------------------------
  package:              ProjectDesign_2026-09-07.zip
                        Project Design master files - binder sweep complete
  files updated:        1
  files created:        1
  files superseded:     1
  conflicts:            0
  errors:               0
  user instructions:    present, shown and acknowledged
  binder builder:       triggered - 24 included, 1 written, 1 superseded
  the package is now:   moved to _superseded/
  folder naming:        no misspelled folders found
------------------------------------------------------------------------
COMPLETED SUCCESSFULLY
========================================================================
```

Every conflict and every error is listed individually, with the filename and the
reason. The last line is one of:

| Status | When |
| --- | --- |
| `COMPLETED SUCCESSFULLY` | Nothing went wrong. Also the "no packages to deploy" case. |
| `COMPLETED WITH ERRORS - every file was deployed, but a later step failed` | The files landed; something after them did not — in practice the binder builder. |
| `COMPLETED WITH ERRORS - the deploy is incomplete` | Some files landed, some did not. |
| `FAILED - nothing was deployed` | The package was rejected, or every file in it conflicted. |

---

## The report

| Kind | Meaning |
| --- | --- |
| `DEPLOYED` / `WOULD DEPLOY` | An updated file written into place. |
| `CREATED` / `WOULD CREATE` | A file that did not exist before. |
| `SUPERSEDED` / `WOULD SUPERSEDE` | The document being replaced, moved into `_superseded`. |
| `CONFLICT` | A destination is taken, or a `replaces` matched more than one file. Nothing overwritten, nothing moved. |
| `SKIPPED` | No packages to deploy, a package waiting its turn, or a `replaces` naming a file that is not in the tree. |
| `INVALID` | The package was rejected. Nothing in it was deployed. |
| `BINDER` | The binder builder was triggered, and what it said. |
| `PROCESSED` / `WOULD PROCESS` | The package itself, moved into `_superseded`. |
| `ERROR` | A filesystem refusal, or a binder builder run that failed. |

Events appear in the order they happened, so a supersession and the write that
depended on it read as one story. The exit code is `0` unless an `ERROR`
occurred — note that a `CONFLICT` and a rejected package both exit `0`, because
nothing failed: the tool did exactly what it should with what it was given. The
completion summary is where you read the outcome.

### Three cases worth understanding

**`INVALID` — the package was rejected.** Validation is a gate, not a filter. A
package that is wrong in one place is not deployed in the places it happens to
be right, because deploying half of a badly-built package leaves the tree in a
state nobody designed. Fix the package and drop it in again.

**`CONFLICT` — something was in the way.** Either a file already sits where the
package wants to write and the package did not name it as superseded, or a
`replaces` filename was found in several folders and the tool will not guess
which one you meant. Nothing is overwritten and nothing is moved. The run says
exactly which file and why.

**A partial deploy keeps its package.** If anything conflicted, the zip stays in
the drop folder rather than moving to `_superseded` — you will need it when you
sort the conflict out, and a package filed away reads as one that was fully
applied.

---

## The folder naming check

Every run walks the tree and reports any folder whose name is *nearly* one of
the conventions — `_superceded` where `_superseded` was meant, and so on. It
appears in the completion summary and nowhere else.

Only folders whose names start with an underscore are looked at, which is the
class every convention name belongs to. An ordinary folder is never flagged.

It is advisory. It never renames anything, never blocks a deploy and never
changes the exit code.

It exists because a misspelled underscore folder is invisible to every tool in
this family: they all skip underscore folders, so a misspelling does no damage
and raises no complaint — it just quietly splits a convention in two and stays
that way. Naming it on every run is how it stops being forgotten.

---

## The log

Every run appends one entry to the log file, live and dry-run alike, each
stamped with the date and the mode. The entry is the whole report, completion
summary included. The log is never rewritten or trimmed.

---

## Scope

It places whole files. It does not merge, patch or edit content, it does not
decide what belongs in a package, and it does not do general version resolution
— it moves the single document each manifest entry names. Tidying the rest of
the tree is version cleanup's job.
<!-- END SOURCE: Infrastructure/file-update-package/README.md -->

---

<!-- BEGIN SOURCE: Infrastructure/Infrastructure_CLI_Decisions_v1.md -->
Infrastructure — CLI Decisions | decisions | Infrastructure_CLI_Decisions@v1 | 2026-09-10

## Utility registration — convention scanning over alternatives

Three options were on the table: convention-based scanning of a subpackage, a registry file listing available utilities, and decorator-based registration.

Convention scanning was chosen (strong recommendation, agreed). There are three utilities now and likely only a handful more over time. A registry file is a second artefact to maintain for no benefit at this scale — every time a utility is added, the registry must also be updated, which is exactly the kind of coordination step that adds friction without adding value. Decorators add a layer of indirection that buys nothing when everything lives in one package. Convention scanning is the simplest thing that works: drop a module in the folder following the agreed shape, and it appears.

The CLI-growth consideration was raised by Dave: this dispatcher may become the full AIDE CLI. The response was that convention scanning does not paint the design into a corner — a folder of utilities following a shared shape is exactly the foundation a bigger CLI would want. The temptation to pre-build grouping, categories, or a richer interface was explicitly named as the apparatus trap. The consideration is logged but does not drive the current design.

## Settings format — JSON over YAML

The three existing utilities already use JSON settings files. YAML is friendlier to hand-edit but would be a new format to introduce for no demonstrated gain. Matching what is already in use on the project costs nothing and avoids a format split between existing utility settings and the new dispatcher settings.

## Settings merge — deep merge over full replacement

Deep merge means a per-project settings file overrides individual values without needing to restate the surrounding structure. The alternative — full replacement per key — would force a project to copy an entire settings block just to change one value inside it. That is more brittle and harder to keep in step with the global defaults as they evolve.

## Three-layer settings — package defaults separated from user global

The original design had two layers: global settings with the installed package, and per-project overrides. This missed a problem: pip overwrites the package directory on every update, so any user-edited global settings (a custom exclude list, a repo URL override) would be lost on the next `aide update`.

The fix separates immutable package defaults (shipped with the package, never edited) from user-global settings (`~/.aide/settings.json`, survives updates). Per-project remains the third layer. The auto-update state file already lived at `~/.aide/state.json`, so the convention was already established — settings just needed to follow it.

## The `_aide` folder — Dave's initiative

The original proposal placed per-project settings under `_utilities`. Dave pushed back: he wanted the number of root-level operational folders kept lean and preferred one generic home for machine-facing files rather than several purpose-specific ones. The folder would hold settings, logs, and utilities as a subfolder only if needed.

The name `_aide` was chosen over `_system` because it matches the framework name and the existing underscore-prefix convention already established for operational folders (`_index`, `_archived`, `_binders`, `_fileupdatepackages`). The underscore sorts it to the top of the directory listing and signals that it is infrastructure, not content.

## Auto-update frequency — daily over every-launch

Checking on every launch adds a network call and a slight delay each time the dispatcher runs, which gets annoying with frequent use. Once a day catches updates promptly without that friction. The manual `aide update` command is always available for an on-demand check, so the daily cadence never blocks a user who wants to check sooner.

## Auto-update version detection — git tags over commit hashes

The package is installed from a git repository, so git tags are the natural version signal. Commit hashes do not indicate whether a change is meaningful — a documentation-only commit and a breaking change look the same. Release tags carry explicit version semantics.

## Auto-update offline behaviour — graceful skip over retry

Dave asked specifically about the retry model. The decision was: no retry loop, no background process, no machinery. If the daily check fails because the network is unreachable, the dispatcher does not update the "last checked" timestamp. The next launch sees the check is still due and tries again naturally. Offline means "still due," not "retry now." This keeps the auto-update behaviour proportionate — a single quiet check, never a blocker.

## Include/exclude form — deny list over allow list

By default, every utility the dispatcher discovers is available. To hide one, name it in an exclude list. The alternative — an allow list where every utility must be explicitly enabled — means that adding a new utility requires updating every project's settings to make it visible. That contradicts the low-fuss spirit of convention scanning: a new module in the subpackage should just work everywhere unless deliberately turned off.

## Include/exclude as a settings concern, not a registration concern

Registration discovers everything that exists in the subpackage. Settings decide what is shown. Mixing the two — having registration itself honour include/exclude rules — would mean the dispatcher's scanning logic needs to know about settings before it has finished loading them. Keeping the concerns separate is both simpler and more predictable: scan first, filter second.

## Include/exclude scope — both global and per-project

This rides on the deep-merge settings model already settled. A global exclude hides a utility everywhere. A per-project exclude hides it for that project only. A per-project override can also restore a globally excluded utility. No new mechanism — it is just another setting following the same merge rules.

## Project root detection — walk up to repo boundary

Three options were considered: hardcoding the documentation root path in settings, using the git repo root directly, or walking up from the current directory. Walk-up was chosen. A hardcoded path is brittle and forces per-project configuration for something that should just work. Using the git root directly would require knowing the documentation folder's name within the repo, which is also configuration. Walking up and looking for `_aide/` is self-discovering — the folder's presence is both the marker and the configuration. The git repo boundary is the natural stop point, since `_aide/` above the repo root would belong to a different project.

## Multi-binder — run all definitions found, not just one

The original design assumed one binder settings file per project. In practice, the AIDE documentation already has two binders with different scopes and different file type rules — one for the full documentation set and one for the AI-facing subset. Erroring on multiple files forced the user to choose one, which defeated the purpose of having both. The utility now discovers all settings files in its subfolder and runs each. No configuration needed — presence is registration, the same principle as utility discovery in the dispatcher.

---

Version note: v1 — reasoning from voice session 2026-09-10. All four items were settled in conversation; this document records the alternatives considered and the reasons for each choice.
<!-- END SOURCE: Infrastructure/Infrastructure_CLI_Decisions_v1.md -->

---

<!-- BEGIN SOURCE: Infrastructure/Infrastructure_CLI_Design_v1.md -->
Infrastructure — CLI Design | design | Infrastructure_CLI_Design@v1 | 2026-09-10

## Summary

The `aide` command is the single entry point to AIDE's infrastructure utilities. It is a Python package distributed via pip from a git repository, installed as a console entry point so that `aide` is available on PATH. On launch it scans for available utilities, applies settings, and presents an interactive menu. Each utility can also be invoked directly as a subcommand.

This document specifies four things: how utilities are discovered, how settings work, how the tool keeps itself current, and how individual utilities can be included or excluded. It is the handoff to a Code session for the build.

Infrastructure owns this design. The individual utility designs (the binder builder, the file-update packager, version cleanup) live with their owning area — File Operations in Working Practices.

---

## Distribution and entry point

The `aide` package is a standard Python package hosted in a git repository and installed with pip. A `console_scripts` entry point registers `aide` as a command, so it is available on PATH after installation.

No PyPI publication. The install source is the git repository directly.

---

## Utility registration

Utilities live as modules in a `utilities/` subpackage inside the `aide` package. The dispatcher scans this subpackage at startup and picks up every module that follows the standard shape:

- A `name` attribute — the display name shown in the menu and used as the subcommand.
- A `description` attribute — a short line shown alongside the name.
- A `run` function — the entry point the dispatcher calls.

Any module in the subpackage that exposes these three things is a utility. No separate registration step, no manifest, no decorator — presence in the subpackage and conformance to the shape is registration.

The three existing utilities each become a module in this subpackage following this shape: the binder builder, the file-update packager, and version cleanup. Their internal logic is unchanged; only the entry point is standardised.

The binder builder supports multiple binder definitions. Each settings file in the binder-builder subfolder defines a separate binder. When the utility runs, it discovers and builds all of them in sequence, reporting results per binder.

**Consideration noted:** this dispatcher may grow into the full AIDE CLI later, but the design does not anticipate that. The registration model is simple enough to extend if that direction is taken, without needing to be redesigned for it now.

---

## Interactive menu and subcommand support

When invoked without arguments, `aide` presents an interactive menu listing every registered utility by name and description. The user selects one and it runs.

When invoked with a utility name as a subcommand (e.g. `aide binder`), the dispatcher calls that utility's `run` function directly, bypassing the menu. This supports both interactive use and scripting.

The auto-update check (described below) and the manual update command are also available through the menu and as subcommands.

---

## Per-project batch launcher

When invoked from within a project that has an `_aide/` folder, the dispatcher can run a defined sequence of utilities in order. The batch configuration lives in the project settings file. This supports common workflows — for example, running version cleanup, the binder builder, and a git commit in sequence.

---

## Settings

### Format

JSON. This matches the format already used by the existing utility settings files.

### Locations

Three levels, each overriding the one before:

- **Package defaults** live with the installed package. Immutable — shipped as part of the package and overwritten on every update. Never edited by the user.
- **User global** live at `~/.aide/settings.json` (on Windows, `C:\Users\<user>\.aide\`). The user's own global settings — their exclude list, repo URL, anything they want everywhere. Survives updates. Created on first use if absent; skipped silently if missing.
- **Per-project settings** live under `_aide/` at the documentation root of the project. These override both layers above for work in that project.

### Merge behaviour

Deep merge at each layer. Package defaults are merged with user-global settings, then the result is merged with per-project settings. A key present in a higher layer replaces the same key from the layer below; everything else is inherited.

This means each layer only declares what it changes. A user who wants a global exclude list sets it once in `~/.aide/settings.json`. A project that needs different exclude rules states those rules and inherits everything else.

---

## The `_aide` folder

Underscore-prefixed folder at the documentation root. It is the single home for machine-facing operational files in a project:

- Settings (the per-project settings file).
- Logs (if utilities produce them).
- Any other operational state the dispatcher or utilities need per-project.

The underscore prefix keeps it sorted to the top of the directory and signals that it is infrastructure, not content. It sits outside AIDE's document processing — consistent with the convention that underscore-prefixed folders are outside binder scope.

Utility-specific settings files live in subfolders under `_aide/utilities/`, one per utility: `binder-builder/`, `file-update-package/`, `version-cleanup/`. This keeps utility configuration out of the `_aide/` root, which holds only the dispatcher settings. The same subfolder structure applies under `~/.aide/utilities/` for user-global utility settings.

---

## Project root detection

The dispatcher walks up the directory tree from the current working directory looking for a folder named `_aide/`. If found, the directory containing `_aide/` is the project root. If the walk reaches the git repository boundary without finding `_aide/`, there is no project context — global settings only apply.

This means `aide` works from any subfolder within a project. No hardcoded documentation root path, no configuration required.

---

## Auto-update

### Automatic check

On launch, the dispatcher checks whether a newer version is available. It does this by comparing the installed version against git release tags in the source repository — no separate update server, no package index query.

The check runs at most once per day. The dispatcher records a "last checked" timestamp and skips the check if less than 24 hours have passed.

### Graceful offline behaviour

If the check fails (no network, repository unreachable), the dispatcher does not retry, does not block, and does not update the "last checked" timestamp. The next launch will try again naturally because the timestamp was not advanced. No retry loop, no error beyond a quiet log entry.

### Manual update

`aide update` forces an immediate update check and applies any available update. Available both as a subcommand and as an item in the interactive menu.

When a newer version is found (by either the automatic or manual check), the dispatcher reports what is available and applies it. The mechanism is a pip install from the git repository — the same command used for initial installation, pointed at the newer tag.

---

## Include and exclude

### Principle

Registration finds everything. Settings decide what is shown.

This is a settings concern, not a registration concern. The dispatcher scans the `utilities/` subpackage and discovers all conforming modules. The settings then filter which of those are presented in the menu and available as subcommands.

### Mechanism

A deny list in settings. Every discovered utility is available by default. To hide one, name it in the exclude list. There is no allow list — the default is "everything on."

### Scope

Both global and per-project, on the same deep-merge model as all other settings. A global exclude hides a utility everywhere. A per-project exclude hides it for that project only, without affecting global availability.

The merge means a project can exclude utilities that are globally available, or (by overriding the exclude list) restore utilities that are globally excluded. The same deep-merge rules apply.

---

## What this document does not cover

- The internal design of the three existing utilities — those are owned by File Operations in Working Practices.
- The broader question of whether utilities grow into a full AIDE CLI — that is a future direction, noted as a consideration, not designed for.
- The content of the global settings file beyond the structures needed for merge and exclude — each utility defines what settings it needs.

---

Version note: v1 — design document from voice session 2026-09-10. All four items were settled in conversation; this document records the design for handoff to a Code session.
<!-- END SOURCE: Infrastructure/Infrastructure_CLI_Design_v1.md -->

---

<!-- BEGIN SOURCE: Infrastructure/Infrastructure_Working_v1.md -->
Infrastructure | working | Infrastructure_Working@v1 | 2026-09-10

## Confirmed direction — session 2026-09-10

### Utility distribution model

Utilities are distributed as a pip package installed from git. `pip install git+https://github.com/...` installs the package and registers the `aide` command on PATH. Updates via `pip install --upgrade` or a self-update command (`aide update`).

The design-to-distribution workflow: update the utility design → rebuild the utility → commit to the utilities repo → user runs `aide update` or is prompted when a new version is available.

This mirrors the AIDE framework's approach to deploying capabilities: design, build, publish, and the consumer installs and updates.

### The aide dispatcher

A single entry point command — `aide` — on PATH. Behaviour:

- **No arguments** — interactive text menu listing available utilities. User selects and runs.
- **With subcommand** — runs directly, e.g. `aide binder-build`, for users who know what they want.
- **Customisation** — allows configuring settings for utilities within the interactive interface.

The dispatcher also serves as the registration point for utilities — adding a utility means adding a module to the package and registering a subcommand. New utilities appear in the menu automatically.

### Per-project launcher

A simple batch file (or similar) placed in the project's documentation folder. Runs the `aide` dispatcher targeting the current folder. Provides right-click or double-click access from Explorer without requiring a terminal.

### Settings model

Global defaults with per-project overrides. Global settings live with the central utility installation. Per-project settings live in the project's documentation folder (in `_utilities/` or `_config/`). The dispatcher merges them — global provides defaults, per-project overrides where needed.

Log files can go to a subfolder under the per-project settings location.

When launching, the execution folder is passed to the utility. The utility probes for settings files relative to the execution location, loads and uses them. If settings are edited within the aide interactive interface, they are written back to the same location.

### Items needing further design

- Utility registration mechanism — how the dispatcher discovers available utilities (subdirectory scan, config file, or package entry points)
- Detailed settings file format and merging rules
- Auto-update behaviour — check on launch, prompt, or silent
- Include/exclude mechanism — option to manually include or exclude utilities, install by default or prompt for new ones

---

Version note: v1 — initial working document from session 2026-09-10. Confirmed direction, not complete design.
<!-- END SOURCE: Infrastructure/Infrastructure_Working_v1.md -->

---

<!-- BEGIN SOURCE: Infrastructure/version-cleanup/README.md -->
# version cleanup

Moves superseded document versions out of the live tree, so a folder only ever
shows the current version of each document.

This folder is the **master copy**. To use the tool, copy `version_cleanup.py`
and `version_cleanup_settings.json` to wherever it should run from, then edit
that copy's settings. Each instance keeps its own settings file and its own log
beside the script, so instances never interfere with each other.

---

## What it does

In each folder it visits, it looks for files whose names are identical apart
from a `_v<number>` suffix immediately before the extension. The highest number
stays put; every lower version moves into a `_superseded` subfolder of the same
folder.

| Files in a folder | Result |
| --- | --- |
| `Foo_v8.md`, `Foo_v9.md` | `Foo_v8.md` moves, `Foo_v9.md` stays |
| `Foo.md`, `Foo_v1.md` | `Foo.md` moves — no suffix counts as v0 |
| `Foo_v3.md` on its own | nothing happens |
| `Foo_v1.md`, `Foo_v2.txt` | nothing happens — extensions must match too |

Grouping is **per folder**. The walk is recursive, but `Foo_v8.md` in one folder
is never compared with `Foo_v9.md` in another. Anything more complicated than
that is a manual job.

Folders whose name starts with an underscore are skipped, which is what keeps
the tool out of the `_superseded` folders it creates.

Nothing is ever overwritten. If a file of the same name is already sitting in
`_superseded`, the source file is left where it is and the run reports a
conflict.

---

## Installing Python on Windows

Only needed once per machine. The tool uses nothing beyond the Python standard
library, so there is nothing else to install.

1. Go to <https://www.python.org/downloads/windows/> and download the latest
   **Windows installer (64-bit)**. Python 3.8 or newer is required; any current
   release is fine.
2. Run the installer. On the first screen, **tick "Add python.exe to PATH"**
   before clicking Install. This is easy to miss and is the usual reason a
   `.py` file will not run afterwards.
3. Choose **Install Now**.
4. To check it worked, open PowerShell and run:

   ```
   python --version
   ```

   It should print something like `Python 3.13.1`.

### Making double-click work

The standard installer associates `.py` files with the Python launcher, so
double-clicking `version_cleanup.py` in File Explorer should just run it. If it
instead opens in Notepad or asks which app to use:

1. Right-click `version_cleanup.py` → **Open with** → **Choose another app**.
2. Pick **Python** (or browse to `C:\Windows\py.exe`).
3. Tick **Always use this app to open .py files**.

The script pauses with *"Press Enter to close..."* when it finishes, so the
console window stays open long enough to read the report.

### Running it from a terminal instead

```
python "C:\path\to\version_cleanup.py"
```

---

## Settings

The script reads `version_cleanup_settings.json` from **its own folder** — not
from wherever the terminal happens to be pointing. If that file is missing, the
script writes a fresh one with default values and explanatory notes, then tells
you to check it.

```json
{
  "root": "..",
  "include": [],
  "exclude": [],
  "log_file": "version_cleanup.log"
}
```

| Setting | Meaning |
| --- | --- |
| `root` | The folder to tidy, including everything beneath it. |
| `include` | Underscore-prefixed folders to process anyway. |
| `exclude` | Folders to skip entirely, along with everything inside them. |
| `log_file` | Where the run log is appended. |

**`root` and `log_file`** take a full path, or a path measured from the folder
the script lives in — so `".."` means "the folder above me", and an instance
sitting in `Documentation/_tools` tidies `Documentation` by default.

**`include` and `exclude`** take three kinds of path:

| Form | Example | Means |
| --- | --- | --- |
| Absolute | `"C:/Docs/_binder"` | that one exact folder |
| Root-anchored | `"~/_binder"` | that one exact folder, measured from `root` |
| Relative | `"_binder"` | a **pattern**: every folder in the tree whose path ends with those segments |

The relative form is the useful one for a corpus. `"_binder"` is not a place,
it is a shape — it matches a `_binder` subfolder wherever one appears, at
any depth. Several segments work too: `"_binder/current"` matches any
`.../_binder/current`.

Two consequences worth holding on to:

- `"~"` here means **the root of the tree being tidied**, never your home
  folder. The tool never expands `~` the way a shell would.
- A relative entry in `exclude` is powerful in the same way. `"_superseded"`
  would skip every `_superseded` folder in the tree, not one of them.

**Writing paths in JSON.** Use forward slashes (`"C:/Users/you/Documents"`) or
doubled backslashes (`"C:\\Users\\you"`); a single backslash is an escape
character in JSON and will break the file.

**Comments.** JSON has no comment syntax, so the notes in the shipped settings
file are carried as keys beginning with `_comment`. They are ordinary JSON and
the tool ignores them. Leave them, edit them, or delete them as you prefer.

**Exclude always wins over include**, and excluding a folder excludes
everything inside it.

To reach a folder nested inside an underscore-prefixed one, just name the
folder you actually want — the walk passes through the underscore folder to
get there without processing its own files.

Example: process every `_binder` in the tree, plus the one `_holding` folder
at the top, and stay out of one scratch area entirely.

```json
{
  "root": "..",
  "include": ["_binder", "~/_holding"],
  "exclude": ["~/Working Practices/scratch"],
  "log_file": "version_cleanup.log"
}
```

The run report echoes the include and exclude lists whenever they are in use,
so a log entry always says which rules produced it.

---

## Running it

Live by default — there is no confirmation prompt:

```
python version_cleanup.py
```

Report only, changes nothing:

```
python version_cleanup.py --dry-run
```

The dry run produces exactly the same report as a live run, with `WOULD MOVE`
in place of `MOVED`. It is the safe way to check a new `root` or a new
include/exclude list before letting the tool loose on a tree.

---

## The log

Every run appends one entry to the log file, live and dry-run alike, each
stamped with the date, the mode and the root it was pointed at. The log is
never rewritten or trimmed. If it grows unwieldy, archive or delete it by hand;
the tool will start a fresh one.

---

## When it declines to act

Two cases where the tool deliberately does nothing and tells you instead:

- **CONFLICT** — a file of that name already exists in `_superseded`. Two
  different documents are competing for one archive slot. Resolve it by hand.
- **AMBIGUOUS** — two files in the folder claim the same version number, which
  can only happen through leading zeros (`Foo_v08.md` and `Foo_v8.md`). Nothing
  in that group moves, because which one is current is genuinely unclear.

---

## Scope

It tidies versions. It does not build binders and it does not deploy anything.
Those are separate tools, run in sequence.
<!-- END SOURCE: Infrastructure/version-cleanup/README.md -->

---

<!-- BEGIN SOURCE: Infrastructure/version-cleanup/version_cleanup_settings.json -->
{
  "_comment": "Settings for the version cleanup tool. Edit the values below. Any key starting with _comment is ignored by the tool - JSON has no comment syntax, so notes live in keys like this one.",

  "_comment_root": "The folder to tidy, including everything beneath it. A relative path is resolved against the folder this script lives in, so \"..\" means the parent folder. Give a full path such as \"C:/Users/you/Documents\" to point somewhere else. Forward slashes are safe on Windows.",
  "root": "..",

  "_comment_paths": "include and exclude accept three kinds of path. ABSOLUTE - \"C:/Docs/_binder\" - names one exact folder. ROOT-ANCHORED - \"~/_binder\" - names one exact folder, measured from the root above. RELATIVE - \"_binder\" - is a pattern rather than a place: it matches every folder in the tree whose path ends with those segments, so one entry covers a _binder subfolder wherever it appears. Note that ~ means the root of the tree here, never your home folder.",

  "_comment_include": "Folders whose names start with an underscore are skipped by default. List any that should be processed anyway. Example: [\"_binder\"] processes every _binder folder in the tree; [\"~/_binder\"] processes only the one at the top.",
  "include": [],

  "_comment_exclude": "Folders to skip entirely, along with everything inside them. Exclude always wins over include. A relative entry here is powerful: \"_superseded\" would skip every _superseded folder in the tree.",
  "exclude": [],

  "_comment_log_file": "Where the run log is appended. One entry per run, never overwritten. Absolute, or \"~/\" for root-anchored, or relative to the script folder.",
  "log_file": "version_cleanup.log"
}
<!-- END SOURCE: Infrastructure/version-cleanup/version_cleanup_settings.json -->

---

<!-- BEGIN SOURCE: Infrastructure/version-cleanup/VersionCleanup_Design_v3.md -->
# Version Cleanup — Design

> **Version 3** (2026-09-04). Corrects the master folder path after the rename to `version-cleanup`.
> v2 added objective, contents, definition of done and sibling
> relationships; records the three-form path model's ratification as an Infrastructure-wide
> convention; reframes verification as required cases rather than a build record. No behaviour
> change from v1.

## Contents

- **Position and objective** — what this is, what it must achieve, its boundary.
- **The matching rule** — document identity, version comparison, deliberate limits.
- **Folder scope** — descend versus process, and the three path forms.
- **Archive behaviour** — where superseded files go and what is never overwritten.
- **Execution model** — master/instance deployment and script-folder resolution.
- **The three files** — script, settings contract, log contract.
- **Run modes and report vocabulary.**
- **Definition of done, idempotence, boundary, required verification cases.**

## Position

Version cleanup is the first piece of **Infrastructure** for the AIDE documentation corpus:
machinery that acts on the document tree but is never loaded into an AI session. It has no
authority over document content and states no methodology; it enforces one physical property of
the tree.

It is a **single-action tool**, not a framework. Sibling tools are separate scripts run in
sequence. There is deliberately no action registry, plugin system or shared base class. Any
commonality between siblings is resolved when the duplication is visible, not in anticipation of
it.

### Relationship to siblings

Version cleanup runs **first** in the corpus pipeline, so tools downstream can take what they find
without version reasoning:

```text
version cleanup  →  binder builder  →  (later siblings)
```

Binder builder supersedes its own previous output within its own folder, so version cleanup never
needs pointing at `_binder`. The governing principle: **a tool cleans up after itself; version
cleanup handles supersession it did not cause.**

## Objective

Keep the live document tree holding exactly one version of each document, so anything reading the
tree — a person, a sibling tool, or an AI loading context — finds the current document without
having to reason about which one it is.

```text
document tree containing many versions per document
  → walk each folder
  → group that folder's files by document identity
  → keep the highest version in place
  → move every lower version into that folder's _superseded
  → report + append log entry
```

## The matching rule

Two files are the same document at different versions when their filenames are identical except
for a `_v<number>` suffix immediately before the extension, and their extensions match.

```text
identity  =  (filename with any trailing _v<number> removed, extension)
version   =  the digits in that suffix, or 0 when there is no suffix
```

| Case | Behaviour |
| --- | --- |
| `Foo_v8.md`, `Foo_v9.md` | `Foo_v8.md` superseded |
| `Foo.md`, `Foo_v1.md` | `Foo.md` superseded — absent suffix is v0 |
| `Foo_v3.md` alone | stays, suffix or not |
| `Foo_v1.md`, `Foo_v2.txt` | different documents — extension is part of identity |
| `Foo_v2_draft.md` | no match — the suffix must be terminal |

Treating an unsuffixed file as v0 removes the special case: `Foo.md` versus `Foo_v1.md` is decided
by the same comparison as `Foo_v8.md` versus `Foo_v9.md`.

Highest number stays; all lower versions move. Version numbers are compared numerically, so
`_v10` outranks `_v9`.

### Deliberate limits

- **Case.** `_v` and `_V` are both recognised. The document identity itself is compared with exact
  case, so `Foo_v1.md` and `foo_v2.md` are two documents and neither moves. Conservative by intent.
- **Ties.** Two files can share a version number only through leading zeros (`Foo_v08.md`,
  `Foo_v8.md`). Which is current is then genuinely unclear, so the tool reports `AMBIGUOUS` and
  moves nothing in that group.
- **Compound extensions.** Only the final extension is treated as the extension, so
  `Foo_v8.tar.gz` has identity `Foo_v8.tar` and never matches. Not a concern for a document corpus.

**The general shape:** where a rule does not determine an answer, report it and move nothing. This
applies to every case in this class, not only ties.

## Folder scope

Grouping is **per folder**. The walk is recursive and visits every folder, but each folder is
compared only against itself. Cross-folder version relationships are handled manually and are out
of scope.

Two distinct questions are asked of every folder:

| Question | Rule |
| --- | --- |
| **Descend** into it? | Not excluded, and either its name does not start with `_`, or it is on the include list, or it is an ancestor of something on the include list. |
| **Process** its own files? | Not excluded, and either its name does not start with `_`, or it is on the include list. |

The distinction matters: an underscore-prefixed folder that merely sits on the path to an included
folder is walked through without its own files being touched.

- The underscore rule is what keeps the tool out of the `_superseded` folders it creates. It is
  the mechanism, not a convention layered on top of one.
- The **root** is an explicit choice in the settings file, so the underscore rule does not apply
  to it. An explicit exclude still does.
- Exclude wins over include. Pruning at an excluded folder is what makes exclusion inherited:
  once a branch is skipped, nothing inside it is ever asked about again.
- Directory symlinks are not followed, so a link cannot cause one tree to be tidied twice.

### Path forms for include and exclude

The tree needs two different kinds of statement: *this exact folder*, and *any folder shaped
like this*. Three spellings carry them.

| Form | Example | Resolution |
| --- | --- | --- |
| Absolute | `C:/Docs/_binder` | one exact folder |
| Root-anchored | `~/_binder` | one exact folder, measured from `root` |
| Relative | `_binder` | a **pattern**, tested against every folder the walk reaches |

**Status: ratified as the Infrastructure-wide convention** (2026-09-04). This is not a local choice
of this tool. Binder builder and later siblings use the same vocabulary; a divergent path model in
a sibling is a defect.

A relative entry is not resolved once at startup. It is a shape, matched when a folder's path
**ends with** the entry's segments, so `_binder` covers a `_binder` subfolder at any depth and
`_binder/current` matches any `.../_binder/current`. The comparison is made against the path
measured from the root, so a pattern can never reach above the root, and the root itself is never
matched by one.

Consequences taken deliberately:

- `~` means the **root of the tree**, never the home folder. `expanduser` is never called on
  these settings, so `~/` cannot quietly resolve to a user profile directory. This is a one-way
  door on that character across Infrastructure.
- The `root` setting itself cannot use `~/`, since it is what defines the root. It takes an
  absolute path or one relative to the script folder, and rejects `~/` with that explanation.
- `..` is rejected inside a relative entry. A pattern has no anchor for it, so silently accepting
  one would produce an entry that never matches.
- Path comparison goes through `os.path.normcase`: case-insensitive on Windows, case-sensitive
  elsewhere. Matching therefore follows the local filesystem rather than diverging from it.
- The multi-segment form needs lookahead. A folder matching a *proper prefix* of an include
  pattern is descended into but not processed, which is how `_binder/current` reaches `current`
  through an underscore-prefixed parent.
- A relative `exclude` entry is correspondingly broad: `_superseded` would skip every such folder
  in the tree. That is the intent, and it is stated in the shipped settings file.

## Archive behaviour

Superseded files move into `_superseded`, a subfolder of the folder the file came from. It is
created lazily — a folder with nothing to archive never gains an empty `_superseded`.

**Nothing is ever overwritten.** If the destination name already exists, the source file is left
in place and the run reports `CONFLICT`. Two different documents competing for one archive slot is
a decision for a person. The destination is re-checked immediately before the move, because
`shutil.move` overwrites silently on Linux and macOS.

Files are moved, not copied and deleted; source and destination are always on the same volume.

## Execution model

```text
Documentation/Infrastructure/version-cleanup/        ← master, source of truth
        │  copy
        ▼
Documentation/_tools/                                ← instance: own settings, own log
```

Each instance resolves its settings file, its log and its root against **the folder holding the
script**, never against the current working directory. The working directory varies with how the
script was launched (double-click, terminal, scheduler) and is unreliable; the script folder does
not. This is also what gives each instance its own settings and its own log without any instance
registry.

Changes are made to the master and redeployed by copying. Instances are not edited in place except
for their settings file.

## The three files

| File | Role |
| --- | --- |
| `version_cleanup.py` | The script. Standard library only, Python 3.8+, cross-platform. |
| `version_cleanup_settings.json` | Per-instance configuration, read on launch. |
| `version_cleanup.log` | Append-only record, one entry per run. Created on first run. |

`README.md` and this design document travel with the master and are not required at runtime.

### Settings contract

```json
{
  "root": "..",
  "include": [],
  "exclude": [],
  "log_file": "version_cleanup.log"
}
```

- **JSON** — no third-party parser needed, editable by hand, and a syntax error is reported with
  line and column rather than as a stack trace.
- JSON has no comment syntax, so the shipped defaults carry their explanatory notes as keys
  beginning with `_comment`. The loader ignores them. The alternative — a JSONC dialect with a
  hand-written comment stripper — buys nothing and adds a parser to maintain.
- `root` and `log_file` resolve against the script folder when relative, so `".."` means "the
  folder above the tool" — the right default for an instance living in `Documentation/_tools`.
  `include` and `exclude` use the three path forms above.
- A missing settings file is written from the shipped defaults rather than being an error, so a
  bare `.py` copied to a new location bootstraps itself.

### Log contract

Append-only, one entry per run, never rewritten or trimmed. Dry runs are logged too, clearly
marked, so the log is a complete record of every time the tool was pointed at the tree. The
on-screen report and the log entry are produced by one function and cannot drift apart.

## Run modes

| Mode | Behaviour |
| --- | --- |
| default | Live. No confirmation prompt. |
| `--dry-run` | Identical report, `WOULD MOVE` in place of `MOVED`, nothing changed. |

Planning and acting are separate stages: `plan_folder` decides, `apply_moves` acts. A dry run
executes the same decision code as a live run, which is what makes it a trustworthy preview rather
than a parallel implementation.

The script pauses for a keypress before exiting so a double-clicked run can be read. The pause is
skipped when no interactive console is attached, so a scheduled run cannot hang on it.

## Report vocabulary

| Kind | Meaning |
| --- | --- |
| `MOVED` | File moved into `_superseded`. |
| `WOULD MOVE` | Dry run — the same file, unmoved. |
| `CONFLICT` | Destination name already taken; source left in place. |
| `AMBIGUOUS` | Duplicate version numbers in one group; nothing in the group moved. |
| `ERROR` | Filesystem refusal — locked file, permissions, unreadable folder. |

Events are grouped by folder in the report. A single failure does not abandon the run: the tool
reports it and continues, so the tree is never left half-tidied by an unrelated locked file.

Exit code is `0` unless at least one `ERROR` occurred. Conflicts and ambiguities are expected
outcomes requiring human attention, not failures of the run.

## Definition of done

Point an instance at a tree and afterwards that tree holds one version of each document, with
lower versions moved into `_superseded` beside where they lived, a readable on-screen report, and
one appended log entry. A dry run produces the identical report and changes nothing. Conflicts and
ambiguities are reported rather than resolved.

## Idempotence

Running the tool twice over the same tree produces no further movement. `_superseded` folders are
underscore-prefixed and therefore outside scope on the second pass; every remaining folder holds
one version per document, so no group has a superseded member.

## Out of scope — hard boundary

Version cleanup tidies versions. It does not assemble binders, does not deploy, does not edit
document content, does not rename files, and does not delete anything. Superseded material is
moved, never removed. Deletion from `_superseded` is a human act.

## Required verification cases

The cases the tool must handle. This is the regression set for any future change, not a record of
one build.

- **Matching** — multi-version groups including `_v10` versus `_v9`; unsuffixed v0; lone versioned
  files; extension mismatch; leading-zero ambiguity.
- **Scope** — nested folders; default underscore skip; all three include forms (a relative pattern
  catching several `_binder` folders at different depths, root-anchored catching only the top one,
  absolute catching one exact folder); a multi-segment pattern traversing an underscore parent
  without processing it; relative and root-anchored excludes.
- **Refusals** — pre-existing archive conflict; malformed JSON; missing root; `..` in a relative
  entry; bare `~`; `~name`; `~/` in the root setting.
- **Repeatability** — a second live run over a tidied tree moving nothing.
<!-- END SOURCE: Infrastructure/version-cleanup/VersionCleanup_Design_v3.md -->

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

---

<!-- BEGIN SOURCE: Project Design/_index.md -->
Project Design | _index | ProjectDesign_Index@v1 | 2026-09-11

Project Design produces a coherent specification for work of any size and manages the response from build as it pertains to design. Fluid in, precise out — it owns both ends of the design-build loop.

## Documents

| Prefix | Document | Type |
|---|---|---|
| ProjectDesign_ | Design v1 | design |
| ProjectDesign_ | Decisions v1 | decisions |
| ProjectDesign_ | Standard v2 | standard |

## Parts

None declared.
<!-- END SOURCE: Project Design/_index.md -->

---

<!-- BEGIN SOURCE: Project Design/ProjectDesign_Decisions_v1.md -->
Project Design — Decisions | decisions | ProjectDesign_Decisions@v1 | 2026-09-11

## D1 — Work register survives and comes home to Project Design

The gap the register fills is temporal, not interpersonal — something must hold "design says X, build hasn't caught up yet." The register is the one artefact where design is both source and target, which is why its states must reconcile against build return. Splitting the producer rule from its own ledger was the original model's mistake. The provider-consumer test settles it: the temporal gap only exists because Project Design owns both ends of the loop — it does not carry meaning outside Project Design.

The alternative — register in Working Practices, producer obligation in Project Design — was tried and withdrawn during this pass.

## D2 — Work item and work register are distinct in kind

There is no subset relationship and none should be implied. A work item is a generic entity flowing through a workflow: raised, judged, given a fate. A work register entry exists because a design change had a downstream impact that has not yet been delivered — different origin, different purpose, different owner. Collapsing them would erase exactly the meaning that makes the register worth having.

The name "work register" was reopened and tested against alternatives (delivery register, obligations register, consequence register, impact register, pending work register). "Obligations" was rejected as too amorphous. "Work register" stands: concrete, side-neutral, and reads cleanly as the register of work owed now that work item and work register are firmly separated.

## D3 — The design-build handoff replaces the work-package doctype

The work-package doctype was designed very early in the original implementation and never reviewed. It was a fixed artefact; the invariant it protected — the responsibility boundary — does not require one. Replaced by the design-build handoff: a transition point whose mechanism varies by build context.

The old doctype's reach was wide: Index references, the flow diagram, the handoff clause, the release lineage, and six decisions (D4, D7, D8, D12 and others). All of these either fall away or are re-grounded in the new mechanism.

Any surviving build-side "work package" is renamed build package so the word "work" is left free and the two never collide.

## D4 — The design doctype is criteria and advice, not a schema

Design composition varies a great deal by project type and build outcome. A schema would constrain composition; criteria describe what the design must achieve regardless of its shape. This is the facilitate-not-constrain position doing its work: AIDE exists to facilitate and empower, not to constrain or be a source of friction.

Nine required criteria, four advice items. The criteria tell the author what a good design must do; the advice tells how others have done it well.

## D5 — Design carries its own live reasoning inline

A design element is a two-part unit: the statement of what is true, plus its inline why. A separate reasoning block was considered and rejected — the reading pattern demands the why at the element, and inline is what makes the retention checkpoint a natural act rather than a bolted-on chore.

Duplication with decisions is accepted and expected: design holds the live why; decisions holds the fuller why, including paths not taken. The authority clause governs: reasoning pertinent to a current design choice belongs in the design.

## D6 — Overview survives as a Project Design doctype

Overview was parked in the block-catalogue session, with discussion reserved for the design pass. The parked return condition was topic-or-corpus scale; this pass corrects that — the real return condition is function, at project scale.

The overview is a purposeful pane-of-glass snapshot and deviation detector, not an overflow valve for a bloated summary. This directly contradicts the old binder's orientation section, which made overview an escalation from summary. The forward design wins; the old orientation section is dropped entirely.

## D7 — The summary suppression rule

Overview and summary do not make each other redundant, but no document ever carries both. While an overview lives inline, the host document does not also carry a summary. The moment the overview branches out to its own document, the source document gets a summary back. The rule prevents double-orienting, which wastes context and confuses consumers about which one governs.

## D8 — Capture and place reframed as a filing obligation, not a workflow entity

An earlier framing treated capture as an act, placement as a fate, and the work item as its subject. That was wrong. The real thing is narrower: a design conversation wanders, and the AI's job is that nothing said gets left where it fell. Each piece gets put where it belongs.

The work-item type list — expected in the earlier framing — does not belong here. It stays with Working Practices, to be surfaced when the work item is designed there, or left unenumerated if nothing demands it.

## D9 — The what/why vs how boundary replaces the old escalation list

The old binder enumerated what returns to design: objective, major scope, acceptance, ownership, architecture, policy. That enumeration is demoted to illustration; a single test replaces it: does what build encountered change what is being delivered or why, or only how it gets delivered? A list is arguable at the margin and rots as the system grows; a test does not.

The tiebreak — if build cannot tell which side it is on, it returns — makes the default deliberately asymmetric. An unnecessary return costs a message. Silently absorbing a design change costs the design's authority.

## D10 — The cost-and-complexity flag is an obligation, not a threshold

Rather than prescribe a numeric or percentage trigger, the flag is an obligation on build's judgement: when the real cost or complexity materially exceeds what the design appeared to assume, build surfaces it. No threshold, no how-long-is-a-piece-of-string test. A rule with a number would be exactly the friction facilitate-not-constrain exists to remove.

The flag defaults to proceed — if design does not intervene, build continues. This gives build two distinct reasons to come back, at different weights: a return for a genuine what/why question, and a flag where it can proceed but the price has moved.

## D11 — Superseded register items: judgement, not procedure

A fixed procedure was drafted for handling superseded items after handoff (freeze the entry, raise a superseding entry, notify build, reconcile) and withdrawn. The right answer genuinely varies — build might have finished, not started, or be halfway through. A fixed rule would get most cases wrong.

The requirement is narrow and strong: design determines the impact and the remedy, makes the call explicitly, and records it. Not that it follows a set path. This is the first instance in this design where facilitate-not-constrain changed a decision rather than sitting inert.

## D12 — Partial coverage dissolved by the register writing rule

Register items are written as logical blocks of work — no children, no task tree. A return covering less than an item is not a partial-coverage case; it is done with deviation or an issue, and reconciliation already handles it. This dissolves the old model's partial/blocked branch and the work-package coverage-ID mechanism.

## D13 — No convergence mechanism for the loop

A return can provoke a design change, which spawns commitments, which spawn handoffs. Nothing terminates this, and nothing should: every trip round the loop is provoked by something real. If issues keep coming, the loop is not failing — the design is being told something. The only addition is visibility: an item that has been round several times is a design smell worth surfacing.

## D14 — Domain-generic demoted from objective to constraint

"Domain-generic" invited creative-production reach when stated as an objective. Demoted to a constraint on how the objectives are written. The claim survives — the purpose and requirements are generic across kinds of work — but as a property of the specification, not a thing to pursue.

## D15 — Design is the default — authored forward, not derived from the old corpus

The old decision D15 ("design is knowledge, not a mandatory document pipeline") was reference material for reasoning already explored. It is not carried forward, amended, or downgraded. The position is restated from the new design: a design almost always exists, and a standard almost always has a design behind it. Authoring straight to standard is the exception. The design holds the reasoning; the standard holds the conclusion. Forcing everything into the standard alone compromises one or the other.

## D16 — Register admits non-design-generated work

The old D12 explicitly held the register is not exclusively design-generated. Under sole ownership by Project Design, the question was whether it still admits confirmed non-design work. Resolved: yes. Each item tags its origin as design-generated or directly-entered. The discipline that real design work should not bypass design is a judgement at entry, not a mechanism.

## D17 — The six-stage per-component review procedure

Adopted as a general procedure for every component review:

1. Clarify purpose.
2. Clarify objectives, model, approach.
3. Discuss and resolve key issues.
4. Review requirements, resolve changes.
5. Work through how the brief is delivered — the design.
6. Review design output — standards etc.

Stages 4 and 6 author forward first: derive requirements from purpose and objectives without reading the old design, then run a two-part sweep of the old corpus as a resource (omissions sweep, approach sweep). The old corpus never gets a default seat.

## D18 — Domains closed as a considered no

No case for domains was raised by anyone. The old corpus used "domain" for two jobs: asserting Project Design is not software-shaped (a genericness claim needing an adjective, not a noun) and naming an owner for production workflows (which topics already do). Domain would be a second ownership axis alongside topic with no stated relationship. The claim survives; the word does not.

## D19 — The binder sweep findings

### Omissions (part 1) — five carried, two dropped, one parked

**Carried:** (1) build is never handed conflicting current designs — ninth design criterion; (2) state the model compactly — design advice; (3) handoff sufficiency has a ceiling — handoff mechanism; (4) requirement distinct from implementation choice — fifth boundary test; (5) linked build project or build outcome — brief section.

**Dropped:** (6) cross-topic reconciliation — absorbed by capture and place; (7) no generic top-level workflow owner — partly implied by purpose, rest may contradict Working Practices.

**Parked then fallen away:** (8) one authoritative instance per scope — blocked on domains, which are now closed.

### Approach (part 2) — eight items adopted

(1) The document set is design, decisions, standard and work register — no index (deferred, not dropped). (2) Four-group design structure (model / definitions / rules / boundaries). (3) Rule weight markers lifted — vocabulary flagged to Standards. (4) Fenced pseudo-flow blocks lifted. (5) Proportionate field list named as a technique. (6) All binder-editing items resolve as decisions against the new documents. (7) The orientation section dropped entirely — direct contradiction with the forward design. (8) The semantic-hosting park falls away with domains.

### Decisions maintenance — no new mechanism needed

The locked decisions/knowledge rules already govern compaction, immutability, and maintenance. The old decisions document's sprawl (22 entries with superseded material reading as current, release-issuance entries recording nothing) is what the settled rules look like unapplied. Compaction is the maintenance mechanism; meaning changes are new entries; release-issuance entries never create entries at all.

## D20 — The work register lives inside the binder

The register is written at master update, which is when the binder rebuilds anyway — the two are already synchronised and there is no churn to avoid. The old exclusion (register loads separately) was carried from the old binder without being tested against the new model. The decisive argument is context cost: separate loading means every session loads binder plus working document plus register, multiplied by however many registers exist.

Items may be written to the working document in the interim and moved to the register at master update.

## D21 — Pending content is placed content whose destination has not yet been written

Generalised from the register correction. The working document holds current working state and pending content destined for master documents not yet written. Pending content is held under its destination document — capture and place already knows the destination at filing time.

A master document is not authoritative alone between updates. The current position on any document is that document plus its pending content in the working document. Two consequences: the working document is always loaded with the topic; reading a master in order to act on it means checking its pending section first.

Not duplicated into each doctype — the property belongs to the two-tier memory model, not any one document type.

---

Version note: v1 — authored fresh from ProjectDesign_Decisions_Pending_v1, 2026-09-11.
<!-- END SOURCE: Project Design/ProjectDesign_Decisions_v1.md -->

---

<!-- BEGIN SOURCE: Project Design/ProjectDesign_Design_v1.md -->
Project Design — Design | design | ProjectDesign_Design@v1 | 2026-09-11

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
6. **Scale trivial to complex without changing method** — including at block level, with detail and language held proportional to scale.

**Definition of done.** The design specifies every element, mechanism and rule needed for a project design to flow from intent through to reconciliation. All six requirements are delivered, or explicitly deferred with a reason.

## The design shape

**One flow, three holding places, one seam.**

The flow: intent → capture and place → brief → design → commitments → register → handoff → build → reconcile.

The holding places: brief, design, overview — plus the work register, which is Project Design's own.

The seam: the design-build handoff — where responsibility crosses from design to build.

Three things to specify: the capture-and-place mechanism; brief-to-design delivery and elasticity; and the commitment-and-return loop. But the elements of a Project Design must be defined first — placement is routing, and each element's definition is the routing rule.

## The document set

**Owned doctypes:** brief (a composite block, mandatory), design, overview, and work register. The producer rule governs the relationship between design changes and the register.

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

Five tests settling where content belongs when the destination is not obvious. These are tie-breakers inside the brief, not top-level routing choices.

1. **Objectives vs requirements.** An objective is what success looks like; a requirement is a condition the solution must meet to get there. "Fast" is an objective; "responds within two seconds" is a requirement.
2. **Considerations vs decisions.** A consideration is live input still bearing on the design; the moment it resolves into a choice it moves to decisions.
3. **Requirements vs scope.** A requirement constrains the solution; scope bounds the work. "Must work offline" is a requirement; "the mobile client is out this phase" is scope. The tell: does it constrain the solution or the effort?
4. **Target/outcome vs definition of done.** The condition you check to say "finished" is definition of done. What you are trying to bring about is target/outcome.
5. **Requirement vs implementation choice.** A requirement states what the outcome must satisfy. A requirement written as "use X" rather than "must achieve Y" pre-decides the design inside the brief, closing the fluid space before it opens. This runs directly against Project Design's purpose — fluid in, precise out.

## Design document

### What the design is

The design is the current confirmed model and approach — the authoritative delivery of the brief. A point-in-time snapshot of what is true now; it must be sufficient on its own to produce outcomes, and it governs on conflict. It is the primary source for the build handoff.

The design carries its own live reasoning inline. Duplication with decisions is accepted and expected: design holds the live why for the current approach; decisions holds the fuller why, including paths not taken and reasoning that no longer bears on the current snapshot. This makes the design genuinely self-sufficient for the handoff without requiring the reader to find the reasoning elsewhere.

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
- Lead with the model before elaborating.
- State the model compactly before elaborating it; if it will not state cleanly, the model is wrong, not the write-up.
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

2. **Placement by destination definitions.** Settled things go to a permanent home — the brief if problem-space, the design if solution-space, decisions if topic-scoped reasoning, knowledge if reasoning with no owning topic. Unsettled things go to a holding place — WIP for live thinking, open items for a parked question, the work register for confirmed work owed. The brief boundary tests are tie-breakers inside the brief, not top-level choices.

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

Version note: v1 — authored fresh from ProjectDesign_Design_Pending_v1, 2026-09-11.
<!-- END SOURCE: Project Design/ProjectDesign_Design_v1.md -->

---

<!-- BEGIN SOURCE: Project Design/ProjectDesign_Standard_v1.md -->
Project Design — Standard | standard | ProjectDesign_Standard@v1 | 2026-09-11

## What Project Design is

Information. Project Design produces the design specification and manages the return from build. It owns both ends of the design-build loop — the outbound specification and reconciliation when build reports back. Purpose in two words: fluid in, precise out.

Information. The flow: intent → capture and place → brief → design → commitments → register → handoff → build → reconcile.

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
<!-- END SOURCE: Project Design/ProjectDesign_Standard_v1.md -->

---

<!-- BEGIN SOURCE: Project Design/ProjectDesign_Standard_v2.md -->
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
<!-- END SOURCE: Project Design/ProjectDesign_Standard_v2.md -->

---

<!-- BEGIN SOURCE: Standards/_index.md -->
# Standards

Role: component design

Standards defines how to create, design, build, and use a standard within the AIDE framework. It is a methodological component — it does not hold all standards. Individual standards are designed and owned by the component or area they serve, under the what-knows-most-about-it principle.

As a capability, Standards owns the definition of what a standard is, the authoring guidance (including leanness), and the pipeline from reference knowledge to deployed standard.
<!-- END SOURCE: Standards/_index.md -->

---

<!-- BEGIN SOURCE: Standards/Standards_Authoring_Standard_v2.md -->
Standards — Standard | standard | Standards_Authoring_Standard@v2 | 2026-09-11

## What a standard is

Information. A standard defines rules, expectations, guidance and context that shape decisions and behaviour while work is being done. It reaches the AI platform as a capability — a skill loaded on trigger, or binder content in project context. Everything behind it (the design, the decisions, the reference knowledge) stays outside the session.

Information. A standard earns its context cost. Everything in it displaces something else the session could hold.

## Authoring rules

**The carry test.** Required. Every item in a standard must pass: "is this needed at the moment of application?" Content that informed the design but is not needed when applying the standard stays in the design document. This is the single most important authoring rule.

**Leanness.** Required. Write the minimum language that achieves the guidance — not terse, not abbreviated, but with nothing that does not work. A well-authored standard leaves the consumer confident about what to do without carrying anything they do not need.

**Discriminating guidance.** Required. A rule that says "do X" without helping the consumer recognise when and how to apply it is governance without value. If the consumer would need to go back to the design to know how to apply a rule, the standard is incomplete.

**Strength assignment.** Required. Every item carries a strength, selected by the author from the vocabulary below. Over-use of required produces rigidity; over-use of optional achieves nothing.

**Self-containment.** Required. A standard must be understandable without its design document present in the session. It may reference the design for deeper reasoning, but must not depend on it being loaded.

## Strength vocabulary

Information. Four levels. These words and definitions are the standard vocabulary — use them consistently across all standards.

- **Required** — must comply. Departure is a defect.
- **Recommended** — should comply. Departure needs a reason, but the reason is the author's judgement, not an approval process.
- **Optional** — available for use. No compliance expectation.
- **Information** — awareness content. Exists so the consumer knows it, not so they act on it.

## Designing a standard

**Design is the default.** Recommended. A design almost always exists behind a standard. Authoring straight to standard is the exception — reserved for cases where the content is simple enough that a design would restate rather than elaborate.

**Author fresh.** Required. A standard is authored from its design, not by modifying a previous version of the standard. The design holds the reasoning and constraints; the standard holds the conclusion as guidance.

**No prescribed template.** Information. A standard has no fixed structure. The author decides what it contains and how it is organised, provided the authoring rules above are met.

## The reference-to-standard pipeline

Information. Reference documents are design-time knowledge. When reference knowledge needs to be present in the AI session, it is authored into a standard at information strength. The decision criterion is the carry test: does the consumer need to be aware of this knowledge at the moment of application? If yes, it earns a place. If it only informed the design, it stays in the design.

Information. Reference is a document type, not an output type. A reference informs the design process; a standard is the delivery mechanism. The distinction matters because it prevents reference from becoming a parallel output channel.

## Deployment

Information. Once a standard is authored and accepted, it is deployed as a capability — packaged by Infrastructure and delivered through the deployment pipeline. The author's responsibility ends at a complete, accepted standard. Packaging into a skill or plugin, and the weight gate that checks the combined load, are owned by Infrastructure and Deployment respectively.

## Ownership

**Each standard lives with its owning component.** Required. Standards is a methodological component — it defines how to build a standard, not where standards live. Each standard is designed and owned by the component or area it serves, under the what-knows-most-about-it principle.

---

Version note: v2 — revised after cross-review. Removed cross-review obligation (Working Practices, not Standards). Removed invented strength-assignment defaults. Added strength to context-setting items. Added deployment boundary. Restored reference document-type distinction.
<!-- END SOURCE: Standards/Standards_Authoring_Standard_v2.md -->

---

<!-- BEGIN SOURCE: Standards/Standards_Decisions_v1.md -->
Standards — Decisions | decisions | Standards_Decisions@v1 | 2026-09-10

## D1 — Standards is a methodological component, same pattern as Infrastructure and Tools

Standards defines how to create its type. Individual instances live with their consuming component. This was settled in the overview as the common pattern for all three capability-type components and confirmed in the structure session. The alternative — Standards holding all standards — was rejected because it violates the what-knows-most-about-it ownership principle.

## D2 — Five authoring rules, not a template

The authoring methodology is expressed as five rules (carry test, leanness, discriminating guidance, strength assignment, self-containment) rather than a prescribed template or structural specification. The author decides what a standard contains and how it is organised, provided it meets the terms.

A template risks becoming apparatus — a structure to fill in rather than a set of outcomes to achieve. The five rules already tell an author what a good standard must do. Document structure belongs to Documentation Methodology; Standards defines what the content must achieve, not what it must look like.

## D3 — Four strength levels, strength per item not per section

The strength model uses four levels: required, recommended, optional, information. The fourth level (information) was added specifically for reference-origin content that needs to reach the platform for awareness without carrying a compliance expectation.

Strength is a property of each item rather than a section organiser because a single standard will naturally mix levels — a section on authoring might contain two required rules, one recommended practice, and one piece of information context. Grouping by strength would break the logical flow of the guidance.

The vocabulary — the four words and their definitions — is standardised. This is the "rule weight markers" technique lifted from the Project Design binder sweep and given its home here, as flagged during that work.

## D4 — The carry test is the single authoring filter

"Is this needed at the moment of application" is the governing test for what goes into a standard. It was stated by Dave as a Standards-wide principle during the Project Design work and is the most important single rule in the authoring methodology.

The test sharpens the three-layer authoring model rather than contradicting it: discriminating guidance belongs in the standard even though it reads like elaboration, because placement and application judgements happen from whatever is memory-resident.

## D5 — Self-containment over cross-referencing

A standard must be understandable without its design document in the session. The alternative — a standard that assumes access to its design — would mean loading both documents to apply the guidance, doubling the context cost and defeating the purpose of the lean standard.

This does not prevent a standard from referencing its design for deeper reasoning. It prevents depending on the design being present.

## D6 — One primary output: the standards authoring standard

The authoring standard covers design, authoring, and deployment. A separate consumption standard — how to apply and work with standards once deployed — is available if it earns its place but is not assumed.

The consumption side probably does not need its own standard now. A well-authored standard is self-evident to consume: the strength levels tell the consumer what is required and what is guidance, and the self-containment rule means the standard explains itself. Good authoring makes consumption fall out naturally.

The boundary is deliberate: the authoring standard's scope stops at deployment. Implementation and consumption details would sit in the separate standard if one is ever needed.

## D7 — Settled decisions binding on Standards but owned elsewhere

Three decisions constrain Standards without being redefined by it:

- **The carry test** was stated as a rebuild-wide governing principle, not by this component. Standards must embody it but does not own the principle.
- **The cross-review requirement** comes from the three-layer authoring model: every authored standard is reviewed by a separate AI before acceptance. The obligation exists because of Standards; the process is a Working Practices collaboration convention.
- **The weight gate at deployment** checks the combined load when capabilities are packaged into a plugin. Standards owns leanness at authoring time; Deployment owns the gate at packaging time.

## D8 — The Contents/Summary edge is Documentation Methodology's concern

The edge between Contents and Summary was flagged during the Project Design work as "a common issue" for standards authors. It is carried to Documentation Methodology because the edge definition is about document-structure blocks — what Contents maps versus what Summary establishes — which is grammar, not authoring methodology. Standards authors will encounter the problem, but the solution belongs to whoever owns the grammar of those blocks.

---

Version note: v1 — initial decisions from the standards design session, 2026-09-10.
<!-- END SOURCE: Standards/Standards_Decisions_v1.md -->

---

<!-- BEGIN SOURCE: Standards/Standards_Design_v1.md -->
Standards — Design | design | Standards_Design@v1 | 2026-09-10

## Brief

**Purpose.** Define how a standard is designed, authored, and deployed within AIDE. Standards is a methodological component — it owns the methodology for building standards, not the standards themselves. Each standard is designed and owned by the component or area it serves, under the what-knows-most-about-it principle.

**Scope.** The authoring methodology, the strength model, the reference-to-standard pipeline, and the relationship between a standard and its design. Individual standards, document structure, packaging, and the cross-review process are out of scope.

**Target outcome.** A deployed standards authoring standard that any component author uses when designing, authoring, and deploying a standard for their component.

## What a standard achieves

A standard shapes decisions and behaviour at the moment of application. It reaches the AI platform as a capability — either as a skill loaded on trigger, or as binder content loaded into project context. In both cases, the standard is what the session consumes. Everything behind it — the design, the decisions, the reference knowledge — stays outside the session.

That single fact drives the authoring model: a standard carries only what is needed at the moment of application, because everything in it costs context space and attention.

## What Standards owns

### The authoring methodology

How to decide what goes into a standard, how to write it, and how lean is lean enough. Five rules govern authoring:

**The carry test.** Every item must pass: "is this needed at the moment of application?" Content that informed the design but is not needed when applying the standard stays in the design document.

**Leanness.** A standard earns its context cost. Every sentence displaces something else the session could hold. The target is the minimum language that achieves the guidance — not terse, not abbreviated, but with nothing that does not work. A well-authored standard reads as a short document that leaves the consumer confident about what to do.

**Discriminating guidance.** A standard that says "do X" without helping the consumer recognise when and how is governance without value. If the consumer would need to go back to the design to know how to apply a rule, the standard is incomplete.

**Strength assignment.** Every item carries one of the four strength levels. The author decides what strength each item warrants. Over-use of required produces a standard that reads as rigid; over-use of optional produces one that achieves nothing.

**Self-containment.** A standard must be understandable without its design document present in the session. It may reference the design for deeper reasoning, but it must not depend on it. The consumer has the standard; the design is available but not loaded.

### The strength model

Four levels defining how strongly an item in a standard applies:

- **Required** — must comply. Departure is a defect.
- **Recommended** — should comply. Departure needs a reason, but the reason is the author's judgement, not an approval process.
- **Optional** — available for use. No compliance expectation.
- **Information** — awareness content. Exists so the consumer knows it, not so they act on it.

Strength is a property of each item, not a section heading, because a single standard will mix levels. The vocabulary — the four words and their definitions above — is standardised so consumers read strengths consistently across all standards.

### The reference-to-standard pipeline

A reference is a design-time document type recording knowledge and concepts. When reference knowledge needs to reach the AI platform, it is authored into a standard at information strength. The decision criterion is the same carry test: does this knowledge need to be present at the moment of application? If the consumer needs to be aware of it to make good decisions, it earns a place. If it only informed the design, it stays in the design.

Reference is a document type only, not an output type. The distinction matters: a reference informs the design process; a standard is the delivery mechanism.

### The relationship between a standard and its design

A design almost always exists behind a standard — authoring straight to standard is the exception. The standard is authored fresh from the design, never by modifying a previous standard version. The design holds the reasoning, the alternatives, the constraints. The standard holds only the conclusion, stated as guidance.

The standard does not carry reasoning into the session. If a consumer needs to understand why a rule exists, the design is available outside the session — but the standard does not depend on it being present.

## What Standards produces

One standard: the standards authoring standard. It is aimed at anyone building a component, telling them how to design, author, and deploy a standard for that component. It consumes its own rules — the first standard is self-describing.

The authoring standard covers design, authoring, and deployment of standards. Implementation and consumption guidance, if it ever earns its place, would live in a separate standard, not in this one.

## What the author decides

A standard has no prescribed template. The author decides what the standard contains and how it is structured, provided it meets the terms defined in the standards authoring standard. The five authoring rules tell the author what a good standard achieves; the author meets them however the content demands.

## Boundaries

Standards does **not** own:

- **The three-layer authoring model** — a project-level convention consumed by all components, not a Standards mechanism.
- **The cross-review process** — the obligation that every standard is reviewed by a separate AI before acceptance is a collaboration convention owned by Working Practices. Standards' output goes through it.
- **Document structure and block grammar** — Documentation Methodology owns how documents are composed.
- **Packaging and delivery** — how a standard becomes a skill or binder entry is owned by Infrastructure (packaging) and Deployment (the weight gate and the pipeline to the marketplace).
- **Any individual standard** — each lives with its owning component.

## Carries to other components

**To Documentation Methodology:** the Contents/Summary edge — Contents maps what is where to judge relevance, Summary gives what the document establishes. Their edges need to stay distinct. Flagged as a common issue for standards authors; the edge definition is document-structure grammar.

---

Version note: v1 — initial design from the standards design session, 2026-09-10.
<!-- END SOURCE: Standards/Standards_Design_v1.md -->

---

<!-- BEGIN SOURCE: Standards/Standards_Working_v1.md -->
Standards | working | Standards_Working@v1 | 2026-09-10

## Confirmed items — session 2026-09-09

### Reference concept and its relationship to standards

A reference is a design-time document type recording knowledge and concepts. When reference knowledge needs to reach the AI platform, it is authored into a standard — it is not a separate capability or output type. Standards already encompass information delivery.

The strength model's fourth level (information) exists specifically for this case: reference-origin content carried in a standard for awareness, with no compliance expectation. The pipeline is: knowledge captured as a reference document during design → authored into a standard when it needs to reach the platform → deployed with information-level strength.

Reference is a document type only, not an output type. The distinction matters: a reference informs the design process; a standard is what reaches the platform. The standard is the delivery mechanism for both governance content and reference knowledge.

---

Version note: v1 — initial working document from session 2026-09-09.
<!-- END SOURCE: Standards/Standards_Working_v1.md -->

---

<!-- BEGIN SOURCE: Tools/Tools_Decisions_v1.md -->
Tools — Decisions | decisions | Tools_Decisions@v1 | 2026-09-11

## D1 — Tools is a methodological component, same pattern as Standards and Infrastructure

Tools defines how to create its type. Individual tool instances live with their consuming component. This was settled in the overview as the common pattern for all three capability-type components and confirmed in the structure session. The alternative — Tools holding all tools — was rejected because it violates the what-knows-most-about-it ownership principle.

## D2 — The invocability test is the governing boundary, owned by Tools

The standard-tool boundary was originally settled as D24 in the old corpus. The test — "if you would say 'run X,' X is a tool; if you would say 'follow the approach in Y,' that is a standard" — survived the rebuild because it is the cleanest available distinction. It says nothing about how the action is carried out, only whether it is invoked or consulted.

Ownership is placed in Tools rather than Standards because the ambiguous cases land here. Someone wondering "is this a standard or a tool?" is almost always holding something that looks invokable, so they are in Tools' territory. The standards side already describes what a standard is clearly enough that the "follow" case is self-evident; it is the "run" case that needs the discriminating guidance.

Standards carries a one-line information-strength pointer to the test rather than restating it. One authority, not two.

## D3 — Seven authoring concerns, not a template

The tool definition listed eight elements a tool "normally" defines. This was an indicative sketch from the terminology-setting session, not a deliberated design. Evaluation against the tool's purpose — encapsulating a repeatable action — produced seven concerns that earn their place, with adjustments:

- **Reporting folded into outputs and effects.** A report is an output. Every existing utility's log and on-screen report is an output of running the tool. Reporting does not need its own category.
- **Failure behaviour and idempotency separated.** The original list combined these into one slot, but they are different concerns. Failure behaviour is what happens when something goes wrong — universal and always relevant. Idempotency is a property of the tool — whether it is safe to run again — better declared alongside the tool's purpose than authored as a procedural section.

The same principle as Standards applies: these are concerns the author must address, not a structure to fill in. A simple tool might have no meaningful escalation conditions; a complex one might need something this list does not name. The author decides how to meet the terms.

## D4 — Tools are AI-performed capabilities

The old WIP carried the qualifier "NOT limited to executable code — migration is a tool and it's an AI task." This was dropped because it introduced confusion by blurring the line between tools and utilities. A tool is a capability; capabilities load into the AI session; the AI performs the procedure. That is the definition, and it does not need a qualifier saying what it is not.

The framework already has clean separation: tools load into the session and the AI executes them; utilities run outside the session and act on the corpus or infrastructure. The qualifier was trying to say tools are not just scripts, but it achieved this by muddying a boundary that was already drawn.

Dropping it also simplifies the authoring guidance. There is one execution context — AI in-session — not two to accommodate. The seven authoring concerns work cleanly for AI-performed procedures.

## D5 — The staging clause governs standard-to-tool transition

A standard may describe a procedure that ought to be a tool but is not yet built. This is legitimate staging, not a defect. When the tool is built, the standard's procedure section is replaced by a pointer to the tool, making the tool the single source.

The staging clause exists because building a tool is more work than describing a procedure in a standard, and the work should not be blocked while the tool is being built. The direction of travel is always toward the tool — a staged procedure is a known debt, not a permanent arrangement.

The clause also protects the invocability test from being treated as rigid: a standard carrying a temporary procedure does not violate the test provided the intent is to replace it. The test governs the steady state, not the transition.

## D6 — The sibling-outputs model governs tool-standard coexistence

A single design can produce both standards and tools. The design describes the behaviour; each output delivers the part of that behaviour appropriate to its type — guidance into a standard, invokable actions into tools. Both derive from the design, not from each other, so they cannot disagree.

This is expected to be common. A component or feature specified in a design may need guidance on how the work is approached (a standard) and a specific invokable action within that work (a tool). The design is the single source; the outputs are its delivery.

The model also prevents the synchronisation problem the invocability test was designed to avoid. Two sibling outputs from one design are coordinated by the design. Two independent documents covering the same behaviour — one as a standard, one as a tool — would drift.

## D7 — The standards authoring rules apply to tools

The five authoring rules (carry test, leanness, discriminating guidance, strength assignment, self-containment) are not Standards-specific — they are properties of any capability that loads into a session and costs context space. A tool that fails the carry test wastes context. A tool that is not self-contained requires its design to be loaded alongside it. The rules apply.

Tools does not restate them. The tool authoring standard consumes them by reference to the standards authoring methodology.

## D8 — Trigger description and segmentation rules are capability-wide

The 130-character trigger budget, front-loading of trigger words, segmentation along dependency lines, and self-containment of each sub-unit were agreed as part of the standards authoring standard v3. They are platform constraints, not standard-specific constraints. A tool deployed as a skill faces the same budget on the same platforms.

Tools applies these rules identically. They are not restated — the tool authoring standard references them as capability-wide rules.

## D9 — One primary output: the tool authoring standard

The tool authoring standard covers design, authoring, and deployment of tools. It parallels the standards authoring standard in scope and shape.

A separate consumption standard — how to invoke and work with tools once deployed — is not assumed. A well-authored tool is self-evident to invoke: the trigger description tells the consumer when to use it, the inputs tell them what to provide, and the procedure tells them what will happen. Good authoring makes consumption fall out naturally.

---

Version note: v1 — initial decisions from the tools design session, 2026-09-11.
<!-- END SOURCE: Tools/Tools_Decisions_v1.md -->

---

<!-- BEGIN SOURCE: Tools/Tools_Design_v1.md -->
Tools — Design | design | Tools_Design@v1 | 2026-09-11

## Brief

**Purpose.** Define what a tool is and how one is designed, authored, and deployed within AIDE. Tools is a methodological component — it owns the methodology for building tools, not the tools themselves. Each tool is designed and owned by the component or area it serves, under the what-knows-most-about-it principle.

**Scope.** The tool definition, the invocability test that draws the boundary between a tool and a standard, the authoring concerns a tool must address, the staging clause, and the sibling-outputs model. Individual tools, document structure, packaging, and the cross-review process are out of scope.

**Target outcome.** A deployed tool authoring standard that any component author uses when designing, authoring, and deploying a tool for their component.

## What a tool is and does

A tool encapsulates a repeatable, named, invokable action so its mechanism does not have to be re-derived each time. It reaches the AI platform as a capability — a skill loaded on trigger, or binder content loaded into project context. In both cases, the tool is what the session consumes. The AI performs the procedure the tool defines.

A tool is a capability. Capabilities are defined platform-neutral — the what — and transformed into platform-specific delivery. A tool loads into the AI session; the AI is the executor. This is what distinguishes a tool from a utility, which runs outside the session and acts on the corpus or infrastructure directly.

## The invocability test

The boundary between a tool and a standard is invocability. If you would say "run X," X is a tool. If you would say "follow the approach in Y," Y is a standard.

A standard shapes decisions and behaviour while work is being done — it is guidance you consult. A tool is a named thing you invoke to get a specific thing done — it is an action you run. A standard may describe a procedure, but it may not define an invokable action.

The reasoning: a named invokable thing must be a tool because only a tool carries the identity, structure, and authoring discipline that keeps a named action honest. A standard that restates an invokable action creates two authorities on the same thing, with no way to keep them in sync.

This test is the heart of the Tools component. It governs what is a tool and what is not.

## The staging clause

A standard may legitimately describe a procedure that ought to be a tool but is not yet built. That is a staging post, not a defect. The standard carries the procedure so the work can be done now; the intent is that a tool will replace it.

When the tool is built, the standard's procedure section is replaced by a pointer to the tool, so the tool becomes the single source. The standard no longer carries the procedure — it references the tool that does.

This is the only case where a standard may describe an invokable procedure without violating the invocability test. The staging is temporary, and the direction of travel is always toward the tool.

## The sibling-outputs model

A single design can produce both standards and tools as sibling outputs. The design describes the behaviour; the standard carries the guidance; the tool carries the invokable action. Both derive from the same design and therefore cannot disagree. Neither authors the other's content.

This is common. A component or feature may need a standard to shape how the work is approached and a tool to perform a specific action within it. The design specifies the full behaviour; the outputs are whatever delivers it — one or more standards, one or more tools, or a mix. Each output is authored from the design, not from its sibling.

## What Tools owns

### The tool definition

What a tool is, what it does, and what distinguishes it from a standard and a utility. The definitions are stated above. Tools owns these definitions and the invocability test that draws the boundary.

### The authoring concerns

Seven concerns a tool author must address. These are not a template — the author decides how to meet them, in whatever structure the content demands. They describe what a complete tool covers, so an author knows what to think about.

**Inputs.** What the tool needs in order to run. Without this, every invocation re-derives what to provide.

**Preconditions.** What must be true before invoking the tool. Running a tool when conditions are not met wastes effort or causes damage.

**Procedure.** The encapsulated mechanism — the sequence of steps the AI performs when the tool is invoked. This is the tool.

**Decision points.** Where judgement is needed during execution. Where the executor needs to think rather than follow. Essential for tools where the AI must choose between paths or assess a situation mid-procedure.

**Escalation conditions.** When to stop and hand back. The boundary between the tool and its invoker — "this is no longer yours, return to the caller." Different from a decision point: a decision point chooses between paths within the tool; an escalation condition exits the tool.

**Outputs and effects.** What the tool produces and what it changes. The invoker needs to know both — what they get back and what is different afterwards.

**Failure behaviour.** What happens when something goes wrong. How the tool reports failure, what state it leaves behind, and what the invoker should do next.

### Idempotency as a declared property

Whether a tool is safe to run again is a property the author declares about the tool, not a section within it. "This tool is idempotent" or "this tool is not safe to run twice" sits naturally alongside the tool's purpose, as a characteristic of the tool rather than a step in its procedure.

### The trigger description

Every tool carries a trigger description — the same mechanism and the same rules as for standards. The trigger description and segmentation rules are capability-wide: the 130-character budget, the front-loading of trigger words, segmentation along dependency lines, and self-containment of each sub-unit all apply to tools identically.

## What the author decides

A tool has no prescribed template. The author decides what the tool contains and how it is structured, provided it addresses the seven authoring concerns and meets the authoring rules inherited from the standards authoring methodology — the carry test, leanness, discriminating guidance, strength assignment, and self-containment. These rules apply to any capability, not only to standards.

## Boundaries

Tools does **not** own:

- **The standards authoring rules** — the carry test, leanness, discriminating guidance, strength assignment, and self-containment are Standards-wide rules that bind all capability authoring. Tools consumes them.
- **The three-layer authoring model** — a project-level convention consumed by all components, not a Tools mechanism.
- **The cross-review process** — the obligation that every capability is reviewed by a separate AI before acceptance is a collaboration convention owned by Working Practices. Tools' output goes through it.
- **Document structure and block grammar** — Documentation Methodology owns how documents are composed.
- **Packaging and delivery** — how a tool becomes a skill or binder entry is owned by Infrastructure (packaging) and Deployment (the weight gate and the pipeline to the marketplace).
- **Any individual tool** — each lives with its owning component.

## Carries to other components

**To Standards:** an information-strength pointer in the standards authoring standard noting that the invocability test in the tool authoring standard draws the boundary between the two capability types.

---

Version note: v1 — initial design from the tools design session, 2026-09-11.
<!-- END SOURCE: Tools/Tools_Design_v1.md -->

---

<!-- BEGIN SOURCE: Working Practices/_index.md -->
# Working Practices

Role: component design
Aliases: WP, workprac

Working Practices owns the conventions and behaviours for how an AI and user actually work together across surfaces. Cross-cutting operational conventions covering file handling, work management, content capture, content delivery, and how the human and AI collaborate.

## Parts

**File Operations** (prefix `WP_FileOps_`)
How files are physically managed — delivery, placement, versioning lifecycle, separation of design and output, git integration.

**Work Management** (prefix `WP_WorkManagement_`)
How work is tracked, progresses, and completes — work items, definition of done, pending content, development lifecycle, WIP conventions.

**Capture and Organisation** (prefix `WP_Capture_`)
How content is captured during work and allocated to its home — capture-and-place rules, session-end allocation, process document types.

**Content Delivery** (prefix `WP_ContentDelivery_`)
How content is assembled and delivered to the AI platform — binder concept, inclusion rules, context loading.

**Human-AI Collaboration** (prefix `WP_HumanAI_`)
How the AI works with the human — the human working model, tiering, confidence, drift detection, anomalies channel.
<!-- END SOURCE: Working Practices/_index.md -->

---

<!-- BEGIN SOURCE: Working Practices/FileOps/WP_FileOps_Working_v1.md -->
Working Practices — File Operations | working | WP_FileOps_Working@v1 | 2026-09-10

## Confirmed items — session 2026-09-10

### File delivery rules

Two rules for when files are updated outside of a FileUpdatePackage:

1. **Chat delivery** — when outputting an updated file for download, instruct the user where to save it based on the path in the document header.
2. **Code / Cowork direct file access** — check the file's physical location against the path in the header; move it if they disagree.

### Design and output separation

Design documents and the outputs they produce are separate. The design folder holds the specification. What gets built from it lives where it is consumed:

- Utilities → `_utilities/`
- Skills → deployed to the skills location
- Standards → deployed as capabilities
- Plugins → deployed to the marketplace

The design folder is always "why and how." The output is always elsewhere, wherever it runs.

### Superseded file handling

Git is the version history. The `_superseded` folder pattern is dropped. When a new version lands, the version-cleanup utility deletes the old version from the working tree and commits the deletion with a descriptive message. Rollback means `git checkout` of the previous version.

### Archived file handling

One `_archived` folder at the documentation root. Files that are no longer active but worth keeping — retired references, completed reviews, outdated knowledge. Moving a file there removes it from binder scope (underscore-prefixed folders are outside AIDE processing) while keeping it in the repo and searchable.

### Utility git commit behaviour

Utilities stage and commit their own changes with descriptive messages. When the FileUpdatePackage applies an update, or version-cleanup removes an old file, or the binder builder regenerates, the utility stages the changes, commits with a clear message (e.g. "FUP: applied Principles_2026-09-08"), and the user does not need to remember to commit.

### FUP move action

The FileUpdatePackage needs a move or rename action for when a document's path changes. The header is updated (authoritative change), the FUP manifest records the move (old path, new path), and the utility executes it. Extends the existing action vocabulary (create, replace) with move.

---

Version note: v1 — initial working document from session 2026-09-10.
<!-- END SOURCE: Working Practices/FileOps/WP_FileOps_Working_v1.md -->

---

<!-- BEGIN SOURCE: Working Practices/WP_Capture_Working_v1.md -->
Working Practices — Capture and Organisation | working | WP_Capture_Working@v1 | 2026-09-10

## Confirmed items

### Capture-and-place rules (confirmed earlier, restated)

Three AI obligations: continuous silent capture, placement by destination definitions, batched surfacing at natural breaks. Homeless pieces are named, not dropped. Claude errs toward over-capture.

### Session-end allocation convention (confirmed 2026-09-10)

At the end of a session or at a checkpoint, work through the session's output and confirm what goes where. It is acceptable to park items in WIP for a quick state save, and in a working document for a longer one, but the key discipline is allocating logic to its home. WIP and working knowledge should ultimately move to their destination and not sit in transition for too long.

This convention applies to every session that produces design decisions, not just formal design passes. The allocation step is part of capture-and-place, not a separate process.

### Process document types (confirmed 2026-09-09)

Three process-supporting document types owned by Workflow (Working Practices), not by Documentation Methodology:

- **Report** — a process document recording findings, analysis, or review results
- **Resource** — a reference or knowledge document supporting the work
- **Working document** — holds incomplete material, confirmed items awaiting placement, and in-progress thinking

These are workflow documents, not design outputs. Documentation Methodology owns the doctype mechanics; Working Practices owns these specific types because they serve the working process.

---

Version note: v1 — initial working document from sessions 2026-09-09 and 2026-09-10.
<!-- END SOURCE: Working Practices/WP_Capture_Working_v1.md -->

---

<!-- BEGIN SOURCE: Working Practices/WP_ContentDelivery_Working_v1.md -->
Working Practices — Content Delivery | working | WP_ContentDelivery_Working@v1 | 2026-09-10

## Confirmed items — session 2026-09-10

### Binder concept ownership

The binder exists to solve a workflow problem: assembling and delivering content to the AI platform for use in a session. Working Practices owns the concept — why the binder exists, how it is used, what it includes, how it delivers content. Documentation Methodology owns the binder as a doctype definition — its structure as a document.

### Three-tier inclusion model

What lives in a project folder falls into three tiers based on its relationship to the AI session:

1. **In the binder** — needed for thinking and reasoning. Design documents, and any other file the AI needs to see to do its work. The test: does it need to be there for thinking and reasoning? If so, include it.

2. **Known to the framework** — part of the project but not needed in context. Listed in the folder's `_index.md`. The framework knows it exists, can reference it, but does not load it. Scripts, settings files, assets.

3. **Just present** — incidental files. AIDE has no opinion. Logs, temp files, personal notes.

The binder is the context-loading mechanism. The `_index` is the awareness mechanism. Files that need neither are just files.

The key question for inclusion is not whether a file is a governed document, but whether it is needed for the work. A utility script that is the project's deliverable may belong in the binder when working on that utility, even though it has no declaration header.

---

Version note: v1 — initial working document from session 2026-09-10.
<!-- END SOURCE: Working Practices/WP_ContentDelivery_Working_v1.md -->

---

<!-- BEGIN SOURCE: Working Practices/WP_WorkManagement_Working_v1.md -->
Working Practices — Work Management | working | WP_WorkManagement_Working@v1 | 2026-09-10

## Development lifecycle — phase vs mode (confirmed 2026-09-09)

The development lifecycle has stages: research, design, build, deploy, review. These are **phases** — they describe what kind of work is being done at a point in time.

AIDE implements these phases as **modes**. A mode is a state the AI session operates in, shaped by which standards and tools are loaded and active. The distinction matters because phases are a general concept (any development process has them) while modes are AIDE's specific mechanism for making them real in a session.

The lifecycle concept is owned by Working Practices because it describes how work progresses — it is a workflow concern. Individual modes (the design mode, the build mode) are shaped by the components that own those phases — Project Design owns what happens during design, Build owns what happens during build.

## Pending content — items awaiting placement

The following confirmed items need design work before they can be placed in this document:

- **Work items** — the generic workflow entity (settled 2026-09-07, owned by WP). Definition, two axes (type and state), four states (open, current, closed, plus any additions). Full content is in the settled rebuild decisions
- **Definition of done** — generic block type owned by WP. The testable-or-assessable invariant. Full content in settled rebuild decisions
- **Pending content rule** — WIP holds current state AND pending content for unwritten masters. A master is not authoritative alone between updates. Full content in WIP v22
- **WP1–WP13** — the original Working Practices design items from the old corpus, to be reconciled against current decisions per finding F10 in the rebuild guide

---

Version note: v1 — initial working document from sessions 2026-09-09 and 2026-09-10.
<!-- END SOURCE: Working Practices/WP_WorkManagement_Working_v1.md -->
