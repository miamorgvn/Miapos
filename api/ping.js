/* ============================================================
   MIAPOS v2.14 — API PING (Vercel Serverless)
   ------------------------------------------------------------
   Dipanggil aplikasi saat buka untuk deteksi mode:
   - Kalau endpoint ini jawab → app tahu sedang berjalan di
     Vercel dengan fitur CLOUD (backup otomatis ke GitHub).
   - `sync: true` → server punya /api/sync (SINKRON OTOMATIS
     ANTAR HP, v2.14). App versi lama mengabaikan field ini.
   - Kalau tidak ada (file:// offline) → app pakai mode
     STANDALONE, data tetap aman tersimpan di HP.
   ============================================================ */
module.exports = async (req, res) => {
  res.setHeader('Cache-Control', 'no-store');
  res.status(200).json({
    ok: true,
    app: 'miapos',
    server: 'vercel',
    engine: 'cloud',
    version: '2.15',
    sync: true,
    time: new Date().toISOString()
  });
};
