# Principles — Index

> **Version 3** (2026-08-31). Reconciles the original Principles seed with current AIDE,
> registers the first canonical Standard and separates concrete Working Practices.
>
> Created: 2026-08-27 | Last modified: 2026-08-31

## Project identity

**Topic:** Principles  
**Master folder / GPT Project:** `AIDE/Principles/`  
**Published capability identity:** `AIDE_Principles@v1`

Principles is a top-level cross-cutting AIDE concern and can also be deployed independently.

## Topic declarations

| Name | Parent topic | Filename prefix | Inheritance | Mode |
|---|---|---|---|---|
| Principles | None | `Principles` | independent | expanded |

## Local configuration

None.

## Document register

| Document | Version | Type | Management | Status |
|---|---:|---|---|---|
| `Principles_Index` | v3 | Index | established | Current |
| `Principles_Brief` | v3 | Brief | established | Current |
| `Principles_Design` | v3 | Design | established | Current |
| `Principles_Decisions` | v3 | Decisions | established | Current |
| `AIDE_Principles_Standard` | v1 | Standard | established | Current canonical AI-facing outcome |

### Withdrawn, renamed or rehomed

None.

## Output model

```text
Principles_Design
        ↓
AIDE_Principles_Standard
```

The Standard is the normal deployable/runtime representation. The Design remains the internal
authority for future change.

## Relationship to Working Practices

Principles owns durable reasoning/problem-solving premises.

Working Practices owns concrete cross-surface collaboration and operating conventions. A Working
Practice may implement a Principle without moving that operational behaviour back into Principles.

## Assets register

None.

---
Dependencies: !AIDE_DocumentationMethodology@v19
References: Principles_Design_v3, AIDE_Principles@v1, WorkingPractices_Design_v2
