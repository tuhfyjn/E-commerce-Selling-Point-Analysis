#!/usr/bin/env python3
from pathlib import Path
import re, sys

root = Path(__file__).resolve().parents[1]
skill = root / "SKILL.md"
errors = []

if not skill.exists():
    errors.append("SKILL.md is missing.")
else:
    text = skill.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        errors.append("SKILL.md must start with YAML frontmatter.")
    else:
        fm = m.group(1)
        fields = {}
        for line in fm.splitlines():
            if ":" in line:
                k, v = line.split(":", 1)
                fields[k.strip()] = v.strip()
        name = fields.get("name", "")
        desc = fields.get("description", "")
        if not name:
            errors.append("Frontmatter field 'name' is required.")
        elif not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name):
            errors.append("'name' must be lowercase kebab-case.")
        if not desc:
            errors.append("Frontmatter field 'description' is required.")

required_refs = [
    "references/product-truth-lock.md",
    "references/decision-friction-map.md",
    "references/purchase-reason-ladder.md",
    "references/hook-proof-pairs.md",
    "references/visual-proof-system.md",
    "references/five-frame-conversion-path.md",
    "references/consistency-and-style.md",
    "references/platform-constraint-router.md",
    "references/scoring-rubric-v1.1.md",
    "references/output-contract-v1.1.md",
]
for rel in required_refs:
    if not (root / rel).exists():
        errors.append(f"Missing referenced file: {rel}")

if errors:
    print("Skill check failed:")
    for e in errors:
        print("-", e)
    sys.exit(1)

print("Skill check passed.")
print("Version:", (root / "VERSION").read_text().strip())
print("Architecture: 8-layer Visual Conversion OS")
