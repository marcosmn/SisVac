importScripts("/static/precache-manifest.6c8c32ca236d9815ab81ccd24df66c3c.js", "/static/workbox-v4.3.1/workbox-sw.js");
workbox.setConfig({modulePathPrefix: "/static/workbox-v4.3.1"});



workbox.core.setCacheNameDetails({prefix: "frontend"});

self.addEventListener('message', (event) => {
  if (event.data && event.data.type === 'SKIP_WAITING') {
    self.skipWaiting();
  }
});

/**
 * The workboxSW.precacheAndRoute() method efficiently caches and responds to
 * requests for URLs in the manifest.
 * See https://goo.gl/S9QRab
 */
self.__precacheManifest = [].concat(self.__precacheManifest || []);
workbox.precaching.precacheAndRoute(self.__precacheManifest, {});

