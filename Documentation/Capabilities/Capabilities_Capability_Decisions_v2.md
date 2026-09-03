# Capabilities Capability Model — Decisions

> **Version 2** (2026-09-03). Records exact Element Production checkpoints and the post-Build workflow boundary.

## D1 — Definition is mandatory and singular

One current Definition supplies capability-level control without duplicating detailed Elements.

## D2 — Semantic releases are not document/package/deployment versions

Each identity answers a separate question and changes only under its own rule.

## D3 — Production checkpoints are mutable; release provenance is immutable

An input change makes an Element potentially stale. Reassessment may clear it without a release;
historic release input snapshots are not rewritten.

## D4 — Existing Dependencies and Migration are reused

Do not create Capability-specific replacements for shared dependency or transition semantics.

## D5 — Evaluated-input checkpoints are exact and comparable

Record stable input identity plus version/revision or digest for every applicable production input,
with evaluation date/status. Advancing this mutable checkpoint after an unchanged reassessment does
not create a semantic Element or Capability release.

## D6 — Post-Build action is workflow state, not package content

Resolve the requested post-Build action into the Build request/WorkPackage and report its actual
result in Outcome. Do not treat the request as Capability Definition semantics or freeze it into the
immutable PackageId payload.

---
Dependencies: !AIDE_DocumentationMethodology@v27
References: Capabilities_Capability_Design_v3, Capabilities_Decisions_v21
