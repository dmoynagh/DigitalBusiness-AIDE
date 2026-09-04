# Documentation Methodology — Decisions

> **Version 16** (2026-08-31). Retains the v18 reconciliation decisions and records the
> Documentation Methodology Design/Standard production and legacy-v17 migration bridge.
>
> Created: 2026-08-30 | Last modified: 2026-08-31

## D1 — Metadata containers are generic hosts

**Decision.** DocMeth owns placement/coexistence/compact rendering for header metadata, temporary
state and footer metadata. Contributing owners retain semantics.

## D2 — Documentation Methodology conformance is a Dependency

**Decision.** Retire the special `Methodology: vN` footer from v18. A document records its
saved/proven DocMeth conformance through `AIDE_Dependencies`.

**Reason.** This removes a duplicate version-gap/checkpoint mechanism and lets Migration govern
Required/OnUpdate/None transitions consistently.

## D3 — v18 migration posture is OnUpdate

**Decision.** v18 is `OnUpdate`.

**Reason.** v17 documents remain safely readable. The metadata/conformance model should be applied
when a document is next changed rather than forcing a corpus-wide rewrite merely to refresh
metadata. An operation that explicitly requires v18-only semantics can require migration first.

## D4 — Tags and Dependencies are hosted, not redefined

**Decision.** `Tags:` and `Dependencies:` are footer properties hosted by DocMeth. Their internal
grammar/build/query/conformance semantics remain with `AIDE_Tags` and `AIDE_Dependencies`.

## D5 — Identity is header metadata

**Decision.** Formal Core `Identity:` metadata is hosted in the header container where a governed
document exposes a referenceable identity. Filename and formal identity remain distinct.

## D6 — Temporary state is compact and owner-labelled

**Decision.** An optional temporary state container is placed near the top of the document.
Entries require stable owner identity plus concise human-readable title/message. The owner alone
defines lifecycle/content.

## D7 — WorkPackage execution semantics move to Build

**Decision.** DocMeth retains WorkPackage/Outcome document naming and archive integration but
delegates generic WorkPackage contract/execution/validation/return semantics to
`AIDE_WorkPackage@v1` and `AIDE_Build@v1`.

## D8 — Machine content remains compact

**Decision.** Metadata, derived state and generated operational content should be as compact as
practicable in human-readable documents.

## D9 — Re-establish a current Documentation Methodology Design

**Decision.** `DocumentationMethodology_Design_v15` is the confirmed internal model from which
the current published outcomes are produced.

**Reason.** A distributable outcome should have an authoritative defining source. The v18 Guide
already describes Design as the confirmed internal position; the operational closure package had
not included the older Design master.

## D10 — Publish a canonical Documentation Methodology Standard

**Decision.** Produce `AIDE_DocumentationMethodology_Standard_v1` with formal capability identity
`AIDE_DocumentationMethodology@v18`.

**Reason.** Documentation Methodology is reusable AI-facing behavioural infrastructure and should
use the same Design → canonical Standard → Build/Deployment path as other AIDE capabilities.

## D11 — Retain the Guide as a human companion

**Decision.** `DocumentationMethodology_Guide_v18` remains the human-readable explanatory outcome.
It is not replaced by the Standard.

**Reason.** The Standard is the concise AI operating contract; the Guide carries richer examples,
rationale and detailed explanatory material. Both derive from the same Design.

## D12 — Documentation Methodology Standard version follows the established methodology release

**Decision.** The canonical Standard for the current methodology release is
`AIDE_DocumentationMethodology_Standard_v18.md` with formal identity
`AIDE_DocumentationMethodology@v18`.

**Reason.** Documentation Methodology already has an established release lineage through v18.
Using `_v1` for the first Standard representation creates an unnecessary second visible version
number for the same methodology state. Aligning the Standard filename with the methodology
release preserves continuity and makes the Standard/Guide pair visibly one release.

**Scope.** This does not collapse the general distinction between document version, capability
release version, package identity, and deployment state. It is a deliberate alignment for this
existing methodology lineage.

## D13 — Legacy `Methodology: v17` supplies the migration starting checkpoint

**Decision.** For the v17→v18 transition only, where no Documentation Methodology dependency
checkpoint exists, an unambiguous legacy `Methodology: v17` declaration is interpreted by
Migration as proven conformance through `AIDE_DocumentationMethodology@v17`.

The interpretation is read-only until a qualifying update/save. Successful migration writes the
v18 dependency checkpoint and removes the legacy line.

**Reason.** v17 predates the generic Dependencies checkpoint. Without this bridge the v18
transition describes the target change but does not mechanically define where Migration obtains
the old conformance checkpoint.

## D14 — No dedicated Documentation Methodology Tool yet

**Decision.** Do not create a DocMeth-specific Tool at this stage.

**Reason.** The demonstrated actions are already owned by generic capabilities such as Migration,
Build Capability and Review. A new Tool without a distinct repeated action contract would add
machinery rather than capability.

## D15 — The common Bundle becomes the normal operational distribution

**Decision.** Include the Documentation Methodology Standard in the common AIDE Standards/Tools
Bundle. Once a project has that Bundle, the Guide is not separately required merely to obtain
operational DocMeth behaviour.

**Reason.** This makes the methodology deployable through the same common operating environment
as the other AIDE Standards/Tools while preserving the Guide as the richer human companion.

---
Dependencies: !AIDE_DocumentationMethodology@v18, DocumentationMethodology_Design_v15
References: DocumentationMethodology_Guide_v18, AIDE_Dependencies@v2, AIDE_Migration@v1
