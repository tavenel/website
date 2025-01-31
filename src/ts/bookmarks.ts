export interface BookmarkT {
	page_title: string | undefined;
	section: string | undefined;
	url: string;

}

export class Bookmarks {

	getFromStorage(): BookmarkT[] {
		if (typeof (localStorage.bookmarks) == "undefined") {
			return [];
		} else {
			return JSON.parse(localStorage.bookmarks);
		}
	}

	storeAll(bookmarks: BookmarkT[]) {
		localStorage.bookmarks = JSON.stringify(bookmarks);
	}

	store(bookmark: BookmarkT) {
		const bookmarks = this.getFromStorage();
		bookmarks.push(bookmark);
		this.storeAll(bookmarks);
	}

	remove(bookmark: BookmarkT) {
		console.error('HERE');
		console.error(bookmark);
		const bookmarks = this.getFromStorage();
		this.storeAll(bookmarks.filter(it => { it !== bookmark }));
	}
}
