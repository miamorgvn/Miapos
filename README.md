<div align="center">

# 🍜 Miapos — Kasir & Manajemen Restoran

**Aplikasi kasir (POS) yang berjalan 100% offline di HP.**
Cocok untuk warung, kafe, kedai, hingga restoran — kasir, dapur, stok, laporan, semuanya tersedia. 🚀

![versi](https://img.shields.io/badge/versi-2.26-10b981?style=flat-square&labelColor=0f172a)
![PWA](https://img.shields.io/badge/PWA-offline%20ready-5A0FC8?style=flat-square&labelColor=0f172a)
![teknologi](https://img.shields.io/badge/React%20%2B%20Tailwind-single%20file%20HTML-orange?style=flat-square&labelColor=0f172a)
![mesin](https://img.shields.io/badge/Python%20%2B%20C%2B%2B-engine-blue?style=flat-square&labelColor=0f172a)

</div>

---

## 🤔 Tentang Aplikasi Ini

Miapos adalah aplikasi kasir bergaya **Progressive Web App (PWA)** — dibuka lewat browser HP,
ditambahkan ke home screen, lalu tampil seperti aplikasi pada umumnya. ⚡

Beberapa hal yang membedakannya:

- 📴 **100% offline** — internet mati pun transaksi tetap berjalan. Seluruh data tersimpan di HP sendiri.
- 📄 **Satu file saja** — inti aplikasinya hanya `index.html`. Mudah disalin, dibackup, maupun dipindah ke HP lain.
- 🏪 **Lengkap** — kasir, dapur, stok bahan, laporan, multi-cabang, printer, QRIS. Tidak perlu langganan bulanan. 💸

---

## ✨ Fitur

### 👤 Akun & Sinkron Antar HP (sejak v2.14, disempurnakan di v2.15)
- **Satu akun untuk semua HP** — cukup mendaftar satu kali (nama, nomor HP, usaha, alamat, kata sandi); data usaha tersimpan per akun
- 🔄 **Sinkronisasi otomatis** — HP lain yang login ke akun yang sama langsung menerima menu, pesanan, omzet, stok, dan laporan. Tidak perlu input ulang, tidak perlu scan QR di setiap HP 🎉
- 🔑 **Sejak v2.15: cukup kata sandi akun** — tidak perlu lagi menyetel password Backup Cloud untuk sinkronisasi.
  Server menerima kata sandi akun yang diketik saat login (jalur password backup lama tetap didukung).
- ⚡ **Real-time dua arah** — HP A menambah menu → HP B otomatis ter-update (polling tiap ±45 detik saat online; saat offline tetap berjalan, begitu kembali online datanya terkirim sendiri)
- 🛡️ **Anti bentrok data** — penghapusan juga ikut tersinkron (tombstone), penyuntingan bersamaan tetap aman
- 🩺 **Status sinkron yang jujur (v2.15)** — kartu akun menampilkan penyebab sinkronisasi tidak berjalan (belum login, server belum ada, password salah) + tombol **Sinkron sekarang** yang selalu bisa dicoba
- 📷 **QR Akun** tetap tersedia untuk kondisi offline — pindai → konfirmasi → data termuat utuh tanpa internet
- Tersedia **Ubah Akun** (ganti nama/nomor/kata sandi) & **Keluar** (log out — data akun tetap aman dan bisa dimuat kembali)
- Memerlukan deployment Vercel/Termux (server Python `main.py` / API `api/sync.js`) — GitHub Pages tidak mendukung sinkronisasi otomatis

### 🧾 Kasir & Pembayaran
- Pembuatan pesanan cepat, keranjang, promo & diskon
- Metode pembayaran **Tunai / QRIS / Transfer** — gambar QRIS restoran bisa diunggah sendiri 📱
- 📝 **Catatan per menu** — di bawah setiap menu pada keranjang tersedia kolom catatan sendiri
  (contoh: "pedas, tanpa es" khusus untuk Mie Ayam tersebut) — meskipun pesanannya sudah masuk
- Nota otomatis: cetak struk kasir, nota dapur, dan nota **tambahan** (item yang ditambahkan belakangan)
- Nama menu pada nota dicetak dengan huruf normal (bukan kapital semua) — lebih hemat kertas 👍
- ✂️ **Garis `====` cukup satu (baru di v2.16!)** — sebelumnya nota kasir & nota dapur masing-masing memakai 2 garis `====`, kini cukup 1 garis di bawah header — kertas lebih hemat dan tidak tampak dobel
- 💰 **Biaya Tambahan (v2.19)** — pada detail pesanan tersedia tombol **Tambah Biaya Tambahan**: isi Nama Biaya + Jumlah Biaya → Simpan. Biaya di luar menu (ongkos kirim, packing, dll.) ikut ke total tagihan, tercetak di struk kasir, dan bisa dihapus kembali sebelum pembayaran
- 🧾 **Biaya Tambahan menjadi item lengkap (baru di v2.24!)** — setiap biaya tambahan kini tampil seperti menu: ada qty (+/−), kolom catatan, dan tombol hapus. "Jumlah Biaya" menjadi harga satuan (contoh: Packing Rp2.800 × 3 = Rp8.400); struk kasir mencetak "Biaya: 3x Packing" beserta catatannya. Biaya lama tanpa qty tetap dihitung sebagai qty 1
- 🚫 **Pesanan yang sudah dibayar dapat dibatalkan (baru di v2.24!)** — tombol **Batalkan Pesanan** pada detail pesanan, lengkap dengan konfirmasi. Berguna saat pelanggan konfirmasi QRIS tetapi transaksi gagal dan ingin beralih ke tunai: batalkan pesanan QRIS, lalu buat pesanan baru dengan pembayaran tunai. Pesanan batal diberi badge **"Dibatalkan"**, tidak dihitung dalam omzet & seluruh laporan, bahan baku otomatis dikembalikan ke stok (tercatat "Pembatalan Pesanan" di Riwayat Pergerakan Stok), dan meja langsung dilepas
- ✏️ **Pesanan batal bisa dibuka lagi (baru di v2.25!)** — tombol **Ubah Pesanan** pada detail pesanan yang dibatalkan: seluruh isinya dimuat kembali ke keranjang — menu beserta qty-nya, biaya tambahan lengkap dengan qty & catatannya, nama pelanggan, tempat/meja, catatan dapur, sampai diskon. Kasir cukup mengubah bagian yang perlu (misalnya mengganti QRIS menjadi tunai) lalu menerima pembayaran seperti biasa — **tidak perlu memasukkan ulang pesanan dari awal**. Catatan pesanan batal tetap tersimpan sebagai "Dibatalkan" (tidak dihitung dalam omzet & laporan); pesanan yang dibayar ulang menjadi pesanan baru dengan nomornya sendiri
- 🛠️ **Ubah metode pembayaran pesanan lunas (baru di v2.26!)** — pada detail pesanan yang sudah dibayar kini ada tombol **Ubah** dengan panah ke atas (polanya sama seperti menu Cetak Dapur, agar detail pesanan tidak sesak tombol). Pilih **Ubah Metode Pembayaran** → Tunai/QRIS/Transfer → Simpan: cocok saat pelanggan sempat tercatat QRIS lalu ternyata membayar tunai. Pesanan tetap "Sudah Bayar", omzet tidak berubah, dan struk yang dicetak berikutnya memakai metode yang baru. Menu ini juga tersedia pada Riwayat/Laporan
- ✏️ **Ubah pesanan lunas + perbaikan status (baru di v2.26!)** — pilihan **Ubah Pesanan** pada pesanan yang sudah dibayar memuat seluruh detailnya kembali ke keranjang; pesanan aslinya **otomatis dibatalkan** agar omzet tidak terhitung ganda, lalu kasir mengubah dan menerima pembayaran seperti biasa. Pesanan yang belum dibayar tidak mendapat menu ini, dan tombol **Batalkan Pesanan** tetap tersedia untuk semua pesanan. Sekaligus perbaikan: pesanan batal tidak lagi dihitung pada filter & jumlah "Belum Bayar" di halaman Pesanan — kini hanya tampil di Semua Status dengan badge Dibatalkan
- 🧹 **Tombol "+ Tambah Menu" di keranjang dihapus (baru di v2.22!)** — sebelumnya (v2.21) tombol tersebut berada persis di bawah pilihan Dine In / Bawa Pulang sehingga terkesan sesak. Kini di bagian itu hanya ada tombol **Tambah Biaya Tambahan** (full-width, lebih rapi). Menambah menu tetap mudah: tutup keranjang → ketuk menunya pada layar Tambah Pesanan → qty otomatis bergabung ke keranjang
- 📝 **Catatan Nota di detail pesanan (baru di v2.21!)** — tombol di bawah daftar item: tulis "Bungkus" / "Bawa Pulang" → masuk ke **header nota dapur** saat dicetak
- 🏷️ **Menu yang sama ditambah lagi = digabung + diberi tanda (baru di v2.21!)** — qty tetap digabung, dan kini ada badge **"Tambahan +N"** pada baris tersebut; tombol + di detail pesanan juga dihitung sebagai tambahan; **Cetak Tambahan** hanya mencetak porsi yang ditambahkan (porsi yang sudah pernah tercetak tidak diulang); kartu pesanan menampilkan "Ada Tambahan"
- 🎨 **Tombol biaya mengikuti tema (baru di v2.20!)** — sebelumnya selalu merah, kini warnanya mengikuti tema yang dipilih (Emerald/Royal/Pink/Charcoal) — konsisten dengan tombol lainnya
- 🖨️ **Pratinjau Nota kini 3 tab (baru di v2.19!)** — Nota Kasir, Nota Dapur, dan **Nota Dapur-Tambahan** — bentuk nota tambahan bisa dilihat lebih dulu di Pengaturan
- 📏 **Judul DAPUR sebesar No. Antrian (baru di v2.17!)** — tulisan DAPUR di kepala nota dapur dicetak setinggi dua kali (lonjong), sama persis dengan No. Antrian di bawahnya — headernya mudah terlihat dari jauh 🍳
- 🖨️ **Popup hasil cetak (baru di v2.16!)** — setelah mencetak, popup langsung menampilkan **berhasil dikirim ke printer apa** atau **gagal beserta alasannya** (plus tombol salin teks nota untuk cetak manual) — tidak perlu bolak-balik memeriksa printer
- Setelah pembayaran langsung muncul 2 tombol: **Cetak Dapur** (dapur langsung memasak) & **Struk Kasir** 🖨️
- Label "Tambahan" hanya tampil di aplikasi — nota cetakan tetap bersih ✨

### 📷 Scan Barcode & QR untuk Input Menu
- Scan barcode/QR memakai kamera → menu langsung masuk, tanpa mengetik satu per satu
- **QR Massal**: 1 QR bisa berisi *banyak menu sekaligus* (ratusan menu pun bisa) —
  scan sekali, semua menu langsung terbagi ke kategori masing-masing 🤯
- Scan dari galeri didukung, tersedia cadangan ketik manual, dan pembaca harganya mengenali
  `27.000`, `Rp27.500`, `25rb`, `27k` — format Indonesia semuanya
- Anti duplikat: menu yang sama tidak akan terinput dua kali

### 📊 Laporan & Laporan Menu
- Omzet hari ini, jumlah transaksi, tren, metode pembayaran
- **Laporan Menu**: daftar yang terjual beserta qty-nya, diurutkan dari yang paling laris 🏆 (+ medali 3 besar)
- 💳 **Laporan Pembayaran (baru di v2.14!)** — ada di **Pengaturan → Laporan Pembayaran**:
  melihat pembayaran hari ini memakai metode apa saja (Tunai/QRIS/Transfer), per metode & per transaksi
- 📅 Bisa melihat **hari-hari sebelumnya** — cukup ketuk tanggal di atas (kalender),
  sama seperti laporan menu: panah mundur/maju + tombol cepat Hari Ini / Kemarin
- Tanggal kemarin bisa diintip, mundur sampai berapa pun — pesanan lama yang terarsip tetap terhitung
- 📐 **Angka otomatis menyesuaikan lebar kartu (baru di v2.16!)** — omzet sepanjang apa pun tampil utuh, tidak ada lagi "Rp4.081.00…" yang terpotong di kartu laporan menu & laporan pembayaran

### 📦 Stok & Bahan Baku
- Kelola bahan baku, stok masuk/keluar, peringatan stok menipis
- Fitur Modal & HPP (harga pokok penjualan) untuk perhitungan laba & margin 💰

### 🏪 Multi Cabang & Multi Kasir
- Beberapa cabang/outlet dalam satu aplikasi, datanya terpisah per outlet
- Kasir bertugas dengan PIN masing-masing, ganti sesi cukup sekali ketuk

### 🖨️ Nota & Printer
- Header nota bisa diganti sendiri (nama resto, alamat, ucapan)
- Printer kasir & printer dapur tersambung terpisah
- Tombol cetak dapur memiliki pilihan **Cetak Dapur / Cetak Tambahan** 🔖

### 🌤️ Dashboard yang Tidak Membosankan
- Kartu cuaca hari ini (data Open-Meteo) + **jam live** pada kartu
- Salam sapa otomatis mengikuti pagi/siang/sore/malam + kalimat ringan acak agar suasana lebih hidup 😄

### ☁️ Backup Cloud & Update Otomatis
- ☁️ **Backup TANPA PASSWORD (baru di v2.23!)** — cukup login akun: backup otomatis (maksimal 1x per 2 jam bila data berubah), tombol **Backup Sekarang** & **Pulihkan** semuanya berjalan TANPA mengisi password. Password backup (BACKUP_KEY) menjadi opsional — hanya untuk yang belum login / ingin memakai kunci sendiri
- Backup otomatis ke GitHub (memakai token sendiri) — data tetap aman walau HP hilang
- Update aplikasi? Timpa file ke repo → semua HP otomatis ter-refresh **tanpa logout** — akun & data tetap ada (asalkan URL/domain sama) 🔄
- Pesanan kemarin "hilang"? Tidak — **auto-arsip**: buka Laporan → tab **Riwayat Pesanan** → pilih tanggalnya 📅
- Reset data dikunci konfirmasi **5 detik** — agar tidak tertekan tanpa sengaja

### 🌏 2 Bahasa — Indonesia / English
- Pengaturan → **Bahasa** → pilih Indonesia atau English — tersimpan otomatis 💬
- ✍️ **Bahasa makin baku (v2.16)** — seluruh teks aplikasi dirapikan menjadi bahasa Indonesia baku (sapaan dashboard, tips, pesan error, semuanya) — tidak ada lagi kata gaul

### 🎨 Puluhan Sentuhan Kecil
- **4 tema warna**: Emerald & Slate · Royal & Orange (benar-benar oranye! 🍊) ·
  Pink & Putih 🌸 · Charcoal Dark — ganti tema, seluruh aplikasi ikut berubah seketika
- Mode layar penuh (judul tidak tertutup lensa kamera),
  scan QRIS dari galeri, kategori menu bebas dibuat/dihapus, dan lain-lain

---

## 🚀 Cara Pakai

### 1️⃣ Pasang sebagai aplikasi di HP (paling mudah)
1. Buka alamat aplikasinya di Chrome Android / Safari iPhone
2. Menu browser → **"Tambahkan ke layar utama"** (Add to Home Screen)
3. Selesai — ikonnya muncul seperti aplikasi biasa, terbuka langsung full screen 📲

### 2️⃣ Upload ke hosting
Bebas: GitHub Pages, Netlify, Vercel, atau hosting sendiri.
Cukup unggah isi folder ini (termasuk folder `lib/`) — pastikan semua filenya ikut terunggah.

### 3️⃣ Jalankan lokal (Termux / laptop)
```bash
# dari folder ini, tinggal:
python3 -m http.server 8080
# buka http://localhost:8080
```

---

## 🔄 Update Versi Baru

Aplikasi ini memakai **Service Worker** dengan pola *network-first*:

1. Timpa file lama dengan file baru di repo
2. Pengguna membuka aplikasi (saat online) → otomatis mengambil versi terbaru
3. Cache lama terhapus sendiri — nama cache di `sw.js` diganti setiap rilis
   (mis. `miapos-v2.26-r1`), jadi jangan lupa menggantinya bila ikut merilis 🔁

> 💡 Aturan project ini: **setiap update, versi selalu naik** (2.19 → 2.20 → 2.21 → 2.22 → 2.23 → 2.24 → 2.25 → 2.26 → ...).

---

## 🗂️ Struktur File

| File | Fungsi |
| --- | --- |
| `index.html` | 🌟 **Seluruh aplikasi** — React + Tailwind dalam satu file |
| `sw.js` | Service worker: auto-update + cache offline |
| `manifest.json` | Identitas PWA (nama, ikon, warna) |
| `lib/` | Bundel library (React, Babel, Tailwind, Lucide) — offline semuanya |
| `engine/` | Native engine C++ (opsional, dipanggil server Python) |
| `api/` | Serverless functions untuk backup cloud & sinkronisasi akun (Vercel) |
| `main.py` | Server Python lokal/Termux — backup cloud + API sinkronisasi akun |
| `sync/` | Data sinkronisasi per akun (`acc-<noHP>.json`) |
| `.well-known/assetlinks.json` | Untuk build Android (TWA / Play Store) |
| `PANDUAN-*.txt` | 📚 Panduan lengkap tiap fitur (ditulis dengan bahasa santai) |

---

## 🛠️ Teknologi

- ⚛️ **React + Tailwind CSS** — bagian UI-nya, dibundel lokal sehingga tetap berjalan offline
- 📷 **BarcodeDetector API** — scan barcode/QR native Chrome, tanpa library kamera eksternal
- ⚙️ **Service Worker** — auto-update, background sync, periodic sync
- 🐍 **Python + C++ Engine** — server bridge & mesin lokal opsional untuk backup/pengolahan data
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
| `PANDUAN-PLAYSTORE.txt` | Menjadikan aplikasi Android sungguhan |
| `PANDUAN-TERMUX.txt` | Menjalankan di HP memakai Termux |
| `PANDUAN-BACKUP-CLOUD.txt` | Backup otomatis ke GitHub |

---

## 🧾 Riwayat Versi (ringkas)

| Versi | Yang baru |
| --- | --- |
| **v2.26** | 🛠️ **pesanan lunas bisa diubah**: tombol **Ubah** dengan panah ke atas pada detail pesanan yang sudah dibayar (pola sama seperti menu Cetak Dapur) berisi **Ubah Metode Pembayaran** — ganti Tunai/QRIS/Transfer tanpa membatalkan pesanan (status tetap Sudah Bayar, struk berikutnya ikut metode baru, tersedia juga di Riwayat/Laporan) — dan **Ubah Pesanan** — seluruh detail dimuat kembali ke keranjang, pesanan lunas aslinya otomatis dibatalkan agar omzet tidak terhitung ganda, lalu dibayar lagi · pesanan yang belum dibayar tidak mendapat menu ini dan tombol **Batalkan Pesanan** tetap tersedia · 🧹 perbaikan: pesanan batal tidak lagi dihitung pada filter & jumlah "Belum Bayar" di halaman Pesanan — hanya tampil di Semua Status (badge Dibatalkan) |
| **v2.25** | ✏️ **pesanan batal bisa dibuka lagi**: tombol **Ubah Pesanan** pada detail pesanan yang dibatalkan — seluruh detail (menu & qty, biaya tambahan beserta qty & catatannya, nama pelanggan, tempat/meja, catatan dapur, diskon) dimuat kembali ke keranjang; kasir cukup mengubah bagian yang perlu (mis. ganti QRIS ke tunai) lalu menerima pembayaran lagi, tanpa mengetik ulang dari awal · catatan pesanan batal tetap tercatat "Dibatalkan" (tidak dihitung omzet/laporan) · konfirmasi pembatalan kini menyebutkan bahwa pesanan masih bisa dibuka lagi |
| **v2.24** | 🧾 **Biaya Tambahan menjadi item lengkap**: qty (+/−), catatan, dan tombol hapus pada setiap biaya — harga satuan × qty, struk kasir mencetak "Biaya: 3x Packing" + catatan · 🚫 **pesanan done (sudah bayar) dapat dibatalkan**: tombol **Batalkan Pesanan** + konfirmasi; badge "Dibatalkan", tidak dihitung dalam omzet & seluruh laporan, bahan baku kembali ke stok, meja dilepas |
| **v2.23** | ☁️ **Backup Cloud TANPA PASSWORD** — cukup login akun: backup otomatis, **Backup Sekarang** & **Pulihkan** berjalan tanpa mengisi password (autentikasi akun di api/backup.js, selaras dengan sinkronisasi v2.15; BACKUP_KEY menjadi opsional) · 🧠 kartu Pengaturan backup diperbarui: badge **CLOUD AKTIF** tanpa password / **BELUM LOGIN / ISI PASSWORD** |
| **v2.22** | 🧹 **keranjang dirapikan**: tombol **"+ Tambah Menu"** yang berada di bawah pilihan Dine In / Bawa Pulang **dihapus sepenuhnya** (mobile & desktop) — di bagian itu sekarang hanya ada **Tambah Biaya Tambahan** (full-width). Menambah menu cukup lewat daftar menu pada layar Tambah Pesanan — qty otomatis bergabung ke keranjang |
| **v2.21** | 🛒 **keranjang**: tombol **+ Tambah Menu** (di tengah) & **Tambah Biaya Tambahan** ditempatkan persis di bawah pilihan Dine In / Bawa Pulang — menambah menu/biaya tanpa menutup keranjang · 📝 **Catatan Nota** di detail pesanan (tulis "Bungkus"/"Bawa Pulang" → masuk ke header nota dapur) · 🏷️ menu yang sama ditambah lagi: qty **tetap digabung** tetapi kini ada badge **"Tambahan +N"** — tombol + di detail juga dihitung sebagai tambahan, **Cetak Tambahan** hanya mencetak porsi yang ditambahkan (yang sudah tercetak tidak diulang), kartu pesanan menampilkan "Ada Tambahan" |
| **v2.20** | 🎨 tombol **Tambah Biaya Tambahan** mengikuti warna tema (bukan merah tetap) · 💬 teks acak kartu cuaca **ditulis ulang** — seperti teman yang berbincang santai, tidak kaku · ⏱️ teksnya **dikunci 5 menit** — tidak berganti setiap pindah layar, berganti sendiri tiap 5 menit · 🔢 **Laporan Pembayaran diurutkan No. Antrian** kecil → besar · 🌙 **No. Antrian reset otomatis saat ganti hari** (pukul 12 malam waktu HP → esok mulai dari 1 lagi) · 🧹 file notif tersisa (PANDUAN-NOTIF.txt, api/push-*) **dihapus permanen** dari repo |
| **v2.19** | 💰 **Biaya Tambahan** di detail pesanan (nama + jumlah, ikut total & struk kasir) · 🔁 menu yang sama pada sheet tambah item **digabung** (qty bertambah, tidak membuat baris baru) · ✏️ tombol & sheet "Tambah Menu" di detail pesanan menjadi **"Tambah Pesanan"** + menampilkan jumlah item di bawah tombol + · 🖨️ pratinjau nota kini memiliki tab **Nota Dapur-Tambahan** · 📱 **tombol back navigasi HP berfungsi di dalam aplikasi**: detail pesanan → daftar pesanan → Dashboard (back kedua di Dashboard keluar dari aplikasi, ada pengingat lebih dulu) |
| **v2.18** | 🚀 No. Antrian pada nota dapur diberi **jeda satu baris** dari daftar menu — tidak menempel lagi, lebih nyaman dibaca |
| **v2.17** | 📏 judul **DAPUR** pada nota dapur dicetak setinggi dua kali (lonjong) — sama besar dengan No. Antrian, headernya mudah dicari di tumpukan nota |
| **v2.16** | ✂️ garis `====` pada nota cukup satu (kasir & dapur, hemat kertas) · 🖨️ popup hasil cetak: berhasil/gagal selalu tertera, tidak perlu memeriksa printer bolak-balik · 📐 angka laporan otomatis menyesuaikan lebar kartu (perbaikan "Rp4.081.00…" terpotong) · ✍️ seluruh teks aplikasi diubah menjadi bahasa baku |
| **v2.15** | 🔑 Sinkronisasi cukup memakai kata sandi akun (tanpa menyetel password backup) · 🩺 status sinkronisasi yang jujur + tombol sync yang tidak gagal diam-diam · 🛠️ perbaikan: menu tidak ikut ke HP lain karena kegagalan autentikasi yang senyap |
| **v2.14** | 🔄 Sinkronisasi otomatis antar HP via akun (menu/pesanan/omzet langsung masuk di HP lain, dua arah, anti bentrok) · 💳 Laporan Pembayaran di Pengaturan (per metode bayar) · 📅 navigasi kalender seperti laporan menu |
| **v2.13** | 📝 Catatan per menu (ikut ke nota dapur) · 🔤 2 bahasa ID/EN + bahasa baku · 🍊 tema Royal Orange diperbaiki + Pink & Putih · 🖨️ tombol cetak dapur & kasir di layar sukses · nota tidak lagi kapital semua |
| **v2.12** | 🔒 Reset data wajib konfirmasi + tombol terkunci 5 detik (anti tertekan tanpa sengaja) · README GitHub baru |
| **v2.11** | ✂️ Perbaikan tulisan paling bawah terpotong di semua layar (akar bugnya: tinggi layar melewati batas aplikasi) |
| **v2.10** | 📷 Scan barcode & QR massal · 📊 Laporan Menu bertanggal · 📱 QRIS · 🔖 Cetak tambahan · 🚫 fitur notifikasi dicabut |

---

<div align="center">

**Dibuat dengan ☕ + 🔥 untuk para penjual.**

Semoga lancar jualannya! 💪

</div>
