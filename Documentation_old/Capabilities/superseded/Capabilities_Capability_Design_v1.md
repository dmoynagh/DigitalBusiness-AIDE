
# Capabilities Capability Model — Design

> **Version 1** (2026-09-02). Defines Capability, Definition, Element, production state and release semantics.

## Model

- Capability — coherent functional component/area.
- Capability Definition — exactly one current capability-level contract/control document.
- Capability Element — typed constituent; initial types Standard and Tool.
- Element Release — confirmed semantic Element outcome.
- Capability Release — confirmed Definition/composition of Element releases.
- Element Production — mutable input/source and LastEvaluated state.
- Release History — immutable released-state/composition records.
- Current Migration — mutable preparation for the next Element release.

Documents are hosts. Capability Definition is a permitted compact host for Capability-level Purpose,
Requirements, Dependencies, Release History, Element Production, Platform Definition, Build
Platforms and post-Build intent. One authoritative section instance exists per scope.

---
Dependencies: !AIDE_DocumentationMethodology@v27, AIDE_Migration@v2, AIDE_Dependencies@v3
References: Capabilities_Design_v12
