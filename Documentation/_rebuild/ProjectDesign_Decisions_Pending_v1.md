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
