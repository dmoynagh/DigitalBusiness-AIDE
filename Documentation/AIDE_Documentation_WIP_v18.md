AIDE Documentation | WIP | AIDE_Documentation_WIP@v18 | 2026-09-16

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

## Completed — Core

### Component alias uniqueness — DONE

Stated in Core_Design_v2: component names and aliases must be unique within the framework; aliases are used as type-reference prefixes in the dot-qualified naming grammar (`pd.brief`); declared in the component's index document. Carried in the Component naming subsection.

### Carries from WP design pass — DONE

Completed 2026-09-15. All six items applied to Core_Design_v2 and Core_AIDEMap_v2, deployed via FUP:

1. **Definition of done** — added as a framework-wide requirement.
2. **Assurance** — added as a framework-wide requirement.
3. **P6** — added as the sixth ownership rule.
4. **Assurance and Improvement** — added to the component map under Guidance. Component count 13 → 15.
5. **Archived folder convention** — added to Core Structure.
6. **Git-as-history** — added to Core Structure; `_superseded` folder pattern dropped.

Also updated: Core_AIDEMap_v2 — Assurance and Improvement added under Guidance; WP subtree updated to reflect WP_Design_v2 areas (Working State, Content Delivery).

Open: the WP entry in Core_Design's component map table still carries a pre-design-pass purpose line and boundary description (predates the Assurance extraction). Flagged for correction, not yet applied.

Source: `_rebuild/WP_CoreCarries_v2.md`.

---

## Completed — Assurance

### Assurance design pass — design, decisions — DONE

Completed 2026-09-15. Assurance_Design_v3, Assurance_Decisions_v3 authored. Three-round cross-review (19 findings, all resolved).

Key outcomes:
- Three concurrent layers of defence: proactive conventions, detective conventions, learning and feedback loop — concurrent, not sequential
- Three autonomy tiers named: directed, collaborative, autonomous. Either side selects directed/collaborative; only the human authorises autonomous
- Conversational confidence vocabulary defined and owned by Assurance: strong, moderate, low (separate from the standards strength model)
- Conformance checking added as a detective convention (cross-review F2) — intended-outcome-to-delivered-outcome closure loop
- Active identification added as a cross-cutting AI obligation (O6) — forward-looking, not retrospective
- Assurance does not make action decisions — identifies, captures, surfaces. Human decides on high-impact instances; Improvement decides on accumulated patterns
- Learning loop designed, implementation deferred until Orchestration is built and tested
- Low friction as proportionate overhead — governing test is whether overhead produces trust that justifies its cost
- Queue-writing ownership: Assurance decides what to capture, Orchestration coordinates the write, Infrastructure provides the plumbing

Fourteen decisions recorded (D1–D14). Pending: standard authoring, old-material pass.

**Correction flagged 2026-09-16:** the queue-writing ownership line above (D14 — "Orchestration coordinates the write") needs revisiting. Orchestration's investigation found the framework inbox and Assurance's data logger are better modelled as remote-hosted MCP services, called directly by any client — there is nothing for Orchestration to coordinate. See Orchestration_Decisions_v1 D19. D14's wording should drop the Orchestration clause when Assurance is next worked. Not yet applied — recorded here so it isn't lost.

**Cases_Working started 2026-09-16.** `Assurance/AIDE_Assurance_Cases_Working_v1.md` — an informal parking place for candidate learning-loop entries, pending the hosted queue service and Improvement's design pass settling the real schema. First entry: a recurring pattern from Orchestration's investigation (documented platform features not behaving as documented — search-for-known-issues should trigger earlier than it did). Unreviewed.

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

### MCP server delivery model — tested 2026-09-16

`Infrastructure/AIDE_Infrastructure_MCPDeliveryModel_v1.md` — a tested, empirically confirmed methodology for delivering AIDE functionality as local MCP servers via marketplace plugins, reaching Code, Cowork, and Chat from one server codebase with automatic update propagation. Discovered during Orchestration's investigation, but the delivery model itself is Infrastructure-owned — components are consumers, not owners (Orchestration_Decisions_v1 D18).

Confirmed via three tested probes (dispatch-probe, mcp-ping-test v1.0.0–v1.0.3). Includes the working configuration (marketplace plugin for Code/Cowork, `claude_desktop_config.json` entry for Chat), five known platform issues with workarounds, and the `.mcpb` Desktop Extension approach as a deprioritised fallback. Not yet a formal design document — carry forward for Infrastructure's design pass, including the open question of whether the Chat bootstrap step should be automated (e.g. `aide mcp-register`).

**Repo distinction noted:** `DigitalBusiness-AIDE-Marketplace` is the temporary testing ground for plugin probes; `DigitalBusiness-AIDE-Deploy` is where the delivery model graduates to once it moves from "confirming the mechanism works" to "this is how AIDE actually ships."

---

## Pending — Build (NOT YET STARTED)

### Seed material

`_rebuild/Build_Input_Working_v1.md` — the design-build separation principle (leaning, not a rule) and the concrete near-term question of where AIDE's own framework outputs go. From FileOps dissolution (D17).

---

## Pending — Orchestration (substantial pre-work done, formal pass still queued behind Build)

Orchestration's design pass has not formally started — it remains queued behind Build in the work order (see Design pass work queue, below), because build delegation (Orchestration's first real use case) needs Build's boundaries to test against. That dependency is unchanged.

However, substantial grounded work happened ahead of the queue position, starting from the original scoping session (`AIDE_Orchestration_WIP_v1.md`) and extending through an investigation and empirical testing pass on 2026-09-15/16:

- **Design v1, Decisions v1 (D1–D19), UseCases v1** drafted in `Orchestration/`. Draft status — not cross-reviewed, not formally accepted.
- **Core boundary correction proposed** — Orchestration owns the crossing (dispatch, invocation, adapters, correlation), not task semantics, verification policy, or response meaning. Core's current wording ("work package structure, verification, and capability profiles") needs correcting to match (D3) — a dependency on Core, not yet applied.
- **Two use-case gaps resolved by dissolution, not extension** — Assurance's learning-loop queue writing and Improvement's scheduling both turned out to be hosted-MCP-service clients, not Orchestration concerns (see the Assurance correction above and D19).
- **Implementation home empirically settled** — not `aide dispatch` in the CLI as first proposed, but a plugin-delivered local MCP server (D10, revised). See the Infrastructure MCP delivery model entry above — this is the concrete evidence base the revision rests on.
- **Real open risk remaining:** build delegation (use case 2) is covered in shape by the dispatch model but genuinely unproven — nothing has exercised it with a real Build payload, because Build doesn't exist yet. This is the actual reason Orchestration can't be called complete ahead of Build, not a formality.

Net position: don't reorder the queue on the strength of this — the dependency on Build is real, not just procedural. But the design-shaping and empirical-testing work already done should carry forward directly into the formal pass rather than being redone.

---

## Pending — Improvement (NEW COMPONENT — identified, not yet scoped)

Iterative improvement of the framework and working practices, regardless of source (human or AI). Owns the pattern analysis, periodic review of the learnings queue, and the decision about what to act on.

**Boundary with Assurance:** Assurance identifies measurable moments, captures learnings to the queue, and surfaces high-impact instances to the human. Improvement owns accumulated-pattern analysis, escalation decisions arising from that analysis, and subsequent action decisions including convention changes. The learnings queue is the interface between them.

**Boundary with Orchestration — correction flagged 2026-09-16:** this was previously stated as "Orchestration provides the mechanism to run the reviewer on a schedule." Orchestration's investigation found scheduling isn't dispatch-shaped any more than queue-writing is (see the Assurance correction above) — the actual dependency is the hosted learnings-queue service existing, not Orchestration being built and tested. Improvement's design pass may be unblockable sooner than previously assumed, once the hosted service (Infrastructure's sub-scope) exists. Wording not yet corrected in a formal document — recorded here so it isn't lost.

**Working-direction name:** Improvement (plain, direct, source-agnostic).

**Component count:** 14 → 15.

---

## Pending — Submission queues

### Task queue — frictionless capture path to AIDE development

AIDE needs a mechanism for submitting tasks, additions, changes and new functionality from work sessions into an AIDE development queue. The charter's frictionless capture principle governs the design.

**Concept.** Work side: single action on any surface, no triage required. AIDE development side: queue reviewed, triaged, worked through the normal design-build-deploy cycle.

**Preferred mechanism.** An MCP server callable from any AI surface, writing to a queue document in the AIDE git repo. **Note 2026-09-16:** this is now a tested, not just proposed, mechanism — see the Infrastructure MCP delivery model entry above.

### Learnings queue — feedback from work outcomes

A distinct queue from the task queue. Holds raw observations from A-B comparisons at measurable moments. AI-initiated, written in the background when significant. Most entries sit and wait for aggregate analysis.

**Two escalation triggers:** a single high-impact instance is surfaced to the human through capture-and-place (the human decides whether it becomes a task); accumulated patterns surface during periodic review by the Improvement component's reviewer.

**Mechanism:** same MCP as the task queue, writing to a separate queue document. The AI can write to it unprompted.

**Ownership — correction flagged 2026-09-16:** previously stated as Infrastructure (MCP server, file format, location), Orchestration (coordinates and invokes writes), Assurance (capture conventions), Improvement (pattern analysis). The Orchestration clause is now understood to be unnecessary — a hosted MCP service is called directly. Ownership narrows to: Infrastructure (the hosted service, the format, the location), Assurance (what and when to write), Improvement (periodic analysis). Not yet applied to a formal document.

---

## Design pass work queue

Current agreed order for remaining component design passes:

1. ~~Working Practices~~ — DONE
2. ~~Assurance~~ — DONE
3. **Messaging** — next
4. Build
5. Infrastructure
6. Orchestration (depends on Messaging and Build) — see Pending — Orchestration above for substantial pre-work already done ahead of this position
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
| Assurance Design v3 (Decisions v3) | Assurance design pass — three-layer behavioural model, autonomy tiering, confidence vocabulary, learning loop, 14 decisions | **Accepted** — three rounds (19 findings resolved). Published 2026-09-15 |
| Orchestration Design v1 (Decisions v1, UseCases v1) | Draft — dispatch model, ownership narrowing, empirically tested MCP delivery mechanism, 19 decisions | **Not yet submitted for cross-review** — draft status, pending Build's design pass for full validation |

---

Version note: v18 — Orchestration's substantial pre-work (Design v1, Decisions v1, UseCases v1, all empirically tested) recorded under a new Pending — Orchestration section, without reordering the design-pass queue. New Pending — Infrastructure entry for the tested MCP server delivery model (Orchestration_Decisions_v1 D18). Assurance's D14 and the Learnings queue ownership both flagged for correction — the Orchestration-coordinates-writes wording is superseded by direct hosted-service calls (D19) — not yet applied to their formal documents. Improvement's Orchestration-dependency wording similarly flagged. Assurance Cases_Working started as an informal parking place for learning-loop candidates pending the hosted queue and Improvement's design pass. Cross-review register updated with Orchestration's draft entry. 2026-09-16. Replaces v17.
