# Claude Code Instructions — Apple-Inspired Design System

A reference-informed design system and engineering toolkit for transforming screenshots, design references, and product assets into complete, cinematic product experiences with native-feeling motion, responsive typography, and evidence-based verification.

---

## 1. Quick Commands & Verification

When working in this repository or executing tasks, use these standard commands:

```bash
# Validate all HTML links, duplicate IDs, and essential assets
python tools/scripts/validate_project.py

# Check JavaScript syntax across landing and demos
node --check assets/landing/studio.js
node --check demos/product-story-studio/app.js

# Combined test run (via npm)
npm test

# Run local preview server
python -m http.server 8000
# or: npx serve . -p 8000
```

---

## 2. Core Philosophy & Operating Contract

1. **Build the Whole Page, Not Just a Hero:** Deliver a complete, functioning site from top announcement/navigation bar down to the legal footer links. No dead placeholder buttons or broken `#` links.
2. **Storytelling is the System:** When a reference screenshot or flow is provided, reproduce the **exact section sequence**. Do not re-arrange sections into generic templates; the sequence is an editorial narrative.
3. **Evidence-Based Engineering:** Categorize every design decision as `OBSERVED`, `INFERRED`, or `UNKNOWN`. Never claim pixel-perfect parity or unmeasured 60fps performance without recorded evidence.
4. **Motion Preserves User Agency:** 
   - Never hijack native document scrolling with custom wheel-scroll or virtual momentum engines.
   - All interactions must be interruptible and reversible.
   - Always honor `@media (prefers-reduced-motion: reduce)`.
   - Never animate layout properties (`width`, `height`, `top`, `margin`); animate only `transform` and `opacity`.
5. **No Framework Bloat:** Use clean semantic HTML5, Vanilla CSS with custom properties (`tokens.css`), and lightweight Vanilla JS.

---

## 3. The 10-Step Execution Pipeline

When the user asks to build or clone an Apple-style product page:

1. **Inventory:** Scan all assets, images, icons, and existing structure before writing code.
2. **Reference Ledger:** Document section boundaries, viewports, and focal points from reference images.
3. **Asset Audit:** Measure dimensions and aspect ratios; map supplied assets to appropriate sections without arbitrary stock replacement.
4. **Story Map:** Define section-by-section roles:
   - *Introduce:* Announcement bar + Global nav + Product nav bar
   - *Reveal:* Cinematic Hero with product imagery, headline & CTA
   - *Explain:* Story split sections, feature deep-dives in exact order
   - *Showcase:* Media close-up / hardware showcase
   - *Explore:* Interactive segmented feature explorer or snap card rail carousel
   - *Detail:* Comparison matrix / Tech specs / FAQ accordion (`<details>`)
   - *Resolve:* Final closing CTA section + complete footer with legal disclaimer
5. **Implement Full HTML Structure:** Use semantic landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<article>`, `<footer>`).
6. **Token-Driven Styling:** Centralize tokens for colors, typography, radii, spacing, and shadows in CSS variables.
7. **Interactive Wiring:** Wire mobile menus, segmented tabs, carousels (with keyboard arrow keys + touch snap), and modal dialogs.
8. **Motion Pass:** Subtle reveals via `IntersectionObserver`, rAF-throttled scroll handlers, direct manipulation without lag.
9. **Accessibility & Responsive Pass:** Ensure focus rings, keyboard navigability, 4.5:1 text contrast, fluid `clamp()` sizing across 320px–1920px viewports.
10. **Evidence & Verification:** Run `validate_project.py` and `node --check`, test in browser, report verified behaviors and noted limitations.

---

## 4. Visual Tokens & Styling Rules

- **Color Palettes:**
  - Dark Theme (Default): Background `#08090b` / `#000000`, Card Surface `rgba(255, 255, 255, 0.05)`, Primary Text `#f5f5f7`, Secondary `#86868b`, Accent Blue `#2997ff`.
  - Light Theme: Background `#fbfbfd`, Card Surface `#ffffff`, Primary Text `#1d1d1f`, Secondary `#6e6e73`, Accent Blue `#0071e3`.
- **Typography:**
  - System font stack: `-apple-system, BlinkMacSystemFont, "SF Pro Text", "SF Pro Display", "Helvetica Neue", Helvetica, Arial, sans-serif`.
  - Fluid heading scales using `clamp(2rem, 5vw + 1rem, 4.5rem)` with modest negative tracking (`letter-spacing: -0.015em` to `-0.03em`).
  - Intentional line breaks (`<br>`) to balance headline rhythm.
- **Glassmorphism:**
  - `backdrop-filter: blur(20px); -webkit-backdrop-filter: blur(20px);`
  - Always provide a solid fallback background (`background: rgba(15, 17, 21, 0.8)`).
- **Cards & Radii:**
  - Outer card radius: `20px` to `28px`.
  - Inner element radius: `12px` to `16px`.
  - Border: `1px solid rgba(255, 255, 255, 0.1)`.

---

## 5. Definition of Done (DoD)

- [ ] All sections present in reference sequence without missing blocks.
- [ ] Every button, link, and interactive toggle has a working target or documented handler.
- [ ] Zero duplicate DOM IDs and zero broken local asset references.
- [ ] Fluid responsive layout from 320px mobile to 4K displays.
- [ ] Keyboard navigation (Tab, Enter, Escape, Arrow keys) functions cleanly.
- [ ] `prefers-reduced-motion` media query respected.
- [ ] Static validation scripts pass (`npm test`).
