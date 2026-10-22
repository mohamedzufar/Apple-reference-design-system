# Starter token hypotheses

These are **estimated starting tokens**, not official Apple tokens. Adjust after measuring the source images and testing in the target product.

## Color roles
| Token | Approximate starter | Use |
|---|---|---|
| `--ref-canvas` | `#FFFFFF` | Main content backgrounds |
| `--ref-canvas-tinted` | `#F5F5F7` | Soft neutral section backgrounds |
| `--ref-text` | `#1D1D1F` | Primary typography |
| `--ref-text-muted` | `#6E6E73` | Supporting copy |
| `--ref-divider` | `#D2D2D7` | Thin separators |
| `--ref-link` | `#06C` | Links and primary action accent |
| `--ref-card` | `#FFFFFF` | Cards on tinted backgrounds |
| `--ref-media-dark` | `#000000` | High-contrast feature media |

## Typography hypotheses
- Typeface: modern sans-serif; exact family not verified.
- Hero: fluid, bold, tight line-height, centered where the content is a product statement.
- Section heading: large but less dominant than hero.
- Body: regular weight, medium gray, relaxed line-height.
- Link: body-sized blue text, generally minimal decoration.
- Small metadata: muted and secondary; maintain readable size.

## Spacing/layout hypotheses
- Content max width: roughly 960–1200px in the supplied desktop captures, varies by section.
- Hero top/bottom whitespace: generous, context-specific.
- Section spacing: large enough to create clear story beats.
- Feature rails: use consistent card gaps; show a partial next card where it improves discoverability.
- Footer: denser vertical rhythm than marketing sections.
- Border radius: varies by component; do not assume every surface uses the same radius.

## Suggested CSS variables
```css
:root {
  --ref-canvas: #fff;
  --ref-canvas-tinted: #f5f5f7;
  --ref-text: #1d1d1f;
  --ref-text-muted: #6e6e73;
  --ref-divider: #d2d2d7;
  --ref-link: #06c;
  --ref-card: #fff;
  --ref-media-dark: #000;
  --ref-content-max: 72rem;
  --ref-section-gap: clamp(4rem, 9vw, 9rem);
  --ref-motion-fast: 160ms;
  --ref-motion-base: 240ms;
  --ref-ease: cubic-bezier(.2, 0, 0, 1);
}
```

Do not blindly apply these to every application. Dashboard surfaces may need higher density, different semantic colors, and stronger data states while retaining the reference's restraint and hierarchy.


## Additional role observations from REF-11–REF-20
- `--ref-control-selected`: near-black fill with light text for active segmented tabs; use only for selected states, not as a second primary CTA.
- `--ref-control-muted`: pale neutral capsule background for inactive tabs/options.
- `--ref-panel`: white rounded media/explorer stage on a light-gray section canvas.
- `--ref-action`: saturated blue remains reserved for primary actions and editorial links.

These are semantic roles, not measured official values. Reuse existing approximate palette until pixel sampling is performed. Image-derived oranges, greens, blues, and dark cinematic colors should not be promoted into UI tokens unless the product itself needs them.


## Dark-theme token hypotheses (REF-21–REF-30)
| Token | Approximate starter | Use |
|---|---|---|
| `--ref-dark-canvas` | `#000000` | Main dark page background |
| `--ref-dark-panel` | `#1C1C1E` | Raised explorer/modal surfaces |
| `--ref-dark-text` | `#F5F5F7` | Main heading and high-emphasis text |
| `--ref-dark-muted` | `#86868B` | Supporting copy and labels |
| `--ref-dark-divider` | `#2C2C2E` | Subtle outlines and separators |
| `--ref-dark-link` | `#0A84FF` | Blue navigation action/link |
| `--ref-dark-selection` | `#F5CE00` | Selected camera/aperture option where observed |

Keep dark tokens separate from light tokens. These values are estimates, not verified official colors.
