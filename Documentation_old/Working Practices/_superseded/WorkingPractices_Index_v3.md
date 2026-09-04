# Working Practices — Index

> **Version 3** (2026-08-31). Adopts the confirmed Documentation Methodology/Working Practices
> ownership boundary, management-folder conventions, independently versioned Binders, and the
> formal Project Handoff practice.
>
> Created: 2026-08-31 | Last modified: 2026-08-31

## Project identity

**Topic:** Working Practices  
**Master folder / GPT Project:** `AIDE/Working Practices/`  
**Published capability identity:** `AIDE_WorkingPractices@v2`

Working Practices is a top-level cross-cutting AIDE concern and can also be deployed independently.

## Topic declarations

| Name | Parent topic | Filename prefix | Inheritance | Mode |
|---|---|---|---|---|
| Working Practices | None | `WorkingPractices` | independent | expanded |

## Local configuration

None.

## Document register

| Document | Version | Type | Management | Status |
|---|---:|---|---|---|
| `WorkingPractices_Index` | v3 | Index | established | Current |
| `WorkingPractices_Brief` | v3 | Brief | established | Current |
| `WorkingPractices_Design` | v3 | Design | established | Current |
| `WorkingPractices_Decisions` | v3 | Decisions | established | Current |
| `AIDE_WorkingPractices_Standard` | v2 | Standard | established | Current canonical AI-facing outcome |

### Generated current consumption artefact

`WorkingPractices_Binder_v1.md` is the current generated/read-only project Binder. It is not an
authoritative master and is regenerated from the Current masters above.

### Withdrawn, renamed or rehomed

None.

## Output model

```text
WorkingPractices_Design
        ↓
AIDE_WorkingPractices_Standard
```

## Relationship to Principles

Principles owns durable reasoning/problem-solving premises.

Working Practices owns concrete cross-surface conventions for carrying out, communicating,
verifying, organising and handing over work.

## Relationship to Documentation Methodology

Documentation Methodology owns document lifecycle meaning and document-governance semantics.

Working Practices owns the practical file/repository handling convention used to realise those
states in the current AIDE workflow, without making a physical folder the definition of a lifecycle
state.

## Assets register

None.

---
Dependencies: !AIDE_DocumentationMethodology@v20
References: WorkingPractices_Design_v3, AIDE_WorkingPractices@v2, Principles_Design_v3
