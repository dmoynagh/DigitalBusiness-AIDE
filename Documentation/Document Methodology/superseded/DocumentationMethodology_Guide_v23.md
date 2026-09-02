# Documentation & Workflow Methodology — Guide

> **Identity:** `AIDE_DocumentationMethodology@v23`
> **Version 23** (2026-09-01). Review A R2 preflight correction: advances current generic Index
> consumption/conformance to `AIDE_Index@v2` while preserving the v22 DocumentationTopic/WIP model.
>
> **Migration posture:** None for v23. This current-contract reference/conformance correction requires
> no consumer content transformation.

## v23 change summary

- **Generic Index current contract.** Core `AIDE_Index@v2` owns generic Item/Item Type/hierarchy/
  extension hosting. Documentation Methodology owns documentation-specific Index sections and the
  `DocumentationTopic` top-level-topic type.
- **DocumentationTopic is a logical top-level-topic boundary.** Its governing Index declares/
  describes and resolves the Item; the Markdown Index file is not itself the semantic boundary.
- **One WIP series per top-level topic.** Use `{TopLevelTopic}_WIP_vN`; keep concurrent thread
  identity inside that WIP rather than creating subtopic-specific WIP series.
- **Top-level topic is the semantic anchor.** A chat project/master folder is a container and may
  hold several top-level topics.
- **WIP is now a distinct DocType.** It preserves volatile current work context cheaply across
  interruptions, sessions and platforms.
- **Working stays distinct.** It is substantial exploratory/formative material that may live much
  longer and may precede any Design.
- **OpenItems is live-only.** Resolved items leave the register rather than accumulating as history.
- **WorkRegister is the undelivered-design-consequence ledger.** It links committed Design to actual
  implementation/output and tracks WorkPackage allocation/return until delivered.
- **Normal Binders exclude WIP, Working, OpenItems and WorkRegister.** Load live state separately.
- **Messaging owns Message schema/semantics.** DocMeth supplies only generic governed-file
  integration for persisted messages.

## 1. The core rule: route information by state

The methodology is easiest to use if each document answers a different question:

| State | Document | Main question |
|---|---|---|
| Current volatile context | `WIP` | What do I need to continue this active work safely? |
| Substantial exploration | `Working` | What thinking/material is being developed before its final home is known? |
| Live attention | `OpenItems` | What still needs attention/revisit/thought? |
| Confirmed model | `Design` | What is the current confirmed position? |
| Reasoning/history | `Decisions` | Why did the confirmed position become this? |
| Confirmed undelivered work | `WorkRegister` | What committed consequence is still owed? |
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

Use WIP to preserve **the current working context** when losing the conversation/session/platform
cache would make continuation materially harder.

Typical content:

```text
Current position
Current thread/problem
Important reasoning not yet represented elsewhere
Draft fragments/candidate wording
Candidate OpenItems
Candidate WorkRegister consequences
Relevant source pointers
Resume from here
```

WIP can be rough. It is allowed to duplicate content temporarily because its job is safe
continuation, not authoritative publication.

### When to checkpoint

Useful triggers include:

- before ending a material work session;
- before switching chats/projects/platforms;
- before changing to unrelated work likely to displace context;
- after a substantial reasoning block not yet represented durably;
- when an AI judges context loss/eviction would be costly; or
- when the user explicitly wants a current physical context file.

Do not update on every conversational turn merely because WIP exists.

### Versioning

Visible filename versioning is intentional:

```text
Capabilities_WIP_v5.md
```

It lets a person or AI verify that the file loaded into a project/context is the latest issued
checkpoint even when the UI does not make replacement/sync state obvious.

Edit freely inside the current context. When issuing a new checkpoint for reuse/sync/resumption,
increment `_vN`; the previous checkpoint becomes Superseded.

There is one current WIP series for the top-level topic. If several threads are active at once, keep
them inside that file, for example:

```markdown
## Active thread — Messaging
...

## Active thread — Architecture Review A
...
```

Do not create `Capabilities_Messaging_WIP_vN` or similar independent subtopic WIP series. This
restriction is specific to WIP; a substantial subtopic may still have its own Working document, and
OpenItems/WorkRegister may still use their separately defined delegation rules.

### End of WIP

At a useful checkpoint route its contents:

```text
still unresolved and durable → OpenItems
large coherent exploration   → Working
confirmed model              → Design
material reasoning           → Decisions
confirmed work owed          → WorkRegister
transient/no longer useful   → discard
```

Once the WIP has no continuation value, withdraw/dispose it. Archive only exceptionally where the
WIP itself has unusual independent historical value.

## 5. Working — substantial exploratory/formative work

Working is **not simply Design in progress**.

It is a substantial body of thinking/material that has become worth preserving independently while
its eventual authoritative form may still be unknown.

Examples:

- an idea worked over several sessions before a Brief exists;
- a concept/review response that may later split across Design and Decisions;
- research plus emerging model not ready to commit;
- a substantial proposal whose eventual document class is not yet clear.

Working can last days/weeks/months. It may be repeatedly reworked, split and reframed.

When it resolves:

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
2. create WorkRegister consequence if confirmed delivery remains; and
3. remove the OpenItem.

Do **not** retain closed rows, strikethrough archives or a permanent closed-items section merely for
history. Git/file history can answer forensic questions; the live register should answer what still
needs attention now.

If identifiers are used, non-reuse is a reasonable local convention for stale-reference safety but
is not a v21 requirement.

## 7. WorkRegister — confirmed work and undelivered Design consequences

WorkRegister answers:

> **What have we already committed to that is not yet fully delivered?**

This is stronger than a generic backlog.

### Hard Design consequence rule

Whenever confirmed Design changes, ask:

```text
Does this change require any downstream code/build/document/production outcome to change?
```

If no: nothing is owed.

If yes:

```text
fully delivered in the same pass? → done
not fully delivered?              → WorkRegister
```

There is no safe third state where Design says one thing and production silently remains on an
older outcome with no record of the gap.

### Entry depth

The entry must be detailed enough to reconcile delivery later. A useful shape is:

```markdown
## WR23 — Implement revised equality semantics

Status: In progress

Source:
Json_Design — equality section / decision reference

Committed design change:
Unknown properties are preserved but excluded from semantic equality unless recognised.

Required outcome changes:
- Update equality comparer.
- Update hash-code behaviour.
- Add/modify tests.
- Review diff semantics for consistency.

WorkPackages:
- WP-31 — comparer + tests — Complete
- WP-34 — diff review — Pending

Returned result:
WP-31 completed comparer/tests successfully.

Remaining:
Diff semantics still require reconciliation.
```

Do not make the WorkRegister duplicate the full implementation plan. It records the **obligation
and delivery reconciliation**, while WorkPackage owns the bounded execution contract.

### WorkPackage mapping

One WorkPackage can cover several WorkRegister items to create a manageable work chunk.

One large WorkRegister item can be delivered through several WorkPackages.

The package should identify the relevant item IDs and which portion of each obligation it covers.

On Outcome return, the director reconciles the register:

- fully delivered → remove item;
- partial → record returned result and remaining work;
- blocked → record blocker/remaining; or
- design problem → return to Project Design, then revise/re-authorise work appropriately.

The closed WorkRegister row is not retained merely as history. Durable Design/Decisions/Outcome
records already own what should survive.

## 8. Design and Decisions

Design remains the current confirmed answer.

Decisions records synthesized reasoning needed to understand why that answer exists and what
credible alternatives were rejected. It is not a transcript and is not an input to downstream
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

When resuming work, load the Binder **plus** the relevant live-state files.

### Do not make the Index a back door for WIP churn

If every `Capabilities_WIP_v5 → v6` checkpoint forced the Index to update its Document
Register, and every Index update forced a Binder rebuild, excluding WIP from Binder would achieve
nothing.

So live-state documents use a deliberately lighter Index relationship:

```text
stable Document Register
    → authoritative/stable corpus documents

optional Live state section
    → active series/locator, version-agnostic
```

Example:

```markdown
### Live state

- `Capabilities_WIP` — current top-level-topic continuation checkpoint.
- `Capabilities_OpenItems` — live attention register.
```

The current issued version is read from the actually available file (`..._v7.md`), not inferred
from an old Index row. Reissuing `_v7` as `_v8` in the same series therefore does **not** require an
Index or Binder issue.

Creation/withdrawal of a live-state series is reconciled at the next normal corpus/output
checkpoint. The generic Index contract permits this because an Index registers significant Items;
it does not have to enumerate every physical file.

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

## 13. Migration to v23

v23 has posture `None`.

Do not mass-rewrite current documents simply because:

- the generic Index owner moved to Core;
- the conceptual filename slot is now called TopLevelTopic instead of Project;
- `DocumentationTopic` was clarified as a logical Item declared by its governing Index; or
- the WIP series rule was corrected.

Do not mass-rename historical or Superseded subtopic-named WIP files. New/current continuity
checkpoints use the single `{TopLevelTopic}_WIP_vN` series.

When an existing governed document is next substantively updated, use the current v23 model under
normal Dependencies/Migration behaviour. v23 itself requires no consumer content transformation.

## 14. Practical summary

Use this small mental model:

```text
Don't lose current thinking       → WIP
Substantial thinking needs a home → Working
Don't forget unresolved attention → OpenItems
Confirmed answer                  → Design
Why                               → Decisions
Confirmed delivery still owed     → WorkRegister
Execute a manageable chunk        → WorkPackage
What actually happened            → Outcome
What exists / where to go         → Index
```

That separation is the point. It lets the system preserve knowledge without making every document a
history, queue, scratchpad and source of truth at the same time.

---
Dependencies: AIDE_Index@v2, AIDE_Dependencies@v2, AIDE_Migration@v1, AIDE_WorkPackage@v2
References: DocumentationMethodology_Design_v20, AIDE_DocumentationMethodology@v23, WorkingPractices_Design_v5
