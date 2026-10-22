const { test, expect } = require('@playwright/test');

test('page loads and has a document title', async ({ page }) => {
  const errors = [];
  page.on('pageerror', error => errors.push(error.message));
  await page.goto('/light/index.html', { waitUntil: 'domcontentloaded' });
  await expect(page.locator('body')).toBeVisible();
  await expect(page).toHaveTitle(/.+/);
  expect(errors, `page errors: ${errors.join('; ')}`).toEqual([]);
});

test('page has no horizontal overflow at the current viewport', async ({ page }) => {
  await page.goto('/light/index.html', { waitUntil: 'domcontentloaded' });
  const sizes = await page.evaluate(() => ({
    viewport: document.documentElement.clientWidth,
    document: document.documentElement.scrollWidth,
    body: document.body.scrollWidth,
  }));
  expect(Math.max(sizes.document, sizes.body), JSON.stringify(sizes)).toBeLessThanOrEqual(sizes.viewport + 1);
});

test('reduced motion preference can be applied without a page crash', async ({ page }) => {
  await page.emulateMedia({ reducedMotion: 'reduce' });
  await page.goto('/light/index.html', { waitUntil: 'domcontentloaded' });
  await expect(page.locator('body')).toBeVisible();
  const preference = await page.evaluate(() => matchMedia('(prefers-reduced-motion: reduce)').matches);
  expect(preference).toBeTruthy();
});
