# Capabilities — Index

> **Version 11** (2026-08-29). Registers the completed Review child corpus and Standards/Tool
> specification, advances the parent checkpoint documents, and moves current priority to
> Migration.
>
> Created: 2026-08-27 | Last modified: 2026-08-29

---

## §1 — Project identity

**Project:** AIDE — Capabilities

**Topic:** Capabilities

**Purpose:** Define reusable infrastructure by which AI-facing capabilities are designed, built
into canonical outcomes, tagged/classified, scoped, connected to dependencies, transitioned,
realised for platforms, packaged, deployed into named Deployment Sets, and independently reviewed.

**Parent system:** AIDE

**Master folder:** `AIDE/Capabilities/`

**Methodology:** `DocumentationMethodology` v17

---

## §2 — Topic declarations

| Name | Parent topic | Filename prefix | Inheritance | Mode |
|---|---|---|---|---|
| Capabilities | AIDE | `Capabilities` | independent | expanded |
| Standards | Capabilities | `Capabilities_Standards` | inherits | expanded |
| Tools | Capabilities | `Capabilities_Tools` | inherits | expanded |
| Tags | Capabilities | `Capabilities_Tags` | inherits | expanded |
| Scope | Capabilities | `Capabilities_Scope` | inherits | expanded |
| Dependencies | Capabilities | `Capabilities_Dependencies` | inherits | expanded |
| Migration | Capabilities | `Capabilities_Migration` | inherits | expanded |
| Deployment | Capabilities | `Capabilities_Deployment` | inherits | expanded |
| Review | Capabilities | `Capabilities_Review` | inherits | expanded |
| Review Tool | Review | `Capabilities_Review_Tool` | inherits | expanded |

WorkPackage is not a Capabilities child. It belongs under `AIDE/Build/WorkPackage`.

---

## §3 — Local configuration

### Custom document types

| Type | Role | Holds | Lifecycle | Distribution |
|---|---|---|---|---|
| `DocMethReviewItems` | Review input | Consequences/questions for separate DocMeth review | Living until dispositioned | Internal |
| `Standard` | Outcome | Published AI-facing capability rules derived from a Capability Design | Living/versioned by capability release | Consuming AI environments |

`Standard` is a Capabilities-local managed type for the current generated outputs. Cross-domain
recurrence may later support promotion during the separate Documentation Methodology review.

### Other local configuration

None confirmed. Build Config and Deployment Config schemas are architecture work, not Index local
configuration at this stage.

---

## §4 — Document register

| Document | Version | Type | Management | Status |
|---|---|---|---|---|
| `Capabilities_Index` | v11 | Index | established | Current |
| `Capabilities_Brief` | v4 | Brief | established | Current |
| `Capabilities_Design` | v5 | Design | established | Current |
| `Capabilities_Decisions` | v11 | Decisions | established | Current |
| `Capabilities_WorkRegister` | v9 | WorkRegister | established | Current |
| `Capabilities_OpenItems` | v11 | OpenItems | established | Current |
| `Capabilities_Overview` | v10 | Overview | established | Current architecture review surface |
| `Capabilities_DocMethReviewItems` | v2 | DocMethReviewItems | custom | Current |
| `Capabilities_Tags_Design` | v1 | Design | established | Current |
| `AIDE_Tags_Standard` | v1 | Standard | custom | Current generated Standard; identity `AIDE_Tags@v1` |
| `Capabilities_Scope_Design` | v1 | Design | established | Current |
| `AIDE_Scope_Standard` | v1 | Standard | custom | Current generated Standard; identity `AIDE_Scope@v1` |
| `Capabilities_Dependencies_Design` | v1 | Design | established | Current |
| `AIDE_Dependencies_Standard` | v1 | Standard | custom | Current generated Standard; identity `AIDE_Dependencies@v1` |
| `Capabilities_Review_Design` | v1 | Design | established | Current |
| `Capabilities_Review_Decisions` | v1 | Decisions | established | Current |
| `AIDE_Review_Standard` | v1 | Standard | custom | Current generated Standard; identity `AIDE_Review@v1` |
| `AIDE_ReviewProfiles_Standard` | v1 | Standard | custom | Current generated Standard; identity `AIDE_ReviewProfiles@v1` |
| `Capabilities_Review_Tool_Design` | v1 | Design | established | Current Review Tool specification; canonical Tool outcome not yet built |
| `Capabilities_Standards_Brief` | v1 | Brief | established | Current source; revision required |
| `Capabilities_Standards_Design` | v3 | Design | established | Current source; materially stale boundaries |
| `Capabilities_Tools_Brief` | v1 | Brief | established | Current source; revision required |
| `Capabilities_Tools_Design` | v1 | Design | established | Current source; materially stale boundaries |

### Superseded by this pass

| Document | Superseded by | Disposition |
|---|---|---|
| `Core_System_Design` v2 | v3 | Identity/metadata/bootstrap system layer added |
| `Core_System_Decisions` v1 | v2 | System-level decisions appended |
| `Capabilities_Brief` v3 | v4 | Eight-component and Tags/Scope/Dependencies requirements added |
| `Capabilities_Design` v3 | v4 | Tags/Scope/Dependencies and Package+Manifest boundary finalised |
| `Capabilities_Decisions` v9 | v10 | New confirmed decisions appended; history retained |
| `Capabilities_WorkRegister` v7 | v8 | Sequence reset; Review current, Deployment deferred |
| `Capabilities_OpenItems` v9 | v10 | Tags/Scope/Dependencies questions closed |
| `Capabilities_Overview` v8 | v9 | Current model rebuilt |
| `Capabilities_Index` v9 | v10 | Tags/new child docs registered |
| `Capabilities_DocMethReviewItems` v1 | v2 | Metadata-container/Tags/Identity review inputs added |
| `Capabilities_Design` v4 | v5 | Review component contract finalised and detailed child corpus referenced |
| `Capabilities_Decisions` v10 | v11 | Review checkpoint decision appended; detailed reasoning delegated to Review Decisions |
| `Capabilities_WorkRegister` v8 | v9 | Review completed; Migration current; external seams handed off |
| `Capabilities_OpenItems` v10 | v11 | Review question closed; environment/communication seams recorded |
| `Capabilities_Overview` v9 | v10 | Review model and new current sequence reflected |
| `Capabilities_Index` v10 | v11 | Review child corpus registered and current parent versions advanced |

---

## §5 — Assets register

None.

---

## §6 — Current priority

1. **Migration** — child Design/Standard against the now-set Dependencies checkpoint model.
2. **Standards reconciliation.**
3. **Tools reconciliation.**
4. **Remaining identity/version + Package/Deployment Manifest contract details.**
5. **Deployment** — complete after the upstream contracts are stable.
6. **Platform evidence/build/deployment standards** as required/parallel.
7. **Review environment/communication ownership handoff** with the owning workstreams.
8. **DocMeth review later** using `Capabilities_DocMethReviewItems` v2.

WorkPackage remains a separate AIDE Build workstream.

---

## §7 — Relationships

- **AIDE/Core:** owns whole-system structure, formal identity convention, and system bootstrap
  primitive.
- **AIDE/Design:** owns design-side methodology; Documentation Methodology sits there and will be
  reviewed later for generic metadata-container integration.
- **AIDE/Build:** owns WorkPackage and generic build-side execution/return methodology.
- **AIDE/Environment:** owns environment structure.
- **Development domains:** CMS, JSON, and other product/application domains consume AIDE but are
  outside the AIDE system topic tree.

---

**Depends on:** `Capabilities_Brief` v4, `Capabilities_Design` v5,
`Capabilities_Decisions` v11.

**References:** `Core_System_Design` v3, `Capabilities_Overview` v10,
`Capabilities_OpenItems` v11, `Capabilities_WorkRegister` v9,
`Capabilities_DocMethReviewItems` v2, `Capabilities_Review_Design` v1,
`Capabilities_Review_Decisions` v1, `AIDE_Review@v1`,
`AIDE_ReviewProfiles@v1`, `Capabilities_Review_Tool_Design` v1.

**Methodology:** v17
