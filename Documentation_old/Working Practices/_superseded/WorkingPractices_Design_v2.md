# Working Practices — Design

> **Version 2** (2026-08-31). Reissued against current Core/Documentation Methodology, establishes
> the canonical Standard and adds current-Binder checking before cross-project master changes.
>
> Created: 2026-08-31 | Last modified: 2026-08-31

## §1 — Purpose

Working Practices defines the practical cross-cutting conventions used when an AI and user work
together.

It answers:

> How should work be approached, communicated, completed and handed over in practice?

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

Working Practices tells the AI **how to work with the user**.

It does not take semantic ownership from specialised components.

Examples:

```text
Documentation Methodology
  defines Current / superseded / archived and document version/lifecycle rules.

Working Practices
  requires a delivery handoff to tell the user which files/actions apply.

AI Deployment
  defines deployment reconciliation/verification.

Working Practices
  requires deployment handoffs to distinguish generated intent from confirmed deployed state.

Core/Domain
  defines Domain resolution.

Working Practices
  may require checking the current owning-project Binder before cross-project edits.
```

## §4 — Base guidance and Guidance Profiles

`AIDE_WorkingPractices@v1` is the portable base.

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
- prior issued versions moving to `superseded/`;
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

### WP8 — Preserve durable handoff when work moves

When substantial confirmed work moves to another project, session, environment or responsible
owner, provide a compact handoff containing:

- authoritative source artefacts;
- confirmed model/decisions;
- what remains to be done;
- important deferred/non-goals; and
- application/integration instructions.

A handoff summary is transfer material unless the destination explicitly adopts it as a master.

Once integrated, stale handoff summaries should not remain in ongoing project context beside the
authoritative sources unless they still have an active purpose.

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
AIDE_WorkingPractices@v1
```

The Standard should be concise, operational and platform-neutral. Rich examples remain in Design
or future Guide material rather than bloating base guidance.

---
Dependencies: !AIDE_DocumentationMethodology@v19
References: WorkingPractices_Decisions_v2, Principles_Design_v3, Core_Bootstrap_Design_v2
