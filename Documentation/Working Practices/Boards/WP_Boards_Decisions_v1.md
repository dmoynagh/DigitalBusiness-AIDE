> identity: WP_Boards_Decisions@v1 | doctype: decisions | updated: 2026-09-17

# Working Practices — Boards Decisions

## Summary

Reasoning and resolutions from the board design session. Five decisions covering the supersession of the work plan, the zone model, the separation from AIDE, the format choice, and the deferred cloud service.

---

## D1. Board supersedes work plan (WP D10)

The work plan addressed visibility of decided, current work as a block type in WIP with named workstreams (WP D10). The board evolved from it and supersedes it.

Key differences: five lifecycle zones replace a flat list — the board captures work from intake to completion, not just current focus; scoped and multiple (one board per scope, each its own document) replaces named workstreams within a single plan; structured tasks with IDs, dependencies, who, sub-items, tags, and work sets replace plain-text entries; self-contained HTML format with collapsible sections; dashboard as cross-board aggregation on demand.

The board is a doctype, not a block type. It earned its own document and its own part under WP. The work plan block type is retired.

## D2. Five zones, not a state field

The original brief described the board as a record of current work only. In practice, there is no other easy place to capture and stage tasks across their full lifecycle. The board absorbs intake through completion: inbox, future, pending, current, done.

The zones are a staging model, not a pipeline with gates. Shortcuts are normal — urgent work goes straight to current. The flow is a default, not a constraint.

A "blocked" condition is not a sixth zone. It is expressed through unresolved dependencies on a current or pending task. A task with an unmet dependency is visibly blocked without needing a separate state.

## D3. Board is a standalone tool, not an AIDE construct

The board originated in the WP design pass as an AIDE convention. During design it became clear the board serves any project, not just AIDE work. It was separated from AIDE's internal constructs — it is not a block type, not a DocMeth grammar element, not an AIDE-specific convention.

AIDE is the primary consumer. WP owns the doctype because the board is working state and the maintenance behaviour is capture-and-place. But the board's value is independent of AIDE — any project scope can have one.

## D4. HTML format with collapsible sections

Markdown was considered and prototyped first. HTML was chosen because the `<details>` / `<summary>` element provides native collapse/expand without JavaScript, giving the board an interactive tree view in any browser.

The HTML structure is semantic enough for the AI to parse and update through text operations — finding a task by ID, changing its zone, or marking a dependency resolved. The format serves both human reading (browser view) and AI writing (structured text updates).

Dark mode follows system preference via CSS media query.

## D5. Cloud service deferred — document-first

The architecture for a cloud service was designed: Azure SQL Database (Basic tier), Azure App Service (Free F1), ASP.NET Core MCP server for AI access from any surface. Estimated cost ~NZ$8–10/month.

Deferred to demonstrated need. The board works now as a document maintained through normal file operations. The cloud service earns its place when the board needs live access from Chat sessions or when multiple non-AIDE boards need cross-board aggregation that file-based access cannot serve.

The task model and properties are unchanged by the persistence choice — the same board, different storage.

---

Version note: v1 — initial decisions from the board design session. 2026-09-17.
