# 📖 PANDUAN miamotion App v2.0.0

Panduan lengkap: jalan di PC, push ke GitHub, auto-update semua device, jalan di Termux (Android), dan bikin API kamu tetap aman.

---

## 1. Isi Paket

```
miamotion-app/
├── index.html              ← dashboard baru (neon cyber + live stats chart)
├── manifest.webmanifest    ← supaya bisa dipasang sebagai "app" (PWA)
├── sw.js                   ← service worker (offline fallback)
├── icons/                  ← icon app (192 & 512)
├── version.json            ← nomor versi (dipakai auto-update detection)
├── launcher.cpp            ← launcher native C++ (opsional, keren aja 😎)
├── run.sh / run.bat        ← cara cepat nyalain server (Linux/Mac/Termux & Windows)
├── termux/run-app.sh       ← launcher Termux (Widget/Boot)
├── config/
│   ├── config.example.json ← template config
│   └── config.json         ← config asli kamu (DIBUAT OTOMATIS, tidak ikut ke GitHub!)
└── server/
    ├── app.py              ← server Python (serve dashboard + proxy API + stats)
    ├── updater.py          ← auto-update dari GitHub
    ├── api_handler.py      ← (mode lokal) tempat logika API kamu
    ├── data/               ← stats & log update (tidak ikut ke GitHub)
    └── requirements.txt    ← dependensi Python
```

**Yang wajib ada:** Python 3.9+. Yang opsional: `git` (untuk auto-update), compiler C++ (untuk launcher).

---

## 2. Quick Start (PC / Laptop)

```bash
cd miamotion-app
pip install -r server/requirements.txt     # sekali saja
bash run.sh                                # Linux / Mac
run.bat                                    # Windows (double click)
```

Buka **http://localhost:8080** → dashboard siap.

**Cara C++ (biar seperti aplikasi beneran):**

```bash
g++ -O2 -std=c++17 -o launch launcher.cpp
./launch                 # otomatis: cek update → nyalakan server
./launch --check         # tes environment saja
```

> Launcher C++ cuma jembatan: dia yang manggil auto-updater lalu menyalakan server Python. Kalau tidak mau compile, `bash run.sh` hasilnya sama.

---

## 3. Push ke GitHub

### a. Pertama kali

1. Buat repo baru di GitHub (disarankan **Public**; private bisa, lihat §4d).
2. Lalu di folder `miamotion-app`:

```bash
git init -b main
git add .
git commit -m "miamotion app v2.0.0"
git remote add origin https://github.com/USERNAME/NAMA-REPO.git
git push -u origin main
```

> ✅ Aman: `config/config.json` (isi key/token) dan `server/data/` **otomatis tidak ikut** ter-push karena sudah ada di `.gitignore`. Yang ter-push hanya kode, bukan rahasia.

### b. Alur update sehari-hari

```bash
git add .
git commit -m "update: deskripsi perubahan"
git push
```

Selesai. **Semua device yang menjalankan app akan update otomatis** (lihat §4).

### c. Minta update ke aku

Kalau mau aku yang update (frontend baru, fitur baru, dll): tinggal bilang → aku kirim **ZIP** → extract, replace isinya → `git add . && git commit -m "update" && git push` → semua device ikut keupdate otomatis. Version di `version.json` naik, dan dashboard tiap device akan nge-toast *"Update applied!"* lalu reload sendiri.

---

## 4. Auto-Update (semua device)

### a. Cara kerja

```
Kamu push ke GitHub
        │
        ▼  (tiap device, tiap 5 menit)
server Python di tiap device → updater.py
        ├── folder ada .git  → git fetch + reset (mirror repo)
        └── tidak ada .git   → download zipball dari GitHub
        │
        ▼
version.json berubah → dashboard nge-toast → reload otomatis
```

### b. Setup

Edit `config/config.json`:

```json
{
  "repo": "USERNAME/NAMA-REPO",
  "branch": "main",
  "update_interval_sec": 300
}
```

- `repo` = `username/nama-repo` (tanpa `https://`).
- `update_interval_sec`: `300` = cek tiap 5 menit. Isi `0` untuk matikan.
- Cek juga jalan saat app baru dinyalakan (launcher/run.sh selalu panggil updater dulu).

### c. File yang dilindungi

Updater **tidak pernah** menimpa: `config/config.json`, `server/data/` (stats kamu), `.env`. Jadi push apa pun ke repo, config & data tiap device tetap aman.

### d. Repo private

Isi `github_token` di `config/config.json` (Classic token dengan scope `repo`, atau fine-grained read-only). Token itu **hanya tersimpan di device** (config.json di-.gitignore), tidak pernah ikut ter-push.

---

## 5. Termux (Android) + Jadi Aplikasi

### a. Install

Buka app **Termux** (download dari F-Droid, versi Play Store tidak lagi diupdate):

```bash
pkg update -y && pkg upgrade -y
pkg install -y python git clang
git clone https://github.com/USERNAME/NAMA-REPO.git miamotion-app
cd miamotion-app
pip install -r server/requirements.txt
bash termux/run-app.sh
```

Buka Chrome di HP → **http://127.0.0.1:8080** → jalan! (HP lain di WiFi yang sama bisa buka lewat `http://IP-HP:8080`).

### b. Jadi "aplikasi" (icon di homescreen, fullscreen)

1. Chrome HP buka `http://127.0.0.1:8080`
2. Menu **⋮** → **Add to Home screen / Tambahkan ke layar utama**
3. Muncul icon app "miamotion" — dibuka jadi fullscreen tanpa address bar (PWA). Ini cara paling gampang, tanpa ribet. 📱

### c. Shortcut 1-tap (Termux:Widget)

1. Install **Termux:Widget** (F-Droid)
2. `mkdir -p ~/.shortcuts && cp termux/run-app.sh ~/.shortcuts/miamotion`
3. Di homescreen, tambahkan widget "Termux:Widget" → tap **miamotion** → server nyala.

### d. Auto-start saat HP nyala (Termux:Boot)

1. Install **Termux:Boot** (F-Droid), buka sekali
2. `mkdir -p ~/.termux/boot && cp termux/run-app.sh ~/.termux/boot/miamotion`
3. Selesai — tiap HP nyala, server ikut nyala.

### e. Tips

- `termux-wake-lock` (dipanggil otomatis oleh `run-app.sh`) mencegah Android mematikan server.
- Matikan **battery optimization** untuk Termux di Settings → biar tidak dibunuh di background.
- Update lewat GitHub juga jalan di Termux (pastikan `repo` terisi di config).

---

## 6. API Tetap Aman 🔒

Prinsip: **key/token tidak pernah ada di browser atau di repo.** Browser cuma bicara ke `/api/activate` di localhost/server kamu.

Dua mode (pilih di `config/config.json` → `api_mode`):

### Mode `proxy` (paling mudah — default)

Request diteruskan ke API serverless kamu yang sekarang:

```json
{
  "api_mode": "proxy",
  "upstream_api_url": "https://your-app.vercel.app/api/activate",
  "upstream_api_key": ""
}
```

- Kalau API kamu butuh key, isi `upstream_api_key` → dikirim server-side lewat header `x-api-key`, **tidak pernah** sampai ke browser.

### Mode `local` (full offline)

Set `"api_mode": "local"` lalu buka `server/api_handler.py` — tempel logika API kamu di fungsi `handle()` (sudah ada contoh kerangka + format response). Semua eksekusi jalan di device sendiri, tanpa server luar.

### Aturan emas

- ❌ Jangan pernah commit `config/config.json`, `.env`, atau key apa pun.
- ✅ File rahasia tinggal di tiap device (`.gitignore` sudah melindungi).
- ✅ Frontend 100% bebas key — bisa di-push ke repo public tanpa risiko.

---

## 7. Stats & Chart "Akun Berhasil Dieksekusi"

| Kartu | Arti |
|---|---|
| **Executed** | Akun yang sukses di-verify & aktif (angka utama 🎯) |
| **Success rate** | Persentase sukses dari total percobaan verify |
| **Emails sent** | Jumlah email verifikasi terkirim |
| **Failed** | Percobaan yang gagal |

- **Bar chart**: eksekusi sukses 7 hari terakhir. **Donut**: rasio sukses vs gagal. **Live activity**: 10 kejadian terbaru (email disamarkan otomatis).
- **Update tiap 4 detik** (real-time).
- **Server mode** (app localhost/Termux): tercatat di `server/data/stats.json`, akurat lintas browser.
- **Tanpa server** (index.html di hosting statis): fallback ke data browser (localStorage) — tetap jalan tapi per-device.
- Tombol ↺ di card Statistics untuk reset.

---

## 8. Troubleshooting

| Masalah | Solusi |
|---|---|
| `Address already in use` / port terpakai | Ganti `"port"` di `config/config.json` (mis. 8081) |
| Auto-update tidak jalan | Pastikan `repo` terisi, `git` terinstall (atau updater otomatis pakai mode zip), `update_interval_sec` > 0 |
| Repo private gagal fetch | Isi `github_token` di config.json |
| `git safe.directory` error (Termux) | `git config --global --add safe.directory '*'` |
| HP sound/server mati di background | Termux:Boot + wake-lock + matikan battery optimization untuk Termux |
| Lupa config | Hapus `config/config.json` → server buat ulang dari contoh saat restart |
| Chart kosong padahal ada eksekusi | Cek `server/data/stats.json` ada; kalau hosting statis berarti data disimpan di browser itu |

---

## 9. Cheat Sheet

```bash
# PC
bash run.sh                    # nyalakan
g++ -O2 -std=c++17 -o launch launcher.cpp && ./launch

# Update routine
git add . && git commit -m "update" && git push

# Termux
cd ~/miamotion-app && bash termux/run-app.sh

# Cek status update (di device)
cat server/data/last_update.json
```
