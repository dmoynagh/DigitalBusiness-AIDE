# Core System — Design

> **Version 2** (2026-08-28). Establishes AIDE as the umbrella AI-development system,
> records its top-level topic structure, and defines the master documentation layout.
>
> Created: 2026-08-28 | Last modified: 2026-08-28

---

## §1 — AIDE system boundary

**AIDE is the overall AI-development system.** Its parts provide methodology, capabilities,
environment structure, and shared foundations that may be used wherever they are applicable.

AIDE is distinct from the development/product domains that use it. Domains such as CMS, JSON,
and other application work consume AIDE; they are not components of AIDE.

The top-level AIDE structure is:

```text
AIDE
├── Core
├── Design
├── Build
├── Capabilities
└── Environment
```

Placement identifies a topic's primary conceptual home and owner. It does **not** create an
exclusive execution boundary. Material primarily owned by Design may be used on Build side and
vice versa. Cross-cutting Standards and Tools may apply on Design side, Build side, or both
according to their scope.

---

## §2 — Top-level topics

### Core

Holds system-wide foundations and reference material that concern AIDE as a whole.

Confirmed Core material includes:

- **Principles** — system-wide principles.
- **System** — the whole-system architecture, topic map, and other AIDE-wide structural
  information.

Core maintains a reference view of the AIDE topic structure for orientation. That reference
does not replace the authoritative designs of the individual topics.

### Design

Holds methodology and mechanisms primarily concerned with design-side work.

Documentation Methodology belongs under Design because document design and corpus management are
primarily design-side concerns. Build-side work may still consume Documentation Methodology
where it creates, reads, or updates governed documents.

### Build

Holds methodology and mechanisms primarily concerned with execution on Build side.

**WorkPackage** is a Build subtopic. It defines the standard design-side-to-build-side handoff,
execution, validation, and return model, including the WorkPackage Outcome.

Design side normally authors WorkPackages and consumes their returned Outcomes; Build side
normally executes them. The topic placement indicates primary concern, not exclusive use.

### Capabilities

Holds reusable AI-facing capability infrastructure:

- Standards
- Tools
- Scope
- Dependencies
- Migration
- Deployment
- Review

Capabilities may apply to Design side, Build side, or both. Applicability is a Scope concern,
not inferred from topic placement.

### Environment

Holds the AI development environment model and supporting structures. Detailed subtopics are
defined as the Environment architecture develops.

---

## §3 — Documentation structure

The master AIDE documentation folders mirror the top-level system structure:

```text
AIDE/
├── Core/
├── Design/
├── Build/
├── Capabilities/
└── Environment/
```

Each top-level folder is **flat by default**.

Topic and document filenames provide the primary internal grouping. Subfolders are introduced
only when the number or complexity of files makes a flat structure less effective.

This keeps the filesystem aligned with conceptual ownership while supporting whole-folder
project-context refreshes without requiring recursive collection from many subfolders.

Development/product domains such as CMS and JSON remain outside this AIDE documentation tree.

---

## §4 — Side and applicability

**Design side** and **Build side** are working contexts, not ownership silos.

A topic or capability may be primarily associated with one side while remaining available to the
other. For Standards and Tools, the capability's effective Scope determines whether it applies
to Design, Build, or both.

The default side for a capability is **both** unless its effective Build/Scope configuration
declares otherwise.

---

**Depends on:** None.

**References:** `Capabilities_Design` v3.

**Methodology:** v17
