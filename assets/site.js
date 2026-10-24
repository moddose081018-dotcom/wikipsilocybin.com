/* Typography experiment switch and privacy-preserving engagement events.
   No data leaves the page unless a consented analytics tool defines window.dataLayer.
   Event definitions: /docs/design/cro-experiment-backlog.md */
(function () {
    try {
        var params = new URLSearchParams(location.search);
        var t = params.get('type');
        if (t === 'sans' || t === 'serif') sessionStorage.setItem('wp-type', t);
        if (sessionStorage.getItem('wp-type') === 'sans') document.documentElement.classList.add('type-sans');
    } catch (e) {}

    function track(name, detail) {
        if (Array.isArray(window.dataLayer)) {
            window.dataLayer.push(Object.assign({ event: name, type_variant: document.documentElement.classList.contains('type-sans') ? 'sans' : 'serif' }, detail));
        }
    }

    document.addEventListener('click', function (e) {
        var a = e.target.closest && e.target.closest('a');
        if (!a) return;
        var href = a.getAttribute('href') || '';
        if (a.closest('sup.ref')) track('citation_open', { ref: href });
        else if (a.closest('.refs, .source-box') && /^https?:/.test(href)) track('source_outbound', { url: href });
        else if (a.closest('.site-nav, .page-tabs')) track('nav_click', { target: href });
        else if (a.closest('.toc')) track('toc_click', { target: href });
        else if (/^\/(about|editorial-policy)\//.test(href)) track('trust_page_open', { target: href });
        else if (/^mailto:/.test(href)) track('contact_intent', {});
    });

    var marks = [50, 90], sent = {};
    window.addEventListener('scroll', function () {
        var h = document.documentElement, pct = (h.scrollTop + innerHeight) / h.scrollHeight * 100;
        marks.forEach(function (m) { if (pct >= m && !sent[m]) { sent[m] = 1; track('read_depth', { percent: m }); } });
    }, { passive: true });
})();
