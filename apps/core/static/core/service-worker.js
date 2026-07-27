const CACHE_NAME = 'v1';
const CACHE_ASSETS = [
  '/',
  '/static/core/css/styles.css',
  '/static/core/js/main.js',
  '/static/core/icons/icon-192x192.png',
  '/static/core/icons/icon-512x512.png',
  // add other assets to cache
];

// Install Event
self.addEventListener('install', (e) => {
  console.log('Service Worker: Installing...');
  e.waitUntil(
    caches.open(CACHE_NAME).then(cache => {
      console.log('Service Worker: Caching Files');
      return cache.addAll(CACHE_ASSETS);
    }).then(() => self.skipWaiting())
  );
});

// Activate Event
self.addEventListener('activate', (e) => {
  console.log('Service Worker: Activated');
  // Remove unwanted caches
  e.waitUntil(
    caches.keys().then(keys => {
      return Promise.all(keys.map(key => {
        if (key !== CACHE_NAME) {
          console.log('Service Worker: Removing Old Cache', key);
          return caches.delete(key);
        }
      }));
    })
  );
});

// Fetch Event - serve cached content when offline
self.addEventListener('fetch', (e) => {
  e.respondWith(
    fetch(e.request).catch(() => caches.match(e.request))
  );
});
