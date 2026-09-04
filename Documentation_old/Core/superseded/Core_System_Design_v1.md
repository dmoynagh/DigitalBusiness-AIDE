# AIDE — System Design

> **Version 1**. Defines the top-level documentation structure for AIDE.
>
> Created: 2026-08-28

---

## Documentation structure

AIDE documentation is organised under five top-level areas:

```text
AIDE/
├── Core/
├── Design/
├── Build/
├── Capabilities/
└── Environment/
```

The structure mirrors the conceptual organisation of the AIDE system.

- **Core** — system-wide material applying across AIDE.
- **Design** — methodology and material primarily concerned with design-side work.
- **Build** — methodology and material primarily concerned with build-side work.
- **Capabilities** — reusable standards, tools, scope, dependencies, migration, deployment, review, and related capability infrastructure.
- **Environment** — the AI development environment and its supporting structures.

Placement indicates the primary conceptual home of a topic. It does not prevent material from being used across Design, Build, or other AIDE contexts.

## Folder structure

Each top-level folder is **flat by default**.

Topic and document filenames provide the primary internal grouping. Subfolders are introduced only when the number or complexity of files makes a flat structure less effective.

This keeps the master documentation structure simple and supports whole-folder context refreshes without requiring recursive collection from many subfolders.

---

**Methodology:** v17
