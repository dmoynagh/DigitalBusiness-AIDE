# Core System — Decisions

> **Version 1** (2026-08-28). Records the decisions establishing AIDE as the umbrella
> AI-development system and its top-level topic/documentation structure.
>
> Created: 2026-08-28 | Last modified: 2026-08-28

---

## D1 — AIDE is the umbrella AI-development system

**Decision.** AIDE is the overall AI-development system. Core, Design, Build, Capabilities, and
Environment are top-level parts of AIDE and may be consumed wherever applicable.

Development/product domains such as CMS and JSON are outside AIDE. They use AIDE to perform
their work but are not components of the AI-development system.

**Reason.** Using AIDE as the umbrella gives one name to the system being built while preserving
clear homes for system-wide foundations, design methodology, build methodology, reusable
capabilities, and environment concerns.

---

## D2 — Top-level AIDE topic structure

**Decision.** The top-level AIDE topics are:

```text
AIDE
├── Core
├── Design
├── Build
├── Capabilities
└── Environment
```

**Reason.** The structure separates conceptual ownership without turning Design and Build into
hard usage boundaries.

---

## D3 — Core owns whole-system material

**Decision.** Core holds information about AIDE as a whole. Principles belongs in Core. Core also
maintains a reference view of the topic/system structure for orientation and documentation ease.

**Reason.** System-wide principles and maps do not naturally belong to Design, Build,
Capabilities, or Environment. `Core` describes shared foundational ownership more accurately than
`Common` or `Global`.

---

## D4 — Documentation Methodology belongs under Design

**Decision.** Documentation Methodology is placed under the top-level Design topic because it is
primarily a design-side proposition.

This does not prevent Build-side use of its rules or document types.

**Reason.** Topic placement identifies primary concern and ownership, not an exclusivity
boundary.

---

## D5 — WorkPackage belongs under Build

**Decision.** WorkPackage becomes a subtopic of the top-level Build topic and will be developed
as its own Standard/topic.

It defines the generic design-side-to-build-side handoff and return model. A WorkPackage
execution returns a WorkPackage Outcome recording success, partial success or failure, reasons,
validation, produced artefacts, deviations, observations, and feedback needed to continue or fix
the work.

**Reason.** WorkPackage is a generic build-execution mechanism used by capability production and
code production; it is not specifically a Capabilities mechanism.

---

## D6 — Topic placement does not restrict side usage

**Decision.** Design side and Build side are working contexts rather than ownership silos.
Material may be used across sides where its Scope says it applies. Standards may apply to Design,
Build, or both.

**Reason.** A methodology's conceptual owner and its runtime applicability answer different
questions. Conflating them would force cross-cutting capability material into the wrong topic.

---

## D7 — Master documentation mirrors the top-level AIDE structure

**Decision.** The master AIDE documentation root mirrors the five top-level AIDE topics:

```text
AIDE/
├── Core/
├── Design/
├── Build/
├── Capabilities/
└── Environment/
```

Each folder remains flat by default. Filenames/topic prefixes provide internal grouping;
subfolders are added only when scale makes them useful.

**Reason.** The physical structure remains legible while whole-folder context refresh remains
simple.

---

**Depends on:** `Core_System_Design` v2.

**References:** `Capabilities_Design` v3.

**Methodology:** v17
