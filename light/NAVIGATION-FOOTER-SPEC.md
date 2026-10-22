# Navigation, Footer, Legal Links & Full Page Architecture

This spec expands the Apple-inspired design system with complete site chrome: desktop and mobile navigation, footer hierarchy, privacy/legal link groups, responsive behavior, and page-level composition. The supplied references support a restrained capsule-style navigation, fine separators, large editorial sections, and low-ornament UI. Exact navigation labels and legal-link ordering below are reusable product recommendations, not claims that every label appeared in the screenshots.

## 1. Site architecture

A typical product marketing site can use this page sequence:
1. Global navigation
2. Product hero
3. Product proof / key media
4. Feature storytelling sections
5. Product comparison or feature rail
6. Trust / security / FAQ (when relevant)
7. Final CTA
8. Multi-column footer with legal links and copyright line

Do not force every product into every section. Use the sequence as a compositional framework and keep each page focused on its goal.

## 2. Desktop navigation

### Geometry
- Header row height: 56–68px.
- Content max-width: 1200–1320px.
- Horizontal padding follows the page gutter token.
- Brand/wordmark at the left; primary links centered or grouped nearby; one key CTA at the right.
- Capsule navigation can use a translucent canvas, fine border, subtle backdrop blur, and 999px radius where it matches the reference.
- Keep the header visually light; avoid thick bars and strong shadows.

### Content hierarchy
- Brand / logo: links to the homepage.
- Primary links: usually 3–6 destinations, e.g. Product, Features, Solutions, Resources, Pricing.
- Utility links: Sign in, Support, language, or account menu only when useful.
- Primary CTA: one clear action, e.g. Get started or Contact sales.
- Avoid putting every footer destination in the main navigation.

### Interaction
- Hover: slight text/neutral-surface change.
- Current page: visible state using weight, underline, or subtle background—not color alone.
- Dropdown: opens on click and keyboard, closes on Escape and outside click, with focus kept predictable.
- Sticky header: optional. If sticky, reserve its height for anchor scrolling and avoid sudden layout shifts.
- Keyboard: all links and controls reachable in logical tab order; focus ring clearly visible.
- Touch target: aim for at least 44×44px.
- Keep the header stable during scrolling; avoid aggressive shrink/expand effects unless they are smooth and tested.

## 3. Mobile navigation

- Header height: around 56–64px.
- Brand on left; menu control on right.
- Use a real button with an accessible name (`Open menu` / `Close menu`).
- Open a simple sheet, popover, or full-screen panel with generous spacing.
- Menu items should be vertically stacked, with clear separators only when needed.
- Keep the primary CTA obvious and easy to reach.
- Close on Escape; restore focus to the trigger; don't trap focus unless the menu is implemented as a modal dialog.
- Prevent background scroll only when using a modal/full-screen menu.
- Avoid shrinking desktop navigation until it becomes cramped.

## 4. Footer structure

Use a footer that feels quiet and well-organized, not like a second sitemap dumped into one column.

### Recommended desktop structure
**Row 1 — Product / brand**
- Brand mark or wordmark
- One-sentence product descriptor, optional
- Optional social links if they serve the product

**Row 2 — Link columns**
- Product: Overview, Features, Pricing, Changelog
- Resources: Documentation, Guides, Help center, Contact
- Company: About, Careers, Press (only if real)
- Legal: Privacy, Terms, Cookie preferences, Security / Trust (only if available)

**Bottom legal bar**
- Copyright notice: `© {year} {Company}. All rights reserved.`
- Privacy
- Terms
- Cookie preferences (if cookies/consent are used)
- Accessibility (if a statement exists)
- Region/language selector only when supported

Keep legal and policy links visible and readable. Do not hide them in hover-only menus. Do not invent policies that the product does not actually have.

### Recommended mobile footer
- Stack the columns vertically or use accessible disclosure/accordion groups.
- Make each group heading and link easy to tap.
- Legal links may wrap across multiple lines; do not force tiny text.
- Copyright should appear at the bottom, with adequate top spacing.
- Keep link order logical and consistent across pages.

## 5. Privacy, terms, copyright and policy pages

A product site commonly needs these routes, depending on its actual features and jurisdiction:
- Privacy Policy — what data is collected, purposes, retention, sharing, rights, contact.
- Terms of Service — acceptable use, account responsibilities, billing, service limitations, termination, liability and dispute terms as applicable.
- Cookie Preferences / Cookie Policy — only if cookies or tracking require disclosure or consent.
- Security / Trust — only if there are meaningful security practices or certifications to describe.
- Accessibility Statement — only if the team can stand behind the statement and contact route.
- Copyright / IP notices — ownership and third-party attribution where relevant.
- Contact / Support — a real, monitored support path.

These pages require product-specific and legal review. This design system provides the UI structure only; it does not generate legally sufficient policy text.

## 6. Link styling
- Default: muted secondary text or clear link color, depending on context.
- Hover: underline or slight contrast shift.
- Focus: visible focus ring.
- Footer link spacing: 10–16px vertical separation for stacked mobile links.
- Footer type: usually 12–14px, but never so small that it becomes hard to read.
- Keep a clear distinction between link and plain text.
- Avoid using only opacity to communicate disabled or unavailable links.

## 7. Footer responsive layout
- Wide desktop: 4 columns, with a separate bottom legal bar.
- Tablet: 2 columns or 3 columns based on text length.
- Mobile: one column or disclosure groups.
- Use CSS grid with `minmax(0, 1fr)` so long labels wrap rather than overflow.
- Add a top border or background transition, not both heavy border and shadow.
- Legal bar can wrap naturally; do not force a single row on narrow screens.

## 8. Page-level interaction and performance
- Navigation and footer links must lead somewhere real in production; use actual route names and never leave decorative fake links.
- Anchor links should account for sticky header height.
- Avoid scroll hijacking.
- Use smooth scrolling only when reduced motion is not requested.
- Keep image dimensions/aspect ratios stable to reduce layout shift.
- Don't use heavy blur or continuous animation as a substitute for good composition.
- Respect `prefers-reduced-motion`.
