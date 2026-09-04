# Documentation Methodology — Review A / queued WIP reconciliation — Change Delivery Instructions — 2026-08-31

## Purpose

Perform one coherent Documentation Methodology substantive pass combining:

1. the Review A Round 1 `DocumentationTopic` clarification required at the Core/Documentation
   Methodology seam; and
2. the already-confirmed queued WIP naming/ownership convention that was explicitly waiting for the
   next normal Documentation Methodology pass.

The current `DocumentationMethodology_Binder_v2.md` / `AIDE_DocumentationMethodology@v21` are the
authoritative baseline.

This pass should not broaden into unrelated Review B work.

## Required release set

Issue:

- `DocumentationMethodology_Index_v7.md` replaces `DocumentationMethodology_Index_v6.md`.
- `DocumentationMethodology_Design_v19.md` replaces `DocumentationMethodology_Design_v18.md`.
- `DocumentationMethodology_Decisions_v20.md` replaces `DocumentationMethodology_Decisions_v19.md`.
- `AIDE_DocumentationMethodology_Standard_v22.md` replaces
  `AIDE_DocumentationMethodology_Standard_v21.md`; identity becomes
  `AIDE_DocumentationMethodology@v22`.
- `DocumentationMethodology_Guide_v22.md` replaces `DocumentationMethodology_Guide_v21.md`.

Regenerate:

- `DocumentationMethodology_Binder_v3.md`

Migration posture for v22: `None`.

This is a semantic clarification and WIP-series rule correction; do not mass-rename or mass-rewrite
existing corpus files solely because v22 is issued.

Where a current Core Index release is issued in the coordinated pass, use the truthful current
`AIDE_Index` dependency at issue time.

---

# 1. Clarify `DocumentationTopic`

Preserve `DocumentationTopic` as a Documentation Methodology-owned semantic Item Type representing
**one top-level documentation topic**.

Do not broaden it to every subtopic.

Canonical distinction:

```text
DocumentationTopic Item
    = logical top-level-topic boundary / scope

governing Index document
    = authoritative declaration/description used to recognise and resolve that logical Item
```

A declaration such as:

```text
{scope: "AIDE/Core", type: DocumentationTopic}
```

appearing in `Core_Index_vN.md` means:

> this Index declares/describes the logical `AIDE/Core` top-level DocumentationTopic boundary.

It does **not** mean the Markdown file itself is the semantic boundary merely because the marker is
written in that file.

Recognition may therefore inspect the authoritative governing Index declaration to identify the
logical topic scope it describes.

The Item provides:

- top-level-topic identity;
- self-describing documentation-boundary behaviour;
- governing Index/Document Register resolution; and
- optional known container/project mapping.

The existing Domain boundary remains:

> Defining `DocumentationTopic` does not grant Domain authority. `AIDE_Domain` alone decides
> whether that Item Type may establish/participate in Domain resolution.

Subtopics remain subordinate structures inside the top-level topic. They are not separate
`DocumentationTopic` Items merely because they have their own Design/Decisions/Index sections.
They may remain within the enclosing effective Domain through structural containment without
becoming Domain-capable roots themselves.

Update Design §9, Standard `DocumentationTopic` section, Guide explanation and Index summary to use
this distinction consistently.

## Decisions

Add a current decision recording the logical-boundary/declaration distinction and the deliberate
top-level-only scope.

Do not rewrite the earlier Foundation decision history; add the new clarification prospectively.

---

# 2. Apply the confirmed root-WIP series convention

The current v21 Standard/Design still permit a subtopic/thread WIP filename/series such as:

```text
Capabilities_Messaging_WIP_v7.md
```

That convention has since been explicitly rejected.

The current rule becomes:

> There is one current WIP series per top-level topic by default and for the normal AIDE workflow.

Canonical filename:

```text
{TopLevelTopic}_WIP_v{N}.md
```

Examples:

```text
Capabilities_WIP_v1.md
Core_WIP_v3.md
DocumentationMethodology_WIP_v2.md
```

Do **not** create subtopic-specific WIP series such as:

```text
Capabilities_Messaging_WIP_v1.md
Capabilities_Review_WIP_v1.md
```

### Concurrent active threads

When several active subtopics/threads coexist, keep their identity **inside** the top-level WIP.

A compact WIP may use sections such as:

```markdown
## Active thread — Messaging
...

## Active thread — Architecture Review A
...
```

or another concise internal structure.

The filename remains the top-level WIP series.

### Why

WIP is a top-level-topic continuation container, not another semantic subtopic document series.

Subtopic-specific series create:

- filename proliferation;
- uncertainty about which WIP to load when resuming the top-level topic;
- duplicate/fragmented continuation state; and
- unnecessary live-state discovery/indexing complexity.

Internal thread identity is sufficient because WIP is deliberately volatile, non-authoritative and
loaded for continuation.

### Scope

This correction applies to WIP only.

It does **not** remove legitimate subtopic-specific `Working` documents or independently justified
delegated OpenItems/WorkRegister scopes under their own rules.

### Versioning

Retain visible WIP `_vN` checkpoint versioning.

Within one editing context, draft freely.

Each issued/persisted continuity checkpoint increments the single top-level WIP series.

The prior issued checkpoint becomes Superseded according to the current lifecycle/physical handling
rules.

### Binder and Index treatment

Normal Binders continue to exclude WIP.

Update live-state examples from:

```text
Capabilities_Messaging_WIP
```

to:

```text
Capabilities_WIP
```

A WIP version increment does not require an Index/Binder reissue.

Creation/withdrawal of the top-level WIP series is reconciled at the next normal corpus checkpoint
where a live-state locator is useful.

---

# 3. Required document-specific edits

## `DocumentationMethodology_Design_v19`

Carry forward v18 and change:

- §4 WIP:
  - replace permission for subtopic/thread-key WIP series with one top-level-topic WIP series;
  - state internal thread sections carry concurrent subtopic identity.
- §6:
  - replace `Capabilities_Messaging_WIP_v7.md` with a top-level example such as
    `Capabilities_WIP_v7.md`.
- §8:
  - replace version-agnostic live-series examples with `Capabilities_WIP`;
  - preserve no-churn Binder/Index semantics.
- §9:
  - clarify `DocumentationTopic` logical boundary versus Index declaration document.
- any other WIP examples/wording:
  - remove the current exception permitting independently named subtopic/thread WIP series.

## `DocumentationMethodology_Decisions_v20`

Preserve v19 decision history and add at least:

### Decision — DocumentationTopic is the logical top-level-topic boundary

Record the clarification from Review A and preserve Domain's exclusive capability-assignment
authority.

### Decision — one WIP series per top-level topic

Trigger: the subtopic-key option created a false model where WIP appeared to belong to an active
subtopic rather than to the top-level continuation context.

Decision:

- use `{TopLevelTopic}_WIP_vN`;
- carry active thread/subtopic identity inside the WIP;
- do not maintain independent subtopic WIP series in the normal model.

Consequences:

- clearer resume contract;
- less live-state proliferation;
- no change to Working/subtopic document semantics;
- no mass rename requirement for historical/superseded WIP files.

## `AIDE_DocumentationMethodology_Standard_v22`

Update:

### Naming / point-in-time keys

Replace:

> WIP: no key normally; use a subtopic/thread key where several parallel active contexts within one
> top-level topic need independent WIP series.

with:

> WIP: one current series per top-level topic using `{TopLevelTopic}_WIP_vN`. Parallel active
> threads are identified inside the WIP, not through independently named subtopic WIP series.

### WIP section

State that WIP normally anchors to the top-level topic and is the single current continuation
checkpoint for that topic.

### Binder/live-state section

Use `Capabilities_WIP` as the version-agnostic example.

### DocumentationTopic section

Apply the logical-boundary/declaration clarification above.

### Migration

Add:

```yaml
Transition:
  Version: v22
  Posture: None
```

Do not require historical WIP renames or corpus-wide rewrites.

## `DocumentationMethodology_Guide_v22`

Update examples and explanatory text consistently:

- `Capabilities_WIP_vN`, not `Capabilities_Messaging_WIP_vN`;
- explain how one WIP holds several active thread sections;
- make the logical `DocumentationTopic` boundary versus Index declaration file distinction explicit;
- retain the explanation that containers may host several top-level topics.

## `DocumentationMethodology_Index_v7`

Update the current document register and release references.

Update the `DocumentationTopic Item Type` summary to say that the Item is the logical top-level-topic
boundary/scope declared/described by its governing Index.

No local configuration change is required.

---

# 4. Review finding deliberately not adopted

RA-R1-F13 is declined.

Do not generalise the special live-state current-version rule into a weaker stable Document Register
authority rule.

The Reviewer's cited evidence did not show a stale stable register row:

- a lower Documentation Methodology dependency version may truthfully record saved/proven
  conformance; and
- a versioned `References:` citation may deliberately identify the version actually used.

This pass makes no change from that finding.

---

# 5. Validation

Before issuing `DocumentationMethodology_Binder_v3.md`, verify:

1. No current v22 source authorises `Capabilities_Messaging_WIP`-style independent WIP series.
2. The canonical WIP name is top-level-topic based.
3. Parallel active threads are represented inside WIP.
4. WIP remains volatile/non-authoritative and outside normal Binders.
5. Working remains distinct and may still be subtopic-specific.
6. OpenItems/WorkRegister delegation rules are unchanged by this WIP correction.
7. `DocumentationTopic` is clearly a logical top-level-topic boundary, not the Markdown Index file.
8. Subtopics are not silently promoted to DocumentationTopics.
9. `AIDE_Domain` remains the only owner that can grant Domain-defining/domain-capable status.
10. v22 transition is `None`.
11. Binder manifest contains only the new Current masters.

## Review continuation

Return `DocumentationMethodology_Binder_v3.md` to Review A together with the revised Core Binder.

Review A remains High and Continuing until the revised seam has been re-reviewed.
