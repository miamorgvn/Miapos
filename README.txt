================================================
  MIAPOS v2.4 — NOTA DIPISAH + PREVIEW BISA DIEDIT
================================================

APA YANG BARU DI v2.4
---------------------
1. NOTA KASIR vs NOTA DAPUR BENER-BENER DIPISAH:
   • NOTA KASIR (buat customer): header resto (nama,
     alamat, telepon) + rincian bayar + ucapan terima
     kasih + promosi. TANPA no. antrian.
   • NOTA DAPUR (buat dapur): bersih — cuma judul "DAPUR"
     + detail pesanan + item + No. Antrian. TANPA nama/
     alamat resto.
   • No. Antrian tetap cetak DOUBLE-HEIGHT (ESC ! 0x10):
     font lonjong ke bawah, beda dari font menu, lalu
     reset normal (ESC ! 0x00).
2. PRATINJAU NOTA SEKARANG BISA DIEDIT:
   • Klik "Edit Contoh" di Pratinjau Nota → ubah nama
     pelanggan, meja, kasir, item (nama/qty/harga/catatan)
     → pratinjau langsung ikut berubah live.
   • Enak buat cek tata letak nota sebelum beneran cetak.
3. WARNA BALIK KE HIJAU EMERALD:
   • Tema utama emerald yang adem di mata (ganti biru).
   • Tombol hapus/batal/error tetap MERAH.
4. SAKLAR "FITUR MODAL & HPP" (baru!):
   • Di Pengaturan ada saklar ON/OFF "Fitur Modal & HPP".
   • Default MATI: laba, margin, modal & HPP (COGS)
     disembunyikan dari Kelola Menu, dialog menu & Laporan.
   • Butuh hitung untung? Tinggal nyalakan saklarnya.

============================== RIWAYAT ==============================

v2.3 — TEMA BIRU + PRATINJAU NOTA + PROMOSI:
- Tema biru natural (dari merah maroon), tren naik/turun
  dibenerin (hijau/merah), bar stok aman hijau.
- Nota kasir: baris promosi "Made by Miapos" di bawah
  ucapan terima kasih (teks bisa diganti).
- Nota dapur: No. Antrian double-height ESC ! 0x10.
- Pratinjau Nota di Nota & Printer (tab kasir & dapur).

v2.2 — UI ROMBAK ALA APLIKASI KASIR:
- Nav bawah 5 slot + FAB tengah buka "Tambah Pesanan"
  (cari menu, chip kategori, list +/-, Subtotal + Lanjut).
- Pengaturan jadi HUB per fitur (Kelola Menu, Stok & Bahan,
  Dapur KDS, Kasir & Karyawan, Cabang, Nota & Printer, Mesin).
- Nota & Printer satu layar: header nota + printer kasir &
  dapur (bluetooth + test print).
- Laporan geser tanggal + daftar per pesanan (arsip ikut).
- Hapus menu (ikon tong sampah + konfirmasi), Layar Penuh
  Sempurna, popup z-index fix, rollover 24 jam.

v2.1 — DATA BERSIH + MESIN LOKAL:
- Semua angka demo dikosongkan; menu bisa tambah/edit/hapus.
- main.py server + API + auto-backup; engine C++ prediksi
  omzet; splash screen animasi; 100% offline (lib/ lokal).

=====================================================================

ISI FOLDER
----------
   index.html            aplikasi utama (buat Vercel/GitHub Pages)
   miapos.html           redirect otomatis ke index.html (link lama aman)
   lib/                  library offline (WAJIB ADA)
   main.py               server Python + API + auto-backup
   engine/               C++ native analytics engine (source)
   install.sh            installer Termux
   start.sh              launcher 1-klik (Termux:Widget)
   manifest.json         data PWA
   icon-192/512.png      ikon aplikasi
   PANDUAN-TERMUX.txt    panduan lengkap Termux
   PANDUAN-GITHUB.txt    cara push ke GitHub + fix merge conflict

CARA PAKAI DI TERMUX
--------------------
   bash install.sh     (sekali saja, butuh internet)
   python main.py      (jalanin app — TANPA internet)

Lalu buka http://localhost:8080/miapos.html — atau lebih
enak: "Tambahkan ke layar utama" di Chrome → app fullscreen
dengan ikon sendiri, persis aplikasi beneran.

SELAMAT PAKAI! — Miapos v2.4
