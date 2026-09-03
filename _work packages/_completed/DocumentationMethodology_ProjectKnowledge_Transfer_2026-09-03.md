# Documentation Methodology — Project Knowledge Transfer

> **Purpose:** Preserve project-specific continuity knowledge that may exist in ChatGPT project/user context rather than in the Documentation Methodology authoritative masters or moved chat history.
>
> **Transfer status:** The substantive Documentation Methodology model is already represented by the moved current Binder/source corpus. This note is therefore intentionally limited to operating preferences, delivery conventions, and continuity rules that are useful to retain in the destination project.
>
> **Authority:** This is a project-context transfer note, not an authoritative AIDE master document. Where it conflicts with current authoritative Standards, Tools, Designs, Decisions, Guides, Indexes, or Working Practices, the authoritative corpus governs.

## 1. Change Delivery Packages

For future AIDE/documentation work, when producing a Change Delivery Package or ZIP:

- deliver the result as one ZIP containing all files created or changed by the work, using their final intended filenames;
- include a concise Change Delivery Instructions file inside the package by default, or provide equivalent clear application instructions in the response when a separate instructions file is not appropriate;
- for each affected file/project, state the required action clearly, including as applicable:
  - **Add** — new file and exact destination;
  - **Replace Current** — which current master it replaces;
  - **Move to `_superseded`** — which prior issued versions should be superseded;
  - **Archive / withdraw / remove** — where another lifecycle action is required;
  - **Rename / move / ownership change** — source and destination;
  - **Binder/Bundle changes** — which generated consumption artefacts must be regenerated/replaced;
  - **Project-context changes** — what should be added/removed/replaced in project context;
  - **Transfer-only artefacts** — identify files that are instructions/handoffs rather than masters.

The instructions document is a transfer/application artefact, not a master document.

## 2. Output cadence

Do not output changed masters or a Change Delivery Package after every individual confirmed change by default.

Instead:

- accumulate/queue confirmed changes during a meaningful unit of work;
- issue files/packages at the end of a significant work unit, work session, completion/checkpoint, or when explicitly requested with wording such as `output updates`, `update docs`, or `build change file/package`;
- avoid unnecessary version/package churn;
- do not allow valuable confirmed work to remain at material risk of loss merely to avoid output churn.

## 3. Cross-topic changes

When a confirmed change affects another AIDE topic:

- if the current authoritative Binder/source context for that topic is available and sufficient to edit it safely, apply the required changes directly to that topic's authoritative masters and include them in the same appropriate change package;
- do **not** create a Project Handoff merely because ownership crosses a topic boundary when direct authoritative editing is safely possible;
- use a **Project Handoff** when the target topic cannot be safely edited from the available authoritative context, or when a genuine transfer boundary requires one.

This is an operating preference intended to reduce unnecessary handoff ceremony while preserving ownership boundaries.

## 4. Physical repository / management-folder convention

The retained practical convention is:

- structural/management folders use an underscore prefix;
- `superseded` is `_superseded`;
- `archived` is `_archived`;
- Change Delivery Packages are staged in:
  - `Documentation/_changeDeliveryPackages/`
  - then moved to `Documentation/_changeDeliveryPackages/_completed/`;
- completed/history management material may periodically be archived outside the active repository.

These are physical workflow conventions, not the semantic definitions of Current/Superseded/Archived.

## 5. Binder handling

Generated project Binders should:

- be versioned so the loaded project-context version is visible at a glance;
- live in the project's active/master folder rather than a separate generated folder;
- remain generated, read-only consumption artefacts rather than editable authoritative masters;
- move replaced Binder versions to `_superseded`;
- be regenerated from authoritative sources rather than edited directly.

## 6. Working style for AIDE documentation work

Retained preferences that may affect how future work should be handled:

- resolve routine, low-risk implementation/detail decisions independently;
- confirm design-shaping or high-impact decisions rather than silently choosing them;
- keep generated metadata and machine-oriented content compact in human-readable documents;
- for review work, prefer a concise orientation covering purpose/requirements/model and the review approach, followed by findings/outcomes rather than a long procedural narration.

## 7. Documentation Methodology ownership stance

A durable design stance retained from earlier work is:

- Documentation Methodology should own **generic, cross-document methodology**;
- capability-specific document semantics/types should remain with their owning capability unless they are genuinely shared enough to become common methodology;
- Documentation Methodology should define the common document model, document-type framework, shared lifecycle/versioning/metadata/container behaviour, and cross-document usage rules without absorbing another capability's substantive semantics.

The current authoritative corpus should be used to interpret the exact present-day boundary.

## 8. Known project continuation state

At the time of this transfer:

- the recent Documentation Methodology Review A and Review B correction/remediation work recorded in this project's conversation history had been completed/applied;
- the top-level-topic WIP naming correction had been incorporated into the current methodology;
- no separate un-applied Documentation Methodology change is known from the retained project continuity context.

Do not infer that this statement replaces checking any live `WIP`, `Working`, `OpenItems`, or `WorkRegister` documents present in the destination project's sources.

## 9. Deliberately not transferred as current knowledge

An earlier exploratory proposal considered splitting Documentation Methodology into separate `Document Definition` and `Document Usage` Standards. This was a proposal, not an established current architecture, and is **not** transferred as a current requirement.

Likewise, older project-context statements naming obsolete versions of AIDE Standards/Tools should not be preserved as current instructions. Resolve current versions from the authoritative destination corpus.

---

**Recommended destination treatment:** Add this note to destination project knowledge/context as non-authoritative continuity guidance. Do not add it to the Documentation Methodology master corpus unless a future design decision deliberately promotes one of these operating preferences into an authoritative owner.
