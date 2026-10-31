/* ============================================================
   MIAPOS v2.9 — API BACKUP CLOUD (Vercel Serverless + GitHub)
   ------------------------------------------------------------
   BACKUP OTOMATIS TANPA TERMUX.
   Data dikirim app (HTTPS) → function ini commit file JSON ke
   folder backups/ di repo GitHub pemilik app → tersimpan aman
   di cloud, bisa dipulihkan kapan pun dari HP mana saja.

   ENDPOINT (satu file, router by method & query):
   - GET  /api/backup              → daftar backup  {ok,backups:[{file,size,time}]}
   - GET  /api/backup?file=NAMA    → isi backup     {ok,file,data}
   - POST /api/backup  (body=data) → simpan backup  {ok,file,total}

   KEAMANAN:
   - Semua akses WAJIB header  x-backup-key: <BACKUP_KEY>
     (sama dengan env BACKUP_KEY yang di-set di Vercel).
   - Banding pakai timingSafeEqual (anti timing-attack).

   ENV WAJIB (di-set di Vercel → Settings → Environment Variables):
   - GITHUB_TOKEN : token GitHub (akses repo ini, Contents: Read&Write)
   - BACKUP_KEY   : password backup bebas, dipakai juga di aplikasi
   ENV OPSIONAL:
   - GITHUB_BRANCH: default 'main' (kalau branch repo lu beda)
   Otomatis dari Vercel (tidak perlu di-set):
   - VERCEL_GIT_REPO_OWNER / VERCEL_GIT_REPO_SLUG

   ROTASI: cukup 7 file terbaru (miapos-backup-YYYY-MM-DD.json),
   satu file per hari (ditimpa kalau hari yang sama backup lagi).
   ============================================================ */
const crypto = require('crypto');

const OWNER = process.env.VERCEL_GIT_REPO_OWNER || process.env.GITHUB_OWNER || '';
const REPO = process.env.VERCEL_GIT_REPO_SLUG || process.env.GITHUB_REPO || '';
const TOKEN = process.env.GITHUB_TOKEN || '';
const KEY = process.env.BACKUP_KEY || '';
const BRANCH = process.env.GITHUB_BRANCH || 'main';
const KEEP = 7;
const DIR = 'backups';

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

async function gh(path, opts) {
  opts = opts || {};
  const headers = {
    'Authorization': 'Bearer ' + TOKEN,
    'Accept': 'application/vnd.github+json',
    'X-GitHub-Api-Version': '2022-11-28',
    'User-Agent': 'miapos-backup'
  };
  if (opts.body) headers['Content-Type'] = 'application/json';
  const r = await fetch('https://api.github.com' + path, {
    method: opts.method || 'GET',
    headers: headers,
    body: opts.body
  });
  let body = null;
  try { body = await r.json(); } catch (e) { body = null; }
  return { ok: r.ok, status: r.status, body: body };
}

const BULAN = ['Jan', 'Feb', 'Mar', 'Apr', 'Mei', 'Jun', 'Jul', 'Agu', 'Sep', 'Okt', 'Nov', 'Des'];
function timeFromName(name) {
  // miapos-backup-2026-10-31.json → "31 Okt 2026"
  const m = /(\d{4})-(\d{2})-(\d{2})/.exec(name || '');
  if (!m) return '-';
  const d = new Date(Number(m[1]), Number(m[2]) - 1, Number(m[3]));
  const pad = (n) => String(n).padStart(2, '0');
  return pad(d.getDate()) + ' ' + BULAN[d.getMonth()] + ' ' + m[1];
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
  const name = (url.searchParams.get('file') || '').replace(/[^a-zA-Z0-9._-]/g, '');

  // --- proteksi env + key (semua operasi data) ---
  if (!TOKEN || !KEY || !OWNER || !REPO) {
    return json(res, 500, { ok: false, error: 'SERVER_BELUM_DISET (env GITHUB_TOKEN / BACKUP_KEY)' });
  }
  if (!keyOk(req)) return json(res, 401, { ok: false, error: 'KEY_SALAH' });

  const base = '/repos/' + OWNER + '/' + REPO + '/contents/' + DIR;

  try {
    // ============ READ (restore) ============
    if (req.method === 'GET' && name) {
      const g = await gh(base + '/' + name + '?ref=' + encodeURIComponent(BRANCH));
      if (!g.ok) return json(res, 404, { ok: false, error: 'BACKUP_TIDAK_ADA' });
      let data;
      try { data = JSON.parse(Buffer.from((g.body && g.body.content) || '', 'base64').toString('utf8')); }
      catch (e) { return json(res, 500, { ok: false, error: 'FILE_RUSAK' }); }
      return json(res, 200, { ok: true, file: name, data: data });
    }

    // ============ LIST ============
    if (req.method === 'GET') {
      const g = await gh(base + '?ref=' + encodeURIComponent(BRANCH));
      if (g.status === 404) return json(res, 200, { ok: true, backups: [] });
      if (!g.ok) return json(res, 502, { ok: false, error: 'GITHUB_ERROR' });
      const backups = (Array.isArray(g.body) ? g.body : [])
        .filter((f) => f && f.type === 'file' && f.name.indexOf('.json') === f.name.length - 5)
        .map((f) => ({ file: f.name, size: f.size || 0, time: timeFromName(f.name) }));
      backups.sort((a, b) => b.file.localeCompare(a.file));
      return json(res, 200, { ok: true, backups: backups });
    }

    // ============ WRITE (backup) ============
    if (req.method === 'POST') {
      const body = await readRawBody(req);
      if (!body || typeof body !== 'object' || Array.isArray(body)) {
        return json(res, 400, { ok: false, error: 'DATA_TIDAK_VALID' });
      }
      const today = new Date().toISOString().slice(0, 10);
      const file = 'miapos-backup-' + today + '.json';

      // sha file kalau sudah ada (timpa hari yang sama)
      let sha;
      const ex = await gh(base + '/' + file + '?ref=' + encodeURIComponent(BRANCH));
      if (ex.ok && ex.body && ex.body.sha) sha = ex.body.sha;

      const p = await gh(base + '/' + file, {
        method: 'PUT',
        body: JSON.stringify({
          message: 'backup otomatis ' + today,
          content: Buffer.from(JSON.stringify(body)).toString('base64'),
          branch: BRANCH,
          sha: sha
        })
      });
      if (!p.ok) return json(res, 502, { ok: false, error: 'GAGAL_COMMIT_GITHUB' });

      // rotasi: sisakan KEEP terbaru
      let total = 1;
      const l = await gh(base + '?ref=' + encodeURIComponent(BRANCH));
      if (l.ok && Array.isArray(l.body)) {
        const files = l.body
          .filter((f) => f && f.type === 'file' && f.name.indexOf('.json') === f.name.length - 5)
          .sort((a, b) => b.name.localeCompare(a.name));
        total = files.length;
        for (const f of files.slice(KEEP)) {
          try {
            await gh(base + '/' + f.name, {
              method: 'DELETE',
              body: JSON.stringify({ message: 'rotasi backup', branch: BRANCH, sha: f.sha })
            });
            total--;
          } catch (e) { /* abaikan */ }
        }
      }
      return json(res, 200, { ok: true, file: file, total: total });
    }

    return json(res, 405, { ok: false, error: 'METHOD_TIDAK_DUKUNG' });
  } catch (e) {
    return json(res, 500, { ok: false, error: 'SERVER_ERROR' });
  }
};
