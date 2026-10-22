# Optional browser QA tooling

This tooling is not wired into the existing site automatically. It is an opt-in test harness so the current demo behavior is not silently changed.

## Run it
1. Install Node.js (LTS) and npm.
2. In this directory run `npm install`.
3. Install browser binaries with `npx playwright install chromium`.
4. Serve the project root (the directory containing `light/` and `dark/`) on port 8000. For example, from the project root: `python -m http.server 8000`.
5. In another terminal, from this directory run `npm test`.
6. For full-page screenshots run `npm run screenshots`.

Set `BASE_URL` to use a different local URL. The supplied tests are smoke checks, not a full accessibility audit or a guarantee of Apple-reference parity. Review screenshots and add component-specific assertions for the interactions used by your product.

## Optional motion primitives
`motion-primitives.css` and `motion-primitives.js` are reference files. Import them only after checking class names and integrating them with the site's existing reveal logic; do not run two reveal systems on the same elements.
