#!/usr/bin/env python3
"""Write sitemap.xml for every live index.html except 404."""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ORIGIN = "https://wikipsilocybin.com"
SKIP = {".git", "assets", "scripts"}


def urls() -> list[str]:
    found = []
    for path in sorted(ROOT.rglob("index.html")):
        rel = path.relative_to(ROOT)
        if rel.parts and rel.parts[0] in SKIP:
            continue
        if len(rel.parts) == 1:
            found.append(f"{ORIGIN}/")
        else:
            found.append(f"{ORIGIN}/{'/'.join(rel.parts[:-1])}/")
    return found


def main() -> None:
    items = urls()
    body = ["<?xml version=\"1.0\" encoding=\"UTF-8\"?>", '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for url in items:
        body.append("  <url>")
        body.append(f"    <loc>{url}</loc>")
        body.append("  </url>")
    body.append("</urlset>")
    body.append("")
    dest = ROOT / "sitemap.xml"
    dest.write_text("\n".join(body), encoding="utf-8")
    print(f"Wrote {len(items)} URLs to sitemap.xml")


if __name__ == "__main__":
    main()
