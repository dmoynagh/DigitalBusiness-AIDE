> identity: WorkingPractices_Standard@v2 | doctype: standard | updated: 2026-09-17 | uses: Standards_Authoring_Standard@v8

# Working Practices

Apply the operational conventions for AI-assisted work — capture-and-place, working state, boards, and content delivery.

Document-level default strength: Required.

## Applicability

Information. This standard applies to any AI-assisted work session, regardless of phase or surface.

## Capture-and-place

The AI's standing responsibility to organise and allocate everything of value produced in a session to its correct home.

**Three obligations:**

1. **Continuous silent capture** — notice and hold content of value as it arises, without interrupting the flow of work.
2. **Placement by destination definitions** — route content to where it belongs using the destination map below.
3. **Batched surfacing at natural breaks** — surface allocations at natural pauses rather than interrupting for each piece.

**Destination map:**

- Component documents (design, decisions, knowledge, brief) — confirmed content with a permanent home
- Open items — work to be discussed or done, not yet home
- Working documents — when the material associated with an item grows beyond inline tracking, or content needs its own working space
- WIP — transient, staging, or homeless content

**Homeless pieces** — content with no identified destination — are named, not dropped. Err toward over-capture. When multiple destinations are plausible and the choice is not confident, surface the alternatives and ask rather than silently choosing.

**Session-end allocation.** Work through the session's output and confirm what goes where. Parking in WIP for a quick save, or a working document for a longer one, is acceptable — but the discipline is allocating to the real home. Content that stays parked in a temporary location past the session it was captured in, when it has a known destination elsewhere, is a signal to address it.

**Proactive knowledge preservation.** Watch for content at risk of being silently lost: session length approaching compaction, context getting heavy, a switch to a new chat or platform without saving. Push back and advise what needs saving before the human proceeds into that risk.

**Uncertain destination.** Confident → place silently. Unsure → recommend a destination with reasoning. No defined home exists → name the gap rather than forcing a fit or dropping the content.

## Operational tools

Named, invokable actions that trigger WP behaviours. Names are the human's to set — treat the following as working labels for the behaviour, not fixed command text.

- **Full stop** — session is over. Run the strongest capture-and-place sweep.
- **Checkpoint and continue** — a natural break. Flush content, then hand off current position and next steps.
- **Flush without closing** — commit captured content to WIP, or push to masters plus binder, while the session continues.
- **/more** — expand the current prompt with additional detail (AI-presented prompts are concise by default).

## File delivery rules

Apply based on the platform's file-access capability, not by which surface is in use:

1. **No direct file access** — when handing back an updated file for download, tell the user where to save it, based on the path in the document's header.
2. **Direct file access** — check the file's physical location against the path in its header. Move it if they disagree.

## Overview-first working discipline

Stay at the overview level until it could drive excellent execution; probe rather than dive into detail before the shape is clear. This applies to any work carrying the temptation to descend into detail early, not only design.

Information. Project Design owns the design-specific application of this discipline. Assurance consumes it as one of its proactive conventions. Neither is restated here.

## Working State

Where content lives while in motion, and how work is tracked and completed.

### WIP

The transactional staging mechanism, with three roles:

1. **Homeless shelter** — temporary home for content without a destination yet. Nothing stays by default; content that looks permanently resident is a signal to place it properly.
2. **Persisted working memory** — current thinking and working state that must survive across sessions.
3. **Transactional staging** — confirmed or pending changes to master documents, held here until written (see Pending content rule below).

**Conventions:** multiple WIP documents may exist at once, split by size or subject. WIP loads directly into context — it is not delivered via the binder. Prefer visibility over a fixed location: easy to find, easy to save to, easy to load. Track active WIP documents in the project's index to prevent orphaned content. Content should flow through a WIP document to its destination, not accumulate in it.

**Caller persistence convention:** when a caller assembles a unit of work (build package or build instruction), WIP is the default home for in-session transactional state — what was requested, what came back. Where the platform provides persistent memory, it is the default for cross-session continuity — durable facts, standing context, and lightweight state the platform manages automatically. WIP persistence is for project-level working state too large or complex for platform memory, and serves both in-session and cross-session roles when platform memory is not available. The caller decides; these are defaults when no decision is made.

### Pending content rule

Confirmed content awaiting delivery to a master document, held in WIP under the destination document's heading.

**Composite authority rule:** the current truth of a master is master content plus its pending overlay. Before acting on a master, check WIP for pending content on it and work from the merge. The pending overlay wins where it explicitly changes master state. If the merged state is ambiguous, surface the conflict rather than infer it.

### Open items

A semantic classification, not a storage location. An open item is an unresolved question, decision needed, or identified work not yet committed — anything surfaced during work that cannot be resolved immediately. Open items are persisted in WIP.

Information. The distinction from "captured into WIP" in the work-item fates: parking as an open item means the content has been assessed as needing resolution — it is classified as unresolved. Capturing into WIP means preserving a work item that has not yet been assessed — it is staged for later sorting and classification. Both may be stored in WIP; the difference is whether the item has been assessed as needing resolution.

**Create** an open item when work produces something needing later discussion, decision, or action and no immediate resolution is available.

**Resolve** by one of: answered and recorded as a decision; committed as work in a work register; or dropped by explicit decision — no silent disappearance, per the no-knowledge-lost rule.

When the material associated with an open item grows beyond what inline tracking can manage, promote it to a working document (the split test from Documentation Methodology governs this escalation). Promotion transfers resolution responsibility to the working document — the working document now owns the lifecycle of whatever the open item identified.

### Working documents

When the material associated with an item grows beyond what inline tracking can manage, or content needs dedicated working room, escalate to a working document. The split test (Documentation Methodology, always-on) governs this escalation.

Information. Three types: **working document** (incomplete material, confirmed items awaiting placement, in-progress thinking), **report** (findings, analysis, or review results), **resource** (reference or knowledge supporting the work). WP owns these types as workflow containers; Documentation Methodology owns their doctype mechanics.

### Work items

A generic entity flowing through a workflow — something noticed that needs tracking, discussion, resolution, or action.

**Two axes:** type (what kind of thing it turned out to be, decided on judgement rather than chosen from an enumerated list) and state (open, current, closed — filtered views over the same items, not separate lists). When a work item is tracked on a board, board zones are the concrete realisation of its lifecycle; the generic state axis applies to work items not on a board.

**Five fates:** dealt with in conversation leaving no trace, resolved and recorded as a decision, parked as an open item, captured into WIP, or becomes committed work in a work register. Placing a work item on a board is a tracking action — it can happen alongside any fate and is not itself a fate.

**No knowledge lost.** A work item may be dropped, but only by deciding it carries nothing worth keeping — disappearance is never an accident.

Recommended. **Scalable implementation.** A session may realise the work-item tracking model not at all, lightly, ad hoc, or in full, chosen by the scale and importance of the work. The no-knowledge-lost rule is Required regardless of implementation level.

**Distinct from work register entries.** A register entry is confirmed work owed under Project Design's commitment ledger — different purpose, different owner, no subset relationship.

### Board

A scoped record of work across its full lifecycle, maintained by the AI as part of capture-and-place. One board per scope, each its own document. A board task is the board's representation of a work item — the same entity, tracked on a board for lifecycle visibility. Not a separate model.

**Five zones** stage work from intake to completion — a staging model, not a pipeline with gates:

- **Inbox** — fast capture: the human provides only a name; the AI assigns zone (inbox), ID, and order mechanically. Zoned to a substantive zone later.
- **Future** — recorded and placed, not yet in play.
- **Pending** — ready to be drawn into current; next in line.
- **Current** — the immediate working context; the orientation view at session start.
- **Done** — completed; kept for reference until cleared.

General flow is inbox → future → pending → current → done, but shortcuts are normal — urgent work goes straight to current. An unresolved dependency, not a separate zone, is what marks a task blocked.

**Task properties — every task carries:** name, ID (a short code for cross-referencing), zone (which lifecycle zone the task is in), and order (position within zone).

**Conditional properties — present when applicable:** dependencies (another task by ID, an external event, or a person — resolved dependencies marked), who, sub-items (parent completes when all children complete), work sets (sub-items with no inter-dependency, all in play at once), categories/tags, a completion link, and notes.

**AI maintenance, as part of capture-and-place:**

- Session start — read the relevant board's current zone; orient from it.
- During work — add agreed work; update zone as work progresses or completes; mark dependencies as they resolve; capture new tasks to inbox or the appropriate zone.
- Session end — the board reflects what happened, as part of the capture-and-place sweep.

Keep boards outside the binder — the same churn handling as WIP.

**Dashboard.** A rendered view across boards, assembled on demand and filtered by zone, tags, who, or dependency state. Not a stored record.

### Definition of done

Every component defines how its own work completes, against a testable-or-assessable invariant. WP owns the definition-of-done block type. Project Design fills it in the brief, component design passes fill it in their own completion criteria, and Build checks outcomes against it.

A definition of done contains one or more testable or assessable criteria that determine when the work is complete. The criteria are stated by the component designer; Build checks outcomes against them.

Information. The full formal schema for this block type lands with the schema definitions task. The minimum stated here is sufficient for construction and use.

### Development lifecycle

Information. Phases (research, design, build, deploy, review) describe what kind of work is being done. AIDE realises phases as modes — states the AI session operates in, shaped by which standards and tools are loaded. WP owns the lifecycle concept; each phase component owns its own mode.

## Content Delivery

How working and project context is assembled and delivered to the AI session.

### Binder

WP owns the binder — why it exists, how it is used, what it includes, and its doctype. Assemble it using the three-tier inclusion model:

1. **In the binder** — needed for thinking and reasoning about the work at hand.
2. **Known to the framework** — part of the project, listed in the folder's index, but not loaded into context.
3. **Just present** — incidental files with no framework registration.

The test for inclusion is whether a file is needed for the work, not whether it is a governed document. Keep high-churn content (WIP, boards) out of the binder — including it would force a rebuild on every change.

## Boundaries

Information.

**WP does not own:** the design method (Project Design), how code is structured (Build), document structure and the split test (Documentation Methodology), the component model and framework-wide requirements (Core), universal reasoning premises (Principles), the work register (Project Design), trust conventions and verification behaviours (Assurance), cross-platform transport (Orchestration).

**WP owns:** capture-and-place, operational tools, the WIP model, work items, boards, open items, pending content, the definition-of-done block type, the development lifecycle concept, process document types, the binder, the generic overview-first discipline, and file delivery rules.

File Operations is dissolved; its content redistributed to natural owners (WP retains only the file delivery rules above).

---

Version note: v2 — cross-review remediation (ChatGPT, 4 rounds, 12 original findings + 6 new). Round 1: trigger description reworded for runtime (F1); placement heuristic removed from applicability (F2); session-end persistence signal qualified (F3); WIP/memory persistence distinction clarified (F4); working-document escalation separated as Required from Information type definitions (F5); split-test source acknowledged (F6); open-item operational model added (F7); scalable implementation explicitly Recommended with invariant no-knowledge-lost (F8); board task defined as work-item representation (F9); task properties split into invariant and conditional (F10); reference-guide deployment output removed from runtime standard (F11); definition-of-done schema noted as pending (F12). Round 2: platform-memory default qualified for capability availability (N1); open-item classification distinguished from WIP storage (N2, partly); board zone renamed from state (N3); definition-of-done mechanism claim softened (F12, partly). Round 3: open-item container language removed and promotion semantics corrected — transfers resolution responsibility, doesn't resolve (N2); WIP fate distinction sharpened to assessment vs staging (N2); board maintenance "state" → "zone" (N4); inbox capture clarified — human provides name, AI assigns mechanical properties (N5); definition-of-done minimum-viable schema added inline (F12). Round 4: open-item persistence restricted to WIP only — removes two-relationship ambiguity with working documents (N6). 2026-09-17. Replaces v1.
