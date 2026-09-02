# Documentation Methodology — Index

> **Version 7** (2026-09-01). Records the v22 Review A `DocumentationTopic` seam clarification and
> the single top-level-topic WIP-series convention.
>
> Created: 2026-08-30 | Last modified: 2026-09-01

`{scope: "AIDE/Document Methodology", type: DocumentationTopic}`

## Contents

- **Documentation Methodology** — document/corpus naming, types, lifecycle, documentation-specific
  Index extensions and work-state document semantics.  
  `{standard: AIDE_DocumentationMethodology@v22}`

## Documentation

### Top-level topic

| Name | Parent topic | Filename prefix | Inheritance | Mode |
|---|---|---|---|---|
| Documentation Methodology | AIDE | `DocumentationMethodology` | independent | expanded |

### Document register

| Document | Version | Type | Status |
|---|---:|---|---|
| `DocumentationMethodology_Index` | v7 | Index | Current |
| `DocumentationMethodology_Design` | v19 | Design | Current confirmed internal model |
| `DocumentationMethodology_Decisions` | v20 | Decisions | Current |
| `AIDE_DocumentationMethodology_Standard` | v22 | Standard | Current; identity `AIDE_DocumentationMethodology@v22` |
| `DocumentationMethodology_Guide` | v22 | Guide | Current human/explanatory companion |

### DocumentationTopic Item Type

Defined by `AIDE_DocumentationMethodology@v22` and consumed through `AIDE_Index@v1`.

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

Do not mass-rewrite existing governed files solely to replace the old conceptual word `Project` in
filename rules where the existing filename already expresses the correct top-level-topic prefix.

### Local configuration

None.

### Superseded by this pass

| Current predecessor | Replacement |
|---|---|
| `DocumentationMethodology_Index_v6` | `DocumentationMethodology_Index_v7` |
| `DocumentationMethodology_Design_v18` | `DocumentationMethodology_Design_v19` |
| `DocumentationMethodology_Decisions_v19` | `DocumentationMethodology_Decisions_v20` |
| `AIDE_DocumentationMethodology_Standard_v21` | `AIDE_DocumentationMethodology_Standard_v22` |
| `DocumentationMethodology_Guide_v21` | `DocumentationMethodology_Guide_v22` |

---
Dependencies: !AIDE_DocumentationMethodology@v22, AIDE_Index@v1, DocumentationMethodology_Design_v19
References: DocumentationMethodology_Guide_v22
