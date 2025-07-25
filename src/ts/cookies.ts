export function getCookie(name: string): string | null {
	const value = `; ${document.cookie}`;
	const parts = value.split(`; ${name}=`);
	if (parts.length === 2) {
		return parts.pop()?.split(';').shift() || null;
	}
	return null;
}

/**
 * Sets a cookie with the given name and value.
 * @param name The name of the cookie.
 * @param value The value of the cookie.
 * @param days The number of days until the cookie expires. Defaults to 365 days.
 */
export function setCookie(name: string, value: string, days: number = 365): void {
	const date = new Date();
	date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000));
	const expires = `expires=${date.toUTCString()}`;
	document.cookie = `${name}=${value}; ${expires}; path=/`;
}

