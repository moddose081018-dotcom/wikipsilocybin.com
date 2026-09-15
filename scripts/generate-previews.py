#!/usr/bin/env python3
"""Build assets/previews.json from every live index.html.

Usage (from the repo root):

    python3 scripts/generate-previews.py

For each page the script records:
  title   - h1.page-title, falling back to <title>
  extract - meta description, falling back to the first meaningful paragraph
  image   - first infobox image, if any

Add a new page, then rerun this script so hover cards stay in sync.
Cloudflare Pages deploys the committed JSON as a static file; there is no
build step on the host.
"""

from __future__ import annotations

import json
import re
from html import unescape
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "assets" / "previews.json"
SKIP_DIRS = {".git", "assets", "scripts"}


def strip_tags(html: str) -> str:
    text = re.sub(r"<script[\s\S]*?</script>", " ", html, flags=re.I)
    text = re.sub(r"<style[\s\S]*?</style>", " ", text, flags=re.I)
    text = re.sub(r"<[^>]+>", " ", text)
    text = unescape(text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def attr(html: str, name: str) -> str:
    match = re.search(rf'''{name}=(?P<q>["'])(?P<val>.*?)(?P=q)''', html, flags=re.I | re.S)
    return unescape(match.group("val")) if match else ""


def first(html: str, pattern: str) -> str:
    match = re.search(pattern, html, flags=re.I | re.S)
    return match.group(1).strip() if match else ""


def page_path(rel: Path) -> str:
    parts = rel.parts
    if parts[-1] != "index.html":
        return ""
    if len(parts) == 1:
        return "/"
    return "/" + "/".join(parts[:-1]) + "/"


def extract_page(html: str) -> dict:
    title = strip_tags(first(html, r'<h1[^>]*class="[^"]*page-title[^"]*"[^>]*>([\s\S]*?)</h1>'))
    if not title:
        title = strip_tags(first(html, r"<title>([\s\S]*?)</title>"))
        title = re.sub(r"\s+[—\-].*$", "", title).strip()

    extract = attr(
        first(html, r'(<meta[^>]+name=["\']description["\'][^>]*>)') or "",
        "content",
    )
    if not extract:
        for para in re.findall(r"<p\b([^>]*)>([\s\S]*?)</p>", html, flags=re.I):
            attrs, body = para
            if "page-subtitle" in attrs or "hatnote" in attrs:
                continue
            text = strip_tags(body)
            if len(text) >= 40:
                extract = text
                break

    image = attr(
        first(html, r'<div class="infobox-image">[\s\S]*?<img\b([^>]+)>') or "",
        "src",
    )

    item = {"title": title, "extract": extract}
    if image:
        item["image"] = image
    return item


def main() -> None:
    pages = {}
    for path in sorted(ROOT.rglob("index.html")):
        rel = path.relative_to(ROOT)
        if rel.parts and rel.parts[0] in SKIP_DIRS:
            continue
        url = page_path(rel)
        if not url:
            continue
        pages[url] = extract_page(path.read_text(encoding="utf-8"))

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(
        json.dumps(pages, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(f"Wrote {len(pages)} previews to {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
