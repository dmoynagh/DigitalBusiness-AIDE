"""Regenerate the Standards Dependency Map (AIDE_Documentation_WIP) from
the `uses:` field of each master document's Declaration header.

Parses the Declaration line (`> identity: ... | doctype: ... | uses: ...`)
of every .md file under the Documentation root, except high-churn or
non-master folders (_binder, _superseded, _rebuild, _temp,
_fileupdatepackages, Boards, FileOps, _archived, and _index.md files).

For each doctype: standard document that declares `uses`, classifies each
entry against the corpus. The version in a `uses` entry is a conformance
stamp — the version of that standard the document was last brought into
line with — so an older stamp is a normal state, not a defect:

  current  — the identity exists and the stamp is its current version
  behind   — the identity exists and the stamp is older than current
             ("stamped vN, current vM"); the standard's migration record
             says what work applies
  broken   — the identity does not exist (or the stamped version is newer
             than any that exists)

An entry with no version stamp is reported as "unstamped": the identity
resolves, but there is nothing to compare, so currency is unknown.

Usage:
    python _tools/dependency_map.py [root]

`root` defaults to the current directory. Run from `Documentation/`:
    python _tools/dependency_map.py .

Output: four sections to stdout (UTF-8) —
  1. each standard's `uses` entries with their state
  2. every standard found, for cross-check against the corpus
  3. a tiered rendering (tier = 1 + max tier of its resolved dependencies,
     0 for no declared uses) suitable for pasting into the WIP's
     Standards Dependency Map section
  4. a count of entries in each state.
"""
import os
import sys

ROOT = sys.argv[1] if len(sys.argv) > 1 else "."
EXCLUDE_DIRS = {"_superseded", "_rebuild", "_temp", "_fileupdatepackages",
                "_binder", "Boards", "FileOps", "_archived"}
UNIVERSAL = {"DocumentationMethodology_Standard"}  # exempt from `uses` declarations


def parse_declaration(line):
    """Parse a `> key: value | key: value | ...` Declaration line into a dict."""
    if not line.startswith(">"):
        return None
    fields = {}
    for part in line[1:].strip().split("|"):
        if ":" not in part:
            continue
        key, val = part.split(":", 1)
        fields[key.strip()] = val.strip()
    return fields


def find_docs(root):
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in EXCLUDE_DIRS]
        for fn in filenames:
            if fn.endswith(".md") and fn != "_index.md":
                yield os.path.join(dirpath, fn)


def load_corpus(root):
    """identity name (without @version) -> {version, doctype, uses_raw, path}."""
    docs = {}
    for path in find_docs(root):
        try:
            with open(path, encoding="utf-8") as f:
                first_line = f.readline()
        except Exception:
            continue
        fields = parse_declaration(first_line)
        if not fields or "identity" not in fields:
            continue
        identity = fields["identity"]
        name, _, ver = identity.partition("@")
        docs[name] = {
            "version": ver or None,
            "doctype": fields.get("doctype", ""),
            "uses_raw": fields.get("uses", ""),
            "path": os.path.relpath(path, root),
        }
    return docs


def split_uses(uses_raw):
    return [t.strip() for t in uses_raw.split(",") if t.strip()]


def version_number(ver):
    """`v3` -> 3; `v4-draft1` -> 4. None if the version can't be read."""
    if not ver or not ver.startswith("v"):
        return None
    num = ver[1:].split("-", 1)[0]
    return int(num) if num.isdigit() else None


def classify(target, docs):
    """Return (state, detail) for one `uses` entry.

    state is one of: current, behind, broken, unstamped.
    """
    tname, _, tver = target.partition("@")
    found = docs.get(tname)
    if found is None:
        return "broken", "no document with this identity exists"
    if not tver:
        return "unstamped", f"identity exists, no version stamp (current {found['version']})"
    if tver == found["version"]:
        return "current", found["path"]
    stamped, cur = version_number(tver), version_number(found["version"])
    if stamped is not None and cur is not None and stamped < cur:
        return "behind", f"stamped {tver}, current {found['version']}"
    return "broken", f"stamped {tver}, but only {found['version']} exists"


def annotate(target, docs):
    """`uses` entry with a trailing marker unless it is current."""
    state, detail = classify(target, docs)
    if state == "current":
        return target
    return f"{target} *{state} — {detail}*"


def compute_tiers(standards_with_uses, all_standards):
    edges = {n: [t.partition("@")[0] for t in split_uses(d["uses_raw"])]
             for n, d in standards_with_uses.items()}
    tier = {}

    def compute(name, stack=frozenset()):
        if name in tier:
            return tier[name]
        if name in stack:
            return 0  # cycle guard — should not occur
        deps = edges.get(name, [])
        m = 0
        for t in deps:
            if t in all_standards:
                m = max(m, compute(t, stack | {name}) + 1)
            else:
                m = max(m, 1)
        tier[name] = m
        return m

    for n in all_standards:
        compute(n)
    return tier


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    docs = load_corpus(ROOT)
    standards = {n: d for n, d in docs.items() if d["doctype"] == "standard"}
    standards_with_uses = {n: d for n, d in standards.items() if d["uses_raw"]}

    print("# Standards declaring `uses` (parsed from Declaration headers)\n")
    for name in sorted(standards_with_uses):
        d = standards_with_uses[name]
        self_id = f"{name}@{d['version']}" if d["version"] else name
        print(f"- {self_id}  ({d['path']})")
        for t in split_uses(d["uses_raw"]):
            state, detail = classify(t, docs)
            print(f"    uses: {t}  [{state}: {detail}]")
        print()

    print("\n# All standards found (for cross-check)\n")
    for name in sorted(standards):
        d = standards[name]
        print(f"- {name}@{d['version']}  uses={d['uses_raw'] or '(none)'}  ({d['path']})")

    print("\n\n# Tiered rendering (paste into WIP Standards Dependency Map)\n")
    tier = compute_tiers(standards_with_uses, set(standards))
    for lvl in range(max(tier.values(), default=0) + 1):
        names = sorted(n for n in standards if tier[n] == lvl)
        print("Tier 0 — no declared uses" if lvl == 0 else f"Tier {lvl}")
        for n in names:
            d = standards[n]
            star = "  *universal, exempt from uses*" if n in UNIVERSAL else ""
            uses = ", ".join(annotate(t, docs) for t in split_uses(d["uses_raw"]))
            print(f"  - {n}@{d['version']}{star}" + (f"  uses: {uses}" if uses else ""))
        print()

    counts = {}
    for d in standards_with_uses.values():
        for t in split_uses(d["uses_raw"]):
            state = classify(t, docs)[0]
            counts[state] = counts.get(state, 0) + 1
    print("# Entry states\n")
    for state in ("current", "behind", "broken", "unstamped"):
        print(f"  {state}: {counts.get(state, 0)}")


if __name__ == "__main__":
    main()
