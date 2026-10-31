/* ============================================================
   MIAPOS v2.10 — API PUSH SUBSCRIBE (Vercel Serverless)
   ------------------------------------------------------------
   HP melakukan pendaftaran push & sinkronisasi konfigurasi notif ke sini.
   Data disimpan ke backups/miapos-push.json di repo GitHub
   (via api/_pushlib.js) — dibaca oleh api/push-send.js saat cron jalan.

   ENDPOINT:
   - POST /api/push-subscribe
       body: { sub: { endpoint, keys:{p256dh, auth} } }   → daftar HP
       body: { config: { notifOwnerName, notifMorningText,
                         notifNightText, notifNightVibrate,
                         notifOpenTime, notifCloseTime, pushServer } }
       body boleh keduanya sekaligus.
   - GET  /api/push-subscribe → status ringan { ok, subs, config, env }

   CATATAN: endpoint push adalah URL rahasia bawaan layanan push
   (sudah unik per HP), jadi penulisan (write) terbuka dengan validasi
   ketat + batas 50 HP. Tidak ada data pelanggan yang tersimpan di sini.
   ============================================================ */
const lib = require('./_pushlib.js');

function readRawBody(req) {
  return new Promise((resolve) => {
    if (req.body) return resolve(req.body);
    const chunks = [];
    req.on('data', (c) => chunks.push(c));
    req.on('end', () => {
      try { resolve(JSON.parse(Buffer.concat(chunks).toString('utf8'))); }
      catch (e) { resolve(null); }
    });
    req.on('error', () => resolve(null));
  });
}

function validSub(sub) {
  return !!(sub && typeof sub.endpoint === 'string' && sub.endpoint.indexOf('https://') === 0 &&
    sub.endpoint.length <= 1200 && sub.keys && typeof sub.keys.p256dh === 'string' &&
    typeof sub.keys.auth === 'string' && sub.keys.p256dh.length <= 512 && sub.keys.auth.length <= 512);
}

function cleanConfig(cfg) {
  const out = {};
  if (!cfg || typeof cfg !== 'object') return out;
  if (cfg.notifOwnerName != null) out.notifOwnerName = String(cfg.notifOwnerName).slice(0, 24);
  if (cfg.notifMorningText != null) out.notifMorningText = String(cfg.notifMorningText).slice(0, 200);
  if (cfg.notifNightText != null) out.notifNightText = String(cfg.notifNightText).slice(0, 200);
  if (cfg.notifNightVibrate != null) out.notifNightVibrate = !!cfg.notifNightVibrate;
  if (cfg.notifOpenTime != null) out.notifOpenTime = String(cfg.notifOpenTime).replace(/[^0-9:]/g, '').slice(0, 5);
  if (cfg.notifCloseTime != null) out.notifCloseTime = String(cfg.notifCloseTime).replace(/[^0-9:]/g, '').slice(0, 5);
  if (cfg.pushServer != null) out.pushServer = !!cfg.pushServer;
  return out;
}

module.exports = async (req, res) => {
  if (req.method === 'GET') {
    // Status ringan (dipakai aplikasi untuk diagnosis). Gak bocorin endpoint.
    try {
      const st = await lib.readStore();
      return lib.json(res, 200, { ok: true, subs: st.data.subs.length,
        config: Object.assign({}, lib.NOTIF_DEFAULTS, st.data.config), env: lib.envSiap() });
    } catch (e) {
      return lib.json(res, 200, { ok: lib.envSiap(), subs: 0, config: lib.NOTIF_DEFAULTS, env: lib.envSiap() });
    }
  }
  if (req.method !== 'POST') return lib.json(res, 405, { ok: false, error: 'METHOD_TIDAK_DUKUNG' });
  if (!lib.envSiap()) return lib.json(res, 500, { ok: false, error: 'SERVER_BELUM_DISET (env GITHUB_TOKEN)' });

  try {
    const body = await readRawBody(req);
    if (!body || typeof body !== 'object') return lib.json(res, 400, { ok: false, error: 'DATA_TIDAK_VALID' });
    const wantSub = body.sub && validSub(body.sub);
    const wantCfg = body.config && typeof body.config === 'object';
    if (!wantSub && !wantCfg) return lib.json(res, 400, { ok: false, error: 'DATA_TIDAK_VALID' });

    const st = await lib.readStore();
    if (wantSub) {
      const id = require('crypto').createHash('sha256').update(body.sub.endpoint).digest('hex').slice(0, 24);
      const entry = { id: id, endpoint: body.sub.endpoint, keys: { p256dh: body.sub.keys.p256dh, auth: body.sub.keys.auth }, at: new Date().toISOString() };
      st.data.subs = st.data.subs.filter((s) => s && s.endpoint !== entry.endpoint);
      st.data.subs.unshift(entry);
      st.data.subs = st.data.subs.slice(0, lib.MAX_SUBS);
    }
    if (wantCfg) st.data.config = Object.assign({}, st.data.config, cleanConfig(body.config));
    const ok = await lib.writeStore(st);
    if (!ok) return lib.json(res, 502, { ok: false, error: 'GAGAL_COMMIT_GITHUB' });
    return lib.json(res, 200, { ok: true, subs: st.data.subs.length });
  } catch (e) {
    return lib.json(res, 500, { ok: false, error: 'SERVER_ERROR' });
  }
};
