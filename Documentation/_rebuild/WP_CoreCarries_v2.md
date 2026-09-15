# Carries to Core from the Working Practices design pass

Working document. Items confirmed during the WP design pass and subsequent FileOps review that require updates to Core documents. To be applied at next Core update or via FUP.

---

## Framework-wide requirements (additions to Core_Design)

### Definition of done

Every component, every piece of work, defines when it is done. The invariant: the completion bar must be testable or assessable. Core states the requirement; WP owns the block type definition (the mechanism consumers use); consumers fill it with their own content.

Source: settled WIP v22 (promoted from WP generic block to framework-wide requirement during WP design pass, D4).

### Assurance

Every component contributes to assurance — the justified confidence that the human's intent is reliably delivered and that anomalies, drift, errors, and misunderstandings are visible when they occur. The Assurance component owns the specific conventions and detection mechanisms; this requirement is the lens every component is designed through.

Source: WP design pass, D16.

## Ownership rules (addition to Core_Design)

### P6 — information holder decides the boundary

When a boundary question arises, the component that holds the information decides. This is a framework governance rule governing how components relate to each other — a sixth ownership rule alongside the existing five.

Source: moved from Principles to WP during the Principles design pass; moved from WP to Core during the WP design pass, D5.

## Core Structure (additions from FileOps dissolution, D17)

### Archived folder convention

One `_archived` folder at the documentation root. Files that are no longer active but worth keeping — retired references, completed reviews, outdated knowledge. Moving a file there removes it from binder scope (underscore-prefixed folders are outside AIDE processing) while keeping it in the repo and searchable.

Source: FileOps dissolution, D17. Originally in `WP_FileOps_Working_v1.md`.

### Git-as-history

Git is the version history. The `_superseded` folder pattern is dropped. When a new version lands, version-cleanup deletes the old version from the working tree and commits the deletion. Rollback means `git checkout` of the previous version.

Source: FileOps dissolution, D17. Originally in `WP_FileOps_Working_v1.md`. The mechanism side (version-cleanup performing the deletion and commit) is an Infrastructure concern, carried separately.

## Component map updates

### New component: Assurance

| Component | Purpose | Key boundaries |
|---|---|---|
| Assurance | Build justified trust in AI-assisted work by defining and evolving the conventions, structures, and detection mechanisms that ensure the human's intent is reliably delivered and that anomalies, drift, errors, and misunderstandings are visible when they occur. | Guidance role. Cross-cutting — every component contributes. Owns the human working model, verification behaviours, drift detection, anomalies channel, learning loop capture conventions. Does not own the substrate (WP), the premises (Principles), or the pattern analysis (Improvement). |

Placed in the Guidance role alongside Principles, Standards, and Tools.

### New component: Improvement

| Component | Purpose | Key boundaries |
|---|---|---|
| Improvement | Iterative improvement of the framework and working practices from accumulated learning, regardless of source (human or AI). | Owns the periodic pattern analysis of the learnings queue, escalation decisions, and the reviewer. Does not own the capture conventions (Assurance) or the scheduling mechanism (Orchestration). |

Component count: 13 → 15.

---

Version note: v2 — adds Core Structure carries from FileOps dissolution (archived folder convention, git-as-history). Adds Improvement to the component map. Updates Assurance boundaries to reflect learning loop. Component count updated to 15. 2026-09-15.
