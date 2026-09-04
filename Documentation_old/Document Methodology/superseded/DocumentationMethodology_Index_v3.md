# Documentation Methodology — Index

> **Version 3** (2026-08-31). Registers the restored current Design and the canonical
> Documentation Methodology Standard while retaining the v18 Guide as the human companion.
>
> Created: 2026-08-30 | Last modified: 2026-08-31

## Project identity

**Topic:** Documentation Methodology  
**Master folder / GPT Project:** `AIDE/Document Methodology/`  
**Published capability identity:** `AIDE_DocumentationMethodology@v18`

## Topic declaration

| Name | Parent concern | Filename prefix | Inheritance | Mode |
|---|---|---|---|---|
| Documentation Methodology | AIDE / Project-design methodology | `DocumentationMethodology` | independent | expanded |

## Document register

| Document | Version | Type | Status |
|---|---:|---|---|
| `DocumentationMethodology_Index` | v2 | Index | Current |
| `DocumentationMethodology_Design` | v15 | Design | Current confirmed internal model |
| `DocumentationMethodology_Decisions` | v16 | Decisions | Current |
| `AIDE_DocumentationMethodology_Standard` | v18 | Standard | Current canonical AI-facing outcome; identity `AIDE_DocumentationMethodology@v18` |
| `DocumentationMethodology_Guide` | v18 | Guide | Current human/explanatory companion |

## Output model

```text
DocumentationMethodology_Design
        ├── AIDE_DocumentationMethodology_Standard
        └── DocumentationMethodology_Guide
```

The Standard is the normal deployable/runtime contract. The Guide remains the fuller human-facing
explanation.

## v17 → v18 migration

**Posture:** OnUpdate.

A legacy `Methodology: v17` line is interpreted as the v17 conformance checkpoint only for the
v17→v18 migration bridge when no modern Documentation Methodology dependency checkpoint exists.

Do not mass-rewrite unchanged v17 documents. Apply the transition on their next qualifying
modification/save, or before an operation that explicitly requires v18-only structure.

## Superseded by this pass

| Document | Superseded by | Disposition |
|---|---|---|
| `DocumentationMethodology_Index` v2 | v3 | Standard/Design output model registered |
| `DocumentationMethodology_Decisions` v15 | v16 | Standardisation and migration bridge recorded |

`DocumentationMethodology_Design_v14`, `DocumentationMethodology_Decisions_v15`, and `DocumentationMethodology_Index_v2` are superseded by this correction.

`DocumentationMethodology_Guide_v18` is **not** superseded by this pass.

---
Dependencies: !AIDE_DocumentationMethodology@v18, DocumentationMethodology_Design_v15
References: AIDE_DocumentationMethodology@v18, DocumentationMethodology_Guide_v18
