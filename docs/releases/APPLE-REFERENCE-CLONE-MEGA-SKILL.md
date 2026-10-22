# Apple Reference Clone Studio — Mega Skill v0.8

## Mission
Build a high-fidelity, Apple-inspired product website from user-supplied screenshots, full-page captures, and assets. The target is a working implementation—not a mood board, generic template, or list of suggestions. Preserve the reference's information architecture, section rhythm, typography hierarchy, media proportions, interactions, and responsive behavior while using assets the user owns or is allowed to use. Do not claim pixel-perfect equivalence until measured in a browser.

## Required operating mode
1. **Inventory first.** Inspect every supplied file and archive. Identify framework, routes, assets, fonts, scripts, existing behaviors, duplicate styles, and current breakages. Never overwrite the project before making a recoverable copy.
2. **Reference decomposition.** For each screenshot, record viewport size, browser zoom if known, scroll position, sticky/fixed elements, section boundaries, content width, columns, image crop, typography, color, radius, and visible states. Label each item `observed`, `inferred`, or `unknown`.
3. **Build a page map.** Create an ordered section manifest: global navigation, announcement bar, hero, proof/feature sections, media gallery, interactive explorer, comparison, CTA, footer, legal notes. Adapt this to the actual reference; never force irrelevant sections.
4. **Asset mapping.** Build an asset manifest with filename, dimensions, aspect ratio, format, file size, likely section, and confidence. Prefer supplied assets. Do not substitute random imagery when an exact asset is present. If an asset is missing, use a clearly documented placeholder rather than inventing a source URL.
5. **Implement the actual page.** Reuse the project's existing framework and conventions. Produce functioning navigation, carousel controls, tabs/selectors, accordion, product feature explorer, media controls, anchor links, responsive states, and keyboard interaction where shown. A visual control that does nothing is a defect.
6. **Compare and refine.** Capture screenshots at matching viewport sizes and scroll positions. Fix the largest differences first: page geometry, section order, hero scale, typography, media sizing/crop, then spacing, colors, borders, shadows, and micro-motion. Repeat until the remaining differences are listed.
7. **Report honestly.** State which routes and interactions were tested, which browser was used, what failed, and what remains unverified. Never say “production-ready”, “pixel-perfect”, or “FPS verified” without evidence.

## Reference fidelity rubric (score 0–5 per category)
- Page structure and section sequence
- Global/navigation geometry
- Typography and line breaks
- Content width, grids, whitespace
- Product imagery and crop
- Color, material, contrast, radii
- Interaction states and behavior
- Scroll/sticky choreography
- Responsive adaptation
- Accessibility and resilience

Record evidence and a short rationale for every score. A score is not a claim of objective pixel similarity unless backed by screenshot-diff measurements.

## Motion engineering rules
- Keep native document scrolling as the default. Do not apply global smooth scrolling to every scroll operation. Smooth-scroll only deliberate anchor navigation and respect reduced-motion preferences.
- Use `requestAnimationFrame` for continuous pointer/scroll visual work; batch reads before writes. Animate `transform` and `opacity` where practical. Avoid per-scroll layout reads, large animated blurs, and blanket `will-change`.
- Scroll-driven effects must be progressive enhancement. Use CSS scroll timelines only with fallback; otherwise use a throttled/rAF-based approach and test high-speed scroll.
- Interactive motion must be interruptible. New input starts from the currently rendered state, not the previous destination. Do not fake spring physics with a long CSS transition if direct manipulation is expected.
- Carousels need coherent pointer capture, drag threshold, velocity-aware release only when useful, keyboard support, reduced-motion behavior, boundary states, and no accidental page-scroll blocking on touch.
- Sticky scenes must not trap users, cause large blank gaps, or create excessive main-thread work. Use scroll pinning only when it materially improves comprehension.
- Use animation only to explain hierarchy, continuity, or state change. Do not animate every element into view.

## Visual language
- Use system typography or supplied brand fonts; define a responsive type scale with `clamp()`, controlled line lengths, optical sizing where supported, and restrained tracking.
- Establish spacing, color, radius, shadow, z-index, and motion tokens before tuning individual sections.
- Glass is a material, not a default card style. Use translucency only where background context matters; preserve text contrast and provide solid fallbacks.
- Product photography is the main visual anchor. Preserve aspect ratio, crop intentionally, avoid unearned gradients and generic glow effects.
- Use large negative space deliberately but do not leave accidental empty viewport-sized sections.
- Match the reference's visual rhythm, not only isolated components.

## Accessibility and resilience
- Semantic landmarks, one clear page H1, logical heading order, descriptive alt text, keyboard-operable controls, visible focus, and accessible names.
- `prefers-reduced-motion`, `prefers-reduced-transparency` where supported, and `prefers-contrast: more` fallbacks.
- Support zoom, narrow viewports, touch, keyboard, unavailable images, and no-JavaScript core content.
- Do not encode meaning with color alone. Keep contrast adequate over imagery and glass.

## Validation gates (must pass or be reported)
### Static
- No syntax errors; no duplicate IDs; no missing local asset references; no dead internal links.
- No accidental horizontal overflow at target viewports.
- No unhandled missing assets or console errors introduced by the work.
### Functional
- Test every visible control, including repeated clicks, keyboard use, escape behavior, resize, and edge states.
- Test reduced motion and theme variations if present.
### Visual
- Capture top, middle, bottom, and interaction states at identical viewport/zoom.
- Compare geometry before decorative details. Log differences and rerun after fixes.
### Performance
- Measure in a real browser. Record LCP/CLS/INP where tooling is available, scroll responsiveness, long tasks, and image weight. Do not infer FPS from CSS inspection.

## Delivery contract
Deliver (1) modified project, (2) README with run instructions, (3) reference/asset map, (4) changelog, (5) QA report, and (6) unresolved issues. Preserve the user's source files and explain any intentional replacements. Avoid making unsupported claims about Apple’s proprietary source code or exact internal physics; reproduce observable behavior with standard web technologies.
