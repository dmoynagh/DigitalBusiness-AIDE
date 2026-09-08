# AIDE Rebuild — WIP v24

> **Version 24** (2026-09-08). WIP split per rebuild guide F9 — settled content extracted to destination files; this document retains purpose, method, current position, open items and next actions.

**Location:** `AIDE/documentation/_rebuild/`
**Status:** Active working document. Archive when the rebuild completes.

---

## Contents

- **Purpose and scope** — why this document exists, what the rebuild is.
- **Method** — parallel rebuild through a filter, not in-place edit; the governing description.
- **Deployment** — parked; custom single-instance deploy.
- **Open questions** — parked, to resolve during the rebuild.
- **Next actions** — where to pick up.
- **Item 7 progress** — component naming: standing rules, purpose lines, candidates, open items.
- **Cross-session items** — Stage 0 deliverable, marketplace-add question, cross-component wiring, tool pipeline gate.
- **Item 8 progress** — per-component design review: the three-layer authoring model, Principles (masters output 2026-09-08), Project Design (design pass complete; pending content extracted to destination files).

---

## 1. Purpose and scope

Unchanged from v2. AIDE's substance is largely right; the corpus has drifted (bloat, buried
defining material, over-engineered deployment). The rebuild strips what doesn't serve a defined
outcome, refocuses what does, restructures so defining material sits at the top, and ensures every
part has a stated outcome, objective and definition of done.

Standing driver: the standards and behaviours that shape how AI works with you should be live in
your sessions, not just designed on paper. Everything else serves that.

---

## 2. Method

### 2a. Method restated — the governing description (2026-09-07)

**Stated by the director, and this is now the governing description of how the
rebuild runs.** It supersedes the process scaffolding that had accumulated on top
of it.

> Work through the whole rebuild design quickly. Review and confirm purpose,
> approaches, and that what a component does is clear and effective. Then look at
> the previous material and bring through only what has a purpose in the new
> design. Just because it was in the previous version does not mean it was
> purposely put there — it may have evolved in, and may not be important,
> impactful, or have a right to exist. That judgement is made against the
> confirmed new model.

**Two phases and one test.**

1. **Design review.** Confirm the component's purpose, objectives and methodology
   until it is clear and effective on its own terms. **This is the load-bearing
   phase and it is where the director's time goes.** The aim is a clean redesign
   with focus and purpose clear, delivered simply, well defined, easily
   maintained, and appropriate to the context and task it has to serve.
2. **Old material as source.** Read the old corpus against the confirmed intent
   and carry only what earns its place. **Claude runs this pass**, surfacing the
   carries and the genuine ambiguities rather than a list of judgements for the
   director.

**The test:** does this have a purpose in the new design? Presence in the old
version is not evidence.

**Sequencing rule, retained from the scaffolding it replaces:** confirm the new
model *before* reading the old material, never the reverse. The old corpus never
gets a default seat.

**Consequence, and a check on Claude.** A confirmed model answers most
old-material questions by itself. **If the old-material pass is producing a long
list of calls for the director, that is a signal the design review was not
finished** — not a sign the pass is going well.

**Counter-risk, stated once.** The failure mode of "the intent answers it" is
Claude deciding something serves the purpose when it is really Claude completing
a gap the design left. **Where an old item only earns its place under an
assumption the confirmed model does not actually state, that is a hole in the
design, not a carry** — it returns to phase 1. This pass had a live example: the
**build project** turned out to be defined nowhere, and it surfaced through old
material rather than through the forward pass.

---

## 6b. Deployment — parked

Deployment is over-engineered for current scale ("sledgehammer") — package-manager-grade machinery
for one person and two platforms; complexity compounded when delegated to AI.

- Will hand-write a **custom single-instance deploy**.
- Extensible/distributed model revisited only if a real need appears.
- **Placement deliberately deferred** — decide where it goes once we know what it does.
- **Stage 0 deliverable** scoped in a separate session (2026-09-03) — see §15b.

---

## 14. Open questions

Carried from v2: Q1 Brief/Considerations boundary (parked); Q2 container names — Working Practices
name collision (workflow map vs portable conduct conventions), one must be renamed; Q3 process
container split by mode (no for now); Q4 acceptance testing placement (deferred); Q5 AIDE containers
(confirmed by filter); Q6 built/deployed artefacts under documentation (open, case by case); Q7
Build-branch outcomes (not yet worked); Q8 Deployment and Principles survival as containers (open);
Q9 binder scope declaration form (open).

Added v8:
- Overview returns as a discussion — topic-or-corpus-scale TLDR is the case to test.
- Deployment placement deferred until its behaviour is known.
- Standard-length vs design-length Decisions variants both drafted; confirm which is canonical when
  the doctype set is built.
- Change management: the migration-format standard is not yet authored; the three-part task shape,
  the structured/prose form split, R23 (action fully describes the work) and R10 (preserve unrelated
  content) are hard inputs. Authoring waits for the doctype set, per the standing sequence. (§11a)
- References block: no longer blocked by Dependencies; decide on its own merits when a consumer
  appears. (§9)
- Does each remaining component have a stated one-line task? Needed before its contents can be
  filtered.

Added v10 (item 7 naming pass):
- §3–5 (lifecycle model, design half, AIDE scope and containers, structure vs transport) are not
  blockers for item 7; downgraded to documentation debt in Contents.
- "Component" confirmed as the single word for the ownership unit. The old
  Capabilities-internal usage (D43, D60, D92) is subsumed.
- Capabilities is a grouping label for now, not a component — revisited if it earns a purpose.
- Q8 (Deployment and Principles container survival) is partly addressed: Deployment is parked with
  a purpose line but deferred mechanism; Principles has a settled purpose line. Neither is closed —
  survival as containers depends on the full picture.
- Tags, Scope, Dependencies form a runtime-machinery cluster with a chain of risk: Dependencies
  shrank under §11a, Scope lost a consumer at CM-Q1, Tags depends on Scope. If Scope falls, Tags
  almost certainly falls with it. All three are candidates with survival open.
- Stage 0 deliverable scoped (2026-09-03 session) — see §15b.
- Open empirical question: whether a CLI-side marketplace-add tracks subsequent merged-PR releases
  automatically, or needs per-release manual action. (2026-09-05 session) — see §15b.

---

## 15. Next actions

1. Fold the two variant Decisions drafts into the rebuild corpus when the doctype set is authored.
2. Revise VersionCleanup for draft-state grouping and key validation.
3. Revise versioning documentation for the draft model.
4. Carry the migration-format standard (§11a) into the standards-authoring pass with the three-part
   task shape, the form split, R23 and R10 as hard inputs; land the R6 publish gate with the publish
   operation.
5. Block-catalogue filter — Tags and References remain parked pending their consuming components;
   Dependencies is closed (§9).
6. Then versioning session (version metadata, migration state, change summaries are all blocks).
7. Name the one-line task for each remaining component, then filter its contents
   against it. **Naming pass COMPLETE — see §15a.** Thirteen components have settled
   purpose lines. Three candidates have draft lines with survival open (Tags, Scope,
   Dependencies). Core is deferred by design. The Capabilities grouping question was
   worked 2026-09-07 and confirmed: it stays a container until a demonstrated need
   forces otherwise. The filter half of this item is folded into item 8.
8. Per-component design and purpose review — in chat, one component at a time. For
   each component: flesh out its purpose, check its approach and design against how
   we now work and what we've learned, confirm it is more than a migration gate, and
   get it into a state that can be properly implemented. This is a design review, not
   just a content filter, and is deliberately kept in chat rather than Claude Code.
   Run the documentation_old filter per component as part of this pass. **In
   progress — Principles reviewed 2026-09-07, see §15c.**
   - Component order: Principles (done, design only) → **Project Design → Standards**
     next, because they define the document types everything else is written in →
     then the remaining components. Standards also answers the authoring bar that
     Principles is waiting on.
   - Output as you go: once a component's design is complete, author its masters into
     the new system and add/update them in that component's binder. The binder is the
     single context-loaded artefact — update one binder, not many loose files. Keep
     outputs small and reviewable rather than one large pass at the end.
   - Standing step: each authored standard is reviewed by a separate AI before it is
     accepted.
9. Author the new corpus at deployable length.

---

## 15a. Item 7 progress — component naming

Working section. Records the standing rules, settled purpose lines, candidates,
new components surfaced, and open items from the item 7 naming pass (v9–v10,
voice sessions 2026-09-07).

### Unit and terminology

**Component** is the single word for the ownership unit — any unit that adds
or extends functionality. It applies at every level. The old
Capabilities-internal usage (D43 "seven top-level Capabilities components,"
D60, D92) is subsumed; the word now means the same thing everywhere.

**Capabilities** is an organisational grouping — a wrapper for components
that extend the development environment (standards, tools, etc.). It is not
itself a component unless it earns a purpose. Components inside the
Capabilities grouping are components in their own right; the grouping is
just filing.

### Standing rules

These govern the whole naming pass and downstream filter work.

1. **Owner is whoever knows the most about it.** Ownership goes to the
   component with the deepest knowledge of the thing. Applies to block types,
   document types, workflow artefacts, and boundary disputes.

2. **Documentation methodology owns structure and mechanics, not content
   definitions.** It defines how documents are built and how the document
   workflow runs. It does not hold a registry of document types belonging to
   other components. The only things that live in methodology are genuinely
   global — a type used across many components where no single component knows
   the most about it.

3. **Each component defines its own block types and document types.** Project
   Design defines objectives, requirements, considerations. Working Practices
   defines work-in-progress, work register. Standards defines what a standard
   is (provisionally in methodology — see open items). Being written down as a
   document does not make something methodology's business.

4. **A purpose line is a filter criterion, not a description.** Its job is to
   reject content. A good line carries an outcome, a consumer, and a visible
   edge. If it rejects nothing from the component's own current documents, it
   was written from the corpus rather than from need.

5. **Mode and interaction pattern are separate axes.** Mode is the
   contract — what role an external AI plays. Interaction pattern (one-shot,
   multi-round, conversational) is how many rounds it takes. Any mode can use
   any pattern. Adversarial/challenge is an approach or style applied to a
   mode, not a separate mode. Adjudication (resolving competing outputs) is a
   role within a workflow, not a separate mode.

6. **Purpose and role first; everything must align to it.** If a piece of
   content cannot trace back to the component's purpose, it is scope creep.
   This is the test that discharges item 7 into item 8 (filter).

7. **Orient before starting a task.** *(Added 2026-09-07 on the director's
   correction — he was spending significant time working out what was happening
   instead of focusing on decisions.)* Before any content, open a task like a
   sweep or a component review with four things, briefly: **what this activity
   is**, in plain language rather than by its label; **why now**, and what it
   unblocks; **the director's role** — which decisions he will actually be asked
   to make, and what Claude is doing without him; and **what done looks like** —
   what exists at the end that does not exist now. Half a screen, once. *If it
   cannot be written, that is the signal the task is not clear enough to start.*
   Two additions: when a task runs long, restate position before each batch; and
   **flag decision points as decision points at the moment they arrive**, not
   buried at the end of a list. Name only the frame in play — the director should
   not have to hold several at once.

8. **Reconcile against settled material before proposing.** *(Added 2026-09-07 on
   the director's correction, after three errors of the same kind in one
   session.)* Reading old material invites proposing something the forward design
   has already answered, because the old document is in front of Claude and the
   settled material is not. **Before proposing anything as a carry or a lift,
   check the forward design for the same ground first.** A technique the forward
   design already covers is *confirmation* or *contradiction* — never a lift.

### Settled purpose lines

| # | Component | Purpose line | Key boundaries / reject-test notes |
|---|---|---|---|
| 1 | Documentation methodology | Define how documents are structured and created — the generic mechanics. | Not a registry of doc types. Specific types live with whoever knows the most. Provisionally holds the definition of what a standard *is* (see open items). |
| 2 | Standards | Make sure standards are applied, honoured, and kept current across the environment. | Owns use, application, and migration of standards. Does NOT own the document-shape definition of a standard (provisionally methodology). |
| 3 | Migration | Bring a document into line with the current version of every standard it depends on, before it is used. | Rejects: Migration Tool content (migration is an AI task, not a script), wide corpus scan material, presence levels and exact pins. |
| 4 | Review | Give work an independent check by a separate reasoning path, so problems are caught before the work is trusted. | Doesn't own fixing or quality rules. Already has five Types (Check, Inspect, Evaluate, Robust, Stress Test) — the challenge/adversarial concept is covered by Robust and Stress Test as approach, not a separate mode. |
| 5 | Research | Get an answer to an open question by putting more than one AI on it and pooling what comes back, so the result is stronger than any single pass. | Convergent — pools toward one answer. Distinguished from parallel solutioning (which keeps answers apart). NEW component. |
| 6 | Parallel solutioning | Get two or more AIs to each produce their own design from the same brief, independently, so different approaches can be compared before committing. | Divergent — deliberately keeps approaches independent. Resolution (picking the winner) is a separate flexible role: human, lead AI, or both depending on automation level. NEW component. |
| 7 | Consultation | Bring an external AI in to discuss something you're working through — a single question or an evolving thread — so its input shapes your thinking. | Defined by the ownership test: primary actor retains ownership of the work; external AI advises without owning the outcome. Renamed from "contributory input." NEW component. |
| 8 | Messaging | Carry a message between AIs reliably — across sessions, platforms, or models — with a known envelope and confirmed receipt. | Owns the envelope and receipt. Does not own message content (sender's job) or route selection (platform transport). |
| 9 | Principles | Give any AI the durable, portable reasoning and interaction premises to think and act well — independent of platform or methodology. | Portability is the defining test. If a candidate principle only makes sense inside AIDE, it's not a principle — it's methodology or working practices. |
| 10 | Working practices | Own the workflows and behaviours for getting work done — including work-in-progress, work registers, and how design and build hand over — whatever the task. | Owns workflow artefacts end to end, definitions included. WIP and work register are NOT methodology's business. Divisional boundaries with project design and build to be resolved by "knows the most." |
| 11 | Project design | Produce a coherent specification for work of any size — one scalable architecture from simple single-document to complex multi-document structures. | Owns both ends of the design-build loop including the work register. WP, open items, decisions and knowledge stay generic. Defines its own block types and document types. |
| 12 | Build | Take defined work and execute it — produce the outcome, report what was done. | Generic core plus specialised paths by work type. Core-vs-path ownership boundary deferred for "knows the most." Handover loop goes to working practices. |
| 13 | Tools | Encapsulate a repeatable invokable action — anything you'd "run" rather than "follow" — so its mechanism and safety checks aren't re-derived each time. | Heart is the invocability test (D24, the standard-tool boundary): "if you would say 'run X,' X is a tool; if you would say 'follow the approach in Y,' that is a standard." NOT limited to executable code — migration is a tool and it's an AI task. |

### Candidates — survival open

These have draft purpose lines but their survival as standalone components is
unresolved. All sit in the runtime-machinery cluster. There is a chain of
risk: Dependencies shrank under §11a (the change-management model), Scope lost
a consumer at CM-Q1 (document-applicability answered by declaration), and Tags
depends on Scope. If Scope falls, Tags almost certainly falls with it.

| Candidate | Draft purpose line | Flag | Trigger to resolve |
|---|---|---|---|
| Tags | Attach machine-readable labels to items so they can be selected by query. | Highest risk — only demonstrated consumer is Scope's machine layer. Block already parked (§9). | Resolved when Scope resolves, or when another consumer demonstrates a need. |
| Scope | Decide whether a given standard, tool, or rule applies in the current situation, so the AI only follows what's relevant. | One of two consumers removed by CM-Q1 (declaration model). Remaining consumer is runtime applicability. | Work through what actually needs runtime applicability; the answer falls out. |
| Dependencies | Let a document declare which standards it depends on and at what version. | Moderate-to-strong risk of not being a component. §11a reduced it to one block, one field. | May resolve as a block owned by whoever owns change management, not a standalone component. |

### Deferred

| Component | Reason | Trigger |
|---|---|---|
| Core | Cannot be judged until everything else has declared what it needs. Core is defined by leftover shared requirements that have no natural home elsewhere. | Resolve last, after all other component purpose lines are settled. |
| AI Deployment | Parked (§6b). Purpose line settled: "Get the finished standards and behaviours live in a session, on whatever surface is in use." Mechanism deferred — will be hand-written, single-instance. | Revisit when mechanism is designed. |

### Capabilities grouping — worked 2026-09-07

Worked as the final item of the naming pass. Confirmed: Capabilities stays an
organisational wrapper, not a component. It earns no purpose line at this stage
because it does no work of its own — every job it could claim is already owned
by a component inside it. Kept provisional under the demonstrated-need rule: if
it later shows a purpose of its own, it graduates to a component then. No
container-tree or ownership consequences were decided in this pass.

### New component candidates — parked

| Candidate | Description | Status |
|---|---|---|
| Decomposed collaboration | Different AIs solve different parts of a larger problem, then results are assembled. | Real pattern. Parked — no demonstrated need for a solo developer. |

### Open items from this pass

1. **Standards definition placement.** Where the concept of a standard, and its
   document type, is defined — methodology or the standards component.
   Provisionally in methodology (it's a document-shape question; sits naturally
   beside other doc-type definitions). Leaning toward capabilities. Review once
   the full standards side is worked through.

2. **Divisional boundaries: project design / build / working practices.** The
   handover between these three has plausible ownership claims from each side.
   Parked for "knows the most" once all three are named and side by side.

3. **Build specialisation paths.** Where the boundary sits between build's
   generic core and each specialised path, and whether a given path is owned
   inside build or by the component that knows that output type.

4. **Consultation external review.** A prompt was sent to an external AI asking
   whether consultation is a coherent distinct mode or collapses into another.
   Response received and triaged:
   - **Accepted:** the ownership test (who owns the outcome) as the defining
     boundary; separating mode from interaction pattern.
   - **Accepted with caution:** three proposed new modes (decomposed
     collaboration, adversarial challenge, adjudication). Challenge is already
     covered by Review's Robust and Stress Test types. Adjudication is the
     resolution role already noted in parallel solutioning. Decomposed
     collaboration is parked as a genuine pattern without demonstrated need.
   - **Rejected:** the four-axis model (mode, topology, lifecycle, integration)
     — over-engineering.
   - **Accepted:** rename from "contributory input" to "consultation."

5. **Core's eventual scope.** The previous Core design material (index, domain
   resolution, bootstrap, platform) is held as reference, not commitment. When
   another component surfaces a shared requirement with no natural home, check
   it against what Core originally proposed. Consideration only.

---

## 15b. Cross-session items

Items from other sessions that belong in the WIP so it holds all current work.

### Stage 0 deliverable (scoped 2026-09-03)

Three artefacts:

1. **Always-on bundle** — Principles, Working Practices, human working model.
   Deployed to: claude.ai project instructions, user preferences, CLAUDE.md,
   ChatGPT project.
2. **One plugin with five skills** — Messaging (known-good control), Review,
   DocMethodology, Standards & Tools, currency probe.
3. **Written acceptance test.**

**Exclusions:** Tags, Scope, Dependencies, Migration (all pre-filter or
unresolved), the whole AI Deployment mechanism, the production chain, plugin
commands/agents/hooks/MCP.

**Naming constraint:** must not carry the AIDE_Core set identity or a release
number the real production chain will want.

### Marketplace-add empirical question (noted 2026-09-05)

Open question: whether a CLI-side `marketplace-add` tracks subsequent
merged-PR releases automatically, or needs per-release manual action. To be
tested empirically.

### Cross-component wiring (raised 2026-09-07)

How design, build, deployment and the other components are actually wired to each
other has never been reviewed as a whole. Three separate holes surfaced it during
the Project Design sweep: the build project being defined nowhere, the old corpus
deferring target definitions to "the domain", and the design-to-build linkage
only ever existing inside a transient work package. Belongs to no single
component; work before the rebuild completes.

### Tool pipeline gate — DISCHARGED (2026-09-07)

All deliverables committed and pushed by Claude-Code. See AIDE_Rebuild_SettledDecisions_v1 for the detail.

---

## 15c. Item 8 progress — per-component design review

Per-component design and purpose review (item 8). One component at a time, in
chat. Records what each pass settled and what remains before the component can
be signed off.

**Three-layer authoring model:** see AIDE_Rebuild_SettledDecisions_v1.md.

### Principles — design pass complete, masters output 2026-09-08

Design v4 and Decisions v4 authored fresh and deployed via the FileUpdatePackage
pipeline. Nine premises (P1–P9), the portability-as-universality defining test,
the Working Practices boundary, the Guidance Profiles move, and the
definition-of-done open item are all recorded in the masters. Verified against
the WIP detail before this trim — no knowledge lost.

**See:** Principles_Design_v4.md, Principles_Decisions_v4.md (in the Principles
master folder).

**Still open:** sign-off waits on the standard (needs the Standards component
defined) and cross-review by a separate AI. Definition of done as a candidate
premise reopens the element list once Working Practices completes its definition.

### Project Design — reviewed 2026-09-07 (design pass COMPLETE to the Standards block)

Design pass complete to the Standards block. All six requirements delivered.
Binder sweep complete end to end. Pending content extracted to destination
files per rebuild guide F9:

- **ProjectDesign_Design_Pending_v1.md** — the settled design elements: model,
  definitions, rules, mechanisms.
- **ProjectDesign_Decisions_Pending_v1.md** — reasoning, rejected alternatives,
  corrections, binder sweep narratives.
- **ProjectDesign_StandardInputs_Pending_v1.md** — items explicitly flagged for
  the Project Design standard.
- **ProjectDesign_WorkRegister_Pending_v1.md** — work owed and carried to other
  components.

**Stage 6** (design output and standards) remains, blocked on Standards.

**Open:** does the work register still admit confirmed non-design work?
