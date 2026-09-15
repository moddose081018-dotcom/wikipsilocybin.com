#!/usr/bin/env python3
"""Shared chrome for language-prefixed pages."""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ORIGIN = "https://wikipsilocybin.com"

LANGS = ("en", "es", "fr", "de", "pt")

UI = {
    "es": {
        "tagline": "La enciclopedia libre de la psilocibina",
        "nav_events": "Acontecimientos recientes",
        "nav_overview": "Panorama",
        "nav_research": "Investigación",
        "nav_safety": "Seguridad y riesgos",
        "nav_addiction": "Adicción",
        "nav_legal": "Situación legal",
        "nav_about": "Acerca de",
        "tab_article": "Artículo",
        "tab_events": "Acontecimientos recientes",
        "tab_project": "Página del proyecto",
        "footer_events": "Todos los acontecimientos",
        "footer_policy": "Política editorial",
        "footer_home": "Psilocibina",
        "footer_danger": "¿Son peligrosos los hongos mágicos?",
        "footer_addiction": "¿Crean adicción los hongos?",
        "footer_legal": "Situación legal",
        "disclaimer": "© 2026 WikiPsilocybin. Solo con fines educativos y de reducción de daños. Este sitio no vende ni promueve el uso de sustancias controladas y no sustituye el consejo médico.",
        "banner": "El inglés es la fuente de referencia. Esta traducción existe para facilitar el acceso y no sustituye el consejo médico.",
        "stub_title": "Aún no traducido",
        "stub_lead": "Esta página todavía no tiene una traducción completa. La versión en inglés es la fuente de referencia.",
        "stub_link": "Leer la página en inglés",
        "from_wiki": "De WikiPsilocybin, la enciclopedia libre de la psilocibina",
    },
    "fr": {
        "tagline": "L'encyclopédie libre de la psilocybine",
        "nav_events": "Événements récents",
        "nav_overview": "Aperçu",
        "nav_research": "Recherche",
        "nav_safety": "Sécurité et risques",
        "nav_addiction": "Addiction",
        "nav_legal": "Statut juridique",
        "nav_about": "À propos",
        "tab_article": "Article",
        "tab_events": "Événements récents",
        "tab_project": "Page du projet",
        "footer_events": "Tous les événements",
        "footer_policy": "Politique éditoriale",
        "footer_home": "Psilocybine",
        "footer_danger": "Les champignons magiques sont-ils dangereux ?",
        "footer_addiction": "Les champignons créent-ils une addiction ?",
        "footer_legal": "Statut juridique",
        "disclaimer": "© 2026 WikiPsilocybin. Uniquement à des fins éducatives et de réduction des risques. Ce site ne vend ni ne promeut l'usage de substances contrôlées et ne remplace pas un avis médical.",
        "banner": "L'anglais est la source de référence. Cette traduction existe pour faciliter l'accès et ne remplace pas un avis médical.",
        "stub_title": "Pas encore traduit",
        "stub_lead": "Cette page n'a pas encore de traduction complète. La version anglaise est la source de référence.",
        "stub_link": "Lire la page en anglais",
        "from_wiki": "Depuis WikiPsilocybin, l'encyclopédie libre de la psilocybine",
    },
    "de": {
        "tagline": "Die freie Psilocybin-Enzyklopädie",
        "nav_events": "Aktuelle Ereignisse",
        "nav_overview": "Überblick",
        "nav_research": "Forschung",
        "nav_safety": "Sicherheit und Risiken",
        "nav_addiction": "Abhängigkeit",
        "nav_legal": "Rechtslage",
        "nav_about": "Über uns",
        "tab_article": "Artikel",
        "tab_events": "Aktuelle Ereignisse",
        "tab_project": "Projektseite",
        "footer_events": "Alle Ereignisse",
        "footer_policy": "Redaktionsrichtlinie",
        "footer_home": "Psilocybin",
        "footer_danger": "Sind Zauberpilze gefährlich?",
        "footer_addiction": "Machen Pilze abhängig?",
        "footer_legal": "Rechtslage",
        "disclaimer": "© 2026 WikiPsilocybin. Nur zu Bildungs- und Schadensminderungszwecken. Diese Website verkauft oder bewirbt keine kontrollierten Substanzen und ersetzt keine medizinische Beratung.",
        "banner": "Englisch ist die verbindliche Quelle. Diese Übersetzung dient der Zugänglichkeit und ersetzt keine medizinische Beratung.",
        "stub_title": "Noch nicht übersetzt",
        "stub_lead": "Diese Seite hat noch keine vollständige Übersetzung. Die englische Fassung ist die verbindliche Quelle.",
        "stub_link": "Seite auf Englisch lesen",
        "from_wiki": "Aus WikiPsilocybin, der freien Psilocybin-Enzyklopädie",
    },
    "pt": {
        "tagline": "A enciclopédia livre da psilocibina",
        "nav_events": "Acontecimentos recentes",
        "nav_overview": "Visão geral",
        "nav_research": "Pesquisa",
        "nav_safety": "Segurança e riscos",
        "nav_addiction": "Dependência",
        "nav_legal": "Situação legal",
        "nav_about": "Sobre",
        "tab_article": "Artigo",
        "tab_events": "Acontecimentos recentes",
        "tab_project": "Página do projeto",
        "footer_events": "Todos os acontecimentos",
        "footer_policy": "Política editorial",
        "footer_home": "Psilocibina",
        "footer_danger": "Os cogumelos mágicos são perigosos?",
        "footer_addiction": "Os cogumelos viciam?",
        "footer_legal": "Situação legal",
        "disclaimer": "© 2026 WikiPsilocybin. Apenas para fins educativos e de redução de danos. Este site não vende nem promove o uso de substâncias controladas e não substitui aconselhamento médico.",
        "banner": "O inglês é a fonte de referência. Esta tradução existe para facilitar o acesso e não substitui aconselhamento médico.",
        "stub_title": "Ainda sem tradução",
        "stub_lead": "Esta página ainda não tem uma tradução completa. A versão em inglês é a fonte de referência.",
        "stub_link": "Ler a página em inglês",
        "from_wiki": "De WikiPsilocybin, a enciclopédia livre da psilocibina",
    },
}


def prefix(lang: str) -> str:
    return "" if lang == "en" else f"/{lang}"


def href(lang: str, path: str) -> str:
    if path.startswith("#"):
        return path
    if path.startswith("/events/") and path != "/events/":
        return path
    if path.startswith("http") or path.startswith("mailto:"):
        return path
    if path == "/":
        return prefix(lang) + "/"
    return prefix(lang) + path


def hreflang_tags(page: str) -> str:
    lines = []
    for code in LANGS:
        url = ORIGIN + (page if code == "en" else prefix(code) + (page if page != "/" else "/"))
        if page == "/" and code != "en":
            url = f"{ORIGIN}/{code}/"
        lines.append(f'    <link rel="alternate" hreflang="{code}" href="{url}">')
    en_url = ORIGIN + page
    lines.append(f'    <link rel="alternate" hreflang="x-default" href="{en_url}">')
    return "\n".join(lines)


def render_page(
    lang: str,
    page: str,
    title: str,
    description: str,
    content: str,
    active_tab: str = "article",
    extra_nav: bool = False,
) -> str:
    ui = UI[lang]
    home = href(lang, "/")
    events = href(lang, "/events/")
    safety = href(lang, "/are-magic-mushrooms-dangerous/")
    addiction = href(lang, "/are-shrooms-addictive/")
    about = href(lang, "/about/")
    policy = href(lang, "/editorial-policy/")
    overview = f"{home}#what-is"
    research = f"{home}#research"
    legal = f"{home}#legal"
    recent = f"{home}#recent-events"

    tab_article_class = ' class="active"' if active_tab == "article" else ""
    tab_events_class = ' class="active"' if active_tab == "events" else ""
    tab_project_class = ' class="active"' if active_tab == "project" else ""

    if active_tab == "project":
        tabs = (
            f'        <a href="{prefix(lang)}{page}"{tab_project_class}>{ui["tab_project"]}</a>\n'
            f'        <a href="{events}"{tab_events_class}>{ui["tab_events"]}</a>'
        )
    else:
        article_href = home if page in {"/", "/events/"} else prefix(lang) + page
        tabs = (
            f'        <a href="{article_href}"{tab_article_class}>{ui["tab_article"]}</a>\n'
            f'        <a href="{events}"{tab_events_class}>{ui["tab_events"]}</a>'
        )

    research_link = (
        f'\n            <a href="{research}">{ui["nav_research"]}</a>' if extra_nav else ""
    )

    return f"""<!DOCTYPE html>
<html lang="{lang}" data-lang="{lang}" data-page="{page}">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <meta name="description" content="{description}">
    <link rel="canonical" href="{ORIGIN}{prefix(lang)}{page if page != '/' else '/'}">
    <link rel="stylesheet" href="/assets/site.css">
    <link rel="stylesheet" href="/assets/previews.css">
{hreflang_tags(page)}
</head>
<body>
<div class="site-top">
    <div class="site-top-inner">
        <div class="site-title">
            <a href="{home}">WikiPsilocybin</a>
            <small>{ui["tagline"]}</small>
        </div>
        <div class="site-tools">
        <nav class="site-nav">
            <a href="{recent}">{ui["nav_events"]}</a>
            <a href="{overview}">{ui["nav_overview"]}</a>{research_link}
            <a href="{safety}">{ui["nav_safety"]}</a>
            <a href="{addiction}">{ui["nav_addiction"]}</a>
            <a href="{legal}">{ui["nav_legal"]}</a>
            <a href="{about}">{ui["nav_about"]}</a>
        </nav>
        <div id="lang-switcher-root"></div>
        </div>
    </div>
</div>
<div class="page-wrap">
    <div class="page-tabs">
{tabs}
    </div>
    <div class="content">
        <div class="ambox i18n"><strong>{ui["banner"]}</strong></div>
{content}
    </div>
</div>
<div class="footer">
    <div class="footer-links">
        <a href="{home}">{ui["footer_home"]}</a>
        <a href="{safety}">{ui["footer_danger"]}</a>
        <a href="{addiction}">{ui["footer_addiction"]}</a>
        <a href="{events}">{ui["footer_events"]}</a>
        <a href="{about}">{ui["nav_about"]}</a>
        <a href="{policy}">{ui["footer_policy"]}</a>
    </div>
    <p>{ui["disclaimer"]}</p>
</div>
    <script src="/assets/site.js" defer></script>
</body>
</html>
"""


def write_page(lang: str, page: str, html: str) -> Path:
    rel = page.strip("/")
    dest = ROOT / lang / (rel + "/index.html" if rel else "index.html")
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(html, encoding="utf-8")
    return dest


def stub_content(lang: str, english_url: str, heading: str) -> str:
    ui = UI[lang]
    return f"""        <h1 class="page-title">{heading}</h1>
        <p class="page-subtitle">{ui["from_wiki"]}</p>
        <p>{ui["stub_lead"]}</p>
        <p><a href="{english_url}">{ui["stub_link"]}</a></p>
"""
