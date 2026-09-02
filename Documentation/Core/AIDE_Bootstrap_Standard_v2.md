# AIDE Bootstrap — Standard

> **Identity:** `AIDE_Bootstrap@v2`
> **Common name:** Bootstrap
> **Version 2** (2026-09-01). Makes effective Profile selection the startup-set gate, defines
> Profile `Why` as rationale, makes Contributions order-independent, and clarifies `{bootstrap}` as
> deliberately pre-Index while retaining thin/lazy subset-neutral Bootstrap.
>
> **Default weight:** Requirement

## Purpose

Keep AIDE's platform-level activation instruction small and stable while allowing each environment
to select a changeable startup subset through a Bootstrap Profile and thin component Bootstrap
Contributions.

## Stable bootstrap contract

Use the strongest persistent instruction mechanism the platform provides.

The persistent bootstrap shall:

1. resolve one effective Bootstrap Profile where available;
2. establish the Profile-selected startup set;
3. process applicable `{bootstrap}` Contributions only for owning material/capabilities brought
   into play by that startup set;
4. continue normally where no Profile exists without automatically processing unrelated deployed
   AIDE Contributions; and
5. load full detail lazily when current work requires it.

Do not embed a release-by-release list of AIDE components or reproduce detailed Standards/Tools in
the permanent platform instruction.

Do not claim stronger startup guarantees than the host platform provides.

## Bootstrap Profile

A Profile is an environment-specific startup map.

Each entry carries only:

```text
What
Why
Where
```

- **What** — identity/material to bring into the Profile startup set.
- **Why** — concise human/AI-readable, non-executable rationale for why the Profile includes it.
- **Where** — locator/discovery information for the authoritative deployed material.

`Why` is not executable conditional syntax and does not create a Bootstrap Scope/applicability
language. Conditional applicability inside substantive capability behaviour uses the normal owning
mechanisms.

`Where` identifies how material can be resolved; it does not grant permission to execute, acquire or
install arbitrary content.

A Profile may use normal Dependencies metadata to declare required presence. Bootstrap does not
create separate dependency syntax.

One effective Profile applies by default. If multiple competing Profiles are applicable and no
governing composition rule exists, surface the conflict rather than inventing precedence.

### No Profile

No Profile is valid.

No Profile means:

```text
no Profile-selected AIDE startup set
→ no automatic processing of deployed AIDE Bootstrap Contributions merely because they are present
```

Physical deployment/availability is not startup selection. When no Profile resolves, unrelated
deployed Contributions are not processed automatically.

## Bootstrap Contributions

`{bootstrap}` marks a thin owner-defined contribution that requires best-effort early-session
discovery when its owning material/capability belongs to the effective Profile startup set.

A Contribution shall be separate from the owner's full detailed material and remain short enough
to process without eagerly loading that material.

It identifies:

- owner/identity;
- early concern/check/action;
- relevance/rationale; and
- where detailed owner material can be resolved if needed.

The owner defines the Contribution's substantive semantics. Bootstrap defines only discovery,
eligibility and the order-independence contract.

Do not create a Contribution merely because a capability exists. Use one only for a demonstrated
early-session need.

### Eligibility

A Contribution is eligible for startup processing only when its owning material/capability is
selected into the effective Profile startup set, unless a future explicitly defined persistent
bootstrap primitive says otherwise.

### Order independence

Bootstrap Contributions are order-independent.

A Contribution must not:

- require another peer Contribution to have executed first;
- depend on another peer Contribution's side effects; or
- use platform file/discovery order as semantic sequencing.

Express required material presence through `AIDE_Dependencies`.

If a future demonstrated startup case requires ordered actions, design that requirement explicitly;
do not infer a startup ordering engine from current Contributions.

## `{bootstrap}` versus Item Type recognition

`{bootstrap}` is deliberately a primitive pre-capability/pre-Index discovery cue.

Bootstrap runs before richer AIDE Index/Item Type machinery can be assumed available, so its own
initial discovery must not depend on Item Type recognition or `ItemTypeRegistry`.

The Bootstrap cue and Item Type recognition mechanisms are intentionally separate.

## Context economy

Bootstrap establishes awareness and genuinely early checks; it is not a universal eager include.

Load full Standards, Tools, Guides, migration histories and other detailed material only when the
current work needs them, unless the Profile deliberately identifies that material as startup
guidance.

## Dependencies and missing requirements

Use `AIDE_Dependencies` for requirement/presence/version semantics.

If startup processing reveals required material is missing:

- surface the missing requirement;
- do not silently weaken or erase the requirement;
- do not silently install/update/remove material; and
- hand remediation to the environment/deployment process authorised to change the host.

A startup presence check does not itself trigger a blanket migration/current-version sweep.

## Deployment boundary

Bootstrap/Profile/Contribution artefacts may be deployed through AI Deployment.

Bootstrap does not own:

- Deployment Set semantics;
- installation/update/remove/reconciliation;
- deployment permission/authority;
- package acquisition; or
- deployment verification.

A future authorised deployment process may obtain a missing requirement from trusted configured
sources. This Standard does not define that acquisition mechanism.

## Startup tasks

No generic startup-task or Contribution-ordering engine exists in v2.

Use Profile selection, order-independent thin owner Contributions and startup-required dependency
checks. Add another mechanism only after a demonstrated startup need cannot be represented cleanly
through these contracts.

## Subset-neutral operation

The same persistent bootstrap may activate, for example:

```text
General Working
  → Principles + Working Practices

AIDE Development
  → broader AIDE operating set

No Profile
  → no Profile-selected AIDE startup set
```

Several AIDE subsets may be physically deployed at once without all becoming startup-active.

```yaml
MigrationSummary:
  CurrentVersion: v2
  LatestRequiredVersion: none
  LatestOnUpdateVersion: none

Transition:
  Version: v1
  Posture: None

Transition:
  Version: v2
  Posture: None
```

---
Dependencies: !AIDE_DocumentationMethodology@v22, AIDE_Dependencies
References: Core_Bootstrap_Design_v3, Core_System_Design_v8
