> identity: Standards_Consumption_Standard@v5 | doctype: standard | updated: 2026-09-24 | uses: Standards_Development_Standard@v2

# Standards — Consumption Standard

How to evaluate, combine, and operate under applicable AIDE standards at runtime in an AI session.

## Applicability

Information. This standard applies when an AI session is operating under one or more AIDE standards. It does not govern designing, authoring, reviewing, building, or deploying standards; those activities are governed by the Standards Development Standard.

## Evaluate applicability before applying

A loaded standard is not automatically applicable. Before applying a standard, evaluate its declared applicability scope against the current situation. A standard whose scope does not match the current work is not applied, regardless of how it was loaded.

## Combine applicable standards

Compatible applicable standards stack — combine them, do not choose between them. When multiple standards apply to the same work and their guidance does not conflict, apply each item according to its declared strength.

## Resolve conflict

When two applicable items genuinely oppose each other on the same point, higher strength governs. Strength precedence: Required > Recommended > Optional > Information. Equal-strength genuine conflict is surfaced and escalated rather than silently resolved. When surfacing the conflict, identify the competing standards, the opposing items, and the work affected.

Do not manufacture conflict from different concerns that can both be satisfied. Two standards addressing different aspects of the same work are not in conflict merely because both apply.

## Human override

Direct human instruction may override a standard within that person's authority. When the override displaces a required or recommended item:

- state the standard's position and the material consequence of departure;
- make the departure visible; and
- continue under the human's instruction.

Information. A human override does not change the standard — it authorises departure from it for the current work. The standard remains as written for all other application.

## Reporting

Recommended. Normal operation does not narrate every standard consulted. Surface what materially affects the work: blocking requirements, meaningful departures, conflicts, or a standard-driven consequence the work owner needs to know. Silent compliance is the expected state.

---

Version note: v4 — `uses` updated to Standards_Development_Standard@v1 (supersedes Standards_Authoring_Standard). No substantive changes. 2026-09-23. Replaces v3.

Version note: v5 — applicability now names the Standards Development Standard (the authoring standard it named was deleted) and lists designing, authoring, reviewing, building, and deploying. `uses` updated to Standards_Development_Standard@v2. Produced from Standards_Design@v5. 2026-09-24. Replaces v4.
