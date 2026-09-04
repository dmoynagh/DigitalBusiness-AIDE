# Capabilities — WIP

> **Version 1** (2026-08-31). Root Capabilities continuation checkpoint after Review A Round 1
> dispositions/remediation definition.

## Current position

Active programme:

`AIDE Architecture — Peer Review Programme`

Current slice:

`Review A — Core substrate`

Review identity:

`AIDE-Architecture-Review-A-Core-Substrate`

State:

```text
R1 reviewer response        Complete — Claude Opus 5
R1 Lead dispositions        Complete
R1 remediation definition  Complete
Review A                    Continuing / High
R2 re-review                Required after authoritative revisions
```

Do not start Review B yet.

## Protected architectural constraint

The Review A registry simplification must preserve Domain-exclusive authority.

```text
Item Type owner
  → defines what its type is, Identify, Provides

optional ItemTypeRegistry
  → domain-neutral recognition optimisation only

AIDE_Domain
  → publishes the approved Domain recognition set
  → alone decides which recognised semantic types/native structures may establish or participate
    in Domain resolution
```

An Item Type defined by another Standard cannot promote itself into a Domain container/root through
its own definition or registry metadata.

## R1 Lead disposition summary

Changes accepted for:

- explicit Domain-owned approved recognition set;
- removal of generic Index as a Domain root;
- honest native Solution/Project minimum recognition ownership;
- Propagation Stop semantics/traversal;
- removal of separate DomainRecognitionRegistry;
- optional/direct recognition fallback and derived-output provenance;
- Bootstrap Profile-gated Contributions;
- logical DocumentationTopic boundary clarification;
- explicit Domain root expected-recognition assertion;
- sole explicit Domain settings host;
- non-executable Profile Why;
- order-independent Bootstrap Contributions;
- explicit pre-Index role of `{bootstrap}`.

RA-R1-F13 was declined.

## Substantive packages prepared

1. `Core_ReviewA_R1_ChangeDelivery_Instructions_2026-08-31.md`
2. `DocumentationMethodology_ReviewA_R1_ChangeDelivery_Instructions_2026-08-31.md`
3. `Capabilities_Architecture_Review_2026-08-31-1_CoreSubstrate_v1.md`

The Documentation Methodology package also applies the already-confirmed queued WIP convention:

```text
one top-level-topic WIP series
Capabilities_WIP_vN
parallel thread/subtopic identity inside the WIP
no Capabilities_Messaging_WIP / Capabilities_Review_WIP series
```

## Remaining work

### 1. Apply owning-project changes

Apply the Core package against current Core masters and issue/regenerate:

- Core Index v2/current Core parent files;
- Domain v3;
- Bootstrap v2;
- `Core_Binder_v2.md`.

Apply the Documentation Methodology package and issue/regenerate:

- `AIDE_DocumentationMethodology@v22`;
- `DocumentationMethodology_Binder_v3.md`.

The generated Binders are read-only outputs, not edit sources.

### 2. Relay R1 Decision response to Claude

Send:

```text
Thread: aide-architecture-review-a-core-substrate
Message-ID: aide-architecture-review-a-core-substrate/gpt/002
In-Reply-To: aide-architecture-review-a-core-substrate/claude/001 @ Claude_v1
Expects: None
```

The message records the complete Lead dispositions and says a later R2 request will follow revised
authoritative material.

### 3. Review A Round 2

When both revised Binders are available in the coordination context:

- verify source sufficiency;
- create R2 Review Input Contract;
- recommended posture: Inspect / High / Full;
- focus on whether R1 changes resolved findings without new contradictions;
- send R2 via AIDE Messaging;
- correlate Claude response;
- disposition any new findings;
- complete Review A only after High-level re-review confidence is sufficient.

### 4. Durable Review evidence

The current Review checkpoint file records R1/dispositions.

On R2 completion, issue the next Review checkpoint/final Review Result with enough Round evidence to
reconstruct the cycle. Do not rewrite Claude's original Finding text.

### 5. WorkRegister

`WR17 — Peer-review major Capabilities architecture slices` remains open.

Do not close WR17 until Reviews A-D, final integrated Review E and required reconciliation are
genuinely delivered under the programme.

## Resume point

Resume by obtaining/confirming the revised:

```text
Core_Binder_v2.md
DocumentationMethodology_Binder_v3.md
```

Then construct Review A Round 2.

---
Dependencies: !AIDE_DocumentationMethodology@v21, AIDE_Review@v2, AIDE_Messaging@v1
References: Capabilities_WorkRegister_v14, Capabilities_Architecture_Review_2026-08-31-1_CoreSubstrate_v1
