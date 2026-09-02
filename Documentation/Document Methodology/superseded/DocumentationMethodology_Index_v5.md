# Documentation Methodology — Index

> **Version 5** (2026-08-31). Registers the v20 lifecycle/storage ownership correction,
> preserves lifecycle semantics while delegating physical repository handling, and records the
> v20 Standard/Guide outcomes.
>
> Created: 2026-08-30 | Last modified: 2026-08-31

## Project identity

**Topic:** Documentation Methodology  
**Master folder / GPT Project:** `AIDE/Document Methodology/`  
**Published capability identity:** `AIDE_DocumentationMethodology@v20`

## Topic declaration

| Name | Parent concern | Filename prefix | Inheritance | Mode |
|---|---|---|---|---|
| Documentation Methodology | AIDE / Project-design methodology | `DocumentationMethodology` | independent | expanded |

## Document register

| Document | Version | Type | Status |
|---|---:|---|---|
| `DocumentationMethodology_Index` | v5 | Index | Current |
| `DocumentationMethodology_Design` | v17 | Design | Current confirmed internal model |
| `DocumentationMethodology_Decisions` | v18 | Decisions | Current |
| `AIDE_DocumentationMethodology_Standard` | v20 | Standard | Current canonical AI-facing outcome; identity `AIDE_DocumentationMethodology@v20` |
| `DocumentationMethodology_Guide` | v20 | Guide | Current human/explanatory companion |

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
- **v20:** `None`; the lifecycle/storage ownership correction changes which concern owns physical
  handling but requires no structural/content migration of existing v19-conformant documents.

A legacy `Methodology: v17` line remains a v17 starting checkpoint only for the retained v18
migration bridge when no modern Documentation Methodology dependency checkpoint exists.

Do not mass-rewrite existing governed documents merely to make them look v20. Existing use of a
particular physical storage layout may continue where the applicable Working Practices/environment
chooses it; v20 removes that layout from Documentation Methodology semantics rather than banning it.

## Superseded by this pass

| Document | Superseded by | Disposition |
|---|---|---|
| `DocumentationMethodology_Index` v4 | v5 | v20 release/current register |
| `DocumentationMethodology_Design` v16 | v17 | lifecycle/storage ownership boundary made authoritative in Design |
| `DocumentationMethodology_Decisions` v17 | v18 | v20 ownership decision appended |
| `AIDE_DocumentationMethodology_Standard` v19 | v20 | canonical runtime contract corrected |
| `DocumentationMethodology_Guide` v19 | v20 | physical workflow/storage rules delegated |

These previous issued masters are **Superseded**. Their physical movement, storage and later
repository cleanup follow the applicable Working Practices/environment; governed history remains
preserved under the Documentation Methodology lifecycle contract.

---
Dependencies: !AIDE_DocumentationMethodology@v20, DocumentationMethodology_Design_v17
References: AIDE_DocumentationMethodology@v20, DocumentationMethodology_Guide_v20
