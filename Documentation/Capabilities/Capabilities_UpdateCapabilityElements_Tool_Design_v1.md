
# Capabilities Update Capability Elements Tool — Design

> **Version 1** (2026-09-02). Succeeds the canonical-element production role formerly carried by Build Capability v2.

## Purpose

Evaluate documented production inputs and produce/refresh/validate canonical Elements without
inventing meaning or creating false releases.

## Result rule

`input changed → reassess Element → semantic change?`

- no: advance `LastEvaluated`; retain Element release;
- yes: produce/validate the Element, convert Current Migration and confirm the next Element release;
- unresolved conflict/gap: return blocked/incomplete.

Directly authored Elements without derivation need not invoke this Tool.

---
Dependencies: !AIDE_DocumentationMethodology@v27, AIDE_Capability@v1, AIDE_StandardsProduction@v3, AIDE_ToolsProduction@v2
References: Capabilities_Capability_Design_v1
