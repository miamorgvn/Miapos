/* ============================================================
   MIAPOS v2.14 — API SINKRON OTOMATIS ANTAR HP (Vercel + GitHub)
   ------------------------------------------------------------
   MASALAH YANG DISELESAIKAN (permintaan owner):
   Dulu pindah data ke HP lain harus SCAN QR / tempel kode —
   capek. Sekarang: HP lain cukup MASUK (login) dengan akun yang
   sama (no. HP + kata sandi) → data akun itu otomatis terunduh
   (menu, pesanan, omzet, stok, laporan, pengaturan). Selama
   dipakai, data tiap HP saling mengikuti otomatis (push/pull).

   CARA KERJA:
   - Satu file JSON per akun di folder sync/ repo GitHub:
       sync/acc-<noHP>.json
     Isi: { acc: profil akun (termasuk passHash), store: data
     usaha, updatedAt, deviceId, v }.
   - App melakukan GET (tarik) tiap ±45 detik saat layar aktif,
     dan PUT (kirim) saat datanya berubah (di-throttle app).
   - Merge anti-timpa dilakukan DI HP (client) — server hanya
     menyimpan file terakhir. Pesanan selalu digabung per-ID,
     jadi penjualan yang dibuat HP A saat HP B offline tidak
     pernah hilang.

   ENDPOINT (router by method & query):
   - GET  /api/sync?acc=NOHP            → {ok, data, sha, updatedAt}
   - GET  /api/sync?acc=NOHP&rev=SHA    → {ok, unchanged:true, sha}
            (hemat kuota: 304-style, jawab cuma kalau file berubah)
   - PUT  /api/sync?acc=NOHP            → simpan  {ok, sha, updatedAt}
   - PUT  /api/sync?acc=NOHP&base=SHA   → simpan dengan deteksi
            konflik; kalau base sudah basi → {ok:false,error:'CONFLICT',sha}

   KEAMANAN:
   - Header x-backup-key WAJIB (sama dengan BACKUP_KEY di Vercel,
     key yang sama dipakai fitur Backup Cloud — tidak perlu setup baru).
   - passHash akun disimpan & diverifikasi client (HP baru harus
     tahu kata sandi akun untuk bisa memuat datanya).

   ENV: sama dengan api/backup.js (GITHUB_TOKEN, BACKUP_KEY,
   GITHUB_BRANCH opsional; OWNER/REPO otomatis dari Vercel).
   ============================================================ */
const crypto = require('crypto');

const OWNER = process.env.VERCEL_GIT_REPO_OWNER || process.env.GITHUB_OWNER || '';
const REPO = process.env.VERCEL_GIT_REPO_SLUG || process.env.GITHUB_REPO || '';
const TOKEN = process.env.GITHUB_TOKEN || '';
const KEY = process.env.BACKUP_KEY || '';
const BRANCH = process.env.GITHUB_BRANCH || 'main';
const DIR = 'sync';
const MAX_BODY = 30 * 1024 * 1024; // 30MB cukup untuk data usaha bertahun-tahun

function json(res, code, obj) {
  res.setHeader('Cache-Control', 'no-store');
  res.status(code).json(obj);
}

function keyOk(req) {
  if (!KEY) return false;
  const got = Buffer.from(String(req.headers['x-backup-key'] || ''));
  const want = Buffer.from(KEY);
  return got.length === want.length && crypto.timingSafeEqual(got, want);
}

function accFile(accRaw) {
  const digits = String(accRaw || '').replace(/[^0-9]/g, '').slice(0, 20);
  if (digits.length < 8) return null;
  return 'acc-' + digits + '.json';
}

async function gh(path, opts) {
  opts = opts || {};
  const headers = {
    'Authorization': 'Bearer ' + TOKEN,
    'Accept': 'application/vnd.github+json',
    'X-GitHub-Api-Version': '2022-11-28',
    'User-Agent': 'miapos-sync'
  };
  if (opts.ifNoneMatch) headers['If-None-Match'] = opts.ifNoneMatch;
  if (opts.body) headers['Content-Type'] = 'application/json';
  const r = await fetch('https://api.github.com' + path, {
    method: opts.method || 'GET',
    headers: headers,
    body: opts.body
  });
  let body = null;
  try { body = await r.json(); } catch (e) { body = null; }
  return { ok: r.ok, status: r.status, body: body, etag: r.headers.get('etag') || '' };
}

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

module.exports = async (req, res) => {
  let url;
  try { url = new URL(req.url, 'http://x'); } catch (e) { return json(res, 400, { ok: false, error: 'BAD_URL' }); }
  const file = accFile(url.searchParams.get('acc'));
  if (!file) return json(res, 400, { ok: false, error: 'ACC_TIDAK_VALID' });

  // --- proteksi env + key (semua operasi data) ---
  if (!TOKEN || !KEY || !OWNER || !REPO) {
    return json(res, 500, { ok: false, error: 'SERVER_BELUM_DISET (env GITHUB_TOKEN / BACKUP_KEY)' });
  }
  if (!keyOk(req)) return json(res, 401, { ok: false, error: 'KEY_SALAH' });

  const base = '/repos/' + OWNER + '/' + REPO + '/contents/' + DIR + '/' + file;

  try {
    // ============ TARIK (GET) ============
    if (req.method === 'GET') {
      const rev = (url.searchParams.get('rev') || '').replace(/[^a-f0-9"]/gi, '');
      const g = await gh(base + '?ref=' + encodeURIComponent(BRANCH), rev ? { ifNoneMatch: '"' + rev.replace(/"/g, '') + '"' } : {});
      if (g.status === 304 || (g.status === 200 && rev && g.etag && g.etag.indexOf(rev) !== -1)) {
        return json(res, 200, { ok: true, unchanged: true, sha: rev });
      }
      if (g.status === 404) return json(res, 404, { ok: false, error: 'AKUN_BELUM_ADA_DI_CLOUD' });
      if (!g.ok) return json(res, 502, { ok: false, error: 'GITHUB_ERROR' });
      const sha = (g.body && g.body.sha) || '';
      let data;
      try { data = JSON.parse(Buffer.from((g.body && g.body.content) || '', 'base64').toString('utf8')); }
      catch (e) { return json(res, 500, { ok: false, error: 'FILE_RUSAK' }); }
      return json(res, 200, { ok: true, data: data, sha: sha, updatedAt: (data && data.updatedAt) || '' });
    }

    // ============ KIRIM (PUT) ============
    if (req.method === 'PUT') {
      const body = await readRawBody(req);
      if (!body || typeof body !== 'object' || Array.isArray(body) || !body.store) {
        return json(res, 400, { ok: false, error: 'DATA_TIDAK_VALID' });
      }
      if (!body.acc || !/^[0-9]{8,20}$/.test(String(body.acc.phone || ''))) {
        return json(res, 400, { ok: false, error: 'ACC_TIDAK_VALID' });
      }
      const payload = {
        v: 2,
        acc: body.acc,
        store: body.store,
        deviceId: String(body.deviceId || '').slice(0, 40),
        updatedAt: new Date().toISOString()
      };
      const content = Buffer.from(JSON.stringify(payload)).toString('base64');

      // sha file sekarang (dari param base biar hemat panggilan, atau cek dulu)
      let sha = (url.searchParams.get('base') || '').replace(/[^a-f0-9]/g, '');
      if (!sha) {
        const ex = await gh(base + '?ref=' + encodeURIComponent(BRANCH));
        if (ex.ok && ex.body && ex.body.sha) sha = ex.body.sha;
      }

      const p = await gh(base, {
        method: 'PUT',
        body: JSON.stringify({
          message: 'sinkron akun ' + body.acc.phone.slice(0, 5) + '****',
          content: content,
          branch: BRANCH,
          sha: sha || undefined
        })
      });
      if (p.ok) {
        return json(res, 200, { ok: true, sha: (p.body && p.body.content && p.body.content.sha) || '', updatedAt: payload.updatedAt });
      }
      // 409/422 = file berubah di perangkat lain sejak base → client akan
      // menarik, menggabungkan (merge), lalu mengirim ulang.
      if (p.status === 409 || p.status === 422) {
        const ex2 = await gh(base + '?ref=' + encodeURIComponent(BRANCH));
        return json(res, 200, { ok: false, error: 'CONFLICT', sha: (ex2.ok && ex2.body && ex2.body.sha) || '' });
      }
      return json(res, 502, { ok: false, error: 'GAGAL_COMMIT_GITHUB' });
    }

    // ============ HAPUS (khusus: keluar & hapus akun dari cloud) ============
    if (req.method === 'DELETE') {
      const ex = await gh(base + '?ref=' + encodeURIComponent(BRANCH));
      if (ex.status === 404) return json(res, 200, { ok: true, deleted: true });
      if (!ex.ok) return json(res, 502, { ok: false, error: 'GITHUB_ERROR' });
      const d = await gh(base, {
        method: 'DELETE',
        body: JSON.stringify({ message: 'hapus sinkron akun', branch: BRANCH, sha: ex.body && ex.body.sha })
      });
      return json(res, d.ok ? 200 : 502, { ok: d.ok });
    }

    return json(res, 405, { ok: false, error: 'METHOD_TIDAK_DUKUNG' });
  } catch (e) {
    return json(res, 500, { ok: false, error: 'SERVER_ERROR' });
  }
};
