import { expect, type Locator, type Page } from '@playwright/test';
import { MenuComponent } from './components/menu';

export class AboutPage {
	readonly page: Page;
	readonly menu: MenuComponent;

	constructor(page: Page) {
		this.page = page;
		this.menu = new MenuComponent(page);
	}

	async goto() {
		await this.page.goto('/');
		return this;
	}

	async checkTitle() {
		await expect(this.page).toHaveTitle(/about/);
		return this;
	}

	// TODO : check content

}
