# Core Bootstrap — Design

> **Version 2** (2026-08-31). Reissued against Core Domain integration and Documentation
> Methodology v19; confirms Bootstrap Profiles, thin Contributions, dependency reuse and the
> deployment boundary.
>
> Created: 2026-08-31 | Last modified: 2026-08-31

## §1 — Purpose and ownership

Bootstrap is the stable AIDE activation seam between an AI platform's persistent machine-level
instructions and the deployable guidance, Standards, Tools and other AIDE material available to a
particular environment.

Bootstrap belongs to Core because it must work before any individual component can assume its full
operating material is already in context.

Core/Bootstrap owns:

- the stable bootstrap primitive;
- Bootstrap Profile semantics;
- Bootstrap Contribution discovery/ordering conventions;
- best-effort early-session processing;
- the boundary between startup activation and lazy detailed context; and
- deterministic failure when competing startup posture cannot be resolved.

It does not own the substantive behaviour of the material it activates.

## §2 — Level 1 model

```text
persistent platform bootstrap
        ↓
Bootstrap Profile
        ↓
thin Bootstrap Contributions
        ↓
full guidance / Standards / Tools loaded when needed
```

The machine-level instruction should be tiny and rarely changed. Environment-specific behaviour
changes by deploying/changing the Profile and referenced material, not by rewriting global
instructions for every release.

## §3 — Persistent platform bootstrap

Deploy the stable primitive through the strongest persistent mechanism available to the platform,
for example ChatGPT Custom Instructions, Claude instructions, Codex/global machine instructions or
an equivalent future surface.

Its job is only to:

1. discover an applicable Bootstrap Profile where available;
2. establish/process that Profile before substantive work where the platform permits;
3. process applicable available Bootstrap Contributions;
4. continue normally where no Profile is available; and
5. reconsider bootstrap only when materially new startup/profile/environment information becomes
   available.

Do not hard-code current AIDE component versions or copy detailed operational Standards into the
persistent platform instruction.

Platform implementations must not claim stronger startup enforcement than the platform provides.

## §4 — Bootstrap Profile

A Bootstrap Profile is an environment-specific **startup map**.

Each Profile entry identifies only:

```text
WHAT  — the guidance/capability/material to bring into play
WHY   — why or when it matters in this environment
WHERE — how the authoritative deployed material can be resolved
```

The Profile does not reproduce the referenced material.

Examples of possible Profiles include:

```text
AIDE Development
General Working
Documentation
Build-oriented environment
```

A general Profile may identify only Principles and Working Practices. A full development Profile
may additionally establish awareness of Core, Domain, Project Design, Build, Documentation
Methodology and relevant Capabilities.

### One effective Profile by default

At most one effective Profile applies to an environment/context by default.

Profile merging/precedence is not designed in v1. If competing Profiles are simultaneously
applicable and no explicit future composition rule resolves them, fail visibly rather than invent
an order.

No Profile is a valid state.

## §5 — Bootstrap Contributions

A Bootstrap Contribution is a **thin, separately deployable early-session instruction** owned by
the Standard, behaviour or component that needs it.

A Contribution exists only where delay until normal use would lose meaningful value.

It should contain only enough to identify:

- its owner/identity;
- the early concern/action/check;
- why/when it applies; and
- where the detailed authoritative material can be loaded when needed.

The full Standard, Tool, history or Guide remains separate.

`{bootstrap}` is the generic marker for content requiring best-effort early-session discovery.
The marker supplies no component-specific semantics.

## §6 — Startup-required dependencies

Bootstrap does not create another dependency grammar.

Where a Profile or owner requires material to be present at startup, declare that through
`AIDE_Dependencies`. The Dependencies owner defines the presence/version/startup marker semantics.

Bootstrap supplies the early-session opportunity to evaluate or surface that requirement.

A missing required item is a visible environment/deployment condition. Bootstrap does not silently
reinterpret the requirement because a deployment set omitted the item.

A startup presence check does not imply a blanket startup migration/current-version scan.

## §7 — Startup tasks

Do not introduce a generic startup-task framework in the current model.

The demonstrated needs are covered by:

- Profile activation;
- owner-defined thin Bootstrap Contributions; and
- startup-required dependency presence checks.

If a future early-session action cannot fit these mechanisms without distortion, design the
additional task concept from that demonstrated case.

## §8 — Deployment boundary

Bootstrap can be part of Deployment but does not govern Deployment.

Keep separate:

```text
requirement            → declaring owner + Dependencies
observed environment   → Environment / applicable presence mechanism
startup surfacing      → Bootstrap
permission/authority   → host administrator / controlling deployment process
deployment action      → AI Deployment
```

Bootstrap never gains installation authority merely by declaring a requirement or locator.

AI Deployment owns installation/update/remove/reconciliation/verification. The entity authorised to
control the host environment decides what may be deployed according to that environment's process
or policy; Core Bootstrap does not define a new formal deployment role.

## §9 — Future source acquisition

The architecture must permit a future flow such as:

```text
required identity missing
        ↓
trusted source/catalog resolution
        ↓
host/deployment policy permits acquisition
        ↓
AI Deployment obtains / installs / verifies
```

Trusted-source resolution, package acquisition and automatic remediation are intentionally not
designed now.

A Profile's `WHERE` field is a locator/discovery aid, not authority to execute or install content
from an arbitrary source.

## §10 — Context economy

Bootstrap is not a universal eager include.

A Profile should establish only:

- what must be recognised now;
- what must be checked now;
- what must merely be discoverable; and
- where authoritative detail can be resolved.

Load full Standards/Tools/guidance when the current work needs them.

Thin bootstrap information and lazy detailed material are a deliberate design requirement.

## §11 — Relationship to Principles and Working Practices

Bootstrap activates guidance; it does not own guidance semantics.

For example:

```text
General Working Profile
  WHAT  AIDE_Principles
  WHY   base reasoning/problem-solving guidance
  WHERE deployed guidance location

  WHAT  AIDE_WorkingPractices
  WHY   base collaboration/operating conventions
  WHERE deployed guidance location
```

The same persistent platform bootstrap can therefore support full AIDE, a narrow guidance-only
environment or no AIDE Profile.

## §12 — Intended output

This Design produces the canonical AI-facing Bootstrap contract:

```text
AIDE_Bootstrap@v1
```

Exact platform rendering of the persistent instruction, Profile and Contributions belongs to
Build/AI Deployment and should preserve these semantics without adding platform-specific behaviour
to Core.

## §13 — Deliberately deferred

- Profile merging/composition.
- Generic startup-task orchestration.
- Automatic source/package acquisition.
- Trusted package catalogs.
- Generic installer behaviour.
- Broad startup migration scans.
- Full Standards/Tools inside Bootstrap Contributions.
- Platform-specific enforcement beyond demonstrated capability.

---
Dependencies: !AIDE_DocumentationMethodology@v19, AIDE_Dependencies
References: Core_System_Design_v6, Core_Bootstrap_Decisions_v2
