/* ============================================================
   MIAPOS v2.10 — PUSHLIB (helper bersama untuk api/push-*.js)
   ------------------------------------------------------------
   Penyimpanan push: file backups/miapos-push.json di repo
   GitHub (sama seperti backup data) — ditulis via GitHub
   Contents API, jadi gak butuh database/cloud tambahan.

   Struktur file:
   {
     subs:   [ { id, endpoint, keys:{p256dh,auth}, at } ],  // maks 50
     config: { notifOwnerName, notifMorningText, notifNightText,
               notifNightVibrate, notifOpenTime, notifCloseTime,
               pushServer },
     upd: "<ISO time>"
   }

   ENV (Vercel → Settings → Environment Variables):
   - GITHUB_TOKEN  : wajib (sama dengan backup cloud)
   - BACKUP_KEY    : opsional — dipakai buat auth tes manual
   - GITHUB_BRANCH : default 'main'
   - VAPID_PUBLIC_KEY / VAPID_PRIVATE_KEY : opsional
     (kalau tidak di-set, pakai kunci bawaan Miapos di bawah)
   ============================================================ */
const crypto = require('crypto');

const OWNER = process.env.VERCEL_GIT_REPO_OWNER || process.env.GITHUB_OWNER || '';
const REPO = process.env.VERCEL_GIT_REPO_SLUG || process.env.GITHUB_REPO || '';
const TOKEN = process.env.GITHUB_TOKEN || '';
const KEY = process.env.BACKUP_KEY || '';
const BRANCH = process.env.GITHUB_BRANCH || 'main';
const PUSH_FILE = 'backups/miapos-push.json';
const MAX_SUBS = 50;

// Kunci VAPID bawaan Miapos (boleh ditimpa lewat env di Vercel).
// Publik dipakai juga di index.html (Notif.PUSH_KEY) — pasangan yang sama.
const VAPID_PUBLIC = process.env.VAPID_PUBLIC_KEY ||
  'BOvogKOEW16o1CBz_kntLf7-RV0CRPsQe_A_6LmjOeh5VaZZoPfIRNd12EcUkfeJJBhYpt0xzt2jth_dBTysD7k';
const VAPID_PRIVATE = process.env.VAPID_PRIVATE_KEY ||
  'rhkY2KU_34X0NkuTSBS9evCbTQaajg9uJYRuC__RvzA';
const VAPID_SUBJECT = process.env.VAPID_SUBJECT || 'mailto:owner@miapos.app';

const NOTIF_DEFAULTS = {
  notifOwnerName: 'morgvn',
  notifMorningText: 'Selamat pagi, saatnya memulai kembali bisnis yaaa! Semangat ya hari ini! \u2600\uFE0F',
  notifNightText: 'Sudah jam 9 malam, waktunya tutup. Capek kan? Rest dulu, besok gas lagi! \uD83D\uDE34',
  notifNightVibrate: true,
  notifOpenTime: '08:00',
  notifCloseTime: '21:00',
  pushServer: true
};

function json(res, code, obj) {
  res.setHeader('Cache-Control', 'no-store');
  res.status(code).json(obj);
}

// Auth: cron Vercel selalu boleh; selain itu harus kunci BACKUP_KEY
// (kalau env BACKUP_KEY tidak di-set, tes manual dibolehkan biar gak ribet).
function authOk(req) {
  if (req.headers['x-vercel-cron']) return true;
  if (!KEY) return true;
  const got = String(req.headers['x-backup-key'] || req.query && req.query.key || '');
  if (!got) return false;
  const a = Buffer.from(got); const b = Buffer.from(KEY);
  return a.length === b.length && crypto.timingSafeEqual(a, b);
}

async function gh(path, opts) {
  opts = opts || {};
  const headers = {
    'Authorization': 'Bearer ' + TOKEN,
    'Accept': 'application/vnd.github+json',
    'X-GitHub-Api-Version': '2022-11-28',
    'User-Agent': 'miapos-push'
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

async function readStore() {
  const g = await gh('/repos/' + OWNER + '/' + REPO + '/contents/' + PUSH_FILE + '?ref=' + encodeURIComponent(BRANCH));
  if (g.status === 404) return { sha: null, data: { subs: [], config: {}, upd: null } };
  if (!g.ok) throw new Error('GITHUB_ERROR');
  let data;
  try { data = JSON.parse(Buffer.from((g.body && g.body.content) || '', 'base64').toString('utf8')); }
  catch (e) { data = { subs: [], config: {} }; }
  if (!data || typeof data !== 'object') data = { subs: [], config: {} };
  if (!Array.isArray(data.subs)) data.subs = [];
  if (!data.config || typeof data.config !== 'object') data.config = {};
  return { sha: (g.body && g.body.sha) || null, data: data };
}

async function writeStore(store) {
  store.upd = new Date().toISOString();
  const p = await gh('/repos/' + OWNER + '/' + REPO + '/contents/' + PUSH_FILE, {
    method: 'PUT',
    body: JSON.stringify({
      message: 'miapos push store update',
      content: Buffer.from(JSON.stringify(store.data)).toString('base64'),
      branch: BRANCH,
      sha: store.sha || undefined
    })
  });
  return p.ok;
}

function envSiap() { return !!(TOKEN && OWNER && REPO); }

module.exports = { json, authOk, gh, readStore, writeStore, envSiap, MAX_SUBS, VAPID_PUBLIC, VAPID_PRIVATE, VAPID_SUBJECT, NOTIF_DEFAULTS };
