# Card, Media, Carousel & Sliding Interaction Specification

This specification extends the Light and Dark theme foundations with detailed, reusable rules for card dimensions, image ratios, horizontal rails, snapping, controls, responsive behavior, and motion. Dimensions are implementation recommendations based on the supplied visual references; they are not claimed to be the original website's exact CSS values.

## 1. Composition rules

The reference style is editorial rather than dashboard-dense:
- Let media establish the composition; do not wrap every image in extra UI.
- Pair a large feature panel with smaller supporting panels when hierarchy calls for it.
- Use unequal card widths when content importance differs.
- A horizontal rail may show part of the next card to hint that more content exists.
- Descriptions generally sit below the image or within the open layout, not in multiple nested containers.
- Use a centered content container around 1200–1320px for most desktop sections, with wider media allowed when the composition benefits.

## 2. Card dimensions

Use these as starting presets. Content should determine height; avoid fixed card heights when text can vary.

### Feature / editorial cards
- Desktop width: 520–680px for a two-up feature; 640–820px for a lead feature.
- Image ratio: 16:9, 3:2, or a deliberately art-directed crop.
- Media radius: 20–24px; outer panel radius: 24–28px.
- Text area padding: 20–28px, or no enclosing card when the reference layout uses open space.
- Heading: 24–32px; description: 15–18px.
- Gap between image and copy: 16–24px.

### Horizontal showcase cards
- Large rail: 440–560px desktop.
- Medium rail: 320–420px desktop.
- Compact rail: 240–300px desktop, only when the content can remain readable.
- Tablet width: usually 70–82vw, with a max width to preserve hierarchy.
- Mobile width: 82–90vw; cap around 360px for compact content and allow wider media-led cards where appropriate.
- Rail gap: 16–24px desktop, 12–16px mobile.
- Use a partial next card on the right where the rail should clearly signal horizontal continuation.

### Grid cards
- Three-column grid: card width depends on container, commonly 280–380px.
- Two-column grid: use when descriptions are longer or the cards need more breathing room.
- Gap: 16–24px.
- Internal padding: 20–28px.
- Card content should align at the top; equal heights are optional, not mandatory.
- Avoid forcing every section into a three-column card grid.

### Utility / compact cards
- Typical width: 220–300px.
- Padding: 16–20px.
- Radius: 16–20px.
- Use for short metadata or controls, not long explanatory content.

## 3. Image sizing and crop

Recommended ratios:
- `16 / 9`: product video, cinematic feature, landscape showcase.
- `3 / 2`: editorial product photography and feature cards.
- `4 / 3`: product tiles or medium content cards.
- `1 / 1`: compact object/product thumbnails.
- `9 / 16`: portrait story or mobile-device imagery.
- `auto`: when the image's full aspect ratio is meaningful and should not be cropped.

Rules:
- Use `object-fit: cover` for art-directed panels; position the crop with `object-position`.
- Use `object-fit: contain` for isolated devices, product renders, logos, and diagrams where cropping would remove information.
- Don't stretch images to fit.
- Use a consistent aspect ratio within a single rail unless the visual reference intentionally mixes sizes.
- Add useful alt text for meaningful images; use empty alt text for decorative media.
- Reserve a neutral background behind media only if the image needs separation from the page.
- For video, preserve a clear poster frame, use controls when playback is user initiated, and avoid auto-playing audio.

## 4. Card surface and radius

### Light theme
- Canvas: `#FFFFFF`; alternate sections: `#F5F5F7`.
- Primary text: `#1D1D1F`; supporting text: `#6E6E73`.
- Borders: `#D2D2D7` or softer `#E8E8ED`.
- Cards are usually flat; use a fine border or section background contrast.
- Shadows are optional and should be reserved for overlays or genuinely floating controls.

### Dark theme
- Canvas: `#000000`; secondary surface: `#1D1D1F`; inset surface: `#111111`.
- Primary text: `#F5F5F7`; secondary text: `#A1A1A6` or `#86868B`, after contrast testing.
- Borders: low-contrast white at 10–16% opacity.
- Separate cards mainly through background contrast, spacing, and media.
- Avoid bright borders and heavy shadows around every item.

### Radius tokens
- Compact control: 10–12px.
- Input / small panel: 12–16px.
- Standard card: 18–22px.
- Large media: 20–24px.
- Feature panel: 24–28px.
- Pill control: 999px.
Use one radius family consistently; don't choose a random radius per component.

## 5. Horizontal carousel / rail

### Layout
- Track: `display: flex`.
- Each item: `flex: 0 0 auto`.
- Desktop: show roughly 2–3 cards depending on card width.
- Tablet: show 1.2–2 cards.
- Mobile: show one card plus a small visible portion of the next item when it improves discoverability.
- Use container padding aligned with the page grid.
- Allow horizontal overflow; hide the scrollbar only if a clear alternative navigation affordance exists.
- Prefer native horizontal scrolling and CSS scroll snapping over a JavaScript animation loop for simple rails.

### Scroll behavior
- Use `scroll-snap-type: x mandatory` for deliberate card-by-card rails, or `x proximity` if free scrolling should remain easy.
- Use `scroll-snap-align: start` on cards.
- Use `scroll-padding-inline` matching the rail's page gutter.
- Native trackpad/touch swiping should work without custom drag code.
- Do not hijack vertical page scrolling.
- Avoid continuous auto-scroll for editorial/product rails unless the reference clearly calls for it.
- Do not use `scroll-behavior: smooth` on every high-frequency update if it creates lag; smooth behavior is best for explicit arrow-button navigation.

### Arrow controls
- Circular button: 40–48px desktop, minimum 44px touch target.
- Neutral surface, fine border, simple outline arrow icon.
- Disabled state is visually muted and actually disabled.
- Keep controls near the rail heading or at the rail edge, consistently.
- Arrow click scroll distance: one card plus its gap, or a deliberate viewport fraction.
- Keyboard: buttons must be focusable; preserve native tab order.
- Provide an accessible label such as “Scroll product highlights forward”.
- Don't imply a control is functional if it does nothing.

### Dots / pagination
- Use dots only when the number of slides is small and the current position matters.
- For long card rails, arrow controls plus visible partial next card are often clearer.
- Active state should be distinct in shape/width as well as color when appropriate.
- Don't render dozens of dots for a large collection.

### Motion
- Arrow-triggered movement: smooth, predictable, approximately 220–420ms depending on distance and browser behavior.
- Hover: subtle border/color shift; optional 1–2px lift for interactive cards.
- Pressed: tiny compression, not a springy bounce.
- Avoid simultaneous heavy blur, parallax, scale, and scroll-linked animation.
- Support `prefers-reduced-motion`.
- Test with fast trackpad scroll and touch swipe. The user must retain control.

## 6. Carousel states

- Start: previous button disabled or omitted.
- Middle: both directions enabled.
- End: next button disabled or omitted.
- Focus: visible focus ring.
- Loading: preserve the rail's geometry with stable skeleton cards.
- Empty: explain there are no items and provide the next step.
- Error: show a short error and retry action if data loading failed.
- Responsive: recalculate card widths with CSS; don't hard-code a desktop pixel width on mobile.

## 7. Accessibility requirements

- Use a labelled section and a list of cards where appropriate.
- Use semantic buttons for controls; don't use clickable `div`s.
- Keep controls operable with keyboard.
- Provide visible focus.
- Don't make color the only signal for selected or disabled states.
- Avoid auto-moving carousels; if autoplay is essential, provide pause controls and stop on user interaction.
- Honor reduced motion.
- Ensure text contrast is checked for both themes.
- Images conveying information need useful alternative text.

## 8. Implementation checklist

- [ ] Card width responds to viewport.
- [ ] Images use intentional aspect ratios and correct `object-fit`.
- [ ] Card gaps and radii come from tokens.
- [ ] Rail aligns to the same content gutter as the page.
- [ ] Partial next card is intentional, not accidental clipping.
- [ ] Touch and trackpad scrolling work naturally.
- [ ] Arrow controls move the rail and have accessible labels.
- [ ] Start/end disabled states are correct.
- [ ] Keyboard focus is visible.
- [ ] Reduced motion is respected.
- [ ] No layout jump while images load.
- [ ] Fast scrolling does not stutter.
