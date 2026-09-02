# Core System — Design

> **Version 3** (2026-08-28). Adds the system-wide formal-identity convention, shared
> referenceable-artifact identity model, generic document metadata-container boundary, and the
> small stable AIDE bootstrap layer.
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
- Tags
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

## §5 — Formal identities and referenceable artefacts

Internal architecture names stay short and readable. Topic names and ordinary source-document
filenames are **not** prefixed merely because they belong to AIDE.

Anything that is formally referenceable, published, deployed, or exposed outside its immediate
working context uses a namespaced AIDE identity where collision is plausible. The standard
namespace is `AIDE_`.

Examples:

```text
Topic / source name        Formal identity
Tags                       AIDE_Tags
Scope                      AIDE_Scope
Dependencies               AIDE_Dependencies
Standards                  AIDE_Standards
```

The formal identity is authoritative for machine references. A common name remains valid in
ordinary prose, and AI may expand the common name to the formal identity where disambiguation is
needed.

A referenceable artefact may expose more than one identity in compact header metadata:

```text
Identity: primary-id@v2, alternate-id@v7, included-id
```

The first entry is the primary identity. Later entries are alternate identities exposed by the
same artefact. A version, where present, belongs to that identity entry. Identity matching is by
name; version comparison is a separate operation performed by the consumer that needs it.

The identity convention applies to documents, Standards, Tools/skills, packages, and other
referenceable artefacts. It does not require incidental or unmanaged files to invent identities.

---

## §6 — Document metadata-container boundary

Documentation Methodology owns the generic **header metadata** and **footer metadata** containers
for governed documents: where they appear, how blocks are hosted, and the common formatting rules
for adding them.

The capability that contributes a metadata block owns the block's contents and semantics.
Documentation Methodology does not need to enumerate or understand every future block.

Conceptually:

```text
DocMeth
  → defines the metadata containers and placement rules

AIDE_Tags
  → uses a footer metadata property it owns

AIDE_Dependencies
  → uses a footer metadata property it owns

Identity
  → uses header metadata
```

The current DocMeth Guide predates this generic boundary; reconciliation is intentionally deferred
to the separate Documentation Methodology review.

---

## §7 — System bootstrap configuration

AIDE has a **small, stable system bootstrap layer** deployed to every participating AI
environment. It should contain only durable system invariants and discovery conventions, and
should change rarely or ideally not at all. Operational behaviour that changes belongs in the
Standards, Tools, or other capability definitions the bootstrap layer points to.

`{bootstrap}` is the generic AIDE marker for instructions requiring elevated early-session
consideration. The system configuration instructs the AI, on a best-effort basis, to discover and
process available `{bootstrap}` blocks at session start before substantive work. If a block is not
available until later, it is processed when first discovered.

The marker itself carries no component-specific semantics. Dependencies, Migration, Environment,
or another component may contribute a bootstrap block; the component owns the block content.

Each target platform uses its strongest available persistent mechanism—custom/project
instructions, platform instructions, package/plugin guidance, repository instructions, or an
equivalent—to establish the bootstrap rule. Platform implementation must not claim stronger
enforcement than the platform actually provides.

---

**Depends on:** None.

**References:** `Capabilities_Design` v4.

**Methodology:** v17
