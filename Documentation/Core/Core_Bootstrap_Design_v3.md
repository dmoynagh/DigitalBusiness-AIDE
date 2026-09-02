# Core Bootstrap — Design

> **Version 3** (2026-09-01). Retains the thin Bootstrap/Profile/Contribution architecture while
> making effective Profile selection the startup-subset gate, defining Profile `Why` as rationale,
> making Contributions order-independent, and clarifying `{bootstrap}` as deliberately pre-Index
> discovery.
>
> Created: 2026-08-31 | Last modified: 2026-09-01

## §1 — Purpose and ownership

Bootstrap is the stable Core-owned activation seam between persistent platform-level instructions
and deployable AIDE guidance, Standards, Tools and other material.

It exists to let one small, rarely changing platform bootstrap support different AIDE subsets
without copying the current operating set into permanent platform instructions.

Core/Bootstrap owns:

- the stable persistent bootstrap contract;
- effective Bootstrap Profile resolution;
- Profile startup-set selection;
- Bootstrap Contribution discovery/eligibility;
- the order-independence contract for Contributions;
- the primitive `{bootstrap}` discovery cue; and
- the boundary between early awareness/checks and lazy full material.

Bootstrap does not own capability semantics, Scope, dependency semantics, deployment, package
acquisition, platform permission/authority or a generic startup-task engine.

## §2 — Stable layered model

The stable flow is:

```text
persistent platform bootstrap
        ↓
resolve one effective Bootstrap Profile, if any
        ↓
establish the Profile startup set
        ↓
process applicable Bootstrap Contributions belonging to that startup set
        ↓
load full detail lazily when current work requires it
```

The persistent instruction is deliberately tiny and changes rarely. It uses the strongest
persistent mechanism the platform supplies but must not claim stronger startup guarantees than the
platform actually provides.

## §3 — Bootstrap Profile

A Profile is an environment-specific startup map.

Each entry carries only:

```text
What
Why
Where
```

- **What** — identity/material to bring into the Profile startup set.
- **Why** — concise human/AI-readable rationale for why the Profile includes it.
- **Where** — locator/discovery information for the authoritative deployed material.

`Why` is **not executable conditional syntax** and does not create a Bootstrap applicability
language. Conditional applicability inside substantive capability behaviour uses the normal owner
and applicability mechanisms.

`Where` is a locator/discovery aid. It does not authorise installation, execution or acquisition of
arbitrary content.

A Profile may use the normal Dependencies mechanism for required-presence facts. Bootstrap does not
invent separate dependency syntax.

## §4 — Effective Profile and startup subset

At most one effective Bootstrap Profile applies by default.

If multiple competing Profiles are applicable and no governing composition rule exists, fail
visibly rather than inventing merge/precedence.

**No Profile is valid.** Its operational meaning is now explicit:

> No Profile means there is no Profile-selected AIDE startup set and therefore no automatic
> processing of deployed AIDE Bootstrap Contributions merely because those Contributions are
> physically available.

Physical deployment/availability is not startup selection.

This gate is what makes the stable bootstrap subset-neutral on a host where several AIDE subsets
may be deployed simultaneously.

## §5 — Bootstrap Contributions

`{bootstrap}` marks a thin owner-defined contribution that needs best-effort early-session discovery
when its owning material/capability belongs to the effective Profile startup set.

A Contribution is separate from the owner's full detailed material and remains small enough to
process without eagerly loading that full material.

It identifies:

- owner/identity;
- early concern/check/action;
- relevance/rationale; and
- where detailed owner material can be resolved when needed.

The owner defines the Contribution's substantive semantics. Bootstrap defines discovery,
eligibility and the order-independence contract.

Do not create a Contribution merely because a capability exists. Use one only for a demonstrated
early-session need.

### Eligibility

A Contribution is eligible for automatic startup processing only when its owning material/capability
is brought into play by the effective Profile, unless a future explicitly defined persistent
bootstrap primitive says otherwise.

The mere presence of a deployed `{bootstrap}` block does not make it part of the startup set.

## §6 — Contributions are order-independent

Bootstrap Contributions are peer, order-independent early contributions.

A Contribution must not:

- require another peer Contribution to execute first;
- depend on a peer Contribution's startup side effects; or
- rely on platform file/discovery order as semantic sequencing.

Required material presence is expressed through the normal Dependencies mechanism.

If a future demonstrated startup case genuinely requires ordered actions, design that requirement
explicitly. Do not infer an ordering engine from current Contribution discovery.

## §7 — `{bootstrap}` is deliberately pre-Index

`{bootstrap}` is a primitive pre-capability/pre-Index discovery cue.

Bootstrap runs before richer AIDE Index/Item Type machinery can be assumed available. Its own
initial discovery must therefore not depend on Item Type recognition or on loading the generic
`ItemTypeRegistry`.

The two recognition mechanisms are intentionally separate:

```text
{bootstrap}
  → minimal early discovery cue

AIDE_Index / Item Types
  → richer semantic recognition after that machinery is available
```

This separation is architectural, not temporary duplication.

## §8 — Dependencies and missing requirements

Use `AIDE_Dependencies` for requirement/presence/version semantics.

If startup processing reveals required material is missing:

- surface the missing requirement;
- do not silently weaken or erase it;
- do not silently install/update/remove material; and
- hand remediation to the environment/deployment process authorised to change the host.

A startup presence check does not itself trigger a blanket Migration/current-version sweep.

A Deployment Set omission does not erase a semantic required-presence fact.

## §9 — Deployment and acquisition boundary

Bootstrap/Profile/Contribution artefacts may be deployed through AI Deployment.

Bootstrap does not own:

- Deployment Set semantics;
- installation/update/remove/reconciliation;
- deployment permission/authority;
- package/source acquisition; or
- deployment verification.

Trusted-source resolution, package acquisition and automatic remediation remain intentionally
undesigned. A Profile's `Where` field never grants authority to acquire/install content.

A future authorised deployment process may obtain missing required material from trusted configured
sources without changing this Bootstrap boundary.

## §10 — Context economy

Bootstrap is not a universal eager include.

A Profile should establish only:

- what belongs in the startup set;
- what must be recognised or checked early;
- what must merely be discoverable; and
- where authoritative detail can be resolved.

Load full Standards/Tools/guidance only when current work needs them, unless the Profile deliberately
selects that material as startup guidance.

Thin Bootstrap information and lazy detailed material are a first-class design requirement.

## §11 — Subset-neutral examples

The same persistent bootstrap may support, for example:

```text
General Working Profile
  → Principles + Working Practices

AIDE Development Profile
  → broader AIDE operating set

No Profile
  → no Profile-selected AIDE startup set
```

Several subsets may be physically deployed to the same host. Only the effective Profile selects
which subset participates in Profile-driven startup processing.

## §12 — Intended output

This Design produces the canonical AI-facing Bootstrap contract:

```text
AIDE_Bootstrap@v2
```

Exact platform rendering of the persistent instruction, Profile and Contributions belongs to
Build/AI Deployment and must preserve these semantics without adding platform-specific behaviour to
Core.

## §13 — Deliberately deferred

- Profile merging/composition.
- Generic startup-task orchestration.
- Ordered Contribution execution.
- Automatic source/package acquisition.
- Trusted package catalogs.
- Generic installer behaviour.
- Broad startup migration scans.
- Full Standards/Tools inside Bootstrap Contributions.
- Item Type dependence for initial `{bootstrap}` discovery.
- Platform-specific enforcement beyond demonstrated capability.

---
Dependencies: !AIDE_DocumentationMethodology@v22, AIDE_Dependencies
References: Core_System_Design_v8, Core_Bootstrap_Decisions_v3
