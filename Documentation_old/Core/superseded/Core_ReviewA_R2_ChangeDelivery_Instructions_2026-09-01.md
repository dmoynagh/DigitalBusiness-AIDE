# Core — Review A Round 2 — Change Delivery Instructions

> **Change Delivery Package issued 2026-09-01.**
>
> This document is a **transfer/application artefact**, not an enduring AIDE master.
>
> Package creation does **not** mean the changes described here have been applied.

## Purpose

Apply the final narrow Core corrections arising from:

`AIDE-Architecture-Review-A-Core-Substrate` — Round R2

The R1 architecture remediation has passed the required High-level re-review. Round R2 found two
remaining determinism defects requiring local correction and one historical-Decisions observation
that the Lead declined.

This package authorises only those final Review A corrections.

Do not broaden into Review B, wider Core cleanup, Capabilities redesign, Build/Deployment work, or
unrelated version/dependency refresh.

## Owning project and authoritative baseline

**Owning top-level topic:** `AIDE/Core`

Apply this package in the **Core owning project** against its current authoritative masters.

Baseline expected at handoff:

- `Core_Binder_v2.md`
- current individual Core masters represented by that Binder

Supporting seam authority:

- `DocumentationMethodology_Binder_v4.md`

The destination's current masters remain authoritative. If they have advanced beyond the expected
baseline, reconcile this package against that newer current state rather than overwriting it.

Never edit a generated Binder directly.

## Package contents

This package contains only:

- `Core_ReviewA_R2_ChangeDelivery_Instructions_2026-09-01.md`

No replacement Core master files are prebuilt in this package.

That is intentional: the changes must be reconciled and issued by the Core owning project from its
current authoritative masters.

## Review disposition summary

| Finding | Lead disposition | Required action |
|---|---|---|
| `RA-R2-F1` — Stop boundary membership ambiguous | **Change** | Make Propagation Stop inclusive of the marked boundary itself and all content within/below it. |
| `RA-R2-F2` — implicit Domain settings host undefined | **Change** | Define deterministic unique-host eligibility; fail visibly on competing/no-unique host where settings are required. |
| `RA-R2-F3` — D6 historical Index example | **Decline** | Do not rewrite D6; D34 already explicitly refines D6 where historical wording used Index as Domain-establishing. |

No Review A Round 3 is planned if the resulting Core Binder implements these dispositions exactly.

---

# Application manifest

Expected smallest coherent replacement set:

| Current master | Action | Replacement / result | Destination |
|---|---|---|---|
| `Core_Index_v5.md` | Replace Current | `Core_Index_v6.md` | `AIDE/Core/` |
| `Core_System_Design_v8.md` | Replace Current | `Core_System_Design_v9.md` | `AIDE/Core/` |
| `Core_Domain_Design_v3.md` | Replace Current | `Core_Domain_Design_v4.md` | `AIDE/Core/` |
| `Core_Domain_Decisions_v3.md` | Replace Current | `Core_Domain_Decisions_v4.md` | `AIDE/Core/` |
| `AIDE_Domain_Standard_v3.md` | Replace Current | `AIDE_Domain_Standard_v4.md` / `AIDE_Domain@v4` | `AIDE/Core/` |
| `Core_Binder_v2.md` | Regenerate/replace generated artefact | `Core_Binder_v3.md` | `AIDE/Core/` |

Use the current semantic lifecycle rules first, then apply the repository physical convention:

- replaced current masters → **Superseded**;
- physically move superseded files to `_superseded/` where that folder convention is in use;
- keep the newly issued current masters in the active Core master-folder root;
- keep the regenerated current Binder in the active Core master-folder root;
- move the replaced Binder to `_superseded/`.

If the owning Core project determines a smaller mechanically valid document-version set under the
current methodology, preserve that discipline, but the semantic result below is mandatory and
already-issued files must not be edited in place.

---

# Change 1 — RA-R2-F1 — Propagation Stop includes the marked boundary

## Lead decision

Choose the **inclusive** interpretation.

`Propagation: Stop` takes effect at the marked recognised/registered structural boundary itself.

The current enclosing effective Domain ceases to apply to:

1. the marked boundary; and
2. all structurally contained content within/below that boundary.

The marked boundary and its contents then resolve independently as one stopped region.

Where a parent Index hosts the Domain-owned Stop property on the registration for the boundary:

- the parent Index is the property host only;
- the registered boundary is the stopped boundary; and
- the parent Index does not become part of the stopped region merely by hosting the property.

Independent resolution may yield:

- another Domain;
- `No Domain context`; or
- a visible unresolved/error result.

No parent/child Domain relationship, inheritance, merge, settings propagation or precedence is
created between the enclosing Domain and any independently resolved Domain.

## Reason

The exclusive reading leaves a Domain-capable boundary inside the enclosing Domain while requiring
its contents to resolve independently from that Domain. For a boundary such as a
`DocumentationTopic`, that makes ordinary containment/resolution indeterminate.

The inclusive reading makes Stop a coherent contextual reset: boundary and subtree leave the
enclosing Domain together.

## Apply to `Core_Domain_Design_v4`

Carry forward v3 and reconcile at minimum:

- canonical Propagation Stop meaning;
- Stop traversal wording;
- Domain resolution procedure;
- examples/summaries currently using only `below` where that could exclude the marked boundary.

Use wording equivalent to:

> `Propagation: Stop` removes the enclosing effective Domain from the marked boundary itself and
> all content within/below it. The marked boundary and its contained region then resolve
> independently.

Do not add another marker, child-Domain model, precedence rule, inheritance mechanism, or generic
filesystem Stop mechanism.

## Apply to `Core_Domain_Decisions_v4`

Preserve prior Decisions unchanged as history.

Add a new decision, e.g.:

`D40 — Propagation Stop includes the marked boundary`

Record proportionately:

- the ambiguity exposed by R2;
- the inclusive choice;
- why the exclusive reading is operationally indeterminate; and
- that this refines D36/D37 without introducing parent/child Domain semantics.

Do not rewrite D36/D37 solely to make historical text look current.

## Apply to `AIDE_Domain_Standard_v4`

Carry the inclusive rule into the canonical AI-facing runtime contract.

Align both:

- Stop/traversal semantics; and
- the Domain resolution procedure.

Do not leave mixed `below` versus `within-and-below` wording that recreates the ambiguity.

---

# Change 2 — RA-R2-F2 — deterministic implicit-Domain settings host

## Lead decision

Close the undefined host through **unique-host eligibility**, not precedence.

For an implicit Domain:

1. An Index is eligible to host Domain-owned configuration only when it is the governing Index of
   an approved semantic recognised root that establishes/participates in that implicit Domain.
2. Mere parent/repository registration of a recognised root does **not** make that parent Index a
   Domain settings host.
3. The eligible governing Index must yield **one unambiguous authoritative host** for that implicit
   Domain.
4. If no unique eligible Index host exists and Domain metadata/settings are needed, use an explicit
   `AIDE_Domain.yaml` representation.
5. A native Solution/Project-only implicit Domain therefore does not acquire an arbitrary Index
   host merely because some Index registers it; use an explicit Domain representation when AIDE
   Domain metadata/settings are required.
6. If multiple eligible Indexes expose or claim Domain-owned configuration for the same implicit
   Domain, fail visibly and reconcile/introduce an explicit Domain rather than merge, rank, or use
   discovery order.

Under the current approved recognition set, the ordinary implicit documentation case is the
governing Index of the `DocumentationTopic`.

A co-root Domain such as one Solution plus one `DocumentationTopic` can therefore have one clear
Index host.

Multiple competing semantic-root Indexes do not gain an implicit precedence rule.

## Reason

The current phrase `applicable authoritative host` does not determine which host wins when several
Indexes could claim the same implicit Domain.

Allowing discovery order to decide would create silent settings variability—the same failure shape
the explicit-Domain host rule already rejects.

The fix establishes uniqueness rather than inventing a settings-precedence engine.

## Apply to `Core_Domain_Design_v4`

Replace the incomplete implicit-host rule with the deterministic eligibility/uniqueness rule above.

Clarify that:

- explicit Domain host semantics remain unchanged;
- generic Index registration alone never grants Domain settings-host authority;
- explicit Domain representation is the escape hatch where an implicit Domain has no unique host.

Extend failure/ambiguity handling to competing/duplicate implicit-Domain host state.

## Apply to `Core_Domain_Decisions_v4`

Add a new decision, e.g.:

`D41 — Implicit Domain settings require one unambiguous authoritative host`

Record:

- the undefined-host defect;
- unique eligible host rather than precedence;
- parent/repository registration does not confer host authority;
- native-only/no-unique-host cases use explicit Domain representation when settings are needed; and
- competing implicit host state fails visibly.

## Apply to `AIDE_Domain_Standard_v4`

Carry the same deterministic rule into the canonical Standard:

- authoritative settings-host semantics;
- failure/ambiguity behaviour.

Do not introduce a generic settings precedence, inheritance, or merge engine.

---

# RA-R2-F3 — no Core correction

Do **not** rewrite historical Decision D6.

The Reviewer reported the D6 Index-established-Domain example as unrefined, but current
`Core_Domain_Decisions_v3` D34 already explicitly states that it refines:

`D5, D6, D8, D9, D10, D15, D19 and D22`

where historical wording/examples used Index as a literal or potentially Domain-establishing
boundary.

D34 supplies the current rule that generic `Index` is outside the approved Domain recognition set.

Therefore:

- D6 remains historical decision text;
- D34 remains its explicit current refinement; and
- rewriting D6 would flatten useful decision evolution.

No new correction is authorised for RA-R2-F3.

---

# Core system-level reconciliation

## `Core_System_Design_v9`

Reissue because the current system Design:

- summarises Stop with wording that can imply only content `below` the boundary; and
- points to `AIDE_Domain@v3`.

Change only what is required to reflect:

- Stop includes the marked boundary and all content within/below it;
- that region then resolves independently;
- implicit settings-host authority is uniquely eligible/deterministic; and
- canonical Domain outcome is `AIDE_Domain@v4`.

Do not broaden the system Design.

## `Core_System_Decisions_v7`

**Intentionally unchanged.**

No new system-level Decision is required. The new reasoning belongs in Domain Decisions and does not
change a cross-foundation ownership boundary.

---

# Intentionally unchanged Core items

Do **not** reissue solely for this package:

- `Core_Index_Design_v2.md`
- `Core_Index_Decisions_v2.md`
- `AIDE_Index_Standard_v2.md`
- `Core_Bootstrap_Design_v3.md`
- `Core_Bootstrap_Decisions_v3.md`
- `AIDE_Bootstrap_Standard_v2.md`
- `Core_System_Decisions_v7.md`

These passed R2 and are not semantically changed by RA-R2-F1/F2.

The new `Core_Index_v6.md` is expected only to register the newly current Core/Domain document
versions and current canonical Domain identity.

---

# Version / migration posture

Canonical Domain identity becomes:

`AIDE_Domain@v4`

Add/retain transition history with:

```yaml
Transition:
  Version: v4
  Posture: None
```

Reason:

v4 removes determinism ambiguity from the current contract but does not require persisted consumer
state transformation.

Update:

```yaml
MigrationSummary:
  CurrentVersion: v4
```

New/reissued Core documents should record the truthful current Documentation Methodology
conformance checkpoint available/proven at issue time, expected here to be
`AIDE_DocumentationMethodology@v23`.

Do not mechanically advance unchanged Core files merely because v23 exists.

---

# Validation before issue

Before regenerating the Binder, verify all of the following:

1. Every **current** Propagation Stop statement includes the marked boundary itself, not only its
   descendants.
2. A parent Index hosting a Stop property is not mistaken for the stopped boundary.
3. Stop still creates no parent/child Domain semantics, inheritance, merge, settings propagation or
   precedence.
4. Implicit Domain settings have one deterministic eligible authoritative host.
5. Generic parent/repository Index registration alone cannot create settings-host authority.
6. Native Solution/Project-only implicit Domains use explicit Domain representation when AIDE
   Domain settings are needed.
7. Competing/duplicate implicit host state fails visibly; no discovery-order, merge or precedence
   rule exists.
8. D6 remains historical and D34 remains the explicit refinement preventing generic Index from
   being Domain-defining.
9. `AIDE_Domain@v4` retains the R1 load-bearing authority constraint:
   external Item Type owners cannot self-elevate into Domain roots/containers.
10. `Core_System_Design_v9` points to `AIDE_Domain@v4` and uses inclusive Stop semantics.
11. `Core_Index_v6` registers the correct current master versions while unchanged child contracts
    retain their existing versions.
12. `Core_Binder_v3.md` contains only the current master set.

---

# Binder / project-context actions

After issuing the replacement masters:

1. Regenerate `Core_Binder_v3.md` from the **current individual Core masters**.
2. Do not edit the Binder directly.
3. Replace `Core_Binder_v2.md` with Binder v3 in the Core project context.
4. Remove/supersede stale Binder v2 context so the project does not simultaneously consume two
   current Core snapshots.
5. Keep the individual current masters as the authoritative corpus; the Binder remains a generated
   consumption artefact.

Do not add this Change Delivery instruction file to the enduring Core authoritative corpus after
application. It is transfer/application material only.

---

# Cross-project / downstream consequences

After application:

- return `Core_Binder_v3.md` to the Capabilities Review coordination context;
- no Documentation Methodology reissue is required by this package;
- no Review A Round 3 is expected;
- Capabilities will perform a Lead verification of the two corrected passages and, if clean, mark
  Review A Complete at High.

Do **not** rebuild the temporary common `AIDE_Bundle_StandardsTools` as part of this Core correction.
Runtime/build/deployment propagation remains later work after Review A closure.

---

# Package lifecycle

This ZIP is an active Change Delivery Package.

Repository convention:

1. stage it in:
   `Documentation/_changeDeliveryPackages/`
2. apply/reconcile it in the Core owning project;
3. once application/review is complete, move the ZIP to:
   `Documentation/_changeDeliveryPackages/_completed/`

The package itself is not an authoritative Core master.

## State at issue

```text
Package produced: yes
Core changes applied: no
Replacement masters produced: no
Core_Binder_v3 produced: no
Review A completed: no
```

Those states must be advanced only by the owning/application processes that actually establish them.
