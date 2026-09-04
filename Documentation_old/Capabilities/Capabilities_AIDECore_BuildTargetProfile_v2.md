# AIDE Core — Build Target Profile

> **Version 2** (2026-09-03). Applies the clarified producer-side RequiredReach contract without claiming concrete Target state.

## Identity and membership

```yaml
BuildTargetProfile:
  Identity: AIDE_Core
  Revision: v2
  MemberCapabilities:
    - Standards
    - Tools
    - Tags
    - Scope
    - Dependencies
    - Migration
    - Review
    - Messaging
  OutputTag: AIDE_Core
```

The explicit member list is the current Profile-owned Build configuration. It does not change the
semantic composition/release of any member Capability. Add/remove decisions are Profile changes and
must be reflected in a later Profile revision.

## Target Definitions

```yaml
BuildTargets:
  ClaudePlugin:
    Representation: ClaudePluginContribution
    OutputRole: MemberContribution
    RequiredReach: [ClaudeAccount, ClaudeCode]
    Conformance: FullUnlessDeclaredOverride
    Tags: [AIDE_Core]

  ClaudeBundle:
    Representation: ClaudeBundleContribution
    OutputRole: MemberContribution
    RequiredReach: [ClaudeBundle]
    Conformance: FullUnlessDeclaredOverride
    Tags: [AIDE_Core]

  ChatGPTBundle:
    Representation: ChatGPTBundleContribution
    OutputRole: MemberContribution
    RequiredReach: [ChatGPTBundle]
    Conformance: FullUnlessDeclaredOverride
    Tags: [AIDE_Core]

  OpenAIPlugin:
    Representation: OpenAIPluginContribution
    OutputRole: MemberContribution
    RequiredReach: [Codex]
    AdditionalReach: [ChatGPTWhereSupported]
    Conformance: FullUnlessDeclaredOverride
    Tags: [AIDE_Core]
```

Every applicable member Capability must supply all four target contributions before a complete
Profile-conforming Capability Package is issued. A producer-owned explicit `NotApplicable` or
permitted degradation declaration is evaluated under the Profile/Capability Build contract and is
carried into the immutable Package for downstream selection and verification.

The four Build Targets are representation contributions, not runtime/install Targets. In
particular, the single `ClaudePlugin` contribution may later be assembled into one plugin output
that is reconciled independently to Claude account and Claude Code Deployment Targets.

`RequiredReach` states the producer representation obligation under applicable supported
conditions. Concrete repository publication, installation, attachment, policy, session pickup and
runtime success remain independently observed AI Deployment facts. Contradictory repeated or
authoritative deployment evidence is returned for Profile/Working Surface reassessment rather than
silently changing this Profile.

## Bundle contribution ordering

Profile members do not declare semantic precedence through file order. Deployment Set assembly uses
stable logical Capability/member identity ordering unless a future owner contract supplies a
genuine semantic ordering requirement.

## Boundary

This Profile contains no marketplace repository, filesystem destination, account/workspace,
credential, update command, refresh rule or runtime verification state. Those are AI Deployment
configuration/adapter facts.

---
Dependencies: !AIDE_DocumentationMethodology@v28, AIDE_CapabilityBuild@v4
References: Capabilities_BuildTargetProfile_Design_v2, AIDeployment_AIDECore_Reference_v2
