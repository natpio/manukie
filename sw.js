const CACHE_NAME = 'manufaktura-v1';
const urlsToCache = [
  '/',
  '/index.html',
  '/sklep.html'
];

self.addEventListener('install', event => {
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(cache => {
        return cache.addAll(urlsToCache);
      })
  );
});

self.addEventListener('fetch', event => {
  event.respondWith(
    caches.match(event.request)
      .then(response => {
        // Zwraca z cache jeśli znajdzie, w przeciwnym razie pobiera z sieci
        return response || fetch(event.request);
      })
  );
});