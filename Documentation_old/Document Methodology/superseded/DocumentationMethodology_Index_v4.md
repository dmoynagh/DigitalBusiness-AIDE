# Documentation Methodology — Index

> **Version 4** (2026-08-31). Registers the v19 Decisions-model completeness correction and the
> corrected canonical Standard/Guide outcomes.
>
> Created: 2026-08-30 | Last modified: 2026-08-31

## Project identity

**Topic:** Documentation Methodology  
**Master folder / GPT Project:** `AIDE/Document Methodology/`  
**Published capability identity:** `AIDE_DocumentationMethodology@v19`

## Topic declaration

| Name | Parent concern | Filename prefix | Inheritance | Mode |
|---|---|---|---|---|
| Documentation Methodology | AIDE / Project-design methodology | `DocumentationMethodology` | independent | expanded |

## Document register

| Document | Version | Type | Status |
|---|---:|---|---|
| `DocumentationMethodology_Index` | v4 | Index | Current |
| `DocumentationMethodology_Design` | v16 | Design | Current confirmed internal model |
| `DocumentationMethodology_Decisions` | v17 | Decisions | Current |
| `AIDE_DocumentationMethodology_Standard` | v19 | Standard | Current canonical AI-facing outcome; identity `AIDE_DocumentationMethodology@v19` |
| `DocumentationMethodology_Guide` | v19 | Guide | Current human/explanatory companion |

## Output model

```text
DocumentationMethodology_Design
        ├── AIDE_DocumentationMethodology_Standard
        └── DocumentationMethodology_Guide
```

The Standard is the normal deployable/runtime contract. The Guide remains the fuller human-facing
explanation. Both derive from the confirmed Design and must agree in substance.

## Migration state

- **v18:** `OnUpdate` for the v17→v18 document-structure/conformance transition.
- **v19:** `None`; the Decisions-model correction changes the canonical operating contract but
  requires no structural/content migration of existing v18-conformant documents.

A legacy `Methodology: v17` line remains a v17 starting checkpoint only for the retained v18
migration bridge when no modern Documentation Methodology dependency checkpoint exists.

Do not mass-rewrite existing Decisions history or unchanged governed documents merely to make them
look v19. Apply the corrected Decisions behaviour prospectively.

## Superseded by this pass

| Document | Superseded by | Disposition |
|---|---|---|
| `DocumentationMethodology_Index` v3 | v4 | v19 release/current register |
| `DocumentationMethodology_Design` v15 | v16 | Decisions semantics made authoritative in Design |
| `DocumentationMethodology_Decisions` v16 | v17 | v19 correction decisions appended |
| `AIDE_DocumentationMethodology_Standard` v18 | v19 | canonical runtime contract corrected |
| `DocumentationMethodology_Guide` v18 | v19 | proportionality/downstream contradiction corrected |

Move the superseded issued masters to `superseded/` after the v19 files are installed as current.

---
Dependencies: !AIDE_DocumentationMethodology@v19, DocumentationMethodology_Design_v16
References: AIDE_DocumentationMethodology@v19, DocumentationMethodology_Guide_v19
