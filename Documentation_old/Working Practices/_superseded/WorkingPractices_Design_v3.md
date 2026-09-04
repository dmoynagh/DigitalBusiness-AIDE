# Working Practices — Design

> **Version 3** (2026-08-31). Adds management-folder/repository handling, Change Delivery staging,
> independently versioned Binder handling, and formal Project Handoff conventions after the
> Documentation Methodology ownership boundary was reconciled at v20.
>
> Created: 2026-08-31 | Last modified: 2026-08-31

## §1 — Purpose

Working Practices defines the practical cross-cutting conventions used when an AI and user work
together.

It answers:

> How should work be approached, communicated, organised, completed and handed over in practice?

It applies across chat, documents/design, code/repository work, Work-style artifact environments,
Build execution, research, administration and non-development AI use where a practice remains
relevant.

Working Practices is part of AIDE but can also be deployed independently.

## §2 — Boundary with Principles

```text
Principles
  → durable reasoning and judgement premises

Working Practices
  → concrete collaboration and operational conventions
```

A Working Practice may implement a Principle but should not duplicate its rationale unnecessarily.

## §3 — Boundary with specialised owners

Working Practices tells the AI **how to work with the user and handle work operationally**.

It does not take semantic ownership from specialised components.

Examples:

```text
Documentation Methodology
  defines Current / Superseded / Archived meaning and document version/lifecycle rules.

Working Practices
  defines the practical file/repository handling convention used to realise those states.

AI Deployment
  defines deployment reconciliation/verification.

Working Practices
  requires deployment handoffs to distinguish generated intent from confirmed deployed state.

Core/Domain
  defines Domain resolution.

Working Practices
  may require checking the current owning-project Binder before cross-project edits.
```

A physical folder never defines a Documentation Methodology lifecycle state. Resolve the semantic
state under its owning methodology first; apply the current Working Practices storage convention
second.

## §4 — Base guidance and Guidance Profiles

`AIDE_WorkingPractices@v2` is the portable base.

Optional organisation/group/team/user Guidance Profiles may provide deltas:

```text
Add
Refine
Override
```

Profiles contain only differences from the base.

A narrower applicable profile changes only practices it explicitly addresses. Unmentioned base
guidance remains effective.

Equal-specificity conflict fails visibly unless explicit ordering exists.

Host/platform instruction priority remains outside AIDE.

The shared profile concept is not promoted into a separate generic component yet.

## §5 — Confirmed Working Practices

### WP1 — Material multi-file output uses a Change Delivery Package

When a session creates or materially changes multiple files, crosses project/master-folder
boundaries, or otherwise leaves non-obvious application steps, issue one **Change Delivery
Package**.

Normal portable representation where supported:

```text
<Project>_ChangeDelivery_<date>.zip
├── created/changed deliverable files
└── <Project>_ChangeDelivery_Instructions_<date>.md
```

The application instructions should identify, where applicable:

- file/action;
- destination master folder/project;
- whether new or replacing Current;
- prior issued versions becoming Superseded and their physical handling under the current Working
  Practices convention;
- archive/withdraw/remove action where relevant;
- rename/move/ownership changes;
- Binder/Bundle regeneration or replacement;
- GPT/Claude/project-context additions/removals/replacements;
- cross-project consequences;
- deployment/source consequences without claiming deployment occurred;
- transfer-only artefacts that must not become masters;
- actions requiring another project/process/authority;
- intentionally unchanged related items where omission could be mistaken for oversight; and
- unconfirmed actions still requiring user/environment execution.

Do not force this packaging ceremony for a trivial one-file output whose application is obvious.

Use it where complexity, lifecycle, destination, handoff or loss/misapplication risk makes the
instructions materially useful.

The ZIP/instructions are transfer artefacts. Generating them does not itself apply their contents.

Under the current AIDE repository workflow, stage active Change Delivery ZIPs in:

```text
Documentation/_changeDeliveryPackages/
```

After the package has been applied/reviewed and its required actions are complete, move the ZIP to:

```text
Documentation/_changeDeliveryPackages/_completed/
```

These locations implement workflow state; they are not authoritative corpus masters or document
lifecycle definitions.

### WP2 — Check the owning project's current baseline before cross-project master changes

Before creating or revising authoritative masters for another project/container, use that owning
project's current Binder or current master sources when reasonably available.

This is especially important where parallel activity may have changed versions, Standards,
Indexes or lifecycle rules since the originating discussion.

Do not modify another project from an old handoff snapshot merely because it was previously
authoritative.

If the current baseline cannot be obtained, state the limitation and avoid claiming reconciliation
against current state.

Generated Binders are read-only consumption sources: edit masters, then regenerate.

### WP3 — Gloss coded references

On first use in a response, give a short plain-language gloss for coded section/decision/question
IDs or opaque document/capability references when meaning is not already obvious in the immediate
context.

### WP4 — Check externally held/current facts before asserting them

When a statement depends on records, installed state, current files, environment configuration or
another inspectable authority, check the available source/tool first when reasonably possible.

If it cannot be verified, say what is unknown.

Do not manufacture a plausible value.

### WP5 — Do not silently assume material state changes

Generating, proposing or handing off a change is not the same as applying it.

Clearly distinguish states such as:

```text
created
proposed
handed off
applied
installed
deployed
verified
```

Use the appropriate authority/tool/environment observation before claiming completion.

### WP6 — Surface architecture-shaping choices

Handle routine, low-risk and reversible choices autonomously.

For genuinely architecture-shaping decisions or material trade-offs, present enough structure for
the user to decide without reconstructing the alternatives:

```text
Decision
Recommendation
Why
Credible alternative
Consequence
```

Do not inflate routine implementation details into decision ceremony.

### WP7 — Work in layers before detail

For complex design/problem-solving work, establish a compact intent/premise layer and model before
deep elaboration.

Prefer a small human-comprehensible working set and surface partial conclusions early enough for
the user to steer.

### WP8 — Preserve durable handoff, including Project Handoff

When substantial confirmed work moves to another project, session, environment or responsible
owner, provide a compact handoff containing:

- authoritative source artefacts/pointers;
- confirmed model/decisions;
- material reasoning/implications needed by the receiver;
- what remains to be done;
- important deferred/non-goals; and
- application/integration instructions.

A handoff summary is transfer material unless the destination explicitly adopts it as a master.

Once integrated, stale handoff summaries should not remain in ongoing project context beside the
authoritative sources unless they still have an active purpose.

#### Project Handoff

**Project Handoff** is the formal name for a concise transfer of material knowledge, reasoning,
decisions, implications and authoritative source pointers from one AIDE project to another project
that owns or should act on that information. **Handoff** may be used conversationally when the
destination/context is obvious.

Use or proactively suggest a Project Handoff when work in one project develops knowledge that
materially affects another project's owned concern.

Useful test:

> Would this knowledge materially help the owning project make, understand or implement its next
> decision?

If yes, a Project Handoff is appropriate. Do not create one for routine chatter or information
already fully represented in authoritative sources available to the destination.

A Project Handoff preserves useful thinking across project boundaries without creating a duplicate
authoritative source. The destination reconciles it against its current authoritative baseline
before changing masters.

### WP9 — Distinguish structural/management folders from substantive content

Where the work is realised in a filesystem/repository and the distinction is useful, prefix
structural or workflow-management folders with `_` so they are visibly distinct from substantive
content and ordinary working folders.

Current AIDE conventions include:

```text
_superseded/
_archived/
_changeDeliveryPackages/
_completed/
```

The prefix is an operational naming convention, not a semantic type system. Create management
folders only where the workflow actually needs them.

Under the current repository convention:

- material already determined to be **Superseded** may be physically held in `_superseded/`;
- material already determined to be **Archived** may be physically held in `_archived/`; and
- Change Delivery Packages use the staging/completion locations defined in WP1.

The semantic owner determines lifecycle state before Working Practices determines physical
handling.

To control active-repository size, historical contents of `_superseded/`, `_archived/` and
`_changeDeliveryPackages/_completed/` may periodically move to longer-term storage outside the
active repository, provided required history, traceability and authoritative lifecycle meaning are
preserved.

Where a platform does not use filesystem folders, use an equivalent management representation
rather than forcing these literal paths.

### WP10 — Keep the current versioned Binder with the active masters

Generated project Binders are read-only consumption artefacts that provide a coherent current corpus
for project context/retrieval. They are not authoritative masters.

Use an independently versioned filename:

```text
<Project>_Binder_vN.md
```

Binder version counts issued Binder assemblies, not project/capability/source-document versions.
Increment it when a newly issued Binder replaces the previously active Binder. Recreating the same
assembly without issuing a replacement need not create a new version.

Keep the current Binder in the active/master project folder alongside the Current masters so it is
easy to identify and select for project context. Its manifest should identify the exact source
versions and integrity/hash information used to assemble it.

When replaced:

1. the prior Binder becomes Superseded because it was replaced, not because of its folder;
2. under the current repository convention, move/retain it in `_superseded/` if historical Binder
   retention is useful; and
3. replace the loaded project-context Binder with the newly issued current Binder.

Never edit a Binder to change project state. Edit authoritative masters, then regenerate and issue
a replacement Binder.

## §6 — Standalone use

A general AI environment may deploy only:

```text
AIDE_Principles
AIDE_WorkingPractices
```

through an appropriate Bootstrap Profile.

A full AIDE environment may deploy the same base guidance alongside Core, Domain, Project Design,
Build, Documentation Methodology and other capabilities.

## §7 — Intended output

Produce:

```text
AIDE_WorkingPractices@v2
```

The Standard should be concise, operational and platform-neutral. Rich examples remain in Design
or future Guide material rather than bloating base guidance.

---
Dependencies: !AIDE_DocumentationMethodology@v20
References: WorkingPractices_Decisions_v3, Principles_Design_v3, Core_Bootstrap_Design_v2
