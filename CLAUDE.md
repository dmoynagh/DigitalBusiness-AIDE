# DigitalBusiness-AIDE — documentation repo

Repo-specific facts and rules. The AIDE standards (DocMeth, WP, PD and the rest) govern the content
itself; this file does not restate them. Write in plain language, with meaning before codes.

## Where things are

- `Documentation/` — the AIDE framework masters, one folder per component. The project root for
  the `aide` CLI (it holds `_aide/`); run `aide` commands from here.
- `Documentation/AIDE_Documentation_WIP_vN.md` — the working state: active threads, open items,
  the build-owed list, the cross-review register, the standards dependency map. Check it first.
- `Documentation/_rebuild/` — the rebuild's working documents (settled decisions, rebuild WIP).
- `Documentation/_tools/` — working scripts not yet promoted to utilities (e.g. `dependency_map.py`).
- `Documentation_old/` — the retired pre-rebuild corpus. Read-only source material; never edit.

## Versioning

- The Declaration line's `identity: Name@vN` is authoritative. The filename mirrors it (`Name_vN.md`).
- A new version is a rename to `_vN+1` (`git mv`), the identity line updated to match, and a
  version note added. Keep the two in step in the same commit.
- Draft markers follow DocMeth: `@vN-draftM` / `_vN-draftM`; publishing drops the marker.
- Git is the archive. Never create `_superseded` folders or archive copies. The old version is
  gone from the tree once renamed; it lives in git history.

## `uses` entries

- A `uses` entry's version is a conformance stamp: the version of that standard this document was
  last brought into line with. It is the change-management trigger — never drop it.
- Stamped version older than current = **behind**. A normal state, not a defect; bring it into
  line when the document is next worked. Only an identity that doesn't exist is **broken**.
- `python _tools/dependency_map.py .` (from `Documentation/`) reports every entry's state.

## Design produces the standard

Change the design first, record new choices as decisions (numbered, with the reasoning), mark a
decision revised or superseded by the new one, then produce the standard from the design.

## Commit discipline

- Stage only your own files, by explicit path. Never `git add -A` or `git commit -a`.
- After committing, run `git status` and confirm nothing of yours is left staged or unstaged.
- One commit per task unless told otherwise. Don't push unless asked.
- Generated run logs (`*.log`) are ignored; don't force-add them.

## Binder

- `aide binder` (run from `Documentation/`) builds `Documentation/_binder/AIDE_Documentation_Binder_vN.md`
  and commits only its own output. Settings:
  `_aide/utilities/binder-builder/binder_builder_AIDE_Documentation_settings.json`.
- It skips underscore-prefixed folders (except `_rebuild`, included by setting) and WIP and board files.
- Rebuild after committing a change to any in-scope file. A WIP-only change needs no rebuild.
- Commit your own work first, with nothing else staged, then run the binder.

## Deploy repo

Skills, plugins, the MCP servers and the `aide` CLI live in `../DigitalBusiness-AIDE-Deploy`.
Plugin changes reach users only through a merged PR there — a change here is not deployed until
then. Rebuilds owed after a standard changes go on the WIP build-owed list.
