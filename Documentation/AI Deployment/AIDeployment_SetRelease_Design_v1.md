# AI Deployment Set Release — Design

> **Version 1** (2026-09-02). Defines exact Set resolution, immutable Set releases, Deployment Outputs and trigger behaviour.

## Set Definition and exact resolution

A **Deployment Set Definition** identifies desired logical composition and the rules used to resolve
eligible registered supply. Resolution selects exact immutable PackageIds and exact compatible
built outputs; it does not reopen producer Design or infer missing target representations.

A candidate is valid only when all applicable required members, semantic required-presence facts
and required Deployment Outputs can be resolved, mechanically assembled and validated.

## Deployment Set Release

A **Deployment Set Release** is the immutable exact resolved content result:

```yaml
DeploymentSetRelease:
  Identity: <Set>@vN
  DefinitionRevision: <exact revision>
  ResolvedMembers: [<LogicalPackage, PackageId, BuildOutput, Integrity>]
  OutputDefinitions: [<identity and revision>]
  Outputs: [<identity and integrity>]
  ResolutionDigest: <digest>
```

`DesiredRelease` is the Set's mutable pointer to the release currently intended for Targets.
Previous releases remain immutable history. `Current` is not used for this pointer because Registry
Current Package state and successful target deployment are separate facts.

There is no generic downstream `Deployment Package`. Upstream Registry supply is a Deployable
Package; the final set-level consumable is a Deployment Output.

## Release creation

Resolve and validate a candidate before assigning the next issued version. A failed candidate does
not consume a Set release number and does not replace the last Desired Release.

A new release is required when exact selected PackageIds/build outputs, final output content, or a
Set/output Definition change alters the exact resolved result. Changed delivery destinations,
credentials, adapters, policy, refresh commands or later verification do not change Set content and
therefore do not alone create another Set release.

The platform-native version may map the AIDE release into a required syntax, but the canonical
identity remains `<Set>@vN`.

## Deployment Output Definitions

Each Definition selects compatible built contributions for one final representation and supplies
deterministic mechanical assembly/validation rules. `MemberContribution` outputs may be combined;
an `AssembledConsumptionArtefact` remains atomic at its Build-owned semantic composition boundary.

Bundle assembly defaults to stable logical Capability/member identity ordering. Ordering is not
semantic precedence unless an owning upstream contract explicitly makes it so.

Every final output carries an intrinsic runtime-visible marker:

```text
AIDE Set Release: <Set>@vN
Output: <output identity/type>
Resolved Set Digest: <digest>
```

Plugin assembly may add a small generated status member solely to expose this provenance. It is not
a Capability and has no independent semantic release.

## Trigger behaviour

Relevant Registry events cause Set re-evaluation. For an automatic Registry event, unchanged exact
resolution is a true no-op: no new release and no delivery retry. An explicit/manual Reconcile may
retry or re-verify failed, blocked, mismatched or unverified Targets of the existing Desired Release.

An Open Release Batch keeps staged changes outside ordinary Current resolution. Batch Release makes
the coordinated Registry changes visible once and therefore causes one Set re-evaluation.

---
Dependencies: !AIDE_DocumentationMethodology@v27, AIDE_Deployment@v6
References: AIDeployment_Registry_Design_v2, AIDeployment_TargetAdapter_Design_v1
