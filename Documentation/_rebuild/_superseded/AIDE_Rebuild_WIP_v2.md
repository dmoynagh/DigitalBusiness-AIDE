# AIDE Rebuild — WIP

> **Version 2** (2026-09-04). Adds: containers must state a purpose; the tree is an output of the
> filter, not an input; AIDE's own defining material sits at the root, not in a Core component;
> structure reflects meaning while transport is handled by generated binders; the payload /
> Infrastructure boundary; and the sweep-and-bind capability. Working document — does not conform
> to the full documentation methodology by design.

**Location:** `AIDE/documentation/_rebuild/`
**Status:** Active working document. Archive when the rebuild completes.

---

## Contents

- **Purpose and scope** — why this document exists, what the rebuild is.
- **Method** — parallel rebuild through a filter, not in-place edit.
- **The lifecycle model** — four modes, cross-cutting threads.
- **The design half** — brief, design, decisions; universal across project types.
- **AIDE scope and containers** — what AIDE is, the root, how containers earn their place.
- **Structure vs transport** — meaning drives the tree; binders carry documents into context.
- **Infrastructure** — machinery that acts on the corpus but is never loaded into the AI.
- **Documentation methodology base** — versioning, structure, sections, conciseness gate.
- **Standards, Tools and Guides** — the output types and their boundaries.
- **Document orientation** — contents, summary, overview; header/footer identity.
- **Filter rules** — the sieve for passing old material into the new structure.
- **Folder structure** — repo layout for the rebuild.
- **Open questions** — parked, to resolve during the rebuild.
- **Next actions** — where to pick up.

---

## 1. Purpose and scope

### Why the rebuild

AIDE's substance is largely right, but the corpus has drifted. Specific problems identified:

- **Bloat and clutter.** Documents are long, with significant fluff. Key defining material is
  buried rather than at the top.
- **Over-engineered deployment.** The deployment machinery became package-manager-grade for what
  is a one-person, two-platform setup. This was the part delegated to GPT on the assumption it was
  mechanical translation work; it wasn't, and it over-built.
- **Solution-led drift.** Parts of the corpus answer "how do we handle this" without a stated goal
  the answer serves.
- **No conciseness discipline.** Documents deployed as AI guidance consume context that should be
  available for the actual work.

### What the rebuild is

Not a rewrite from nothing. The thinking is nearly all there. The job is:

1. Strip what doesn't serve a defined outcome.
2. Refocus what does.
3. Restructure into a clear hierarchy so defining material sits at the top.
4. Ensure every part has a stated outcome, objective and definition of done.

**Target effort:** a fast rip-through, hours not weeks.

### Standing driver

The primary driver for AIDE, restated: **the standards and behaviours that shape how AI works with
you should be live in your sessions, not just designed on paper.** Everything else — production
chain, deployment machinery — exists to serve that. Anything that doesn't serve it is a candidate
for removal.

---

## 2. Method — parallel rebuild through a filter

**Decision: build parallel, don't modify in place.**

Reasoning: a live corpus carries its history in context and anchors every decision toward keeping
what's there. Modifying in place makes "stays" the default and puts the burden of proof backwards.
A parallel build flips it — nothing gets in unless it earns its place by serving a defined outcome.

This is consistent with the prior finding that most of the gain in recent work came from the
restart, not the platform: fresh restatement from curated source beats incremental evolution.

**Process:**

1. Establish the clean structure and the outcomes each part must hit. *(This session — largely done.)*
2. That structure becomes the filter/sieve.
3. Pass each piece of the existing corpus through it: **moves as-is** / **moves reshaped** /
   **left behind**.
4. The old corpus becomes a **source to mine, not a thing to edit**.

**Practical note:** don't do the *shaping* work inside a project loaded with the old corpus — its
presence in context anchors toward the additive. **Refined (v2):** that warning applies to shaping,
not to filtering. The filter pass needs the old material to hand, and needs adjacent documents
available so tangential references can be resolved. So the corpus may be loaded during filtering,
under a standing rule:

> **The old corpus is evidence, not authority. Nothing earns passage by existing. Question
> everything. Where the old structure and the stated outcomes disagree, the outcomes win.**

Much of the old corpus is redundant, bloated and without hierarchy. Treat it accordingly.

**Hybrid confirmed:** filter passes can be run with Claude or by the user directly, per document.

---

## 3. The lifecycle model — four modes

**Modes, not tool boundaries.** You may be in the same chat with the same AI; the mode is the
state of work you're in.

| Mode | What it is |
|---|---|
| **Design** | Defining what's to be made and how it will be approached. |
| **Build** | Creating it. |
| **Deploy** | Getting it live and active. |
| **Review** | Life-cycle: monitoring, assessing what to fix, expand, or do next. |

Review feeds back into Design. It's a loop, not a line.

### Why four and not more

Classic lifecycle models segment further (requirements / design / implementation / testing /
deployment / maintenance; or the DevOps loop: plan, code, build, test, release, deploy, operate,
monitor). Collapsed to genuine mode changes — points where the nature of the work actually shifts
— these land on the four above.

### Testing — decided

**Testing folds into Build, as its exit gate.** Not a separate mode.

- Mechanically, building and testing are one loop; splitting them implies a handoff that doesn't
  exist.
- But **build is not complete until the thing is made *and proven*.** Passing verification is the
  definition of done for build, and the gate before deploy.

**Noted, not yet built:** there are two flavours of testing — technical (unit, build) which clearly
sits inside build, and acceptance testing against requirements, which sits closer to the deploy
boundary and may vary by deliverable type. We know it exists and roughly where it sits. **Do not
invent the stage before it's needed** — define it further when the methodology work forces the
question.

### Cross-cutting threads

Two things run through *all* modes rather than being modes themselves:

- **Documentation.** Every mode produces and consumes chunks of information needing a home.
  Design → brief, design, decisions. Build → outcomes and records. Deploy → state (what's actually
  live). Review → findings and identified needs.
- **Verification.** Not just build testing. Each mode has its own verification gate: build's is
  testing; deploy's is confirming the thing is actually live and active.

### The fork

The **design half is universal** — brief, design and decisions work the same whether you're
designing a document, a process, a graphic design piece, a building, or software. Definition has
the same shape regardless of the thing.

**At the design/build boundary, the path forks by deliverable type.** Building software has a
different execution shape from producing a document. Generic becomes specific at the handoff.

**Two build branches identified so far:**

1. **Software development** — the general capability to build things.
2. **AIDE extensions** — the standards, capabilities and deployment into the AI environment.

These are intertwined: you need (2) to properly deliver (1), and (2) is itself built using the
same design-and-build model. It's self-hosting — if the model is good, you feel it immediately.

**Branch (2) is the most defined and the current priority** — it's where the over-engineering is,
and where clear outcomes will do the most to stop the behemoth.

---

## 4. The design half — the information chunks

These are **chunks of information that need to reside somewhere**, not documents. How they get
stored and organised into documents is arbitrary and can vary.

### The Brief — the target

Three parts:

- **Objective** — what are we doing, what's the driver, the reason, the goal, the end outcome,
  who's it for.
- **Requirements** — must do this, must deliver that, has to achieve this, needs to factor in
  that. The non-negotiables.
- **Considerations** — not hard requirements, but must be factored in. E.g. a neighbouring
  component it should work well with, allowance for extension into an area, a known hard spot or
  issue to design around.

**Priority runs through all of it:** musts vs would-likes.

### The Design — the current snapshot

The confirmed model of what's to be made. Present tense. Clean.

### Decisions — the reasoning record

**Scope:** *all* thinking, not just design decisions. Why this objective, why that requirement is
framed as it is, why a consideration matters — the reasoning behind the whole target, not only the
solution.

**Boundary with the other documents:** Brief and Design carry only the **live why** — the
reasoning that explains the *current* state. The moment reasoning becomes historical (how you
arrived here, what you considered and moved past), it belongs in Decisions.

**Outcome test for Decisions (the definition of done):**

> If you lost the Brief and the Design tomorrow, Decisions should hold enough thinking that you
> could **reconstruct them without redoing the intellectual work.**

That test tells you what belongs in it: if a piece of thinking would be needed to justify or
rebuild a current position, it goes in. If not, it's noise.

**Second function — the two-way guard:**

- Prevents accidentally reintroducing something already thought through and rejected, because the
  rejection and its reasoning are present.
- **But keeps rejections reversible on purpose.** Because the *why* of a rejection is retained,
  it can be genuinely reassessed when new information means the original reason no longer holds.
  A rejected option isn't dead — it's parked with its reasoning intact.

### The line

Brief / Design / Decisions = **knowing**. Everything after = **doing**. That's the design/build seam.

---

## 5. Methodology validity — is this the right thing to target?

Question raised: is a cohesive-document methodology the right target, given modern agile/RAD
practice favours log-format, sequential, fragmentary documentation (ADRs, changelogs, tickets)?

**Position reached: yes, and it isn't a regression.**

Agile went fragmentary not because sequential logs are better, but because **keeping cohesive
living documents in sync by hand was too expensive.** People stopped paying that cost and framed
it as a philosophy.

**AI removes the cost that forced the compromise.** If you can describe a change and have it
written into the right place in a cohesive document, the original reason for going fragmentary
largely disappears. This is taking the good part of the old way — coherent living documents —
without the maintenance burden that killed it.

**It also avoids the waterfall trap:** no screens of documentation before work starts. The brief is
lightweight, and material gets written in as it emerges.

**The caveat that makes or breaks it:** the value is the living document *staying coherent*. The
methodology must make continuous reconciliation nearly free, or people quietly drift back to logs.

### Three risks to design against

1. **The reconciliation trap.** New information often touches three or four places at once — a
   decision that changes a requirement that changes a consideration. If updating one leaves the
   others stale, you've recreated the drift. **Rule needed: a chunk gets reconciled everywhere it
   lands, not just filed once.** (Consistent with verification being the corpus's biggest gap.)
2. **Loss of the settled/moving boundary.** In a log you see sequence. In a cohesive document,
   history flattens and everything reads as equally current — you lose how you got here and why
   something was rejected. **This is why Decisions sits beside Design rather than inside it.**
3. **No home for the not-yet-placed.** Material described mid-flow can't always be perfectly filed
   instantly. There must be a legitimate holding place (**WIP**) so things aren't lost or forced
   into the wrong box prematurely.

---

## 6. AIDE — scope and containers

**AIDE = AI Development Environment.** A **container** — the umbrella for anything that supports
doing software development in an AI-based environment. Not one thing; the home for a set of
supporting facilities.

Naming AIDE as the umbrella was the single biggest structural win of the recent work. The old
system had no top of the tree, so every new concern had to become an awkward sub-topic of a peer —
that's what bred the confusion.

### How containers earn their place — decided (v2)

**A container earns its existence the same way a document does: it must state what it is for.**
Without a stated purpose it is just a box things got dumped in because they needed somewhere to go.
That is exactly how the old corpus grew *Core* — a home of last resort, not a coherent concern.

Two consequences:

1. **The purpose statement is the filter for the contents.** Material sits in a container if it
   serves that container's stated purpose; if it doesn't, it belongs elsewhere or nowhere.
2. **The tree is an output of the filter, not an input.** Containers exist because surviving
   content needs grouping, and you cannot know the right grouping until you know what survives.
   Do not settle the tree in advance; let it crystallise from the work.

**Flat until an umbrella pays for itself.** Nesting for its own sake recreates the bloat one level
up. Considered and rejected this session: placing Project Design under Working Practices. It would
have pulled Build, Deploy and Review guidance in behind it and made Working Practices a second
home-of-last-resort. If, during the work, two areas turn out to share rules that want stating once,
*that shared thing* is the umbrella — and it will have a real purpose rather than "these felt
related."

### The root — AIDE's own defining material

AIDE is a thing being designed, so it has a brief like anything else. Its objective, requirements
and purpose are authored under the same design half and the same documentation methodology
everything else uses. **This is self-hosting: if the design half can't express AIDE's own brief,
the design half isn't good enough yet.**

**That material sits at the root of the tree, not in a component.** It is not a peer of the
containers below; it is the parent statement of purpose each of them is judged against. The old
corpus's *Core* was reached for as the home for this kind of material, but Core was a grab-bag. The
root is not: it holds exactly one thing — the definition of the whole environment. Anything more
specific drops into its proper container. The genuinely foundational parts of old Core come up to
the root; the rest scatter or don't survive.

### Provisional container set

**Held loosely. Names and membership to be confirmed by the filter, not before it.**

| Container | Purpose |
|---|---|
| **Documentation** | Managing documents in the environment — creating, managing and maintaining them. Consumed by everything else. |
| **Capabilities** | Extending the environment — adding functionality, guidance or behaviour that is **loaded into the AI**. |
| **Working Practices** | Defining how we work — the workflow, behaviour and process followed for a piece of work. |
| **Project Design** | Supporting the design half — brief, design and decisions; what they are and how they relate. |
| **Infrastructure** | Machinery that acts on the corpus to support the work but is **never loaded into the AI**. See §6a. |

**Not yet resolved:** whether **Deployment** and **Principles** survive as containers. Deployment
serves the standing driver directly, so a concern by that name almost certainly persists; whether it
is its own container or distributes across Capabilities and Infrastructure is open. Principles
(portable base reasoning guidance) is cheap and portable and probably worth keeping, but needs a
stated outcome or it doesn't move.

**Mode vs component — resolved.** *Design* is the mode (a state of work). *Project Design* is the
component providing process guidance for that mode. Two different things; the naming wobble came
from wanting one name to do both jobs.

**Structural implication:** if Project Design is the process guidance for Design mode, it's a
sibling of whatever guides Build, Deploy and Review. The Process component may naturally split by
mode, giving every mode a home for its guidance. *Hold lightly — don't lock until the skim is done.*

### The provider/consumer pattern

**Documentation Methodology is a provider. Every mode component is a consumer.**

- Documentation Methodology provides **document capability** — it doesn't know or care that it's
  making a brief.
- Project Design consumes it to produce Brief / Design / Decisions.
- Build will consume it for outcome records; Deploy for state records; Review for findings.

**Ownership rule:** the owner should be **whatever knows the most about the thing.**

**The boundary:** Project Design owns **meaning and role** (what a brief is for, what belongs in
decisions and why). Documentation Methodology owns **mechanics** (naming, versioning, storage,
lifecycle, structure).

**Documentation Methodology is a standard, not a store.** Not a central repository — a common set
of principles and functionality anyone applies in their own context. It gives the universal grammar
of documents; each consumer speaks its own dialect on top, specialising for its own document types
and information needs.

This is the generic-separated-from-specific pattern: the generic capability lives once, and
specialisation layers on per consumer without dragging context-specific material back into the core.

---

## 6a. Infrastructure — the payload boundary

**Discovered this session, from the work rather than imposed.** There is a real line between:

- **Payload** — Standards, Tools and guidance that get **loaded into the AI environment** to shape
  how it behaves. This is Capabilities.
- **Infrastructure** — machinery that **acts on the corpus** to support the work and is never
  loaded into an AI session. Build-time and workshop equipment.

The name matters: *Tools* is already load-bearing in the invocability test (§8), so reusing it here
would blur a distinction worth keeping sharp. **Infrastructure** carries the right sense — the
thing underneath that makes everything run without being the thing on show.

**Purpose statement (the filter for its contents):** *things that act on the corpus and support the
work, but are never loaded into the AI environment.*

---

## 6b. Structure vs transport

**Much of the old corpus's structure was designed for transport, not meaning.** Flat directories
and careful folder contents were shaped by the cost of manually syncing documents in and out of
context — you cannot drag in a folder that contains material you don't want. Structure served the
tooling's limitations rather than the architecture.

**This is a distortion to discard, not carry forward.** It is exactly what filter rule 2
(solution-led without a stated goal) exists to catch: structure serving a mechanism rather than an
outcome.

> **Requirement: structure reflects meaning. Assembly and delivery are a separate, solved problem,
> handled by generated binders and packages — not by hand.**

The hierarchy can be as deep and as meaningful as it needs to be, because nobody hand-syncs
folders. A binder gathers the right documents regardless of where they physically sit.

### The sweep-and-bind capability — Infrastructure's first inhabitant

Needed immediately: the problem lands as soon as the first file is saved. Three distinct named
things:

| Thing | What it is |
|---|---|
| **Binder definition** | **Authored.** Declares the binder's scope — a whole tree, a named set, or a tree with exclusions. The authority. A document type, so its structure and lifecycle belong to Documentation. |
| **Sweep** | **The tool.** Runs over a nominated tree after a commit. Invokable — "run the sweep." |
| **Binder** | **Generated output.** Disposable. Never hand-edited: change the definition or the source documents and re-run. |

**Sweep procedure (sketch, not yet a design):**

1. **Supersede** — where a newer version of a document is present, move the older into an
   `_superseded` subfolder, so the live tree holds only current documents.
2. **Resolve** — read the binder definition against the current state of the tree.
3. **Assemble** — produce the binder as a single file: the stale one comes out of context, the
   fresh one goes in.

**Hard boundary: the sweep assembles; it does not deploy.** Making a binder live in a session is
the delivery-and-verification concern. Keeping this line stops the sweep sprawling into the
behemoth pattern that afflicted the old deployment machinery.

**Next step is the brief, not the build** — objective, requirements, considerations, definition of
done — authored under the design half like anything else.

---

## 7. Documentation Methodology — the base

### Versioning

**Outcomes it must deliver:**

- See at a glance what version a document is, **without opening it**.
- Verify the right version is in place in distributed, non-real-time environments.
- History and rollback.
- Anything knows what version it's on. Work, work, work, then **commit → version increments**.

**Refinement:** git already provides history and rollback underneath. The **visible** version number
is really doing the *at-a-glance currency* job — the thing a filesystem or plugin can't show you.
So: keep visible versioning for currency signalling; let the repository carry deep history, rather
than duplicating that work by hand.

**Standing instruction:** where an outcome can be achieved by a better means than the mechanism
proposed, recommend it. This applies to everything in the rebuild, not just versioning.

### Document structure

A document has:

- **Title**
- **DocType** — the anchor. Associates the document with the standard defining its purpose and
  use, so anyone can ask *what is this* and *where are the rules for it* and get an answer.
- **Sections** — the building blocks.

**Sections:**

- Some are defined **inside a DocType** and apply only there.
- Others are **defined once and reusable** across DocTypes by context.
- A section's definition can be **tight** (rigid data structure, e.g. YAML) or **loose** (just a
  container for *this kind of information*), chosen by how much rigidity that section actually
  needs.

**Why loose is valuable:** it supports the value judgment — *I have this information, where does it
most likely go?* and *I want this information, where should I look?* That's the core navigational
outcome.

### Expansion and contraction

Documents expand or contract by volume. A Brief may hold objective, requirements and considerations
inline on a small project; on a large one, requirements and considerations split off into their own
DocTypes. **Same meaning, different physical shape.**

**Principle: documentation must facilitate, not inhibit, control, or be draconian.**

### Conciseness — a hard gate

**This is the property the current corpus most fails.**

Documents deployed as AI guidance compete for context with the actual work. If guidance consumes
half the available room, the system defeats itself.

**Outcome test:** does a consumer get exactly what's needed to implement the intended logic, in the
simplest, most concise, applicable form, **with the least consumption of tokens and context?**
Brevity **without compromising the *what***.

**Made a testable definition of done:** a standard is not done until it passes.

> **If a sentence can be removed without losing a required instruction or definition, it wasn't
> done.**

**Critically: author at deployable length in the first place.** Do not write long and then try to
compress. This was previously identified as the single most valuable action available.

---

## 8. Standards, Tools and Guides

These belong to **Capabilities**, not Documentation Methodology. Documentation Methodology is
concerned with document structure and management; **how behaviour or functionality is translated
into the AI environment** is a different concern.

Two production methodologies exist and both are sound.

### Standard vs Tool — the existing definition (retain)

**The test is invocability.**

- If you'd say **"run X"** → X is a **Tool**.
- If you'd say **"follow the approach in section Y"** → that's a **Standard**.

A Standard may *describe* a procedure; it may not *define an invokable action*.

**Sibling outputs from one design.** A single design describes a body of behaviour. Its outputs are
whatever implements that behaviour — one or more Standards, one or more Tools, siblings from a
common source. Neither authors the other's content; both derive from the same design and therefore
**cannot disagree**.

**Staging is legitimate:** a Standard may describe a procedure that *should* be a tool but isn't
yet. That's a staging post, not a defect. When the tool is built, the Standard's procedure section
is replaced by a pointer.

**Rationale:** a named invokable thing must be a Tool because only a Tool carries the identity,
versioning and publishing machinery that keeps a named thing honest. A Standard restating an action
creates two authorities with no synchronisation.

### Standard vs Guide — retain and sharpen

- **Standard** — terse, prescriptive, precise. "Almost like a legal document." Machine-referenced.
- **Guide** — optional, discursive companion. The *why and how* rather than the *what*. Embellished,
  giving a human (or a machine needing extra reasoning) a rounded, qualified picture.

**Both generate from the same design**, so they cannot drift.

**Sharpening added this session:** if the Guide's understanding *can't be inferred from* the
Standard, that's a signal the Standard wasn't designed as well as it could be. The Guide should add
richness, not supply missing meaning.

*(Note: the Specification document type was previously dropped — it sat between Standard and Design
with no clear reason to exist. The Standard holds that ground.)*

---

## 9. Document orientation — purpose-driven structure

**Documents must have purpose: human use or machine use** (often both). Structure should serve the
reader's decision, not just the author's sequence.

**The core outcome:** a reader — human or machine — should be able to decide **"is this the right
document for my task?"** and **"where in it will I find what I want?"** *without a full document
traverse.*

### The layers (already present in the corpus — lift and tighten)

**Identity — header or footer.** DocType and identity go at the very start or very end. These are
the only two reliably cheap points to read for both humans and machines.

**Contents — near the top.** Answers *what significant information is in this document and where?*
A **compact curated semantic map**, not an exhaustive repetition of headings. Describes information
rather than repeating headings. Uses stable headings or numbered-section locators, not line numbers.

Enables: quick scan → *relevant or not?* → discard, or load only the needed part. Second-order
searching.

**Summary — after Contents.** Answers *what does this document establish at a high level?* Faithful
representation of objective, model/approach, key logic, boundaries and outcome. **Not independent
authority** — the body governs where precision is needed; material inconsistency is a defect.

**Overview — an independent optional DocType.** For a substantial human-facing high-level snapshot
warranting its own document.

### Applicability

Value-based and dual-audience. Include only where they materially improve orientation,
comprehension, discovery, search or selective loading — **not for consistency**. Standards
generally don't need Summary; they're not designed for that. Small or immediately scannable
documents may omit.

**Each DocType owner defines** whether they apply, their role, scope and expected depth.

---

## 10. Filter rules — the sieve

Apply to every piece of existing material:

1. **Does it serve a defined outcome?** If no defined outcome exists for it, it doesn't move.
2. **Is it solution-led without a stated goal?** Redirect to the outcome, or drop.
3. **Is it proportionate?** One person, two platforms. Package-manager-grade machinery for that
   scale is over-build.
4. **Does it pass the conciseness gate?** Every sentence carries a required instruction or
   definition, or it goes.
5. **Is it in the right place in the hierarchy?** Defining elements up top; supporting detail below.
6. **Is it in the right home?** Owner = whoever knows the most. Generic capability lives once;
   specialisation layers on.
7. **Live why or historical why?** Live why stays with the current document; historical why goes to
   Decisions.
8. **Does it have an outcome, objective and definition of done?** If not, define one or drop it.

**Disposition for each item: moves as-is / moves reshaped / left behind.**

---

## 11. Folder structure

```text
AIDE/                          (repo — digital business)
└── documentation/             all AIDE documentation: how it works, build outcomes
    ├── _rebuild/              this rebuild's working documents; archive when complete
    └── ...                    the new, clean structure
    
documentation_old/             the previous corpus — SOURCE TO MINE, not to edit
```

**Conventions for `_rebuild`:**

- Leading underscore marks it as a management/workflow folder, visually distinct from substantive
  content.
- **Documents here need not conform to the full specification** — they're transitional scaffolding,
  not the building. Holding them to the final standard would be pointless friction.
- **But use simple visible versioning** so currency is readable at a glance as documents move around.
- **Consolidation:** where multiple rebuild documents exist, be able to gather them into a single
  file for adding to context and moving around. (The binder concept applied pragmatically.)

**Open:** whether built/deployed artefacts live under `documentation/` or elsewhere — decide case
by case.

---

## 12. Open questions

| # | Question | Status |
|---|---|---|
| Q1 | Is the Brief purely the target/problem space with no solution in it, or can early solution leanings live in Considerations? | **Parked** — decide once the fuller shape is on the table. |
| Q2 | Are the container names right? | **Reframed (v2)** — names emerge from the filter, not ahead of it. Note a live collision: *Working Practices* means the workflow map in this document but portable conduct conventions in the old corpus. One of the two needs renaming. |
| Q3 | Does the Process container split by mode (Design, Build, Deploy, Review as siblings)? | **Reframed (v2)** — was "leaning yes"; now held at **no for now**. Split only where there is real content. Design has it; Deploy's content is mostly machinery, Review's is mostly a capability. Four-way symmetry would manufacture containers to complete a pattern. |
| Q4 | Where does acceptance testing (vs unit/build testing) formally sit? | **Deferred deliberately** — don't invent the stage before needed. Varies by deliverable type. |
| Q5 | What are the AIDE containers? | **Reframed (v2)** — provisional set recorded in §6; confirmed by the filter, not before it. |
| Q6 | Do built/deployed artefacts live under `documentation/` or elsewhere? | **Open** — case by case. |
| Q7 | What are the Build-branch outcomes (both branches)? | **Not yet worked** — next major piece. |
| Q8 | Do Deployment and Principles survive as containers, and with what stated purpose? | **Open (v2)** — see §6. |
| Q9 | How does a binder definition declare scope — tree, named set, or tree-with-exclusions? | **Open (v2)** — resolve in the sweep-and-bind brief. |

---

## 13. Next actions

**Reordered in v2.** The component skim is no longer a precursor step — the tree is an output of the
filter, so it settles through the work rather than before it.

1. **Place this document** in `AIDE/documentation/_rebuild/`.
2. **Write the sweep-and-bind brief** — objective, requirements, considerations, definition of done.
   Needed immediately (it bites on the first saved file) and doubles as the first real test of the
   design half on live work.
3. **Draft AIDE's own root brief** — the parent purpose every container is judged against.
4. **Define Build-branch outcomes** — starting with the AIDE-extensions branch (most defined, most
   over-engineered).
5. **Run the filter** over `documentation_old`, document by document, recording disposition. Let the
   containers crystallise as material finds its home.
6. **Author the new corpus at deployable length** — not write-then-compress.

---

## Appendix — outcome statement drafted for the AIDE-extensions build branch

*Drafted this session, not yet confirmed. Included as a starting point.*

**Objective.** Take a confirmed AIDE capability and make it genuinely live and effective in the AI
sessions where it's needed, so the standards and behaviours actually shape how the AI works, rather
than existing only on paper.

**Requirements (musts).**

- Get the capability's content **actually active** in a session, not merely present.
- Work across the surfaces actually in use.
- Allow **trust that what should be active is active** — the verification gap.
- Allow new capabilities to be added without redesigning the framework each time.

**Considerations.**

- Stay proportionate to real scale: one person, a couple of platforms.
- Allow for future growth without building that machinery now.
- Lean on delivery mechanisms that already exist (e.g. plugins) rather than inventing carriers.

**Definition of done.** A capability is delivered when its behaviour is **observably active in a
live session**, and that can be **confirmed rather than assumed**.

---

*End of WIP v2.*
