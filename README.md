# Reference Studio — Apple-Inspired Design System v1.0 Final

A reference-informed toolkit for building complete, cinematic product pages from screenshots. It focuses on preserving story order, reproducing visible layout and interactions, native-feeling motion, accessibility, and evidence-based QA. This is an independent project, not affiliated with Apple Inc.

## Start here

1. **Landing page:** open `index.html`.
2. **Main reusable skill:** `docs/skills/APPLE-DESIGN-SYSTEM-SKILL-V1.0-FINAL.md`.
3. **Working product-story demo:** `demos/product-story-studio/index.html`.
4. **Run static checks:** `python tools/scripts/validate_project.py`.

For a local server, run `python -m http.server 8000` from this folder and visit `http://localhost:8000/`.

## Repository structure

```text
.
├── index.html                    # Main v1.0 landing page
├── assets/landing/               # Landing page CSS and JavaScript
├── demos/product-story-studio/   # Working product-storytelling demo
├── light/                        # Light-theme specimens and components
├── dark/                         # Dark-theme specimens and components
├── docs/
│   ├── skills/                   # Current canonical skill
│   ├── design-system/            # Shared foundations and component specs
│   └── releases/                 # Historical skills, changelogs, release notes
├── references/apple-reference-corpus/ # Screenshot corpus and analysis
├── tools/
│   ├── scripts/                  # Static project validation
│   └── qa/v0.9-legacy/            # Optional earlier Playwright/motion tooling
├── .github/                      # GitHub Actions and issue templates
├── README.md
├── CONTRIBUTING.md
└── .gitignore
```

## Storytelling and cloning workflow

1. Inventory the supplied project and authorized assets.
2. Map every screenshot to the page's exact section order.
3. Label findings as observed, inferred, or unknown; don't invent unseen behavior.
4. Implement the entire page from header through footer, including all interactive states.
5. Compare at matching viewport, zoom, state, and scroll position. Fix large geometry differences first.
6. Run static and browser checks, then document what was and wasn't verified.

## Validation

```bash
python tools/scripts/validate_project.py
node --check assets/landing/studio.js
node --check demos/product-story-studio/app.js
```

These are static checks, not proof of pixel-perfect similarity or real-device smoothness. The optional older Playwright tooling is documented under `tools/qa/v0.9-legacy/tooling/README.md`; install its dependencies and run a local server before using it.

## Publish to GitHub

Create an empty repository, then from this folder run:

```bash
git init
git add .
git diff --cached --check
git commit -m "Release Reference Studio v1.0"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
git push -u origin main
```

Replace the URL with your actual repository. If a Git repository already exists, check `git status` and `git remote -v` before changing anything. For GitHub Pages, choose **Settings → Pages → Deploy from a branch → main → /(root)**. Verify paths after publishing under a repository subpath.

## License and asset rights

Choose and add a license before public release. Use only images, fonts, logos, and screenshots you own or are licensed to use. Replace demo copy and placeholder product artwork with your own authorized assets before presenting the demo as a commercial product.
