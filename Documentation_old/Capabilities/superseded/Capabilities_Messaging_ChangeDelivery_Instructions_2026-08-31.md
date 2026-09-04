# Capabilities Messaging — Change Delivery Instructions — 2026-08-31

## Purpose

Apply the confirmed Messaging reconciliation as one coherent Capabilities checkpoint. This package
adds Messaging as the eighth peer capability, publishes canonical Messaging v1, resolves Review's
communication-owner seam through Review v2, closes WR16, and establishes the next peer architecture
Review item.

## Add — new Messaging masters

Add to `AIDE/Capabilities/`:

- `Capabilities_Messaging_Brief_v1.md`
- `Capabilities_Messaging_Design_v1.md`
- `Capabilities_Messaging_Decisions_v1.md`
- `Capabilities_Messaging_Tool_Design_v1.md`
- `AIDE_Messaging_Standard_v1.md`
- `AIDE_Messaging_Tool_v1.md`

These are the first authoritative AIDE Messaging masters/canonical outcomes.

## Replace Current — parent Capabilities masters

Add the new current files to `AIDE/Capabilities/` and move the replaced issued versions to
`AIDE/Capabilities/_superseded/`:

- `Capabilities_Index_v16.md` replaces `Capabilities_Index_v15.md`.
- `Capabilities_Brief_v8.md` replaces `Capabilities_Brief_v7.md`.
- `Capabilities_Overview_v14.md` replaces `Capabilities_Overview_v13.md`.
- `Capabilities_Design_v9.md` replaces `Capabilities_Design_v8.md`.
- `Capabilities_Decisions_v15.md` replaces `Capabilities_Decisions_v14.md`.

## Replace Current — Review masters/canonical outcomes

Add the new current files to `AIDE/Capabilities/` and move the replaced issued versions to
`AIDE/Capabilities/_superseded/`:

- `Capabilities_Review_Design_v2.md` replaces `Capabilities_Review_Design_v1.md`.
- `Capabilities_Review_Decisions_v2.md` replaces `Capabilities_Review_Decisions_v1.md`.
- `Capabilities_Review_Tool_Design_v2.md` replaces `Capabilities_Review_Tool_Design_v1.md`.
- `AIDE_Review_Standard_v2.md` replaces `AIDE_Review_Standard_v1.md` as current canonical Review Standard.
- `AIDE_Review_Tool_v2.md` replaces `AIDE_Review_Tool_v1.md` as current canonical Review Tool.

Leave `AIDE_ReviewProfiles_Standard_v1.md` unchanged/current. Review v2 changes only the resolved
communication dependency/ownership seam; Profiles semantics are unchanged. The v2 transition
posture is `None`.

## Replace Current — live WorkRegister

- `Capabilities_WorkRegister_v14.md` replaces `Capabilities_WorkRegister_v13.md`.
- Move `Capabilities_WorkRegister_v13.md` to `_superseded/`.
- WR16 is complete and is therefore removed rather than retained as history under v21 live-only
  WorkRegister semantics.
- WR17 is the new current confirmed undelivered item for the planned peer architecture Review.

## Withdraw — Messaging WIP

`Capabilities_Messaging_WIP_v1.md` has served its continuation purpose. Its material is now routed
into the authoritative Messaging Design/Decisions/Brief and current WorkRegister.

Withdraw it from the active master folder. For the current repository handling convention, move it
to `AIDE/Capabilities/_superseded/`; do not keep it loaded as live state and do not create a WIP v2.

## Generated Binders

Place these generated read-only consumption artefacts in the active `AIDE/Capabilities/` folder:

- `Capabilities_Binder_Core_v2.md` replaces `Capabilities_Binder_Core_v1.md`; move v1 to `_superseded/`.
- `Capabilities_Binder_Messaging_v1.md` is new.
- `Capabilities_Binder_Review_v2.md` replaces the currently loaded Review Binder; move the prior
  Binder issue to `_superseded/` according to its actual filename.

The Binders are not authoritative masters. Do not edit them directly.

## No change in this package

- `Capabilities_OpenItems_v15.md` remains current.
- `AIDE_ReviewProfiles_Standard_v1.md` remains current.
- The temporary account/project `AIDE_Bundle_StandardsTools_v5` is **not** rebuilt here. Platform/
  deployment artefacts are deliberately deferred until the planned architecture Review and later
  Build/AI Deployment work.

## Result after application

The current Capabilities architecture has eight peers: Standards, Tools, Tags, Scope, Dependencies,
Migration, Review and Messaging. Messaging v1 is canonical; Review v2 consumes Messaging; no
permanent Messaging obligations register or default Bootstrap Contribution exists; the next current
Capabilities work is WR17 peer architecture Review.
