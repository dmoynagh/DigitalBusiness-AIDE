# Capabilities Update Tool — Design

> **Version 1** (2026-09-02). Defines aggregate Required-Migration and Update orchestration across authorised AIDE targets.

---

## Contents

- **Purpose and identity** — aggregate orchestration boundary and logical actions. §1–§2
- **Targets and selection** — supported selectors, authority and authoritative-corpus rules. §3–§5
- **Operations** — Resolve, Check Required, Apply Required, Update and Status. §6–§10
- **Execution integrity** — ordering, idempotency, failures and reporting. §11–§14
- **Ownership boundaries** — genuine dependencies and external capability seams. §15

## Summary

The Update Tool applies AIDE migration/update behaviour to an explicitly selected collection rather
than requiring each artefact to be named and invoked manually. It can resolve one or several
Domains, the Domains active in the current session, a Documentation Topic, explicit artefacts or a
criteria-selected set.

The Tool owns aggregate target resolution, selection, orchestration and reporting. It mutates only
artefacts authoritative within the selected target and current work authority; consuming or
external-owner artefacts are reported rather than rewritten unless independently selected with
authority. It delegates every artefact's transition evaluation, application, failure state and
dependency-checkpoint advancement to `AIDE_Migration`/`AIDE_MigrationTool`.

Required Migration and Update are deliberately different aggregate operations. Required Migration
selects only artefacts with outstanding applicable Required work; OnUpdate-only artefacts are not
swept. Update is an explicit qualifying update for every selected authoritative artefact and
reconciles its applicable Required and OnUpdate work through current where possible.

## §1 — Purpose and boundary

Repeated per-artefact Migration is insufficient when an operator needs to bring a coherent
authoritative corpus forward. This Tool provides the reusable aggregate action while preserving the
existing transition owner and checkpoint truth.

It does not define Domain membership, Documentation Topic structure, dependency/version facts,
transition semantics, applicability language, artefact authority or platform implementation.

## §2 — Identity and logical actions

```yaml
Tool:
  Identity: AIDE_UpdateTool@v1
  CommonName: Update
  PrimaryInvocation: update
  LogicalActions:
    - Resolve
    - CheckRequired
    - ApplyRequired
    - Update
    - Status
```

Platform builds may expose conversational intents, commands, skills, UI actions or automation while
preserving these semantics.

### Trigger

Run on explicit user/work-owner request or invocation by an authorised governing Standard/Tool.
Selecting `SessionDomains` does not create an automatic session-start migration sweep; it only
defines the target of an invoked aggregate operation. Any environment-specific scheduled/automatic
invocation must carry its own authority and must not change Migration's affected-use default.

## §3 — Target forms

The caller supplies exactly one aggregate target expression:

```yaml
Target:
  Kind: Domain | Domains | SessionDomains | DocumentationTopic | Artefacts | Criteria
  Value: <identity/list/query where required>
```

- `Domain` — one resolved AIDE Domain.
- `Domains` — an explicit ordered set of resolved AIDE Domains.
- `SessionDomains` — the Domains participating in the current Working Context/session.
- `DocumentationTopic` — the current authoritative corpus registered for one Documentation Topic.
- `Artefacts` — an explicit ordered set of artefact identities/locators.
- `Criteria` — a selection query inside an explicitly bounded authorised search corpus.

Several selected Domains remain separate Domains. Selection does not create Domain inheritance,
merging or a new parent Domain.

## §4 — Criteria and discovery facts

Criteria may consume owner-supplied facts such as:

- artefact/document type, identity or location;
- declared dependency or checkpoint relation;
- migration posture/state;
- Tags and Scope facts; and
- authoritative/current status within the bounded corpus.

Use the strongest available authoritative Index/Domain/Topic registers and direct corpus discovery.
Do not infer authority or membership merely because a file is reachable or mentions another item.
Unresolvable selection facts are reported; substantive ambiguity is not silently guessed.

## §5 — Authority and mutation corpus

Resolve the **selected authoritative corpus** before mutation.

An artefact is mutable only when:

1. it is inside the resolved target expression;
2. it is authoritative for that target rather than a consuming copy/reference;
3. the current work authority permits its modification; and
4. the requested operation applies to it.

External-owner artefacts and consuming copies encountered through dependencies, links or search are
report-only. They may be changed only through a separate explicit authoritative selection and
appropriate authority. Do not expand to dependency closure by default.

## §6 — Resolve

`Resolve` is read-only.

1. Resolve target identities/boundaries using their owning contracts.
2. Enumerate candidate artefacts.
3. classify authoritative, consuming/external, duplicate, excluded and unresolved candidates;
4. apply criteria where present; and
5. return the deterministic selected corpus and all exclusions/ambiguities.

## §7 — Check Required

`CheckRequired` is read-only.

For each selected authoritative artefact, invoke per-artefact Migration Check for relevant
dependencies and report whether applicable Required work is outstanding. Do not classify an
artefact as requiring action solely because OnUpdate work or a behind-current checkpoint exists.

## §8 — Apply Required

1. Resolve/freeze the selected authoritative corpus for this run.
2. Check each artefact under `AIDE_Migration`.
3. Invoke per-artefact Apply only for outstanding applicable Required work.
4. Preserve and report each proven saved result/checkpoint.
5. Do not select another artefact merely because it has OnUpdate-only work.

When Required work causes a save, that artefact follows normal Migration behaviour: pending
applicable OnUpdate/None versions may be traversed through current in the same save where possible.

## §9 — Update

`Update` is an explicitly authorised qualifying update for every artefact in the selected
authoritative corpus.

For each target, invoke per-artefact Migration Update so all applicable outstanding Required and
OnUpdate work is reconciled through current where possible. `None`/NotApplicable versions may be
included in the next proven saved checkpoint under normal Migration rules.

Do not invent a substantive content change merely to advance a checkpoint. The operation applies
declared transition work and saves only the truthful resulting artefact state.

## §10 — Status

Report current/resolved aggregate state without mutation, including prior partial/failure/defer
state where available and the next action needed.

## §11 — Aggregate ordering

Preserve explicit target order where supplied. Otherwise use the authoritative Index/corpus order
or a stable identity order and report it. This order is operational determinism, not semantic
cross-artefact dependency order.

Each artefact independently follows `AIDE_Migration` dependency/version/item ordering. Do not infer
a cross-artefact migration graph from mutual conformance checkpoints.

## §12 — Idempotency and concurrency

Resolve/CheckRequired/Status are read-only. Re-running ApplyRequired or Update against unchanged
successfully current artefacts produces no duplicate substantive effect.

Before saving an artefact, detect conflicting concurrent change under the per-artefact Tool. Do not
overwrite newer authority. Re-resolve only the affected artefact or stop the run where the target
boundary itself has changed materially.

## §13 — Failure and partial completion

Aggregate execution is stepwise rather than globally transactional. Preserve successful
per-artefact updates/checkpoints. For Failed, Deferred, UnsupportedBaseline, exact-version block,
authority failure or unresolved selection:

- preserve the exact per-artefact result/state;
- continue with independent targets where safe and authorised;
- do not mark the aggregate operation complete; and
- return overall `Partial` or `Failed` truthfully with the outstanding set.

Resume re-resolves current facts and does not replay already-proven work.

## §14 — Reporting

Report at least:

- requested target expression and logical action;
- resolved Domains/Topic/boundary and authority basis;
- selected authoritative artefacts;
- consuming/external, excluded, duplicate and unresolved candidates;
- per-artefact Check/Apply/Update result, changed state and resulting checkpoints;
- skipped/current/NotApplicable outcomes;
- blockers, failures, deferrals and partial completion; and
- aggregate status plus next action.

Narration may be compact, but the persisted/returned operation result must remain sufficient to
reconcile every selected target.

## §15 — Ownership and dependency boundaries

- `AIDE_Domain` owns Domain resolution/membership.
- Documentation Methodology/Index owns Documentation Topic corpus navigation.
- `AIDE_Tags`/`AIDE_Scope` own classification/applicability facts used by criteria.
- `AIDE_Dependencies` owns dependency identity/version/checkpoint facts.
- `AIDE_Migration`/`AIDE_MigrationTool` own all per-artefact transition and checkpoint semantics.
- Working Context supplies current session Domains and work authority.
- Platform Build owns concrete commands/skills/UI/automation.

Governed documents participate through their genuine `AIDE_DocumentationMethodology` dependency.
Do not introduce or require a synthetic universal `AIDE_Doc` dependency solely to make aggregate
update selection possible.

---
Dependencies: !AIDE_DocumentationMethodology@v28, AIDE_Migration@v3, AIDE_MigrationTool@v3, AIDE_Dependencies@v3, AIDE_Scope@v2
References: Capabilities_Migration_Design_v3, AIDE_Domain, AIDE_Index@v2, AIDE_Tags@v2
