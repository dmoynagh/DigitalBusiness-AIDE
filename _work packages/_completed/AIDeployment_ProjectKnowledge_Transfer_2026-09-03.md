# AI Deployment — Project Knowledge Transfer

> **Transfer date:** 2026-09-03  
> **Status:** Non-authoritative project-knowledge transfer artefact  
> **Purpose:** Preserve useful AI Deployment context that may exist in retained project/session knowledge outside the moved chat history and source/context files before the former project is deleted.

## Authority and use

All AI Deployment chats and source/context files have already been moved to the destination AIDE project. Those materials remain the evidence and authority for the work.

Treat the current AI Deployment masters / current `AIDeployment_Binder_v7.md` as authoritative for the design. This transfer does **not** create new architecture and must not override a newer master, Binder, Decision, Standard or Tool in the destination project.

The main conclusion from reviewing retained project knowledge is:

> There is no separate hidden AI Deployment architecture that needs to be promoted into authority. The durable extra value is mainly continuation intent, operating assumptions, empirical platform cautions and a small current-state reconciliation warning.

---

## Retained continuation knowledge worth preserving

### 1. AI Deployment was deliberately generalised beyond Capabilities

The design direction was intentionally broader than "deploy a Capability".

AI Deployment is intended to support deployment of validated built AIDE material generally, including as applicable:

- capability packages;
- Standards and Tools;
- skills/plugins and their contributions;
- Bundles / instruction representations;
- Bootstrap material;
- workflows, prompts/templates, knowledge or configuration artefacts where a producer supplies a conforming deployable Build output; and
- future deployable AIDE artefact kinds without requiring the generic Deployment architecture to become Capability-specific.

The old dedicated AI Deployment project was therefore a **working-context/container split**, not a reason to narrow semantic ownership. Consolidating it back into one AIDE project should not reverse the established producer / Build / Deployment ownership boundaries.

### 2. One deployment framework, but not one assumed runtime/channel

The intended outcome is one generic deployment/reconciliation model across relevant AI surfaces, while keeping actual Targets distinct.

Important retained platform intent:

- Claude account/plugin deployment and Claude Code/local plugin deployment can be independently reconciled Targets even when they consume the same built plugin Output.
- ChatGPT, Codex and other OpenAI surfaces must not be assumed to share executable reach merely because they can see the same plugin representation or marketplace source.
- A representation, distribution channel, runtime/surface, destination and pickup behaviour are separate facts.

This is why the design consistently treats runtime verification as stronger evidence than install/UI presence.

### 3. Manual Bundle replacement is intentionally a valid interim Target implementation

For surfaces where no reliable automated adapter exists, manual project/context Bundle replacement was deliberately accepted as a normal channel implementation of the same Deployment architecture.

It should not be treated as a temporary architecture exception that needs a second deployment model. A future automated sync/import/install adapter can replace the manual mechanics while preserving the same Set / Output / Target / State semantics.

### 4. Version visibility is an operational goal

A repeated deployment requirement was that deployed artefacts should make their concrete version/release identity readily visible where the platform permits it.

In particular:

- plugin/package/bundle outputs should use versioned identities or version-visible filenames/metadata where practical;
- replaced versions should remain distinguishable from the new current result; and
- operators should be able to determine which concrete artefact is installed/published rather than relying on an unversioned filename plus memory.

This is complementary to, not a substitute for, Deployment State. The architecture still distinguishes desired Set Release, publication state, platform-installed/attached state and runtime-observed state.

### 5. Runtime verification must be fresh enough for the claim being made

Retained empirical caution from platform work:

- UI presence, an enabled flag, repository publication, filesystem presence or marketplace visibility does not prove that the running AI surface can use the deployed material.
- Existing sessions may retain older/pinned state after an update; a fresh session can be necessary to establish pickup.
- A fresh target-appropriate runtime marker/content/behaviour probe is preferred when claiming executable availability.

Do not reconstruct a prior probe result or infer runtime execution from the presence of source files.

### 6. Concrete Build/package identity matters independently of semantic release

The project repeatedly distinguished semantic release identity from concrete Build/package identity.

A new Build of semantically unchanged material can still be a different deployable instance and may legitimately require Registry publication, Set resolution or Target reconciliation because PackageId, integrity, exact output bytes or runtime pickup changed.

Conversely, Deployment/Registry state must not become semantic production authority.

### 7. Empirical adapter questions remain different from generic architecture questions

The generic deployment layer was considered sufficiently defined for the initial AIDE Core outcome. Remaining uncertainties were deliberately classified as empirical/platform adapter work rather than reasons to reopen the generic model unless testing exposes a genuinely missing concept.

The retained empirical items include:

- exact supported ChatGPT reach of the OpenAI plugin for the configured account/workspace;
- which Claude installation actually governs the Claude Desktop Code-tab runtime;
- provider-specific adapter/install/update/remove mechanics not yet tested;
- exact platform-specific multi-member composition rules where needed;
- refresh/reload/new-session pickup behaviour on individual Targets; and
- future trusted package/catalog acquisition infrastructure and source-trust mechanics.

### 8. Consolidation removes an old transfer boundary, not the semantic topic boundary

Now that the former sibling projects are being consolidated into one AIDE project:

- keep **AI Deployment** as its own top-level semantic/documentation topic;
- do not reinterpret the old GPT Project boundary as architecture;
- where a confirmed AI Deployment change affects another AIDE topic and the destination project has the current authoritative Binder/source masters for that topic, update that owner directly in the same coherent change pass rather than creating a Project Handoff solely because the work used to live in separate GPT projects; and
- retain existing historical Project Handoff artefacts where useful as evidence, but do not create new cross-project ceremony when there is no longer a real transfer boundary.

---

## Retained ideas that should **not** be carried forward as unresolved

Earlier project knowledge included uncertainty around the final Registry term/contract, the Registry publish/register Tool, the minimal package-to-Registry interface and the final Set/output terminology.

Those are now superseded by the current AI Deployment corpus. In particular, the current Binder establishes the Deployment Registry, Deployable Package, immutable PackageId/current lifecycle split, `AIDE_DeploymentRegistryTool`, Deployment Set Releases, Deployment Outputs, Delivery Actions and Target Adapters.

Do **not** re-open those questions merely because older chat/context memory records them as pending. Re-open only if new evidence or a current Review finding identifies a defect.

---

## Current-state reconciliation warning observed during this transfer

This is not hidden project knowledge; it is an observed handover risk worth making explicit.

At the time this transfer note was created:

- `AIDeployment_Binder_v7.md` identifies the current deployment runtime contracts as `AIDE_Deployment@v7`, `AIDE_DeploymentTool@v7` and `AIDE_DeploymentRegistryTool@v2`, and it references current related producer contracts including `AIDE_CapabilityBuild@v4` and `AIDE_Tags@v3`.
- the provided `AIDE_Bundle_StandardsTools_v9.md` still contains `AIDE_Deployment_Standard_v6`, `AIDE_Deployment_Tool_v6`, `AIDE_DeploymentRegistry_Tool_v1`, `AIDE_CapabilityBuild_Standard_v3` and `AIDE_Tags_Standard_v2`.

Therefore the supplied Standards/Tools Bundle v9 should **not** be assumed to contain the latest AI Deployment-related Standards/Tools after the Review D R1 changes. Regenerate/reconcile the Bundle from the current authoritative Standards/Tools unless a later Bundle already exists in the destination project.

---

## Suggested destination-project treatment

1. Add this file as a **non-authoritative transfer/continuation artefact**, not as a master design document.
2. Use `AIDeployment_Binder_v7.md` and its current masters as the AI Deployment baseline.
3. Reconcile the Standards/Tools Bundle currency warning above against whatever is current in the destination project.
4. Once the destination project's retained knowledge clearly includes these continuation points, this transfer file may be archived with the project-consolidation records; it does not need to become a permanent semantic source.

---

## Source baseline consulted for reconciliation

- `AIDeployment_Binder_v7.md` — current AI Deployment generated Binder supplied to this project.
- `AIDE_Bundle_StandardsTools_v9.md` — current supplied common Standards/Tools Bundle at transfer time.

The retained knowledge above was intentionally reconciled against these current materials so that superseded project-memory uncertainty was not passed forward as current design state.
