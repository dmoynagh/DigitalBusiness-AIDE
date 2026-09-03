# Project Design — Project Knowledge Transfer

> **Transfer artefact — not an authoritative Project Design master.**
> Prepared 2026-09-03 for consolidation of the Project Design chat project into another AIDE project.
>
> Purpose: preserve useful Project Design-specific context that may have existed in project-level knowledge/memory rather than only in the moved chats or project source files. The destination project should reconcile this material against its current authoritative AIDE corpus and retain only what is not already represented there.

## Summary

There is very little substantive Project Design knowledge that appears to exist only in project-level context. The current Project Design Binder and Standards/Tools bundle already contain the important confirmed semantic model.

The items below are the remaining project-level continuity facts and operating conventions worth carrying across during project deletion. Several are also present in moved chats or have since been incorporated into current masters; they are included here defensively so the destination project does not depend on this project's retained memory.

## 1. Canonical Project Design naming and location

- The canonical top-level term is **`Project Design`**.
- The filename prefix remains **`ProjectDesign`**.
- Earlier references to **`Design Project`** were naming errors, not a historical canonical topic name.
- The earlier physical path statement `AIDE/Design Project/` was a factual path error, not a historical folder name.
- Current repository-relative Project Design location should be resolved from the authoritative Index/current repository layout. The current Project Design Binder records `Documentation/Project Design/` as the repository-relative master folder.

## 2. Confirmed Project Design / WorkRegister ownership boundary

Preserve this ownership split:

- **Project Design** owns the mandatory producer rule: every substantive confirmed Design change must identify downstream consequences; anything not fully delivered in the same pass must be recorded/updated in the owning top-level topic's WorkRegister.
- **Documentation Methodology** owns general WorkRegister admission/type semantics.
- WorkRegister is therefore not exclusively Design-generated and is not a generic backlog.
- Build reports execution evidence but does not close the WorkRegister; the directing/owning process performs reconciliation.
- A mapped Outcome that has returned but cannot be reconciled immediately uses compact state **`Returned — reconciliation pending`** before the context is left.
- WorkRegister ↔ WorkPackage mapping remains many-to-many.
- For deliberately split obligations, the current `AIDE_WorkPackage@v3` `Covers` rule identifies precise covered portions without requiring synthetic structured sub-obligation identifiers.

These semantics are already represented in the current Project Design and Documentation Methodology masters; retain them here only as a continuity check during consolidation.

## 3. Current WorkPackage handoff contract

Where Project Design hands work to Build, the current contract is:

`AIDE_WorkPackage@v3`

Do not reintroduce an active/current instruction to use `AIDE_WorkPackage@v2`. Historical Decision entries that truthfully record an earlier v2 state should remain historical rather than being rewritten.

## 4. Cross-topic editing convention

For AIDE work generally, when a confirmed Project Design change affects another AIDE topic and the current authoritative Binder/source context for that topic is available in the working context, prefer to apply the required changes directly to that topic's authoritative masters and include them in the same coordinated change package.

Use a **Project Handoff** only when the target topic cannot be safely edited from available authoritative context or a genuine transfer boundary exists.

This is an operating convention rather than Project Design semantic authority.

## 5. Output cadence / change batching

Do not output changed masters or a Change Delivery Package after every small confirmed change by default.

Instead:

- accumulate/queue confirmed changes through a meaningful work unit;
- issue updated masters/packages at the end of a significant work unit/session/checkpoint, when loss risk makes a checkpoint prudent, or when explicitly requested (for example, “output updates”, “update docs”, or “build change package”);
- avoid unnecessary version churn while never leaving material confirmed state only in volatile conversation.

This operating rule is primarily owned by Working Practices, but it materially affected how this Project Design project was run.

## 6. Change Delivery Package convention

When a ZIP / Change Delivery Package is produced for AIDE documentation work, include a concise **Change Delivery Instructions** file in the package by default, or provide equivalent application instructions in the response where a separate file is not appropriate.

Instructions should clearly identify, as applicable:

- Add;
- Replace Current;
- Move old issued versions to `_superseded`;
- Archive / withdraw / remove;
- Rename / move / ownership change;
- Binder/Bundle regeneration or replacement; and
- project-context/source additions or removals.

Management-folder conventions used in the wider AIDE workflow include `_superseded`, `_archived`, and `Documentation/_changeDeliveryPackages/` with completed packages moved beneath `_completed/`.

## 7. Binder handling

- Project Binders are generated, read-only consumption artefacts; authoritative masters remain the individual source files.
- Keep the current generated Binder in the topic's active/master folder under the applicable repository Working Practices.
- Binder filenames are versioned so the loaded project-context version is visible at a glance.
- Replaced Binder versions move to `_superseded` under the applicable physical workflow.
- Live WorkRegister/WIP/Working/OpenItems state is not part of the normal stable Binder unless a specialised live-state Binder is deliberately designed.

## 8. WIP continuity convention relevant to Project Design work

AIDE now uses one current WIP series per top-level topic, named from the top-level topic prefix, for example:

`ProjectDesign_WIP_vN.md`

Parallel subtopic/thread state is represented inside that WIP rather than through subtopic-specific WIP filenames. This convention is owned by Documentation Methodology / Working Practices rather than by Project Design itself.

## 9. Project Design release-lineage caution

The current Project Design semantic release is `AIDE_ProjectDesign@v6` in the transferred current Binder.

The release lineage around v4/v5 was specifically corrected in the current Project Design Binder:

- v4 was the WorkPackage preflight correction to the `AIDE_WorkPackage@v3` handoff target;
- v5 added flexible Design contributions, semantic-section hosting, and direct cross-Topic reconciliation;
- v6 added the current Design/Brief orientation model and Summary-to-Overview escalation rule.

Do not reconstruct this lineage from older project memory when the current Binder is available.

## 10. Outstanding-work caution during consolidation

An older `ProjectDesign_WorkRegister_v2` recorded an obligation to rebuild the common Standards & Tools Bundle so its Project Design member was no longer the old release. The subsequently supplied `AIDE_Bundle_StandardsTools_v9` already contains `AIDE_ProjectDesign_Standard_v6`.

Therefore, the old WorkRegister row should **not** be carried forward automatically as still outstanding. Reconcile against current generated bundle/source state first; on the available evidence, the original bundle-propagation objective appears to have been overtaken/satisfied by later bundle generations.

## Destination-project application

Treat this file as migration/continuity context only.

Recommended application:

1. Add any genuinely missing durable operating knowledge to the destination project's own project knowledge/memory.
2. Prefer the transferred current authoritative Binders/masters over this file whenever they differ.
3. Do not create new master-document versions solely because this transfer file restates information already incorporated in the current corpus.
4. After consolidation is verified, this transfer artefact may be retained with migration records or discarded; it is not a canonical AIDE source.
