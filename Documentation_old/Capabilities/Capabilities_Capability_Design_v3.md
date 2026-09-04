# Capabilities Capability Model — Design

> **Version 3** (2026-09-03). Defines exact evaluated-input checkpoints and keeps post-Build workflow state outside Capability semantics.

## Model

- Capability — coherent functional component/area.
- Capability Definition — exactly one current capability-level contract/control document.
- Capability Element — typed constituent; initial types Standard and Tool.
- Element Release — confirmed semantic Element outcome.
- Capability Release — confirmed Definition/composition of Element releases.
- Element Production — mutable exact evaluated-input checkpoint state.
- Release History — immutable released-state/composition records.
- Current Migration — mutable preparation for the next Element release.
- Build Target Definition — producer-side contract for one named deployment-facing Build output.
- Build Target Profile — reusable grouping of compatible Build Target Definitions.

Documents are hosts. Capability Definition is a permitted compact host for Capability-level Purpose,
Requirements, Dependencies, Release History, Element Production, Platform Definition, Build
Platforms and Build Target Profile selection/producer overrides. Profile-owned
explicit membership or an authorised Build request may also establish selection; exactly one
effective target set must resolve before Build. One authoritative section instance exists per scope.

Each Element Production checkpoint records the exact applicable inputs last evaluated using stable
input identity plus version/revision or digest, together with evaluation date/status. The checkpoint
may advance without a semantic release when reassessment finds unchanged meaning. A date plus an
unresolved phrase such as “current sources” is insufficient because it cannot be compared with the
next input state.

Post-Build action/request remains mutable workflow authority. It is resolved into the Capability
Build WorkPackage, executed after validation and reported in Outcome; it is not Capability
Definition semantics or immutable package content.

---
Dependencies: !AIDE_DocumentationMethodology@v27, AIDE_Migration@v2, AIDE_Dependencies@v3
References: Capabilities_Design_v15, Capabilities_BuildTargetProfile_Design_v2
