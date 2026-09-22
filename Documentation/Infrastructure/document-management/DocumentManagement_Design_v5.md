> identity: DocumentManagement_Design@v5 | doctype: design | updated: 2026-09-23

# Document Management — Design

## Summary

A Python MCP server providing safe, format-agnostic file primitives over document sources. Twelve tools cover discovery, browsing, reading, writing, patching, copying, renaming, deleting, directory creation, git staging, committing, and binder builds. The server has no knowledge of AIDE document-content vocabulary — it does not interpret declarations, understand versioning grammar, or know what a doctype is. All document intelligence lives in a governing skill that is a separate deliverable.

The server has two bounded areas of structural awareness: source discovery (reading `_index.md` for role and name) and the binder build operation (hosting the binder-builder script). Both are acknowledged exceptions with explicit contracts.

---

## Model and approach

### Central principle — primitives server, smart skill

The server provides reliable file primitives with safety guarantees. The AI in session, with a governing skill loaded, provides AIDE document intelligence. The server does not interpret document content for AIDE purposes.

This split exists because AIDE document conventions evolve through standards, and standards change through the normal design-build-deploy cycle. If the server embedded document-content knowledge (versioning grammar, declaration parsing, doctype rules), every standards change would require a server rebuild and redeployment. With the split, standards changes update the governing skill only — the server is stable infrastructure.

The boundary is clean: the server does things to files, the AI decides which things to do. Multi-step sequences (version-copy, cleanup passes, declaration updates) are orchestrated by the AI using the server's primitives.

### Structural awareness — two bounded exceptions

The server is not entirely format-agnostic. It has structural awareness in two places:

**Source discovery** reads `_index.md` files to register sources. The contract is minimal and fixed: the server reads the filename (`_index.md`), the heading (source name), and the role field (whether the value is `Documentation Solution` or `Documentation Project`). This is structural metadata about folders, not document-content interpretation — comparable to git reading `.gitignore`. The `_index` specification is defined by the Core Structure Standard and is expected to be extremely stable. A change to the `_index` format would require a server update.

**Binder build** hosts the binder-builder Python script as an invocable operation. The server reads the binder-builder settings file to determine the output path, invokes the script, and stages the declared output. The declared output path is the binder builder's complete filesystem mutation set — the builder must not create, modify, or delete files outside it. The server's coupling is limited to: locating the settings file, reading the output path from it, applying containment and safety checks, calling the script with the source path, capturing success/failure, and staging the declared output file.

### What the server owns

File operations with safety guarantees. Path containment enforcement. Source discovery and config. Git staging with clean-file preconditions and content-verified commit using expected path states. The `_recycle` safety net for non-git sources. Keyed-data unique-match validation on patches. Readonly enforcement across all mutating operations. Error reporting.

### What the server does not own

Any AIDE document-content convention. Versioning decisions, declaration management, cleanup decisions, document identity, docmeth rules, doctype awareness. These are the governing skill's concern. The governing skill is a separate deliverable, designed and built after the server exists.

---

## Source discovery

The server discovers document sources at startup by scanning configured roots.

**Discovery algorithm:**

1. Read `~/.aide/config.yaml` for scan roots and explicit includes.
2. For each scan root (when auto-discover is on), walk immediate subdirectories looking for `_index.md` files.
3. Read each `_index.md` — if the role field declares Documentation Solution or Documentation Project, register as a source.
4. Source name comes from the `_index` heading.
5. Detect whether the source is git-backed by checking for a `.git` directory at or above the `_index` location.
6. Add any explicit includes from config. An explicit include for the same path as an auto-discovered source overrides the auto-discovered registration (the explicit config wins — it may carry a name override or readonly flag).
7. Apply excludes.

**Source naming and collision rules:**

- Source names are case-insensitive on Windows, case-sensitive on other platforms — matching the host filesystem convention.
- When two auto-discovered projects share a name, they are qualified as `Solution\Project` using the parent Documentation Solution's name. The solution relationship is determined by folder containment: a Documentation Project inside a Documentation Solution's folder tree belongs to that solution.
- If two explicit includes specify the same name, the config is invalid — the server reports the collision at startup and registers neither.
- An explicit include that has no `_index.md` heading and no `name` in config is invalid — the server reports it and skips it.
- Duplicate solution names are handled the same way as duplicate project names — by the containing path. If the collision is at the top level with no further containment to qualify, the config is invalid and reported.
- **After all qualification, source names must be unique.** Any remaining collision — an explicit include matching an auto-discovered name at a different path, a Documentation Solution and Documentation Project resolving to the same name, two same-named projects inside the same solution — is rejected at startup. Neither colliding source is registered, and the collision is reported. The resolution is always manual: add a `name` override in config.

Registered sources are held in memory for the server's lifetime. A restart re-scans. No file-watching or hot-reload — the set of sources changes rarely and a restart is trivial.

---

## Config

Machine-level config at `~/.aide/config.yaml`, read at startup, shared across all surfaces.

```yaml
scan-roots:
  - C:\Users\david\dev\repos

auto-discover: true   # default: true — scan roots for _index.md sources

include:               # explicitly add sources not under scan roots
  - path: C:\Users\david\docs\client-project
    name: client-project       # optional — overrides _index heading
    readonly: true             # optional — default false

exclude:               # skip discovered sources by path or name
  - C:\Users\david\dev\repos\archived-project
```

**Semantics:**

- `scan-roots` — directories to scan for repos and folders containing `_index.md`. Not recursive beyond one level of subdirectories.
- `auto-discover` — when true (default), the server walks scan roots on startup. When false, only explicit includes are registered.
- `include` — sources added by explicit path. Each may carry a name override and a readonly flag. An explicit include for a path that auto-discover also finds overrides the auto-discovered registration.
- `exclude` — paths or names to skip during auto-discovery. Does not affect explicit includes.
- `readonly` — when true, the server rejects all mutating operations on that source: write, patch, delete, rename, copy-to, mkdir, binder_build, and commit. Reads, browse, and status are unaffected.

---

## Path containment

Every tool that accepts a caller-supplied path enforces containment within the registered source root. The same containment rules apply to paths derived from settings (such as the binder output path).

**Rules:**

- Paths are normalised before any operation. Path separators are canonicalised to the OS convention.
- `..` components are resolved after normalisation. If the resolved path falls outside the source root, the operation is rejected.
- Absolute paths are rejected — all paths are relative to the source root.
- Symbolic links and junctions inside the source are resolved to their real target. If the target falls outside the source root, the operation is rejected.
- The containment check runs before any filesystem operation (read, write, delete, etc.).

This is a server-side safety guarantee. The caller cannot escape the source boundary regardless of what path it supplies, and settings-derived paths cannot escape it either.

---

## Text and binary handling

The server distinguishes text and binary files for read, write, and patch operations.

**Detection:** on read, the server uses the same heuristic git uses — scan the first 8,000 bytes for null bytes. Null bytes present means binary. This matches the caller's expectations since the source is a git repo or git-like structure.

**Text files:**

- Default encoding is UTF-8. Files that are not valid UTF-8 are reported as an error on read rather than silently mangled.
- Line endings are preserved as-is — the server does not normalise. Git's own `core.autocrlf` setting governs line-ending behaviour in the repo.
- Patch matching operates on the raw file bytes (after UTF-8 decoding). The match must be exact including whitespace and line endings.

**Binary files:**

- Read returns base64-encoded content.
- Write accepts base64-encoded content. The caller must set a `binary: true` flag on write so the server knows to decode from base64 rather than treating the content as text.
- Patch is rejected on binary files.

---

## Tool surface

Twelve tools. Each succeeds or fails independently. All file-mutating operations on git-backed sources enforce the clean-file precondition, stage the change, and record the expected path state for commit verification.

### list_sources

Returns all discovered sources with metadata: name, path, git-backed flag, readonly flag. No parameters.

### browse

List contents of a directory within a source.

- **source** — source name
- **path** — directory path within the source (optional — defaults to source root)
- **pattern** — glob filter (optional — e.g. `MyDoc_v*.md`)

Returns entries with: name, type (file or directory), size. Underscore-prefixed directories are included but flagged. Path containment enforced.

### read

Read a file's contents.

- **source** — source name
- **path** — file path within the source
- **lines** — return only this many lines from the top (optional, text files only)

Returns: content (text or base64), a flag indicating text or binary, and file size. When `lines` is specified on a text file, returns only the requested number of lines. Path containment enforced.

### write

Write or overwrite a file's entire content.

- **source** — source name
- **path** — file path within the source
- **content** — the full file content (text, or base64 when binary flag is set)
- **binary** — boolean flag (optional, default false) — when true, content is decoded from base64 before writing

Creates the file if it doesn't exist. Overwrites if it does. On git-backed sources: clean-file precondition enforced on the first mutation of this path in the session (including rejection of existing untracked files), change staged, expected state recorded as `present + hash`. Rejected on readonly sources. Path containment enforced.

### patch

Apply a partial update to a text file using keyed-data unique-match.

- **source** — source name
- **path** — file path within the source
- **old** — the text to find (must match exactly once in the file)
- **new** — the replacement text (empty string to delete the matched text)

The server validates that `old` matches exactly once before applying. On zero matches or multiple matches, the operation fails and returns the match count. Rejected on binary files and readonly sources. On git-backed sources: clean-file precondition enforced on the first mutation of this path in the session (including rejection of existing untracked files), change staged, expected state recorded as `present + hash`. Path containment enforced.

### copy

Copy a file.

- **source** — source name of the original
- **path** — file path of the original
- **dest_source** — destination source name (optional — same source if omitted)
- **dest_path** — destination file path

If the destination file already exists, the operation fails — no silent overwrite. On git-backed destinations: change staged, expected state recorded as `present + hash`. Rejected if the destination source is readonly. Path containment enforced on both source and destination paths.

### rename

Rename or move a file within a source.

- **source** — source name
- **path** — current file path
- **new_path** — new file path

If the destination path already exists, the operation fails — no silent overwrite. On git-backed sources: clean-file precondition enforced on the original path (first mutation in the session, including rejection of existing untracked files). Old path: deletion staged, expected state recorded as `absent`. New path: addition staged, expected state recorded as `present + hash`. Rejected on readonly sources. Path containment enforced on both paths.

### delete

Remove a file from a source. Safety behaviour depends on the source type — the caller does not need to know or branch.

- **source** — source name
- **path** — file path to delete

On git-backed sources: clean-file precondition enforced on the first mutation of this path in the session. Existing untracked files are rejected as dirty — git cannot preserve their history, so deletion would lose unretrievable content. For tracked files: actual file deletion, staged, expected state recorded as `absent`. Git retains the history.

On non-git sources: the file is moved to `_recycle` at the source root, preserving its relative path within `_recycle`. If a file already exists at the recycle destination, a numeric suffix is appended (e.g. `foo.md` → `foo_1.md`, `foo_2.md`) to avoid collisions from repeated deletions.

Rejected on readonly sources. Path containment enforced.

### mkdir

Create a directory within a source.

- **source** — source name
- **path** — directory path to create

Creates intermediate directories as needed. No git staging (git doesn't track empty directories). Rejected on readonly sources. Path containment enforced.

### commit

Commit the server's changes to a source's git repo.

- **source** — source name
- **message** — commit message

Before committing, the server verifies every recorded expected path state against the current filesystem:

- **Expected present + hash:** the file must exist and the SHA-256 of its current working-tree content must match the recorded hash.
- **Expected absent:** the file must not exist. If a deleted or renamed-away path has been recreated externally, the verification fails.

If any expected state does not match, the conflict is reported (naming the affected paths and what was expected vs found) and the commit is not made.

When all expected states verify, the server commits using `git commit -- <recorded-paths>`. Since `git commit -- <paths>` commits working-tree contents for the named paths, and verification just confirmed those contents match the server's intended state, the commit reflects the server's work.

Fails if the source is not git-backed, if there are no recorded paths, or if the source is readonly.

**Residual TOCTOU window:** a narrow race exists between state verification and the git commit command — an external write or file creation in that window could enter the commit. This is concurrent filesystem access to the same file within the same instant, entirely theoretical for the solo-developer context. Stated as an accepted residual, not an unaddressed risk.

### status

Show the current state of a source's git working tree.

- **source** — source name

Returns: files the server has staged in this session (recorded paths with their expected states), other staged files (not recorded by this session), modified-but-unstaged files, and untracked files. This distinction lets the caller see what `commit` will include versus what exists independently. Fails with a clear message if the source is not git-backed.

### binder_build

Run the binder builder for a source.

- **source** — source name

The server locates the binder-builder settings file within the source and reads the output path from it. Before invoking the builder, the server:

1. applies path containment to the declared output path — rejected if it resolves outside the source root;
2. applies the clean-file precondition to the declared output path — rejected if it is dirty or untracked.

The server then invokes the bundled Python binder-builder script against the source's document root. On success, the server stages the output file at the declared path and records it as `present + hash`.

The declared output path is the binder builder's complete filesystem mutation set. The builder must not create, modify, or delete files outside the declared output path. This is a builder contract requirement — the server applies its full safety model to the declared output and has no visibility of mutations outside it.

The server's role is containment verification, invocation, output staging, and error capture. The binder-builder script owns its own logic, settings resolution, and document-processing conventions.

Rejected on readonly sources. Fails if no binder settings are found for the source, if the output path fails containment, or if the binder-builder script reports failure.

---

## Git model

**Clean-file precondition, stage with expected path state, verified commit.**

The server's git model provides content-verified commit isolation through three mechanisms:

**1. Clean-file precondition.** Before the server's first mutation of any file in a session, the file must have no uncommitted changes — neither staged, unstaged, nor untracked. An existing untracked file at the target path is treated as dirty and rejected, because git cannot preserve untracked content and the server cannot guarantee safety for it. Once the server has mutated a file, subsequent server operations on that same file in the same session are permitted without rechecking — the server owns the path.

**2. Stage and record expected path state.** After each mutation, the server runs `git add <path>` (or `git rm <path>` for deletions) and records the expected path state:

- **Write, patch, copy, rename-new-path:** expected state is `present` with a SHA-256 hash of the content the server wrote.
- **Delete, rename-old-path:** expected state is `absent`.

The expected state is server-owned — independent of the shared git index.

**3. Content-verified commit.** At commit time, the server checks each recorded path against its expected state:

- For `present + hash`: the file must exist and its current working-tree content must hash to the recorded value.
- For `absent`: the file must not exist.

If any expected state does not match, the commit is rejected with the affected paths reported. When all states verify, `git commit -- <recorded-paths>` commits only the named paths. Since verification confirmed the working-tree state matches the server's intended outcome, the commit reflects the server's work.

**What this catches:**
- Pre-existing changes cannot be absorbed (clean-file precondition rejects dirty and untracked files).
- External modification after staging is caught by hash comparison at commit time.
- External recreation of a deleted file is caught by the absent-state check at commit time.
- Other staged files cannot be included (`git commit -- <paths>` scopes to named paths only).
- Same-path concurrency between sessions: the losing session's expected states won't match at commit time.

**Residual TOCTOU window:** a narrow race exists between state verification and the git commit command. An external write or file creation in that window could enter the commit undetected. This is concurrent filesystem access within the same instant — entirely theoretical for the solo-developer context and substantially narrower than the verification windows in standard git workflows. Stated as an accepted residual, not an unaddressed risk.

No branch-based staging, no separate index, no commit-per-file, no automatic commits.

**Implementation:** `subprocess.run(["git", ...])` for all git operations. No git library dependency. The server shells out to the git binary on the user's PATH. Content hashing uses SHA-256 on the file bytes.

---

## Error model

Each operation succeeds or fails independently. The server reports failures and stops — it does not recover, retry, or swallow errors. The AI manages multi-step sequences and decides what to do when a step fails.

**Error categories and what the server returns:**

- **Dirty file** — file has uncommitted changes (staged, modified, or untracked) and cannot be mutated. Names the path and its state.
- **Commit verification failure** — a recorded path's current state does not match the expected state. For `present + hash`: names the path and reports expected vs actual hash, or that the file is missing. For `absent`: names the path and reports that it unexpectedly exists. The commit is not made.
- **Path containment violation** — the resolved path falls outside the source root. Names the path and the source. Applies to caller-supplied paths and settings-derived paths (such as binder output).
- **Patch mismatch** — zero matches or multiple matches. Returns the match count.
- **Readonly rejection** — mutating operation attempted on a readonly source. Names the source and the operation.
- **Destination exists** — copy or rename target already exists. Names the destination path.
- **File not found** — names the path.
- **Source not found** — names the source.
- **Source name collision** — two sources resolve to the same name after qualification. Names both paths. Reported at startup.
- **Invalid config** — names the config issue (missing name, invalid path, etc.) at startup.
- **Binary rejection** — patch attempted on a binary file. Names the path.
- **Encoding error** — file is not valid UTF-8. Names the path.
- **Git failure** — returns git's error output verbatim.
- **Filesystem error** — returns the OS error (permissions, locked file, disk full).
- **Binder build failure** — returns the binder-builder script's error output.

Every error returns a structured response with: success flag, error type, and a human-readable message containing enough detail for the caller to act.

---

## Packaging and delivery

Delivered as part of the `aide` plugin in the `digitalbusiness-aide` marketplace, following the tested MCP delivery model documented in `Infrastructure_MCPDeliveryModel@v2`.

The server's tools are available on **Desktop only** — Code and Cowork — via desktop app marketplace registration (Settings → Plugins → marketplace). The server runs as a local process with local filesystem access. Chat does not have access to the server's tools because local MCP server tools are not available through the web surface.

Plugin skills (such as the governing skill, when it exists) are a separate matter — skills can reach Chat via web UI account-level registration. That is the skill's delivery path, not this server's.

The binder-builder Python script is bundled inside the plugin so that `binder_build` has no external dependency beyond the script itself and the source's binder settings.

**Build references:** the builder should consult `Infrastructure_MCPDeliveryModel@v2` for the packaging methodology, plugin structure, registration paths, and known platform issues. The Orchestration dispatch server in the same plugin is a working example of the same delivery pattern. These are reference documents for the builder, not standards dependencies — they do not govern this design's content and are not declared in `uses`.

---

## Boundaries

The server does not:

- Interpret, parse, or validate AIDE declarations, doctypes, identity fields, or versioning grammar
- Make versioning decisions or cleanup decisions
- Load, read, or reference any AIDE standard or skill at runtime
- Push to remote repositories
- Operate on non-local filesystems
- Watch for file changes or run operations automatically
- Commit changes it did not make (within the stated TOCTOU residual)
- Serve tools to Chat or any web surface

The server does have bounded structural awareness for source discovery (`_index.md` format) and binder building (hosting the script, reading the output path from settings). These are stated exceptions with explicit contracts.

---

Version note: v5 — N2/N3/N4 remediation. Commit verification generalised from content-hash to expected path state (`present + hash` or `absent`) — covers delete and rename-old-path (N2). Clean-file precondition expanded to include untracked files as dirty (N3). Binder output path subjected to containment and clean-file checks before invocation (N4). 2026-09-23. Replaces v4.
