import { expect, type Locator, type Page } from '@playwright/test';
import { HomePage } from '../homePage';

export class MenuComponent {
	readonly page: Page;
	// readonly getStartedLink: Locator;

	constructor(page: Page) {
		this.page = page;
		// this.getStartedLink = page.locator('a', { hasText: 'Get started' });
	}

	async clickHome() {
		await this.page.getByTestId('menu-home-link').click();
		return new HomePage(this.page);
	}

	async clickAbout() {
		await this.page.getByTestId('menu-about-link').click();
		return new AboutPage(this.page);
	}

	// await expect(this.gettingStartedHeader).toBeVisible();
}
