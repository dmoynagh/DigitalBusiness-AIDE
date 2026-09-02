# Working Practices — Change Delivery Instructions — 2026-08-31-2

> Transfer/application artefact. Not an authoritative corpus master.

## Purpose

This is a corrective **pre-distribution reconciliation** of the Working Practices master folder.

The previously applied files combined two branches of work inconsistently: the Current v4/v3
Project Handoff branch and the later Documentation Methodology v20 repository/Binder branch.
Nothing has yet been distributed, so this package corrects the existing issue contents **without
incrementing their document version numbers**.

The formal capability identity remains:

```text
AIDE_WorkingPractices@v1
```

No Working Practices consumer migration is created because there is no distributed earlier
Working Practices capability state to migrate.

## Destination

Apply to:

```text
AIDE/Working Practices/
```

## Replace Current in place

Replace the contents of these Current files using the package copies, retaining the same filenames
and version numbers:

| File | Action |
|---|---|
| `WorkingPractices_Index_v4.md` | Replace Current in place with corrected v4 content. |
| `WorkingPractices_Brief_v3.md` | Replace Current in place with corrected v3 content. |
| `WorkingPractices_Design_v4.md` | Replace Current in place with corrected v4 content. |
| `WorkingPractices_Decisions_v4.md` | Replace Current in place with corrected v4 content. |
| `AIDE_WorkingPractices_Standard_v3.md` | Replace Current in place with corrected v3 content. |

Do **not** move the replaced pre-distribution copies to `_superseded/` merely because their contents
were corrected. They are the same not-yet-distributed document issues being finalised before
publication.

## Correct Current register after application

The Current set is:

```text
WorkingPractices_Index_v4.md
WorkingPractices_Brief_v3.md
WorkingPractices_Design_v4.md
WorkingPractices_Decisions_v4.md
AIDE_WorkingPractices_Standard_v3.md
```

The formal published capability identity is still:

```text
AIDE_WorkingPractices@v1
```

## Generated Binder

Replace the current generated `WorkingPractices_Binder_v1.md` **in place** with the package copy.

Binder v1 remains appropriate because this is correction of the first Binder before distribution,
not a later issued Binder replacement.

The corrected Binder manifest must contain exactly:

```text
Index v4
Brief v3
Design v4
Decisions v4
AIDE_WorkingPractices Standard document v3
```

with hashes matching the corrected files.

If `WorkingPractices_Binder_v1.md` is already loaded into this GPT Project context, remove/re-add
the corrected Binder so the loaded content is the corrected assembly.

## What this correction preserves and adds

The corrected corpus preserves the complete existing Project Handoff contract, including:

- material-knowledge trigger;
- proactive suggestion/production;
- proportionate Handoff contents;
- destination reconciliation against current Binder/masters;
- ownership-preserving `originating project → Handoff → owning project → authoritative update`;
- separation from separately authorised cross-project master editing; and
- distinction between Project Handoff and Change Delivery Package.

It also incorporates the confirmed Documentation Methodology v20 consequences:

- Documentation Methodology owns lifecycle meaning; Working Practices owns practical physical
  repository/workflow handling;
- management/structural folders use `_` where useful;
- current physical conventions include `_superseded/` and `_archived/`;
- Change Delivery ZIPs stage in `Documentation/_changeDeliveryPackages/` and complete in
  `Documentation/_changeDeliveryPackages/_completed/`;
- historical management material may periodically leave the active repository while required
  history/traceability is preserved;
- generated Binders are independently versioned;
- the current Binder stays with active masters; and
- a replaced Binder becomes Superseded because it was replaced, not because of its folder.

## Do not restore the superseded branch

Do not restore the intermediate branch whose Current model was:

```text
Index v3
Brief v3
Design v3
Decisions v3
AIDE_WorkingPractices Standard v2 / AIDE_WorkingPractices@v2
```

That branch incorrectly treated the new conventions as a new capability release and weakened the
already-developed Project Handoff contract.

## Bundle / build / deployment consequence

Nothing has yet been distributed from Working Practices. On the next normal Bundle/build/deployment
reconciliation, use:

```text
AIDE_WorkingPractices_Standard_v3.md
Identity: AIDE_WorkingPractices@v1
```

as the canonical Working Practices member.

Do not use `AIDE_WorkingPractices_Standard_v2.md`.

Documentation Methodology v20 and other Bundle updates remain part of the separate Bundle
reconciliation job.

## Change Delivery Package handling

Stage this ZIP in:

```text
Documentation/_changeDeliveryPackages/
```

while applying/reviewing it.

After the corrected masters, Binder and project context have been verified, move this ZIP to:

```text
Documentation/_changeDeliveryPackages/_completed/
```

The earlier applied Working Practices Change Delivery package may remain as completed transfer
history; it is not an authoritative corpus source.

## Verification

After application:

1. the master folder contains the five Current masters listed above plus
   `WorkingPractices_Binder_v1.md`;
2. Index v4 registers Brief v3, Design v4, Decisions v4 and Standard document v3;
3. every Current master that depends on Documentation Methodology records v20;
4. Design/Brief/Index/Standard consistently identify `AIDE_WorkingPractices@v1`;
5. Standard v3 contains the full Project Handoff contract plus WP9/WP10;
6. Binder v1 manifest hashes match the five corrected Current masters; and
7. the loaded project-context Binder is the corrected Binder v1.
