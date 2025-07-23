export class TOC {
	private tocContainer: HTMLUListElement;
	private headings: HTMLElement[] = [];
	private tocLinks: HTMLAnchorElement[] = [];
	private sections: HTMLElement[] = [];
	// stack[level] holds the most recent <li> for that heading level
	private stack: Array<HTMLLIElement | null> = [];

	constructor(
		private tocSelector: string,
		private contentSelector: string,
		private maxLevel: number // max heading level (h1 to h4)
	) {
		const container = document.querySelector<HTMLUListElement>(this.tocSelector);
		if (!container) {
			throw new Error(`TOC container not found: ${this.tocSelector}`);
		}
		this.tocContainer = container;
	}

	public init(): void {
		this.collectHeadings();
		this.buildTOC();
		this.setupScrollSpy();
	}

	private collectHeadings(): void {
		const sel = Array.from({ length: this.maxLevel }, (_, i) => `h${i + 1}`).join(', ');
		this.headings = Array.from(
			document.querySelectorAll<HTMLElement>(`${this.contentSelector} ${sel}`)
		);
	}

	private buildTOC(): void {
		// reset stack
		this.stack = new Array(this.maxLevel + 1).fill(null);

		this.headings
			.slice(1) // 1st element is the 'Chapitres' heading
			.forEach(heading => {
				const level = this.getLevel(heading.tagName);
				if (!level || level > this.maxLevel) return;

				// ensure ID
				if (!heading.id) heading.id = this.slugify(heading.textContent || '');

				const li = this.createListItem(heading.id, heading.textContent || '', level);

				// find parent <ul> for this level
				const parentUl = this.getParentListForLevel(level);
				parentUl.appendChild(li);

				// update stack: this level gets this li, deeper levels reset
				this.stack[level] = li;
				for (let l = level + 1; l <= this.maxLevel; l++) {
					this.stack[l] = null;
				}
			});
	}

	private setupScrollSpy(): void {
		this.tocLinks = Array.from(
			this.tocContainer.querySelectorAll<HTMLAnchorElement>('a')
		);
		this.sections = this.tocLinks
			.map(a => document.getElementById(a.hash.slice(1)))
			.filter((el): el is HTMLElement => el !== null);

		window.addEventListener('scroll', () => this.onScroll());
		this.onScroll();
	}

	private onScroll(): void {
		const offset = 100;
		const idx = this.sections.findIndex((sec, i) => {
			const top = sec.getBoundingClientRect().top;
			const next = this.sections[i + 1];
			return top <= offset && (!next || next.getBoundingClientRect().top > offset);
		});

		this.tocLinks.forEach(a => a.classList.remove('active'));
		if (idx >= 0) this.tocLinks[idx].classList.add('active');
	}

	// Helpers

	/** Convert "H2" → 2 */
	private getLevel(tag: string): number | null {
		const m = tag.match(/^H([1-9])$/);
		if (!m) return null;
		return parseInt(m[1], 10);
	}

	/** Create <li><a href=...>text</a></li>, also tracks links for scroll-spy */
	private createListItem(id: string, text: string, level: number): HTMLLIElement {

		const link = document.createElement('a');
		link.href = `#${id}`;
		link.textContent = text;
		// Add class h1, h2, ... to each heading
		link.classList.add(`toc-h${level}`);

		const li = document.createElement('li');
		li.appendChild(link);
		this.tocLinks.push(link);
		return li;
	}

	/**
	 * For a heading of `level`, returns the <ul> under which its <li> should be appended:
	 * - level=1 → the root tocContainer
	 * - level>1 → the nested <ul> inside the most recent <li> at level-1 (creating it if needed)
	 */
	private getParentListForLevel(level: number): HTMLUListElement {
		if (level === 1) return this.tocContainer;

		const parentLi = this.stack[level - 1];
		if (!parentLi) {
			// no preceding higher-level heading: fall back to root
			return this.tocContainer;
		}

		let subUl = parentLi.querySelector<HTMLUListElement>('ul');
		if (!subUl) {
			subUl = document.createElement('ul');
			parentLi.appendChild(subUl);
		}
		return subUl;
	}

	private slugify(text: string): string {
		return text
			.toLowerCase()
			.trim()
			.replace(/[^\w]+/g, '-');
	}
}

