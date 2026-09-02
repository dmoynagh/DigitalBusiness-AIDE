# Capabilities — Index

> **Version 9** (2026-08-28). Reconciled to the canonical capability / Build WorkPackage /
> Deployment Set architecture and the new AIDE top-level structure.
>
> Created: 2026-08-27 | Last modified: 2026-08-28

---

## §1 — Project identity

**Project:** AIDE — Capabilities

**Topic:** Capabilities

**Purpose:** Define reusable infrastructure by which AI-facing capabilities are designed, built
into canonical outcomes, scoped, connected to dependencies, transitioned, realised for
platforms, packaged, deployed into named Deployment Sets, and reviewed.

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

### Other local configuration

None confirmed. Build Config and Deployment Config schemas are architecture work, not Index local
configuration at this stage.

---

## §4 — Document register

| Document | Version | Type | Management | Status |
|---|---|---|---|---|
| `Capabilities_Index` | v9 | Index | established | Current |
| `Capabilities_Brief` | v3 | Brief | established | Current |
| `Capabilities_Design` | v3 | Design | established | Current |
| `Capabilities_Decisions` | v9 | Decisions | established | Current |
| `Capabilities_WorkRegister` | v7 | WorkRegister | established | Current |
| `Capabilities_OpenItems` | v9 | OpenItems | established | Current |
| `Capabilities_Overview` | v8 | Overview | established | Current architecture review surface |
| `Capabilities_DocMethReviewItems` | v1 | DocMethReviewItems | custom | Current |
| `Capabilities_Standards_Brief` | v1 | Brief | established | Current source; revision required |
| `Capabilities_Standards_Design` | v3 | Design | established | Current source; materially stale boundaries |
| `Capabilities_Tools_Brief` | v1 | Brief | established | Current source; revision required |
| `Capabilities_Tools_Design` | v1 | Design | established | Current source; materially stale boundaries |

### Superseded by this pass

| Document | Superseded by | Disposition |
|---|---|---|
| `Capabilities_Brief` v2 | v3 | Production/handoff/deployment requirements revised |
| `Capabilities_Design` v2 | v3 | Platform realisation moved Build side; Deployment Set added |
| `Capabilities_Decisions` v8 | v9 | New confirmed decisions appended; prior history preserved |
| `Capabilities_WorkRegister` v6 | v7 | Work reset to current architecture |
| `Capabilities_OpenItems` v8 | v9 | Questions reframed around current boundaries |
| `Capabilities_Overview` v7 | v8 | Current flow and review surface rebuilt |
| `Capabilities_Index` v8 | v9 | Parent/location/status reconciled |

---

## §5 — Assets register

None.

---

## §6 — Current priority

1. **Deployment** — complete Deployment Set/config/composition/publication design.
2. **WorkPackage under AIDE Build** — establish generic handoff and Outcome contract.
3. **Scope** — revalidate boundary against Build Config and platform build.
4. **Dependencies** — confirm minimal dependency/conformance contract.
5. **Review** — finalise common method and profiles.
6. **Identity/version + package contracts** — resolve iteratively with the above.
7. **Migration child design** — formalise embedded declarations and Migration Build Standard.
8. **Platform evidence/build standards** — Claude, Codex, ChatGPT.
9. **Reconcile Standards and Tools child corpora.**
10. **DocMeth review later** using `Capabilities_DocMethReviewItems` v1.

---

## §7 — Relationships

- **AIDE/Core:** owns whole-system structure and Principles.
- **AIDE/Design:** owns design-side methodology; Documentation Methodology sits there.
- **AIDE/Build:** owns WorkPackage and generic build-side execution/return methodology.
- **AIDE/Environment:** owns environment structure.
- **Development domains:** CMS, JSON, and other product/application domains consume AIDE but are
  outside the AIDE system topic tree.
- **DocMeth:** separate review pending for dependency/migration consequences.

---

**Depends on:** `Capabilities_Brief` v3, `Capabilities_Design` v3,
`Capabilities_Decisions` v9.

**References:** `Core_System_Design` v2, `Capabilities_Overview` v8,
`Capabilities_OpenItems` v9, `Capabilities_WorkRegister` v7,
`Capabilities_DocMethReviewItems` v1.

**Methodology:** v17
