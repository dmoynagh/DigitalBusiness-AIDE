
# AIDE Update Capability Elements — Tool

> **Identity:** `AIDE_UpdateCapabilityElementsTool@v1`
> **Common name:** Update Capability Elements
> **Version 1** (2026-09-02). First design-side Element production/update Tool.

## Actions

`Evaluate | Update | Validate | Status`

## Procedure

1. Resolve the current Capability Definition, target Elements and documented Element Production inputs.
2. Compare each current input/version with its `LastEvaluated` checkpoint.
3. Reassess potentially stale Elements using the applicable production contract.
4. If meaning is unchanged, update only the evaluated checkpoint.
5. If meaning changes, update and validate the canonical Element, complete Current Migration and
   confirm the next Element release/history.
6. If current inputs conflict or are insufficient, return the smallest actionable defect; do not choose/invent.
7. Update the Capability release only if composition or substantive Capability-level Definition changed.

## Migration from Build Capability v2

Calls that used `AIDE_BuildCapabilityTool@v2` to produce canonical Standards/Tools migrate to this
Tool. Do not reinterpret an unreviewed v2 invocation as Build Capability v3.

---
Dependencies: !AIDE_DocumentationMethodology@v27, AIDE_Capability@v1, AIDE_StandardsProduction@v3, AIDE_ToolsProduction@v2
References: Capabilities_UpdateCapabilityElements_Tool_Design_v1, AIDE_BuildCapabilityTool@v2
