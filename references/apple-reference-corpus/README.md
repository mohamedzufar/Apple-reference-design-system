# Apple Reference Design System — Working Corpus v0.3

This is a **living reference corpus**, not a finished design system. It captures patterns from 30 screenshots, separated into light- and dark-theme references. Add future screenshots to the appropriate `light_theme/reference_images/` or `dark_theme/reference_images/` folder, update `REFERENCE_CATALOG.md`, and extend the analysis documents rather than replacing previous findings.

## Purpose
Extract the design principles, layout patterns, typography behavior, colors, component behavior, and scroll-storytelling cues visible in the supplied references. Use those principles to build original product experiences; do not copy Apple's page pixel-for-pixel or claim this is Apple's official/proprietary system.

## How to use
1. Keep the screenshots as the source of truth.
2. Review `REFERENCE_CATALOG.md` to identify each image.
3. Read `ANALYSIS.md`, `TOKENS.md`, `MOTION_AND_SCROLL.md`, and `COMPONENT_PATTERNS.md`.
4. Add future images to `reference_images/` using the next unused `apple-ref-NN.png` ID across both theme folders, and update the catalog with an ID, filename, page/section, and observed patterns.
5. When a pattern is not visible in the screenshots, mark it as an inference or unknown. Do not invent exact values from screenshots.
6. Use tokens as starting estimates; calibrate by sampling pixels and measuring screenshots if precise reproduction is required.

## Important
- Colors and dimensions in this pack are approximate observations from screenshots, not verified official Apple tokens.
- The source images include product page content, navigation, feature storytelling, card carousels, FAQ, comparison, environmental messaging, and footer navigation.
- Product details shown in screenshots may be fictional, future-dated, or region-specific; treat them as visual reference only, not factual product claims.


## Latest update
- 2026-10-22: Added 10 new screenshots as REF-11–REF-20 and extended the analysis with segmented media selectors, interactive feature explorers, metric-led heroes, immersive media stages, product image rails, and playback/pagination affordances.


## Theme-separated corpus
- `light_theme/reference_images/`: REF-01–REF-20 (original light/neutral references).
- `dark_theme/reference_images/`: REF-21–REF-30 (new dark/cinematic references).
- Keep both collections in this same corpus; do not merge the dark references into the light-theme analysis.

- 2026-10-22: Added REF-21–REF-30 to `dark_theme/reference_images/`; created separate `light_theme/` and `dark_theme/` collections and appended dark-theme typography, color-role, component and motion observations.
