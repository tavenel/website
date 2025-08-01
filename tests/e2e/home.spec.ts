import { test, expect } from '@playwright/test';
import { HomePage } from './pageObjects/homePage';

let homePage: Promise<HomePage>;

test.beforeEach(async ({ page }) => {
	homePage = new HomePage(page).goto();
});

test('home page title', async ({ page }) => {
	await homePage
		.then(homePage => homePage.checkTitle());
});
