/* ============================================================
   MIAPOS v2.10 — API PUSH SEND (Vercel Cron)
   ------------------------------------------------------------
   Ngirim notif buka/tutup resto ke semua HP terdaftar — WALAU
   APP DITUTUP. Dijalankan otomatis oleh Vercel Cron 2x sehari:
     01:00 UTC = 08:00 WIB → notif BUKA
     14:00 UTC = 21:00 WIB → notif TUTUP (+ getar pendek)
   (lihat vercel.json → crons)

   Tes manual dari browser/Owner Zone:
   GET /api/push-send?kind=buka   (header x-backup-key / ?key=)
   → balikan { ok, kind, sent, removed, total }

   Teks & nama pengirim diambil dari config yang owner atur
   di Owner Zone (disinkron lewat /api/push-subscribe).
   ============================================================ */
const lib = require('./_pushlib.js');
const webpush = require('web-push');

webpush.setVapidDetails(lib.VAPID_SUBJECT, lib.VAPID_PUBLIC, lib.VAPID_PRIVATE);

module.exports = async (req, res) => {
  if (req.method !== 'GET') return lib.json(res, 405, { ok: false, error: 'METHOD_TIDAK_DUKUNG' });
  if (!lib.envSiap()) return lib.json(res, 500, { ok: false, error: 'SERVER_BELUM_DISET (env GITHUB_TOKEN)' });
  if (!lib.authOk(req)) return lib.json(res, 401, { ok: false, error: 'KEY_SALAH' });

  // ---- tentukan jenis notif: param ?kind= atau jam WIB (UTC+7) ----
  let kind = String((req.query && req.query.kind) || '').toLowerCase();
  if (kind !== 'buka' && kind !== 'tutup') {
    const wibHour = (new Date().getUTCHours() + 7) % 24;
    if (wibHour === 1) kind = 'buka';
    else if (wibHour === 14) kind = 'tutup';
    else return lib.json(res, 400, { ok: false, error: 'KIND_TIDAK_JELAS (pakai ?kind=buka|tutup)' });
  }

  try {
    const st = await lib.readStore();
    const cfg = Object.assign({}, lib.NOTIF_DEFAULTS, st.data.config);
    if (cfg.pushServer === false) {
      return lib.json(res, 200, { ok: true, kind: kind, skipped: 'PUSH_MATI (dimatikan di Owner Zone)', sent: 0, removed: 0, total: st.data.subs.length });
    }
    const owner = String(cfg.notifOwnerName || 'morgvn').trim() || 'morgvn';
    const text = kind === 'buka' ? cfg.notifMorningText : cfg.notifNightText;
    const title = kind === 'buka' ? '\u2600\uFE0F Miapos \u00B7 Buka Resto' : '\uD83C\uDF19 Miapos \u00B7 Waktunya Tutup';
    const vib = kind === 'tutup'
      ? (cfg.notifNightVibrate === false ? [60, 40, 60] : [220, 130, 220])
      : [80, 40, 80];
    const payload = JSON.stringify({ title: title, body: owner + ': ' + text, tag: 'miapos-' + kind, vibrate: vib, url: './' });

    let sent = 0, failed = 0;
    const dead = [];
    const results = await Promise.allSettled(st.data.subs.map((s) =>
      webpush.sendNotification({ endpoint: s.endpoint, keys: s.keys }, payload, { TTL: 12 * 3600 })
    ));
    results.forEach((r, i) => {
      if (r.status === 'fulfilled') sent++;
      else {
        failed++;
        const code = r.reason && r.reason.statusCode;
        if (code === 404 || code === 410) dead.push(st.data.subs[i].endpoint); // langganan mati → buang
      }
    });
    if (dead.length) {
      st.data.subs = st.data.subs.filter((s) => dead.indexOf(s.endpoint) === -1);
      try { await lib.writeStore(st); } catch (e) { /* abaikan */ }
    }
    return lib.json(res, 200, { ok: true, kind: kind, title: title, body: owner + ': ' + text, sent: sent, failed: failed, removed: dead.length, total: st.data.subs.length });
  } catch (e) {
    return lib.json(res, 500, { ok: false, error: 'SERVER_ERROR' });
  }
};
