import { expect, type Locator, type Page } from '@playwright/test';
import { MenuComponent } from './components/MenuComponent';

export class HomePage {
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
		await expect(this.page).toHaveTitle('/home/tavenel');
		return this;
	}

}
