const { test } = require('@playwright/test');
const path = require('path');
const fs = require('fs');

test('capture light and dark reference pages', async ({ page }, testInfo) => {
  const output = path.join(testInfo.config.rootDir, 'screenshots');
  fs.mkdirSync(output, { recursive: true });
  for (const theme of ['light', 'dark']) {
    await page.goto(`/${theme}/index.html`, { waitUntil: 'networkidle' });
    await page.screenshot({ path: path.join(output, `${theme}-${testInfo.project.name}.png`), fullPage: true });
  }
});
