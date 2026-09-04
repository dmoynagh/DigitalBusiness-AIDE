# AIDE Core Deployment — Reference Configuration

> **Version 2** (2026-09-03). Makes AIDE Core desired membership explicit and updates the bundle publication repository path.

## Shared identity

`AIDE_Core` is reused deliberately as three related but distinct identities:

| Layer | Meaning |
|---|---|
| Build Target Profile | reusable four-target Capability Build requirements |
| Registry/package tag | classification of eligible AIDE Core built contributions |
| Deployment Set | logical desired composition resolved from Registry supply |

The immutable exact Set release is `AIDE_Core@vN`.

## Deployment Set and Outputs

```yaml
DeploymentSetDefinition:
  Identity: AIDE_Core
  MembershipMode: Fixed
  RequiredMembers:
    - Standards
    - Tools
    - Tags
    - Scope
    - Dependencies
    - Migration
    - Review
    - Messaging
  SupplySelector:
    TagQuery: AIDE_Core
    PackageRelation: Current
  RequiredOutputDefinitions:
    - ClaudePlugin
    - ClaudeBundle
    - ChatGPTBundle
    - OpenAIPlugin
  ReleaseIdentity: AIDE_Core@vN
  CandidatePolicy: IssueOnlyAfterAllRequiredOutputsValidate

DeploymentOutputs:
  ClaudePlugin:
    Inputs: BuildTarget=ClaudePlugin
    Assembly: DeterministicMemberContributionAssembly
    Identity: aide-core-claude

  ClaudeBundle:
    Inputs: BuildTarget=ClaudeBundle
    Assembly: StableLogicalMemberOrder
    Identity: AIDE_Core_Claude_Bundle_vN.md

  ChatGPTBundle:
    Inputs: BuildTarget=ChatGPTBundle
    Assembly: StableLogicalMemberOrder
    Identity: AIDE_Core_ChatGPT_Bundle_vN.md

  OpenAIPlugin:
    Inputs: BuildTarget=OpenAIPlugin
    Assembly: DeterministicMemberContributionAssembly
    Identity: aide-core-openai
```

Every output carries `AIDE_Core@vN`, its output identity/type and the resolved-set digest. Plugin
outputs include the generated provenance-only `aide-core-status` member.

## Delivery Actions and destinations

```yaml
DeliveryActions:
  PublishAIDECoreMarketplace:
    Inputs: [ClaudePlugin, OpenAIPlugin]
    Channel: GitMarketplace
    Repository: DigitalBusiness-AIDE-Marketplace
    Areas:
      ClaudePlugin: claude/
      OpenAIPlugin: openai/
    Evidence: GitCommit

  PublishAIDECoreBundles:
    Inputs: [ClaudeBundle, ChatGPTBundle]
    Channel: LocalFile
    RepositoryRoot: 'C:\Users\david\dev\repos\DigitalBusiness-AIDE'
    Destination: 'C:\Users\david\dev\repos\DigitalBusiness-AIDE\Documentation\_deploymentPackages'
    SupersededDestination: 'C:\Users\david\dev\repos\DigitalBusiness-AIDE\Documentation\_deploymentPackages\_superseded'
    Rule: MoveEarlierCurrentBundlesThenPublishBothNewVersionedFiles
```

The shared Git commit/local operation is an implementation convenience and provenance point, not a
cross-runtime transaction guarantee.

## Target map

| Output | Deployment Target | Initial adapter/pickup posture |
|---|---|---|
| Claude Plugin | Claude account plugin | marketplace/account update; account-backed surfaces reconcile together where platform evidence supports it |
| Claude Plugin | Claude Code plugin | separate local marketplace/plugin update and reload/session pickup |
| Claude Bundle | local published bundle | automatic versioned file replacement/publication |
| Claude Bundle | configured Claude contexts | manual/platform-specific placement until a verified adapter exists |
| ChatGPT Bundle | local published bundle | automatic versioned file replacement/publication |
| ChatGPT Bundle | configured ChatGPT contexts | manual/upload/import until a verified adapter exists |
| OpenAI Plugin | GitHub/OpenAI marketplace publication | repository publication and marketplace sync/import |
| OpenAI Plugin | required Codex target | install/update then runtime marker/behaviour verification |
| OpenAI Plugin | supported ChatGPT target | additional reach only where that surface supports the plugin |

The Claude account and Claude Code installations are independently reconcilable even though they
consume one Claude plugin output. Which installation governs a particular Claude Desktop Code-tab
runtime remains an empirical adapter fact to re-probe; architecture does not assume it.

## Trigger configuration

Re-evaluate `AIDE_Core` on:

```text
PackageCurrentChanged
PackageDeprecated
PackageWithdrawn
ReleaseBatchReleased
Deployment Set/output Definition change
Target/environment configuration change
explicit/manual Reconcile
```

For Registry events, resolve first and no-op when exact state is unchanged. A target/environment
configuration change reconciles the existing Desired Release unless content changes. Manual
Reconcile may retry or re-verify incomplete Targets without issuing a new Set release.

## Verification baseline

Record Desired Release, publication state, installed/attached platform release, runtime-observed
release, verification status and assurance separately. A Target becomes fully verified only after
its required release-marker and behaviour checks pass. Manual placement/action is reported as
`ManualRequired`; local publication alone does not claim a project/chat context is using the bundle.

---
Dependencies: !AIDE_DocumentationMethodology@v28, AIDE_Deployment@v7, AIDE_CapabilityBuild@v4
References: Capabilities_AIDECore_BuildTargetProfile_v2, AIDeployment_SetRelease_Design_v2, AIDeployment_TargetAdapter_Design_v1, AIDeployment_OpenAI_Reference_v3
