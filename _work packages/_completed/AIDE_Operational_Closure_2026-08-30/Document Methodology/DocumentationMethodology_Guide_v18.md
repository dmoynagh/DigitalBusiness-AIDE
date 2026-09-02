# Documentation & Workflow Methodology — Guide

> **Identity:** `AIDE_DocumentationMethodology@v18`
> **v18** (2026-08-30). Reconciles document structure with AIDE Identity, Tags, Dependencies and
> Migration; introduces extensible metadata/state containers; moves WorkPackage execution semantics
> to `AIDE_WorkPackage`; and replaces the special `Methodology: vN` footer with generic dependency
> conformance.
>
> **Migration posture:** OnUpdate. Existing v17 documents remain readable; apply the v18 document
> transition when they are next modified/saved. An operation requiring v18-only metadata/state may
> explicitly require prior migration.
>
> v17 remains the historical predecessor. The document-type/lifecycle model is otherwise retained
> unless this release states a replacement.


---

## v18 change summary

- **Document conformance is a dependency.** `Methodology: vN` is retired. Governed documents
  declare their saved/proven Documentation Methodology conformance through `Dependencies:`.
- **Metadata containers are extensible hosts.** Header metadata, temporary state and footer metadata
  have fixed placement; Identity, Tags, Dependencies and future owners retain their own semantics.
- **Temporary operational state is generic and owner-labelled.** DocMeth owns placement/coexistence,
  not the state meaning or lifecycle.
- **WorkPackage execution semantics move to `AIDE_WorkPackage@v1`.** DocMeth retains only the
  document-type/naming/archive behaviour specific to WorkPackage files.
- **Machine-generated metadata stays compact** in human-readable documents.
- All other v17 rules remain in force unless explicitly superseded below.

## Summary

These rules carry most of this document. Everything else is detail. **No count is stated** — a
count is a second thing to keep true, and §4's list carries the scar from having one.

1. **One authoritative answer per question.** No document restates what another states; it
   references it.
2. **Route by kind, not by convenience.** Guide = the published rule. Design = the confirmed
   internal position. Decisions = the journey to it. OpenItems = what is in flight. Index =
   what exists.
3. **Naming is legible; the Index is authoritative.** A filename says what a document is; the
   Index resolves it.
4. **Nothing travels unless its type is cleared to travel.**
5. **A document is as short as its function permits, conclusion first.**
6. **A confirmed change is applied or registered — never neither.**
7. **A version counts outputs, not edits — and confirmed material is never left unwritten.**
   §16 remains the output discipline; document conformance/version transitions use Dependencies + Migration.

## 1. Scope and the ownership boundary

**This methodology owns naming, structure and lifecycle.** The originating project owns
creation, authoring and use — who writes a document, when, against what trigger, and what good
content looks like.

Carve-out: **topic naming convention is owned here; topic choice is the project's.** Which
topics exist inside a container and what they are called is the project's. How a topic name
renders in a filename, and what structure a topic segment may carry, is this methodology's.

Where a project needs a variation, the Index's local configuration section (§8) is the declared
mechanism for recording it. A project manages only its own document set: an observation
affecting another project is proposed, never enacted directly.

## 2. Core working style

- **Nothing goes into documentation until confirmed.** Discuss and draft first — in
  conversation, or in a Working doc for larger changes.
- **Feed living documents as pieces confirm**, not only once a topic fully resolves.
- **One decision at a time.**
- **Capture during, assemble after.** Where a decision involves real back-and-forth — a
  proposal revised after pushback, a distinction drawn mid-discussion, a tradeoff knowingly
  accepted — the working is recorded as it happens, in the Working doc or the Working section
  of a condensed topic doc. The Decisions entry is assembled from that record, not from
  recollection. A small, uncontested decision needs no Working doc.
- **Rejected alternatives are recorded, not discarded.**
- **Push back on complexity.** Check whether an existing mechanism covers a need before adding
  one.
- **A cross-project transmission substantial enough to need a stated addressee or an expected
  response is a Message** (§4f). An ad hoc, one-off observation stays informal.

## 3. Naming convention

```
{Project}_{Topic}_{DocType}[_{Key}]_v{N}.md
```

- **`{Project}`** — short project prefix. Omitted entirely for standalone items outside any
  project.
- **`{Topic}`** — the subject. Omitted for project-wide registers (Decisions, Index, OpenItems,
  Work Register). A project's shared entity/state model is a reserved topic name (`Domain`,
  `CoreModel`), not a document type.
- **`{DocType}`** — one of the established types (§4), or a declared custom type (§4h).
  `Message` is the one deliberate exception to this slot order (§4f).
- **`{Key}`** — present only on types that are inherently point-in-time (Review, WorkPackage,
  archived Working). Either a date-sequence `{YYYY-MM-DD}-{N}` or a **descriptive key**;
  see §3b.
- **`_v{N}`** — the version suffix, always last. It counts outputs, not edits: see §16.

### 3a. Topic structure

**A topic segment may be compound** — several underscore-joined parts — expressing either of
two relationships:

- **Instantiation** — siblings that are versions of one thing (`Platform_Claude`,
  `Platform_OpenAI`).
- **Subdivision** — a child that is part of its parent's subject (`Workflow_DesignSide`).

**Topics nest to any depth. No fixed tier count.** Depth beyond about three parts is a signal
the branch may warrant its own Index (§8b), not a rule violation.

**Topic and type resolve against the Index**, which holds the topic set and its hierarchy. A
filename is legible but not authoritative: right-to-left matching against the established type
list is a fallback for a reader without the Index to hand, and it does not survive custom types
(§4h).

**A cross-reference takes one of two forms, and the form carries the meaning:**

- **`abc_Design_v5`** — fully version-qualified. The reference is deliberately tied to that
  version, and means that version specifically.
- **`abc_Design`** — unqualified. Resolves to whatever version is current.

Neither is a default the other departs from. The author chooses by whether the tie is real. A
reader can then tell which they are looking at without knowing why it was written — which is the
property that was missing when the version suffix was merely optional.

**Dropping the last part of a compound topic** means "whichever instance applies." Filenames on
disk are always fully specified.

### 3b. The point-in-time key

**A date-sequence and a label, not a choice between them.** They answer different questions —
*when* and *about what* — and a slot that takes one or the other forces a document to drop the
answer it has.

- **Order: date first, then label.** `CMS_FullDesign_Review_2026-07-22-1_ContractSplit_v1.md`.
  A topic's Reviews then sort chronologically in a plain directory listing, which is what the
  date is for; label-first loses that as soon as the labels vary.
- **Date-sequence** is `{YYYY-MM-DD}-{N}`; `{N}` disambiguates same-day instances and is not a
  revision counter.
- **Each segment is a single segment with no underscores** — underscores are the topic-nesting
  separator.

**Per type:**

- **`Review`** — date **mandatory**, label optional. A Review is a snapshot and its date is what
  identifies it.
- **`Working`** — **no key in the normal case** (§4-w). A label is available where two Working
  docs are live on one topic at once. A date is permitted and not normally added, because
  archival supplies one through the rename.
- **`WorkPackage`** — date mandatory, as the day it opened; its `WorkPackage_Outcome` shares it.

**This supersedes the earlier either/or form.** A document already carrying a label alone is
renamed at migration; a rename is not a content change and the version does not move.

**Archive mechanics are unchanged:** `_Archived_{date}` slots immediately after the DocType,
before the document's own pre-existing key —
`Workflow_Review_Archived_2026-09-01_2026-08-14-1_ContractSplit_v1.md`.

### 3c. Document metadata containers and conformance

A governed document uses three possible machine-facing regions around the human-readable body:

```text
Title
Header metadata container
Temporary state container (only while state exists)
Body
Footer metadata container
Internal section (where applicable)
```

The containers are **extensible hosts**. Documentation Methodology owns placement, coexistence and
general compact rendering. The owner of a property/state entry owns its meaning, generation,
validation and lifecycle.

#### Header metadata

Placed immediately after the title/version preamble where present. Known consumers include Core
Identity:

```text
Identity: primary-id@v2, alternate-id@v7
```

This list is not closed. Formal identity is not inferred from filename.

#### Temporary state

Optional and placed after header metadata, before normal body content, because unresolved
operational state may affect safe use/update.

Compact owner-labelled form:

```text
State: Migration [AIDE_Migration] — v11 failed while targeting v12: source metadata unavailable.
```

Each entry has a stable owner identity, short title/name and concise current message. The owner may
create/update/remove only its own entry. DocMeth does not define the state semantics.

#### Footer metadata

Placed after body content and before the Internal section where one exists.

Known examples:

```text
Tags: design, doctype:[design]
Dependencies: !AIDE_DocumentationMethodology@v18, abc_Design@v5
References: pqr_Reference_v8
Type: Playbook — custom. Defined in ThisProject_Index.
```

- `Tags:` content/behaviour belongs to `AIDE_Tags`.
- `Dependencies:` content/identity/version/conformance behaviour belongs to `AIDE_Dependencies`.
- Migration consequences of a version gap belong to `AIDE_Migration`.
- `References:` remains a document-methodology citation relationship with no conformance
  obligation.
- Custom-type definition/pointer rendering remains a DocMeth concern.

**Document methodology conformance is no longer a special footer line.** A governed document that
depends on this methodology records the version against which it was last saved/proven conformant
through the normal Dependencies contract, normally:

```text
Dependencies: !AIDE_DocumentationMethodology@v18
```

The exact presence marker is governed by `AIDE_Dependencies`; this Guide does not redefine it.

A newer Documentation Methodology release does not by itself rewrite every document. `AIDE_Migration`
determines whether a declared transition is Required, OnUpdate or None, and the dependency checkpoint
advances only with a saved/proven document state.

#### Compactness

Metadata, derived state and other machine-generated content in human-readable documents should be
as compact as practicable while remaining unambiguous and machine-usable. Rich diagnostics belong
in the active work/result record unless durable document context requires them.


## 4. Document types

**The model, before the list.** Types are not peers. Four roles, in one direction:

```
Brief  ──▶  Design  ──▶  outcomes
              ▲
          Decisions
```

- **`Brief` defines** — the objective, the scope, the requirements. What is to be achieved.
- **`Design` determines delivery** — how the Brief's objective gets met. The confirmed position
  at a point in time.
- **`Decisions` informs the Design** — the history, the path, what was tried and set aside, so
  the next change to the Design is made with the evolution visible rather than from the snapshot
  alone. Its role is to produce good Design, and it feeds nothing else.
- **Outcomes deliver** — `Guide`, `Reference`, `WorkPackage`, a skill, an asset, a code build.
  Produced from the Design, they are what actually serves the topic's goals.

`Working` is Design in progress. `Review` and `Message` sit outside the flow: one assesses it,
one transmits across it.

**Resource, as vocabulary.** A type whose purpose is to be drawn on rather than produced or
delivered reads naturally as a *resource* — `Review`, `Reference`, `Glossary`, and an adopted
`Guide` sitting in a consuming project. The word infers purpose and nothing keys off it: it is a
reading aid for choosing a type, not a class. Nothing is recorded as a resource and no behaviour
follows from the word. **Resource-ness depends on which container is reading.** A `Guide` is an
outcome where it is produced and a resource where it is consumed.

**Three consequences, stated because each is routinely inferred wrongly:**

- **An outcome requires something defining it.** That is normally a Design, but it may be a
  Brief or another document where the definition genuinely sits there. What cannot happen is an
  outcome with nothing behind it — see §4a.
- **Decisions is not an input to outcomes.** Nothing downstream of the Design reads it. A
  consideration that must reach an outcome belongs in the Design, and its absence there is a
  Design defect, not a reason to reach back past it. §7d's bundle self-containment rule is this
  consequence.
- **Outcomes do not own each other.** An outcome's owner is what defines it, never a
  sibling outcome (§13a).

**The established types.** A project needing something else declares a custom type (§4h) or
holds the file unmanaged (§15).

**No count is stated.** Earlier versions of this Guide said "ten established types, the list is
closed" while listing ten and recognising more — `Index`, `OpenItems` and `WorkRegister` occupy
the type slot in real filenames throughout, and `OpenItems` had its own subsection and a row in
the distribution table. A count is a second thing to keep true, it earns nothing, and its being
wrong is what made the omission invisible: a project reading the closed list and not finding
`OpenItems` was being told to declare it custom. The list states itself.

| Type | Role | Holds | Lifecycle | Distribution |
|---|---|---|---|---|
| `Brief` | Defines | Why, scope, requirements, success signals | Living | Internal |
| `Requirements` | Defines | Standing cross-topic requirements, split from `Brief` when size warrants | Living | Internal |
| `Design` | Determines | The confirmed internal position — what *is* | Living | Internal |
| `Decisions` | Informs Design | The journey — requirement, alternatives, decision, consequences | Living | Internal |
| `Working` | Design in progress | In-progress discussion; items carry status | Merges, then archives or is disposed (§4-w) | Internal |
| `Review` | Assesses | A point-in-time assessment; findings carry status | Archives when every finding is resolved or superseded | Internal |
| `Guide` | Outcome | The published rule, derived from Design | Living | Consuming projects |
| `Reference` | Outcome | Published lookup material | Living | Consuming projects |
| `Glossary` | Outcome | Defined terms for a topic or project | Living | Consuming projects |
| `Overview` | Outcome | The standing narrative entry point: what this corpus is, reading order, current state | Living | Consuming projects |
| `WorkPackage` | Outcome | A unit of dev-side work; absorbs the Outcome on completion | Archives on completion | Dev side |
| `WorkPackage_Outcome` | Returns | The builder's record of what was actually done and observed | Folds into its Work Package on archival | Dev side (returns) |
| `Message` | Transmits | A governed cross-project transmission | Per §4f | Named recipient |
| `Index` | Records | What exists, at what version, and the project's local configuration | Living | Internal |
| `OpenItems` | Records | What is in flight and unresolved | Living | Internal |
| `WorkRegister` | Records | Consequences decided and not yet applied | Living | Internal |

Project-wide registers, no topic segment: `Decisions`, `Index`, `OpenItems`, `WorkRegister`.
`Requirements` is project-wide where it covers standing cross-topic requirements.

**`Overview` and `Glossary` are restorations, not additions.** Both were established at v14 and
vanished in the v15 restructure with no recorded decision. If your container re-derived either
under a local name, adopt the established type rather than keeping the local one.

**`Requirements` normally resides in the `Brief`.** Split it into its own document only where
size warrants.

**Assets are not document types.** A file whose filename is fixed by the tool that consumes it
is an **asset** (§13), outside the naming convention and outside the document register. The
`Reference`-versus-asset boundary is at §13c.

### 4-r. Retired types

A type that was established and no longer is has no version to resolve and appears in no list,
so nothing implies it existed. A reader holding a dead *filename* has §8c; a reader holding a
dead *type name* had nothing, and one project consequently re-derived `Overview` as a local
invention.

| Retired name | What became of it |
|---|---|
| `Glossary` | Restored. Established again — see the list above. |
| `Overview` | Restored. Established again — see the list above. |
| Standing `Review` | Withdrawn, folded into nothing. The continuously-updated, never-archived variant v14 defined separately from the dated one. `Review` as established is point-in-time only; a living evaluative commentary has no type. A surviving instance becomes a dated Review. |
| `WorkPackage_Implementation` | Folded into `WorkPackage` (§7a). |
| `Open Questions` register | Renamed `OpenItems`. |

**Declaring a custom type checks this table first (§4h).** A name here is a re-derivation
wanting restoration, not an invention wanting declaration, and the two want opposite handling.

### 4a. Guide

An **outcome**. Derived from the Design; states the rule, not the reasoning. Distributable.

**An outcome requires something defining it.** For a Guide that is normally a Design, but the
definition may legitimately sit in a Brief or another document where that is genuinely where it
lives. The rule is not "a Guide must have a Design" — it is that a Guide with *nothing* behind
it is incoherent, because an outcome is by definition the delivery of something determined
elsewhere. Where the definition sits outside a Design, the Guide says where.

### 4b. Design

The confirmed internal position — what *is*. Design is internal; its Guide travels. The pair
exists so that a rule confirmed but not appropriate to publish has a home. Design and Guide
overlapping heavily is an acceptable outcome: the pair exists for consistency, not because the
two must differ.

**A Design declares its outputs** — which Guides, References or other artefacts it produces,
and which handlers outside the corpus consume it. Declared in the Design itself, alongside its
related-documents header. Where a topic has no Design, its Guide carries the declaration or
states that it is itself the output.

### 4c. Brief

Why, the case, the objective, and — for a per-topic Brief — the requirements content
(functional, topic-specific non-functional, acceptance criteria, non-requirements, open
assumptions). Living, not dated. Optional by stakes, not mandatory by topic.

Recommended sections: opportunity or capability gap; who it serves; what is offered; success
signals; non-goals; open uncertainties. Deliberately not locked.

Standing project-wide NFRs are not restated per topic — they live in the project-wide
requirements register, or in a standards corpus, referenced.

The **blind-assessment boundary** sits between Brief and Design: a second reviewer may be given
the Brief without the Design to propose an independent approach.

### 4d. Decisions

Records thinking, not just outcomes. Written to the depth standard: requirement, problem found,
alternatives genuinely considered, key points worked through, decision, consequences —
proportionate to the thinking actually involved, in the manner of substantive meeting minutes.

**When an entry is owed.** Any change to the Design. Any requirement established or revised. Any
rejected alternative that a future reader might re-derive — the entry is what stops the
re-derivation. A Design change without a Decisions entry recording the reasoning behind it is
incomplete: the "what" and the "why" are produced together, not sequentially, because reasoning
that exists only in conversation is lost when the conversation closes (§16b).

**Existing entries are not retroactively rewritten.**

**A rejected alternative always gets at least a brief summary of why.** Proportionality governs
how much space it gets, not whether it appears. Omission is appropriate only where the
alternative was genuinely trivial.

**Decisions informs the Design and nothing downstream.** Its purpose is to make the next Design
change a good one — the path, the evolution, the experience, so a change is made with more than
the current snapshot in view. It is not an input to any outcome. Where a consideration must be
factored into delivery, it belongs in the Design; a Design that omits it is defective, and the
remedy is to fix the Design rather than to route an outcome's author back through the reasoning.

**Decisions follows the Design's granularity.** A Design at a sub-topic gets a Decisions at that
sub-topic. Project-level and topic-level Decisions coexist without conflict — §3 already lists
`Decisions` among the project-wide registers that omit a topic segment, so the project-level form
is the convention's default and a per-topic split is the departure.

**Reach is governed by the inheritance flag** (§8a), not restated per entry. A decision recorded
at a parent reaches every child declared `inherits`. A child declared `independent` does not
inherit it and holds its own.

**Where the right level is unclear, ask.** Scope is a design judgement, not a routing
calculation, and a project-wide rule filed under one topic is buried from every other.

**Growth.** Split only once retrieval starts surfacing the wrong entries. The axis is
**closure, not chronology**: a live register plus one or more closed volumes of fully settled
entries, with the live register retaining pointers. Never deletion; never rewriting an entry to
be shorter.

### 4e. OpenItems

**What is in flight.** Project-wide register, no topic segment. Supersedes any use of an
Index section for the same purpose.

- **Scope** — anything unresolved: open questions, work in flight, documents not yet produced,
  deferred items, pending message threads.
- **Current-work section** — what is active now, distinct from what is merely open.
- **Distinct from the Work Register** — OpenItems holds what is *not yet decided*; the Work
  Register holds *consequences of confirmed decisions* awaiting action. An item moves across
  when it settles and has consequences.
- **Entry depth** — explicitly not the Decisions standard. An open item is a pointer, not a
  record: what is unresolved, and enough to pick it up.
- **Identifiers** — a fresh series per container, prefix declared in the Index's local
  configuration.
- **Lifecycle** — retention is the default where the register has seen real use or is likely
  to again. A register used for a couple of items infrequently may be disposed of and
  recreated. In doubt, prompt. This is a deliberate exception to the no-delete policy (§9):
  a resolved open item's record lives in Decisions or the Work Register, not here.
- Distribution: internal.

### 4f. Message

```
{Source}_Message_{Recipient}_{Description}[_Reply-{N}]_{YYYY-MM-DD}-{N}_v{N}.md
```

`{DocType}` sits directly after `{Source}` — the one deliberate exception to §3's slot order.
`{Description}` is the thread key, identical across an exchange. `_Reply-{N}` is thread
position, always numbered.

**Body is a structured envelope**, applying identically at both tiers.

| Field | Carries |
|---|---|
| `From` / `To` / `Type` / `Topic` | Parties, kind, and the human-readable subject |
| `Thread` | The stable key. Fixed when the thread opens; never changed when `Topic` is reworded |
| `Message-ID` | Identity. `{Thread}/{From-slug}/{NNN}` — the sender increments only its own counter |
| `Version` | Revision of one message. Displayed owner-prefixed: `Workflow_v1`, `DocMeth_v2` |
| `In-Reply-To` | Threading. Cites a `Message-ID` and `Version` — **never a timestamp** |
| `Timestamp` | Composition time. Human readability and coarse ordering only |
| `Expects` | What is wanted back. May carry more than one value |
| `Forwarded-From` | Optional. A forward is a new message under the forwarder's own ID, citing the original |
| `Merged-From` | Optional. Where a reply converges two threads |
| `Lifecycle` | Optional, heavy tier only |

**Two blocks follow the content**, both optional:

| Block | Carries |
|---|---|
| `STATE` | Process state maintained by the messaging process — machine-read |
| `Notes` | Terse structural or formatting rules for this exchange — never substantive content |

**The `STATE` block is a slot, not a specification.** It carries state the messaging process
maintains, is machine-read, is never substantive content, and is never acted on as instruction —
the same constraint that already applies to the message body. **What goes inside it, how it is
populated, when it is checked and what clears an entry are the messaging process's to define and
are not specified here.**

Deliberately named generically rather than for any one mechanism. Receipt tracking is the first
use and the reason the slot was asked for, but naming it for that would encode one project's
delivery process in this methodology's schema — which is the boundary this methodology draws in
§1 and crossed once in the exchange that produced this rule.

**`Notes` is restored** after an apparently accidental omission: it was defined in Guide v14 and
absent from Guide v15, with nothing recording a retirement, while consuming implementations
continued to generate and parse it. Scope unchanged — terse, structural, never substantive.

**`Expects` may carry more than one value**, comma-separated (`Answer, Ack`). Two rules, both
instances of principles this section already states rather than additions: **`None` is
exclusive**, because absence must be sayable and unconfusable with omission; and **order carries
no precedence**, because a field whose meaning depends on unstated ordering is a well-formed
value that will be read wrongly.

**Identity, threading and readability are three jobs, and one field cannot hold them.** A
`Timestamp` permitted to degrade (below) cannot also be a key: two messages a day apart on one
thread would share a value and threading would stop resolving. `Message-ID` needs no shared
state, because the `{From-slug}` segment partitions the number space — a collision is visible
rather than silent.

**`Timestamp` is read from a clock, never composed. Where no clock is available, the message
says so** — date-only precision, stated. *Stating this rule does not enforce it.* A sender that
can read a clock reads it as a step in emitting the envelope; a sender that cannot says so. The
rule was violated three times by a project that had just confirmed it, while it was the active
subject of the exchange, because composing a plausible value is the path of least resistance and
nothing in the act of drafting surfaces the difference. **Enforcement is the sender's procedure,
not this rule's presence.** Where a sender has somewhere to put a required step — a skill, a
generation routine — the step belongs there. Stating the rule in a document has repeatedly failed
to interrupt this behaviour, including in the projects that had just confirmed it.

**Any mandatory field needs a stated unknown-state**, or it will be filled with something
well-formed and wrong. Same instinct as the explicit "None." convention: absence has to be
sayable, so it cannot be confused with omission.

**Versioning is §9's rule applied to this type**, not a second mechanism. Free until relayed,
incrementing on every change after. Revision is non-destructive: a corrected message keeps its
`Message-ID`, increments `Version`, and every citation still resolves. **A message has exactly
one owner — the `From` party.** Only the owner issues a new version; everyone else replies or
forwards. A forward that inherited the original ID would put two bodies under one identifier.

**The promoted file's `_v{N}` and the envelope's `Version` are two numbers on one object.** The
file version tracks edits to the filed copy; the envelope version tracks the message content.
One rule, two applications.

**A message terminates with its terminator, and its absence means the message is incomplete.**
A message received without its terminator **must not be acted on** and is reported back to the
sender. Truncation in transit is silent otherwise: a long message cut short arrives looking
well-formed, and a recipient acting on it answers a message the sender never wrote.

**Not a message:** a body both parties edit and pass back and forth. Once two parties are
editing one body it is a document with an owner or an explicit handoff, and takes normal
versioning.

### 4f-i. Source marking

**Unmarked content is AI-produced in this session on the sender's behalf.** Stated once here,
never re-declared per message. Two markers and one suffix:

| Marker | Means |
|---|---|
| `[human]` | The person's own statement or view |
| `[project: {ref}]` | A recorded position carrying corpus authority |
| `, out-of-band` | **Mandatory** suffix on any statement made outside the thread |

**Mark only where the source changes the weight the recipient should give the statement.**
Ordinary reasoning, analysis and drafting stay unmarked; a message where most sentences carry a
marker is using the convention wrongly.

**The out-of-band suffix is the mandatory one**, because it is the only case the recipient
cannot work out. Every other marker tells them something they could in principle derive; that
one tells them the record they hold is incomplete.

**A person operating two projects is not the projects speaking.** A statement made inside one
container is the person's, not that container's — collapsing the two produced a correct
misattribution correction that was then wrongly withdrawn.

**Frozen once relayed.** A post-relay correction is the thread's next turn, never a silent
mutation. Revision under `Version` is the sanctioned route and is not silent.

**Two persistence tiers.** Light: conversation-only, never a file, nothing to archive. Heavy:
promoted to a file, indexed by both sides while current, archived per its own terminal event
with the `_Archived_{date}` rename. Which tier a message takes is the sending project's
orchestration concern, not this methodology's. The light tier is expected to serve most
exchanges.

**States what it expects back** in its own header rather than carrying a generic status field.

### 4g. Review

A faithful record of an assessment at a point in time. **What it asserts must not change** —
the boundary is meaning, not mechanism.

Permitted: error corrections including numbering; a marked addendum; folding in a companion
Review; instructed changes. Any change increments the version. In doubt, prompt rather than
edit.

**Excluded:** a finding reworded, softened, closed or removed because it was subsequently
resolved or disputed. Working that results from a Review — resolutions, progress, findings
being closed — goes in a Working document.

Where the defect was in a **delivered** copy, the correction is noted in the Review's internal
section (§11), so a holder of the earlier copy can discover why their numbering differs.

Archival freezes the document: a defect found in an archived Review is handled by addendum or
a superseding Review, not corrected in place.

**Findings carry status, set in the Review itself.** The finding's text is never touched; the
status sits alongside it. This is not an exception to the paragraphs above — the rule's target
is a Review quietly updated as findings close until nobody can tell what was originally found,
and a marker beside an intact finding does not do that.

- **Values, closed:** `Open`, `Resolved`, `Declined`, `Superseded`. `Declined` earns its place —
  a finding assessed and deliberately not actioned is a real outcome, and without it those are
  marked resolved untruthfully or left open indefinitely.
- **`Open` is a finding's default and needs no marker.** A marker appears when the status
  changes.
- **A status may carry a pointer** to where the work went — an open item, a Work Register entry.
  The reasoning does not follow it; that belongs in a Working document.
- **A holder of a delivered copy is not reissued on a status change.** It is not a correction to
  what the Review asserts, so §11's delivered-copy notice does not apply.

The archive condition — every finding resolved or superseded — is then readable from the
document rather than tracked beside it.

### 4-w. Working

**Design in progress.** A WIP document: the distillation of a chat, a review's fallout, or any
other source into something to work through. It is added to and changed freely, and this is its
whole difference from a `Review` — a Review asserts what was found at a moment and its findings
do not move; a Working doc's items are meant to be reworked, split, reworded or dropped.

- **Named without a key** in the normal case — `{Project}_{Topic}_Working_v{N}.md`. A label is
  available where two are live on one topic at once (§3b).
- **Items carry status**, the same values §4g uses, and with none of §4g's edit boundary.
- **Threads may share one document** where a project has a single topic and can therefore name
  only one live Working doc.
- **Terminal event: all items complete.**

**Disposal is prompted, and takes one of two routes:**

- **Archive** — where anything in it is worth retaining. `_Archived_{date}` rename, per §9.
- **`/superseded`** — where the content is genuinely held elsewhere.

**Archive is the lean and the prompt is not skipped.** A Working doc often has little value once
worked through, and where `Decisions` and `Design` have done their jobs everything that mattered
is already in them — if the corpus is functioning, disposal is usually right. The argument
against relying on that is that `/superseded` is swept and guarantees nothing, so the judgement
"it is all held elsewhere" is unrecoverable if it proves optimistic, and it is made at the moment
someone wants to be finished.

**The trace costs nothing either way.** A Decisions entry assembled from a Working doc names it
in that entry's footer references (§3c), so a disposed Working doc still leaves a name and a
version behind in the document it fed.

### 4h. Custom document types

**This methodology exists to add capability, not to constrain.** Your project needs to be free to
create documents as its work requires. Where an established type does not fit, declare a custom
type — and nothing about that is a compliance failure, a workaround, or a state to be corrected.

**Custom-typed documents are fully managed.** They follow the naming convention, carry a version
suffix, carry the §3c footer, sit in the Index document register, and use `/superseded`,
`/archived` and supersession exactly as established types do. Nothing behaves differently.

**What the project owns is the semantics and the lifecycle.** What the type means, what belongs
in it, when to use it, what good looks like, and when a document of that type ends — all yours.
The undertaking is the point: **a project creating a document outside this methodology's defined
types is responsible for that document and its lifecycle.**

**This methodology never initiates a lifecycle event for a custom-typed document.** No archival
prompt, no staleness flag, no sweep, no supersession detection. The mechanisms are available and
you are welcome to use them; nothing fires unless you fire it.

**Consequence for the register.** A custom-typed document's register row is a claim this
methodology cannot stand behind — nothing checks it, so it can read current indefinitely while
the file rots. That is yours to carry by design, and the row says so, per §14.

**Definition — recommended, not required.**

*Always worth stating:* what the type holds, and which established type it was nearly. The second
matters most — it is what stops two containers inventing the same thing under different names,
and it is the evidence that decides promotion.

*Only where it differs from the default:* lifecycle and distribution.

*Only where it applies:* the type's position in §4's model. Needed if documents of the type
define an outcome or an asset, because that is what makes them a legitimate owner (§13a);
irrelevant otherwise.

**Shape** — the same columns as the type table above: name, role, holds, lifecycle, distribution.
Promotion then becomes moving a row rather than rewriting a definition into a foreign shape.

**A project that states only what the type holds has produced a valid definition. A project that
states nothing has produced a valid document** — the register records it as custom and the type
is undefined, which is a fact about your own material and not a defect this methodology asserts.

**Where the definition lives — your choice, three valid locations:**

- **In the document's §3c footer.** Recommended for a single document of its type, and required
  in effect for any custom type that travels: a footer definition goes with the file.
- **In the Index's local configuration.** Recommended where several documents share the type.
- **Elsewhere**, with the register row recording where.

**Where the definition is not in the file, the file states that it is a custom type and where the
definition is held** (§3c).

**Defaults on silence: living, and internal.** These are what this methodology assumes when it
must assume something, so that silence produces a defined outcome rather than an error. **No
declaration gates creation** — name the document, register it, and you are done; a definition may
follow later or never. The cost is accepted: a project that meant its type to be terminal and
never said so gets living behaviour, and nothing flags the mismatch.

**Recognition** — anything not on the established list is custom by definition. No marker syntax.
Collision with an established type name is prohibited. **The retired-type table (§4-r) is checked
first:** a name there is a re-derivation wanting restoration, not an invention wanting
declaration.

**Promotion** — a custom type that recurs across containers, or is identified as generally
useful, is defined in this Guide as an established type; projects are then instructed to adopt
it, or to migrate specific documents to it. Promotion is this methodology's decision, proposed by
the originating project as a Message. The trade it offers is explicit: full freedom over what a
type means and when it ends, in exchange for nothing watching it — promotion is where this
methodology starts caring on your behalf. Demotion needs no mechanism: a type that falls out of
use stops being used.

### 4i. Not document types

- **Per-symbol API reference** — generated from source, not a corpus document.
- **A shared entity/state model** — a reserved topic name, not a type.
- **An asset** — a file whose filename is fixed by the tool that consumes it. Its own
  category, not a type; see §13.

## 5. Condensed and expanded topic documents

A small topic may hold Brief, Design, Decisions, open items and Working discussion as
**sections within one file**. Terms: **condensed** (one file) and **expanded** (separate
per-type documents). Switching either way is valid; if it is unclear which is meant, ask.

- **Naming** — a condensed file takes the DocType of its highest-order content: `Design` where
  it holds confirmed rules, `Brief` where the topic is still only scoped. No condensed marker
  in the filename.
- **Mode is recorded in the Index**, against the topic (§8a).
- **The Index and the Work Register never condense** — both are per-container, not per-topic.
- **Decisions may split out alone** while the rest stays combined, once it grows.
- **A Guide does not condense into a Design.** Condensing concerns internal working documents;
  a distributable Guide differs by class, not by size.

**Signals to expand** (any one is sufficient): a Working section reaches confirmation and needs
archiving; retrieval surfaces the wrong section; the whole file must be read to find anything;
sections have genuinely independent edit cadence; **a blind review is required** — Decisions
inside the Design file means handing over the design hands over the reasoning; or you are told
to.

## 6. Tracking work: the Work Register

**Any design change with a downstream consequence is either applied in the same pass or written
to the Work Register. There is no third option.**

A register line states: what changed, what it now requires, where that lands, and status.
Dispositions include a Work Package, a Guide or Reference update, a Message to another project,
or a change handled by tooling.

**Scope** — project-wide, spanning topics, because its distinctive job is catching consequences
that cross them. Delegable to a branch on the same signals as the Index (§8b), one
authoritative register per branch. Never folded into a condensed topic doc.

## 7. WorkPackage document integration

Generic WorkPackage authoring/execution/validation/return semantics are owned by
`AIDE_WorkPackage@v1` and `AIDE_Build@v1`. This methodology owns only how WorkPackage and
WorkPackage Outcome **documents** are named, versioned and archived.

### 7a. Live document pairing

A WorkPackage is an established point-in-time document type. Its date key identifies the opened
unit of work.

Where a separate `WorkPackage_Outcome` file is produced, it shares the WorkPackage's key during the
live phase so the pair is discoverable by filename.

The content contract, statuses, review posture and execution evidence are not restated here; use
`AIDE_WorkPackage`.

### 7b. Archival consolidation

After the director of work has reconciled the returned Outcome, the WorkPackage may archive.

Where a separate Outcome file exists, append it **verbatim** as the final outcome/addendum material
before archival; evidence is not paraphrased merely to make the archive shorter. The consolidated
file records the absorbed Outcome filename in its Internal section so older references can resolve.

The archived filename follows the normal `_Archived_{date}` convention. Superseded intermediate
versions are not gathered into the archive.

### 7c. Design/Build ownership

Project Design normally defines/authorises the work. Build executes within the WorkPackage
authority and returns evidence. A design-shaping issue exposed by execution returns to Project
Design rather than being silently settled by document mechanics.


## 8. The Index

The authoritative source for what exists, what version is current, what type a document is,
and — per §3a — the topic set and its hierarchy. Every other document defers to it.

**Five sections, in this order:**

1. **Project identity** — self-contained, with a stated rationale.
2. **Topic declarations** — §8a.
3. **Local configuration** — overrides, substitutions, type extensions, custom type and
   OpenItems identifier declarations. Each entry reasoned, or "None." stated explicitly.
4. **Document register** — what exists and what is current, plus the `/archived` contract (§9)
   and the withdrawn/renamed/rehomed record (§8c). Every row carries a **management** value:
   `established`, `custom` or `unmanaged` (§4h, §15). Unmanaged files sit in this register rather
   than in a sub-table of their own.
5. **Assets register** — where the container has any. Structure and contract at §13d. Assets stay
   separate because their fields differ — file, deploy path, owner, dependencies — and they are
   not named by the corpus at all.

**No changelog.** Pass-grouping is carried by Decisions consequences and, for a git-backed
corpus, by the commit. A changelog in the Index is a third copy in the most-read document.

**The Index carries local exceptions only** — never a restatement of a convention stated here.

### 8a. Topic declarations

Each topic is declared with five fields:

| Field | Meaning |
|---|---|
| Name | The topic |
| Parent topic | Its place in the hierarchy |
| Filename prefix | What a reader looks up to resolve a filename |
| Inheritance | `inherits` \| `independent` — whether the parent's context loads with the child |
| Mode | `condensed` \| `expanded` (§5) |

`inherits` and `independent` are defined here so they mean the same thing in every corpus; what
a project does with the signal is the project's. A single-topic project declares its one topic
with no parent rather than omitting the section.

**Inheritance governs decision reach, not only context loading.** A decision recorded at a parent
reaches every child declared `inherits`, and does not need restating there. A child declared
`independent` does not inherit it and holds its own — which is what caps a decision at a
threshold (§4d).

Stated because it is a real consequence of setting the flag, and previously the field was
described only in terms of retrieval. A project declaring a branch `independent` for resource
reasons — it shares a container without being a subdivision of its parent's subject — is also
declaring that the parent's reasoning does not reach it.

### 8b. Index delegation

**Inheritance by default, delegation by exception.** A topic is covered by the nearest Index
above it. Exactly one authoritative Index per branch.

**Signals to delegate** (any one is sufficient): the branch has its own working cadence and
changes for reasons unrelated to the parent; the parent's register can no longer be read for
the parent's own purposes; the branch's topic name has reached three-plus parts; or you are
told to.

- **The parent** records the delegated topic path and the child Index's filename, and nothing
  else about that branch. No document list, no version summary.
- **The child** carries the full section set on its own account, naming its parent Index
  in its identity block, and tracks its own `/archived` contents.
- **Delegation is reversible.** A branch that goes quiet folds back and its Index is retired —
  to `/superseded`, not `/archived`, since no terminal event of its own type occurred.

### 8c. The withdrawn, renamed and rehomed record

A sub-table of the document register, recording documents that ended without their own type ever
reaching its terminal event (§9): old filename, and what it became.

| Document | What it became |
|---|---|
| `DI_Lazy_Guide_v1.md` | Folded into `DI_Guide.md` as its Lazy section |

**Why it is separate from the register itself.** The current-documents register implies what
existed for a document still living — anything below its current version existed, anything above
it did not. That inference does not reach a document that was withdrawn, renamed or rehomed: it
is not a lower version of anything current and appears nowhere in the register. Same reasoning
that keeps `/archived` tracked (§9).

- **Keyed per name a reader might hold — not per document.** The reader arrives holding a name
  that no longer resolves and asks what became of it. Where a document changed names more than
  once, **every dead name gets its own row**; keying one row per document resolves only the most
  recent, and a reader holding an earlier name finds nothing. An intermediate row points to the
  confirmed row that carries it onward rather than restating the whole chain.

  The bound is unaffected: rows are bounded by naming events, not by version count.

- **An unconfirmed successor is recorded as unknown, never as a plausible value.** Where a chain
  ends with no confirmed destination — a file possibly retired at a reorganisation rather than
  carried forward — the cell is left empty and says so. A prose hypothesis about likely
  retirement is the composed-value failure in a softer form and is not a substitute for an empty
  cell.

  This is §14 applied to this table: a plausible successor filename is a well-formed value
  composed rather than read, and is indistinguishable from a real one by inspection.

- **Confirmed versus inferred is marked so that no reader can mistake one for the other.** Stated
  once at the table where the table is uniform; **per row where it is mixed.**

  *This revises the earlier rule*, which required the statement once at the table and prohibited
  per-cell annotation. That works only where every row is the same. The first container to build
  the record held eleven confirmed rows and five inferred, and a single statement would have
  either overclaimed eleven or underclaimed five. Mixture is the normal case, because inference
  enters exactly where recovery reached a limit.

  *Annotation alone remains rejected, and this is not that.* Marking an inferred cell and
  stopping there tells a reader "uncertain" and gives them nothing to look up. The answer is the
  resolution row — marking says the value is inferred, the resolution row says where to go
  instead.

- **A terminal-fate record, not version tracking.** Bounded by how often such an event happens
  rather than growing with every version bump. Entries are not removed.
- **"Withdrawn, and folded into nothing"** is a valid entry. A document abandoned before it
  reached any terminal state is exactly the case that has no other record.
- **Absorption is excluded.** An Outcome folding into its Work Package (§9) is recorded on the
  package's `/archived` line and does not appear here.

A container that has had no such event states **"None."** rather than omitting the sub-table.

## 9. Storage and the no-delete policy

Superseded version files are not deleted.

**When a version increments is at §16.** In short: a version identifies an issued file and
increments once per output. Before a document is first issued it is revised in place without a
bump; after that, each output is the next version.

**Delivery is judged by the person, not by the drafting agent.** Where a document or message
reaches its destination by hand — copy-paste relay, manual upload — the agent that composed it
cannot observe whether that happened, and a message believed sent may never have been relayed at
all. A revision made before relay stays at the same version; the person relaying is the
authority on whether relay occurred. Message's frozen-once-sent rule (§4f) is §16's rule applied
to a type that is delivered by definition, not a separate mechanism.

- **`/superseded`** (formerly `/prev versions`) — superseded version files of any document.
  **No guarantees**: the folder makes no promise about what it holds or that anything stays,
  and it is periodically swept. **Nothing cites a superseded file.** **Not tracked** in the
  Index — the current-documents register already implies what existed, and tracking a swept
  folder cannot be relied on.
- **`/archived`** — the final, frozen version of a document that reached a terminal lifecycle
  event. **Tracked, one line per file**, as cold storage that can be requested from: nothing
  else records that these documents existed at all.

**A document withdrawn, renamed or rehomed** — never reaching a terminal event of its own type
— goes to `/superseded`, keeping its plain `_vN` filename, no `_Archived_{date}` rename. The
Index records what it was folded into, in the document register's withdrawn/renamed/rehomed
sub-table (§8c).

**A type's terminal event may be absorption rather than archival.** An Outcome reaches its
terminal event by folding into its Work Package (§7a), which then archives as one file. The
Outcome's own file is not separately archived and does not go to `/superseded` — it was not
superseded by a newer version of itself. The Index's archived line for the package carries the
absorbed Outcome's original filename so citations to it resolve.

**Assets are excepted from the no-delete policy** (§13e). A regenerable asset loses nothing by
being deleted, and without the exception stated a container preserves generated files forever
out of caution. The exception's limit is stated with it.

**Neither folder's contents may be assumed present** in context. Absence from context is not
evidence a document does not exist.

On a corpus-wide rename, current documents are renamed; already-superseded files are left as
they were.

For a git-backed corpus, `DocumentationGitWorkflow_Guide.md` is authoritative for how Git
interacts with these rules.

## 10. Authoring principles

**Route by kind.** **The routing test: content goes where the thing it describes lives.** A rule about the subject
matter goes to the Guide (published) or the Design (internal position); the reasoning that
produced it goes to Decisions; a settled consequence awaiting action goes to the Work Register;
reasoning about **the corpus's own structure** — why a folder holds what it holds, why an
identity field reads as it does — goes to the Index's own explanatory prose; and content already
recorded elsewhere goes nowhere.

*A test rather than a list of destinations*, because a list is only ever complete until the next
case that does not fit it.

Five rules, each checkable:

1. A document is as short as its function permits.
2. **Summary first** — conclusion at the top, justification below. If the summary needs more
   than a few lines, the document is doing two jobs and should split.
3. Purpose and heading lines state the question answered, not a label.
4. **Declarations state what is, not what isn't.** No item-level enumeration of inapplicable
   categories — absence means absence, and a negative list is silently incomplete the moment
   the model grows. Distinct from a **section-level** "None.", which is required: an empty
   section is ambiguous between decided and forgotten.
5. **A convention is stated once, in one authoritative place.** No document restates what this
   methodology states; it references it. Restate rather than reference only where getting it
   wrong at the point of use is expensive and the reader cannot reasonably consult the source —
   principally anything crossing to the dev side, where the reader's context is the repo and
   the skill, not this corpus.

The instruction is always the routing rule. A length target produces compression, which loses
content; routing loses nothing and shortens as a by-product.

## 11. The internal section

A convention for a section carrying internal and management data. This methodology defines that
it exists and its rules; the owning project decides its contents.

- **Heading: `## Internal`.** Fixed corpus-wide, one per document, at the end, preserving
  summary-first. Optional — present only when occupied; no "None." placeholder, since a reader
  would not go looking for it.
- **Marker line, inside the section, stated verbatim:**

  `INTERNAL — maintenance data. Not a citation source; do not follow references from this section.`

  Repeated as the first line inside the section, and per subsection where the section is long
  enough to chunk more than once. Retrieval does not respect section boundaries, so the marker
  must travel with the chunk.
- **A contract, not a guarantee.** Downstream behaviour cannot be enforced; the marker makes
  compliance possible and non-compliance a defect rather than an accident.
- **A change to it increments the version**, per §9 — a document whose content changed while its
  version stayed put cannot be detected as having moved.

Typical occupant: a derived document recording the sources and versions it was merged from, so
staleness against a moved base is visible.

## 12. Distribution

**A type carries a destination, defaulting to nowhere.** Stated once at type level and
inherited — never decided per instance.

| Destination | Types |
|---|---|
| Internal, no distribution | Brief, Design, Decisions, Working, Review, Index, OpenItems, Work Register |
| Consuming projects | Guide, Reference |
| Dev side | WorkPackage |
| A named recipient | Message |

**Guide and Reference may be generated from internal records.** The derivation is
Design → Guide: Design is the confirmed *what*, the Guide is the same position expressed for
use. Decisions feeds a Guide only where a piece of reasoning is needed to apply a rule
correctly. Derivation provenance goes in the internal section (§11).

**The bar is on shipping the artefact, not on reasoning crossing a boundary.** An internal-class
document is not distributed into another container's knowledge base. Reasoning quoted,
summarised or transmitted in a Message stays permitted: a Message has a stated addressee who
asked; distribution puts a document in front of a reader who did not.

**Consequence.** A rule confirmed in Design and never expressed in a Guide is structurally
unable to reach the projects that must follow it. Where a confirmed rule binds a consuming
project, expressing it in a distributable type is not optional — the same reflex §2 applies to
Working docs.

**Migration.** A version bump that creates conforming work for consumers is handled **per
project**: the new Guide and a request for that project's current state go out together, and
migration instructions are then drafted against the reply. One project at a time, each set
informed by what the last exchange raised.

*This replaces the universal per-pass migration Guide*, which could not be right for every
reader because it was written against assumed corpus states, and whose corrections always arrived
after someone had already followed the defective step.

**Do not infer another project's state — ask.** Recovery advice in particular: `/superseded`
guarantees nothing, so it may be checked but never stated as a reliable route.

## 13. Assets

**An asset is a file this corpus produces whose filename is fixed by the tool that consumes
it.** That is the test. It is normally generated from one or more documents, and that is the
useful everyday heuristic — *is this argued about here, or generated from something argued about
here?* — but generation is not the definition. A corpus `README.md` is authored rather than
generated and is still an asset, because the corpus produces it and its name is not the corpus's
to choose.

**A file this corpus writes rules about but does not produce is subject matter, not an asset**,
however tightly its name is fixed elsewhere. A coding-standards corpus that names
`.editorconfig` or `Directory.Build.props` and mandates their contents does not thereby hold
them as assets — it does not produce them.

An asset is **not a document type** (§4i). It is outside the naming convention (§3), outside the
document register (§8), and outside the distribution table (§12).

**A rendering of a document is that document, not an asset.** A Reference printed to PDF carries
its own versioned filename and needs no provenance line and no naming exemption. Only a
tool-fixed filename creates an asset.

**A Guide is a document, not an asset**, and this holds under the test rather than by assertion:
a Guide's filename follows `{Project}_{Topic}_{DocType}_v{N}` and is therefore not fixed by
anything consuming it. Stated explicitly because a Guide is deployed into consuming projects,
which is superficially asset-like.

**An asset is your file.** Its creation, content, format, management, versioning, and lifecycle
are the responsibility of your project and the asset's owner. This methodology does not govern
those things. What it provides is a set of conventions you can use — a register, dependency
tracking, a provenance line, a storage convention — each of which confers a benefit when
adopted. A project that uses none of them has assets this methodology records and nothing more.
A project that records dependencies gets change-impact flagging. A project that uses the
provenance line gets currency tracking. The methodology is additive: it adds capability where
you opt in.

### 13a. Owner

**An asset has an owner, and the owner is responsible for it.** The owner may be a document (a
Design that defines it), a process (a workflow rule that generates it), a convention (a standard
that mandates its shape), a person, or the asset itself where nothing else defines it. What the
owner is and how you state it is your choice.

**Where the owner is a document, that document is also the dependency edge.** A change to the
document surfaces the asset as potentially stale — the same mechanism as document-to-document
dependency in the footer (§3c), extended to assets.

**Where the owner is a process or convention, the register records that description.** The
dependency edge is whatever you state — the name of the process, a pointer to where it is
defined, or nothing. Where nothing is stated, this methodology records nothing and asserts
nothing; the owner is responsible for knowing when the asset needs attention.

**A document created solely to hold a deployed asset's text is not an owner.** It is a second
copy wearing a document's name, and typing it makes the duplication governed rather than removing
it. The remedy is to route its content into the document that should hold it, or to declare the
asset self-owned.

**This replaces the mandatory-master model.** Earlier versions required every asset to state a
master and made the master the only permitted owner. If your container built its register against
that, the field set below is a superset — nothing you recorded becomes invalid, and the mandatory
parts shrink to two.

### 13b. Storage and paths

**An asset declares a deploy path at creation.** The deploy path is the asset's identity, not its
filename — because the filename is fixed by the consuming tool and is therefore commonly
identical across instances (`README.md` exists once per folder, `SKILL.md` is identical across
every skill).

**Where the corpus holds a master copy, that copy sits in the assets folder or a subfolder of
it.** An `assets\` folder is a recommended default, not a rule. **Subfolders within it are
available for organisation**, particularly where naming collisions would otherwise occur —
several skills each named `SKILL.md` distinguished by subfolder, for instance. Where the master
file physically sits is a container concern; the register records the path.

**An asset is not in context.** Assets are output files, normally deployed elsewhere, and are not
loaded as project knowledge. Cite the owner or the source document, not the asset.

### 13c. Versioning, currency, and the boundary against `Reference`

**This methodology does not assign version identity to assets.** The Index does not give an asset
a `_v{N}` identity the way it does a document. How you version your own assets — in the filename,
in the file content, by timestamp, or not at all — is your choice, and this methodology records
whatever you state. **The filename-versioning prohibition is withdrawn.**

**The provenance line is an available convention, not a requirement.** Where you use it, the line
carries source documents with versions and a generated date, in a form and placement defined by
the process that produces the asset. Where the format can carry a provenance line, the file is
authoritative and the Index row mirrors it. Where it cannot, the Index row is the sole record,
and the asset's row says so.

**Stated limit.** A matching provenance line proves the asset was generated from those versions.
It does not prove the body reflects them. A line updated without regenerating is a well-formed
value that any check will believe.

**The `Reference` boundary.** A `Reference` holds distilled lookup material, never a verbatim
second copy of a live asset. Where content genuinely has no source and never will — third-party
text neither authored nor routable into a Design — a `Reference` holding it verbatim is correct,
carrying a line stating that it is a copy and where the original lives.

### 13d. The assets register

Where a container has assets, its Index carries a section for them (§8). One row per asset. Two
fields identify it; everything else you record as you choose:

| Field | Purpose |
|---|---|
| **File** | What the asset is — filename and location in the assets folder, or a subfolder path |
| **Deploy path** | Where it is read from — the asset's identity |
| Owner | What defines it — a document, process, convention, or `self` |
| Version / timestamp | However you track currency, in whatever form you use |
| Dependencies | Documents, other assets, or processes the asset depends on |
| Generated | Date of last generation or update |
| Source versions | The document versions it was generated from, where applicable |
| Disposition | What happens when the owner reaches a terminal event (§13e) |

**The first two are identification; the rest are optional.** An unsupplied field reads as "not
established" rather than blank — a row stating what is unknown reads as checked rather than
skipped. A register row with only the file and deploy path is valid and expected.

**Where dependencies are recorded, they are the change-impact edge.** When a dependency changes,
the AI searches its context for what to do — an instruction from the owner, a convention, a
process definition — and acts on best effort. Responsibility for what happens on a dependency
change sits with the owner; this methodology's job is to make the dependency visible so the
change is not missed. Where no dependency is recorded, no flag fires, and that is your choice
rather than a gap.

No separate dependency register exists — a hand-maintained second edge list decays silently.

### 13e. Lifecycle

**Deletion.** Assets are excepted from the no-delete policy (§9): a regenerable asset loses
nothing by being deleted. *Limit:* regenerable means the **file** is recoverable, not the
**bytes**. The same source versions regenerated by a changed generator produce a different
artefact. Where exact deployed bytes matter — reconstructing what a tool actually read during an
incident — regeneration is not a substitute and this exception promises nothing.

**Where the owner is a document and that document reaches a terminal event**, the register's
disposition field states what happens to the asset. Where a disposition is declared, it is
applied. Where none is declared, the asset follows its owner by default.

**Where the owner is a process or convention**, the process owns the asset's lifecycle and the
register records the disposition but does not trigger it. Enacting cleanup belongs to the owner.

**This methodology's obligation is that declared dispositions are recorded and visible.** The
register holds the answer; visibility at the moment the lifecycle event occurs is a step the
owner takes, not a property the register has.

**The automatic lifecycle triggers are withdrawn.** Earlier versions had this methodology fire on
a master's terminal event and enumerate dependent assets. Nothing fires unless you fire it.

## 14. Claimed versus verified

**This methodology's currency and provenance mechanisms record a claim, not a verified fact.**
They make the honest case cheap and the record legible; they do not make the dishonest case
impossible.

**The act, not the list.** Earlier versions enumerated the mechanisms carrying this property.
Enumeration cannot work, because each new mechanism arrives without the caveat and the list is
always one instance behind. What all of them share is a single act:

> **A well-formed value composed rather than read.**

Composing is always the path of least resistance — a plausible value costs nothing, requires no
tool, and is indistinguishable from a real one by inspection. Nothing in the act of writing
surfaces the difference, and every downstream reader believes it.

Known instances, offered as illustration rather than as the definition:

| Mechanism | The composed value |
|---|---|
| Asset provenance line (§13c) | Source versions the asset was not generated from |
| Source markers (§4f-i) | An attribution not held |
| Skill-to-marker version check | A version not compared |
| `Timestamp` (§4f) | A time not read from a clock |
| Send history | An assertion of delivery with no record behind it |
| A successor filename (§8c) | A plausible destination in place of an unknown one |
| Statements about another container's contents | Inference reported as inspection |

**Two rules follow.**

**A mechanism that cannot be checked states so where it is defined.** The failure to avoid is a
new mechanism arriving without the caveat, and a reader inferring verification from silence.

**Where the true value is available, read it.** Most instances above were not unverifiable — the
clock, the file, the register were all reachable, and were not consulted. The unverifiable case
needs the caveat; the available case needs the step.

**Send history has a verification condition, which most of these do not.** A claim about whether,
when or to whom something was sent is established **only by a reply demonstrating receipt** — the
other party referencing the content back. The sending is not evidence, and nothing short of the
reply is. Absent one, it is an assumption and is written as one.

**The authoring consequence:** a message is written to stand alone, not to depend on an earlier
one having arrived. *"Supersedes the earlier X"* is true whether or not X landed; *"further to
our message of the 14th"* is not. Where prior delivery genuinely matters, ask — a question is
answerable where an assertion is not.

**Delivery handling itself — tracking, follow-up, acknowledgement, reconciliation — is not this
methodology's.** It belongs to the process that operates the channel. What is stated here is what
a record proves, which is a documentation question.

## 15. Unmanaged files

**An unmanaged file is a file the container holds and this methodology does not govern.**
Reference material, a parked draft, a record kept for context, something dropped in from
elsewhere — and equally, a document your project authored and has chosen to manage on its own
terms. The obligation is to note that it is there; not to own it, name it, version it or give it
a lifecycle.

**A project-authored unmanaged file is legitimate, not a compliance failure.** This class was
previously named *held file* and every example given was foreign in origin, so a project reading
it concluded that the only route for something off the type list was a custom type declaration —
which is this methodology asking to govern something you never asked it to govern. The class was
always defined by governance rather than origin; the name and the examples said otherwise.

**Four classes of file, and the boundary between them is who governs, not where it came from:**

| Class | Type defined by | Managed | The corpus… |
|---|---|---|---|
| **Established type** | this methodology | yes | names it, types it, versions it, governs its lifecycle |
| **Custom type** (§4h) | your project | yes | names it, versions it, registers it — you own its meaning and its lifecycle |
| **Unmanaged** | nobody; it is a file, not a type | no | holds it, records it, asserts nothing further |
| **Asset** (§13) | its owner | — | produces it but cannot name it: the consuming tool fixes the filename |

Assets sit outside the first three rather than alongside them: theirs is a question about who
chooses the *filename*, not about who defines a type.

**The choice you face, stated as a choice.** Declare a custom type where you *want* this
methodology's file behaviour — naming, versioning, registration, the ability to travel. Record it
as unmanaged where you want this methodology to stay out. Both are correct answers; neither is a
fallback from the other.

### 15a. What is recorded

Unmanaged files sit in the Index document register alongside everything else, carrying
`unmanaged` in the register's management column (§8). They are not given a separate sub-table: a
reader meeting an unfamiliar filename goes to one place and finds out what it is.

**Mandatory — two fields.** The filename, and the date it was recorded.

**Optional — five attributes**, each of which produces stated behaviour when supplied and none of
which is required:

| Attribute | Behaviour when supplied |
|---|---|
| **Purpose** | None. Context for a reader — and in practice the most valuable of the five, because it answers the question a session actually has. |
| **Editable** | `read-only` means a session does not modify the file. `editable` asserts no constraint beyond permitting change. |
| **Versioned** | `yes` applies §9's delivery-based version rule on edit: the version increments on every change after delivery. It confers no type and no lifecycle. |
| **Source** | None. Where the file came from, which is what makes a later decision about it possible. |
| **Lifecycle** | A tie to a topic or a unit of work. When that reaches its terminal event, the unmanaged file surfaces for a decision about what becomes of it. |

**An unsupplied attribute is recorded as "not established," never left blank.** A row stating
what is unknown reads as checked; a blank reads as skipped — the same device §13d uses for asset
register fields. It also makes the gaps a set that can be acted on, which is what the review
behaviour below needs and could not otherwise have.

An unmanaged file with all five unestablished is a valid and expected entry. It is recorded, it is
dated, and nothing further is asserted about it.

### 15b. Two limits, stated rather than left to inference

**A type segment in an unmanaged file's name is not a claim under this methodology.** An
unmanaged file may arrive carrying what looks like a DocType and a version — `SomeThing_Working_v1.md` — without any
of the behaviour those segments imply in a governed document. It confers no lifecycle and no
obligation. Renaming a file over a naming coincidence is ceremony this methodology resists; the
register row's `unmanaged` management value carries the disclaimer instead (§8, §15a). This is
the one place a reader who has consulted the Index can still be misled by a filename.

**The lifecycle field is defined; the behaviour that fires on completion is not.** The field is
recorded from the outset so nothing needs migrating later, and the intent is stated — the entry
surfaces for a decision — but no procedure is written until a real instance exists. The first
case in hand ends by promotion to another project, which is neither a topic nor a work unit
reaching a terminal event, and inventing the procedure around a case that does not fit it is
exactly what R8 resists.

### 15c. What this methodology does not define

**When unmanaged files are reviewed, and how a user is prompted about one, is out of scope.** That is
behaviour applied through an interface — process, owned elsewhere. This section defines what is
recorded and what each attribute means when supplied; it states no cadence and no trigger.

Stated explicitly so the omission reads as a boundary rather than a gap. What this corpus
provides to whatever does own the behaviour is a record whose unestablished fields are visible
and queryable; expanding an entry over time is expected, and is not written here as a duty
because an unenforceable duty is worth less than a self-flagging record.

## 16. Output and version discipline

This governs when a document is produced, who asks for it, and what its version number counts.
It was previously nowhere: §3 stated the increment rule as a gloss on a filename segment, §9
stated it differently as a storage rule, and the rest was local practice that never travelled.

### 16a. The version counts outputs

**A version identifies an issued file.** It increments **once per output**, not once per change.
A working session that makes forty edits and issues one document produces one version.

- **Before a document is first issued** it is revised in place without a bump. Nothing has been
  seen, so there is nothing to distinguish from.
- **After that, each output is the next version.** Changes accumulated between outputs are one
  increment, and none is exempt on the grounds of feeling small.
- **Versions are not created unnecessarily.** A version produced to record a trivial edit that
  nobody asked to receive is churn: it displaces its predecessor in `/superseded` and buys
  nothing.

**This supersedes the change-triggered wording** that stood in §9, which counted changes rather
than issues. The rule it was protecting is intact — the failure it was written against was
editing a delivered document and leaving the version alone, and that remains a violation,
because the edit reaches a reader only by being issued.

### 16b. When output happens, and who asks

- **Normally at the end of a unit of work or a session, or at a key point** within one — a
  decision locking, a thread closing, a body of confirmed material large enough to be worth
  holding.
- **Either side initiates.** The owner requests it, in whatever terms — update, produce, issue,
  output. The drafting agent prompts where it judges the moment right, and says why.
- **Nothing is produced without confirmation**, or as part of an action already prompted and
  agreed. No unrequested new versions. No unrequested new documents. A draft offered in
  conversation is not an output and needs no confirmation; writing a file is.
- **A Design change is accompanied by a Decisions entry.** The two are produced together in the
  same pass, not sequentially. A Design output without the corresponding Decisions entry leaves
  the reasoning in the conversation where it will be lost (§4d).

### 16c. Pending content is not lost

**This is the overriding rule of this section, and it outranks the three above it.** Every rule
in §16a and §16b restrains output; this one compels it, and where they conflict this one wins.

Confirmed material that exists only in a conversation is one closed window from being gone.
Where that is the situation, **the prompt becomes a mandate**: the drafting agent states the
exposure plainly, names what would be lost, and presses — it does not mention the risk in
passing and proceed as though it had discharged the obligation.

**Restraint is not a defence against loss.** "Nothing is produced without confirmation" is not a
licence to sit on confirmed material until asked; it governs *what* is produced, not *whether*
the exposure is raised. An agent holding unwritten confirmed decisions and waiting quietly to be
asked has broken this rule, not observed the previous one.

**Where output is blocked** — a stale corpus, a missing current version, an unresolved
dependency — the block is stated, and something that can be safely written is written instead.
A blocked pass is not a reason to hold everything.


## 17. v18 migration declaration

```yaml
MigrationSummary:
  CurrentVersion: v18
  LatestRequiredVersion: none
  LatestOnUpdateVersion: v18

Transition:
  Version: v18
  Posture: OnUpdate
  Change: >
    Replace the special Methodology footer checkpoint with AIDE_Dependencies conformance,
    adopt extensible metadata/state container placement, and delegate generic WorkPackage
    execution semantics to AIDE_WorkPackage.
  Items:
    - Replace Methodology: v17 with the document's AIDE_DocumentationMethodology dependency checkpoint.
    - Convert legacy Depends on relationships that are true conformance dependencies to Dependencies: syntax.
    - Preserve References as document citations where no conformance obligation exists.
    - Host Tags/Identity/temporary state under the v18 container rules where present.
    - Do not otherwise rewrite unchanged document content merely because v18 is applied.
  Success: >
    The saved document uses v18 metadata placement, records a truthful Documentation Methodology
    dependency checkpoint, and has no contradictory legacy Methodology footer.
```

---
Dependencies: AIDE_Dependencies@v2, AIDE_Migration@v1, AIDE_Tags@v1, AIDE_WorkPackage@v1
References: Core_System_Design_v4
