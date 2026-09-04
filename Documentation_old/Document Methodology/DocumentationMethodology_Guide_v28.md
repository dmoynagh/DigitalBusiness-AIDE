# Documentation & Workflow Methodology — Guide

> **Identity:** `AIDE_DocumentationMethodology@v28`
> **Version 28** (2026-09-02). Adds dual-audience Contents/Summary guidance and the Overview escalation boundary.

## Contents

- **Current release and core model** — what v28 changes and how information is routed by state. §1
- **Topic structure and naming** — container/topic boundaries and governed filenames. §2–§3
- **Live work documents** — WIP, Working, OpenItems and WorkRegister usage. §4–§7
- **Confirmed knowledge and navigation** — Design/Decisions, Index extensions and Binder/live-state discovery. §8–§10
- **Ownership, lifecycle and migration** — Messaging boundary, disposition and adoption posture. §11–§13
- **Practical operating model** — compact routing summary. §14
- **Semantic sections and orientation** — host authority, Knowledge, Binder navigation, Contents, Summary and Overview. §18–§19

## Summary

Documentation Methodology gives each kind of documentation information a distinct role: WIP
preserves volatile continuation, Working holds substantial exploration, OpenItems preserves live
unresolved attention, Design states the confirmed position, Decisions records its reasoning,
WorkRegister tracks confirmed work owed, and WorkPackage/Outcome bound and report execution.

The top-level Documentation Topic and its Index provide the structural navigation boundary.
Authoritative masters remain primary; Binders are generated context artefacts. Semantic sections
can live in different permitted hosts while retaining one authoritative instance.

For suitable substantial documents, a curated Contents section provides a quick map of significant
information and stable locations, followed by a Summary that explains the document's high-level
substance. DocType owners decide whether these sections apply and how deep they should be. They are
used only where they improve human and machine comprehension/navigation without adding distracting
clutter or compromising the document's function. Overview remains a separate optional high-level
document for explicit user need or cases where an adequate Summary would become disproportionate.

## v28 change summary

- **Contents is a semantic map.** It describes significant information and stable section locations
  for both human navigation and machine search/selective loading; it does not repeat every heading.
- **Summary is a real high-level representation.** Its coverage is DocType-defined and may be more
  substantial where the body is complex, but remains cheaper to consume and subordinate to the
  detailed authority.
- **Applicability is value-based.** Contents/Summary are omitted when they add clutter, duplicate an
  equivalent structure or compromise function, readability or usability.
- **Overview stays independent.** It may be explicitly requested or created when a substantial
  high-level representation deserves its own document; a current Overview may reduce, but not erase,
  a related Design's minimum Summary role.

## Earlier v24–v26 reconciliation summary

- **Round 2 closing references corrected.** The canonical Standard now uses `AIDE_Build@v5` in its
  current WorkPackage integration instruction and `AIDE_Review@v2` in its current Review document
  integration instruction.
- **D41 is refined, not rewritten.** D41 remains the historical R1 event; D42 records that its
  five-master verification claim was too broad and states the narrower result actually established.
- **No general policy is introduced.** Footer dependency/reference currency and the broader
  in-body-version/conformance relationship remain reserved for Review C / Dependencies.

- **Coordinated WorkPackage seam corrected.** `AIDE_WorkPackage@v3` now explicitly carries the
  deterministic-enough split-obligation `Covers` rule. This adds no new mechanism or structured
  sub-obligation identifier system and does not change the WorkRegister/WorkPackage ownership boundary.
- **WorkRegister admission is general but bounded.** It holds confirmed work owed by the owning
  top-level topic and not yet fully delivered; ideas/unconfirmed/unresolved matters remain elsewhere.
  Confirmed Design consequences remain a mandatory producer subset.
- **WIP threads now have an exit rule.** Remove a routed `Active thread — ...` section from the next
  checkpoint; withdraw the whole WIP only after no active continuation thread remains.
- **Working is discoverable without Binder inclusion.** A new Working series gets a version-agnostic
  locator in the topic Index `Live state`; later versions do not churn the Index.
- **Returned is not reconciled.** Use `Returned — reconciliation pending` when an Outcome has arrived
  but owner reconciliation cannot be completed immediately; keep only compact reconciliation state
  in WorkRegister.
- **Split obligations stay simple.** Required changes are independently identifiable and WorkPackage
  `Covers` names the exact portions; no structured sub-obligation IDs are introduced.
- **Negative OpenItems do not create tombstones.** Preserve a material reusable negative conclusion
  in Decisions/another proper durable owner only when it could credibly be re-raised.
- **Ownership seam is explicit.** Documentation Methodology owns work-state semantics, routing,
  authority and Binder/live-state meaning; Working Practices owns operational checkpoint timing,
  transfer/sync and physical file/repository workflow.
- **Review C is not pre-empted.** Historical/stable version references were not rewritten and no new
  general in-body capability-version policy is created.

## 1. The core rule: route information by state

The methodology is easiest to use if each document answers a different question:

| State | Document | Main question |
|---|---|---|
| Current volatile context | `WIP` | What do I need to continue this active work safely? |
| Substantial exploration | `Working` | What thinking/material is being developed before its final home is known? |
| Live attention | `OpenItems` | What still needs attention/revisit/thought? |
| Confirmed model | `Design` | What is the current confirmed position? |
| Reasoning/history | `Decisions` | Why did the confirmed position become this? |
| Confirmed owed work | `WorkRegister` | What confirmed obligation is still not fully delivered? |
| Bounded execution | `WorkPackage` | What is Build authorised to deliver now? |
| Execution evidence | `Outcome` | What was actually delivered/observed? |
| Structural map | `Index` | What significant things are registered here and where? |

The most important practical test is:

> **Do not lose thinking, but do not turn every transient thought into permanent history.**

WIP is the cheap capture layer that makes those two goals compatible.

## 2. Container versus top-level topic

A **container** is a practical context/storage boundary: a chat project, master folder, workspace or
similar pool of shared material.

A container may hold more than one top-level topic because the topics benefit from the same context.
The container is therefore not automatically the semantic scope of registers.

Default structure:

```text
Container
├── Top-level Topic A
│   ├── Index/document set
│   ├── OpenItems
│   └── WorkRegister
└── Top-level Topic B
    ├── Index/document set
    ├── OpenItems
    └── WorkRegister
```

Many current AIDE containers happen to be 1:1. Do not turn that convenience into a rule.

## 3. Naming

Normal governed Markdown filename:

```text
{TopLevelTopic}_{Subtopic...}_{DocType}[_{Key}]_v{N}.md
```

Examples:

```text
Capabilities_Design_v9.md
Capabilities_Review_Design_v2.md
Capabilities_WIP_v3.md
Capabilities_Messaging_Working_v2.md
Core_WorkRegister_v1.md
```

The earlier methodology described the first slot as `{Project}`. Most existing filenames already
use the top-level topic there, so the conceptual correction normally requires no rename.

The version suffix is last. It counts issued/persisted outputs, not every edit.

## 4. WIP — current active work persistence

### Purpose

Use WIP to preserve **the current working context** when volatile context needs a persisted
continuation representation.

Typical content:

```text
Current position
Current thread/problem
Important reasoning not yet represented elsewhere
Draft fragments/candidate wording
Candidate OpenItems
Candidate WorkRegister obligations
Relevant source pointers
Resume from here
```

WIP can be rough. It is allowed to duplicate content temporarily because its job is safe
continuation, not authoritative publication.

### When to checkpoint

Documentation Methodology defines what WIP **is** and how an issued checkpoint is versioned; it does
not own operational checkpoint timing. `AIDE_WorkingPractices` defines practical triggers for when to
persist WIP, when to batch normal file output, and how to transfer/sync/verify context replacement.

The semantic rule here is simply: when the operating process decides that a WIP checkpoint is being
issued, treat it as an issued document checkpoint under the versioning rule below.

### Versioning

Visible filename versioning is intentional:

```text
Capabilities_WIP_v5.md
```

It distinguishes successive issued continuation checkpoints. Edit freely inside the current
context; when a new checkpoint is issued, increment `_vN`; the previous checkpoint becomes
Superseded. Transfer/sync mechanics and verification belong to Working Practices/environment.

There is one current WIP series for the top-level topic. If several threads are active at once, keep
them inside that file, for example:

```markdown
## Active thread — Messaging
...

## Active thread — Architecture Review B
...
```

Do not create `Capabilities_Messaging_WIP_vN` or similar independent subtopic WIP series. This
restriction is specific to WIP; a substantial subtopic may still have its own Working document, and
OpenItems/WorkRegister may still use their separately defined delegation rules.

### Thread exit and end of WIP

Route each thread's material according to state:

```text
still unresolved and durable → OpenItems
large coherent exploration   → Working
confirmed model              → Design
material reasoning           → Decisions
confirmed work owed          → WorkRegister
transient/no longer useful   → discard
```

When an `Active thread — ...` section's useful material is safely routed, remove that thread from
the **next** WIP checkpoint. Do not let routed material accumulate indefinitely beside active
continuation state.

Withdraw/dispose the whole WIP only when no active continuation thread remains. Archive only
exceptionally where the WIP itself has unusual independent historical value.

## 5. Working — substantial exploratory/formative work

Working is **not simply Design in progress**.

It is a substantial body of thinking/material that has become worth preserving independently while
its eventual authoritative form may still be unknown.

Examples:

- an idea worked over several sessions before a Brief exists;
- a concept/review response that may later split across Design and Decisions;
- research plus emerging model not ready to commit; or
- a substantial proposal whose eventual document class is not yet clear.

Working can persist across many work units. It may be repeatedly reworked, split and reframed.

When a **new Working series** is issued, add its version-agnostic series locator to the owning topic
Index `Live state` section, for example `Capabilities_Messaging_Working`. New-series issuance and the
locator are one semantic corpus change. This is required because a Working series can include
subtopic/key structure that cannot be derived reliably from the root topic name. Reissuing `_v2` as
`_v3` within that same series does not require another Index update. Remove/withdraw the locator when
the Working series ceases to be live.

This targeted locator rule does not make the normal Binder include Working and does not create a
complete live-state manifest for WIP/OpenItems/WorkRegister.

When Working resolves:

- move current confirmed state to the appropriate authoritative source;
- move material reasoning to Decisions where warranted;
- move remaining live attention to OpenItems;
- move confirmed delivery obligations to WorkRegister; then
- Supersede/withdraw Working if fully absorbed, or Archive it if the Working artefact itself remains
  independently valuable.

## 6. OpenItems — live durable attention

OpenItems answers:

> **What must not be forgotten and still needs attention?**

It may contain:

- open questions;
- current/pending/future tasks not yet confirmed delivery obligations;
- ideas/concepts not yet ready for Design;
- deferred concerns;
- investigations/reminders;
- pending review/message threads; and
- pointers to active WIP/Working.

Keep enough context to resume, but do not turn the register into a Working document.

### Scope

Default: one OpenItems register per top-level topic.

Create/delegate a subtopic register only when the amount/cadence of live state makes that easier to
use. Do not create one merely because a child topic exists.

### Closure

Every visible row means attention is still required.

When resolved:

1. preserve any genuinely durable outcome in its proper owner (Design/Decisions/etc.);
2. create a WorkRegister obligation if confirmed delivery remains; and
3. remove the OpenItem.

A conclusion of **no change** does not justify keeping a tombstone. If the negative conclusion and
reason are material and could credibly be raised again, preserve the conclusion first in Decisions
(or another genuinely proper durable owner) and then remove the OpenItem. If not, remove it with no
durable history.

Do **not** retain closed rows, strikethrough archives or a permanent closed-items section merely for
history. Repository/file history may support forensic questions, but the live register answers what
still needs attention now.

If identifiers are used, non-reuse is a reasonable local convention for stale-reference safety but
is not a v24 requirement.

## 7. WorkRegister — confirmed work owed and delivery reconciliation

WorkRegister answers:

> **What work has this top-level topic genuinely committed/owes that is not yet fully delivered?**

This is broader than Design consequences but narrower than a generic backlog.

### Admission rule

Put an item in WorkRegister only when the work is genuinely **confirmed/committed/owed** and some of
that owed result remains undelivered.

Do **not** put these in WorkRegister merely because they may matter later:

- ideas or possible future work;
- unconfirmed Review findings;
- unresolved questions/concerns still requiring judgment; or
- speculative improvements.

Those belong in OpenItems/Working/another appropriate live state until the owning topic actually
commits the work.

### Hard Design consequence producer rule

Whenever confirmed Design changes, ask:

```text
Does this change require any downstream code/build/document/production outcome to change?
```

If no: nothing is owed from that Design change.

If yes:

```text
fully delivered in the same pass? → done
not fully delivered?              → WorkRegister
```

There is no safe third state where Design says one thing and production silently remains on an
older outcome with no record of the gap. This is a **mandatory producer rule**, not the whole
WorkRegister definition.

### Entry depth

The entry must be detailed enough to reconcile delivery later. A useful shape is:

```markdown
## WR23 — Implement revised equality semantics

Status: In progress

Source:
Json_Design — equality section / decision reference

Confirmed obligation:
Deliver the revised equality semantics across implementation, tests and related documentation.

Required outcome changes:
- Update equality comparer.
- Update hash-code behaviour.
- Add/modify tests.
- Review diff semantics for consistency.

WorkPackages:
- WP-31 — Covers: equality comparer; tests — Complete
- WP-34 — Covers: diff semantics review — Returned — reconciliation pending

Returned result:
WP-34 / Outcome-34 — Complete; diff review found no additional implementation change.

Remaining:
Owner reconciliation of the diff conclusion is still required.
```

Do not make WorkRegister duplicate the full implementation plan or Outcome evidence. It records the
**obligation and reconciliation state**.

If one obligation will be split across several WorkPackages, write the required changes so the
portions are independently identifiable—normally bullets like the example. Each WorkPackage
`Covers` mapping names the exact claimed portions. `AIDE_WorkPackage@v3` now makes that
deterministic-enough mapping rule explicit. No extra sub-obligation identifier scheme is needed.

### Return and reconciliation

A returned Outcome and a reconciled obligation are distinct states.

If a mapped Outcome arrives and the owner cannot complete full reconciliation in the same
uninterrupted step, update the mapping/equivalent compact state first to:

```text
Returned — reconciliation pending
```

If reconciliation is immediate, do not persist that intermediate state ceremonially.

While the WorkRegister item remains open, keep only:

- current/terminal WorkPackage status;
- stable WorkPackage/Outcome reference;
- concise returned result where it helps reconciliation; and
- remaining obligation/blocker.

Detailed execution, validation and evidence stay in the WorkPackage Outcome. Reference them; do not
copy them into WorkRegister.

On reconciliation:

- fully delivered → remove item;
- partial → keep compact returned state plus remaining obligation;
- blocked → keep blocker/remaining obligation; or
- design problem → return to Project Design, then revise/re-authorise work appropriately.

The closed WorkRegister row is not retained merely as history. Durable Design/Decisions/Outcome
records already own what should survive.

## 8. Design and Decisions

Design/Definition/Standards/Tools hold the applicable current confirmed answer.

Decisions remains broad: it records topic/subtopic-specific thinking, investigation, working, alternatives, reasoning, knowledge and explicit decision history needed to understand how that answer evolved. It is not a transcript and is not an input to downstream
outcomes.

A Decisions event is owed for:

- substantive confirmed Design change;
- requirement established/materially revised; or
- credible rejected alternative a future reader could reasonably re-derive.

Editorial/formatting/metadata/migration/mechanical maintenance alone does not create a Decisions
event.

Produce substantive Design and Decisions reasoning together so the “what” and “why” do not become
separated by context loss.

## 9. Generic Index and documentation extensions

Generic Index is `AIDE_Index@v2` in Core.

Its minimum shape is:

```text
Index identity/scope
Contents — hierarchical significant Items
owner-defined extension sections
```

A generic Index is authoritative for its registrations and Index-owned facts, not for the internals
of every thing it lists.

### Documentation extensions

Documentation Methodology contributes, where applicable:

- topic declarations;
- Document Register;
- custom document type declarations;
- assets/unmanaged documentation records;
- rename/rehoming/dead-locator history; and
- local documentation configuration.

This means a documentation Index can look like:

```markdown
# Capabilities — Index

`{scope: "AIDE/Capabilities", type: DocumentationTopic}`

## Contents
...

## Documentation
### Top-level topics
...
### Document register
...
### Local configuration
...
```

### DocumentationTopic

`DocumentationTopic` is a semantic Item Type owned by Documentation Methodology. The Item is the
**logical boundary/scope of one top-level documentation topic**, not the chat project/master folder
that may happen to contain it and not the Markdown Index file itself.

The governing Index declares/describes the logical Item. For example:

```text
{scope: "AIDE/Capabilities", type: DocumentationTopic}
```

inside `Capabilities_Index_vN.md` means “this Index declares/describes the logical
`AIDE/Capabilities` top-level DocumentationTopic boundary.” Recognition can inspect that
authoritative declaration to identify the scope, and the topic then resolves its governing
Index/document register through it.

A repository/root Index can register a DocumentationTopic, give enough description/location to
select it, and stop. Where one physical container hosts several top-level topics, the Index may show
the container structurally with several distinct DocumentationTopic Items beneath it.

A subtopic is not promoted into a DocumentationTopic merely because it has separate Design,
Decisions or an Index section. Domain remains the only owner that decides whether
`DocumentationTopic` may establish/participate in Domain resolution; the type does not self-assign
Domain authority.

## 10. Binder, Index and live-state churn

A normal Binder answers:

> What stable/current knowledge should a consuming AI load for this topic?

That is different from:

> What are we actively working on right now?

Normal Binders therefore exclude:

- WIP;
- Working;
- OpenItems; and
- WorkRegister.

Load relevant live state separately when doing active work.

### Working locator without live-state manifest churn

Working needs one special discovery rule because its series name may contain subtopic/key structure
that cannot be derived from the top-level topic name.

When a new Working series is issued, add a version-agnostic locator to the topic Index:

```markdown
### Live state

- `Capabilities_Messaging_Working` — active Messaging exploratory Working series.
```

The current issued version is resolved from the actually available file, not stored as `_vN` in the
Index. Therefore `Capabilities_Messaging_Working_v2 → v3` does **not** require an Index/Binder issue.
When that Working series ceases to be live, remove/withdraw the locator.

This is deliberately **not** a requirement to enumerate WIP, OpenItems and WorkRegister as a
complete live-state manifest. Their individual live versions remain outside the stable Document
Register. A topic may still use locally useful owner-defined locators without implying completeness.

Documentation Methodology defines these semantic inclusion/discoverability rules, including that a
new Working-series issue carries its Index locator. Working Practices owns physical batching/
replacement, repository handling and context transfer/sync.

A specialised live-state Binder remains possible if a workflow deliberately needs one.

## 11. Message ownership

The existing AI-MESSAGE system has outgrown document-schema ownership by Documentation
Methodology.

Messaging owns:

- message type/envelope fields;
- identity/threading/revision semantics;
- source marking;
- receipt/reconciliation state;
- messaging commands/workflow; and
- light/heavy message persistence criteria.

Documentation Methodology only supplies generic governed-file behaviour when a message is promoted
to a file: version/lifecycle/metadata hosting and any common naming rules that Messaging chooses to
consume.

The Messaging capability is reconciled in its own pass; v21 establishes the ownership boundary.

## 12. Lifecycle and storage

Lifecycle is semantic:

- **Current** — authoritative for normal current use;
- **Superseded** — replaced/displaced older issue;
- **Archived** — type-specific terminal historical record.

Physical folders/storage do not create those states. Working Practices/environment decides how the
current repository realises them.

## 13. Migration through v28

v26, v27 and v28 have posture `None`.

Do not mass-rewrite current documents because of this Round 2 closing correction, the v25
pre-Round-2 correction, or the v24 work-state clarifications. Existing current
WIP/Working/OpenItems/WorkRegister artefacts adopt the v24/v25/v26 rules on their next relevant
substantive issue/update under normal Dependencies/Migration behaviour.

Do not mass-rename historical or Superseded subtopic-named WIP files. New/current continuity
checkpoints continue to use the single `{TopLevelTopic}_WIP_vN` series.

The pre-Round-2 correction updated the Review B R1 WorkPackage seam affected by the coordinated
Build/WorkPackage remediation. Round 2 then identified two additional current executable references
in the canonical Standard; v26 corrects them to `AIDE_Build@v5` and `AIDE_Review@v2`. D41 remains
unchanged as the R1 event and D42 records the narrower truthful verification scope. Historical
Decision references remain history, and footer `Dependencies:` / `References:` are not generally
swept merely for version currency. No general in-body capability-version or dependency-checkpoint
policy is established here; that relationship remains reserved for Review C / Dependencies.

v28 does not require a corpus-wide rewrite to add Contents or Summary. New documents and documents
undergoing a normal substantive update apply the orientation posture defined by their DocType when
it adds value.

## 14. Practical summary

Use this small mental model:

```text
Don't lose current thinking       → WIP
Substantial thinking needs a home → Working
Don't forget unresolved attention → OpenItems
Confirmed answer                  → Design
Why                               → Decisions
Confirmed work still owed         → WorkRegister
Execute a manageable chunk        → WorkPackage
What actually happened            → Outcome
What exists / where to go         → Index
```

That separation is the point. It lets the system preserve knowledge without making every document a
history, queue, scratchpad and source of truth at the same time.


## 18. Sections, Knowledge and Binder navigation

Treat a document as a host. Keep one authoritative instance of a semantic section; choose a compact
permitted host first and split it out only when size, lifecycle, retrieval, reuse or complexity pays
for the extra document.

Use Topic Knowledge for broad durable research/evidence that does not fit a particular subtopic's
Decisions. It is a library of intellectual assets, not a hidden rulebook. Stable `K` IDs make later
correction and curation practical.

Binders are for Documentation Topics. Start with one per top-level Topic; partition deliberately and
publish a small Binder-set map when context limits require it. Use Index to navigate structure and
current source; use Overview for the human TLDR.

## 19. Contents, Summary and Overview

When both orientation sections apply, use this reading order:

```text
Title and essential header
Contents — what is here and where?
Summary — what does this document establish?
Detailed body — full authority, reasoning and implementation detail
```

A useful Contents block normally groups related sections into a small set of descriptive entries.
Prefer section names/numbers that survive ordinary edits. Its test is whether a person or file-based
AI can decide quickly what to read next.

A useful Summary gives genuine high-level understanding rather than merely restating Purpose. Its
depth varies by DocType. A substantial Design may need several paragraphs, a compact model and key
logic; a short Standard or Tool may already be sufficiently self-explanatory and omit it.

Index, Decisions, WIP, WorkRegister, OpenItems and structured data normally do not use Summary.
Equivalent specialised structures can satisfy the same objective. If a Design cannot provide a
proportionate useful Summary without duplicating/bloating itself, create an Overview. A user or work
owner may also request an Overview directly. When one exists, keep the Design Summary concise but
sufficient for someone who opens the Design first.

---
Dependencies: AIDE_Index@v2, AIDE_Dependencies@v3, AIDE_Migration@v3, AIDE_WorkPackage@v3
References: DocumentationMethodology_Design_v25, AIDE_DocumentationMethodology@v28, WorkingPractices_Design_v5, AIDE_WorkingPractices
