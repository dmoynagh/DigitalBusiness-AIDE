# Documentation Methodology — Index

> **Version 12** (2026-09-02). Registers Documentation Methodology v27 and the section/Knowledge/Binder navigation model.
>
> Created: 2026-08-30 | Last modified: 2026-09-02

`{scope: "AIDE/Document Methodology", type: DocumentationTopic}`

## Contents

- **Documentation Methodology** — document/corpus naming, types, lifecycle, documentation-specific
  Index extensions and work-state document semantics.  
  `{standard: AIDE_DocumentationMethodology@v27}`

## Documentation

### Top-level topic

| Name | Parent topic | Filename prefix | Inheritance | Mode |
|---|---|---|---|---|
| Documentation Methodology | AIDE | `DocumentationMethodology` | independent | expanded |

### Document register

| Document | Version | Type | Status |
|---|---:|---|---|
| `DocumentationMethodology_Index` | v11 | Index | Current |
| `DocumentationMethodology_Design` | v24 | Design | Current confirmed internal model |
| `DocumentationMethodology_Decisions` | v25 | Decisions | Current |
| `AIDE_DocumentationMethodology_Standard` | v27 | Standard | Current; identity `AIDE_DocumentationMethodology@v27` |
| `DocumentationMethodology_Guide` | v27 | Guide | Current human/explanatory companion |

### DocumentationTopic Item Type

Defined by `AIDE_DocumentationMethodology@v27` and consumed through `AIDE_Index@v2`.

A DocumentationTopic is the logical boundary/scope of one top-level documentation topic. Its
governing Index declares/describes that logical Item and is used to recognise and resolve its
Document Register; the Markdown Index file is not itself the semantic boundary. Subtopics remain
subordinate structures rather than separate DocumentationTopics. A chat project/master folder may
host one or several top-level DocumentationTopics. `AIDE_Domain` alone decides whether the Item Type
may establish or participate in Domain resolution.

### Migration state

- v18 — `OnUpdate` legacy structure/conformance transition.
- v19 — `None`.
- v20 — `None`.
- v21 — `None`; new Index/work-state/topic semantics apply prospectively/on substantive update.
- v22 — `None`; `DocumentationTopic` clarification and root-WIP series rule apply prospectively.
- v23 — `None`; current generic Index consumption/conformance corrected to `AIDE_Index@v2`.
- v24 — `None`; Review B R1 work-state/discoverability/owner-seam clarifications.
- v25 — `None`; pre-Round-2 correction aligns the current split-obligation seam with `AIDE_WorkPackage@v3` without changing ownership or adding a mechanism.
- v26 — `None`; Round 2 closing correction updates the two additional active in-body capability references and refines D41 without establishing general reference/dependency policy.
- v27 — `None`; section hosting, Knowledge, Documentation-Topic Binder boundaries and Index-led navigation apply prospectively/on substantive update.

Do not mass-rewrite existing governed files solely to replace the old conceptual word `Project` in
filename rules where the existing filename already expresses the correct top-level-topic prefix.

### Binder boundary

One top-level Documentation Topic Binder containing the five current masters; live state is loaded separately.

### Local configuration

None.

### Superseded by this pass

| Current predecessor | Replacement |
|---|---|
| `DocumentationMethodology_Index_v10` | `DocumentationMethodology_Index_v11` |
| `DocumentationMethodology_Design_v22` | `DocumentationMethodology_Design_v23` |
| `DocumentationMethodology_Decisions_v23` | `DocumentationMethodology_Decisions_v24` |
| `AIDE_DocumentationMethodology_Standard_v25` | `AIDE_DocumentationMethodology_Standard_v26` |
| `DocumentationMethodology_Guide_v25` | `DocumentationMethodology_Guide_v26` |

---
Dependencies: !AIDE_DocumentationMethodology@v27, AIDE_Index@v2, DocumentationMethodology_Design_v24
References: DocumentationMethodology_Guide_v27
