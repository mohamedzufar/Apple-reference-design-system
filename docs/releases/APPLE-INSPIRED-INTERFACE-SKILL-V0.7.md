# Apple-Inspired Interface Craft — Advanced Skill v0.7

## Purpose
Use this skill to design and implement high-craft product websites informed by the supplied Apple reference corpus. The goal is not to copy Apple's proprietary source code or assert pixel-perfect equivalence. Extract transferable principles: clear hierarchy, product-led storytelling, deliberate whitespace, image composition, responsive behavior, immediate feedback, and motion that remains under the user's control.

## Operating contract
1. Inspect the existing project before editing. Preserve its framework, route structure, assets, naming, and working interactions unless the task explicitly calls for a change.
2. Separate observed evidence from hypotheses. A screenshot proves visual arrangement, not source CSS, exact easing, video behavior, or responsive breakpoints.
3. Make the smallest coherent set of changes. Avoid adding decorative effects just to make a page look more “premium.”
4. Never claim browser performance, accessibility, or visual fidelity is verified unless tests were actually run and results recorded.
5. Prefer a complete implementation over a pile of disconnected snippets. Include accessible states, responsive behavior, and fallback behavior.

## Design intent
- Product and content are the focal point; interface chrome is secondary.
- Use generous but purposeful whitespace. The gap should establish hierarchy, not create empty dead zones.
- Choose section composition based on the story: centered hero, asymmetric feature split, media rail, comparison, metric cluster, FAQ, or dense navigation. Do not force every section into the same card grid.
- Use a restrained neutral canvas, near-black primary text, muted secondary text, thin separators, and a clear accent for actions. Treat all extracted colors and sizes as approximations unless measured from source assets.
- Use large typography sparingly. Hero scale is not a universal heading style.
- Use high-quality, correctly cropped media as evidence for product claims. Avoid fake product UI and arbitrary stock imagery when real product assets exist.
- Keep radii and shadows component-specific. Avoid stacking borders, shadows, gradients, and blur on every surface.

## Layout and typography
- Establish a content max-width and responsive gutters with CSS custom properties.
- Use a consistent spacing scale but allow section-specific rhythm when the content requires it.
- Use a system font stack with sensible fallbacks; never assume a proprietary font is available or licensed.
- Use `clamp()` for fluid type only when it improves continuity; cap line length for readable body copy.
- Headings should have intentional line breaks, tight but readable line-height, and modest negative tracking at display sizes.
- Keep body text comfortably readable and supporting copy visually subordinate.
- Test narrow screens, zoom, long labels, translated text, and content that wraps unexpectedly.

## Motion model: direct, interruptible, restrained
### First principle
Motion must preserve user agency. It should respond immediately, communicate cause and effect, and never trap the user in a long animation.

### Scroll
- Keep native document scrolling as the default. Do not hijack wheel, touch, or trackpad input with custom scroll engines.
- Do not apply global `scroll-behavior: smooth` as a substitute for good motion. Use smooth programmatic scrolling only for explicit user-initiated navigation, and respect reduced motion.
- Do not animate layout-heavy properties on every scroll frame. Prefer transform and opacity for small, optional reveals.
- Reveal content once, with a small travel distance and no large stagger cascade. Content must remain available if JavaScript or IntersectionObserver is unavailable.
- Avoid scroll-linked parallax unless the task calls for it and it remains stable under fast input, zoom, and reduced motion.
- Never hide important content until an observer fires; ensure initial and failure states remain readable.
- Test fast wheel scroll, trackpad fling, touch momentum, keyboard PageUp/PageDown, Home/End, anchor navigation, and sticky-header transitions.

### Springs and dragging
- Use spring-like motion only where the user manipulates a physical-feeling object: drawers, draggable cards, carousels, or spatial controls. Ordinary buttons and text do not need spring simulation.
- For drag interactions, track the pointer continuously, preserve the original grab offset, use Pointer Events, and use pointer capture where appropriate.
- A gesture must be interruptible: if the user reverses direction, animate from the current rendered position, not the stale target.
- Transfer velocity only when the interaction model calls for it. Do not add fake momentum to standard page scrolling.
- Clamp boundaries deliberately; if rubber-banding is used, make it subtle, bounded, and accessible.
- Cancel animation frames and remove listeners on teardown. Avoid per-frame React/state updates when direct transform writes or a well-designed animation library is more appropriate.
- Use `requestAnimationFrame` only for frame-synchronized work; avoid expensive DOM reads/writes in the same loop. Prefer Web Animations API or CSS transitions for simple state changes.

### Timing and easing
- Choose duration based on distance and meaning, not a single global duration.
- Small state feedback should feel immediate; larger overlays may take longer but must remain interruptible.
- Use ease-out for arrivals and ease-in for departures as a starting point, then test the real interaction.
- Avoid bouncy overshoot for routine UI. Reserve stronger spring/bounce for explicit throws or playful interactions.
- Never infer Apple's exact easing constants from still screenshots.

## Glass and materials
- Blur is a material choice, not a default card style. Use it for floating navigation, overlays, or controls that genuinely sit above moving content.
- Ensure text contrast on the actual background image and theme. Add a sufficiently opaque fallback when `backdrop-filter` is unavailable.
- Avoid multiple stacked translucent surfaces; they can muddy contrast and increase compositing cost.
- Provide `prefers-reduced-transparency` handling where supported, and test solid-surface fallbacks.
- Avoid animating blur radius during scrolling. Prefer stable blur and subtle opacity changes.

## Component behavior contract
Every interactive component must define: default, hover (where relevant), focus-visible, active/pressed, selected, disabled, loading (if applicable), empty/error (if applicable), and narrow-screen behavior.

- Navigation: semantic links, disclosure button for mobile menu, Escape-to-close when appropriate, focus return, outside-click behavior only where expected, and no inaccessible hidden focus targets.
- Accordion: button controls with `aria-expanded` and `aria-controls`; expand-all state must reflect actual open panels.
- Carousel: native horizontal scrolling where possible, labeled previous/next buttons, keyboard access, correct boundaries, visible focus, and no assumptions about a fixed slide count.
- Segmented controls: explicit selected state and keyboard semantics appropriate to tabs or radio groups; don't mix patterns.
- Media controls: truthful play/pause labels and states. Do not imply actual playback if the asset is static.
- Dialog/explorer: clear close affordance, Escape handling, focus management, and no background interaction while modal when applicable.
- Forms: visible labels, inline errors, helpful status text, and real validation rather than decorative success messages.
- Buttons: use buttons for actions and links for navigation. Never leave an interactive-looking control inert.

## Accessibility and resilience
- Respect `prefers-reduced-motion`; remove nonessential motion rather than merely shortening it.
- Respect increased-contrast and reduced-transparency preferences where supported.
- Keep semantic HTML, logical headings, landmarks, keyboard operability, visible focus, sufficient contrast, and accessible names.
- Never rely on color, hover, motion, or icon shape alone to convey state.
- Maintain usable content when JavaScript fails, media is blocked, fonts fail, or blur is unsupported.
- Test 200% zoom and narrow viewport widths; avoid horizontal overflow except intentional, clearly usable rails.
- Provide alt text that communicates the purpose of meaningful images; decorative images should not create noise for assistive technology.

## Performance and implementation
- Prefer CSS transforms and opacity for motion. Avoid animating `top`, `left`, width, height, large shadows, and blur when a compositor-friendly alternative works.
- Do not blanket-apply `will-change`. Add it only after profiling and remove it when no longer needed.
- Avoid layout thrashing: batch reads before writes and do not measure layout inside a tight frame loop.
- Use passive listeners for scroll/touch where appropriate; never prevent default scrolling unless the interaction absolutely requires it.
- Use IntersectionObserver for reveal/lazy activation, with a no-observer fallback.
- Clean up observers, event listeners, media, timers, and animation frames.
- Optimize media dimensions, formats, loading priorities, and aspect-ratio reservation to prevent layout shifts.
- Treat Core Web Vitals and Lighthouse as measurements, not badges. Record baseline and after-change results on representative routes.

## Reference interpretation workflow
1. Inventory the supplied screenshots and group by page type and theme.
2. Record only visible facts: alignment, relative scale, whitespace, crop, section order, typography hierarchy, controls, and contrast.
3. Label each statement `Observed`, `Inferred`, or `Unknown`.
4. Build a traceability map from each implemented pattern to reference IDs.
5. Implement one representative component and validate it at multiple viewport widths before applying it broadly.
6. Compare screenshots at the same viewport, device scale, scroll position, and font-loading state.
7. Verify interactions separately; static image comparison cannot prove motion or accessibility.

## Quality gates before delivery
- [ ] Existing routes and content preserved unless explicitly changed.
- [ ] No dead controls, broken local links, missing assets, or console errors in tested pages.
- [ ] No global smooth-scroll rule that competes with native scrolling.
- [ ] Reduced-motion path verified.
- [ ] Keyboard-only navigation and focus order checked.
- [ ] 320/375/768/1024/wide desktop layouts checked.
- [ ] Fast scroll and horizontal rail behavior checked in a real browser.
- [ ] Light and dark themes checked for contrast and state consistency.
- [ ] Motion, image loading, and layout shifts measured on representative pages.
- [ ] Claims in documentation match what was actually tested.

## Delivery format
For every meaningful change, summarize: what changed, why it changed, files touched, how to run it, what tests were run, what failed or remains unverified, and the next highest-value improvement. Be honest about limits. Do not call a static source review “production certified.”
