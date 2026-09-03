# AIDE Build — Project Knowledge Transfer

> **Transfer artefact — not an authoritative corpus master.**
> Created 2026-09-03 for consolidation of the former **AIDE Build** project into the destination **AIDE** project.
>
> The chats and project source/context files have already been transferred separately. This document records durable project/context knowledge that may have been retained outside those files and therefore could otherwise be lost when the source project is deleted.

## How to use this transfer

- Treat the destination project's current authoritative AIDE masters/binders as the source of truth.
- Use this document only to restore useful working conventions, remembered decisions and project-operating context that are not already represented there.
- If a statement here conflicts with a current authoritative source, keep the authoritative source and treat this transfer statement as stale context requiring reconciliation.
- Do not create new corpus mechanisms solely because they appear in this transfer; first check whether the current corpus already expresses them.

## 1. Change/output cadence

AIDE documentation/build work should **not output changed master files or a Change Delivery Package after every individual confirmed change by default**.

Preferred operating model:

- accumulate/queue confirmed changes during a meaningful unit of work;
- issue changed files/packages at the end of a significant work unit, work session or checkpoint;
- output earlier when the user explicitly requests it (for example: `output updates`, `update docs`, `build change file/package`); and
- never delay output when doing so creates a material risk of losing confirmed state.

The purpose is to reduce version/package churn without risking loss of work.

## 2. Change Delivery Package convention

When a Change Delivery Package or ZIP is produced, include a concise **Change Delivery Instructions** document inside the package by default, unless equivalent application instructions are more appropriate in the response.

The instructions should state, for every affected file/project, what action is required and where, including as applicable:

- **Add**;
- **Replace Current**;
- **Move to `_superseded`**;
- **Archive / withdraw / remove**;
- **Rename / move / ownership change**; and
- any Binder/regeneration action required after application.

Normal staging convention retained in project context:

```text
Documentation/_changeDeliveryPackages/
Documentation/_changeDeliveryPackages/_completed/
```

Packages are staged in `_changeDeliveryPackages/` and moved to `_completed/` after application. Management folders may later be archived outside the repository.

## 3. Structural/management folder naming

Durable AIDE repository/documentation convention:

- structural/management folders are prefixed with `_`;
- `superseded` is represented as `_superseded`;
- `archived` is represented as `_archived`.

This is a physical/working-practice convention rather than a redefinition of Documentation Methodology lifecycle semantics.

## 4. Binder handling

Generated project Binders are versioned so the loaded project-context version is visible at a glance.

Operating convention:

- keep the **current generated Binder in the project's active/master folder** rather than a separate generated folder;
- move replaced Binder versions to `_superseded`;
- Binders remain generated, read-only consumption artefacts; and
- authoritative individual source masters remain the source of truth.

For Capabilities-family Binder naming, the retained convention was to use the `Capabilities_Binder_...` prefix and current case conventions.

## 5. WIP naming and ownership

Use **one current WIP series per top-level topic**, named from the top-level-topic prefix, for example:

```text
Build_WIP_vN.md
Capabilities_WIP_vN.md
```

Do not normally create independent subtopic/thread WIP filename series such as `Capabilities_Messaging_WIP_vN.md`.

Where several active threads coexist, represent their identity and continuation state **inside the top-level-topic WIP**. WIP remains compact volatile continuation state; substantial independently useful exploration may instead belong in Working material under the normal methodology.

## 6. Direct cross-topic editing versus Project Handoff

A later AIDE working convention superseded the earlier tendency to create a Project Handoff for every cross-topic consequence.

When a confirmed change affects another AIDE topic and the **current authoritative Binder/source context for that topic is available and sufficient**, apply the required change directly to that topic's authoritative source masters and include it in the same coherent change package/pass.

Use a **Project Handoff** when:

- the target topic cannot safely be edited from the available authoritative context;
- authority/context is genuinely missing; or
- a real transfer boundary exists and the destination owner must reconcile/decide the consequence.

Topic ownership determines the authoritative baseline and destination, not the physical chat/project in which the work happened.

## 7. Confirmed-state preservation rule

A durable operating principle used throughout AIDE work:

- if material information, reasoning or confirmed work is at genuine risk of being lost from volatile conversation/context, persist it before moving on;
- if the correct durable owner is unclear, preserve the material in the appropriate live/decision mechanism rather than letting it disappear;
- confirmed design-shaping reasoning should not be left only in chat when loss would materially impair future understanding.

This operates alongside the normal preference to avoid unnecessary version/output churn.

## 8. Delegation / decision threshold

The retained working preference is:

- resolve routine, low-risk, implementation-level matters autonomously when they remain within established authority;
- explicitly confirm design-shaping, high-impact or ownership-changing decisions with the user;
- do not turn ordinary execution detail into unnecessary approval ceremony.

This is consistent with the Build boundary that execution may resolve ordinary implementation detail but must return design-level ambiguity rather than silently taking design authority.

## 9. Review presentation preference

For substantial AIDE review/design work, the preferred human-facing review shape is:

1. a brief statement of purpose / requirements / current model;
2. a short summary of the review approach; then
3. findings, outcomes and required actions.

Keep machine-oriented metadata compact in otherwise human-readable documents.

## 10. Build-specific retained context

The following Build positions were repeatedly reinforced in project context. They should already be represented in the transferred current Build sources, so treat this section as continuity context rather than separate authority:

- Build is objective-driven execution, not synonymous with coding or compilation.
- Project Design/owning design authority determines committed meaning; Build executes a bounded WorkPackage/equivalent contract.
- Build may resolve ordinary implementation detail within authority but does not silently alter objective, major scope, acceptance, architecture/policy or reserved decisions.
- WorkRegister mapping is traceability/reconciliation input, not a substitute for a self-contained WorkPackage.
- Build returns evidence; the owning/directing process reconciles and closes the source WorkRegister obligation.
- Derived/platform representations are built from current authoritative semantic sources, not patched forward from an older Bundle/package as though that derived artefact were authoritative.
- Build output and Deployment state are distinct.
- Deployment-facing Build output exposes provenance, concrete output/package identity/integrity and composition posture so Deployment does not infer semantic authority from payload shape.
- `MemberContribution` may be mechanically assembled downstream without semantic reconstruction; `AssembledConsumptionArtefact` is atomic at its Build-owned internal semantic/member-composition boundary.
- A producer-side **Build Target** is distinct from an AI Deployment runtime/install Target.
- Domain/specialised producers own specialised Build logic; generic Build owns the reusable WorkPackage/execution/validation/provenance framework.
- Post-Build actions are explicit owner-defined Tool actions after successful validation; post-Build failure does not erase a successful validated Build result.

## 11. Project consolidation note

At the time of this transfer, the former AIDE Build project was being consolidated into the broader **AIDE** project. The working expectation is that future AIDE work can reconcile multiple top-level topics in one sufficiently sourced working context rather than requiring separate project chats solely to preserve topic ownership boundaries.

The transferred current source files/binders remain authoritative for the actual Build release state. This document should not be used to infer a newer or older Build version than those files establish.

## 12. What is deliberately not transferred here

This document intentionally excludes:

- personal/user information unrelated to AIDE;
- detailed content already represented in transferred Build masters/binders;
- chat transcripts or reasoning that has already been moved to the destination project;
- superseded architectural proposals where a current authoritative source now exists; and
- speculative future mechanisms that were never confirmed.

## Recommended destination action

Add this file to the destination project's temporary transfer/knowledge material and let the destination AIDE project reconcile any still-useful conventions into its own project knowledge.

Once reconciled, this transfer artefact does not need to become an authoritative AIDE corpus master.
