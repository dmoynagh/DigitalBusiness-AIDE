> identity: DocMeth_Working@v9 | doctype: working | updated: 2026-09-14

# Documentation Methodology — Working

## Session history

Session 2026-09-14. Clean-sheet rebuild of the Documentation Methodology standards. Dave guided concept and shape; three new standards authored, cross-reviewed twice, all defects resolved, published as v1.

## What was done

- **Clean-sheet rebuild** — built the main standard from Dave's concept, starting with purpose, principles, key functions, then defining each function iteratively
- **Three-standard structure** — split by load profile: main (always-on), schema definitions (always-on), schema authoring (on-demand)
- **Two cross-review rounds** — first round found 7 defects, all fixed; second round found 3 residual defects, all fixed; all 8 acceptance operations pass
- **Published** — three standards versioned as v1 with Declarations, replacing the existing v4 set
- **Decisions updated** — v7, twenty-nine decisions (thirteen carried, sixteen new/superseded)

## Current state

- **DocumentationMethodology_Standard_v1** — published, always-on, 246 lines
- **DocumentationMethodology_SchemaDefinitions_Standard_v1** — published, always-on, 91 lines
- **DocumentationMethodology_SchemaAuthoring_Standard_v1** — published, on-demand, 130 lines
- **DocMeth_Decisions_v7** — published
- **DocMeth_Design_v6** — superseded in substance by the v1 standards; the design was done output-first this session and decisions captured in v7. A new design document reflecting the current architecture is deferred unless needed

## Superseded documents

- DocumentationMethodology_Authoring_Standard_v4 → replaced by DocumentationMethodology_Standard_v1
- DocumentationMethodology_Schema_Standard_v4 → replaced by DocumentationMethodology_SchemaAuthoring_Standard_v1
- DocumentationMethodology_Definitions_Standard_v4 → replaced by DocumentationMethodology_SchemaDefinitions_Standard_v1
- DocMeth_Decisions_v6 → replaced by DocMeth_Decisions_v7

## Open items

- **Migration action** — other standards with `uses` referencing the old v4 identities need updating. Known affected: Standards_Authoring_Standard (uses DocMeth Schema v4), PD_Schema_Standard (uses DocMeth Schema v4), Core_Schema_Standard (uses DocMeth Schema v4), DocMeth_SchemaDefinitions (uses DocMeth SchemaAuthoring v1 — already current)
- **Binder rebuild** — the DocMeth binder needs rebuilding with the new standards replacing the old
- **Schema review** — survey all component schema definitions against the simplified definition contract
- **Design document** — v6 is superseded in substance. A v7 reflecting the current architecture can be authored if needed; the standards and decisions are the authoritative sources
- **Fourth standard** — DocumentationMethodology_Authoring_Standard planned for when authoring content grows enough to justify splitting from the main standard
- **Uses semantics update** — the dependency map in AIDE_Documentation_WIP needs updating for the new standard identities and the source-defined propagation model

---

Version note: v9 — clean-sheet rebuild session. Replaces v8. 2026-09-14.
