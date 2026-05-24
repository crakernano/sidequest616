#!/usr/bin/env python3
import os
import sys
import yaml
import requests


def load_template(path):
    text = open(path, encoding="utf-8").read()
    if text.startswith("---"):
        parts = text.split("---", 2)
        if len(parts) >= 3:
            meta = yaml.safe_load(parts[1]) or {}
            body = parts[2].strip()
            return meta, body
    # fallback: no frontmatter
    return {}, text


def issue_exists(repo, headers, title):
    url = f"https://api.github.com/repos/{repo}/issues"
    page = 1
    while True:
        params = {"state": "all", "per_page": 100, "page": page}
        r = requests.get(url, headers=headers, params=params)
        r.raise_for_status()
        items = r.json()
        if not items:
            return False
        for it in items:
            if it.get("title") == title:
                return True
        page += 1


def main():
    repo = os.environ.get("GITHUB_REPOSITORY") or os.environ.get("REPO")
    # Accept either the automatic GITHUB_TOKEN or a custom CI token (e.g. secrets.CI_TOKEN)
    token = os.environ.get("GITHUB_TOKEN") or os.environ.get("CI_TOKEN") or os.environ.get("TOKEN")
    if not repo or not token:
        print("GITHUB_REPOSITORY and GITHUB_TOKEN must be set in the environment.")
        sys.exit(1)

    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github+json",
    }

    templates_dir = os.path.join(".github", "ISSUE_TEMPLATE")
    if not os.path.isdir(templates_dir):
        print(f"Templates directory not found: {templates_dir}")
        sys.exit(1)

    for fname in sorted(os.listdir(templates_dir)):
        if not fname.endswith('.md'):
            continue
        path = os.path.join(templates_dir, fname)
        meta, body = load_template(path)
        title = meta.get('title') or meta.get('name') or fname
        labels = [l.strip() for l in meta.get('labels', '').split(',')] if isinstance(meta.get('labels'), str) else meta.get('labels') or []
        assignees = meta.get('assignees') or []

        print(f"Processing template: {fname} -> {title}")

        if issue_exists(repo, headers, title):
            print(f"Issue already exists: {title}")
            continue

        payload = {"title": title, "body": body, "labels": labels}
        if assignees:
            payload['assignees'] = assignees

        url = f"https://api.github.com/repos/{repo}/issues"
        r = requests.post(url, json=payload, headers=headers)
        if r.status_code in (200, 201):
            print(f"Created issue: {r.json().get('html_url')}")
        else:
            print(f"Failed to create issue {title}: {r.status_code} {r.text}")


if __name__ == '__main__':
    main()
