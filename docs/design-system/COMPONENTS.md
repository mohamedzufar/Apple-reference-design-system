# Component Guidelines

## Navigation
A compact floating or static capsule is suitable for product/marketing pages. Keep the number of top-level items low. On small screens, replace the full navigation with a clear menu control.

## Buttons
- Primary: accent fill, high-contrast label.
- Secondary: neutral surface with a subtle border.
- Inverse: light fill or outline on dark sections.
- Disabled: visibly unavailable and not interactive.
- Loading: preserve the button's dimensions to avoid layout shift.

## Cards
Use cards only when they group related information. Avoid wrapping every paragraph in a card. Separate surfaces with spacing first, borders second, shadows last.

## Forms
Use explicit labels, short helper text, visible focus rings, and inline error messaging. Do not use placeholder text as the only label.

## Media panels
Use a consistent 20–28px radius. Use object-fit intentionally. Provide alt text for meaningful imagery and empty alt text for purely decorative images.

## Feedback
Use concise success/error messages. Toasts should not be the only place where critical information is conveyed.

## Empty and loading states
Explain what happened and provide a useful next action. Skeletons should reflect the final layout rather than flashing generic blocks.
