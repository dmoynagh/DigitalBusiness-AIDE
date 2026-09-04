
# Capabilities Capability Model — Decisions

> **Version 1** (2026-09-02). Records the foundational Capability model decisions.

## D1 — Definition is mandatory and singular

One current Definition supplies capability-level control without duplicating detailed Elements.

## D2 — Semantic releases are not document/package/deployment versions

Each identity answers a separate question and changes only under its own rule.

## D3 — Production checkpoints are mutable; release provenance is immutable

An input change makes an Element potentially stale. Reassessment may clear it without a release;
historic release input snapshots are not rewritten.

## D4 — Existing Dependencies and Migration are reused

Do not create Capability-specific replacements for shared dependency or transition semantics.

---
Dependencies: !AIDE_DocumentationMethodology@v27
References: Capabilities_Capability_Design_v1, Capabilities_Decisions_v17
