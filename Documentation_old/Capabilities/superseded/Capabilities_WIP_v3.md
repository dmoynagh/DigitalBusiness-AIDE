# Capabilities — WIP

> **Version 3** (2026-09-01). Review A continuation checkpoint after R2 preflight found one
> Documentation Methodology/Core Index version-seam correction still required.

## Current position

Programme:

`AIDE Architecture — Peer Review Programme`

Current slice:

`Review A — Core substrate`

Review:

`AIDE-Architecture-Review-A-Core-Substrate`

State:

```text
R1 reviewer response                 Complete — Claude Opus 5
R1 Lead dispositions                 Complete
R1 remediation definition           Complete
R1 disposition relay                 Complete
Messaging revision correction        Sent — gpt/002 @ GPT_v2
Core authoritative remediation       Applied — Core_Binder_v2 received
DocMeth authoritative remediation    Applied — Binder v3 received
R2 preflight                         One narrow seam defect found
Review A                             Continuing / High
R2                                  Not sent yet
```

## R2 preflight finding

Core now publishes/uses:

`AIDE_Index@v2`

The revised Documentation Methodology v22 material correctly implements the
`DocumentationTopic` semantic correction, but several current/normative statements and dependency
checkpoints still consume:

`AIDE_Index@v1`

This is an incomplete application of the Review A Core/Documentation Methodology seam and should be
corrected before R2 rather than intentionally sent to the Reviewer as known-broken state.

Prepared correction package:

`DocumentationMethodology_ReviewA_R2_PreflightCorrection_2026-09-01.md`

Expected corrected Review input:

`DocumentationMethodology_Binder_v4.md`

Do not reissue Core solely for DocMeth v23: Core's saved/proven DocMeth v22 dependency remains a
truthful checkpoint where v23 is a None transition.

## Protected architectural constraint

```text
Item Type owner
  → identity, Identify, Provides

AIDE_Index@v2 / ItemTypeRegistry
  → Domain-neutral recognition only

AIDE_Domain@v3
  → approved Domain recognition set
  → exclusive Domain-capability authority
```

External Item Type owners cannot promote themselves into Domain roots.

## Effective R1 Lead disposition identity

Use for R2:

`aide-architecture-review-a-core-substrate/gpt/002 @ GPT_v2`

## Remaining work

1. Apply the narrow Documentation Methodology preflight correction.
2. Return `DocumentationMethodology_Binder_v4.md`.
3. Re-run the R2 preflight against:
   - `Core_Binder_v2.md`
   - `DocumentationMethodology_Binder_v4.md`
4. If clean, send Review A R2:
   - Type: Inspect
   - Level: High
   - Mode: Full
5. Correlate Reviewer response and disposition any R2 Findings.
6. Complete Review A only when High-level re-review is satisfactory.
7. Do not start Review B before Review A completion.

`WR17` remains open for the peer architecture Review programme.

---
Dependencies: !AIDE_DocumentationMethodology@v22, AIDE_Review@v2, AIDE_Messaging@v1
References: Capabilities_Architecture_Review_2026-08-31-1_CoreSubstrate_v1, Capabilities_WorkRegister_v14
