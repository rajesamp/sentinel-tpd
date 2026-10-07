"""Detect drift from the paper baseline; never score or rewrite research evidence."""
import argparse
import hashlib
import json
from pathlib import Path, PurePosixPath
import re


def check(root):
    root = root.resolve()
    baseline = json.loads((root / "docs/research-baseline.json").read_text())
    if baseline["schema_version"] != 1 or not re.fullmatch(r"[0-9a-f]{40}", baseline["evaluated_revision"]):
        raise ValueError("Invalid research baseline identity")
    entries = baseline["files"]
    expected = {item["path"] for item in entries}
    if not entries or len(expected) != len(entries):
        raise ValueError("Empty or duplicate research baseline inventory")
    actual_modules = {str(p.relative_to(root)) for p in (root / "sentinel_tpd").rglob("*.py")}
    expected_modules = {name for name in expected if name.startswith("sentinel_tpd/")}
    if actual_modules != expected_modules or not actual_modules:
        raise ValueError("Runtime module inventory changed; review paper alignment before claiming current coverage")
    for item in entries:
        path = PurePosixPath(item["path"])
        if path.is_absolute() or ".." in path.parts:
            raise ValueError("Unsafe baseline path")
        file = (root / path).resolve()
        if not file.is_relative_to(root):
            raise ValueError("Baseline path escapes repository")
        if hashlib.sha256(file.read_bytes()).hexdigest() != item["sha256"]:
            raise ValueError("Paper baseline drift: " + item["path"] + "; review and re-evaluate changed behavior")
    return {"status": "aligned", "evaluated_revision": baseline["evaluated_revision"],
            "files_verified": len(entries), "runtime_modules_verified": len(actual_modules),
            "scope": "Baseline byte alignment; not new scientific evaluation"}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    print(json.dumps(check(args.root), indent=2))
