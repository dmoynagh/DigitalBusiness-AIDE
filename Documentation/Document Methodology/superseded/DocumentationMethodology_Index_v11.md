# Documentation Methodology — Index

> **Version 11** (2026-09-01). Review B R2 closing correction: advances the current corpus to
> v26 to correct the two additional active capability-version references found in Round 2 and to
> refine D41's overbroad verification claim; no general reference/dependency policy is introduced.
>
> Created: 2026-08-30 | Last modified: 2026-09-01

`{scope: "AIDE/Document Methodology", type: DocumentationTopic}`

## Contents

- **Documentation Methodology** — document/corpus naming, types, lifecycle, documentation-specific
  Index extensions and work-state document semantics.  
  `{standard: AIDE_DocumentationMethodology@v26}`

## Documentation

### Top-level topic

| Name | Parent topic | Filename prefix | Inheritance | Mode |
|---|---|---|---|---|
| Documentation Methodology | AIDE | `DocumentationMethodology` | independent | expanded |

### Document register

| Document | Version | Type | Status |
|---|---:|---|---|
| `DocumentationMethodology_Index` | v11 | Index | Current |
| `DocumentationMethodology_Design` | v23 | Design | Current confirmed internal model |
| `DocumentationMethodology_Decisions` | v24 | Decisions | Current |
| `AIDE_DocumentationMethodology_Standard` | v26 | Standard | Current; identity `AIDE_DocumentationMethodology@v26` |
| `DocumentationMethodology_Guide` | v26 | Guide | Current human/explanatory companion |

### DocumentationTopic Item Type

Defined by `AIDE_DocumentationMethodology@v26` and consumed through `AIDE_Index@v2`.

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

Do not mass-rewrite existing governed files solely to replace the old conceptual word `Project` in
filename rules where the existing filename already expresses the correct top-level-topic prefix.

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
Dependencies: !AIDE_DocumentationMethodology@v26, AIDE_Index@v2, DocumentationMethodology_Design_v23
References: DocumentationMethodology_Guide_v26
