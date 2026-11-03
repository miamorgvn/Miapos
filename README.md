<div align="center">

# 🍜 Miapos — Kasir & Manajemen Restoran

**Aplikasi kasir (POS) yang jalan 100% offline di HP.**
Buat warung, kafe, kedai, sampai resto — kasir, dapur, stok, laporan, semua ada. 🚀

![versi](https://img.shields.io/badge/versi-2.13-10b981?style=flat-square&labelColor=0f172a)
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

### 👤 Akun & Sinkron Antar HP (baru di v2.13!)
- **Satu akun untuk semua HP** — daftar sekali (nama, no. HP, usaha, alamat, kata sandi), data usaha tersimpan per akun
- 📷 **QR Akun** — HP lain tinggal **Pindai QR Akun** → muncul popup info akun (nama, usaha, alamat lengkap) → konfirmasi → semua data (menu, pesanan, omzet, stok, laporan) langsung ke-load
- Kalau data sudah kebesaran buat QR, otomatis ada **Kode Data Lengkap** — salin → kirim lewat WhatsApp ke HP lain → tempel → beres
- Ada **Ubah Akun** (ganti nama/nomor/kata sandi) & **Keluar** (log out — data akun tetap aman & bisa dimuat lagi)
- 100% offline, tanpa server — sinkron lewat QR/kode, sekali pindah datanya utuh semua

### 🧾 Kasir & Pembayaran
- Buat pesanan cepat, keranjang, promo & diskon
- Metode bayar **Tunai / QRIS / Transfer** — QRIS resto bisa upload gambar sendiri 📱
- 📝 **Catatan per menu** — di bawah tiap menu di keranjang ada kolom catatan sendiri
  (contoh: "pedas, tanpa es" buat Mie Ayam-nya aja) — walau pesanannya udah masuk
- Nota otomatis: cetak struk kasir, nota dapur, dan nota **tambahan** (item yang ditambah belakangan)
- Nama menu di nota dicetak **huruf normal** (bukan KAPITAL semua) — hemat kertas 👍
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
- Bisa intip tanggal kemarin, mundur sampai belakang — pesanan lama yang terarsip tetap kehitung

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
   (mis. `miapos-v2.13-r1`), jadi jangan lupa ganti kalau ikut ngerilis 🔁

> 💡 Aturan project ini: **setiap update, versi selalu naik** (2.11 → 2.12 → 2.13 → ...).

---

## 🗂️ Struktur File

| File | Fungsi |
| --- | --- |
| `index.html` | 🌟 **Seluruh aplikasi** — React + Tailwind, satu file |
| `sw.js` | Service worker: auto-update + cache offline |
| `manifest.json` | Identitas PWA (nama, ikon, warna) |
| `lib/` | Library bundel (React, Babel, Tailwind, Lucide) — offline semua |
| `engine/` | Native engine C++ (opsional, dipanggil server Python) |
| `api/` | Serverless functions buat backup cloud (Vercel) |
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
| **v2.13** | 📝 Catatan per menu (ikut ke nota dapur) · 🔤 2 bahasa ID/EN + bahasa baku · 🍊 tema Royal Orange dibenerin + Pink & Putih · 🖨️ tombol cetak dapur & kasir di layar sukses · nota gak kapital semua |
| **v2.12** | 🔒 Reset data wajib konfirmasi + tombol terkunci 5 detik (anti ke pencet) · README GitHub baru |
| **v2.11** | ✂️ Fix tulisan paling bawah kepotong di semua layar (akar bugnya: tinggi layar nembus batas app) |
| **v2.10** | 📷 Scan barcode & QR massal · 📊 Laporan Menu bertanggal · 📱 QRIS · 🔖 Cetak tambahan · 🚫 fitur notifikasi dicabut |

---

<div align="center">

**Dibuat dengan ☕ + 🔥 buat para penjual.**

Semoga lancar jualannya! 💪

</div>
