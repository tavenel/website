import { test, expect } from '@playwright/test';
import { HomePage } from './pageObjects/homePage';
import type { MenuComponent } from './pageObjects/components/MenuComponent';

let menu: MenuComponent;

test.beforeEach(async ({ page }) => {
	const po = new HomePage(page);
	menu = po.menu;
	po.goto();
});

test('home link', async ({ page }) => {

	await menu.clickHome()
		.then(homePage => homePage.checkTitle());
});

test('about link', async ({ page }) => {

	await menu.clickAbout()
		.then(aboutPage => aboutPage.checkTitle());
});

// TODO
// menu-favorites-link
// menu-theme-link
// menu-theme-select
// menu-search
// menu-promo-name
// menu-promo-link
// menu-promo-select
