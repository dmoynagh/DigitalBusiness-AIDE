# AI Deployment Target Adapter — Design

> **Version 1** (2026-09-02). Defines Delivery Actions, Target Adapters, layered verification, Deployment State and invocation Result.

## Relationship

```text
Deployment Set Release
  → Deployment Output
  → one or more Deployment Targets
  → Target Adapter
  → publish / install / attach / refresh / remove
  → verify
  → Deployment State + Deployment Result
```

One output may feed several independently reconcilable Targets. A Target Adapter is the
platform/channel-specific implementation behind an existing Deployment Target, not a new top-level
deployment concept.

## Target Adapter contract

```yaml
TargetAdapter:
  Representation: <Plugin | Bundle | other>
  Channel: <GitMarketplace | LocalFile | ManualUpload | other>
  Destination: <environment-owned reference>
  Actions:
    Publish: <mechanism>
    InstallOrUpdate: <mechanism if available>
    Remove: <mechanism if available>
  Pickup: <immediate | refresh | reload | new-session | manual | unknown>
  Verification:
    Publication: [<checks>]
    PlatformState: [<checks>]
    RuntimeState: [<checks/probes>]
  Policy: <environment Deployment Policy>
```

Concrete layouts, commands, Git mechanics, UI actions, destinations and credentials remain adapter/
environment configuration rather than Capability semantics or generic Deployment rules.

## Delivery Action

A **Delivery Action** is an idempotent configured operation that moves one or more Deployment
Outputs toward one or more Targets. It identifies input Output, Adapter, Destination, invocation
mode, prerequisites and action-level verification. It owns no semantic content and is not part of
the immutable Set release.

Several outputs may share one convenient publication action, such as one repository commit, without
claiming atomic installation or activation across their later runtime Targets.

## Verification layers

Use the layers a Target actually exposes:

1. **Output** — frozen release, integrity, expected marker and valid assembly.
2. **Publication** — expected bytes/revision exist at the distribution destination.
3. **Platform** — expected release is installed, attached or resolved by the platform.
4. **Runtime** — the running surface observes the intrinsic release marker and, where needed,
   passes a behaviour probe.

Visibility or installation alone does not prove runtime execution. Published, installed/attached
and runtime-observed releases may differ.

Verification assurance is:

- `Enforced` when evidence is obtained independently of model choice/compliance; or
- `Advisory` when the model materially selects, executes or reports the check.

## Deployment State

State is mutable and per Target. Record, as applicable:

```yaml
DeploymentState:
  Target: <identity>
  Desired: <SetRelease, Output, Integrity>
  Publication: <observed release and evidence>
  Platform: <installed/attached release and evidence>
  Runtime: <observed release, availability and session pickup>
  Verification:
    Status: Verified | Mismatch | Unverified
    Assurance: Enforced | Advisory
    Evidence: <reference>
    EvidenceAt: <time>
  Mismatches: [<facts>]
  NextAction: [<actions>]
```

## Deployment Result

A Result records one reconciliation invocation rather than duplicating persistent State. Use:

- `Complete` — every requested Target is at the required verified desired state, including a
  verified no-op;
- `Partial` — some requested Targets are Complete and others remain blocked, failed or unverified;
- `Blocked` — a known authority, prerequisite, manual action or required-verification condition
  prevents progress; or
- `Failed` — an attempted operation or validation failed.

Report target-level `Applied | NoOp | ManualRequired | Failed` action facts and the resulting State.

---
Dependencies: !AIDE_DocumentationMethodology@v27, AIDE_Deployment@v6
References: AIDeployment_SetRelease_Design_v1, AIDeployment_AIDECore_Reference_v1
