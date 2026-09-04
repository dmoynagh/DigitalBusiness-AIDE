# Documentation Methodology — Index

> **Version 8** (2026-09-01). Review A R2 preflight correction: advances current generic Index
> consumption/conformance to `AIDE_Index@v2`; no semantic model change.
>
> Created: 2026-08-30 | Last modified: 2026-09-01

`{scope: "AIDE/Document Methodology", type: DocumentationTopic}`

## Contents

- **Documentation Methodology** — document/corpus naming, types, lifecycle, documentation-specific
  Index extensions and work-state document semantics.  
  `{standard: AIDE_DocumentationMethodology@v23}`

## Documentation

### Top-level topic

| Name | Parent topic | Filename prefix | Inheritance | Mode |
|---|---|---|---|---|
| Documentation Methodology | AIDE | `DocumentationMethodology` | independent | expanded |

### Document register

| Document | Version | Type | Status |
|---|---:|---|---|
| `DocumentationMethodology_Index` | v8 | Index | Current |
| `DocumentationMethodology_Design` | v20 | Design | Current confirmed internal model |
| `DocumentationMethodology_Decisions` | v21 | Decisions | Current |
| `AIDE_DocumentationMethodology_Standard` | v23 | Standard | Current; identity `AIDE_DocumentationMethodology@v23` |
| `DocumentationMethodology_Guide` | v23 | Guide | Current human/explanatory companion |

### DocumentationTopic Item Type

Defined by `AIDE_DocumentationMethodology@v23` and consumed through `AIDE_Index@v2`.

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

Do not mass-rewrite existing governed files solely to replace the old conceptual word `Project` in
filename rules where the existing filename already expresses the correct top-level-topic prefix.

### Local configuration

None.

### Superseded by this pass

| Current predecessor | Replacement |
|---|---|
| `DocumentationMethodology_Index_v7` | `DocumentationMethodology_Index_v8` |
| `DocumentationMethodology_Design_v19` | `DocumentationMethodology_Design_v20` |
| `DocumentationMethodology_Decisions_v20` | `DocumentationMethodology_Decisions_v21` |
| `AIDE_DocumentationMethodology_Standard_v22` | `AIDE_DocumentationMethodology_Standard_v23` |
| `DocumentationMethodology_Guide_v22` | `DocumentationMethodology_Guide_v23` |

---
Dependencies: !AIDE_DocumentationMethodology@v23, AIDE_Index@v2, DocumentationMethodology_Design_v20
References: DocumentationMethodology_Guide_v23
