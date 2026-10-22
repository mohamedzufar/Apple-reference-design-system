# Master Style & Structure Extraction — Reference-Informed Design System

## Purpose and source fidelity
This is a reusable design specification based on the user-provided Apple-style product-page reference notes and prior design-system requests. Color values, dimensions, and motion timings are approximate implementation recommendations unless the source explicitly identifies them. Still screenshots cannot prove exact original CSS, hidden states, or precise animation timing.

## A. Visual identity
- Overall language: editorial, minimal, high-contrast, product-led.
- Primary surfaces: white / near-white in light mode; black / charcoal in dark mode.
- Typography: modern sans-serif, confident compact headings, comfortable body copy.
- Accent: one vivid blue reserved for primary actions and links.
- Media: large, deliberate images or video with generous rounded corners.
- Depth: mostly flat; hierarchy comes from spacing, typography, background contrast, and imagery.
- Motion: restrained, smooth, and non-blocking.
- Density: spacious rather than dashboard-dense.

## B. Design tokens

### Light
```css
:root {
  --bg-primary: #FFFFFF;
  --bg-secondary: #F5F5F7;
  --surface-primary: #FFFFFF;
  --surface-inverse: #000000;
  --text-primary: #1D1D1F;
  --text-secondary: #6E6E73;
  --text-tertiary: #86868B;
  --text-on-dark: #F5F5F7;
  --accent-primary: #0071E3;
  --accent-hover: #0077ED;
  --border-subtle: #D2D2D7;
  --border-soft: #E8E8ED;
}
```

### Dark
```css
:root {
  --bg-primary: #000000;
  --bg-secondary: #1D1D1F;
  --surface-primary: #111111;
  --surface-elevated: #1C1C1E;
  --text-primary: #F5F5F7;
  --text-secondary: #A1A1A6;
  --text-tertiary: #86868B;
  --text-on-light: #1D1D1F;
  --accent-primary: #2997FF;
  --accent-hover: #45A5FF;
  --border-subtle: rgba(255,255,255,.12);
  --border-control: rgba(255,255,255,.28);
}
```

Use semantic tokens rather than raw color values in component CSS. Validate contrast for actual text sizes and weights.

## C. Typography architecture

| Role | Recommended size | Weight | Line height | Tracking |
|---|---:|---:|---:|---:|
| Hero display | 56–88px | 600–700 | 1.0–1.08 | -0.025em to -0.05em |
| Page title | 44–56px | 600–700 | 1.05–1.15 | -0.03em to -0.04em |
| Section heading | 32–48px | 600–700 | 1.08–1.2 | -0.025em to -0.04em |
| Feature/card heading | 20–28px | 500–600 | 1.15–1.3 | slightly negative |
| Lead copy | 18–20px | 400 | 1.45–1.6 | neutral |
| Body | 15–18px | 400 | 1.4–1.6 | neutral |
| Label / caption | 11–14px | 400–600 | 1.3–1.45 | neutral; avoid wide tracking |
| Button / nav | 13–16px | 500–600 | 1.0–1.3 | neutral |
| Footnote | 11–13px | 400 | 1.35–1.5 | neutral |

- SF Pro is the closest Apple-family match where available; Inter or system sans-serif are practical alternatives.
- Default to sentence case. Reserve uppercase for tiny, optional category labels.
- Use purposeful line breaks and a readable text measure, commonly 55–75 characters.
- Do not make every heading enormous. Establish hierarchy through scale, weight, alignment, and spacing.

## D. Grid, container and spacing

### Container
- Main desktop content: approximately 1120–1320px; wide media may extend to 1400px.
- Desktop side gutters: 40–96px depending on viewport.
- Tablet gutters: 28–36px.
- Mobile gutters: 20–24px.
- Desktop grid: 12 columns or flexible editorial columns.
- Mobile: stack columns and keep copy readable; don't shrink desktop layouts uniformly.

### Spacing tokens
`4, 8, 12, 16, 24, 32, 48, 64, 80, 96, 128px`

- Tight heading-to-copy gap: 12–24px.
- Media-to-caption gap: 16–24px.
- Card gaps: 16–24px.
- Section padding: 64–128px desktop; 48–80px mobile depending on content.
- Use spacing before adding borders or extra card containers.
- Align nav, hero, content sections, carousel rail and footer to a common horizontal grid.

## E. Page structure

A typical product storytelling page can follow this structure, selectively:
1. Global navigation
2. Hero: eyebrow (optional), large headline, concise supporting text, one primary CTA and optional secondary CTA
3. Hero media or product visual
4. Feature story sections with alternating editorial compositions
5. Horizontal product/feature rail
6. Comparison, proof points, metrics or specifications when relevant
7. Trust/security/FAQ where the product requires it
8. Final CTA
9. Footer link groups
10. Bottom legal/copyright row

Do not add all sections automatically. Choose based on the product's purpose and information hierarchy.

## F. Navigation structure

### Desktop
- Approximate row height: 56–68px.
- Brand left; 3–6 main links; one clear CTA on the right.
- Optional utility links (sign in/support) only if useful.
- Capsule or lightly translucent background, fine border, subtle blur if appropriate.
- Minimal shadow; no thick navigation bar.
- Current page and focus state must be visible.
- Dropdowns must support keyboard interaction and Escape.

### Mobile
- Brand left, menu trigger right.
- Expand into a sheet, panel, or vertically stacked links.
- Keep tap targets around 44×44px.
- Close on Escape; return focus to the trigger.
- Do not compress the desktop nav until it becomes cramped.

## G. Hero and editorial section structure

### Hero
- Centered or left-aligned according to the reference composition.
- One clear headline, one concise description, one main action.
- Large display text with tight line-height.
- Keep width constrained; avoid headline spanning the entire screen.
- Give the hero generous vertical padding and let media provide the visual impact.

### Editorial feature section
- Left-aligned headline and copy are common for content sections.
- Pair copy with a large media panel, or place descriptive copy beneath media.
- Alternate section composition to maintain rhythm without changing the design language.
- Avoid nesting multiple cards around the same image and copy.

## H. Card system

### Size presets (recommended)
- Compact: 240–300px.
- Medium: 320–420px.
- Large showcase: 440–560px.
- Feature lead: 640–820px where layout permits.
- Mobile rail items: commonly 82–90vw, with a sensible max-width.

### Image ratios
- 16:9: hero media/video/feature landscape.
- 3:2: editorial photography.
- 4:3: product/content tile.
- 1:1: compact square tile.
- 9:16: portrait story/device image.
- Natural ratio: when the complete image should remain visible.

### Surface and content
- Media radius: 20–24px.
- Card/panel radius: 18–28px depending on scale.
- Compact control radius: 10–16px.
- Pill controls: 999px.
- Internal padding: 20–28px standard, 16–20px compact.
- Prefer flat surfaces; use a fine border or background contrast, not both border and heavy shadow.
- Card height should generally follow content. Avoid fixed height where copy can wrap.
- Unequal widths are acceptable when the content hierarchy requires them.

## I. Horizontal image sliding / carousel

- Use a native horizontally scrollable flex rail for straightforward carousels.
- `scroll-snap-type: x proximity` for relaxed snapping or `mandatory` for deliberate card-by-card movement.
- `scroll-snap-align: start` on each item.
- Align rail padding to the same page gutter.
- Show 2–3 cards on desktop, 1–2 on tablet, and one card plus a partial next card on mobile where appropriate.
- Gap: 16–24px desktop, 12–16px mobile.
- Arrow buttons: 40–48px circular; minimum 44px hit area.
- Move by one card plus gap, or by a deliberate viewport fraction.
- Disable previous at start and next at end.
- Native touch/trackpad scrolling must work; never hijack vertical scrolling.
- Avoid auto-scroll unless the reference specifically calls for it.
- Dots are best for a small number of slides, not large card collections.
- Respect reduced-motion settings and test fast scrolling for jank.

## J. Image and video treatment
- `object-fit: cover` for editorial crops; set `object-position` intentionally.
- `object-fit: contain` for product renders, device mockups, logos and diagrams.
- Never stretch media.
- Reserve stable aspect ratios to prevent layout shift.
- Use a subtle neutral backing only if the image needs separation.
- Meaningful images need alt text; decorative images use empty alt.
- Avoid autoplay audio; provide clear controls for user-initiated video.

## K. Buttons, controls and icons

### Primary action
- Blue fill, high-contrast label, pill shape.
- Slight color shift on hover; small compression on press.
- One prominent CTA per section is usually enough.

### Secondary action
- Neutral/transparent surface with fine border.
- Subtle gray surface on hover.

### Text link
- Blue or secondary text according to context.
- Underline on hover/focus; don't rely only on color.

### Controls
- Inputs: visible labels, 44–48px height, 12–16px radius.
- Segmented selector: clear selected state and readable labels.
- Carousel arrows: circular, neutral, clearly disabled at boundaries.
- Icons: simple outline style, 1.5–2px stroke, typically 16–24px.
- Keep icon weight consistent and align with text baseline.

## L. Footer and legal information

### Desktop groups
- Product: Overview, Features, Pricing, Changelog.
- Resources: Documentation, Guides, Help, Contact.
- Company: About, Careers, Press, only if real.
- Legal: Privacy, Terms, Cookie preferences if applicable, Security/Accessibility only if supported.

### Bottom row
- `© {year} {Company}. All rights reserved.`
- Privacy
- Terms
- Cookie preferences where relevant
- Accessibility statement if one exists
- Region/language only if supported

### Responsive
- Four columns on wide screens; two columns on tablet; stacked or disclosure groups on mobile.
- Footer link text commonly 12–14px; preserve readability and touch spacing.
- Legal links must not depend on hover to be visible.
- Do not invent policy pages; legal copy needs product-specific review.

## M. Surface, borders and depth
- Light theme: white primary, pale gray secondary, near-black text, muted gray copy.
- Dark theme: black canvas, charcoal surfaces, near-white text, muted gray copy.
- Borders are fine and low contrast.
- Flat is the default; use shadows mainly for overlays/popovers.
- Use glass blur only for a few floating navigation/control elements, not every card.
- Don't use gradients, neon glows, thick borders, or strong shadows as default decoration.

## N. Motion and scrolling
- Short UI transitions: roughly 160–240ms as a practical baseline.
- Use opacity and transform for micro-interactions when possible.
- Avoid heavy blur + parallax + scale running together.
- No scroll hijacking or aggressive continuous auto-animation.
- Keep sticky navigation stable; account for its height in anchor offsets.
- Respect `prefers-reduced-motion`.
- Test real high-speed trackpad and touch scrolling.

## O. Responsive breakpoints (starting points)
- Small mobile: <= 560px.
- Tablet / compact layout: <= 900px.
- Desktop: > 900px.
These are implementation breakpoints, not a claim about the source site's breakpoints. Prefer content-driven breakpoints when a layout stops working.

## P. Accessibility and production quality
- Semantic landmarks and correctly ordered headings.
- Keyboard access to all controls and links.
- Visible focus ring.
- Text contrast tested in both themes.
- Touch targets around 44×44px where practical.
- Labels not replaced by placeholders.
- Selected/error states not communicated by color alone.
- Reduced motion supported.
- Real routes for navigation and footer links.
- Legal text accurate to the product and reviewed where needed.
- Stable image sizes to prevent layout shift.
- No fake controls in production.

## Q. What not to do
- Too many bright accent colors.
- Gradient-heavy backgrounds or glassmorphism everywhere.
- Every section inside a card.
- Equal-size card grids for all content regardless of hierarchy.
- Tiny gray copy or excessive all-caps.
- Random corner radii and spacing values.
- Overanimated scroll effects.
- Desktop layouts merely shrunk on mobile.
- Unverified claims that approximate dimensions are exact source CSS.

## R. Implementation principle
Treat this as a tokenized system, not a screenshot-only skin. Keep semantic tokens and component rules shared; keep Light and Dark theme values separate; preserve component behavior and accessibility; and tailor page structure to the actual product.
