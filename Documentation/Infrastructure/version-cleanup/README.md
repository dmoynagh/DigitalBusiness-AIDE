# version cleanup

Deletes superseded document versions from the working tree, so a folder only
ever shows the current version of each document. Git history is the record of
what a superseded version contained — the working tree does not keep one.

The tool is `aide cleanup`, one of the utilities built into the `aide` CLI
(`aide-cli`, in the deploy repo `DigitalBusiness-AIDE-Deploy`, distributed via
`aide update`). This folder holds the design documentation for the tool, not
the tool itself — there is no standalone script to run here.

**Dry run by default.** `aide cleanup` on its own only reports what it would
delete. Nothing is removed from disk until you pass `--apply`.

---

## What it does

In each folder it visits, it looks for files whose names are identical apart
from a `_v<number>` suffix immediately before the extension. The highest number
stays put; every lower version is deleted.

| Files in a folder | Result |
| --- | --- |
| `Foo_v8.md`, `Foo_v9.md` | `Foo_v8.md` is deleted, `Foo_v9.md` stays |
| `Foo.md`, `Foo_v1.md` | `Foo.md` is deleted — no suffix counts as v0 |
| `Foo_v3.md` on its own | nothing happens |
| `Foo_v1.md`, `Foo_v2.txt` | nothing happens — extensions must match too |

Grouping is **per folder**. The walk is recursive, but `Foo_v8.md` in one folder
is never compared with `Foo_v9.md` in another. Anything more complicated than
that is a manual job.

Folders whose name starts with an underscore are skipped by default — this is
what keeps the tool out of `_binder`, `_rebuild`, and its own kind.

When a live run (`--apply`) deletes at least one file, the tool stages and
commits the deletions itself, with a message such as
`cleanup: deleted 2 superseded version(s)`. Git history is where the deleted
content lives afterwards — there is no `_superseded` folder for this tool.

---

## Running it

From anywhere inside a project (the tool walks up from the current folder to
find `_aide/`):

```
aide cleanup            # dry run — reports what would be deleted, changes nothing
aide cleanup --apply    # deletes the files and commits the deletion
```

The dry run produces exactly the same report as a live run, with `WOULD
DELETE` in place of `DELETED`. It is the safe way to check a new `root` or a
new include/exclude list before letting the tool loose on a tree.

---

## Settings

`aide cleanup` reads the `cleanup` key of the project's per-project runtime
settings file, `_aide/settings.json` — not a settings file of its own, and not
from wherever the terminal happens to be pointing:

```json
{
  "cleanup": {
    "root": "..",
    "include": [],
    "exclude": [],
    "log_file": "~/_aide/utilities/version-cleanup/version_cleanup.log"
  }
}
```

Anything left out falls back to the package default shipped with `aide-cli`
(`root`: the project root; `include`/`exclude`: empty; `log_file`: the path
above).

| Setting | Meaning |
| --- | --- |
| `root` | The folder to tidy, including everything beneath it. Defaults to the project root (where `_aide/` lives). |
| `include` | Underscore-prefixed folders to process anyway. |
| `exclude` | Folders to skip entirely, along with everything inside them. |
| `log_file` | Where the run log is appended. |

**`root` and `log_file`** take a full path, or a `~/` path measured from the
project root. `include` and `exclude` take three kinds of path:

| Form | Example | Means |
| --- | --- | --- |
| Absolute | `"C:/Docs/_binder"` | that one exact folder |
| Root-anchored | `"~/_binder"` | that one exact folder, measured from `root` |
| Relative | `"_binder"` | a **pattern**: every folder in the tree whose path ends with those segments |

The relative form is the useful one for a corpus. `"_binder"` is not a place,
it is a shape — it matches a `_binder` subfolder wherever one appears, at
any depth. Several segments work too: `"_binder/current"` matches any
`.../_binder/current`.

Two consequences worth holding on to:

- `"~"` here means **the root of the tree being tidied**, never your home
  folder. The tool never expands `~` the way a shell would.
- A relative entry in `exclude` is powerful in the same way. `"_superseded"`
  would skip every `_superseded` folder in the tree, not one of them.

**Writing paths in JSON.** Use forward slashes (`"C:/Users/you/Documents"`) or
doubled backslashes (`"C:\\Users\\you"`); a single backslash is an escape
character in JSON and will break the file.

**Exclude always wins over include**, and excluding a folder excludes
everything inside it.

To reach a folder nested inside an underscore-prefixed one, just name the
folder you actually want — the walk passes through the underscore folder to
get there without processing its own files.

Example: process every `_binder` in the tree, plus one `_holding` folder at
the top, and stay out of one scratch area entirely.

```json
{
  "cleanup": {
    "root": "..",
    "include": ["_binder", "~/_holding"],
    "exclude": ["~/Working Practices/scratch"]
  }
}
```

The run report echoes the include and exclude lists whenever they are in use,
so a log entry always says which rules produced it.

This is the same path model as the binder builder, deliberately. Two
Infrastructure tools with different path semantics would be a trap.

---

## The log

Every run appends one entry to the log file, live and dry-run alike, each
stamped with the date, the mode and the root it was pointed at. By default the
log lands at `_aide/utilities/version-cleanup/version_cleanup.log`. The log is
never rewritten or trimmed. If it grows unwieldy, archive or delete it by hand;
the tool will start a fresh one.

---

## When it declines to act

One case where the tool deliberately does nothing to a group of files and
tells you instead:

- **`AMBIGUOUS`** — two files in the folder claim the same version number,
  which can only happen through leading zeros (`Foo_v08.md` and `Foo_v8.md`).
  Nothing in that group is deleted, because which one is current is genuinely
  unclear.

A file that fails to delete because of a filesystem error (locked, permission
denied) is reported as `ERROR` and left in place.

---

## Scope

It tidies versions. It does not build binders and it does not deploy anything.
Those are `aide binder` and `aide fup`, run in sequence.
