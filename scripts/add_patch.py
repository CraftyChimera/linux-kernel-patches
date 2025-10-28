#!/usr/bin/env python3
import argparse
import sys
from datetime import datetime
from pathlib import Path

FIELDS = [
    ("status", "Under Review / Accepted / Rejected / RFC"),
    ("patch_commit", ""),
    ("regression_commit", ""),
    ("subsystem", ""),
    ("title", ""),
    ("dashboard_url", ""),
    ("discussion_url", ""),
    ("backported", "yes/no") 
]

DEFAULT_FIELDS = {"status", "patch_commit", "subsystem", "title", "discussion_url"}
BUG_FIX_FIELDS = set([key for key, _ in FIELDS])

allowed_fields = [ 
    DEFAULT_FIELDS, 
    BUG_FIX_FIELDS,
    BUG_FIX_FIELDS,
    DEFAULT_FIELDS,
    DEFAULT_FIELDS,
    DEFAULT_FIELDS,
    DEFAULT_FIELDS,
    DEFAULT_FIELDS
]

LOREM = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."

def build_content(patch_type):
    lines = []
    lines.append("### Patch Info\n")
    lines.append("| Property | Value |")
    lines.append("|-------|--------|")
    for key, val in FIELDS:
        if key in allowed_fields[patch_type - 1]:
            lines.append(f"| **{key}** | {val} |")
    lines.append("\n### Summary\n")
    lines.append(LOREM)
    lines.append("")
    return "\n".join(lines)

def main():
    p = argparse.ArgumentParser(description='Generate a patch-note file for quick reviewer consumption.')
    for key, helptext in FIELDS:
        p.add_argument(f"--{key}", help=helptext)
    p.add_argument("--output", "-o", default="patch_note", help="Output filename (default: patch_note.md)")
    p.add_argument("--patch_type", "-type", default = 8, help="weight attached to the patch depending on the type")
    p.add_argument("--yes", "-y", action="store_true", help="Don't prompt; use empty values for missing fields.")
    
    args = p.parse_args()
    patch_type = int(args.patch_type)

    if patch_type > 8 or patch_type < 1:
        print("Invalid patch type")
        sys.exit(2)

    content = build_content(patch_type)
    repo_root = f"{Path(__file__).resolve().parent}/.."

    start_char = f"{patch_type}"
    match = next((p for p in Path(f"{repo_root}/patches").iterdir() if p.is_dir() and p.name.startswith(start_char)), None)
    if match:
        print(f"Found directory: {match}")
    else:
        print("No matching directory found.")
        sys.exit(2)

    out = f"{match}/{args.output}.md"

    try:
        with open(out, 'w', encoding='utf-8') as f:
            f.write(content)
    except Exception as e:
        print(f"Failed to write {out}: {e}", file=sys.stderr)
        sys.exit(2)
    
    print(f"Patch Type: {patch_type}")
    print(f"Wrote: {out}\n\n--- file content ---\n")
    print(content)

if __name__ == '__main__':
    main()
