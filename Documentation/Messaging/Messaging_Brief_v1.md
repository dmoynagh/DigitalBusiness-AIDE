> identity: Messaging_Brief@v1 | doctype: brief | updated: 2026-09-15

# Messaging — Brief

## Purpose

Define the format, structure, and conventions for reliable communication across any boundary — between AI sessions, projects, platforms, or contexts that may share nothing except relayed text.

Messaging is a grammar, not a transport. It defines what is carried, not how. Messages travel by Orchestration transport (automated) or by copy-paste (manual, always available). The format is the same regardless of channel.

## Objectives

**O1. A recognisable, correlatable message format** that works over any channel — including channels with no shared state, no guaranteed delivery, and no message log.

**O2. Identity and threading without shared state** between parties.

**O3. Best-effort receipt integrity** — raise the probability that a missed relay is noticed, without requiring mandatory acknowledgement round-trips for every exchange.

**O4. A clear persistence model** — light by default, persisted only when the body itself needs retrieval.

**O5. Platform-neutral semantics** — the format works regardless of transport mechanism or AI platform.

## Requirements

R1. The envelope must be a single copyable text block. Copy-paste is the baseline transport; the format must survive it.

R2. Identity, threading, and readability must remain separate concerns — combining them caused concrete failures.

R3. No shared state between parties is required for any operation.

R4. No platform-specific mechanism in the standard or tool.

R5. Receipt integrity is honest about what it can and cannot prove — integrity, not assurance.

## Scope and boundaries

**In scope:** envelope format, field meanings, identity/threading/versioning, Expects and fulfilment, STATE receipt integrity, receipt escalation (Ack/Query/Reconcile), source marking and authority, drafting protections, persistence model, logical actions.

**Out of scope:** transport mechanism (Orchestration), what messages carry (sender's concern), platform-specific skills/commands/triggers (Build), Review lifecycle (Review consumes Messaging).

**Boundary with Documentation Methodology:** DocMeth supplies generic document mechanics (naming, versioning, lifecycle) when a message is persisted as a governed document. Messaging owns the message-specific semantics.

**Boundary with Orchestration:** Messaging defines the format; Orchestration provides automated transport. Copy-paste is always available as baseline.

**Boundary with Review:** Review owns the Review lifecycle and request semantics. Messaging owns the envelope, relay, and receipt behaviour Review consumes for indirect/manual transport.

## Linked build outcome

A skill replacing the current `workflow-messaging` skill, authored from the Messaging standard and tool.

## Definition of done

1. A Messaging standard defining envelope format, field semantics, identity, threading, STATE receipt integrity, source marking, persistence, and drafting protections.
2. A Messaging tool defining the logical actions for composing, receiving, replying, forwarding, acknowledging, querying, reconciling, and promoting messages.
3. Both deployable as a skill.
4. Cross-reviewed by a separate AI.

---

Version note: v1 — initial brief from the Messaging design pass. 2026-09-15.
