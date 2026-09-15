(function () {
    'use strict';

    var LANGS = [
        { code: 'en', name: 'English', native: 'English' },
        { code: 'es', name: 'Spanish', native: 'Español' },
        { code: 'fr', name: 'French', native: 'Français' },
        { code: 'de', name: 'German', native: 'Deutsch' },
        { code: 'pt', name: 'Portuguese', native: 'Português' }
    ];

    var TRANSLATED = {
        '/': true,
        '/are-magic-mushrooms-dangerous/': true,
        '/are-shrooms-addictive/': true,
        '/about/': true,
        '/editorial-policy/': true,
        '/events/': true
    };

    var UI = {
        en: { languages: '5 languages', untranslated: 'Some pages are still English only.' },
        es: { languages: '5 idiomas', untranslated: 'Algunas páginas siguen solo en inglés.' },
        fr: { languages: '5 langues', untranslated: 'Certaines pages restent en anglais uniquement.' },
        de: { languages: '5 Sprachen', untranslated: 'Einige Seiten gibt es weiterhin nur auf Englisch.' },
        pt: { languages: '5 idiomas', untranslated: 'Algumas páginas ainda existem só em inglês.' }
    };

    function normalizePath(pathname) {
        if (!pathname) return '/';
        var path = pathname.split('#')[0].split('?')[0];
        if (path.length > 1 && path.charAt(path.length - 1) !== '/') path += '/';
        return path || '/';
    }

    function detectLang(pathname) {
        var match = pathname.match(/^\/(es|fr|de|pt)(\/|$)/);
        return match ? match[1] : 'en';
    }

    function pageKey(pathname) {
        var path = normalizePath(pathname);
        var stripped = path.replace(/^\/(es|fr|de|pt)(?=\/|$)/, '');
        return normalizePath(stripped || '/');
    }

    function langPrefix(code) {
        return code === 'en' ? '' : '/' + code;
    }

    function targetForLang(code, key) {
        var dest = key;
        if (!TRANSLATED[key]) {
            if (key.indexOf('/events/') === 0) dest = code === 'en' ? key : '/events/';
            else dest = '/';
        }
        if (dest === '/') return langPrefix(code) + '/';
        return langPrefix(code) + dest;
    }

    function currentLang() {
        return document.documentElement.getAttribute('data-lang') ||
            detectLang(normalizePath(location.pathname));
    }

    function currentKey() {
        return document.documentElement.getAttribute('data-page') ||
            pageKey(location.pathname);
    }

    function wrapNav() {
        var inner = document.querySelector('.site-top-inner');
        if (!inner || inner.querySelector('.site-tools')) return;
        var nav = inner.querySelector('.site-nav');
        var tools = document.createElement('div');
        tools.className = 'site-tools';
        if (nav) tools.appendChild(nav);
        var host = document.createElement('div');
        host.id = 'lang-switcher-root';
        tools.appendChild(host);
        inner.appendChild(tools);
    }

    function buildLanguageSwitcher() {
        wrapNav();
        var host = document.getElementById('lang-switcher-root');
        if (!host) return;

        var lang = currentLang();
        var key = currentKey();
        var strings = UI[lang] || UI.en;
        var fullyTranslated = !!TRANSLATED[key];

        var nav = document.createElement('nav');
        nav.className = 'lang-switcher';
        nav.setAttribute('aria-label', strings.languages);

        var btn = document.createElement('button');
        btn.type = 'button';
        btn.className = 'lang-switcher-btn';
        btn.id = 'lang-switcher-btn';
        btn.setAttribute('aria-expanded', 'false');
        btn.setAttribute('aria-controls', 'lang-switcher-menu');
        btn.textContent = strings.languages;

        var menu = document.createElement('ul');
        menu.className = 'lang-switcher-menu';
        menu.id = 'lang-switcher-menu';

        LANGS.forEach(function (item) {
            var li = document.createElement('li');
            var a = document.createElement('a');
            a.href = targetForLang(item.code, key);
            a.lang = item.code;
            a.hreflang = item.code;
            a.textContent = item.native;
            if (item.code === lang) a.setAttribute('aria-current', 'page');
            li.appendChild(a);
            menu.appendChild(li);
        });

        if (!fullyTranslated) {
            var note = document.createElement('li');
            note.className = 'lang-switcher-note';
            note.textContent = strings.untranslated;
            menu.appendChild(note);
        }

        function setOpen(open) {
            btn.setAttribute('aria-expanded', open ? 'true' : 'false');
            if (open) menu.classList.add('open');
            else menu.classList.remove('open');
        }

        btn.addEventListener('click', function (e) {
            e.stopPropagation();
            setOpen(btn.getAttribute('aria-expanded') !== 'true');
        });

        document.addEventListener('click', function () { setOpen(false); });
        document.addEventListener('keydown', function (e) {
            if (e.key === 'Escape') {
                setOpen(false);
                btn.focus();
            }
        });

        nav.appendChild(btn);
        nav.appendChild(menu);
        host.appendChild(nav);
    }

    var lastTouchAt = 0;
    document.addEventListener('touchstart', function () {
        lastTouchAt = Date.now();
    }, true);

    function isEmulatedTouchMouse() {
        return Date.now() - lastTouchAt < 600;
    }

    function lookupPreview(map, pathname) {
        var path = normalizePath(pathname);
        if (map[path]) return map[path];
        if (path.length > 1 && map[path.slice(0, -1)]) return map[path.slice(0, -1)];
        return null;
    }

    function isPreviewableLink(link) {
        if (!link || !link.getAttribute) return false;
        var raw = link.getAttribute('href');
        if (!raw || raw.charAt(0) === '#' || raw.indexOf('mailto:') === 0 || raw.indexOf('javascript:') === 0) {
            return false;
        }
        var url;
        try { url = new URL(link.href, location.origin); } catch (e) { return false; }
        if (url.origin !== location.origin) return false;
        if (url.hash && normalizePath(url.pathname) === normalizePath(location.pathname)) return false;
        return true;
    }

    function placeCard(card, link) {
        var rect = link.getBoundingClientRect();
        var scrollY = window.pageYOffset || document.documentElement.scrollTop;
        var scrollX = window.pageXOffset || document.documentElement.scrollLeft;
        var width = card.offsetWidth || 320;
        var top = rect.bottom + scrollY + 8;
        var left = rect.left + scrollX;
        var viewW = document.documentElement.clientWidth;
        if (left + width > viewW - 8) left = viewW - width - 8;
        if (left < 8) left = 8;
        var cardH = card.offsetHeight || 0;
        if (rect.bottom + cardH + 16 > window.innerHeight && rect.top > cardH + 16) {
            top = rect.top + scrollY - cardH - 8;
        }
        card.style.top = top + 'px';
        card.style.left = left + 'px';
    }

    function initPreviews(map) {
        var card = document.createElement('div');
        card.className = 'wp-preview';
        card.id = 'wp-preview';
        card.setAttribute('role', 'tooltip');
        card.setAttribute('hidden', '');
        card.innerHTML =
            '<img class="wp-preview-img" id="wp-preview-img" alt="">' +
            '<div class="wp-preview-body">' +
            '<div class="wp-preview-title" id="wp-preview-title"></div>' +
            '<div class="wp-preview-text" id="wp-preview-text"></div>' +
            '</div>';
        document.body.appendChild(card);

        var cardImg = card.querySelector('.wp-preview-img');
        var cardTitle = card.querySelector('.wp-preview-title');
        var cardText = card.querySelector('.wp-preview-text');
        var showTimer = null;
        var hideTimer = null;
        var activeLink = null;

        function hideCard() {
            card.classList.remove('visible');
            card.setAttribute('hidden', '');
            if (activeLink) {
                activeLink.removeAttribute('aria-describedby');
                activeLink = null;
            }
        }

        function showCard(link, data) {
            if (data.image) {
                cardImg.src = data.image;
                cardImg.alt = data.title || '';
                cardImg.style.display = 'block';
            } else {
                cardImg.removeAttribute('src');
                cardImg.style.display = 'none';
            }
            cardTitle.textContent = data.title || '';
            cardText.textContent = data.extract || '';
            card.removeAttribute('hidden');
            card.classList.add('visible');
            activeLink = link;
            link.setAttribute('aria-describedby', 'wp-preview');
            placeCard(card, link);
        }

        function scheduleShow(link) {
            if (!isPreviewableLink(link)) return;
            var data = lookupPreview(map, new URL(link.href, location.origin).pathname);
            if (!data) return;
            clearTimeout(hideTimer);
            clearTimeout(showTimer);
            showTimer = setTimeout(function () { showCard(link, data); }, 250);
        }

        function scheduleHide() {
            clearTimeout(showTimer);
            hideTimer = setTimeout(hideCard, 180);
        }

        document.addEventListener('mouseover', function (e) {
            if (isEmulatedTouchMouse()) return;
            var link = e.target.closest && e.target.closest('a[href]');
            if (link) scheduleShow(link);
        });
        document.addEventListener('mouseout', function (e) {
            var link = e.target.closest && e.target.closest('a[href]');
            if (!link) return;
            var to = e.relatedTarget;
            if (to && (card.contains(to) || link.contains(to))) return;
            scheduleHide();
        });
        card.addEventListener('mouseover', function () { clearTimeout(hideTimer); });
        card.addEventListener('mouseout', function (e) {
            if (e.relatedTarget && card.contains(e.relatedTarget)) return;
            scheduleHide();
        });

        document.addEventListener('focusin', function (e) {
            var link = e.target.closest && e.target.closest('a[href]');
            if (link) scheduleShow(link);
        });
        document.addEventListener('focusout', function (e) {
            var link = e.target.closest && e.target.closest('a[href]');
            if (link) scheduleHide();
        });
        document.addEventListener('keydown', function (e) {
            if (e.key === 'Escape') hideCard();
        });
        document.addEventListener('click', function () {
            hideCard();
        }, true);
    }

    function loadPreviews() {
        fetch('/assets/previews.json', { credentials: 'same-origin' })
            .then(function (res) { return res.ok ? res.json() : {}; })
            .then(initPreviews)
            .catch(function () { initPreviews({}); });
    }

    function ready(fn) {
        if (document.readyState === 'loading') {
            document.addEventListener('DOMContentLoaded', fn);
        } else {
            fn();
        }
    }

    ready(function () {
        buildLanguageSwitcher();
        loadPreviews();
    });
})();
