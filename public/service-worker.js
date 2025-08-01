const APP_PREFIX = 'avenel_';
const VERSION = '02';

// Files available offline
const URLS_INSTALLED = [
	`/`,
	`/icons/favicon.svg`,
	`/icons/android-chrome-192x192.png`,
	`/icons/android-chrome-512x512.png`,
	`/icons/apple-touch-icon.png`,
	`/index.html`,
]

const CACHE_NAME = APP_PREFIX + VERSION

// Cache install - init when the PWA is installed (1st visit to the website)
self.addEventListener('install', function (e) {
	e.waitUntil(
		caches.open(CACHE_NAME).then(function (cache) {
			return cache.addAll(URLS_INSTALLED)
		})
	)
})

self.addEventListener('activate', function (e) {
	e.waitUntil(
		caches.keys().then(function (keyList) {
			var cacheWhitelist = keyList.filter(function (key) {
				return key.indexOf(APP_PREFIX)
			})
			cacheWhitelist.push(CACHE_NAME);
			return Promise.all(keyList.map(function (key, i) {
				if (cacheWhitelist.indexOf(key) === -1) {
					return caches.delete(keyList[i])
				}
			}))
		})
	)
})

// Fetch of any ressource in the PWA.
// Strategy is : network 1st - cache 2nd
// https://developer.chrome.com/docs/workbox/caching-strategies-overview/
self.addEventListener('fetch', (event) => {
	// Check if this is a navigation request
	if (event.request.mode === 'navigate') {
		// Open the cache
		event.respondWith(caches.open(CACHE_NAME).then((cache) => {
			// Go to the network first
			return fetch(event.request.url).then((fetchedResponse) => {
				cache.put(event.request, fetchedResponse.clone());

				return fetchedResponse;
			}).catch(() => {
				// If the network is unavailable, get
				return cache.match(event.request.url);
			});
		}));
	} else {
		return;
	}
});
