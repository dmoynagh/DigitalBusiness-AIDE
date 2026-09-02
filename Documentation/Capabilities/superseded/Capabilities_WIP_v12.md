# Capabilities — WIP

> **Version 12** (2026-09-01). Records Review C Round 1 response and Lead disposition. Review C
> remains open at High pending coordinated Capabilities remediation and focused R2 verification.

## Current position

Programme:

`AIDE Architecture — Peer Review Programme`

WorkRegister:

`WR17 — Peer-review major Capabilities architecture slices`

Completed:

- `Review A — Core substrate` — Complete at High.
- `Review B — Documentation/work-state model` — Complete at High.

Current slice:

`Review C — Capabilities`

Current lifecycle state:

`R1 disposition complete — remediation pending`

## Active thread — Review C — Capabilities

Review identity:

`AIDE-Architecture-Review-C-Capabilities`

Messaging:

```text
R1 request:
  aide-architecture-review-c-capabilities/gpt/001 @ GPT_v1

R1 response:
  aide-architecture-review-c-capabilities/claude/001 @ Claude_v1

Lead disposition:
  aide-architecture-review-c-capabilities/gpt/002 @ GPT_v1
```

R1 posture:

```text
Type: Robust
Level: High
Mode: Full
Reviewer: Claude
Actual reviewer model: Claude Opus 5
Assessment: Sound with targeted changes
```

### R1 Lead disposition summary

All eleven findings are accepted, with Lead refinements where noted.

- **RC-R1-F1 — capability-reference semantics:** Accept with refinement.
  - `Dependencies: X@vN` remains a saved/proven conformance checkpoint.
  - `References:` carries no currency/conformance obligation.
  - current executable capability references are operational instructions, not checkpoints.
  - executable references should normally be versionless.
  - a specific version is valid where the instruction deliberately depends on that release/contract;
    production validates that the specificity is intentional and correct rather than mechanically
    forcing the newest version.

- **RC-R1-F2 — checkpoints are non-ordering:** Accept.
  Mutual conformance checkpoints do not create dependency/execution cycles. Declaration-order
  precedence applies only where the governing operation actually needs processing order.

- **RC-R1-F3 — legacy DocMeth footer form:** Accept with confirmed migration fact.
  Documentation Methodology v18 is `OnUpdate`. Do not sweep untouched artefacts. Any artefact
  substantively changed by this remediation must perform the v18 footer/container migration in that
  same qualifying save.

- **RC-R1-F4 — Review Profiles executable v1 references:** Accept.
  Make the two current executable Review references versionless and issue the resulting current
  Review Profiles release with transition posture `None`.

- **RC-R1-F5 — exact-version constraint treatment:** Accept with refinement.
  `X@!vN` is a hard present constraint. If exact vN is unavailable, the dependency is unsatisfied
  and affected use that requires it is blocked. It is not a conformance checkpoint or ordinary
  migration gap. Changing/removing the pin is an explicit dependent-artefact change that must be
  validated and saved. Do not add another generic pin-policy mechanism.

- **RC-R1-F6 — canonical Tool production contract:** Accept.
  Publish a canonical Tools Production Standard from the existing Tools-owned contract and have
  Build Capability consume it instead of duplicating the Tool-production contract in its body.

- **RC-R1-F7 — tag freshness:** Accept with refinement.
  Tags already owns generic freshness semantics; there is no need for another orchestration owner.
  Strengthen the rule so source-changing operations rebuild applicable generated tags before
  publishing/relying on them, or treat freshness as uncertain and rebuild before tag-dependent use.
  Platform/build realisation remains a Review D carry.

- **RC-R1-F8 — Review versus Messaging correlation:** Accept.
  Review/Round correlation is authoritative for Review semantics; Messaging correlation is
  transport-level. A disagreement between them is a quarantine condition.

- **RC-R1-F9 — STATE limitation:** Accept as clarification.
  State explicitly that STATE's evidential value depends on retained evidence; a genuinely stateless
  context provides no receipt evidence. Use explicit Ack where receipt assurance matters. Do not
  reinstate a register.

- **RC-R1-F10 — dependency precedence versus Bootstrap:** Accept.
  Clarify that dependency declaration order does not sequence independent artefacts or peer
  Bootstrap Contributions.

- **RC-R1-F11 — behind-current checkpoints are normal:** Accept.
  Record that saved consumer checkpoints routinely lag current releases by design and this is not
  decay or an automatic update trigger.

### Carried Review D item

Review D must test concrete platform/build realisation of generated-tag freshness and related
production/build sequencing. Review C defines only the semantic requirement.

### Review E carry

The possible `OpenItems + WorkRegister` merge remains deferred to Review E. Review C produced no
evidence requiring earlier reconsideration.

## Required Review C continuation

Apply the accepted R1 remediation as one coherent Capabilities pass across the affected parent,
Dependencies/Migration, Tools/Build Capability, Tags/Scope, Review/Profiles and Messaging sources and
canonical outcomes.

Regenerate affected Capabilities Binders after the authoritative masters are updated.

Because Review C is High and the remediation includes substantive ownership/public-contract changes,
perform a focused:

```text
R2: Inspect / High / Full — Claude Opus 5
```

R2 should verify the remediated architecture and all R1 dispositions. Another Robust round is not
required unless remediation introduces a materially different architecture.

Do not begin Review D until Review C completes or explicitly escalates.

---
Dependencies: !AIDE_DocumentationMethodology@v26, AIDE_Review@v2, AIDE_Messaging@v1
References: Capabilities_WorkRegister_v16, Capabilities_OpenItems_v15, Capabilities_Architecture_Review_2026-08-31-1_CoreSubstrate_v2, Capabilities_Architecture_Review_2026-09-01-2_DocumentationWorkState_v1
