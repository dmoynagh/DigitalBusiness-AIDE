AIDE Documentation | WIP | AIDE_Documentation_WIP@v15 | 2026-09-15

## Active threads

### DocMeth — schema review across components

All components owning doctypes or block types must define them using the accepted definition contract. The definition contract has been simplified in the rebuild (6 blocktype properties, 4 doctype properties). Assessment produced (DocMeth_Schema_Review_v1) — rework is a separate task per component.

Note: PD_Schema_Standard_v1 was authored against the old Schema Standard v4 property vocabulary. It should be reviewed against the simplified contract in DocumentationMethodology_SchemaAuthoring_Standard_v1 when next worked. Core_Schema_Standard_v2 is provisional and will be reviewed when Core's design pass is done.

### WP — remaining items

Old-material pass (WP1–WP13 from old corpus) not yet run — required before WP can be called complete per the rebuild method and F10.

WP schema definitions not yet written — doctypes (WIP, working document, report, resource) and block types (work item, work plan) need formal definitions per the documentation methodology schema contract.

---

## Completed — Project Design

### PD standard update — design-approach content — DONE

PD Standard v4 deployed 2026-09-14. Design-approach content folded in: two-part design structure (PD-F1), approach completeness check and element quality check as application-time guidance, operations test, context rule and derive-from-model, difficulty-as-evidence in the commitment-and-return loop. Brief-required gate made explicit with override. Overview section strengthened. DocMeth definition-contract and schema-placement pointers added (PD-F2, PD-F3). aide-design-check skill regenerated from the updated standard.

Cross-reviewed — ten findings, all resolved. PD Design v3, Decisions v3, Standard v4 all accepted.

### PD standard update — brief rule — DONE

Included in PD Standard v4 above.

---

## Completed — Principles

### Principles premise strengthenings — DONE

Completed 2026-09-15. Three candidate premise strengthenings from the design-approach work, all resolved as strengthenings of existing premises per F12 pattern. Premise count stays at nine.

P3 (model before elaboration) strengthened: difficulty-as-evidence feedback signal and apparatus-avoidance failure mode (D10). P4 (keep the working set human-comprehensible) strengthened: proportionality signal (D11).

Cross-review: F1 remediated (false-exclusive removed from difficulty signal), F2 remediated (positive injunction → naming the form), F3 remediated (universal causation → warning signal). Deployed: Principles_Design v5, Principles_Decisions v5, Principles_Standard v2.

---

## Completed — Standards

### Clarification block — DONE

Carry from DocMeth resolved by existing definition. The Standards Authoring Standard (v8 schema definitions section) already defines the Clarification blocktype — purpose, recognition, and split test governance — and includes it as optional in the Standard doctype. Definition-contract compliant. No design work needed. 2026-09-15.

---

## Completed — Documentation Methodology

### DocMeth — binder rebuild — DONE

Three superseded draft standards removed from the binder. The naming convention changed between drafts (`DocMeth_` prefix) and published v1 standards (`DocumentationMethodology_` prefix), so version cleanup didn't catch them. Files moved to `_superseded/`, binder rebuilt v64 → v65. Commit `f040d4b`. 2026-09-15.

---

## Completed — Working Practices

### WP design pass — brief, design, decisions — DONE

Completed 2026-09-15. WP_Brief_v1, WP_Design_v1, WP_Decisions_v1 authored. Check 1 passed with noted gaps (FileOps parked, lifecycle modes thin, old-material pass pending).

Key outcomes:
- Assurance extracted as a new top-level component (Guidance role) and framework-wide requirement in Core (D1, D16)
- Capture-and-place elevated to WP component level with proactive knowledge preservation (D12)
- Workflow commands replace session-transition commands as broader concept (D11)
- Working State absorbs Work Lifecycle (D3) — WIP three-role model, work items, work plan with named workstreams, pending content
- Capture and Organisation dissolved — content moved to WP component level and Working State (D2)
- Human-AI Collaboration dissolved — content moved to Assurance component (D1)
- Definition of done elevated to Core framework-wide requirement (D4)
- P6 moved to Core as sixth ownership rule (D5)
- Guidance Profiles deferred — no demonstrated consumer for solo developer (D6)
- Overview-first working behaviour owned by WP generic, PD consumes (D7)
- Verification behaviours placed in Assurance (D8)
- FileOps dissolved — content redistributed to WP component level, Core Structure, Infrastructure, and Build (D17, superseding D14)

Seventeen decisions recorded (D1–D17). FileOps dissolved (D17) — content redistributed to WP component level, Core Structure, Infrastructure, and Build. Pending: old-material pass, schema definitions, standard authoring.

---

## Pending — Core

### Component alias uniqueness

Component names and aliases must be unique within the framework. Aliases are used as type-reference prefixes in the dot-qualified naming grammar (`pd.brief`). Core Structure owns this rule.

### Carries from WP design pass

Items to add to Core_Design (detailed in `_rebuild/WP_CoreCarries_v2.md`):

1. **Definition of done** — framework-wide requirement. Invariant: testable or assessable. WP owns the block type; consumers fill content.
2. **Assurance** — framework-wide requirement. Every component contributes to assurance.
3. **P6** — sixth ownership rule. Information holder decides the boundary.
4. **Assurance** — new component in the Guidance role added to the component map. Component count 13 → 15 (Assurance + Improvement).
5. **Archived folder convention** — one `_archived` folder at the documentation root; underscore prefix removes from binder scope; files remain in the repo and searchable. (From FileOps dissolution, D17.)
6. **Git-as-history** — git is the version history; the `_superseded` folder pattern is dropped. Rollback means `git checkout` of the previous version. (From FileOps dissolution, D17.)

---

## Pending — Assurance (NEW COMPONENT — next in queue)

Guidance role. Brief sketch expanded to v2 in `_rebuild/Assurance_Brief_Sketch_v2.md`.

**Purpose:** Build justified trust in AI-assisted work by defining and evolving the conventions, structures, and detection mechanisms that ensure the human's intent is reliably delivered and that anomalies, drift, errors, and misunderstandings are visible when they occur.

**Scope correction (2026-09-15):** Assurance runs the full lifecycle from first conversational concept through to delivery, not primarily a build-side concern. The quality of the top two design levels carries a near one-to-one relationship with everything downstream. Assurance protects the highest-leverage work first.

**Three areas of concern:** proactive conventions (human working model, overview-first discipline), detective conventions (verification, drift detection, anomalies channel), and the learning and feedback loop (measurable moments, A-B comparisons, learnings queue, two escalation triggers).

**Learning loop additions (2026-09-15):** AI-initiated background comparison at measurable moments; learnings queue distinct from the task queue; two escalation triggers (single high-impact instance, or accumulated pattern); threshold and frequency tunable. The Improvement component (see below) owns the periodic pattern analysis; Assurance owns the capture conventions.

**Confirmed design decisions (to review at full design pass):** Named tiers for autonomy, anomalies channel as behaviour with capture-and-place destination, confidence uses existing framework strength vocabulary, learnings queue distinct from task queue, two escalation triggers.

**Design pass is next** — Assurance moved ahead of Messaging in the work queue because it is the framework's primary objective (O1) and the cross-cutting lens later passes should be designed through.

---

## Pending — Infrastructure

### Carries from FileOps dissolution (D17)

- **Utility git commit behaviour** — utilities stage and commit their own changes with descriptive messages. When the file-update-package applies an update, or version-cleanup removes an old file, or the binder builder regenerates, the utility stages changes and commits with a clear message. Carry to the relevant utility design documents.
- **FUP move action** — the file-update-package needs a move/rename action for when a document's path changes. Header updated, manifest records old and new path. Extends the existing action vocabulary (create, replace) with move. Carry to the FUP design document.
- **Version-cleanup deletion mechanism** — when a new version lands, version-cleanup deletes the old file from the working tree and commits the deletion with a descriptive message. Carry to the version-cleanup design document.

### FUP manifest — `user_instructions` field clarification

The `user_instructions` field is only for tasks the user must do outside the AI platform. All client-side instructions are presented in chat alongside the FUP. Carry to the FUP design document.

### FUP deployer — user_instructions display order

The `user_instructions` message should display after the deploy success statement, not before the deploy prompt. Log for Code session.

---

## Pending — Build (NOT YET STARTED)

### Seed material

`_rebuild/Build_Input_Working_v1.md` — the design-build separation principle (leaning, not a rule) and the concrete near-term question of where AIDE's own framework outputs go. From FileOps dissolution (D17).

---

## Pending — Improvement (NEW COMPONENT — identified, not yet scoped)

Iterative improvement of the framework and working practices, regardless of source (human or AI). Owns the pattern analysis, periodic review of the learnings queue, and the decision about what to act on.

**Boundary with Assurance:** Assurance identifies measurable moments and captures learnings to the queue. Improvement analyses the queue, finds patterns, and decides what to act on. The learnings queue is the interface between them.

**Boundary with Orchestration:** Orchestration provides the mechanism to run the reviewer on a schedule. Improvement owns the business logic — what the reviewer does, what counts as a pattern, when to escalate.

**Working-direction name:** Improvement (plain, direct, source-agnostic).

**Component count:** 14 → 15.

---

## Pending — Submission queues

### Task queue — frictionless capture path to AIDE development

AIDE needs a mechanism for submitting tasks, additions, changes and new functionality from work sessions into an AIDE development queue. The charter's frictionless capture principle governs the design.

**Concept.** Work side: single action on any surface, no triage required. AIDE development side: queue reviewed, triaged, worked through the normal design-build-deploy cycle.

**Preferred mechanism.** An MCP server callable from any AI surface, writing to a queue document in the AIDE git repo.

### Learnings queue — feedback from work outcomes

A distinct queue from the task queue. Holds raw observations from A-B comparisons at measurable moments. AI-initiated, written in the background when significant. Most entries sit and wait for aggregate analysis.

**Two escalation triggers:** a single high-impact instance escalates to the task queue immediately; accumulated patterns surface during periodic review by the Improvement component's reviewer.

**Mechanism:** same MCP as the task queue, writing to a separate queue document. The AI can write to it unprompted.

**Ownership:** the queue mechanism is Infrastructure; the capture conventions are Assurance; the periodic analysis is Improvement.

---

## Design pass work queue

Current agreed order for remaining component design passes:

1. ~~Working Practices~~ — DONE
2. **Assurance** — next (moved ahead of Messaging; directly delivers O1, sets the cross-cutting lens)
3. Messaging
4. Build
5. Infrastructure
6. Orchestration (depends on Messaging and Build)
7. Migration and Deployment (either order)

---

## Standards Dependency Map

How standards depend on each other via declared `uses` relationships. Current as of binder v65.

```
Tier 0 — Foundation (no declared uses)
│
├── DocumentationMethodology_Standard_v1 ★    universal, exempt from uses
│
├── Principles_Standard_v2    no declared uses
│
├── DocumentationMethodology_SchemaAuthoring_Standard_v1    no declared uses
│   │
│   ├── DocumentationMethodology_SchemaDefinitions_Standard_v1 ★
│   │
│   ├── Core_Schema_Standard_v2 (provisional)
│   │
│   └── PD_Schema_Standard_v1
│       │
│       └── PD_Standard_v4
│
└── Standards_Authoring_Standard_v8 ★
    │
    │   Tier 1
    │
    ├── Standards_Consumption_Standard_v3
    │
    └── Tools_Authoring_Standard_v8
```

★ = universal or always-on dependency

---

## Completed items (prior sessions)

### DocMeth — uses migration — DONE

All three affected standards updated to reference new DocMeth v1 identities. Standards_Authoring_Standard_v7, PD_Schema_Standard_v1, and Core_Schema_Standard_v2 all current.

### Standard design approach — two classes by load pattern — DONE

Captured in Standards_Design_v3, Standards_Decisions_v3 (D15–D19), and Standards_Authoring_Standard_v7 (authoring rules, design guidance, default-Required strength model, acceptance test). DocMeth clean-sheet rebuild is the worked example. Cross-reviewed and accepted.

### Standards review batch — DONE

Six standards reviewed against the full methodology (no-consumer-no-rule, earn-your-place, name-your-principles, operations test, acceptance test, task-vs-carried classification). Findings:

- **Tools Authoring Standard v4 → v7** (substantive): authoring rules reference updated from a named list of five to the full capability-wide set. Explicit incorporation contract, applicability section, acceptance test, noun-substitution rule, scope narrowed to deployment handoff, trigger made generic, sibling-outputs corrected. Three cross-review rounds, ten findings across rounds 1–2 all resolved, round 3 finding (acceptance-test ambient-context wording) accepted as a Standards carry. Tools Decisions v4 → v7, Tools Design v3 → v6 updated alongside.
- **Core Schema Standard v1 → v2** (minor): Tags block type removed per no-consumer-no-rule; `uses` updated.
- **Standards Consumption Standard v2 → v3** (minor): `uses` updated to Standards_Authoring_Standard@v7.
- **Principles Standard v1, PD Schema Standard v1, PD Standard v4**: clean — no changes needed.

### Standards acceptance-test ambient-context fix — DONE

Completed 2026-09-15. Acceptance test amended for ambient framework context (D21). Cross-review: two defects remediated (F1 definition added, F2 "guaranteed" replaces "available within scope"), one concern accepted (F3 Tools sync included). Deployed: Standards_Authoring_Standard v8, Standards_Decisions v4, Tools_Authoring_Standard v8.

---

## Cross-review register

| Item | Reason | Status |
|---|---|---|
| DocMeth clean-sheet rebuild (three v1 standards) | Full rework of DocMeth standards | **Accepted** — two rounds, all findings resolved. Published 2026-09-14 |
| Standards design approach update (Design v3, Decisions v3, Authoring Standard v7) | New design approach, three new authoring rules, strength model change, acceptance test | **Accepted** — two rounds, all findings resolved. Published 2026-09-14 |
| PD Standard update (Design v3, Decisions v3, Standard v4) | Design-approach content, new gates, brief rule | **Accepted** — ten findings, all resolved. Published 2026-09-14 |
| Tools Authoring Standard v7 (Design v6, Decisions v7) | Authoring rules reference, incorporation contract, scope | **Accepted** — three rounds (10 findings resolved, 1 carried to Standards). Published 2026-09-14 |
| Principles premise strengthenings (P3, P4) | Three candidate strengthenings from design-approach work (F12 pattern) | **Accepted** — F1 remediated (false-exclusive), F2 remediated (D10 wording), F3 remediated (D11 wording). Published 2026-09-15 |
| Standards acceptance-test wording (ambient context) | Framework-contract issue exposed by Tools cross-review | **Accepted** — F1 defect (definition), F2 defect (guaranteed wording), F3 concern (Tools sync) — all remediated. Published 2026-09-15 |
| WP Design v1 (Brief v1, Decisions v1) | WP design pass — new component model, Assurance extraction, 16 decisions | **Pending cross-review** |

---

Version note: v15 — FileOps dissolved (D17), content redistributed. Assurance brief sketch expanded to v2 (learning loop, full-lifecycle scope, Improvement boundary). Work queue updated: Assurance next. Improvement identified as new component (count 14 → 15). Two submission queues distinguished (task queue, learnings queue). Build input document created. Core and Infrastructure carries from FileOps noted. 2026-09-15. Replaces v14.
