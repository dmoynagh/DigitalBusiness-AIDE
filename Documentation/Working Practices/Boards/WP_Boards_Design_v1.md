> identity: WP_Boards_Design@v1 | doctype: design | updated: 2026-09-17

# Working Practices — Boards Design

## Summary

A board is a scoped record of work across its full lifecycle — from capture through to completion. One board per scope. Each board is its own document, held in the documentation root of its scope. Maintained by the AI as part of capture-and-place. Human-readable, AI-parseable.

The board supersedes the work plan (WP D10). Same purpose — visibility of decided work — elevated from a block type in WIP to a scoped doctype with its own document, structured task model, and lifecycle zones.

---

## Brief

### Problem

A session needs to orient quickly — what are we working on, what's the state of each piece, what order, what's blocked. Without a defined record, orientation means reading long documents and reconstructing position from memory.

### Purpose

Give any session — human or AI — immediate visibility of current work within a scope, without reading everything else.

### Objectives

1. Record decided work with enough structure for the AI to orient a session, track dependencies, and present filtered views.
2. Capture work from intake through completion — not just the current focus.
3. Support multiple scopes with independent boards and cross-board aggregation.
4. Keep the human burden near zero — the AI maintains the board as part of working practice.

### Definition of done

The board doctype is defined with properties and zones. The AI maintenance behaviour is stated. The format is settled. A working board exists for the AIDE Framework scope.

---

## Model

### What a board is

A scoped, ordered list of tasks across five lifecycle zones, maintained by the AI, readable by anyone. It answers: what are we doing, what's next, what's waiting, what's done.

It is not a project plan, a backlog, or a Gantt chart. It is not a work register — the register is PD's commitment ledger for design-to-build obligations. It is not WIP — WIP is transactional staging and working memory. The board is the "what are we doing" layer that sits alongside them.

### Scope

Each board covers one scope — a project, a solution, a component cluster, a personal initiative. The scope is declared on the board, not derived. One board per scope; no nesting of boards.

### Five zones

Zones stage work from intake to completion:

- **Inbox** — fast capture. A task with just a name, allocated to a zone later. A board's inbox holds tasks that belong to this scope but haven't been defined properly yet.
- **Future** — recorded and placed, not in play. Work acknowledged but not picked up. Long, medium, or short term — not currently active.
- **Pending** — ready to be drawn into current. Next in line. "What's pending?" draws from here.
- **Current** — the immediate working context. This session, today, the next few days. The orientation view — what the AI reads at session start.
- **Done** — completed. Stays for reference until cleared.

The general flow is inbox → future → pending → current → done, but shortcuts are normal. Something urgent goes straight to current. Something in future may jump to current when circumstances change. The zones are a staging model, not a pipeline with gates.

### Task properties

A task on a board has:

- **Name** — what it is.
- **ID** — a short code for cross-referencing in dependencies (e.g. `WP-STD`, `PD-UPD.1`).
- **State** — which zone the task is in.
- **Order** — position within zone. Matters most in current and pending; looser in future.
- **Dependencies** — what must be true before this task can start. Another task by ID, an external event, or a person delivering something. Resolved dependencies are marked.
- **Who** — a person or agent this task depends on or is assigned to.
- **Sub-items** — children of a task. The parent completes when its children complete.
- **Work sets** — a parent task whose children execute in parallel with no dependency between them. The set completes when all members complete. Not a separate mechanism — expressed as sub-items with no inter-dependency, parent marked as a set.
- **Categories/tags** — what kind of work. Enables cross-board filtering and dashboard views.
- **Completion link** — pointer to what happens next when this task is done.
- **Notes** — anything else: context, blocking detail, description.

### Parallel items

No separate concept. Parallel items are sub-items with no dependency between them — all in play at once, parent completes when all children complete. Where sequencing matters, dependencies express it. Work sets are the named pattern for this.

### Dashboard

A rendered view across boards, assembled on demand. Filtered by zone, tags, who, dependency state, or any task property. Not a stored record — the AI reads the boards in scope and presents the aggregated picture.

---

## Maintenance

### AI responsibility

The board is maintained by the AI as part of capture-and-place. This is not a separate admin step — it is how the AI manages working state.

- **Session start** — read the relevant board's current zone. Orient from it.
- **During work** — when work is agreed, add it. When work completes, update state. When dependencies resolve, mark them. When new tasks surface, capture to inbox or the appropriate zone.
- **Session end** — the board reflects what happened. Part of the capture-and-place sweep.

### Handling

Outside binders — same churn handling as WIP. The board is high-churn content maintained continuously. Including it in binders would force rebuilds on every task state change.

### Document sync

A board can be rendered to a document in a documentation project, giving any session working on that project the current picture without needing live service access. The board document is a projection of the board state.

**Board is master.** The document is a rendered view with optional write-back.

**One-way is the baseline.** The AI renders the board to a document on demand, at a trigger, or on a schedule.

**Two-way adds write-back with conflict rules:**

- Item added to doc → pushed to board on next sync
- Item completed in doc → synced to board
- Item changed → most recent wins
- A change counter on the doc provides optimistic locking
- Structural changes resolve automatically; content conflicts at both ends are surfaced

The document format serves both directions — the same format one-way render produces is what two-way sync consumes. No format migration when write-back lands.

---

## Format

Self-contained HTML. Collapsible `<details>` / `<summary>` sections per task. Zones as top-level sections. Tasks as structured items within each zone.

- **Collapsed view** — ID and name only. Enough to scan.
- **Expanded view** — description, dependencies, sub-items, tags, notes. The full picture.
- **Work sets** — parent with nested children.
- **Dependencies** — reference task IDs, show resolved state.
- **Dark mode** — follows system preference.

Human-readable in any browser. AI-parseable for updates — the HTML structure is semantic enough that finding a task by ID, changing its zone, or marking a dependency resolved are straightforward text operations.

---

## Relationship to existing concepts

- **WIP** — the board lives alongside WIP, not inside it. Both are working state; WIP is transactional staging and working memory, the board is task tracking.
- **Work register** — PD's commitment ledger. A register entry might appear on a board when picked up as active work. Different purpose, different owner.
- **Open items** — parked, unresolved things. Not on the board unless brought into play. An open item that becomes decided work moves to the board.
- **Work items** — the generic workflow entity. A work item may be placed on the board for tracking alongside any of its five fates (dealt with, decision, open item, WIP, work register). The board is a tracking mechanism, not a fate — a work item on a board may also be in a work register, in WIP, or parked as an open item.

---

## Boundaries

The board does not own:

- **The work item model** — WP Working State. The board consumes work items; it does not define them.
- **The work register** — Project Design. Different purpose and lifecycle.
- **Document structure** — Documentation Methodology owns the doctype mechanics.
- **How the board is deployed as a service** — Infrastructure, when the cloud service is built.

The board owns:

- The zone model and task properties
- The document format and structure
- The maintenance behaviour (as a capture-and-place convention)
- The dashboard concept (cross-board aggregation)
- The document sync model

---

## Future development

The board is designed to serve as a document maintained by the AI through normal file operations. The architecture for a cloud service (Azure SQL + App Service + MCP server) has been settled but is deferred until demonstrated need beyond the documentation project. When built, the board model and task properties are unchanged — only the persistence and access layer changes.

---

Version note: v1 — initial design from the board design session. Supersedes the work plan (WP D10). 2026-09-17.
