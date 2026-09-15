#!/usr/bin/env python3
"""Write honest not-yet-translated stubs for about, editorial policy, and events."""

from i18n_chrome import UI, render_page, stub_content, write_page

STUBS = {
    "about": {
        "page": "/about/",
        "en": "/about/",
        "active": "project",
        "title": {
            "es": "Acerca de WikiPsilocybin",
            "fr": "À propos de WikiPsilocybin",
            "de": "Über WikiPsilocybin",
            "pt": "Sobre o WikiPsilocybin",
        },
        "description": {
            "es": "Quién edita WikiPsilocybin. Esta página aún no está traducida; la versión en inglés es la fuente de referencia.",
            "fr": "Qui édite WikiPsilocybin. Cette page n'est pas encore traduite ; la version anglaise est la source de référence.",
            "de": "Wer WikiPsilocybin herausgibt. Diese Seite ist noch nicht übersetzt; die englische Fassung ist die verbindliche Quelle.",
            "pt": "Quem edita o WikiPsilocybin. Esta página ainda não está traduzida; a versão em inglês é a fonte de referência.",
        },
    },
    "policy": {
        "page": "/editorial-policy/",
        "en": "/editorial-policy/",
        "active": "project",
        "title": {
            "es": "Política editorial",
            "fr": "Politique éditoriale",
            "de": "Redaktionsrichtlinie",
            "pt": "Política editorial",
        },
        "description": {
            "es": "Normas de redacción de WikiPsilocybin. Esta página aún no está traducida; la versión en inglés es la fuente de referencia.",
            "fr": "Normes éditoriales de WikiPsilocybin. Cette page n'est pas encore traduite ; la version anglaise est la source de référence.",
            "de": "Redaktionsstandards von WikiPsilocybin. Diese Seite ist noch nicht übersetzt; die englische Fassung ist die verbindliche Quelle.",
            "pt": "Normas editoriais do WikiPsilocybin. Esta página ainda não está traduzida; a versão em inglês é a fonte de referência.",
        },
    },
    "events": {
        "page": "/events/",
        "en": "/events/",
        "active": "events",
        "title": {
            "es": "Acontecimientos recientes",
            "fr": "Événements récents",
            "de": "Aktuelle Ereignisse",
            "pt": "Acontecimentos recentes",
        },
        "description": {
            "es": "Investigación, política y cultura en torno a la psilocibina. El listado de acontecimientos sigue en inglés.",
            "fr": "Recherche, politique et culture autour de la psilocybine. La liste des événements reste en anglais.",
            "de": "Forschung, Politik und Kultur rund um Psilocybin. Die Ereignisliste bleibt auf Englisch.",
            "pt": "Pesquisa, política e cultura em torno da psilocibina. A lista de acontecimentos permanece em inglês.",
        },
    },
}


def main() -> None:
    for lang in ("es", "fr", "de", "pt"):
        ui = UI[lang]
        for spec in STUBS.values():
            heading = spec["title"][lang]
            html = render_page(
                lang=lang,
                page=spec["page"],
                title=f"{heading} | WikiPsilocybin",
                description=spec["description"][lang],
                content=stub_content(lang, spec["en"], heading),
                active_tab=spec["active"],
                extra_nav=(spec["page"] == "/events/"),
            )
            dest = write_page(lang, spec["page"], html)
            print(f"wrote {dest}")
    print("stubs done")


if __name__ == "__main__":
    main()
