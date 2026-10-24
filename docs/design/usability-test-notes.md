# Usability test notes

> **Status: no participant testing has been run yet.** The results below come from an automated walkthrough (Playwright, 1366 px and 390 px) plus an expert heuristic review [S2]. They are pre-test findings, not user data. Participant results must be added to the log in §3 before the design is finalised.

## 1. Pre-test walkthrough (2026-10-24)
| # | Task | Result | Errors / confusion found |
|---|---|---|---|
| 1 | Understand the site's purpose | ✅ Subtitle ("the free psilocybin encyclopedia — updated daily") is above the fold on desktop and mobile. | "Encyclopedia" + "updated daily" could suggest a wiki anyone can edit; About clarifies. Watch for this in testing. |
| 2 | Locate main research hubs | ✅ Desktop: all 7 nav links visible. ⚠️ Mobile: previously **hidden**; now a scrollable row, only 3 of 7 links fully visible without swiping. | Header links "Overview / Research / Legal status" are in-page anchors on the homepage, which may not read as separate hubs. |
| 3 | Find a product-format explanation | ❌ No section or page covers product formats (dried mushrooms, capsules, edibles, etc.). Nearest is "Microdosing" on the homepage. | **Content gap** — out of scope for a visual-only change. Flagged for the editors. |
| 4 | Identify the evidence behind a claim | ✅ 6 inline citations on the homepage, 0 broken anchors. Event pages have a "Source" box. Jumped-to references are now highlighted. | Citation markers are small (superscript); hit area enlarged with padding. |
| 5 | Find contact & methodology pages | ⚠️ About is in the header; **Editorial policy (methodology) is only in the footer**; the contact email is only on About/Editorial policy. | Recommend adding "Methodology" to the header nav and a contact link to the footer — content/nav decisions for the editors (CRO backlog E1). |

## 2. Moderated test protocol
- **Participants:** 5 per round (finds most usability problems per round; run iterative rounds) [S15]. Mix: 3 mobile, 2 desktop; include at least one screen-reader or zoom user.
- **Method:** think-aloud, unmoderated tasks above, no hints. Start each task from the homepage.
- **Record per task:** completion (success / with assistance / fail), time, wrong paths, verbatim confusion, confidence (1–7 SEQ).
- **Success criteria:** ≥ 4/5 complete each task unassisted before launch.

## 3. Participant log (to fill in)
| Participant | Device | T1 | T2 | T3 | T4 | T5 | Errors / confusion notes |
|---|---|---|---|---|---|---|---|
| P1 | | | | | | | |
| P2 | | | | | | | |
| P3 | | | | | | | |
| P4 | | | | | | | |
| P5 | | | | | | | |
