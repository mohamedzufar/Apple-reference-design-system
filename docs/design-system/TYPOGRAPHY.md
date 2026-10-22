# Complete Text & Typography System

This file defines the text styles to use consistently across the Light and Dark themes. The values are responsive starting points and should be checked against the supplied visual references when pixel-level matching is required.

## Font family
- Preferred: SF Pro Display / SF Pro Text when available and appropriately licensed.
- Fallback: `-apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif`.
- Code: `SFMono-Regular, Consolas, "Liberation Mono", monospace`.

## Display and heading styles

| Token / class | Desktop target | Weight | Line-height | Letter spacing | Use |
|---|---:|---:|---:|---:|---|
| `text-display-xl` | 72–80px | 600–700 | 1.00–1.06 | -0.05em | Hero headline |
| `text-display-lg` | 56–64px | 600–700 | 1.02–1.08 | -0.045em | Large feature title |
| `text-display-md` | 44–52px | 600 | 1.05–1.12 | -0.04em | Page title |
| `text-heading-xl` | 36–40px | 600 | 1.10–1.18 | -0.035em | Main section heading |
| `text-heading-lg` | 28–32px | 600 | 1.15–1.22 | -0.03em | Section heading |
| `text-heading-md` | 22–24px | 600 | 1.20–1.28 | -0.02em | Card / subsection title |
| `text-heading-sm` | 18–20px | 600 | 1.25–1.35 | -0.015em | Small component title |

## Body and utility styles

| Token / class | Size | Weight | Line-height | Use |
|---|---:|---:|---:|---|
| `text-body-lg` | 18–20px | 400 | 1.45–1.60 | Hero description / lead |
| `text-body` | 16–17px | 400 | 1.45–1.60 | Default reading text |
| `text-body-sm` | 14–15px | 400 | 1.45–1.60 | Supporting information |
| `text-caption` | 12–13px | 400–500 | 1.35–1.50 | Metadata and captions |
| `text-label` | 13–14px | 500–600 | 1.30–1.45 | Form labels |
| `text-button` | 14–16px | 500–600 | 1.00–1.20 | Button labels |
| `text-overline` | 11–12px | 600 | 1.30 | Short category labels; use sparingly |
| `text-code` | 13–14px | 400 | 1.50 | Code and token values |

## Responsive behavior
- Hero text should use `clamp()` so it scales smoothly rather than jumping at breakpoints.
- On small screens, display headings generally reduce to 40–48px, section headings to 30–36px, and body text remains at least 16px for comfortable reading.
- Avoid fixed heights around text; let content wrap naturally.
- Keep paragraph measure near 55–75 characters where practical.
- Use sentence case. Avoid all-caps for long labels.
- Use weight, size, and spacing to create hierarchy before adding color.

## Content rules
- Write short, direct headings.
- Keep one main idea per paragraph.
- Avoid long lines across the full viewport.
- Supporting copy should have a clear contrast from the main heading without becoming too faint.
- Never use placeholder text as the only accessible label.
- Do not use text color alone to convey status; include a label or icon when necessary.
