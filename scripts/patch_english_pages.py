#!/usr/bin/env python3
"""Replace per-page inline CSS/preview JS with shared assets and add hreflang."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ORIGIN = "https://wikipsilocybin.com"

TRANSLATED_KEYS = {
    "/",
    "/are-magic-mushrooms-dangerous/",
    "/are-shrooms-addictive/",
    "/about/",
    "/editorial-policy/",
    "/events/",
}


def page_key(rel: Path) -> str:
    if rel.name != "index.html":
        return ""
    if len(rel.parts) == 1:
        return "/"
    return "/" + "/".join(rel.parts[:-1]) + "/"


def hreflang_block(key: str) -> str:
    lines = []
    if key in TRANSLATED_KEYS:
        mapping = {
            "en": key,
            "es": f"/es{key if key != '/' else '/'}",
            "fr": f"/fr{key if key != '/' else '/'}",
            "de": f"/de{key if key != '/' else '/'}",
            "pt": f"/pt{key if key != '/' else '/'}",
        }
        if key == "/":
            mapping = {code: (f"/{code}/" if code != "en" else "/") for code in mapping}
        for code in ("en", "es", "fr", "de", "pt"):
            lines.append(
                f'    <link rel="alternate" hreflang="{code}" href="{ORIGIN}{mapping[code]}">'
            )
        lines.append(f'    <link rel="alternate" hreflang="x-default" href="{ORIGIN}{key}">')
    else:
        lines.append(f'    <link rel="alternate" hreflang="en" href="{ORIGIN}{key}">')
        lines.append(f'    <link rel="alternate" hreflang="x-default" href="{ORIGIN}{key}">')
    return "\n".join(lines)


HEAD_ASSETS = """    <link rel="stylesheet" href="/assets/site.css">
    <link rel="stylesheet" href="/assets/previews.css">
"""


def patch(html: str, key: str) -> str:
    html = re.sub(r"<html\b[^>]*>", f'<html lang="en" data-lang="en" data-page="{key}">', html, count=1)
    html = re.sub(r"<style>[\s\S]*?</style>\s*", "", html)
    html = re.sub(
        r'\s*<div class="wp-preview"[\s\S]*?</div>\s*<script>[\s\S]*?</script>\s*',
        "\n",
        html,
        count=1,
    )
    html = re.sub(r'\s*<script src="/assets/site\.js"[^>]*>\s*</script>\s*', "\n", html)

    if 'href="/assets/site.css"' not in html:
        html = html.replace(
            "</head>",
            HEAD_ASSETS + hreflang_block(key) + "\n</head>",
            1,
        )
    else:
        if 'rel="alternate"' not in html:
            html = html.replace("</head>", hreflang_block(key) + "\n</head>", 1)

    if 'id="lang-switcher-root"' not in html:
        html = html.replace(
            '        <nav class="site-nav">',
            '        <div class="site-tools">\n        <nav class="site-nav">',
            1,
        )
        html = html.replace(
            "        </nav>\n    </div>\n</div>",
            '        </nav>\n        <div id="lang-switcher-root"></div>\n        </div>\n    </div>\n</div>',
            1,
        )

    if "</body>" in html and 'src="/assets/site.js"' not in html:
        html = html.replace("</body>", '    <script src="/assets/site.js" defer></script>\n</body>')
    return html


def main() -> None:
    count = 0
    for path in sorted(ROOT.rglob("index.html")):
        rel = path.relative_to(ROOT)
        if rel.parts and rel.parts[0] in {".git", "assets", "scripts", "es", "fr", "de", "pt"}:
            continue
        key = page_key(rel)
        if not key:
            continue
        original = path.read_text(encoding="utf-8")
        updated = patch(original, key)
        if updated != original:
            path.write_text(updated, encoding="utf-8")
            count += 1
            print(f"patched {rel}")
    print(f"updated {count} English pages")


if __name__ == "__main__":
    main()
