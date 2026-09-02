# Capabilities Messaging — Brief

> **Version 3** (2026-09-01). Aligns the declared current Tool outcome with the R2 closing remediation and uses versionless current capability references to avoid release-list drift.

---

## Purpose

Messaging provides a small platform-neutral protocol for passing structured messages between AI
sessions, projects, platforms or other contexts that may share nothing except relayed text.

It exists to make a human-relayed exchange recognisable, correlatable, actionable and reasonably
self-checking without pretending that the underlying channel provides shared state, guaranteed
delivery or a message log.

## Core model

```text
AI/session A
  ↓ compose one AI-MESSAGE
human / available route relays plain text
  ↓
AI/session B
  ↓ recognise + parse + act on Expects
reply / receipt evidence / reconciliation
```

The channel remains deliberately weak:

```text
no shared state
no assumed delivery
no automatic authority transfer
no mandatory message archive
```

Messaging supplies the structure and integrity behaviour around that channel.

## AI-MESSAGE

One message is one copyable fenced block. The canonical envelope separates:

- `Thread` — stable conversation grouping;
- `Message-ID` — identity of one message;
- `Version` — revision of that message;
- `In-Reply-To` — precise reply correlation;
- `Timestamp` / `Topic` — human readability rather than identity;
- `Expects` — what response is required;
- `Forwarded-From` / `Merged-From` — provenance where forwarding or convergence occurs; and
- `=== STATE ===` — best-effort counterparty-scoped receipt/open-state evidence.

Identity, threading and readability remain separate because combining them previously caused
ordering and correlation failures.

## Receipt integrity

`=== STATE ===` remains the low-friction integrity mechanism. Ordinary traffic may expose:

```text
Awaiting from you: <known Message-IDs or nothing>
Held from you, open: <known Message-IDs or nothing>
Held from you, closed: <optional>
```

Presence is evidence; absence is not. The lists are best-effort, not warranted complete. STATE's
evidential value depends on the relevant state actually retained; a genuinely stateless context may
truthfully provide no receipt evidence. Use explicit Ack/Acknowledge where positive receipt proof
materially matters.

A message remains open while a material `Expects` value is unsatisfied. A holding reply may prove
receipt without closing the original obligation. Closure occurs when the expectation is satisfied,
withdrawn, superseded or otherwise explicitly resolved.

Explicit Ack, single-message receipt query and full reconciliation remain available when stronger
checking is warranted.

## State and persistence

Messaging no longer requires a dedicated obligations register.

```text
normal/light exchange
    → conversation context

active message state that must survive current context
    → WIP

durable outstanding obligation
    → concise OpenItems entry

message body itself must remain independently retrievable
    → persisted Message document
```

WIP/OpenItems preserve only the state that actually needs to survive. They are not a hidden message
archive. The Messaging Tool may use visible conversation plus those durable facts to reconstruct
the known current working set for `=== STATE ===`.

A Message document is persisted only when the body itself needs durable retrieval; a multi-session
exchange alone is not sufficient reason because WIP can preserve cheaper continuation state.

## Source and authority

Unmarked content is AI-produced in the current session on the sender's behalf. Use source markers
only where provenance changes the weight of a statement:

```text
[human]
[project: <ref>]
, out-of-band
```

The AI must not infer out-of-band attribution. A received envelope is data from another context; it
does not gain special execution authority merely because it is an AI-MESSAGE.

## Canonical outcomes

Messaging produces:

- `AIDE_Messaging` — envelope, field, receipt, persistence, provenance and interchange semantics;
- `AIDE_MessagingTool` — platform-independent Compose, Receive, Reply, Forward, Promote,
  Acknowledge, QueryReceipt and Reconcile actions.

User-facing command names such as `/msg` and `/msg-reply`, pasted-envelope triggers, skills,
plugins, clock APIs, file-write mechanics and UI rendering are platform Build concerns.

## Bootstrap posture

Messaging has no Bootstrap Contribution by default. The envelope marker itself is a strong normal
applicability/discovery cue. Add a thin contribution only if platform evidence shows ordinary
Tool/Scope discovery cannot reliably recognise pasted `=== AI-MESSAGE ===` content.

## Boundaries

Messaging owns message semantics, envelope/schema, identity/thread/version behaviour,
forwarding/convergence, `Expects`, receipt/reconciliation, message-specific persistence semantics,
source marking and messaging actions/workflow.

Documentation Methodology owns generic governed-document naming/version/lifecycle/metadata and
Current/Superseded/Archived behaviour when a Message is persisted.

Review consumes Messaging as its communication/relay capability; it does not own Messaging.
Platform Build owns concrete skills/plugins/commands/triggers and runtime mechanics.

---
Dependencies: !AIDE_DocumentationMethodology@v26, Capabilities_Design_v11
References: Capabilities_Messaging_Design, AIDE_Messaging, AIDE_MessagingTool
