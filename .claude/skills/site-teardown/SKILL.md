---
name: site-teardown
description: Run an outside-in "Live Site Teardown" SEO + AI-visibility audit on any domain and publish it as a client-ready report (17 sections, priority tags, 90-day roadmap). Use when asked to audit, tear down, or report on a website we manage or a client/prospect site. Args - the domain, plus optional market/country and any owner-supplied data (GSC, analytics, AI-impression screenshots).
---

# Site Teardown

Produces a plain-English report explaining what is happening with a site: where it shows up (Google + AI answers), why it isn't getting clicks, what is broken, and a costed 90-day plan. Modelled on the "Live Site Teardown" format.

## Inputs
- `domain` (required)
- `country` (default: the site's main market; ask if unclear)
- Optional owner data: Search Console, analytics, CMS access, AI-impression screenshots. If absent, state the audit is outside-in.

## 1. Collect data (record date + source for every number)
| Need | Tool |
|---|---|
| DR, traffic, keywords, top pages, competitors | Ahrefs `site-explorer-metrics`, `-organic-keywords`, `-top-pages`, `-organic-competitors` |
| Head/"money" queries + volumes | Ahrefs `keywords-explorer-overview` / `-matching-terms` |
| Who ranks + AI Overview presence | Ahrefs `serp-overview` (or DataForSEO `serp_organic_live_advanced`) |
| AI citations (ChatGPT, Perplexity, AIO…) | Ahrefs `site-explorer-ai-responses-count`, `brand-radar-*`; DataForSEO `ai_opt_llm_ment_*` |
| Backlinks, referring domains, spam | Ahrefs `site-explorer-referring-domains`; DataForSEO `backlinks_bulk_spam_score` |
| Rendered + raw HTML of sampled pages, robots.txt, sitemaps | DataForSEO `on_page_instant_pages` / `on_page_content_parsing`; fetch robots.txt + sitemap index |
| Fact cross-check | 1–2 authoritative third-party sources for the niche |

Sample at least: home, 2 category/listing pages (incl. page 2), 5 top-traffic pages, 5 template-generated pages.

## 2. Analyses
1. **Click gap** – keywords where the site appears only inside an AI Overview / AI answer with no organic position; head queries where it is absent. Note: Ahrefs counts AIO slots as positions, so "top 3" can be inflated.
2. **Data accuracy** – sanity-check facts/specs/prices (impossible values, conflicting numbers on one page, same entity on two URLs with different data). YMYL sites: check medical/legal claims against primary sources.
3. **Index quality** – sitemap URL count vs pages with unique value; thin variants, paginated pages being cited instead of page 1, noindex/canonical conflicts.
4. **Cannibalisation** – which URL ranks/gets cited per query vs which should; overlapping posts/templates.
5. **Click layer** – first screen: does the page answer the query (table, price, verdict) or show ads/fluff first? Titles/snippets worth clicking?
6. **Entity** – is the brand name distinctive; consistent About/Organization schema; sameAs social profiles; authors/E-E-A-T.
7. **Links** – real vs spam referring domains; best genuine links; anything toxic.
8. **What's fine** – list what is working so the report is balanced.

## 3. Report structure (sections 00–16)
00 Summary · 01 Verdict · 02 Measurement scope & limits · 03 The numbers · 04 Click gap · 05 Data accuracy · 06 Index quality · 07 Cannibalisation · 08 Click layer · 09 Entity · 10 Links · 11 What's fine · 12 Questions for the owner · 13 90-day roadmap · 14 FAQ · 15 Jargon glossary · 16 Sources

Every finding includes:
- **Priority tag**: Critical / High / Foundation / Operator / Advanced
- **Evidence**: exact URL(s), number, source, date
- **Takeaway** labelled **RULE** (applies to any site) or **OBSERVATION** (this site only), plus a **10-minute check** the owner can do themselves

## 4. Roadmap (default ~100 hours, three gates)
- **Days 1–30 – Clean & cut**: one source of truth per entity, sanity-check script, 301 duplicates, noindex thin variants, answer on page 1, ads off the first screen.
- **Days 31–60 – Brand**: digital PR / data stories, consistent entity description, linked socials, ~30 genuine links.
- **Days 61–90 – Test & scale**: one scoped template test (~40 pages), judged on impressions *and* clicks.
Each gate has a pass/fail metric before moving on. Include **"What not to buy"** (link packages, DR boosting, page sprawl, reports that treat AI impressions as the KPI).

## 5. Rules
- Never invent numbers; every figure cites tool + date. Mark estimates as directional and note small denominators.
- Flag data that doesn't reconcile (e.g. AI platform splits not summing to the total) instead of hiding it.
- Write for a non-SEO business owner: short sentences, glossary for jargon.
- Name third parties factually; do not impersonate other agencies' branding.

## 6. Output
Publish as an HTML Artifact (title: "<Domain> Site Teardown"), private by default, and give the user the link. Save the raw data pulls in the scratchpad so the numbers can be re-checked.
