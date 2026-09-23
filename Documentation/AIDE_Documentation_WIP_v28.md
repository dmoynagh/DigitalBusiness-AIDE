AIDE Documentation | WIP | AIDE_Documentation_WIP@v28 | 2026-09-23

## Active threads

### Capabilities component and development standards — 2026-09-23

Capabilities created as 17th component (Guidance role). Produces the Capabilities Development Standard — base methodology for designing, building, and deploying all four capability types (standards, tools, services, utilities). Design v1-draft1 and Decisions v1-draft1 (D1–D8) committed.

**Capability definition extended:** four types, two distinguishing properties (execution context, direction of service). Development standards replace authoring standards — broader scope covering design → author (conditional) → build → deploy → consumption. Build specifics as build standards per capability type's build domain.

**Charter updated:** development principles section added with framework-delivered solutions principle. When an issue is identified, the framework delivers the structural solution — not a behavioural commitment.

**Core updated:** AIDEMap v4 (Capabilities and Services in Guidance), Core_Design v7 (capability definition expanded, component count 15→17).

**Work owed:**
- Charter standard: reauthor from updated charter, cross-review, deploy as skill
- Remaining charter development principles (demonstrated need, simplest model, etc.) not yet in charter text — add in the same pass
- Standards Development Standard: author from accepted Standards + Capabilities base (supersedes Standards_Authoring_Standard_v8)
- Tools Development Standard: same pattern (supersedes Tools_Authoring_Standard_v8)
- Services Development Standard: author from Services design once reviewed and accepted
- Utilities: component creation, design pass, development standard
- Capabilities Design: Dave's review, then cross-review

**Open items (logged in project memory OI-1 to OI-3):**
- OI-1 (PD, short-term): update design-check skill to load PD, WP, DocMeth standards at design start
- OI-2 (Build, short-term): create build-check skill, same pattern for build sessions
- OI-3 (WP, short-term): create work-check skill — identifies work type, bootstraps context

**Housekeeping:**
- Project memory (aide-rebuild.md) at capacity — needs consolidation or splitting
- Services Design v1-draft1 pending Dave's review (committed earlier this session)

### Open items — 2026-09-23

- **OI-WP-1:** "update state" and "update docs" as operational commands. Update state = WIP, board. Update docs = masters then binder. Content-update actions complementing the existing session-lifecycle commands. WP design, short-term
- **OI-WP-2:** binder notification convention — after doc changes via document manager, notify user binder needs updating in context. WP or Infrastructure, assess placement
- **OI-WP-3:** persistence summary convention — after writing to docs, provide a brief routing summary (x written to Core_Design, y to WIP) so user can check destinations. WP, assess placement
- **OI-WP-4:** open-item timing heuristic — WIP storage, board for 1-3 day items. WP design refinement of the open-item model
- **OI-WP-5:** doc-manager edit discipline — document manager makes master edits frictionless, risk of constant churn replacing the batch workflow. WIP is the frequent-update layer; masters update when work is done. Needs WP guidance on when to use doc manager for master edits vs accumulate in WIP. Discuss soon
- **OI-PD-1:** inbox as a scoped artifact — uncommitted, pre-triage capture stage upstream of the board. Append-cheap, unordered, low-ceremony. Declared per scope in the index file at whatever tier fits (solution or project). Triage is periodic with outcomes: promote to board, park, bin, or reroute to another scope's inbox. The remote intake path (MCP submission queue) is the inbox's write API, resolving scope through the index. Not a duplication of the board — the board is committed current work, the inbox is "don't lose this." Ownership: PD
- **OI-PD-2:** WIP scoping — same scoping logic as inbox. WIP lives at whatever tier it naturally belongs to, declared in the index. Primary WIP at top, delegated WIPs inside projects when a chunk of work earns its own. Tree-crawlable to find the appropriate WIP. Inbox and WIP are both scoped artifacts declared in the index — one idea covering both. Ownership: PD
- **OI-PD-3:** overview doctype already defined in PD Schema Standard v1 — project-scale snapshot, concise context, deviation detector. Compiled for human consumption, not a WIP or parking place for in-flight work. No new definition needed; confirmed during voice session
- **OI-DEP-1:** deploy component schema standards as skills — PD Schema Standard v1 is authored but not deployed as a skill. Check Core Schema Standard v2 and any others in the same state. Evaluate pickup only after deployment

### DocMeth — schema review across components

All components owning doctypes or block types must define them using the accepted definition contract. The definition contract has been simplified in the rebuild (6 blocktype properties, 4 doctype properties). Assessment produced (DocMeth_Schema_Review_v1) — rework is a separate task per component.

Note: PD_Schema_Standard_v1 was authored against the old Schema Standard v4 property vocabulary. It should be reviewed against the simplified contract in DocumentationMethodology_SchemaAuthoring_Standard_v1 when next worked. Core_Schema_Standard_v2 is provisional and will be reviewed when Core's design pass is done.

### WP — remaining items

Old-material pass (WP1–WP13 from old corpus) not yet run — required before WP can be called complete per the rebuild method and F10.

WP schema definitions not yet written — doctypes (WIP, working document, report, resource, board) and block types (work item) need formal definitions per the documentation methodology schema contract.

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

**Cross-reviewed 2026-09-17.** Three rounds via ChatGPT, 14 findings total, all resolved. Final documents: WP_Brief_v2, WP_Design_v5, WP_Decisions_v3 (20 decisions, D18–D20 from cross-review remediation).

Key outcomes:
- Assurance extracted as a new top-level component (Guidance role) and framework-wide requirement in Core (D1, D16)
- Capture-and-place elevated to WP component level with proactive knowledge preservation (D12)
- Workflow commands replace session-transition commands as broader concept (D11)
- Working State absorbs Work Lifecycle (D3) — WIP three-role model, work items, board (settled name; design session starting — replaces "work plan with named workstreams"), pending content
- Capture and Organisation dissolved — content moved to WP component level and Working State (D2)
- Human-AI Collaboration dissolved — content moved to Assurance component (D1)
- Definition of done elevated to Core framework-wide requirement (D4)
- P6 moved to Core as sixth ownership rule (D5)
- Guidance Profiles deferred — no demonstrated consumer for solo developer (D6)
- Overview-first working behaviour owned by WP generic, PD consumes (D7)
- Verification behaviours placed in Assurance (D8)
- FileOps dissolved — content redistributed to WP component level, Core Structure, Infrastructure, and Build (D17, superseding D14)

Twenty decisions recorded (D1–D20, with D18–D20 from cross-review remediation). FileOps dissolved (D17) — content redistributed to WP component level, Core Structure, Infrastructure, and Build. Pending: old-material pass, schema definitions, standard authoring.

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

Closed 2026-09-17: WP purpose line and Orchestration entry corrected (CORE-ORC + CORE-WP). Core_Design_v4, Core_AIDEMap_v3.

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

## Completed — Messaging

### Messaging design pass — design, standard, tool, cross-review — DONE

Completed 2026-09-15. Full design pass with legacy binder review (Capabilities_Binder_Messaging_v6, ~23 decisions consolidated). Three cross-review rounds (F1–F7, R1–R4, R5–R7), all resolved. Final documents: Messaging_Brief_v1, Messaging_Design_v4, Messaging_Decisions_v4 (D1–D28), Messaging_Standard_v4, Messaging_Tool_v4.

Key outcomes:
- Repositioned as format and methodology, not transport (D1, from Core D4) — Foundation role, structurally equivalent to Documentation Methodology
- Single merged design document replacing legacy separate design and tool-design (D16)
- Legacy Capability/Element model superseded (D17)
- One slug rule for Thread/From-slug/Version (D18)
- Promote duplicate-check as precondition (D22)
- QueryReceipt response as canonical positive-evidence form (D23/D26)
- Receive idempotency split from dispatched-action idempotency (D27)

Skill rebuilt from accepted Standard v4 + Tool v4 (Phase 2 completion, PR #3, 2026-09-17). FUP deployed, binder current at v95.

---

## 10. Build ✅

Take defined work and produce the outcome by creating and modifying files against a target. Return the result for acceptance. Behavioural component — conventions applied by following them, not machinery.

**Design and decisions**
- Build_Brief_v1.md
- Build_Design_v3.md
- Build_Decisions_v3.md (D1–D32)
- Build_Overview_v1.md

**Standards**
- Deferred by design (D32) — first instance authored when documentation-update build standard has a consumer

**Pending:** Cross-review (BLD-XR) — v3 documents deployed, prompt drafted, not yet submitted. Carry note for Assurance: consider V&V as its own area.

### Work register tracking for deployed skills

Once a standard or tool has a deployed skill, design changes to that component must be tracked in a work register so the skill is rebuilt and redeployed. This closes the design-build-deploy loop: a design change produces a standard update, the standard update is a build input, and the skill is the build output that gets deployed. Without the work register entry, a changed standard silently drifts from its deployed skill. Convention starts with Phase 2 skill authoring — each component's work register should carry the skill rebuild as a linked build outcome.

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

### MCP server delivery model — tested 2026-09-16, Phase 1 deployed 2026-09-17

`Infrastructure/AIDE_Infrastructure_MCPDeliveryModel_v2.md` — a tested, empirically confirmed methodology for delivering AIDE functionality as local MCP servers via marketplace plugins, reaching Code, Cowork, and Chat from one server codebase with automatic update propagation. Discovered during Orchestration's investigation, but the delivery model itself is Infrastructure-owned — components are consumers, not owners (Orchestration_Decisions_v1 D18).

Confirmed via three tested probes (dispatch-probe, mcp-ping-test v1.0.0–v1.0.3). Includes the working configuration (marketplace plugin for Code/Cowork, `claude_desktop_config.json` entry for Chat), five known platform issues with workarounds, and the `.mcpb` Desktop Extension approach as a deprioritised fallback. Not yet a formal design document — carry forward for Infrastructure's design pass, including the open question of whether the Chat bootstrap step should be automated (e.g. `aide mcp-register`).

**Deploy repo PR requirement (2026-09-17).** All changes to `DigitalBusiness-AIDE-Deploy` must go through a PR and merge — direct commits to `main` do not trigger plugin updates. This is a hard build/deployment requirement, not a workflow preference. The Documentation repo (`DigitalBusiness-AIDE`) uses direct commits. Discovered during the Messaging skill rebuild when a direct commit did not propagate; corrected via revert and PR #3. The delivery model doc (v2) lists "merge PR" as a step but does not flag it as mandatory for update propagation — needs explicit statement as a build constraint in the update path section. Carry for when the doc is next worked (Infrastructure design pass or sooner).

**v2 update (2026-09-17):** Registration-path distinction added as known issue #7 — two separate registration paths exist (desktop app Settings → Plugins → Discover for Code tab MCP tools; claude.ai web UI Settings → Plugins for account-level server-side skill mount at `/mnt/skills/plugins/`). Both needed for full three-surface coverage. Missing `%APPDATA%\Claude` path documented as issue #8. MSIX section corrected. "Skill delivery to chat" section added.

**Phase 1 deployed (2026-09-17).** Plugin marketplace `digitalbusiness-aide` live on `DigitalBusiness-AIDE-Deploy` (PR #1 merged). `aide` plugin: dispatch MCP server (claude-code and codex targets) + design-check and messaging skills — confirmed working on Code, Cowork, and Chat. `aide-dev` plugin: scaffold only, no skills yet. Blocking issue resolved: skills require web UI registration (account-level) in addition to desktop app registration (Code tab only). See `_rebuild/Deployment_Plugin_Working_v1.md` for the full plugin structure, skill-to-plugin allocation, and phased rollout plan.

**Repo distinction noted:** `DigitalBusiness-AIDE-Marketplace` is the temporary testing ground for plugin probes; `DigitalBusiness-AIDE-Deploy` is where the delivery model graduates to once it moves from "confirming the mechanism works" to "this is how AIDE actually ships."

**Phase 1 outstanding — all resolved 2026-09-17:**
- ~~Flatten `plugins/aide/` to `aide/` at repo root~~ — resolved: `plugins/` structure is correct per Anthropic's documented pattern. No change needed.
- ~~Remove old test probes from account via web UI~~ — done.
- ~~Test update propagation~~ — confirmed during troubleshooting.

### Phase 2 — deploy completed standards as skills — DONE

Eight skills authored from cross-reviewed, accepted standards and deployed to `aide` (5: principles, docmeth, docmeth-schema-definitions, standards-consumption, pd-standard) and `aide-dev` (3: standards-authoring, tools-authoring, docmeth-schema-authoring). Confirmed on all three surfaces (Code, Cowork, Chat). PR #2 merged.

**Messaging skill rebuilt (Phase 2 completion).** The Phase 1 messaging skill was a legacy migration. Rebuilt from the accepted Messaging standard v4 and tool v4 — legacy content replaced (obligations register, envelope Lifecycle field, Capability/Element model, `/msg-*` command vocabulary). PR #3 merged. Messaging `_index.md` updated to reference v4 masters (commit `253c6fc`).

### Phase 3 — rolling deployment

Scoped as rolling deployment as standards land, not a batch. WP standard cross-reviewed (ChatGPT, 4 rounds, 18 findings), renamed to WorkingPractices_Standard_v2, deployed (commit 0a60d6a, aide plugin PR #8). Assurance standard cross-reviewed (ChatGPT, 2 rounds, 10 findings), deployed (commit 11c47ca, aide plugin PR #7). Build standard and `db-aide-info` resources plugin remain parked by design.

**Work ownership clarifications (2026-09-17).** During WP standard deployment, the distinction between board (tracking view, WP), work register (commitment ledger, PD), and WIP (transactional staging, WP) was sharpened. The fifth work-item fate was corrected from "board" back to "work register" — the board is a tracking mechanism orthogonal to all five fates. A caller persistence convention was added to WIP (default: WIP for in-session transactional state, memory for cross-session continuity). Context summary produced for the Build cross-review.

---

## Completed — Orchestration

### Orchestration design pass — design, decisions, use cases, cross-review — DONE

Completed 2026-09-17. Design pass carried forward substantial pre-work (scoping session, investigation, empirical testing, design-shaping pass in another AI). Four cross-review rounds plus acceptance check via ChatGPT: 29 findings total, all resolved. Final documents: Orchestration_Design_v5 (D1–D48), Orchestration_Decisions_v5 (D1–D48), Orchestration_UseCases_v2.

Key outcomes:
- Central model: dispatch, not orchestration-of-work — owns the crossing, not the work (D1/D2)
- Dispatch request separated from dispatch — caller sends request, Orchestration creates dispatch_id (D35)
- Thin dispatch contract: target (required), payload (required, UTF-8 text), workspace (optional, fails if target requires and not supplied), model (optional, three forms: level/exact/default), response_schema (optional, fails if unsupported rather than silent degradation)
- Transport result contract with success and failure paths, five failure categories (D26/D36)
- Provenance required on completed results — three model-selection forms represented symmetrically (D27/D37/D47)
- Exact-model path pins identity only, provider-native defaults for other settings (D45/D48)
- Two endpoint operations: available_targets() and dispatch(request) (D39)
- Framework Resources consumer contract: three behaviours required from Core (D34/D40)
- Infrastructure owns delivery mechanism, Orchestration requires local execution endpoint (D30/D42)
- Caller-owned routing (D17) and tier (D16)
- Messaging owns message/thread correlation; Orchestration owns dispatch correlation (D22)
- Use cases 5/6 (queue writing, scheduling) dissolved — not Orchestration's responsibility, downstream action required (D31)
- Capability-level names pre-deployment decision, not indefinitely deferred (D33/D41)

Pending: deployment of v5 documents to binder. Assurance D14 correction (D19) — drop Orchestration clause when Assurance is next worked.

---

## Pending — Improvement (NEW COMPONENT — identified, not yet scoped)

Iterative improvement of the framework and working practices, regardless of source (human or AI). Owns the pattern analysis, periodic review of the learnings queue, and the decision about what to act on.

**Boundary with Assurance:** Assurance identifies measurable moments, captures learnings to the queue, and surfaces high-impact instances to the human. Improvement owns accumulated-pattern analysis, escalation decisions arising from that analysis, and subsequent action decisions including convention changes. The learnings queue is the interface between them.

**Boundary with Orchestration — corrected 2026-09-17:** previously stated as "Orchestration provides the mechanism to run the reviewer on a schedule." Orchestration's accepted design (v5, D19/D31) confirmed scheduling is not dispatch-shaped — the actual dependency is the hosted learnings-queue service existing (Infrastructure's sub-scope), not Orchestration. Improvement's design pass is unblockable by Orchestration; it depends on the hosted service, which Infrastructure owns.

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

**Ownership — corrected 2026-09-17:** previously stated as Infrastructure (MCP server, file format, location), Orchestration (coordinates and invokes writes), Assurance (capture conventions), Improvement (pattern analysis). Orchestration's accepted design (v5, D19/D31) confirmed there is nothing for Orchestration to coordinate — a hosted MCP service is called directly. Ownership narrows to: Infrastructure (the hosted service, the format, the location), Assurance (what and when to write), Improvement (periodic analysis). Assurance's D14 correction tracked in Orchestration D19.

---

## Design pass work queue

Current agreed order for remaining component design passes:

1. ~~Working Practices~~ — DONE
2. ~~Assurance~~ — DONE
3. ~~Messaging~~ — DONE
4. ~~Build~~ — DONE
5. Infrastructure
6. ~~Orchestration~~ — DONE (cross-review accepted 2026-09-17, v5 documents pending deployment)
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
| WP Design v5 (Brief v2, Decisions v3) | WP design pass — new component model, Assurance extraction, 20 decisions | **Accepted** — three rounds via ChatGPT (14 findings resolved). Carry: D19 — PD sufficiency contract needs composite-authority amendment. Published 2026-09-17 |
| Assurance Design v3 (Decisions v3) | Assurance design pass — three-layer behavioural model, autonomy tiering, confidence vocabulary, learning loop, 14 decisions | **Accepted** — three rounds (19 findings resolved). Published 2026-09-15 |
| Orchestration Design v5 (Decisions v5, UseCases v2) | Dispatch model, ownership narrowing, full dispatch/result contract, 48 decisions | **Accepted** — four rounds + acceptance check (29 findings resolved). Deployed 2026-09-17 |
| Build Design v8 (Brief v4, Decisions v8, Overview v6) | Build design pass — behavioural component, file-target execution model, 34 decisions | **Accepted** — five rounds (15 findings resolved). 2026-09-17. Standard deferred by design (D32) |
| Core_Design_v4, Core_AIDEMap_v3 (WP carries + housekeeping) | Six WP-design-pass carries applied to Core, plus Orchestration and WP component map corrections (CORE-ORC, CORE-WP) | **Not cross-reviewed** — carries deployed via FUP 2026-09-15; corrections applied direct 2026-09-17. Build F3 carry registered for generic-caller update |
| WorkingPractices_Standard_v2 | WP standard cross-review — renamed from WP_Standard, 18 findings (12 + 6 new) | **Accepted and deployed** — 4 rounds. Documentation repo commit 0a60d6a, aide plugin PR #8. 2026-09-17 |
| Assurance_Standard_v1 | Assurance standard cross-review — 10 findings | **Accepted and deployed** — 2 rounds. Documentation repo commit 11c47ca, aide plugin PR #7. 2026-09-17 |

---

Version note: v27 — WP standard cross-reviewed (4 rounds, 18 findings), renamed to WorkingPractices_Standard_v2, deployed (commit 0a60d6a, aide plugin PR #8). Assurance standard cross-reviewed (2 rounds, 10 findings), deployed (commit 11c47ca, aide plugin PR #7). Build cross-review accepted (5 rounds, 15 findings). Orchestration deployment complete. Core CORE-ORC + CORE-WP closure. Cross-review register updated. Assurance uses declaration corrected (WP_Standard → WorkingPractices_Standard). 2026-09-17. Replaces v26.
