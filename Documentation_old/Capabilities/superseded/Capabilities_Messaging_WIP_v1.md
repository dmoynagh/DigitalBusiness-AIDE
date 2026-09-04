# Capabilities — Messaging — WIP

> **Version 1** (2026-08-31). Current continuation checkpoint for the next Messaging capability
> pass after Foundation consolidation.
>
> Status: WIP — non-authoritative current-work context.

## Current position

Messaging is confirmed as an **AIDE Capability**.

The existing AI-MESSAGE system is already useful in practice and should be **reconciled/reviewed,
not redesigned from scratch**. The current Workflow Messaging brief is the primary source for the
existing functionality: platform-agnostic envelope, message/thread identity, light/heavy tiers,
receipt integrity, commands, obligations handling and the deployed Claude skill.

Confirmed ownership direction:

```text
Messaging
  owns Message semantics
  owns envelope/schema/fields
  owns threading/identity/version rules
  owns receipt/reconciliation behaviour
  owns messaging commands/logical workflow
  owns message-specific persisted-document contract

Documentation Methodology
  owns only generic governed-file hosting/lifecycle/version/metadata behaviour
  when a Message is actually promoted to a file

Review
  consumes Messaging for cross-session/platform review transport
```

## Messaging state persistence direction

Do not create a permanent message archive/register by default.

Expected model:

```text
normal/light exchange
    → chat/conversation context

outstanding exchange in current active work
    → WIP if persistence is needed

obligation that must outlive current work/context
    → concise OpenItems entry

message whose body itself must remain retrievable
    → promote/persist Message (expected to be uncommon)
```

The existing `=== STATE ===` receipt-integrity mechanism must be reviewed carefully before removing
its historical obligations-register assumption. Preserve the successful behaviour unless WIP /
OpenItems can demonstrably provide equivalent state without extra machinery.

## Review questions for Messaging

- Is the current envelope still the smallest reliable format?
- Are `Thread`, `Message-ID`, `Version`, `In-Reply-To`, `Timestamp` and `Expects` still correctly
  separated?
- Does `=== STATE ===` remain the best low-friction receipt-integrity mechanism?
- Can outstanding-message state use WIP/OpenItems instead of a dedicated obligations register?
- Are Light/Heavy promotion rules still proportionate?
- Does Messaging need any specialised persisted Message fields beyond its own schema?
- Are source-marking and out-of-band rules worth retaining unchanged?
- Which parts become canonical Messaging Standard versus Messaging Tool/platform implementation?
- What Bootstrap Contribution, if any, is genuinely required for pasted-envelope recognition?

## Planned work sequence after Messaging

1. Reconcile existing Messaging Design/Specification/skill against the new AIDE ownership model.
2. Peer-review the major AIDE architecture slices with Claude, including Messaging.
3. Build lightweight platform-specific Bootstrap implementations.
4. Build the deployment system/targets: ChatGPT Bundle, Claude plugin/marketplace, Codex and
   separately proven OpenAI/Work routes.
5. Run a final cross-system integration review before broad deployment.

## Authoritative foundation now expected

Messaging should use the newly issued foundation contracts where applied:

- `AIDE_Index@v1`
- `AIDE_Domain@v2`
- `AIDE_DocumentationMethodology@v21`
- `AIDE_WorkingPractices@v1` (Standard document v4)
- `AIDE_ProjectDesign@v2`
- `AIDE_Build@v4`
- `AIDE_WorkPackage@v2`

## Live Capabilities state

- `Capabilities_WorkRegister_v13` — `WR16` is the confirmed outstanding Messaging delivery
  obligation.
- `Capabilities_OpenItems_v15` — live-only unresolved attention; the former shared-communication
  ownership question is no longer open because Messaging ownership is confirmed.

These live-state documents are intentionally separate from the normal stable Binder.

## Resume point

Start the next chat by loading the current Capabilities Binder/current masters,
`Capabilities_WorkRegister_v13`, `Capabilities_OpenItems_v15`, this WIP checkpoint,
and the existing **Workflow — Messaging (Brief)**. Reconcile the old Workflow ownership model into
Capabilities/Messaging before editing masters. Review first for preserved value; change only where
the new architecture or review demonstrates an improvement.

---
Dependencies: !AIDE_DocumentationMethodology@v21
References: Capabilities_WorkRegister_v13, Capabilities_OpenItems_v15, AIDE_Index@v1, AIDE_ProjectDesign@v2, AIDE_WorkPackage@v2
