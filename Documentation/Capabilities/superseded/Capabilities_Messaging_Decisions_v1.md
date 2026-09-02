# Capabilities Messaging — Decisions

> **Version 1** (2026-08-31). Records the reconciliation decisions behind the first AIDE Messaging
> Design, Standard and Tool while preserving the successful AI-MESSAGE mechanisms that continue to
> earn their cost.
>
> Created: 2026-08-31 | Last modified: 2026-08-31

---

## D1 — Messaging is a first-class Capabilities component

**Decision.** Messaging owns reusable AI-to-AI/session/project/platform message semantics and
workflow rather than remaining inside Workflow, Review or Documentation Methodology.

**Reason.** The mechanism serves multiple AIDE concerns and future non-Review consumers. Ownership
by the first workflow that used it would duplicate or constrain a genuinely reusable capability.

---

## D2 — Preserve the AI-MESSAGE envelope rather than redesign from scratch

**Decision.** Retain the existing one-envelope structured-text model and change only mechanisms
whose old architectural assumptions no longer hold.

**Reason.** The system has worked successfully in real copy/paste operation. Blank-sheet review did
not reveal a simpler alternative with equivalent identity, receipt and recovery properties.

---

## D3 — Identity, threading and readability remain separate

**Decision.** Keep `Thread`, `Message-ID`, `Version`, `In-Reply-To`, `Topic` and `Timestamp` as
separate concepts. Timestamp never identifies or threads a message.

**Reason.** The earlier combined approach caused concrete ordering/thread-resolution failures.
Separate jobs cost little in the envelope and remove ambiguity.

---

## D4 — Sender-partitioned Message-ID remains the no-shared-state identity model

**Decision.** Use `{Thread}/{From-slug}/{NNN}` with each sender owning only its own sequence.
Never reconstruct an identifier from recollection.

**Reason.** The parties need no shared counter, collisions are visually attributable, and
identifier evidence can be carried by conversation/WIP/OpenItems without a global registry.

---

## D5 — Version remains distinct from Message-ID and file version

**Decision.** A revised message keeps its Message-ID and advances only the sender-owned envelope
Version after known relay. A persisted document's `_vN` remains a separate DocMeth document
version.

**Reason.** New-message identity, revision identity and document-file revision answer different
questions. Conflating them would make replies and durable copies ambiguous.

---

## D6 — Forwarding and convergence provenance remain optional explicit fields

**Decision.** Keep `Forwarded-From` for Forward and optional `Merged-From` for deliberate thread
convergence.

**Reason.** They solve real provenance questions while imposing no cost on ordinary messages when
omitted.

---

## D7 — Expects remains the response contract

**Decision.** Keep `Answer`, `Decision`, `Code`, `Review`, `Action`, `Ack`, `None`; `None` is
exclusive and Ack may combine with a substantive expectation.

**Reason.** The field turns a received message into an explicit requested outcome without embedding
a workflow-specific task system.

---

## D8 — Receipt and fulfilment are separate

**Decision.** A reply may prove receipt without closing the original message. An item remains open
until material Expects are satisfied, withdrawn, superseded or otherwise explicitly resolved.

**Reason.** The previous statement that any reply closes the message contradicted the useful
holding-reply behaviour, where receipt is demonstrated but the substantive ask remains outstanding.

---

## D9 — STATE remains the default low-friction receipt-integrity mechanism

**Decision.** Retain counterparty-scoped `Awaiting from you`, `Held from you, open` and optional
closed state on ordinary traffic where prior state exists.

**Reason.** It demonstrates receipt/open state as a by-product of communication rather than adding
a mandatory acknowledgement exchange. No cheaper mechanism found in review provides equivalent
probability of exposing a missed relay.

---

## D10 — STATE inference remains intentionally asymmetric

**Decision.** Presence of an unexpected identifier is a mismatch signal; absence proves nothing.
`nothing` means no known item from available evidence, not warranted completeness.

**Reason.** Conversation/WIP/OpenItems state can be incomplete. Treating omission as proof would
turn a best-effort integrity mechanism into false assurance.

---

## D11 — Remove the dedicated obligations register

**Decision.** Messaging does not require a permanent obligations/sent-items register. Use visible
conversation first, WIP for active continuation state, OpenItems for durable obligations, and a
persisted Message only when its body needs retrieval.

**Reason.** The old register mixed receipt bookkeeping with durable work persistence. DocMeth v21
now supplies purpose-specific WIP/OpenItems mechanisms, so retaining another live ledger would
duplicate state and create reconciliation burden.

**Rejected alternative.** Keep the old register for tidiness/continuity. Rejected because its
unique value disappears once receipt-state construction is allowed to consume the existing durable
state sources.

---

## D12 — Drafted-but-unsent is not a canonical durable state

**Decision.** Draft generation does not establish delivery. A draft that genuinely must survive
context loss may be preserved in WIP, but Messaging creates no dedicated durable drafted state.

**Reason.** Only the human/actual route can establish relay. A permanent draft ledger adds friction
to the default light tier without strengthening that epistemic boundary.

---

## D13 — Light remains default; persist only when the body needs retrieval

**Decision.** Conversation is the default residence. A Message document is justified when the
actual body must be independently retrievable, not merely because an exchange is long, important or
crosses a session.

**Reason.** WIP/OpenItems can preserve continuation/obligation cheaply. Persisting every durable
ask would recreate a message archive and undermine the original low-friction tiering.

---

## D14 — Lifecycle is removed from the envelope

**Decision.** Do not carry `Lifecycle` inside AI-MESSAGE. When persisted, generic lifecycle,
filename, metadata and Current/Superseded/Archived mechanics are supplied by Documentation
Methodology.

**Reason.** Lifecycle is a property of the governed persisted document, not of a light transport
envelope. The old field reflected the prior DocMeth ownership split.

---

## D15 — Persisted Message semantics remain Messaging-owned

**Decision.** A persisted Message preserves the complete envelope as its substantive record;
envelope Version remains independent of document version, and another party's body is not silently
rewritten. Generic document mechanics remain DocMeth-owned.

**Reason.** This preserves message fidelity while respecting the one-owner boundary established by
Documentation Methodology v21.

---

## D16 — Source marking and out-of-band protections remain

**Decision.** Keep `[human]`, `[project: <ref>]` and human-supplied `, out-of-band` marking only
where provenance changes weight. The AI does not infer out-of-band attribution.

**Reason.** Cross-context AI messages otherwise blur AI-generated wording, human statements and
recorded project positions. The markers are cheap when sparse and prevent materially different
sources being presented as equivalent.

---

## D17 — Drafting protections remain operational requirements

**Decision.** Obtain a clock rather than inventing timestamps; never reconstruct identifiers from
memory; never infer out-of-band attribution; output one envelope; render it as one fenced copy
block.

**Reason.** These rules came from observed failures. They are construction checks rather than
stylistic preferences and remain warranted despite their small procedural cost.

---

## D18 — Keep seven user-facing commands and add canonical Receive

**Decision.** Preserve the familiar `/msg`, `/msg-reply`, `/msg-fwd`, `/msg-promote`, `/msg-ack`,
`/msg-query`, `/msg-reconcile` compatibility vocabulary. The canonical Tool additionally defines
`Receive` as a logical action for pasted/returned envelope processing without requiring an eighth
slash command.

**Reason.** Every existing command still has one clear job. Receive was already significant runtime
behaviour but lacked an explicit logical-action home.

---

## D19 — Platform mechanics move to Build

**Decision.** Claude skills/command files, ChatGPT/Codex representations, pasted-envelope trigger
implementation, clock/file APIs and similar mechanics are Build outputs, not canonical Messaging
semantics.

**Reason.** The envelope is platform-neutral. Baking the currently successful Claude implementation
into the Standard would make implementation evidence into architecture.

---

## D20 — No Messaging Bootstrap Contribution by default

**Decision.** Normal Scope/Tool discovery should recognise the strong `=== AI-MESSAGE ===` marker.
Create a thin Bootstrap Contribution only when platform evidence demonstrates that normal discovery
cannot do so reliably enough.

**Reason.** Bootstrap is intentionally thin and should not become a universal eager include. No
current evidence shows Messaging requires session-start processing merely to recognise an envelope
later in the conversation.

---

## D21 — Review consumes Messaging and does not own transport

**Decision.** Review supplies Review/Round/request semantics; Messaging supplies AI-MESSAGE relay,
receipt/reconciliation and messaging actions. Direct platform routes may optimise transport without
changing that ownership split.

**Reason.** Review and Messaging have different lifecycles and consumers. Resolving the previously
open communication seam to Messaging preserves one owner without enlarging Review.

---

## D22 — Old Specification/Migrations/requirements artefacts are source, not the new output model

**Decision.** The former Workflow Specification, Migrations and requirements register remain useful
source/history but are not recreated as required AIDE Messaging siblings. Current production uses
Messaging Design → canonical Standard/Tool and `AIDE_Migration` transition declarations.

**Reason.** Current Capabilities/Standards already replaced the separate Specification production
layer and owns generic release-transition machinery. Recreating the old artefact topology would
duplicate current architecture.

---

Dependencies: !AIDE_DocumentationMethodology@v21, Capabilities_Design_v9
References: Capabilities_Messaging_Design_v1, Workflow_Messaging_Design_v5,
Workflow_Messaging_Specification_v1, Workflow_Messaging_Requirements_v1
