# Capabilities — WIP

> **Version 5** (2026-09-01). Review A continuation checkpoint after Claude R2 completed and Lead
> dispositions narrowed final remediation to two Core determinism corrections.

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
R1 Lead dispositions                 Complete — gpt/002 @ GPT_v2
R1 authoritative remediation         Applied
R2 preflight                         PASS
R2 request                            gpt/003 @ GPT_v1
R2 reviewer response                 Complete — claude/002 @ Claude_v1 — Claude Opus 5
R2 Lead dispositions                 Complete
R2 disposition reply                 Prepared — gpt/004 @ GPT_v1
Final Core correction                Pending
Review A                              Continuing / High
Round 3                               Not planned
```

## R2 outcome

Claude verified the R1 remediation at High:

- RA-R1-F1 through F12 — Resolved
- RA-R1-F13 — Superseded / Not Applicable under Lead Decline
- RA-R1-F14 — Resolved

Claude raised three R2 Findings.

### RA-R2-F1 — Change

Choose inclusive Propagation Stop semantics:

- the marked boundary itself leaves the enclosing effective Domain;
- all content within/below it also leaves that Domain;
- the marked boundary + subtree resolve independently as one stopped region;
- a parent Index may host the Stop property but is not itself the stopped boundary; and
- no parent/child Domain relationship, inheritance, merge, settings propagation or precedence is
  introduced.

### RA-R2-F2 — Change

Implicit Domain settings-host authority must be deterministic:

- an Index is eligible only when it governs an approved semantic recognised root participating in
  the implicit Domain;
- parent/repository registration alone grants no settings-host authority;
- one unambiguous host is required;
- no unique eligible host + settings needed → use explicit `AIDE_Domain.yaml`;
- native Solution/Project-only implicit Domain does not acquire an arbitrary Index host; and
- competing implicit host state fails visibly rather than using merge/precedence/discovery order.

### RA-R2-F3 — Decline

Claude described D6 as unrefined, but current Domain Decision D34 explicitly refines D6 (along with
D5/D8/D9/D10/D15/D19/D22) where historical wording/examples used Index as literal/potentially
Domain-establishing.

D34 supplies the current rule that generic Index is not in the approved Domain recognition set.

Therefore:

- D6 is preserved historical reasoning;
- D34 is the explicit current refinement;
- do not rewrite D6 merely to make history read as if the later model had always applied.

## Final Core correction package

Prepared:

`Core_ReviewA_R2_ChangeDelivery_Instructions_2026-09-01.md`

Expected corrected review-completion input:

`Core_Binder_v3.md`

The smallest expected replacement set is:

- `Core_Index_v6`
- `Core_System_Design_v9`
- `Core_Domain_Design_v4`
- `Core_Domain_Decisions_v4`
- `AIDE_Domain_Standard_v4` / `AIDE_Domain@v4`
- `Core_Binder_v3`

Index and Bootstrap child contracts remain unchanged.

`AIDE_Domain@v4` transition posture: `None`.

## Review completion posture

No Review A Round 3 is planned.

Claude explicitly judged another full Round unlikely to add material value. The accepted R2 changes
are local determinism corrections inside the model already inspected at High.

After `Core_Binder_v3` is returned:

1. verify RA-R2-F1 inclusive Stop wording in Domain Design/Standard/System Design;
2. verify RA-R2-F2 unique implicit settings-host rule and failure handling;
3. verify D6 remains historical and D34 remains its explicit refinement;
4. verify the R1 Domain-authority constraint remains intact;
5. if clean, mark Review A Complete at High;
6. issue the final durable Review Result/update;
7. supersede/withdraw this active WIP as appropriate; and
8. proceed to Review B.

## Out-of-scope observation to carry forward

Claude noted that `AIDE_Index` and Documentation Methodology can cite/depend on each other if a
Documentation Methodology conformance checkpoint is treated the same as a functional dependency.

No Review A action.

Carry this observation into the later Capabilities/Dependencies review slice (Review C) to test
whether dependency resolution/cycle detection needs to distinguish documentation-conformance
checkpoint semantics from functional dependency semantics.

Do not create a separate work item yet; WR17 already owns the peer architecture Review programme.

## Messaging

Effective outgoing R2 disposition:

`aide-architecture-review-a-core-substrate/gpt/004 @ GPT_v1`

Replying to:

`aide-architecture-review-a-core-substrate/claude/002 @ Claude_v1`

`Expects: None`.

## Resume point

Resume from:

`Core_Binder_v3.md`

No Claude response is required before applying the Core correction.

---
Dependencies: !AIDE_DocumentationMethodology@v23, AIDE_Review@v2, AIDE_Messaging@v1
References: Capabilities_Architecture_Review_2026-08-31-1_CoreSubstrate_v1, Capabilities_WorkRegister_v14
