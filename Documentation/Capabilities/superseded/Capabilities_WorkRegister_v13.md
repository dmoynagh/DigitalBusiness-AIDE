# Capabilities — Work Register

> **Version 13** (2026-08-31). Converts the register to live-only v21 semantics and records the
> confirmed Messaging capability reconciliation as the current outstanding Capabilities work.
>
> Created: 2026-08-27 | Last modified: 2026-08-31

## WR16 — Reconcile and publish Messaging as an AIDE Capability

**Status:** Confirmed / queued — not yet delivered

**Source / committed change**

Messaging is confirmed as an AIDE Capability. Message semantics, AI-MESSAGE envelope/schema,
thread/message identity, receipt/reconciliation behaviour, messaging workflow/commands and
message-specific persisted-document semantics move to Messaging ownership. Documentation
Methodology retains only generic governed-file integration when a Message is persisted.

**Required delivery**

- Reconcile the existing Workflow Messaging Design/Specification/Migrations/Requirements and
  deployed Claude skill against the current AIDE architecture rather than redesigning from scratch.
- Preserve the behaviours that have worked well unless review demonstrates a better approach.
- Reconcile outstanding-message persistence against WIP/OpenItems and remove a dedicated
  obligations register if it no longer has an independently necessary role.
- Confirm the `=== STATE ===` receipt-integrity mechanism still works under the new persistence
  model before removing any state it relies on.
- Produce the canonical Messaging Design/Decisions and appropriate Standard/Tool outcomes under
  Capabilities.
- Define any genuinely required Bootstrap Contribution and platform implementations separately
  from the canonical Messaging semantics.
- Prepare the Messaging architecture for peer review with Claude as part of the wider AIDE review
  pass.

**Target outcomes**

Capabilities/Messaging authoritative masters and canonical Messaging Standard/Tool as determined
by the reconciled Design.

**WorkPackage mapping**

None yet. Create manageable WorkPackage(s) only after the Messaging Design/review establishes the
required build/platform work.

**Current result / remaining**

Foundation ownership is confirmed and `Capabilities_Messaging_WIP_v1` preserves the current
continuation context. Messaging design reconciliation, peer review and canonical production remain
outstanding.

---
Dependencies: !AIDE_DocumentationMethodology@v21
References: Capabilities_Messaging_WIP_v1, AIDE_Index@v1, AIDE_ProjectDesign@v2
