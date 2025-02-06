export class SlideShow {

	private chapters: NodeListOf<HTMLElement>;
	private currentChapter: number = 0;
	private slides: NodeListOf<HTMLElement>;
	private currentSlide: number = 0;

	constructor() {
		this.chapters = document.querySelectorAll("#slides-content .chapter");
		this.slides = this._initNewChapter(false);
	}

	reset() {
		this.currentChapter = 0;
		this.currentSlide = 0;
		this._initNewChapter(false);
	}

	nextChapter(): void {
		if (this.currentChapter >= this.chapters.length - 1) {
			return;
		}
		this._hideSlide();
		this.currentChapter += 1;
		this._initNewChapter(false);
	}

	prevChapter(lastSlide: boolean) {
		if (this.currentChapter <= 0) {
			return;
		}
		this._hideSlide();
		this.currentChapter -= 1;
		this._initNewChapter(lastSlide);
	}

	nextSlide(): void {
		if (this.currentSlide < this.slides.length - 1) {
			this._hideSlide();
			this.currentSlide += 1;
			this._showSlide();
		} else {
			this.nextChapter();
		}
	}

	prevSlide(): void {
		if (this.currentSlide > 0) {
			this._hideSlide();
			this.currentSlide -= 1;
			this._showSlide();
		} else {
			this.prevChapter(true);
		}
	}

	private _hideSlide(): void {
		this.slides[this.currentSlide].style.display = 'none';
	}

	private _showSlide(): void {
		this.slides[this.currentSlide].style.display = 'block';
	}

	private _initNewChapter(lastSlide: boolean) {
		const slides = this.chapters[this.currentChapter].querySelectorAll('.slide-elt') as NodeListOf<HTMLElement>;
		this.slides = slides;
		this.currentSlide = lastSlide ? this.slides.length - 1 : 0; // are we going backwards of forwards ?
		this._showSlide();
		return slides;
	}

};

export function generateSlides() {
	const course = document.getElementById('course') as HTMLElement;
	const slidesContainer = document.getElementById('slides-content') as HTMLElement;

	let currentChapter = createChapter(slidesContainer);
	let newSlide = createSlideDiv(currentChapter);

	let node = course.firstChild
	while (node) {
		// remove from current parent
		course.removeChild(node);

		if (node instanceof Element && node.id.startsWith('layout-section')) {

			currentChapter.removeChild(newSlide); // hack : there is 1 <hr> more because of `---layout:section\n---```

			currentChapter = createChapter(slidesContainer);
			newSlide = createSlideDiv(currentChapter);
		}

		if (node.nodeName === "HR") {
			// `---` => new slide
			newSlide = createSlideDiv(currentChapter);
		} else {
			newSlide.appendChild(node);
		}

		// iterate
		node = course.firstChild;
	}
}

function createChapter(container: HTMLElement) {

	const newDiv = document.createElement("div");
	newDiv.classList.add("chapter");

	container.appendChild(newDiv);

	return newDiv;
}

function createSlideDiv(container: HTMLElement) {

	const newDiv = document.createElement("div");
	newDiv.classList.add("slide-elt", "slide-mode");

	container.appendChild(newDiv);

	return newDiv;
}
