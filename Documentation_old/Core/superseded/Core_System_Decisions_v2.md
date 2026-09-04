# Core System — Decisions

> **Version 2** (2026-08-28). Adds system-wide formal identity, metadata-container ownership,
> and stable bootstrap/discovery decisions while preserving the original AIDE structure decisions.
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

## D8 — Formal AIDE identities are namespaced; internal topic and source names are not

**Decision.** Topic names and ordinary internal source-document filenames remain simple and do
not receive an `AIDE_` prefix merely because they belong to the AIDE system.

Formally referenceable, published, or deployed AIDE Standards, Tools, and similar artefacts use
an `AIDE_`-prefixed identity where they may be referenced outside their immediate local context.
Each may retain a common name for natural prose. Formal metadata and machine references use the
full identity; generated prose may use the common name where unambiguous and expand it when
needed.

**Reason.** Namespacing avoids collision when generic names such as `Tags` or `Standards` travel
into environments that contain unrelated capabilities with the same common names. Applying the
prefix to topics and source filenames would add noise without solving an identity problem.

---

## D9 — Referenceable artefacts may expose multiple identities

**Decision.** A referenceable artefact may expose a compact ordered identity list in header
metadata:

```text
Identity: primary-id@v2, alternate-id@v7, included-id
```

The first entry is primary. Later entries are alternate identities exposed by the same artefact.
Version, where present, belongs to the individual identity entry. Identity matching ignores
version; consumers compare version after identity resolution.

**Reason.** Documents, Standards, skills, bundles, and packages may legitimately be addressable
through more than one identity, and those identities may have different version meaning.
Separating identity resolution from version comparison lets a newer available capability still
resolve a dependency whose conformance checkpoint is older.

---

## D10 — Document methodology hosts metadata containers; block owners own their contents

**Decision.** Documentation Methodology owns generic header/footer metadata containers for
governed documents and the placement/format contract for adding blocks. The capability that uses
a metadata block owns that block's internal content and behaviour.

DocMeth therefore does not need to know about every future Tags, Dependencies, Review, or other
metadata block in order to host it.

**Reason.** A generic host/owner boundary keeps document structure coherent without turning
DocMeth into the semantic owner or registry for every capability that needs machine metadata.
The current Guide requires later reconciliation; the architectural boundary is established now.

---

## D11 — AIDE has a small stable bootstrap layer and generic `{bootstrap}` marker

**Decision.** AIDE maintains a short system configuration applied to every participating AI
environment. It contains stable system invariants and discovery conventions rather than
operational logic that changes frequently.

`{bootstrap}` is a system-level discoverability marker. The deployed system configuration tells
the AI, on a best-effort basis, to find and process available `{bootstrap}` blocks at session
start, and to process blocks on first discovery when the platform could not make them visible at
startup. Components own the instructions inside their own blocks.

**Reason.** Chat environments do not provide a universally enforceable session-start hook. A
small stable pointer layer gives changing capabilities the best chance of being considered
without copying their logic into every platform's permanent instructions. It can be strengthened
when a platform exposes better hooks without changing the component-level semantics.

---

**Depends on:** `Core_System_Design` v3.

**References:** `Capabilities_Design` v4.

**Methodology:** v17
