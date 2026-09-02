# Project Handoff — Build → AI Deployment

We have reconciled the AIDE **Build** model following the recent canonical guidance/bootstrap architecture work.

Treat the **current AI Deployment Binder/current masters in the AI Deployment project as authoritative**. This Handoff carries a Build-owned consequence for reconciliation; it is not itself an authoritative AI Deployment source.

## Reason for the Handoff

Build now makes explicit the general production boundary:

```text
current authoritative/canonical semantic source
        ↓
Build
        ↓
platform-compatible artefact / representation / package / assembled consumption artefact
        ↓
AI Deployment
        ↓
target-state reconciliation + delivery/install/update/remove + runtime verification
```

A successful Build does not claim that its output is deployed or runtime-usable.

Build also makes explicit that derived representations are produced from current authoritative inputs, not from an older Bundle/package as a substitute source of truth, and that Build may produce independently deployable subsets rather than assuming one full-AIDE package.

## AI Deployment seam to reconcile

The current `AIDE_Deployment@v1` wording includes:

- Deployment reconciliation step: `compose the target representation deterministically`; and
- boundary wording that AI Deployment owns `set-aware composition, delivery/reconciliation and verification` while Build owns `target-compatible member/contribution production`.

This may already be intended as **mechanical target assembly/orchestration of built contributions** rather than semantic Build production. If so, no architectural mechanism change is required, but the wording should be checked so it cannot be read as AI Deployment independently rebuilding canonical Standards/Tools into target representations.

## Proposed ownership interpretation

Preserve:

```text
Build
→ render/transform/package authoritative semantics into build outputs
→ may assemble an authorised consumption representation when that is the Build output
→ reports source identity/version provenance

AI Deployment
→ owns Deployment Set desired composition
→ selects/consumes the appropriate built members/artefacts for a Target
→ may perform target-specific mechanical assembly required for reconciliation
→ installs/updates/removes/reconciles target state
→ verifies actual target/runtime availability
```

The important distinction is semantic production versus target-state reconciliation. AI Deployment should not become a second semantic renderer from Design history or stale deployed material.

## Bootstrap consequence

Bootstrap/Profile/Contribution/full Standard or Tool remain distinct semantic roles upstream of Deployment. Deployment may place built forms into target-specific locations/compositions, but should not collapse those roles or infer missing Bootstrap semantics.

## Requested reconciliation

Please check the current AI Deployment Design/Decisions/Standard/Tool and determine whether the existing wording already preserves this boundary.

If it does, no new mechanism is needed.

If wording such as `compose the target representation deterministically` is materially ambiguous, tighten it so that:

1. Build production remains upstream;
2. Deployment owns desired composition and target reconciliation;
3. any Deployment-time composition is clearly mechanical assembly of already built/authoritative members rather than independent semantic production; and
4. deployment status never substitutes for Build/canonical provenance.

Do not modify Build masters from AI Deployment. Return any material Build-owned consequence as a Project Handoff.
