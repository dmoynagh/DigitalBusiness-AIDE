# Capabilities — Index

> **Version 10** (2026-08-28). Adds Tags, registers the completed Tags/Scope/Dependencies
> component designs and first Standards, and resets current priority to Review.
>
> Created: 2026-08-27 | Last modified: 2026-08-28

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
| `Capabilities_Index` | v10 | Index | established | Current |
| `Capabilities_Brief` | v4 | Brief | established | Current |
| `Capabilities_Design` | v4 | Design | established | Current |
| `Capabilities_Decisions` | v10 | Decisions | established | Current |
| `Capabilities_WorkRegister` | v8 | WorkRegister | established | Current |
| `Capabilities_OpenItems` | v10 | OpenItems | established | Current |
| `Capabilities_Overview` | v9 | Overview | established | Current architecture review surface |
| `Capabilities_DocMethReviewItems` | v2 | DocMethReviewItems | custom | Current |
| `Capabilities_Tags_Design` | v1 | Design | established | Current |
| `AIDE_Tags_Standard` | v1 | Standard | custom | Current generated Standard; identity `AIDE_Tags@v1` |
| `Capabilities_Scope_Design` | v1 | Design | established | Current |
| `AIDE_Scope_Standard` | v1 | Standard | custom | Current generated Standard; identity `AIDE_Scope@v1` |
| `Capabilities_Dependencies_Design` | v1 | Design | established | Current |
| `AIDE_Dependencies_Standard` | v1 | Standard | custom | Current generated Standard; identity `AIDE_Dependencies@v1` |
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

---

## §5 — Assets register

None.

---

## §6 — Current priority

1. **Review** — from purpose/value/outcomes/model into detailed mechanics.
2. **Migration** — child Design/Standard against the now-set Dependencies checkpoint model.
3. **Standards reconciliation.**
4. **Tools reconciliation.**
5. **Remaining identity/version + Package/Deployment Manifest contract details.**
6. **Deployment** — complete after the upstream contracts are stable.
7. **Platform evidence/build/deployment standards** as required/parallel.
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

**Depends on:** `Capabilities_Brief` v4, `Capabilities_Design` v4,
`Capabilities_Decisions` v10.

**References:** `Core_System_Design` v3, `Capabilities_Overview` v9,
`Capabilities_OpenItems` v10, `Capabilities_WorkRegister` v8,
`Capabilities_DocMethReviewItems` v2.

**Methodology:** v17
