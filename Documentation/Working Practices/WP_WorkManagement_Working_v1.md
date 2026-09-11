Working Practices — Work Management | working | WP_WorkManagement_Working@v1 | 2026-09-10

## Development lifecycle — phase vs mode (confirmed 2026-09-09)

The development lifecycle has stages: research, design, build, deploy, review. These are **phases** — they describe what kind of work is being done at a point in time.

AIDE implements these phases as **modes**. A mode is a state the AI session operates in, shaped by which standards and tools are loaded and active. The distinction matters because phases are a general concept (any development process has them) while modes are AIDE's specific mechanism for making them real in a session.

The lifecycle concept is owned by Working Practices because it describes how work progresses — it is a workflow concern. Individual modes (the design mode, the build mode) are shaped by the components that own those phases — Project Design owns what happens during design, Build owns what happens during build.

## Pending content — items awaiting placement

The following confirmed items need design work before they can be placed in this document:

- **Work items** — the generic workflow entity (settled 2026-09-07, owned by WP). Definition, two axes (type and state), four states (open, current, closed, plus any additions). Full content is in the settled rebuild decisions
- **Definition of done** — generic block type owned by WP. The testable-or-assessable invariant. Full content in settled rebuild decisions
- **Pending content rule** — WIP holds current state AND pending content for unwritten masters. A master is not authoritative alone between updates. Full content in WIP v22
- **WP1–WP13** — the original Working Practices design items from the old corpus, to be reconciled against current decisions per finding F10 in the rebuild guide

---

Version note: v1 — initial working document from sessions 2026-09-09 and 2026-09-10.
