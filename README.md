<div align="center">

# 🍜 Miapos — Kasir & Manajemen Restoran

**Aplikasi kasir (POS) yang jalan 100% offline di HP.**
Buat warung, kafe, kedai, sampai resto — kasir, dapur, stok, laporan, semua ada. 🚀

![versi](https://img.shields.io/badge/versi-2.16-10b981?style=flat-square&labelColor=0f172a)
![PWA](https://img.shields.io/badge/PWA-offline%20ready-5A0FC8?style=flat-square&labelColor=0f172a)
![teknologi](https://img.shields.io/badge/React%20%2B%20Tailwind-single%20file%20HTML-orange?style=flat-square&labelColor=0f172a)
![mesin](https://img.shields.io/badge/Python%20%2B%20C%2B%2B-engine-blue?style=flat-square&labelColor=0f172a)

</div>

---

## 🤔 Ini Apaan?

Miapos itu aplikasi kasir bergaya **Progressive Web App (PWA)** — buka di browser HP,
tambah ke home screen, jadilah aplikasi kaya punya restoran beneran. ⚡

Yang bikin beda:

- 📴 **100% offline** — internet mati? Gak masalah, jualan terus. Semua data tersimpan di HP sendiri.
- 📄 **Satu file aja** — inti aplikasinya cuma `index.html`. Copy, backup, pindah HP = gampang.
- 🏪 **Lengkap** — kasir, dapur, stok bahan, laporan, multi-cabang, printer, QRIS. Nggak perlu bayar langganan bulanan. 💸

---

## ✨ Fitur

### 👤 Akun & Sinkron Antar HP (baru di v2.14, dibenerin di v2.15!)
- **Satu akun untuk semua HP** — daftar sekali (nama, no. HP, usaha, alamat, kata sandi), data usaha tersimpan per akun
- 🔄 **Sinkron OTOMATIS** — HP lain login ke akun yang sama → menu, pesanan, omzet, stok, laporan **langsung masuk sendiri**. Gak perlu input ulang, gak perlu scan QR di tiap HP 🎉
- 🔑 **v2.15: cukup kata sandi akun** — gak perlu setel password Backup Cloud lagi buat sinkron!
  Server menerima kata sandi akun yang lu ketik waktu login (jalur password backup lama tetap jalan).
- ⚡ **Real-time dua arah** — HP A nambah menu → HP B otomatis ke-update (polling tiap ±45 detik saat online; offline tetap jalan, begitu online ketrimbalan sendiri)
- 🛡️ **Anti tabrakan data** — penghapusan juga ikut tersinkron (tombstone), edit barengan tetap aman
- 🩺 **Status sinkron yang jujur (v2.15)** — kartu akun nunjukin kenapa sync gak jalan (belum login, server belum ada, password salah) + tombol **Sinkron sekarang** selalu bisa dicoba
- 📷 **QR Akun** tetap ada buat kondisi offline — pindai → konfirmasi → data utuh ke-load tanpa internet
- Ada **Ubah Akun** (ganti nama/nomor/kata sandi) & **Keluar** (log out — data akun tetap aman & bisa dimuat lagi)
- Butuh deployment Vercel/Termux (server Python `main.py` / API `api/sync.js`) — GitHub Pages gak bisa sinkron otomatis

### 🧾 Kasir & Pembayaran
- Buat pesanan cepat, keranjang, promo & diskon
- Metode bayar **Tunai / QRIS / Transfer** — QRIS resto bisa upload gambar sendiri 📱
- 📝 **Catatan per menu** — di bawah tiap menu di keranjang ada kolom catatan sendiri
  (contoh: "pedas, tanpa es" buat Mie Ayam-nya aja) — walau pesanannya udah masuk
- Nota otomatis: cetak struk kasir, nota dapur, dan nota **tambahan** (item yang ditambah belakangan)
- Nama menu di nota dicetak **huruf normal** (bukan KAPITAL semua) — hemat kertas 👍
- ✂️ **Garis `====` cukup satu (baru di v2.16!)** — dulu nota kasir & nota dapur masing-masing punya 2 garis `====`, sekarang cukup 1 garis di bawah header — kertas lebih hemat, gak keliatan dobel
- 💰 **Biaya Tambahan (v2.19)** — di detail pesanan ada tombol **Tambah Biaya Tambahan**: isi Nama Biaya + Jumlah Biaya → Simpan. Biaya di luar menu (ongkos kirim, packing, dll) ikut ke total tagihan, tercetak di struk kasir, dan bisa dihapus lagi sebelum bayar
- 🎨 **Tombol biaya ikut tema (baru di v2.20!)** — dulu selalu merah, sekarang warnanya ikut tema yang dipilih (Emerald/Royal/Pink/Charcoal) — konsisten sama tombol lain
- 🖨️ **Pratinjau Nota kini 3 tab (baru di v2.19!)** — Nota Kasir, Nota Dapur, dan **Nota Dapur-Tambahan** — bentuk nota tambahan bisa dilihat dulu di Pengaturan
- 📏 **Judul DAPUR sebesar No. Antrian (baru di v2.17!)** — tulisan DAPUR di kepala nota dapur dicetak tinggi dobel (lonjong), sama persis kaya No. Antrian di bawahnya — headernya jelas keliatan dari jauh 🍳
- 🖨️ **Popup hasil cetak (baru di v2.16!)** — habis cetak, popup langsung bilang **berhasil dikirim ke printer apa** atau **gagal + alasannya** (plus tombol salin teks nota buat cetak manual) — gak perlu bolak-balik ngecek printer
- Habis bayar langsung muncul 2 tombol: **Cetak Dapur** (dapur langsung masak) & **Struk Kasir** 🖨️
- Label "Tambahan" cuma tampil di app — nota cetakan tetap bersih ✨

### 📷 Scan Barcode & QR Buat Input Menu
- Scan barcode/QR pakai kamera → menu langsung masuk, tanpa ngetik satu-satu
- **QR Massal**: 1 QR bisa berisi *banyak menu sekaligus* (ratusan menu pun bisa) —
  scan sekali, semua menu langsung kebagi kategori masing-masing 🤯
- Bisa scan dari galeri, ada fallback ketik manual, parser harganya paham
  `27.000`, `Rp27.500`, `25rb`, `27k` — format Indonesia semua
- Anti dobel: menu yang sama gak bakal keinput dua kali

### 📊 Laporan & Laporan Menu
- Omzet hari ini, jumlah transaksi, tren, metode pembayaran
- **Laporan Menu**: apa aja yang kejual, berapa qty, ke-sortir dari yang paling laris 🏆 (+ medali 3 besar)
- 💳 **Laporan Pembayaran (baru di v2.14!)** — ada di **Pengaturan → Laporan Pembayaran**:
  lihat hari ini orang bayar pakai apa aja (Tunai/QRIS/Transfer), per metode & per transaksi
- 📅 Bisa lihat **hari-hari sebelumnya** — tinggal ketuk tanggal di atas (kalender),
  sama persis kaya laporan menu: panah mundur/maju + tombol cepat Hari Ini / Kemarin
- Bisa intip tanggal kemarin, mundur sampai belakang — pesanan lama yang terarsip tetap kehitung
- 📐 **Angka otomatis menyesuaikan lebar kartu (baru di v2.16!)** — omzet sepanjang apapun tampil utuh, gak ada lagi "Rp4.081.00…" kepotong di kartu laporan menu & laporan pembayaran

### 📦 Stok & Bahan Baku
- Kelola bahan baku, stok masuk/keluar, peringatan stok menipis
- Fitur Modal & HPP (harga pokok penjualan) buat yang mau ngitung laba & margin 💰

### 🏪 Multi Cabang & Multi Kasir
- Banyak cabang/outlet dalam satu app, data kepisah per outlet
- Kasir bertugas dengan PIN masing-masing, ganti sesi sekali ketuk

### 🖨️ Nota & Printer
- Header nota bisa diganti sendiri (nama resto, alamat, ucapan)
- Sambung printer kasir & printer dapur terpisah
- Tombol cetak dapur ada menu **Cetak Dapur / Cetak Tambahan** 🔖

### 🌤️ Dashboard yang Gak Membosankan
- Kartu cuaca hari ini (data Open-Meteo) + **jam live** keren di kartu
- Salam otomatis yang ganti pagi/siang/sore/malam + kalimat santai acak biar kasir gak bete 😄

### ☁️ Backup Cloud & Update Otomatis
- Backup otomatis ke GitHub (pakai token lu sendiri) — data aman walau HP ilang
- Update app? Timpa file ke repo → semua HP otomatis ke-refresh tanpa ngapa-ngapain 🔄
- Reset data dikunci konfirmasi **5 detik** — biar gak ke pencet gak sengaja (pernah kejadian 😅)

### 🌏 2 Bahasa — Indonesia / English
- Pengaturan → **Bahasa** → pilih Indonesia atau English — tersimpan otomatis 💬
- ✍️ **Bahasa makin baku (v2.16)** — seluruh teks aplikasi dirapikan jadi bahasa Indonesia baku (sapaan dashboard, tips, pesan error, semua) — gak ada lagi kata gaul

### 🎨 Puluhan Sentuhan Kecil
- **4 tema warna**: Emerald & Slate · Royal & Orange (beneran oranye! 🍊) ·
  Pink & Putih 🌸 · Charcoal Dark — ganti tema = seluruh app ikut berubah instan
- Mode layar penuh (judul gak ketutup lensa kamera),
  scan QRIS dari galeri, kategori menu bebas dibuat/dihapus, dan lain-lain

---

## 🚀 Cara Pakai

### 1️⃣ Buat jadi app di HP (paling gampang)
1. Buka alamat app-nya di Chrome Android / Safari iPhone
2. Menu browser → **"Tambahkan ke layar utama"** (Add to Home Screen)
3. Selesai — ikonnya nongol kaya app biasa, buka langsung full screen 📲

### 2️⃣ Upload ke hosting
Bebas: GitHub Pages, Netlify, Vercel, atau hosting sendiri.
Tinggal unggah isi folder ini (termasuk folder `lib/`) — jangan lupa semua file-nya ya.

### 3️⃣ Jalanin lokal (Termux / laptop)
```bash
# dari folder ini, tinggal:
python3 -m http.server 8080
# buka http://localhost:8080
```

---

## 🔄 Update Versi Baru

App ini pakai **Service Worker** dengan pola *network-first*:

1. Timpa file lama pakai file baru di repo
2. Pengguna buka app (saat online) → otomatis ambil versi terbaru
3. Cache lama terhapus sendiri — nama cache di `sw.js` diganti tiap rilis
   (mis. `miapos-v2.20-r1`), jadi jangan lupa ganti kalau ikut ngerilis 🔁

> 💡 Aturan project ini: **setiap update, versi selalu naik** (2.18 → 2.19 → 2.20 → ...).

---

## 🗂️ Struktur File

| File | Fungsi |
| --- | --- |
| `index.html` | 🌟 **Seluruh aplikasi** — React + Tailwind, satu file |
| `sw.js` | Service worker: auto-update + cache offline |
| `manifest.json` | Identitas PWA (nama, ikon, warna) |
| `lib/` | Library bundel (React, Babel, Tailwind, Lucide) — offline semua |
| `engine/` | Native engine C++ (opsional, dipanggil server Python) |
| `api/` | Serverless functions buat backup cloud & sinkron akun (Vercel) |
| `main.py` | Server Python lokal/Termux — backup cloud + API sinkron akun |
| `sync/` | Data sinkron per akun (`acc-<noHP>.json`) |
| `.well-known/assetlinks.json` | Buat build Android (TWA / Play Store) |
| `PANDUAN-*.txt` | 📚 Panduan lengkap tiap fitur (bahasa santai) |

---

## 🛠️ Teknologi

- ⚛️ **React + Tailwind CSS** — UI-nya, dibundel lokal jadi tetap jalan offline
- 📷 **BarcodeDetector API** — scan barcode/QR native Chrome, tanpa library kamera eksternal
- ⚙️ **Service Worker** — auto-update, background sync, periodic sync
- 🐍 **Python + C++ Engine** — server bridge & mesin lokal opsional buat backup/olah data
- 🌤️ **Open-Meteo** — data cuaca gratis, tanpa API key

---

## 📚 Dokumentasi Lengkap

Semua panduan ada di file teks, bahasanya santai & langkah demi langkah:

| Panduan | Isinya |
| --- | --- |
| `README.txt` | Catatan lengkap tiap versi + fitur |
| `CHECKLIST-UPDATE.txt` | Checklist semua fitur & langkah update |
| `PANDUAN-GITHUB.txt` | Upload ke GitHub + backup cloud otomatis |
| `PANDUAN-SCAN.txt` | Scan barcode/QR (termasuk format QR massal) |
| `PANDUAN-PLAYSTORE.txt` | Jadiin app Android beneran |
| `PANDUAN-TERMUX.txt` | Jalanin di HP pakai Termux |
| `PANDUAN-BACKUP-CLOUD.txt` | Backup otomatis ke GitHub |

---

## 🧾 Riwayat Versi (ringkas)

| Versi | Yang baru |
| --- | --- |
| **v2.20** | 🎨 tombol **Tambah Biaya Tambahan** ikut warna tema (bukan merah tetap) · 💬 teks random kartu cuaca **ditulis ulang** — kaya teman ngobrol santai, gak baku/gak kaku · ⏱️ teksnya **dikunci 5 menit** — gak ganti tiap pindah layar, ganti sendiri tiap 5 menit · 🔢 **Laporan Pembayaran diurut No. Antrian** kecil → besar · 🌙 **No. Antrian auto-reset ganti hari** (jam 12 malam waktu HP → besok mulai 1 lagi) · 🧹 file notif tersisa (PANDUAN-NOTIF.txt, api/push-*) **dihapus permanen** dari repo |
| **v2.19** | 💰 **Biaya Tambahan** di detail pesanan (nama + jumlah, ikut total & struk kasir) · 🔁 menu yang sama di sheet tambah item **digabung** (qty nambah, gak bikin baris baru) · ✏️ tombol & sheet "Tambah Menu" di detail pesanan jadi **"Tambah Pesanan"** + tampil jumlah item di bawah tombol + · 🖨️ pratinjau nota kini ada tab **Nota Dapur-Tambahan** · 📱 **tombol back navigasi HP jalan di dalam app**: detail pesanan → daftar pesanan → Dashboard (back kedua di Dashboard keluar app, ada pengingat dulu) |
| **v2.18** | 🚀 No. Antrian di nota dapur dikasih **jeda satu baris** dari daftar menu — gak nempel lagi, lebih lega dibaca |
| **v2.17** | 📏 judul **DAPUR** di nota dapur dicetak tinggi dobel (lonjong) — sama besar kaya No. Antrian, headernya gampang dicari di tumpukan nota |
| **v2.16** | ✂️ garis `====` di nota cukup satu (kasir & dapur, hemat kertas) · 🖨️ popup hasil cetak: berhasil/gagal selalu tertera, gak perlu ngecek printer bolak-balik · 📐 angka laporan otomatis menyesuaikan lebar kartu (fix "Rp4.081.00…" kepotong) · ✍️ seluruh teks app dibikin bahasa baku |
| **v2.15** | 🔑 Sinkron cukup pakai kata sandi akun (tanpa setel password backup) · 🩺 status sinkron jujur + tombol sync yang gak gagal diam · 🛠️ fix: menu gak ikut ke HP lain karena auth kegagalan diam-diam |
| **v2.14** | 🔄 Sinkron otomatis antar HP via akun (menu/pesanan/omzet langsung masuk di HP lain, dua arah, anti tabrakan) · 💳 Laporan Pembayaran di Pengaturan (per metode bayar) · 📅 navigasi kalender kaya laporan menu |
| **v2.13** | 📝 Catatan per menu (ikut ke nota dapur) · 🔤 2 bahasa ID/EN + bahasa baku · 🍊 tema Royal Orange dibenerin + Pink & Putih · 🖨️ tombol cetak dapur & kasir di layar sukses · nota gak kapital semua |
| **v2.12** | 🔒 Reset data wajib konfirmasi + tombol terkunci 5 detik (anti ke pencet) · README GitHub baru |
| **v2.11** | ✂️ Fix tulisan paling bawah kepotong di semua layar (akar bugnya: tinggi layar nembus batas app) |
| **v2.10** | 📷 Scan barcode & QR massal · 📊 Laporan Menu bertanggal · 📱 QRIS · 🔖 Cetak tambahan · 🚫 fitur notifikasi dicabut |

---

<div align="center">

**Dibuat dengan ☕ + 🔥 buat para penjual.**

Semoga lancar jualannya! 💪

</div>
