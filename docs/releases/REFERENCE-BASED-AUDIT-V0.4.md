# Reference-Based Audit — v0.4

## Scope
Compared the earlier 28-file `apple-inspired-design-system-full(1).zip` against the user's supplied reference corpus `apple-reference-design-system-v0.3.zip`, which contains 30 screenshots (REF-01–REF-30) plus a reference catalog and analysis. Then updated the design system to v0.4.

## Main reference-derived gaps found
The earlier system did not provide implemented demos for several patterns explicitly present in the user's reference catalog:
- REF-04 FAQ accordion and expand/collapse-all control.
- REF-05 three-up value cards with icon/plus affordance.
- REF-09/10/13/15/27 split technical specification and numeric metrics layouts.
- REF-12 segmented media selector, caption state and playback affordance.
- REF-17/28 interactive feature explorer with grouped options and a close/reset action.
- REF-16/21/22/23/24/26/29/30 cinematic media and dark-storytelling patterns.
- It did not bundle the reference screenshot corpus or provide a per-reference traceability map.

## Confirmed code issues fixed in v0.4
1. Replaced dead placeholder links in the navigation/footer demo with existing local documentation or explicit local template pages.
2. Added demo privacy, terms, accessibility, and cookie-preference pages. These are clearly marked as templates; they are not legal advice or a production consent manager.
3. Changed the extra typography specimen H1 in both foundation pages to a non-heading specimen, leaving one page-level H1.
4. Replaced hard-coded carousel slide count and assumed card gap with a count and target position derived from the actual card elements and rail geometry.
5. Improved mobile navigation disclosure: initial closed state uses `inert`/`aria-hidden`, opening focuses the first link, Escape returns focus to the trigger, outside click closes the menu, and resize closes the menu on desktop widths.
6. Added dynamic copyright year behavior where the shared script is loaded.
7. Added a reference-patterns demo page in both themes.

## Validation performed
- Archive now contains 80 files, including the full 30-screenshot reference corpus and documentation.
- Static HTML audit: all 18 HTML pages have one H1 and no missing same-page fragment targets.
- Static local-resource audit: all relative local file links and linked assets resolve.
- JavaScript syntax checks: both theme scripts and all inline HTML scripts passed `node --check`.

## Not performed / cannot claim
- No real browser automation, screenshot visual regression, or device testing was run.
- No screen-reader testing was run.
- No exact pixel measurements or original source CSS were recovered.
- Media stage playback is a UI-state demo, not actual video playback.
- Cookie preference choices are not persisted and do not set/read cookies.
- Legal pages are placeholders and must be replaced with product-specific, reviewed content.
- Reference values are approximate; screenshots cannot prove original breakpoints, motion timing, or responsive behavior.

## Final status
The v0.4 archive is more complete and traceable to the user's reference corpus. It remains a **reference-informed design-system prototype**, not an official Apple system or a production-certified component library. The next step for true completion is live browser/device QA and screenshot comparison at matched viewport sizes.
