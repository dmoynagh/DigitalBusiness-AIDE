> identity: DocumentManagement_Brief@v3 | doctype: brief | updated: 2026-09-23

# Document Management — Brief

A local MCP server that gives every local AI surface a common, reliable way to work with documents in AIDE document sources.

## Purpose

AI-assisted document work currently relies on surface-native file access (Code's filesystem, Chat's file output) with no shared operational layer. Each surface has different capabilities, different git behaviour, and no common way to discover or address document sources. Convention enforcement depends entirely on skills firing and the AI following them correctly — every surface, every model, every session must get it right independently.

A shared document operations server solves three problems: surfaces that cannot access files directly gain access through it, surfaces that can access files gain safety guarantees they don't have natively, and the token-cost bottleneck (a 2-line change currently costs ~4,000 output tokens regenerating the whole file) is eliminated through partial-update operations.

## Objectives

1. **Efficient document updates.** A caller can update a document without regenerating the entire file.
2. **Safe operations by default.** The server prevents common errors — partial matches, writes to readonly sources, untracked deletions, path escapes — without the caller needing to manage safety.
3. **Source discovery.** The server knows where document sources are and exposes them by name, so callers address sources, not filesystem paths.
4. **Complete file operations.** All common file operations — read, write, copy, rename, delete, browse, partial update — are available through the server, including operations that currently require manual steps or separate CLI invocations.
5. **Reduce manual burden.** Git management is handled by the server. A multi-file update session produces one commit without the caller managing staging or commit timing.

## Scope and boundaries

**In scope:** Source discovery and listing. File reads and writes (text and binary). Partial-update operations on text. Copy, rename, delete with safety. Directory browsing. Git staging and commit. Binder build. Config-driven source management with readonly enforcement.

**Out of scope:** Mobile and web surfaces (local filesystem only — the server runs as a local process). Remote GitHub API operations and push to remote. AIDE document-content conventions including versioning, declarations, and cleanup decisions — these are owned by a governing skill that is a separate deliverable, designed and built independently, using the server's operations as primitives. Document structure decisions (owned by Core Structure). The docmeth rules themselves (owned by DocMeth).

## Prior decisions

The following are fixed inputs from the architecture session, not requirements derived from the problem:

- Python MCP server, shells out to git directly.
- Delivered as a marketplace plugin per the tested MCP delivery model.
- Machine-level config at `~/.aide/config.yaml`, shared across surfaces.
- The server/skill split — the server provides format-agnostic file primitives; AIDE document intelligence is the governing skill's concern.

## Requirements

- Readonly sources must reject all write operations.
- Format-agnostic file operations.
- Errors must return enough information for the caller to decide what to do next.
- Caller-supplied paths must be contained within the registered source — the server enforces the boundary.

## Linked build outcome

The MCP server, deployed via the `aide` plugin in the `digitalbusiness-aide` marketplace.

## Separate dependency

A governing skill providing AIDE document intelligence — versioning sequences, declaration management, convention enforcement, cleanup decisions — using the server's operations as primitives. This skill is a separate deliverable, designed and built after the server exists. It is not part of this design.

## Definition of done

1. The server discovers document sources and lists them by name.
2. A caller can browse the contents of any discovered source.
3. A caller can read any file and write to any non-readonly source.
4. A caller can partially update a text file without replacing the whole file.
5. Copy, rename, and delete work on any file, with delete handling git and non-git sources safely.
6. A multi-file update session produces one git commit on caller command, containing only the changes the server made.
7. Caller-supplied paths cannot escape the registered source boundary.
8. Errors are reported with enough detail for the caller to act.
9. Binder build is available as a server operation.
10. The server runs on Desktop and Code via the marketplace plugin.

---

Version note: v3 — cross-review remediation. Governing skill removed from this design's build outcome and placed as a separate dependency (F1). Objective 4 reworded — "file operations" not "lifecycle operations including version management" (F1/F13). Prior decisions section added — Python, MCP, marketplace, server/skill split moved from requirements (F13). Path containment added as a requirement and definition-of-done item (F4). Commit scope narrowed — "only the changes the server made" (F5). Surface scope clarified — local process (F11). 2026-09-23. Replaces v2.
