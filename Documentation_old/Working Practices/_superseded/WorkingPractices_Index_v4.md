# Working Practices — Index

> **Version 4** (2026-08-31). Registers the consolidated Project Handoff, Documentation
> Methodology v20 ownership boundary, repository/Binder conventions and checkpoint-based output
> batching for the first distributable Working Practices capability.
>
> Created: 2026-08-31 | Last modified: 2026-08-31

## Project identity

**Topic:** Working Practices  
**Master folder / GPT Project:** `AIDE/Working Practices/`  
**Published capability identity:** `AIDE_WorkingPractices@v1`

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
| `WorkingPractices_Index` | v4 | Index | established | Current |
| `WorkingPractices_Brief` | v3 | Brief | established | Current |
| `WorkingPractices_Design` | v4 | Design | established | Current |
| `WorkingPractices_Decisions` | v4 | Decisions | established | Current |
| `AIDE_WorkingPractices_Standard` | v3 | Standard | established | Current canonical AI-facing outcome; identity `AIDE_WorkingPractices@v1` |


### Generated current consumption artefact

`WorkingPractices_Binder_v1.md` is the current generated/read-only project Binder. It is kept in
the active/master project folder for easy project-context selection, is not an authoritative
master, and is regenerated from the Current masters above.

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
verifying and handing over work.

## Relationship to Documentation Methodology

Documentation Methodology owns document lifecycle meaning and document-governance semantics.

Working Practices owns the practical file/repository handling convention used to realise those
states in the current AIDE workflow, without making a physical folder the definition of a lifecycle
state.

## Assets register

None.

---
Dependencies: !AIDE_DocumentationMethodology@v20
References: WorkingPractices_Design_v4, AIDE_WorkingPractices@v1, Principles_Design_v3
