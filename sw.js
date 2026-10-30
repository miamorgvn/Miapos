/* ============================================================
   MIAPOS SERVICE WORKER — AUTO-UPDATE
   ------------------------------------------------------------
   Cara kerja:
   1. Setiap aplikasi dibuka saat online → SW ambil versi TERBARU
      dari jaringan dulu (network-first). Kalau gagal/putus
      internet → baru pakai cache (tetap bisa dipakai offline).
   2. Ada versi baru di server? SW langsung aktif (skipWaiting),
      halaman di-reload otomatis oleh app → pengguna langsung
      pakai versi baru TANPA ngapa-ngapain.
   3. Ubah CACHE name di bawah tiap rilis (mis. miapos-v2.6)
      supaya cache lama otomatis dibuang.
   Tidak jalan di file:// (Termux) — aman, app tetap offline.
   ============================================================ */

const CACHE = 'miapos-v2.6';

const CORE = [
  './',
  './index.html',
  './miapos.html',
  './manifest.json',
  './favicon.ico',
  './icon-192.png',
  './icon-512.png',
  './lib/react.min.js',
  './lib/react-dom.min.js',
  './lib/babel.min.js',
  './lib/tailwind.js',
  './lib/lucide.min.js'
];

self.addEventListener('install', (e) => {
  e.waitUntil(
    caches.open(CACHE)
      .then((c) => c.addAll(CORE))
      .then(() => self.skipWaiting())
  );
});

self.addEventListener('activate', (e) => {
  e.waitUntil(
    caches.keys()
      .then((keys) => Promise.all(keys.filter((k) => k !== CACHE).map((k) => caches.delete(k))))
      .then(() => self.clients.claim())
  );
});

self.addEventListener('fetch', (e) => {
  const req = e.request;
  if (req.method !== 'GET') return;
  let url;
  try { url = new URL(req.url); } catch (err) { return; }
  if (url.origin !== location.origin) return;

  // NETWORK-FIRST: versi baru selalu menang; offline pakai cache
  e.respondWith(
    fetch(req)
      .then((res) => {
        if (res && res.ok) {
          const copy = res.clone();
          caches.open(CACHE).then((c) => c.put(req, copy));
        }
        return res;
      })
      .catch(() =>
        caches.match(req).then((hit) => {
          if (hit) return hit;
          if (req.mode === 'navigate') return caches.match('./index.html');
          return undefined;
        })
      )
  );
});
