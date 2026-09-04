# Capabilities — Index

> **Version 8** (2026-08-28). Reconciled to the seven-component parent architecture. Registers
> the rewritten parent corpus and DocMeth review-input record, replaces the old subtopic tree,
> marks child Standards/Tools documents for revision, and resets priorities around the
> architecture checkpoint and component designs.
>
> Created: 2026-08-27 | Last modified: 2026-08-28

---

## §1 — Project identity

**Project:** Dev — Capabilities

**Topic:** Capabilities

**Owner:** Dave (Alpha Publishing Ltd)

**Purpose:** Define the reusable infrastructure by which AI-facing capabilities are designed,
made applicable, connected to dependencies, transitioned, built, packaged, deployed, and
reviewed across platforms.

**Methodology:** `DocumentationMethodology` v17

---

## §2 — Topic declarations

| Name | Parent topic | Filename prefix | Inheritance | Mode |
|---|---|---|---|---|
| Capabilities | None | `Capabilities` | independent | expanded |
| Standards | Capabilities | `Capabilities_Standards` | inherits | expanded |
| Tools | Capabilities | `Capabilities_Tools` | inherits | expanded |
| Scope | Capabilities | `Capabilities_Scope` | inherits | expanded |
| Dependencies | Capabilities | `Capabilities_Dependencies` | inherits | expanded |
| Migration | Capabilities | `Capabilities_Migration` | inherits | expanded |
| Deployment | Capabilities | `Capabilities_Deployment` | inherits | expanded |
| Review | Capabilities | `Capabilities_Review` | inherits | expanded |

The seven child topics are peer components. Standards and Tools produce capability packages;
the other five provide shared behaviour and contracts.

---

## §3 — Local configuration

### Custom document types

| Type | Role | Holds | Lifecycle | Distribution |
|---|---|---|---|---|
| `DocMethReviewItems` | Review input | Consequences and questions for the separate DocMeth review | Living until every item is dispositioned in that review | Internal |

Nearest established type: `Message`. The local type exists because this is a standing collected
input rather than a transmission issued into the DocMeth corpus during this pass.

### Other local configuration

None.

---

## §4 — Document register

| Document | Version | Type | Management | Status |
|---|---|---|---|---|
| `Capabilities_Index` | v8 | Index | established | Current |
| `Capabilities_Brief` | v2 | Brief | established | Current — rewritten parent architecture |
| `Capabilities_Design` | v2 | Design | established | Current — rewritten parent architecture |
| `Capabilities_Decisions` | v8 | Decisions | established | Current — history preserved and reconciled |
| `Capabilities_WorkRegister` | v6 | WorkRegister | established | Current |
| `Capabilities_OpenItems` | v8 | OpenItems | established | Current |
| `Capabilities_Overview` | v7 | Overview | established | Current — architecture review surface |
| `Capabilities_DocMethReviewItems` | v1 | DocMethReviewItems | custom | Current — separate review input, not applied to DocMeth |
| `Capabilities_Standards_Brief` | v1 | Brief | established | Current source; revision required against parent v2 (`WR18`) |
| `Capabilities_Standards_Design` | v3 | Design | established | Current source; materially stale boundaries (`WR18`) |
| `Capabilities_Tools_Brief` | v1 | Brief | established | Current source; revision required against parent v2 (`WR19`) |
| `Capabilities_Tools_Design` | v1 | Design | established | Current source; materially stale boundaries (`WR19`) |

### Superseded by this pass

| Document | Superseded by | Disposition |
|---|---|---|
| `Capabilities_Brief` v1 | v2 | Parent scope and component model rewritten |
| `Capabilities_Design` v1 | v2 | Publisher/four-layer/five-stage ownership replaced by current architecture |
| `Capabilities_Decisions` v7 | v8 | Earlier decisions retained inside v8 with revised/superseded status |
| `Capabilities_WorkRegister` v5 | v6 | Work reconciled to current component ownership |
| `Capabilities_OpenItems` v7 | v8 | Questions reconciled and current contract questions added |
| `Capabilities_Overview` v6 | v7 | Rebuilt as seven-component architecture review surface |
| `Capabilities_Index` v7 | v8 | Topic tree and register rebuilt |

### Rehomed or removed topic declarations

| Earlier declaration | Current disposition |
|---|---|
| Domains under Capabilities | Removed; domain carrier question moved to AIDE (`Q1`) |
| Deployment as the only shared child beside Standards/Tools | Retained as one of seven peer components |

No archived documents are introduced by this pass.

---

## §5 — Assets register

None.

---

## §6 — Current priority

1. **Architecture checkpoint:** review `Capabilities_Overview` v7 for the component set,
   ownership boundaries, flows, and open parent concerns.
2. **Scope, Dependencies, and Migration foundations:** `WR14`, `WR15`, `WR16`, including the
   Required Migration / On-Update separation and `/update-doc` contract.
3. **Reconcile Standards child corpus:** `WR18`, then produce the Standards Production and Usage
   standards through `WR4`.
4. **Reconcile Tools child corpus:** `WR19`, explicitly defining commands and resolving `WR6`.
5. **Define shared package boundary:** `WR20`, resolving `Q12` and `Q13` without creating more
   parent components.
6. **Design Deployment:** `WR13`, from completed package through platform publication.
7. **Design Review:** `WR17`, resolving the common review outcome and profile model (`Q14`).
8. **Run platform probes and trigger inventory:** `WR10`, `Q8`–`Q10`, recorded in relevant
   platform designs.
9. **DocMeth review later:** `WR21`, using `Capabilities_DocMethReviewItems` v1; do not redesign
   DocMeth inside current Capabilities work.

---

## §7 — Relationship to other topics

- **Workflow/AIDE:** consumers of Capabilities components; do not own the generic Standards
  Usage or Review models.
- **DocMeth:** owns shared document types and components; consumes Dependencies for dependency
  semantics after its separate review. Domains may define local document types.
- **Principles:** separate top-level topic under `D8`; not active Capabilities work.
- **Platform references/designs:** own platform facts and divergence; generic Capabilities
  documents remain platform-agnostic.

---

**Depends on:** `Capabilities_Brief` v2, `Capabilities_Design` v2,
`Capabilities_Decisions` v8.

**References:** `Capabilities_Overview` v7, `Capabilities_OpenItems` v8,
`Capabilities_WorkRegister` v6, `Capabilities_DocMethReviewItems` v1.

**Methodology:** v17
