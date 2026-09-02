# Capabilities — WIP

> **Version 4** (2026-09-01). Review A continuation checkpoint after the corrected
> Documentation Methodology Binder passed R2 preflight and the Round 2 request was prepared.

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
Effective R1 disposition             gpt/002 @ GPT_v2
Core authoritative remediation       Applied — Core_Binder_v2
DocMeth R1 remediation               Applied
DocMeth R2 preflight correction      Applied — DocumentationMethodology_Binder_v4
Final R2 preflight                   PASS
R2 request                           Prepared — gpt/003 @ GPT_v1
Review A                             Continuing / High
```

## R2 authoritative inputs

- `Core_Binder_v2.md`
- `DocumentationMethodology_Binder_v4.md`

The final preflight confirmed that Documentation Methodology current/normative consumption now uses
`AIDE_Index@v2`.

The remaining `AIDE_Index@v1` occurrence in the v4 Binder is historical Decisions text recording
the original v1 adoption and is intentionally preserved as history.

## Protected architectural constraint

```text
Item Type owner
  → identity, Identify, Provides

AIDE_Index@v2 / optional ItemTypeRegistry
  → Domain-neutral recognition/provision optimisation

AIDE_Domain@v3
  → publishes the approved Domain recognition set
  → exclusively controls Domain eligibility / resolution
```

External Item Type owners cannot self-elevate into Domain containers or Domain-defining roots.

## R2 request

Prepared Messaging identity:

`aide-architecture-review-a-core-substrate/gpt/003 @ GPT_v1`

Review posture:

```text
Type: Inspect
Level: High
Mode: Full
```

R2 is a remediation verification round, not a repeat blank-sheet Robust review.

It asks Claude to:

- verify each RA-R1-F1 ... RA-R1-F14 disposition against the revised authoritative material;
- inspect cross-cutting coherence in the changed Review A scope;
- raise only material new/residual R2 Findings; and
- judge whether Review A now warrants completion at High.

## Remaining work

1. Relay `gpt/003 @ GPT_v1` to the same Claude Review thread.
2. Supply/attach:
   - `Core_Binder_v2.md`
   - `DocumentationMethodology_Binder_v4.md`
3. Return Claude's complete correlated R2 AI-MESSAGE unchanged to this Capabilities Review context.
4. Correlate the response and record actual Reviewer/model.
5. Disposition any RA-R2 Findings.
6. If High re-review is satisfactory:
   - complete Review A;
   - issue/update the durable Review record/result;
   - route any residual work correctly;
   - update/withdraw this WIP as appropriate; and
   - proceed to Review B.
7. If material remediation remains, keep Review A Continuing and run only the further scoped work
   justified by the R2 result.

Do not start Review B before Review A completes.

`WR17` remains open for the full peer architecture Review programme.

## Resume point

Resume from the Claude response to:

`aide-architecture-review-a-core-substrate/gpt/003 @ GPT_v1`

---
Dependencies: !AIDE_DocumentationMethodology@v23, AIDE_Review@v2, AIDE_Messaging@v1
References: Capabilities_Architecture_Review_2026-08-31-1_CoreSubstrate_v1, Capabilities_WorkRegister_v14
