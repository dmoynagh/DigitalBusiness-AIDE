> identity: WP_Design@v7 | doctype: design | updated: 2026-09-24

# Working Practices — Design

## Summary

Working Practices defines the operational conventions, behaviours, and working methods that govern how work is conducted — across any phase, any surface, and any kind of work. It is the umbrella for action and behaviour. Phase-specific methods are owned by their phase component; WP owns what they all consume.

WP operates at two levels. At component level, capture-and-place, operational tools, file delivery rules, and the overview-first discipline are standing obligations and mechanisms available across WP. Below that, two areas provide the models and conventions work uses: Working State (where content lives while in motion, how work is tracked and completed) and Content Delivery (how content reaches the AI session).

The standard states a document-level default strength and marks most sections Required, Recommended, or Information. Applying it correctly means interpreting those strength markers and evaluating the Applicability section before treating any of it as binding — exactly what Standards Consumption governs. The standard declares `uses Standards_Consumption_Standard@v5` for this reason, not because Standards Consumption was used to author it (D22).

The Assurance component, identified during this design pass, takes ownership of the human working model, trust-building conventions, verification behaviours, drift detection, and anomalies — the content originally placed in a Human-AI Collaboration area. Assurance is both a component (Guidance role) and a framework-wide requirement (Core).

---

## Component-level concerns

These are not inside any area. They are standing obligations and mechanisms that govern everything WP does.

### Capture-and-place

The AI's standing responsibility to organise and allocate everything of value produced in a session to its correct home. This is the operational delivery of the no-knowledge-lost framework-wide requirement stated in Core.

**Three AI obligations:**

1. **Continuous silent capture** — the AI notices and holds content of value as it arises, without interrupting the flow of work.
2. **Placement by destination definitions** — the AI knows where things belong and routes them correctly.
3. **Batched surfacing at natural breaks** — rather than interrupting to allocate each piece, the AI batches and surfaces allocations at natural pauses.

Homeless pieces — content with no identified destination — are named, not dropped. The AI errs toward over-capture. When multiple plausible destinations exist and the AI cannot confidently distinguish between them, it surfaces the alternatives and asks rather than silently selecting one.

**The destination map** — where capture-and-place routes content:

- Component documents — design, decisions, knowledge, brief (confirmed, permanent home known)
- Open items — work to be done or discussed, allocated to a component, area, or part
- Working documents — when volume exceeds what open items can hold, or content needs its own working space (the split test governs the escalation)
- WIP — transient, staging, or homeless content (the three-role model described in Working State below)

**Session-end allocation** — at the end of a session or unit of work, the AI works through the session's output and confirms what goes where. Parking content in WIP for a quick state save, or in a working document for a longer one, is acceptable — but the discipline is allocating to the real home. Content sitting in WIP or working documents that should be somewhere else needs to be addressed; persistent residence in temporary locations is a signal.

**Proactive knowledge preservation** — the AI does not only capture at the end. It actively watches for situations where content persisted only in the session is at risk: session length approaching compaction, context getting heavy, switching to a new chat or a different platform without saving. The obligation: push back, advise what needs saving, and do not let the human proceed into a situation where valuable content would be silently lost.

**Four methodology rules from the Core shaping session (confirmed):** The AI captures continuously; places by destination definitions; batches surfacing at natural breaks; and names homeless pieces rather than dropping them.

### Operational tools

Named, invokable actions that trigger WP operational behaviours. These are tools in the framework sense — Tools owns what a tool is and how tools are authored (the invocability test, the authoring standard); WP owns these specific tools because they invoke WP behaviours.

**Confirmed tools (working labels — names are the human's to set):**

- **Full stop** — session over; strongest capture-and-place sweep
- **Checkpoint and continue** — a natural break; flush content plus a handoff of current position and next steps
- **Flush without closing** — commit to WIP, or push to masters plus binder, while the chat continues
- **/more** — expand the current prompt with additional detail (AI-presented prompts are concise by default)

**A deployment output:** a summary reference guide listing all active operational tools and what they do, maintained as tools are added or modified.

### File delivery rules

Two rules based on the platform's file-access capability, not named surfaces:

1. **No direct file access** (downloadable delivery) — when outputting an updated file for download, instruct the user where to save it based on the path in the document header.
2. **Direct file access** — check the file's physical location against the path in the header; move it if they disagree.

### Overview-first working discipline

The generic discipline of staying at the overview level until it could drive excellent execution, probing rather than diving. This is broader than design — it applies to any work where there is a temptation to descend into detail before the shape is clear. Project Design owns the design-specific application in its standard; WP states the generic behaviour.

The discipline is consumed by the Assurance component as one of its proactive conventions — an effective overview reduces misalignment and drift.

---

## Working State

Where content lives while in motion, and how work is tracked, progressed, and completed.

### WIP

The framework's transactional staging mechanism. Three roles:

**1. Homeless shelter** — temporary home for content that doesn't yet have a destination. The discipline: nothing stays by default. If something looks permanently resident in WIP, that is a signal to address it — work out where it belongs and move it there.

**2. Persisted working memory** — current thinking, current working state, things that need to survive across chats and sessions. This is the continuity mechanism — the AI's memory between sessions for content that is actively being worked.

**3. Transactional staging** — confirmed or pending changes to master documents, held here until written. A master is not authoritative alone between updates. Reading a master means checking WIP for pending content and working from a merge of both. This keeps heavy churn in one document rather than thrashing the whole corpus.

**Multiple WIPs.** WIP supports multiple documents in use simultaneously, broken up to manage size and subject. Usually obvious which applies in a given situation; if not, ask which is primary or which to use for a given piece of information.

**Not in binders.** WIP is loaded directly into context, not via the binder mechanism. The binder is persisted memory of the confirmed state; WIP is the working state that may not yet be confirmed.

**Visibility over location.** WIP files commonly live at the documentation root folder, but that is not a rule. The real requirements: easy to find, easy to save to, easy to load into context. Easily visible so they are known and not forgotten.

**WIP tracking.** A register of active WIP documents prevents orphaned or neglected content. The natural home for this register is the project's index document — it already indexes what a scope contains.

**WIP lifecycle.** WIP documents hold short-to-medium-life content in a potentially long-life document. The document itself can persist as long as it is useful; the content within it should flow through to its destination and not accumulate.

### Working documents

Content that needs its own working space. Used when volume exceeds what open items can hold, or when content needs dedicated room for development. The escalation from open items to a working document is governed by the split test: externalise when keeping content in its host would compromise the host's primary role.

WP owns three process document types that serve the working process:

- **Working document** — holds incomplete material, confirmed items awaiting placement, and in-progress thinking
- **Report** — a process document recording findings, analysis, or review results
- **Resource** — a reference or knowledge document supporting the work

These are workflow documents, not design outputs. Documentation Methodology owns the doctype mechanics; Working Practices owns these specific types because they serve the working process.

### Work items

A generic entity flowing through a workflow. A thing noticed that needs to be tracked, discussed, resolved, or acted on.

**Two axes:**

- **Type** — what kind of thing it turned out to be, determined on judgement. Types are not enumerated in advance; capture-and-place surfaces the real type list over time, and types are recorded as an output of that work, not an input to it.
- **State** — open, current, closed. These are views, not different entities: "the open work items" is a filter, not a separate list.

**Five fates** — what can become of a work item, chosen by the session on context:

- Dealt with in conversation, leaving no trace (it warranted none)
- Resolved and recorded as a decision (reasoning worth keeping)
- Parked as an open item (live but unresolved)
- Captured into WIP (active thinking mid-flight)
- Becomes committed work in a work register

**The governing rule: no knowledge lost.** A work item may be dropped, but only by a decision that it carries nothing worth keeping. Escalation is a judgement; disappearance is not an accident.

**Defined concept, scalable implementation.** A session may realise the work item model not at all, lightly, ad hoc, or in full — chosen by scale, severity, importance, and the nature of the workflow.

**Distinct from work register entries.** A work item is a generic entity flowing through a workflow. A work register entry is confirmed work owed under the Project Design commitment ledger. Different purpose, different owner (work register is Project Design), different state model. A register entry may originate from a design change with downstream impact or be directly entered — origin is not the distinguishing property. No subset relationship.

### Board

Supersedes the work plan (D10). A scoped record of work across its full lifecycle — from capture through completion. Boards is a part under WP with its own design and decisions — see `WP_Boards_`.

### Pending content rule

Confirmed content awaiting delivery to master documents. Held in WIP under the destination document's heading. The master is not the sole authority between updates — reading a master to act on it means checking its pending section in WIP first and working from the composite of both. This is the transactional staging role of WIP formalised as a rule.

**Composite authority rule:** the current truth is master + pending overlay. When pending content exists for a master, the effective state is the merge. Pending overlay wins where it explicitly changes master state; if the intended merged state cannot be determined unambiguously, surface the conflict rather than infer it. This is stated explicitly because the framework's other conventions (particularly Project Design's sufficiency contract) assume a single authoritative source. The pending content model is a deliberate exception — justified by the cost of thrashing the whole corpus on every confirmed change — and the merge rule is the mechanism that makes it work. Carry to Project Design: PD's "current confirmed model, sufficient on its own" contract needs an explicit acknowledgement that pending content may exist and the merge rule applies.

### Definition of done

Core states the framework-wide requirement: every component defines how its work completes, with a testable-or-assessable invariant. WP owns the definition-of-done block type — the mechanism consumers use to declare and check completion.

The block type defines what a definition of done contains, how it is structured, and how it is evaluated. It is used by PD in the brief, by component design passes in their own completion criteria, and by Build to check whether an outcome meets the stated bar.

Schema definition deferred (pending schema definitions task). The ownership and role are stated here; the formal block type properties land when the schema is authored.

### Development lifecycle

Phases and modes. Phases describe what kind of work is being done at a point in time: research, design, build, deploy, review. These are a general concept — any development process has them.

AIDE implements phases as modes. A mode is a state the AI session operates in, shaped by which standards and tools are loaded and active. The distinction matters because phases are general while modes are AIDE's specific mechanism for realising them.

WP owns the lifecycle concept because it describes how work progresses — a workflow concern. Individual modes are shaped by the components that own those phases — Project Design owns what happens during design, Build owns what happens during build.

---

## Content Delivery

How working and project context is assembled and delivered to the AI session, particularly binder-based context. This does not include capability packaging, triggering, or deployment — those are owned by Infrastructure (packaging) and Deployment (the pipeline to the session).

### Binder concept

WP owns the binder — the concept (why it exists, how it is used, what it includes, how it delivers content) and the doctype definition (its structure as a document type). WP knows most about the binder, so under Core's ownership rules the doctype belongs here, not with Documentation Methodology. Documentation Methodology owns the document structure mechanics that the binder doctype consumes.

### Three-tier inclusion model

Core Structure owns the three-tier file model — a framework-wide construct governing what lives in a project folder based on its relationship to the AI session. WP consumes it for binder assembly:

1. **In the binder** — needed for thinking and reasoning. The test: does it need to be there for thinking and reasoning? If so, include it.

2. **Known to the framework** — part of the project but not needed in context. Listed in the folder's index document. The framework knows it exists, can reference it, but does not load it.

3. **Just present** — incidental files. AIDE has no opinion.

The binder is the context-loading mechanism. The index is the awareness mechanism. Files that need neither are just files.

The key question for inclusion is not whether a file is a governed document, but whether it is needed for the work. A utility script that is the project's deliverable may belong in the binder when working on that utility, even though it has no declaration header.

---

## File Operations — DISSOLVED (D17)

The File Operations area was dissolved after review. Its six confirmed items from the 2026-09-10 session were grouped by subject ("files") rather than by purpose, and once redistributed to their natural owners no coherent area remained.

Content redistributed to:

- **WP component level** — file delivery rules (already placed above)
- **Core Structure** — archived folder convention; git-as-history decision (superseded-folder pattern dropped). Carried in `_rebuild/WP_CoreCarries_v2.md`.
- **Infrastructure** — utility git commit behaviour; FUP move action; version-cleanup deletion mechanism. Carried in WIP.
- **Build** — design-and-output separation principle as an unsettled leaning (not yet a decision), supplied as input for Build's design pass. Concrete output conventions remain for Build to determine. Captured in `_rebuild/Build_Input_Working_v1.md`.

The working document `Working Practices/FileOps/WP_FileOps_Working_v1.md` is superseded by this redistribution.

---

## Boundaries

WP owns generic operating behaviour and live state — the middle placement band.

**WP does not own:**

- The design method — Project Design
- How code is structured — Build
- Document structure, the definition contract, the split test as a rule — Documentation Methodology
- The component model, ownership rules, framework-wide requirements — Core
- Universal reasoning premises — Principles
- The work register — Project Design
- Trust conventions, the human working model, verification behaviours, drift detection, anomalies — Assurance
- Cross-platform transport and coordination — Orchestration

**WP owns:**

- Capture-and-place as the primary operational mechanism
- Operational tools that invoke WP behaviours (session transitions, flush, more)
- WIP model and conventions
- Work items, board (part — see `WP_Boards_`), open items, pending content
- Definition of done as a block type (Core states the framework-wide requirement)
- The development lifecycle concept (phases and modes)
- Process document types (working document, report, resource)
- The binder (concept, doctype, and assembly — three-tier model consumed from Core Structure)
- The overview-first working discipline (generic)
- File delivery rules

---

Version note: v6 — Work plan section replaced by Board reference; Boards added as a part under WP (WP_Boards_Design_v1, WP_Boards_Decisions_v1). Boundaries updated. 2026-09-17. Replaces v5.

Version note: v7 — round-3 cross-review remediation (N1): the standard's `uses` pointed at the deleted Standards_Authoring_Standard, a dependency from how the standard was authored, not from how it is applied. Replaced with `uses Standards_Consumption_Standard@v5`, the genuine runtime dependency (D22). 2026-09-24. Replaces v6.
