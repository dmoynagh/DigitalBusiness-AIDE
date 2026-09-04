# AIDE Standards Usage — Standard

> **Identity:** `AIDE_StandardsUsage@v2`
> **Common name:** Standards Usage
> **Version 2** (2026-09-01). Carries current Machine Scope tag-freshness and expected dependency-checkpoint lag into the runtime Standards consumer contract.
>
> **Default weight:** Requirement

---

## Purpose

Operate under applicable AI-facing Standards consistently while preserving declared weights,
Scope, dependencies, migration requirements, human authority, and visible handling of genuine
conflict or deviation.

## Applicability

Apply whenever an AI session relies on one or more governed Standards to perform, assess, or advise
work.

```yaml
Scope:
  Context: >
    Apply when governed Standards are available and relevant to the current work or action.
```

## Establish the applicable set

1. Discover the Standards available to the current execution context.
2. Resolve their formal identities and dependency state where relevant.
3. Before affected use, honour any applicable Required Migration under `AIDE_Migration`.
4. Before relying on Machine Scope, satisfy the current-tag freshness precondition owned by `AIDE_Scope`/`AIDE_Tags`; then evaluate `AIDE_Scope`. An item that is not applicable contributes no rule to the current work.
5. Use only the material needed for the current work while preserving each retrieved unit's
   effective weight and necessary context.

Do not treat installation/presence alone as applicability.

## Interpret weights

- `Requirement` — satisfy it for the stated outcome/consumer; if it cannot be satisfied, surface
  the consequence and do not silently claim conformance.
- `Expectation` — follow by default; if departing, make the departure visible.
- `Guidance` — follow where it adds value; departure is allowed and the resulting consequences are
  owned.
- `Context` — use as information/reasoning; it creates no obligation by itself.

A lower-weight statement does not silently cancel a higher-weight statement on the same point.

## Combine Standards

Compatible applicable Standards stack. Do not choose one merely because several apply.

When two applicable statements genuinely oppose each other on the same point:

1. higher weight governs;
2. equal-weight conflict is surfaced/escalated rather than silently resolved; and
3. the conflict record identifies the competing Standards/statements and the work affected.

Do not manufacture conflict from different concerns that can both be satisfied.

## Human instruction and deviation

Direct human/work-owner instruction may override a Standard within that person's authority.
When it displaces a Requirement or Expectation:

- state the Standard position and material consequence;
- make the departure visible in the appropriate work record where durability matters; and
- continue under the authorised instruction unless another non-overridable external constraint
  applies.

Guidance may be departed from without approval, but material consequences remain the responsibility
of the work owner/Lead.

## Missing, stale, or unresolved Standard state

- Missing required dependency → surface under `AIDE_Dependencies` and follow the governing
  operation's blocking posture.
- A dependency conformance checkpoint behind the available release is expected steady state and is not by itself stale, missing, or an update trigger; applicable Required Migration before affected use remains the gate.
- Required Migration outstanding → reconcile before affected use.
- Unsupported migration baseline or ambiguous transition → stop affected use and escalate.
- Unresolvable Standard identity/version → do not guess which contract governs.
- Genuine equal-weight conflict → escalate rather than select silently.

## Runtime economy

Prefer cheap applicability/version checks before loading detailed Standard material. Use
`MigrationSummary`, Scope machine filters, Tags, and platform discovery metadata where available,
then load only the detailed content needed for the work.

Performance optimisation must not change Standard meaning or hide an applicable Requirement.

## Reporting

Normal operation need not narrate every Standard consulted. Surface what materially affects the
work: blocking requirements, meaningful expectations/deviations, conflicts, migration state, or a
Standard-driven consequence the user/work owner needs to know.

```yaml
MigrationSummary:
  CurrentVersion: v2
  LatestRequiredVersion: none
  LatestOnUpdateVersion: none

Transition:
  Version: v1
  Posture: None

Transition:
  Version: v2
  Posture: None
```

---
Dependencies: !AIDE_DocumentationMethodology@v26, Capabilities_Standards_Design_v6, AIDE_Scope@v2, AIDE_Dependencies@v3, AIDE_Migration@v2
References: AIDE_StandardsProduction
