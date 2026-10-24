# CRO experiment backlog

Rules: one material change per test; hypothesis, primary metric and minimum sample fixed **before** launch; no peeking-based stopping; no winners from colour preference [S16, S17, S18]. Prioritise task success, research engagement and genuine enquiries over raw clicks.

## Instrumented events (`/assets/site.js`)
Pushed to `window.dataLayer` **only if** a consented analytics tool defines it; otherwise nothing is sent. Every event carries `type_variant` (serif/sans).

| Event | Fires when | Meaning |
|---|---|---|
| `citation_open` | Inline citation clicked | Reader checks evidence |
| `source_outbound` | External link in references/source box clicked | Reader goes to primary source |
| `nav_click` | Header nav or page tab clicked | Hub navigation |
| `toc_click` | Table-of-contents link clicked | In-article navigation |
| `trust_page_open` | Link to About / Editorial policy clicked | Credibility check |
| `contact_intent` | `mailto:` link clicked | Legitimate enquiry |
| `read_depth` | 50 % / 90 % scrolled (once each) | Reading engagement |

## Backlog
| ID | Change (one only) | Hypothesis | Primary metric | Guardrails | Min. sample / duration |
|---|---|---|---|---|---|
| E0 | **Typography:** Source Serif 4 + Inter (A) vs all-Inter (B) | Font family changes reading depth on long articles; direction unknown [S12] | `read_depth` 90 % rate per article view | Time on page, bounce | Power calc for ±2 pp at 80 % power, α 0.05; ≥ 2 full weeks. Pair with a 5-user comprehension check. |
| E1 | Add "Methodology" (Editorial policy) to header nav | Makes methodology findable (usability task 5 gap) | Usability task 5 success; `trust_page_open` rate | `nav_click` to other hubs | Usability round first; then A/B if traffic allows |
| E2 | Add contact link ("Email the editor") to footer | More legitimate corrections/enquiries | `contact_intent` per 1k sessions | Spam volume | ≥ 4 weeks (low base rate) |
| E3 | Primary CTA under homepage intro: "Read the safety evidence review" (`.btn-primary`) | Clear next step increases engagement with the main research hub | Sessions reaching a guide + `read_depth` 50 % there | `citation_open` | Power calc; ≥ 2 weeks |
| E4 | Label evidence level on claims (e.g. "RCT", "Observational", "Hypothesis") | Readers can tell verified findings from hypotheses | Comprehension check: % correctly identifying evidence level | `citation_open` | Moderated test, 5–8 users |
| E5 | Mobile nav: scroll row vs "Menu" disclosure | Disclosure improves hub discovery on phones | Usability task 2 success (mobile) | `nav_click` | Usability round |

Not to be tested: urgency banners, fake counts, testimonials, colour swaps without a usability hypothesis.
