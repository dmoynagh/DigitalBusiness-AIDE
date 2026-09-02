# AIDE Bootstrap — Standard

> **Identity:** `AIDE_Bootstrap@v1`
> **Common name:** Bootstrap
> **Version 1** (2026-08-31). First canonical Bootstrap contract produced from
> `Core_Bootstrap_Design_v2`.
>
> **Default weight:** Requirement

## Purpose

Keep AIDE's platform-level activation instruction small and stable while allowing each environment
to select a changeable startup posture through a Bootstrap Profile and thin component Bootstrap
Contributions.

## Stable bootstrap contract

Use the strongest persistent instruction mechanism the platform provides.

The persistent bootstrap shall:

1. discover an applicable Bootstrap Profile where available;
2. establish/process the Profile before substantive work where reasonably possible;
3. process applicable available `{bootstrap}` Contributions;
4. continue normally where no Profile exists; and
5. avoid repeatedly reprocessing unchanged bootstrap state during the same session.

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

- **What** — identity/name of guidance, capability or material to bring into play.
- **Why** — concise reason or relevance condition.
- **Where** — locator/discovery information for the authoritative deployed material.

`Where` identifies how material can be resolved; it does not grant permission to execute/install
arbitrary content.

A Profile may use normal Dependencies metadata to declare required presence. Bootstrap does not
create separate dependency syntax.

One effective Profile applies by default. If multiple competing Profiles are applicable and no
governing composition rule exists, surface the conflict rather than inventing precedence.

No Profile is valid; continue without AIDE bootstrap activation.

## Bootstrap Contributions

`{bootstrap}` marks a thin owner-defined contribution that requires best-effort early-session
discovery.

A Contribution shall be separate from the owner's full detailed material and remain short enough
to process without eagerly loading that material.

It identifies:

- owner/identity;
- early concern/check/action;
- relevance/reason; and
- where detailed owner material can be resolved if needed.

The owner defines the contribution's substantive semantics. Bootstrap defines only
discovery/ordering.

Do not create a Contribution merely because a capability exists. Use one only for a demonstrated
early-session need.

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
- hand remediation to the environment/deployment process that is authorised to change the host.

A startup presence check does not itself trigger a blanket migration/current-version sweep.

## Deployment boundary

Bootstrap/Profile/Contribution artefacts may be deployed through AI Deployment.

Bootstrap does not own:

- deployment-set semantics;
- installation/update/remove/reconciliation;
- deployment permission/authority;
- package acquisition; or
- deployment verification.

A future authorised deployment process may obtain a missing requirement from trusted configured
sources. This Standard does not define that acquisition mechanism.

## Startup tasks

No generic startup-task engine exists in v1.

Use Profile activation, thin owner Contributions and startup-required dependency checks. Add a
generic task mechanism only after a demonstrated early-session need cannot be represented by these
mechanisms cleanly.

## Subset-neutral operation

The same persistent bootstrap may activate, for example:

```text
General Working
  → Principles + Working Practices

AIDE Development
  → broader AIDE operating set
```

or operate with no Profile.

```yaml
MigrationSummary:
  CurrentVersion: v1
  LatestRequiredVersion: none
  LatestOnUpdateVersion: none

Transition:
  Version: v1
  Posture: None
```

---
Dependencies: !AIDE_DocumentationMethodology@v19, AIDE_Dependencies
References: Core_Bootstrap_Design_v2, Core_System_Design_v6
