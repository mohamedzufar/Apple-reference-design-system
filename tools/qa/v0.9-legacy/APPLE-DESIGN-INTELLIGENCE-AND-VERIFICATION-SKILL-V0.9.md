# Apple Design Intelligence & Verification Skill — v0.9

## Mission
Build refined, Apple-inspired product experiences through reference analysis, deliberate storytelling, robust interaction engineering, and evidence-based QA. Do not claim an implementation matches a reference or is production-ready until it has been tested.

## Operating contract
1. Inspect the existing repository before editing. Preserve its architecture unless a measured reason supports changing it.
2. Inventory routes, assets, CSS, JS, dependencies, scripts, and current test coverage.
3. Treat screenshots as evidence of visible appearance only. Label findings as **observed**, **inferred**, or **unknown**. Never claim to know proprietary source code or hidden animation physics from screenshots.
4. Write a small plan and baseline before changing code. Capture baseline screenshots at fixed viewport sizes when browser tooling is available.
5. Implement in small, reversible slices. Avoid replacing whole files when a targeted patch is safer.
6. Run syntax checks, automated browser checks, accessibility checks, and visual comparison where tools permit. Report every check as passed, failed, skipped, or not available.
7. Finish with a change log, test evidence, known limitations, and exact run instructions.

## Reference-analysis protocol
For each reference, record:
- Viewport dimensions, browser zoom if known, scroll position, theme, and device/input context.
- Section map: announcement/navigation, hero, feature proof, media story, interactive explorer, comparison, CTA, footer.
- Typography: hierarchy, max line length, line breaks, weight, tracking, and responsive changes.
- Layout: content width, section spacing, image ratio/crop, grid behavior, negative space, alignment.
- Materials: background, contrast, borders, shadows, blur, translucency, and fallback behavior.
- Interaction evidence: visible controls, selected states, progress indicators, pause controls, carousel arrows, disclosure affordances.
- Uncertainties requiring live interaction or browser inspection.

Never use a single screenshot to infer an entire page's behavior. Use multiple scroll positions and interaction states. Do not copy Apple branding or product claims into unrelated products; reproduce design principles, not trademarks or misleading claims.

## Storytelling composition
Choose sections to fit the product and narrative, not by a rigid template. A common sequence is:
1. Promise: concise headline and hero visual.
2. Context: what the product does and for whom.
3. Proof: concrete capabilities, demos, evidence, or measured outcomes.
4. Exploration: carousel, comparison, or feature explorer only when it adds value.
5. Objections: compatibility, security, workflow, pricing, or constraints.
6. Action: clear CTA and useful next step.
7. Support: FAQs, legal, accessibility, and footer navigation.

Use oversized typography and negative space with restraint. Avoid long empty sections caused by fixed heights, decorative animation without meaning, or images that fail to explain the product.

## Motion engineering rules
- Prefer native document scrolling. Do not globally force smooth scrolling; use smooth behavior only for intentional in-page navigation and disable it for `prefers-reduced-motion`.
- Animate `transform` and `opacity` first. Avoid animating layout properties (`top`, `left`, `height`, `margin`) unless required and profiled.
- Keep animations interruptible. A new input must not wait for an old transition to finish.
- Use pointer capture for custom drag controls and preserve the initial grab offset. Always support cancellation and pointer release.
- Keep velocity tracking bounded and defensive; ignore invalid timestamps and non-finite values.
- Use springs only when physical continuity improves the interaction. Use simple transitions for low-emphasis state changes.
- Do not hijack wheel/touch input or replace native scroll momentum to imitate a reference.
- Respect `prefers-reduced-motion`; offer static states instead of merely shortening every animation.
- Apply `will-change` temporarily and only after profiling demonstrates a need.
- Avoid multiple overlapping `backdrop-filter` layers; provide readable opaque fallbacks.

## Component behavior contracts
Every interactive component must define:
- Semantic element and accessible name.
- Default, hover, focus-visible, active, selected, disabled, loading, empty, and error states as relevant.
- Keyboard behavior and focus order.
- Touch/pointer behavior and cancellation.
- Responsive layout behavior.
- Reduced-motion behavior.
- What happens when content is missing or media fails.

For carousels, include boundary behavior, keyboard controls, a clear active indicator, and no automatic motion unless there is a strong content reason. If autoplay exists, provide pause/stop controls and stop motion when the user requests it or reduced motion is enabled.

## Visual verification loop
1. Capture a baseline and target at matching viewport, zoom, theme, and scroll position.
2. Compare structure first: content width, section order, image dimensions/crops, and alignment.
3. Compare typography second: line wraps, font scale, line height, weight, and spacing.
4. Compare materials and details third: contrast, borders, radius, shadows, icons, and states.
5. Fix the highest-impact mismatch, then recapture. Do not make many unrelated changes before checking again.
6. Use pixel diffs as a signal, not as the sole quality metric. Dynamic media and antialiasing can create harmless diffs.

## Required QA
- Syntax/lint checks for changed source.
- Local links/assets and console errors.
- Desktop and mobile viewport screenshots.
- Horizontal overflow, sticky navigation, and long-page scrolling.
- Keyboard-only navigation and focus visibility.
- Reduced-motion and contrast preference checks.
- Interactive states for every changed control.
- Performance measurements when browser tooling is available: frame timing, long tasks, layout shifts, and asset load behavior.

If browser automation is unavailable, explicitly mark browser QA as **not run**. Never invent FPS, Lighthouse scores, accessibility scores, or cross-browser compatibility.

## Severity model
- **P0:** broken core flow, inaccessible primary action, scroll hijack, severe layout failure, crash.
- **P1:** major visual mismatch, broken component state, keyboard trap, significant mobile failure.
- **P2:** spacing/typography inconsistency, minor visual regression, polish issue.
- **P3:** optional enhancement without clear user impact.

Fix P0 before P1; fix P1 before visual polish. Prioritize measured user impact over adding effects.

## Final response format
Provide: (1) files changed, (2) behavior changed, (3) commands/tests run and results, (4) screenshots/evidence if available, (5) known limitations, (6) how to run locally. Distinguish implemented changes from recommendations. Do not label a build production-certified without an agreed test matrix and passing evidence.
