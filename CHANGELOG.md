# Changelog

All notable changes to Reference Studio — Apple-Inspired Design System are documented here.
Format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

---

## [1.0.0] — 2026-10-22 — Initial Public Release

### Added
- `docs/skills/APPLE-DESIGN-SYSTEM-SKILL-V1.0-FINAL.md` — Canonical v1.0 skill with full 10-step pipeline
- `demos/product-story-studio/` — Complete working ProBook product storytelling demo
- `light/` and `dark/` theme specimen directories with full component sets
- `tools/scripts/validate_project.py` — Static project validation (HTML links, IDs, asset references)
- `tools/scripts/audit_accessibility.py` — Accessibility attribute audit (alt, lang, landmarks, skip links)
- `tools/scripts/audit_html.py` — HTML quality checker (title, meta description, heading hierarchy)
- `.github/workflows/validate.yml` — GitHub Actions CI for all static checks
- `.claude/skills/apple-design-system/SKILL.md` — Claude Code skill with full design tokens and blueprints
- `skills/apple-design-system/SKILL.md` — Antigravity IDE compatible skill
- `CLAUDE.md` — Claude Code project instructions and quick command reference
- `LICENSE` — MIT License with Apple independence disclaimer
- `package.json` — npm scripts (`test`, `validate`, `check:js`, `serve`)
- `SECURITY.md` — Vulnerability reporting policy
- `CHANGELOG.md` — This file

### Fixed
- `CONTRIBUTING.md`: broken script path `tools/tools/scripts/` corrected to `tools/scripts/`
- `.github/workflows/validate.yml`: same duplicate-path bug fixed

### Changed
- `docs/skills/` promoted to canonical skill location; historical skills moved to `docs/releases/`

---

## [0.9.0] — Legacy

See `docs/releases/V0.9-CHANGELOG.md` for pre-release history.

## [0.8.0] — Legacy

See `docs/releases/V0.8-RELEASE-NOTES.md`.

## [0.7.0] — Legacy

See `docs/releases/V0.7-ADVANCED-SKILL-RELEASE-NOTES.md`.
