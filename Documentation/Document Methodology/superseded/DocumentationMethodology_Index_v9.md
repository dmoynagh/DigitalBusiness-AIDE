# Documentation Methodology — Index

> **Version 9** (2026-09-01). Review B R1 remediation: advances the current Documentation
> Methodology corpus to v24 and records the clarified work-state/discoverability semantics.
>
> Created: 2026-08-30 | Last modified: 2026-09-01

`{scope: "AIDE/Document Methodology", type: DocumentationTopic}`

## Contents

- **Documentation Methodology** — document/corpus naming, types, lifecycle, documentation-specific
  Index extensions and work-state document semantics.  
  `{standard: AIDE_DocumentationMethodology@v24}`

## Documentation

### Top-level topic

| Name | Parent topic | Filename prefix | Inheritance | Mode |
|---|---|---|---|---|
| Documentation Methodology | AIDE | `DocumentationMethodology` | independent | expanded |

### Document register

| Document | Version | Type | Status |
|---|---:|---|---|
| `DocumentationMethodology_Index` | v9 | Index | Current |
| `DocumentationMethodology_Design` | v21 | Design | Current confirmed internal model |
| `DocumentationMethodology_Decisions` | v22 | Decisions | Current |
| `AIDE_DocumentationMethodology_Standard` | v24 | Standard | Current; identity `AIDE_DocumentationMethodology@v24` |
| `DocumentationMethodology_Guide` | v24 | Guide | Current human/explanatory companion |

### DocumentationTopic Item Type

Defined by `AIDE_DocumentationMethodology@v24` and consumed through `AIDE_Index@v2`.

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

Do not mass-rewrite existing governed files solely to replace the old conceptual word `Project` in
filename rules where the existing filename already expresses the correct top-level-topic prefix.

### Local configuration

None.

### Superseded by this pass

| Current predecessor | Replacement |
|---|---|
| `DocumentationMethodology_Index_v8` | `DocumentationMethodology_Index_v9` |
| `DocumentationMethodology_Design_v20` | `DocumentationMethodology_Design_v21` |
| `DocumentationMethodology_Decisions_v21` | `DocumentationMethodology_Decisions_v22` |
| `AIDE_DocumentationMethodology_Standard_v23` | `AIDE_DocumentationMethodology_Standard_v24` |
| `DocumentationMethodology_Guide_v23` | `DocumentationMethodology_Guide_v24` |

---
Dependencies: !AIDE_DocumentationMethodology@v24, AIDE_Index@v2, DocumentationMethodology_Design_v21
References: DocumentationMethodology_Guide_v24
