# Apple-Inspired Product Storytelling & Motion Engineering — Skill v0.8

## Mission
Build polished, reference-informed product websites with the storytelling rhythm, restrained visual language, media composition, and interaction quality visible in the supplied Apple product-page screenshots. This is a transferable design/engineering skill, not a claim to reproduce Apple's private source code or exact physics.

## Non-negotiable operating contract
1. Inspect the existing project, routes, assets, styles, scripts, and interactions before editing. Preserve working behavior unless the task explicitly asks to replace it.
2. Treat screenshots as evidence of visible composition only. Separate **observed**, **inferred**, and **unknown**. Never claim an exact easing curve, scroll implementation, breakpoint, or source behavior from a screenshot alone.
3. Keep a small audit ledger: issue, evidence, severity, proposed fix, files changed, validation performed, remaining uncertainty.
4. Implement complete, integrated changes, not disconnected snippets. Check both themes and all affected pages.
5. Never claim performance, accessibility, browser compatibility, or pixel fidelity without running the relevant tests.
6. Prefer native browser scrolling and controls where they already provide the desired behavior. Do not add custom scroll engines or scroll hijacking by default.
7. No invented product claims, fake testimonials, fabricated metrics, or arbitrary placeholder imagery presented as real product evidence.

## Reference interpretation workflow
For each screenshot or URL, record:
- viewport and browser zoom if visible;
- page frame: global nav, product subnav, announcement bars, content width;
- section archetype: cinematic hero, editorial split, feature grid, media rail, comparison, product explorer, specs, environmental/values section, legal details;
- hierarchy: eyebrow, headline, supporting copy, CTA, media, footnotes;
- alignment, whitespace, line length, image crop, card proportion, contrast and density;
- interaction affordances visible (buttons, selectors, carousel arrows, expand icons, sticky bars);
- confidence: observed / inferred / unknown.
Do not confuse browser chrome or screenshot zoom with website layout.

## Product-storytelling architecture
Design the page as a sequence of distinct narrative beats, not a stack of identical cards:
1. **Orient** — restrained product navigation and concise value proposition.
2. **Reveal** — product-led hero with a deliberate media focal point and generous negative space.
3. **Explain** — feature section using asymmetric text/media composition or a focused grid.
4. **Prove** — performance, specs, compatibility, or concrete evidence with honest qualification.
5. **Explore** — optional carousel, selector, or interactive product view when it adds real value.
6. **Resolve** — comparison, FAQ, accessibility/environmental information, and a clear next action.
Use only the beats the content needs. Vary section scale intentionally; whitespace must support pacing, not create accidental blank zones.

## Visual system
- Typography: system stack, optical sizing when supported, tight tracking for large headings, readable body leading, controlled line length. Use oversized type only for key moments.
- Layout: define content and wide-media widths, responsive gutters, spacing tokens, and section-specific rhythm.
- Media: prioritize high-quality relevant product imagery/video; use deliberate crop and aspect ratio. Provide poster/fallback and meaningful alt text. Never fabricate image URLs.
- Color: use a restrained canvas, strong primary text, muted secondary text, and one action accent. Treat screenshot colors as approximations unless measured.
- Cards: use only where content is naturally grouped. Avoid every-section card grids, excessive borders, gradient overlays, and stacked shadows.
- Glass: apply blur/translucency only where it communicates layering (typically navigation or a floating control). Ensure readable contrast and a solid fallback; avoid stacking translucent layers.
- Responsive behavior: test content reflow at narrow widths, tablet widths, desktop, browser zoom and long text. Avoid fixed heights for text-led sections.

## Motion and scroll engineering
### Default rules
- Preserve native document scrolling and browser momentum. Never intercept wheel/touch scrolling merely to imitate a reference.
- Motion should clarify hierarchy, state, or spatial continuity. Static content must remain understandable without animation.
- Animate `transform` and `opacity` where appropriate. Avoid per-frame layout reads/writes and large blur/filter animations.
- Use `requestAnimationFrame` only for genuine frame-driven interaction; cancel it on completion/unmount and avoid duplicate loops.
- Avoid global `scroll-behavior: smooth`; use it only for deliberate in-page navigation if it does not conflict with user preferences.
- Use `IntersectionObserver` for one-time reveal when appropriate; unobserve completed items and provide an immediate-visible fallback.

### Interaction quality
- Respond on pointer-down for press feedback; keep state updates continuous for direct manipulation.
- For draggable UI, use Pointer Events and pointer capture, preserve the grab offset, handle cancel/lost capture, and make the interaction reversible.
- If an animation is interrupted, continue from the current rendered value rather than snapping to the previous target.
- Use spring-like motion only where it communicates physical continuity. Keep ordinary disclosures and navigation restrained and quick. Avoid overshoot by default; reserve bounce for explicit playful/flick interactions.
- For carousels, define boundaries, keyboard controls, touch behavior, focus behavior, reduced-motion behavior, and clear disabled states. Native horizontal overflow is preferred when it meets the requirement.
- Sticky elements must not cover anchor targets or focused controls; use scroll padding and verify real viewport behavior.
- Do not simulate “momentum” with arbitrary CSS easing if native scrolling already behaves correctly.

## Accessibility and resilience
- Honor `prefers-reduced-motion: reduce`: remove nonessential transforms, parallax, auto-advancing motion, and animated scroll; keep content visible.
- Honor `prefers-reduced-transparency: reduce` where supported with opaque material alternatives.
- Support `prefers-contrast: more` where supported; ensure focus indicators, text contrast, boundaries and selected states remain visible.
- All functionality must be keyboard reachable with logical focus order and visible `:focus-visible`.
- Controls need accessible names, correct semantics, current/expanded/selected states, and predictable focus handling.
- Do not use color alone to indicate state. Keep touch targets usable and respect zoom/reflow.
- Provide image alt text, video captions/transcripts where applicable, and non-motion alternatives for important information.

## Implementation workflow
1. Inventory files and current behavior.
2. Map the screenshot to reusable patterns and write observed/inferred/unknown notes.
3. Prioritize issues: P0 broken behavior/accessibility/performance hazards; P1 major composition and interaction gaps; P2 polish.
4. Define tokens and component states before duplicating styles.
5. Implement the smallest coherent patch; do not replace project architecture without need.
6. Validate HTML references, JS syntax, IDs, theme parity and responsive CSS.
7. Run browser checks for key flows when browser tooling is available; otherwise explicitly mark those checks as unverified.
8. Compare screenshots at the same viewport and zoom. Record what changed and what remains.

## Required QA matrix
- Viewports: narrow mobile (~375px), tablet (~768px), desktop (~1280px+); test intermediate widths and 200% zoom.
- Input: mouse, keyboard, touch/trackpad as available.
- Preferences: reduced motion, increased contrast, reduced transparency where supported.
- Flows: nav open/close, in-page links, carousel edges, selectors, accordions, media controls, focus return, resize during interaction.
- Quality: console errors, missing assets, horizontal overflow, layout shifts, image loading, sticky overlap, keyboard traps, contrast/focus visibility.
- Performance: record real browser metrics and profiling evidence before making numerical claims. A static code scan is not an FPS test.

## Definition of done
- Existing project behavior preserved or intentionally documented as changed.
- Desktop and mobile layouts have been checked.
- Controls have complete states and keyboard access.
- Reduced-motion path is usable and content is never hidden by failed animation setup.
- No known broken local links/assets or syntax errors in changed scripts.
- Changelog lists exact modifications and unverified checks.
- Release is called production-ready only after appropriate browser/device QA; otherwise label it a production-hardening candidate.
