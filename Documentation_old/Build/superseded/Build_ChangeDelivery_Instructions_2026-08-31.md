# Build — Change Delivery Instructions — 2026-08-31

## Purpose

Apply the Build reconciliation for canonical guidance/bootstrap architecture with the smallest Build-owned change set.

The resulting Build position is:

- canonical/authoritative semantics remain upstream of platform/consumption representations;
- Build may render/package authorised subsets without assuming the full AIDE system;
- Build preserves distinct upstream semantic roles such as Bootstrap/Profile/Contribution/full Standard;
- generated Bundles/packages are derived consumption/build artefacts, not authoritative sources;
- derived outputs record enough source identity/version provenance to be reproducible;
- insufficient canonical semantics return upstream rather than being invented during Build; and
- Build output is distinct from AI Deployment target-state reconciliation and verification.

No new Bootstrap-specific Build mechanism is introduced. `AIDE_WorkPackage@v1` remains unchanged.

## Apply to AIDE/Build masters

### Add / Replace Current

Add these files to the current Build master folder `AIDE/Build/`:

- `Build_Index_v2.md` — replaces current `Build_Index_v1.md`.
- `Build_Design_v2.md` — replaces current `Build_Design_v1.md`.
- `Build_Decisions_v2.md` — replaces current `Build_Decisions_v1.md`.
- `AIDE_Build_Standard_v2.md` — replaces current `AIDE_Build_Standard_v1.md`; canonical identity becomes `AIDE_Build@v2`.

### Move to `_superseded`

Move the replaced issued versions to the Build project's `_superseded/` management folder:

- `Build_Index_v1.md`
- `Build_Design_v1.md`
- `Build_Decisions_v1.md`
- `AIDE_Build_Standard_v1.md`

### Leave Current unchanged

Do not replace or reissue:

- `Build_WorkPackage_Design_v1.md`
- `AIDE_WorkPackage_Standard_v1.md`

The Handoff did not expose a material WorkPackage semantic gap.

## Binder change

Add `Build_Binder_v2.md` as the new generated Build Binder and use it as the Build project-context Binder.

Replace/remove the previously loaded unversioned `Build_Binder.md` from active project context. Move the old generated Binder to the normal `_superseded/` location if retained locally.

The Binder is derived and must not be edited directly.

## Common Standards/Tools Bundle

Do **not** patch `AIDE_Bundle_StandardsTools_v3.md` directly from this package.

It is now stale with respect to Build because it contains `AIDE_Build@v1`. The wider Handoff also identifies newer canonical `AIDE_Bootstrap@v1`, `AIDE_Principles@v1`, `AIDE_WorkingPractices@v1` and `AIDE_Domain@v1` material that is not safely reconstructable from this Build package alone.

Regenerate the common Bundle in the planned cross-project Bundle build using current Binders/current canonical Standards/Tools from every owning AIDE project. During that build, select `AIDE_Build@v2` from `Build_Binder_v2.md` and record the selected source identity/version in the Bundle manifest/provenance.

Only replace Bundle v3 in project contexts once that full current-source regeneration is complete.

## AI Deployment Project Handoff

`Project_Handoff_Build_to_AI_Deployment_2026-08-31.md` is a transfer artefact, not a Build or AI Deployment master.

Paste/pass it into the AI Deployment project and reconcile it against that project's current Binder/masters.

The specific seam to review is current AI Deployment wording around `compose the target representation deterministically` / `set-aware composition`. The goal is to distinguish:

- Build semantic rendering/packaging of authoritative material; from
- Deployment desired composition, target-specific mechanical assembly where needed, state reconciliation, delivery and runtime verification.

Do not modify AI Deployment masters directly from this package.

## Capability/version consequence

`AIDE_Build@v2` declares `Transition: v2 / Posture: None`.

Existing consumers checkpointed against `AIDE_Build@v1` do not require state transformation merely because v2 is available. Their dependency checkpoint advances only through the normal Dependencies/Migration/save rules when applicable.

## Project-context changes

After applying the master changes:

1. replace the Build project-context Binder with `Build_Binder_v2.md`;
2. do not add this Change Delivery Instructions file as authoritative project context;
3. do not treat the Project Handoff file as a Build master; and
4. later replace the common Standards/Tools Bundle only after the full cross-project regeneration described above.

## Package contents

```text
Build_ChangeDelivery_2026-08-31.zip
├── Build_Index_v2.md
├── Build_Design_v2.md
├── Build_Decisions_v2.md
├── AIDE_Build_Standard_v2.md
├── Build_Binder_v2.md
├── Project_Handoff_Build_to_AI_Deployment_2026-08-31.md
└── Build_ChangeDelivery_Instructions_2026-08-31.md
```
