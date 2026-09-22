> identity: DocumentManagement_Decisions@v5 | doctype: decisions | updated: 2026-09-23

# Document Management — Decisions

## D1. Concurrent multi-surface staging — residual risk stated

Two surfaces operating on the same git repo simultaneously share the same working tree and index. The design handles this differently depending on whether the surfaces touch the same or different files.

**Different-path concurrency** is safe. The clean-file precondition and content-verified commit (D6) ensure each session's commit contains only its own changes. Git's file-level locking prevents mechanical index corruption.

**Same-path concurrency** is detected at commit time. If two sessions mutate the same file, the second session's write overwrites the first's content. When the first session tries to commit, its expected path state won't match — either the content hash is wrong (for present paths) or a deleted path has been recreated. The first session's commit is rejected. The clean-file precondition catches the sequential case (second session sees a dirty file); the expected-state verification catches the concurrent case (both pass the precondition but only one can commit successfully).

This is an accepted limitation. The losing session's commit is rejected, not silently corrupted. Revisit only if the rejection proves too coarse in practice.

## D2. Primitives server, not AIDE-aware server

The server provides file primitives with no AIDE document-content vocabulary. All document intelligence (versioning, declarations, cleanup) lives in a governing skill loaded in session. The split exists because AIDE document conventions evolve through standards — if the server embedded them, every standards change would require a server rebuild. With the split, the server is stable infrastructure that changes only when file operations change.

Considered and rejected: embedding docmeth rules as deterministic enforcement in the server (the original architecture-session position). Reversed during the design session when Dave observed that the AI has the standards loaded and can orchestrate versioning sequences from primitives — making the enforcement-in-server coupling unnecessary.

## D3. Structural awareness for source discovery

The server reads `_index.md` files for source registration — filename, heading, and role field. This is structural folder metadata, not AIDE document-content interpretation. Comparable to git reading `.gitignore`. The `_index` specification is defined by the Core Structure Standard and expected to be extremely stable. A change to the `_index` format would require a server update — accepted as the cost of a genuine dependency on a stable specification.

Considered and rejected: fully config-driven discovery with no `_index` awareness. This would require every source to be explicitly configured, losing the auto-discover capability that makes the server low-friction.

## D4. Config-based source registration at `~/.aide/config.yaml`

Machine-level YAML config, read at startup, shared across surfaces. Holds scan roots, auto-discover flag, explicit includes (with optional name override and readonly flag), and excludes.

Considered and rejected: per-repo config files (`.aide.yaml` in each repo). Previously rejected in the architecture session — per-repo config distributes settings across repos and complicates the server's startup scan.

## D5. Explicit include overrides auto-discover for the same path

When an explicit include names a path that auto-discover also finds, the explicit config wins. This lets the user override the auto-discovered name or add a readonly flag to a source that would otherwise be writable.

## D6. Clean-file precondition and expected-state verified commit

The git isolation model uses three mechanisms: a clean-file precondition (reject mutations on files with uncommitted changes or untracked status), stage-and-record with expected path state (the server tracks what it did and what state each path should be in), and expected-state verified commit (check every recorded path against its expected state before committing).

The expected path state is either `present + SHA-256` (for writes, patches, copies, and rename destinations) or `absent` (for deletes and rename source paths). This generalisation from a hash-only record allows the verification to cover operations whose intended result is the absence of a file — `delete` and the old path of `rename` — which a content-hash-only model cannot verify.

The expected state is server-owned — independent of the shared git index, which can be modified by other processes. This is what establishes ownership of the committed content.

Considered and rejected: content-hash-only verification (the design v3/v4 position). Cross-review identified that delete and rename-old-path produce an intended state of absence, which has no content to hash. The expected-state model covers all mutation types uniformly.

Also considered and rejected: a separate git index per session. This would provide true isolation but adds substantial complexity for a solo-developer context where the expected-state verification already catches external interference.

## D7. Subprocess git, no library

All git operations via `subprocess.run(["git", ...])`. No git library dependency. The server shells out to the git binary on the user's PATH. The git operations are trivial (`add`, `commit`, `status`, `rm`, `diff`); a library adds dependency weight for no capability gain.

## D8. Delete safety — git delete vs `_recycle`

Git-backed sources: actual deletion, staged. Git is the version history. Non-git sources: file moved to `_recycle` at source root with relative path preserved. The caller always calls `delete`; the server determines behaviour from source metadata. Numeric suffix handles repeated deletions to the same recycle path.

Considered and rejected: always moving to `_superseded`. Changed during the design session — `_recycle` is a better name for a general-purpose safety net that isn't specific to AIDE versioning semantics.

## D9. Keyed-data unique-match patching

The patch operation requires exactly one match. Zero or multiple matches fail with the count returned. The match is exact on the raw text including whitespace and line endings. This is the primary token-efficiency mechanism — partial updates without regenerating the file.

## D10. Binder builder as a hosted operation

The binder builder is bundled as a Python script and invoked by the server. This is an acknowledged exception to the pure-primitives model. The server's coupling is limited to reading the output path from the binder settings file, applying containment and safety checks, invocation, output staging, and error capture. The script owns its own logic and settings.

## D11. Governing skill is a separate deliverable

The governing skill that provides AIDE document intelligence (versioning sequences, declaration management, cleanup decisions) is not part of this design. It is a separate deliverable, designed and built after the server exists. It depends on the server's primitives and is updated independently when AIDE document conventions change.

Originally listed in the brief's build outcome and definition of done. Removed during cross-review remediation — the skill requires its own design.

## D12. Marketplace plugin delivery

Delivered via the `aide` plugin in the `digitalbusiness-aide` marketplace per `Infrastructure_MCPDeliveryModel@v2`. The builder should consult that document and the Orchestration dispatch server as a working example.

## D13. No hot-reload or file watching

Source list is loaded at startup and held in memory. A restart re-scans. No file-watching or hot-reload. The set of sources changes rarely and a restart is trivial. Hot-reload would add complexity for a problem that barely exists.

## D14. Copy and rename fail on existing destination

No silent overwrite on copy or rename. If the destination path already exists, the operation fails and reports the collision. Write deliberately does allow overwrite — the semantics are "set the content of this file", which is different from "put a copy here" or "move this file there".

## D15. Binder output contract — declared output is complete mutation set

The server reads the binder-builder settings file and extracts the output path before invocation. After the script runs, the server stages and records only the declared output file. The declared output path is the binder builder's complete filesystem mutation set — the builder must not create, modify, or delete files outside it. This is a builder contract requirement, not a suggestion. The server applies its full safety model (containment, clean-file precondition, expected-state recording) to the declared output and has no visibility of mutations outside it. Undeclared mutations are a builder contract violation.

## D16. Source name uniqueness enforced after all qualification

After all qualification rules have been applied (solution/project nesting, explicit name overrides), source names must be unique. Any remaining collision — regardless of cause — is rejected at startup with both paths reported. Resolution is manual: the user adds a `name` override in config. This covers cases the individual collision rules cannot anticipate.

## D17. Server tools on Desktop only — Chat gets skills, not tools

The server runs as a local process and its MCP tools are available only on Desktop surfaces (Code and Cowork) via desktop app marketplace registration. Local MCP server tools are not available through the web surface. Plugin skills (such as the governing skill, when it exists) can reach Chat via separate web UI account-level registration — that is the skill's delivery path, not this server's.

## D18. Delivery model is a reference document, not a standards dependency

Cross-review finding F12 requested that `Infrastructure_MCPDeliveryModel@v2` be formally declared as a dependency via the document's `uses` field. Rejected. The `uses` field is defined by DocMeth for standards dependencies — "standards this document depends on, as `standard@version` references." The MCP delivery model is explicitly not a standard. One design document referencing another in prose is the correct mechanism. The Build references section points the builder to it and to the Orchestration dispatch server as a working example. Accepted by the reviewer in pass 4.

## D19. Residual TOCTOU window — accepted

A narrow race condition exists between expected-state verification and the `git commit` command. An external write or file creation in that window could enter the commit undetected because `git commit -- <paths>` reads working-tree contents at commit time, not at verification time.

This is concurrent filesystem access to the same file within the same instant — entirely theoretical for a solo developer working one surface at a time. Stated as an accepted residual. A separate git index would eliminate it entirely but is rejected as disproportionate to the risk (D6).

## D20. Untracked files treated as dirty

An existing untracked file at a target path is treated as dirty by the clean-file precondition. The server rejects mutation on that path. The human must either track and commit the file (preserving it in git history) or remove it before the server will touch that path.

This is because git cannot preserve untracked content — deleting or overwriting an untracked file would lose unretrievable data. The server's safety model cannot guarantee protection for content git doesn't know about, so it refuses to touch it.

## D21. Binder output path subjected to containment before invocation

The binder output path is read from the settings file, not supplied by the caller. It is nevertheless subjected to the same path-containment rules as caller-supplied paths before the builder is invoked. A malformed or stale setting designating a path outside the source root is rejected. The clean-file precondition is also applied to the output path before invocation.

Cross-review finding N4 identified that without this check, a settings-derived path could bypass the source-containment model.

## D22. Expected path state covers all mutation types

The commit verification record is generalised from `path + content hash` to `path + expected state`:

- `present + SHA-256` for write, patch, copy, and rename-new-path
- `absent` for delete and rename-old-path

This ensures the verification model covers every mutation type uniformly. A hash-only record cannot verify that a deleted file has stayed deleted or that a renamed-away path has not been recreated.

Cross-review finding N2 identified the gap: the original hash-only model had no representation for the intended absence of a file.

---

Version note: v5 — N2/N3/N4 remediation. D1 updated for expected-state verification language. D6 rewritten for expected path state replacing hash-only. D20 added for untracked-as-dirty (N3). D21 added for binder output containment (N4). D22 added for expected path state covering all mutation types (N2). 2026-09-23. Replaces v4.
