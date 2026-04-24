#!/usr/bin/env python3
import argparse
import json
import sys
import textwrap
import urllib.request
from pathlib import Path


def fetch_latest_release(repo: str) -> dict:
    url = f"https://api.github.com/repos/{repo}/releases/latest"
    request = urllib.request.Request(
        url,
        headers={
            "Accept": "application/vnd.github+json",
            "User-Agent": "openclaw-mastery-curriculum",
        },
    )
    with urllib.request.urlopen(request, timeout=30) as response:
        return json.load(response)


def build_issue_body(state: dict, latest: dict) -> str:
    tracked_tag = state["last_reviewed_release"]
    latest_tag = latest["tag_name"]
    surfaces = "\n".join(f"- `{item}`" for item in state.get("review_surfaces", []))
    lines = [
        "# OpenClaw upstream review required",
        "",
        f"The curriculum baseline is currently reviewed through **{tracked_tag}**, but upstream has moved to **{latest_tag}**.",
        "",
        "## Upstream release",
        "",
        f"- Repository: `{state['tracked_repo']}`",
        f"- Latest release: [{latest_tag}]({latest['html_url']})",
        f"- Published at: `{latest['published_at']}`",
        "",
        "## Current curriculum baseline",
        "",
        f"- Last reviewed release: `{tracked_tag}`",
        f"- Last reviewed date: `{state['last_reviewed_date']}`",
        "",
        "## Required maintainer review",
        "",
        "Check these curriculum surfaces first:",
        "",
        surfaces,
        "",
        "## Review checklist",
        "",
        "- [ ] Read the upstream release note in full",
        "- [ ] Classify the change type: provider, security, install/deploy, automation, plugin/ecosystem, contributor workflow, or docs-only",
        "- [ ] Update only the affected curriculum files",
        "- [ ] Keep stable-vs-preview labeling correct",
        "- [ ] Update `curriculum/maintenance/review-log.md`",
        "- [ ] Update `curriculum/maintenance/upstream-state.json`",
        "- [ ] Decide whether a new validation pass is required",
        "",
        "## Quality rule",
        "",
        "This issue is generated automatically for detection only. Curriculum wording should **not** be changed blindly. Detection is automated; quality judgment remains explicit.",
    ]
    return "\n".join(lines).strip() + "\n"


def write_outputs(path: str, data: dict) -> None:
    with open(path, "a", encoding="utf-8") as handle:
        for key, value in data.items():
            handle.write(f"{key}={value}\n")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--state", required=True)
    parser.add_argument("--issue-body", required=True)
    parser.add_argument("--outputs")
    args = parser.parse_args()

    state_path = Path(args.state)
    state = json.loads(state_path.read_text(encoding="utf-8"))
    latest = fetch_latest_release(state["tracked_repo"])

    drift = latest["tag_name"] != state["last_reviewed_release"]
    Path(args.issue_body).write_text(build_issue_body(state, latest), encoding="utf-8")

    outputs = {
        "drift": "true" if drift else "false",
        "latest_tag": latest["tag_name"],
        "latest_url": latest["html_url"],
        "latest_published_at": latest["published_at"],
        "baseline_tag": state["last_reviewed_release"],
    }
    if args.outputs:
        write_outputs(args.outputs, outputs)
    else:
        print(json.dumps(outputs, indent=2))

    return 0


if __name__ == "__main__":
    sys.exit(main())
