# Documentation Methodology — Index

> **Version 6** (2026-08-31). Adopts `AIDE_Index@v1`, records the v21 top-level-topic and live
> work-state model, and moves generic Index ownership to Core.
>
> Created: 2026-08-30 | Last modified: 2026-08-31

`{scope: "AIDE/Document Methodology", type: DocumentationTopic}`

## Contents

- **Documentation Methodology** — document/corpus naming, types, lifecycle, documentation-specific
  Index extensions and work-state document semantics.  
  `{standard: AIDE_DocumentationMethodology@v21}`

## Documentation

### Top-level topic

| Name | Parent topic | Filename prefix | Inheritance | Mode |
|---|---|---|---|---|
| Documentation Methodology | AIDE | `DocumentationMethodology` | independent | expanded |

### Document register

| Document | Version | Type | Status |
|---|---:|---|---|
| `DocumentationMethodology_Index` | v6 | Index | Current |
| `DocumentationMethodology_Design` | v18 | Design | Current confirmed internal model |
| `DocumentationMethodology_Decisions` | v19 | Decisions | Current |
| `AIDE_DocumentationMethodology_Standard` | v21 | Standard | Current; identity `AIDE_DocumentationMethodology@v21` |
| `DocumentationMethodology_Guide` | v21 | Guide | Current human/explanatory companion |

### DocumentationTopic Item Type

Defined by `AIDE_DocumentationMethodology@v21` and consumed through `AIDE_Index@v1`.

A DocumentationTopic represents one self-describing top-level documentation topic and resolves its
own governing Index/Document Register. A chat project/master folder may host one or several such
topics; the container boundary is not itself the semantic topic boundary.

### Migration state

- v18 — `OnUpdate` legacy structure/conformance transition.
- v19 — `None`.
- v20 — `None`.
- v21 — `None`; new Index/work-state/topic semantics apply prospectively/on substantive update.

Do not mass-rewrite existing governed files solely to replace the old conceptual word `Project` in
filename rules where the existing filename already expresses the correct top-level-topic prefix.

### Local configuration

None.

### Superseded by this pass

| Current predecessor | Replacement |
|---|---|
| `DocumentationMethodology_Index_v5` | `DocumentationMethodology_Index_v6` |
| `DocumentationMethodology_Design_v17` | `DocumentationMethodology_Design_v18` |
| `DocumentationMethodology_Decisions_v18` | `DocumentationMethodology_Decisions_v19` |
| `AIDE_DocumentationMethodology_Standard_v20` | `AIDE_DocumentationMethodology_Standard_v21` |
| `DocumentationMethodology_Guide_v20` | `DocumentationMethodology_Guide_v21` |

---
Dependencies: !AIDE_DocumentationMethodology@v21, AIDE_Index@v1, DocumentationMethodology_Design_v18
References: DocumentationMethodology_Guide_v21
