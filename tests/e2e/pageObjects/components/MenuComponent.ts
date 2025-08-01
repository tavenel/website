import type { Page } from 'playwright';
import { HomePage } from '../homePage';
import { AboutPage } from '../aboutPage';


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

}

