# Documentation Methodology — Review A R2 Preflight Correction — Change Delivery Instructions — 2026-09-01

## Purpose

Correct one narrow incomplete application of the coordinated Review A Round 1 Core /
Documentation Methodology seam before Review A Round 2.

The revised Core corpus now publishes the current generic Index contract as:

`AIDE_Index@v2`

The newly issued Documentation Methodology v22 corpus correctly implements the
`DocumentationTopic` logical-boundary semantics, but several **current/normative** references and
dependency checkpoints still point to `AIDE_Index@v1`.

This correction changes no Review A Lead disposition and introduces no new architecture.

Do not broaden into Review B or other cross-capability cleanup.

## Authoritative inputs

- `Core_Binder_v2.md`
- `DocumentationMethodology_Binder_v3.md`

Core is authoritative for the current generic Index contract.

## Required correction

Where Documentation Methodology is stating or depending on the **current generic Index contract**,
replace `AIDE_Index@v1` with:

`AIDE_Index@v2`

This includes current/normative occurrences in:

- Documentation Methodology Index;
- Documentation Methodology Design;
- canonical Documentation Methodology Standard;
- Documentation Methodology Guide; and
- current dependency metadata in any reissued current master.

### Preserve historical version-specific reasoning

Do **not** mechanically replace historical statements whose meaning is specifically that the
generic Index was originally established/adopted at `AIDE_Index@v1`.

For example, a historical Decisions entry saying that D22 adopted `AIDE_Index@v1` may remain
unchanged as history.

The correction is to **current consumption/conformance**, not historical rewriting.

## Current semantic seam after correction

```text
Core / AIDE_Index@v2
    owns:
    - generic Index / Item / Item Type
    - optional Domain-neutral ItemTypeRegistry

Documentation Methodology
    owns:
    - DocumentationTopic semantic Item Type
    - documentation-specific Index extensions

AIDE_Domain@v3
    owns:
    - approved Domain recognition set
    - Domain eligibility / Domain resolution
```

`DocumentationTopic` remains a logical top-level-topic boundary declared/described by its governing
Index. No Item Type owner can self-elevate into Domain authority.

## Issue/version discipline

Do not replace already-issued v22 bytes in place.

Issue the smallest truthful correction release/checkpoint set required by the current Documentation
Methodology versioning rules.

Expected current replacements:

- `DocumentationMethodology_Index_v8.md`
- `DocumentationMethodology_Design_v20.md`
- `DocumentationMethodology_Decisions_v21.md` only if its current dependency metadata is changed;
  no new substantive Decisions event is required solely for this mechanical correction
- `AIDE_DocumentationMethodology_Standard_v23.md`
- `DocumentationMethodology_Guide_v23.md`

Canonical capability identity becomes:

`AIDE_DocumentationMethodology@v23`

Add:

```yaml
Transition:
  Version: v23
  Posture: None
```

Reason: this is a current-contract reference/conformance correction; it requires no consumer
content transformation.

Regenerate:

`DocumentationMethodology_Binder_v4.md`

If the owning project determines a smaller mechanically valid file-version set under the current
methodology, preserve that discipline, but do not edit already-issued current files in place.

## Core impact

Do not reissue Core solely because Documentation Methodology advances from v22 to v23.

The current Core documents truthfully record their last saved/proven Documentation Methodology
checkpoint at v22. A v23 `None` transition does not require them to be rewritten merely because
v23 becomes available.

## Validation

Before issuing the replacement Binder:

1. current/normative Documentation Methodology statements consume `AIDE_Index@v2`;
2. current dependency metadata uses `AIDE_Index@v2` where the reissued document has been proven
   against that contract;
3. historical Decisions references to the original v1 adoption remain historical where appropriate;
4. `DocumentationTopic` logical-boundary semantics remain unchanged;
5. `AIDE_Domain` remains the exclusive Domain-capability authority;
6. the one-WIP-series-per-top-level-topic rule remains unchanged;
7. no unrelated Review B / Review / Messaging / WorkRegister semantics are changed;
8. the generated Binder contains only the corrected current masters.

## Review continuation

Return the corrected:

`DocumentationMethodology_Binder_v4.md`

to the Capabilities Review coordination context.

Review A remains `Continuing / High`.

Round 2 should then review:

- `Core_Binder_v2.md`
- `DocumentationMethodology_Binder_v4.md`

against the R1 Findings and effective Lead disposition
`aide-architecture-review-a-core-substrate/gpt/002 @ GPT_v2`.
