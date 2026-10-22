# Component patterns extracted from screenshots

## Product sub-navigation
- Compact horizontal bar, product name at left, secondary and primary action at right.
- Rounded capsule-like container, thin border, white/light surface.
- Must collapse gracefully on mobile.

## Hero section
- Optional eyebrow above a large headline.
- Headline can be centered; line breaks are deliberate.
- Large product visual is the main event.
- Keep CTA count low and visual hierarchy clear.

## Feature story
- Section headline and optional short introduction.
- Mixed-width media cards or a large feature image.
- Captions below media with muted body text and a simple link.
- Alternate dark media stages and light content backgrounds when content benefits.

## Value cards
- Usually a small number of cards, often three.
- Simple icon, concise title/message, restrained semantic accent, optional expand affordance.
- Use only where the card grouping serves a clear purpose.

## Carousel
- Horizontal rail with consistent gap and card alignment.
- Partial next card may communicate continuation.
- Previous/next controls are separate from cards and accessible by keyboard.
- Must support touch and avoid layout shifts.

## FAQ accordion
- Strong section heading.
- Rows separated by thin rules, questions aligned left, chevron aligned right.
- Expand-all control may appear at top right.
- Use semantic buttons and `aria-expanded`.

## Specification comparison
- Split explanatory copy and numeric metrics.
- Numbers receive stronger emphasis than labels.
- Comparison selector and metrics grouped on a soft neutral panel.
- Keep units and footnotes readable.

## Footer
- Several columns grouped under clear labels.
- Dense but consistent spacing.
- Divider separates navigation from legal/region row.
- On mobile, columns should collapse into accessible accordions or a logical stacked layout.


## 7. Additional patterns from REF-11–REF-20

### Segmented media selector
- Place a compact capsule selector below the media frame.
- Use a dark selected pill and quiet inactive labels.
- Keep the description in its own text block below the control.
- Provide keyboard-operable selection, visible focus, and a semantic selected state in implementation.

### Interactive feature explorer
- Use a spacious rounded panel with options at left and a product/UI demonstration at right.
- Keep option controls visually grouped and consistently shaped.
- Selected state should be unmistakable without relying on color alone.
- Collapse to a stacked layout on narrow screens; do not shrink the demonstration until it becomes unreadable.

### Media-stage / film panel
- Place a large media surface inside a generous white or neutral stage.
- Keep playback and pagination controls close to the media, not detached far away.
- Use a visible pause/play state and accessible labels.
- Do not autoplay sound; honor reduced-motion preferences.

### Product metric hero
- Combine eyebrow, oversized headline, concise supporting copy, product image, and two or more numerical proof points.
- Give metrics enough spacing to read as separate facts.
- Use muted labels below or beside the number; do not use decorative cards unless needed by the content.

### Product image rails
- Support variable card widths and intentional viewport clipping.
- Keep captions below imagery and constrain their line length.
- Use circular low-emphasis navigation controls and ensure touch/keyboard operation.


## Dark-theme component patterns (REF-21–REF-30)

### Dark product sub-navigation
- Near-black rounded bar with subtle outline; product title at left, quiet outlined secondary action and blue primary action at right.
- Maintain readable contrast without turning the bar into a bright card.

### Cinematic media hero
- Black canvas, muted eyebrow, large white headline, generous gap, then a very wide rounded image/video stage.
- Keep controls and text away from the focal subject.

### Dark feature carousel
- White section title, two or more large landscape media cards, bold white/near-white lead-in and gray description beneath.
- Let the next card peek into view; controls remain small and low-emphasis.

### Parameter selector
- Compact rounded segmented control centered below media.
- Selected state can use a product-specific accent (yellow in the aperture example); inactive labels stay gray.
- Selection label and explanatory copy should update together in an implementation.

### Feature explorer overlay
- Dimmed page behind a large dark panel, close button in the upper corner, stacked options on the left, product demonstration on the right.
- On smaller screens stack options above the demo rather than compressing both columns.

### Dark comparison metrics
- Centered intro, thin separator, comparison dropdown, then evenly distributed metrics with strong value / quiet label hierarchy.
