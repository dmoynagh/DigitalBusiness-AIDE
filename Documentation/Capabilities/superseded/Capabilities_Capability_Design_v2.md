
# Capabilities Capability Model — Design

> **Version 2** (2026-09-02). Adds reusable Build Target Profile/Definition selection while preserving semantic release boundaries.

## Model

- Capability — coherent functional component/area.
- Capability Definition — exactly one current capability-level contract/control document.
- Capability Element — typed constituent; initial types Standard and Tool.
- Element Release — confirmed semantic Element outcome.
- Capability Release — confirmed Definition/composition of Element releases.
- Element Production — mutable input/source and LastEvaluated state.
- Release History — immutable released-state/composition records.
- Current Migration — mutable preparation for the next Element release.
- Build Target Definition — producer-side contract for one named deployment-facing Build output.
- Build Target Profile — reusable grouping of compatible Build Target Definitions.

Documents are hosts. Capability Definition is a permitted compact host for Capability-level Purpose,
Requirements, Dependencies, Release History, Element Production, Platform Definition, Build
Platforms, Build Target Profile selection/producer overrides and post-Build intent. Profile-owned
explicit membership or an authorised Build request may also establish selection; exactly one
effective target set must resolve before Build. One authoritative section instance exists per scope.

---
Dependencies: !AIDE_DocumentationMethodology@v27, AIDE_Migration@v2, AIDE_Dependencies@v3
References: Capabilities_Design_v14, Capabilities_BuildTargetProfile_Design_v1
