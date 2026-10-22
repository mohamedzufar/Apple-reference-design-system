# Apple-Inspired Design System Skill — v1.0 Final

## Mission
Turn supplied screenshots, URLs, and assets into a complete, reference-informed, working product website. The deliverable is the implemented site, not only advice or a prompt. Optimize for storytelling order, page geometry, interaction fidelity, native-feeling motion, accessibility, and maintainability.

## Non-negotiable workflow
1. **Inventory before edits:** list every file, entry point, route, dependency, image/font/video, and existing interaction. Make a recoverable copy or work on a branch.
2. **Reference ledger:** for each screenshot note viewport/zoom/scroll position and section boundaries. Tag every conclusion `OBSERVED`, `INFERRED`, or `UNKNOWN`. Never infer hidden interactions as facts.
3. **Asset audit:** map file name, type, dimensions, aspect ratio, size, likely usage, and confidence. Reuse supplied assets first. Do not hotlink invented image URLs or replace supplied product imagery with unrelated stock.
4. **Story map:** preserve the reference's exact section order when the user asks for a clone. Create a manifest with section id, purpose, copy intent, media, background/material, interaction, entry/exit behavior, and mobile adaptation. Do not reorder sections just because a generic template suggests it.
5. **Build the whole page:** header/announcement/product nav, hero, every middle section, interactive stories, specs/comparison if present, CTA, footer, and secondary pages required by the reference. No placeholder buttons or dead anchors.
6. **Wire all interactions:** navigation, carousel, tabs/segmented controls, accordions, media controls, selectors, dialogs, and anchor links. Include keyboard states, focus, empty/disabled boundaries, and responsive behavior.
7. **Motion pass:** preserve native document scroll. Use deliberate smooth anchor navigation only when appropriate and respect `prefers-reduced-motion`. Use transform/opacity for simple transitions. Use rAF for continuous pointer/scroll rendering only when needed. Batch layout reads before writes. No global scroll hijacking, blanket `will-change`, fake inertial effects, or long animation that blocks input.
8. **Visual comparison loop:** capture at matching viewport sizes and scroll positions. Compare section order and geometry first, then hero scale, typography/line breaks, image crop, spacing, color/material, then micro-details. Fix the highest-impact mismatch and repeat.
9. **Responsive and accessible pass:** test desktop/tablet/mobile, keyboard-only, visible focus, contrast, reduced motion/transparency, zoom, narrow width, and touch interaction. Use semantic landmarks and accessible names.
10. **Release evidence:** report exact commands run, browser/device, passed/failed checks, known gaps, and screenshots. Never claim pixel-perfect, production-certified, FPS-verified, or cross-browser-tested without evidence.

## Storytelling is mandatory
When the reference supplies an order, reproduce that order. The order is an editorial system, not a bag of components. Typical roles may include:
- context/announcement and global navigation
- product identity and primary promise
- cinematic hero / product reveal
- concise emotional or functional statement
- feature story sections in the supplied order
- media / close-up / interaction sequence
- proof, comparisons, specs, or ecosystem context when present
- feature explorer or carousel
- FAQ/support and final CTA
- complete footer, legal, accessibility and privacy routes as required

Do not force this sample sequence over the screenshot. Derive the real sequence from evidence and preserve it. Match section height and pacing intentionally; whitespace must serve the story, not pad out the page.

## Reference evidence schema
For each section record:
- `id`, `order`, `purpose`
- `viewport`, `scrollY`, `sticky state`
- `heading hierarchy`, `line breaks`, `content width`
- `media asset`, `aspect ratio`, `crop/focal point`
- `background/material`, `spacing`, `alignment`
- `visible interaction state`
- `OBSERVED / INFERRED / UNKNOWN`
- implementation file and screenshot used for comparison

## Motion quality bar
- Input response starts immediately; do not wait for pointer-up to acknowledge a press.
- Interactions can be interrupted and reversed; avoid stale target animations.
- Use springs only when motion has a physical/direct-manipulation rationale. Keep ordinary transitions restrained.
- Carousels must have sensible boundary states, keyboard controls, touch behavior, and no accidental page-scroll blocking.
- Sticky scenes must not trap scroll, create unexplained blank space, or hide content at zoom.
- Use scroll-linked effects as progressive enhancement with a fallback.
- Avoid expensive animated blur, layout properties, excessive layers, and scroll handlers that measure layout every frame.

## Visual system
Centralize color, typography, spacing, radius, shadow, z-index, and motion tokens. Use fluid typography with `clamp()`, reasonable line lengths, restrained tracking, and real supplied fonts/assets where available. Glass is contextual material, not a universal card style; provide solid fallbacks and preserve contrast. Maintain coherent light/dark parity where both themes exist.

## Definition of done
- [ ] All requested sections exist in the right order.
- [ ] Every visible control works or is explicitly disabled with reason.
- [ ] No broken local links or missing assets.
- [ ] No unintended horizontal overflow at supported widths.
- [ ] Keyboard and reduced-motion paths work.
- [ ] Light/dark theme behavior is coherent where applicable.
- [ ] Browser console checked; automated checks run where available.
- [ ] Screenshots captured at matching viewports and differences documented.
- [ ] README contains setup, run, test, structure, deployment and Git publishing steps.
- [ ] Claims in release notes match checks actually performed.

## Git delivery protocol
1. `git status --short` and inspect current branch.
2. Create a feature/release branch unless user explicitly requests direct main push.
3. Run documented checks; inspect `git diff --check` and `git diff --stat`.
4. Never commit secrets, `.env`, node_modules, generated browser profiles, or copyrighted assets without permission.
5. Commit with a clear message, e.g. `feat: release v1.0 storytelling design system`.
6. Push only when authenticated remote and explicit authorization are available. If not, provide exact commands; do not claim a push occurred.

## Accuracy / rights
This is a reference-informed system, not Apple's proprietary source code. Use user-provided screenshots and assets or assets the user is licensed to use. Do not claim official affiliation. Pixel similarity is a measured outcome, not a promise.
