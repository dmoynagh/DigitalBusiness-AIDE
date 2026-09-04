# AIDE Update — Tool

> **Identity:** `AIDE_UpdateTool@v1`
> **Common name:** Update
> **Version 1** (2026-09-02). Introduces aggregate Required-Migration and Update orchestration over authorised AIDE targets.

---

## Contents

- **Target and authority** — supported aggregate selectors and authoritative-corpus boundary.
- **Actions** — Resolve, Check Required, Apply Required, Update and Status.
- **Execution integrity** — ordering, partial completion, idempotency and reporting.

## Summary

Use this Tool to apply migration/update behaviour across one or more Domains, current session
Domains, a Documentation Topic, explicit artefacts or a criteria-selected set. The Tool resolves
and reports the aggregate selection, but delegates each artefact's transition work and checkpoint
advancement to `AIDE_MigrationTool`.

Apply Required selects only artefacts with outstanding applicable Required work. Update is a
qualifying update for every selected authoritative artefact and reconciles its applicable Required
and OnUpdate work. Consuming/external-owner artefacts remain report-only unless separately selected
with authority.

## Logical actions

```yaml
Tool:
  Identity: AIDE_UpdateTool@v1
  CommonName: Update
  PrimaryInvocation: update
  LogicalActions: [Resolve, CheckRequired, ApplyRequired, Update, Status]
```

Run on explicit user/work-owner request or authorised governing Standard/Tool invocation.
`SessionDomains` is a target selector, not an automatic startup sweep. Platform automation requires
its own authority and does not change `AIDE_Migration` trigger semantics.

## Target

Accept exactly one:

```yaml
Target:
  Kind: Domain | Domains | SessionDomains | DocumentationTopic | Artefacts | Criteria
  Value: <identity/list/query where required>
```

Resolve membership and current authoritative artefacts through the applicable Domain,
Documentation Topic/Index and Working Context contracts. Multiple Domains remain separate;
selection does not create inheritance or merge semantics.

Criteria may use owner-supplied type, identity, dependency/checkpoint, Tags/Scope,
migration-state/posture and current/authoritative facts inside an explicitly bounded corpus.

## Authority

Mutate only artefacts that are both authoritative within the resolved target and within current
work authority. Report and skip consuming copies, external-owner sources, dependency-reachable
artefacts outside the target, unresolved authority and excluded candidates. Do not expand to
dependency closure or infer authority from filesystem reachability.

## Resolve

Read-only: return the deterministic candidate classification and selected authoritative corpus,
including every exclusion or ambiguity.

## Check Required

Read-only: invoke per-artefact Migration Check and report outstanding applicable Required work.
Behind-current or OnUpdate-only state does not by itself select an artefact for required action.

## Apply Required

Invoke per-artefact Apply only where Required work is outstanding. Do not sweep OnUpdate-only
artefacts. If Required work saves an artefact, allow normal per-artefact reconciliation through
pending applicable OnUpdate/None versions.

## Update

Treat the explicit request as a qualifying update for every selected authoritative artefact and
invoke per-artefact Update. Reconcile applicable Required and OnUpdate work through current where
possible. Do not invent substantive content merely to advance metadata; save only truthful proven
state.

## Status

Return current aggregate selection/progress, prior failure/defer state where available and next
actions without mutation.

## Ordering and integrity

Use explicit target order, otherwise authoritative corpus order or stable identity order, and
report it. This is operational order only. Each artefact retains `AIDE_Migration` dependency,
version and item order.

Resolve/CheckRequired/Status are read-only. ApplyRequired/Update are resumable and must not duplicate
proven work. Detect concurrent artefact changes and never overwrite newer authority.

## Partial completion

Preserve successful artefact updates/checkpoints when another target fails or defers. Continue with
independent targets where safe. Return `Partial`/`Failed` with every outstanding target; never claim
aggregate completion from partial per-artefact success.

## Reporting

Report target/action, resolved boundaries/authority, selected artefacts, exclusions and unresolved
candidates, per-artefact result/change/checkpoints, skipped/current/NotApplicable outcomes,
blockers/failures/deferrals and aggregate status/next action.

## Ownership boundary

This Tool owns only aggregate target resolution, selection, orchestration and reporting.
`AIDE_Migration`/`AIDE_MigrationTool` own each artefact's transition discovery, ordering, success,
failure/defer state, durable progress and dependency-checkpoint advancement.

Use genuine declared dependencies. Governed documents use `AIDE_DocumentationMethodology`; do not
create a synthetic universal `AIDE_Doc` dependency solely as an update/migration hook.

```yaml
MigrationSummary:
  CurrentVersion: v1
  LatestRequiredVersion: none
  LatestOnUpdateVersion: none

Transition:
  Version: v1
  Posture: None
```

---
Dependencies: !AIDE_DocumentationMethodology@v28, AIDE_Migration@v3, AIDE_MigrationTool@v3, AIDE_Dependencies@v3, AIDE_Scope@v2
References: Capabilities_Update_Tool_Design_v1, AIDE_Domain, AIDE_Index@v2, AIDE_Tags@v2
