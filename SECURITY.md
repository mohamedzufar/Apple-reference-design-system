# Security Policy

## Supported Versions

| Version | Supported |
|---------|-----------|
| 1.0.x   | ✅ Active |
| < 1.0   | ❌ No longer maintained |

## Scope

This is a **static, client-side only** project containing:
- HTML, CSS, and Vanilla JavaScript files
- Python validation scripts (run locally, never deployed as a server)
- No server-side code, databases, authentication, or user data collection

The primary security surface is:
- **Dependency supply chain** — npm devDependencies (Playwright) and Python stdlib only
- **Content injection** — any fork/contribution that inserts untrusted URLs or scripts
- **Asset rights** — use of unlicensed images or copyrighted Apple assets

## Reporting a Vulnerability

If you discover a security concern (e.g., a dependency with a known CVE, an unsafe pattern in the JS that could affect users who embed the demo):

1. **Do NOT open a public GitHub issue** for the vulnerability.
2. Open a [GitHub Security Advisory](https://docs.github.com/en/code-security/security-advisories/guidance-on-reporting-and-writing/privately-reporting-a-security-vulnerability) on this repository.
3. Include:
   - Description of the vulnerability
   - Steps to reproduce
   - Potential impact
   - Suggested fix (optional)

You will receive a response within **7 days**. If accepted, a fix will be released within **30 days** and credited in the CHANGELOG.

## Asset & Rights Security

Per the project's `LICENSE` and `README`:
- Do **not** submit pull requests that include unlicensed Apple logos, screenshots, or proprietary assets.
- Do **not** introduce `eval()`, `innerHTML` with user-controlled data, or external resource loading without explicit justification.
- Do **not** include credentials, API keys, or `.env` files in any commit.
