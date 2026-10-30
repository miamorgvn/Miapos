================================================
  MIAPOS v2.6 — 3 TEMA WARNA + CHIP KASIR/CABANG
        + AUTO-UPDATE + SIAP PLAY STORE
================================================

APA YANG BARU DI v2.6 (tema warna + perapihan header)
-----------------------------------------------------
1. 3 TEMA WARNA — GANTI GANTI SESUKA HATI:
   • EMERALD & SLATE (default): hijau emerald #10B981
     ala dashboard favorit — fokus & kesuksesan transaksi.
   • ROYAL & ORANGE: biru royal #2563EB + tombol bayar
     oranye #F97316 — kepercayaan & fokus pengguna.
   • CHARCOAL DARK: gelap #121212 + aksen neon #D1FF1A —
     minimalis & ideal, mata nggak silau malam hari.
   • Cara ganti: Pengaturan → "Tema Warna" → muncul
     pop up berisi 3 KARTU PREVIEW (kayak setelan dark
     mode di HP) → ketuk salah satu → SELURUH app
     langsung berubah: header, tombol, FAB, grafik,
     laporan, toggle — dan PILIHAN TERSIMPAN OTOMATIS
     (buka ulang tetap ingat).
2. CHIP "GANTI KASIR" BALIK & LEBIH GAMPANG:
   • Fitur cepat ganti kasir TIDAK dihapus — sekarang
     malah selalu keliatan di HP: jadi chip HITAM
     (avatar + nama kasir) di baris kedua header.
     Ketuk → langsung pilih kasir aktif.
   • Chip CABANG/OUTLET dibikin PUTIH garis HITAM,
     kontras jelas di sampingnya. Dua-duanya hitam
     putih biar beda dari tombol warna tema.
   • Chip-kip ini punya BARIS SENDIRI di bawah judul →
     judul, chip kasir & logo cabang NGGAK PERNAH
     sempit-sempitan/nabrak lagi.
3. HEADER PUTIH BERSIH — HABIS "BLEND" IJO-IJO:
   • Header sekarang putih (mengikuti tema terang),
     warna bilah status Android ikut putih tulang —
     rapi kayak aplikasi beneran. Warna tema tetap
     nempel di tombol, FAB, tab & grafik.
   • Charcoal Dark = gelap total, bilah status ikut
     #121212. Splash screen tetap keren gelap.
4. TOMBOL BAYAR IKUT WARNA AKSEN TEMA:
   • Royal & Orange → tombol Bayar/Konfirmasi oranye.
   • Charcoal Dark → tombol Bayar neon green.
   • Emerald & Slate → tetap hijau emerald.
5. LABEL VERSI: "Miapos F&B Suite v2.6".

APA YANG BARU DI v2.5.1 (perbaikan tampilan)
--------------------------------------------
1. TEKS HEADER NGGAK NABRAK LAGI:
   • Subjudul header panjang (statistik layar Pesanan)
     sekarang OTOMATIS DIPOTONG (...) sebelum menyentuh
     tombol kanan/kiri. Nggak ada lagi teks nimpa tombol
     swapper kasir / logo cabang.
   • Chip "Ganti Kasir" (huruf C) hanya tampil di layar
     lebar (tablet/desktop) — di HP header jadi lega.
     Ganti kasir tetap bisa dari layar Kasir & Pengaturan.
   • Subjudul Pesanan diringkas: "Hari ini · 3 pesanan"
     (+ " · 1 belum bayar" hanya kalau ada).
2. HEADER SOLID, NGGAK "BLEND" JELEK LAGI:
   • Header hijau sekarang SOLID (bukan gradasi) dan
     warnanya PERSIS sama dengan warna bilah status
     Android (theme-color #10b981) → nyatu mulus ala APK
     asli: di web, PWA, maupun Layar Penuh Sempurna.
3. WARNA LEBIH "EMERALD" BENERAN:
   • Skala hijau naik satu tingkat ke emerald-500
     (#10b981): header, tombol, FAB, toggle — semuanya
     lebih terang & fresh, nggak gelap muram lagi.
4. LABEL VERSI: "Miapos F&B Suite v2.5.1".

APA YANG BARU DI v2.5
---------------------
1. JUDUL TIAP LAYAR DI TENGAH:
   • Header semua halaman (Dashboard, Pesanan, Kasir,
     Laporan, Pengaturan, dst) judulnya sekarang PERSIS
     di tengah, ala titlebar aplikasi asli.
   • Tombol kembali & tombol aksi di kiri/kanan tidak
     menggeser posisi judul.
2. BILAH NOTIFIKASI TETEP KELIATAN, WARNA NGIKUT:
   • Mode PWA diganti dari "fullscreen" ke "standalone" →
     jam, sinyal & baterai di bilah atas tetap terlihat,
     warnanya mengikuti tema emerald app.
   • Aman dari lensa kamera! HP dengan punch-hole (mis.
     Oppo A54) atau Dynamic Island (iPhone) tidak lagi
     nutup judul.
   • Saklar "Layar Penuh Sempurna" tetap ada (opsional).
     Kalau dinyalakan, judul otomatis turun 30px biar
     tidak ketutup lensa kamera.
3. AUTO-UPDATE (SERVICE WORKER — baru!):
   • Aplikasi cek versi terbaru tiap dibuka saat online.
     Ada versi baru? Langsung reload sendiri. Pengguna
     tidak perlu ngapa-ngapain.
   • Lu cukup timpa/push file ke GitHub → Vercel deploy →
     semua HP pengguna otomatis ke-update ±1 menit.
   • Offline tetap jalan (cache). Buka dari file:// juga
     aman (fitur ini otomatis nonaktif, nol error).
4. SIAP RILIS KE PLAY STORE:
   • Panduan lengkap gratis di PANDUAN-PLAYSTORE.txt
     (via PWABuilder, $25 sekali bayar; setelah live,
     update tetap otomatis lewat push GitHub).
5. LABEL VERSI: "Miapos F&B Suite v2.5" (Setelan → Mesin
   Lokal) buat mastiin update sudah masuk.

============================== RIWAYAT ==============================

v2.4 — NOTA DIPISAH + PREVIEW BISA DIEDIT:
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
   sw.js                 service worker AUTO-UPDATE (WAJIB ada
                         di repo biar app bisa update sendiri)
   miapos.html           redirect otomatis ke index.html (link lama aman)
   lib/                  library offline (WAJIB ADA)
   main.py               server Python + API + auto-backup
   engine/               C++ native analytics engine (source)
   install.sh            installer Termux
   start.sh              launcher 1-klik (Termux:Widget)
   manifest.json         data PWA (mode standalone: bilah notif terlihat)
   icon-192/512.png      ikon aplikasi
   PANDUAN-TERMUX.txt    panduan lengkap Termux
   PANDUAN-GITHUB.txt    cara push ke GitHub + fix merge conflict
   PANDUAN-PLAYSTORE.txt cara rilis ke Play Store (PWABuilder)

CARA PAKAI DI TERMUX
--------------------
   bash install.sh     (sekali saja, butuh internet)
   python main.py      (jalanin app — TANPA internet)

Lalu buka http://localhost:8080/miapos.html — atau lebih
enak: "Tambahkan ke layar utama" di Chrome → app jadi
kayak APK dengan ikon sendiri (judul di tengah, bilah
notifikasi tetap kelihatan, warnanya ngikut tema).

UPDATE VERSI BARU: cukup timpa file ke repo GitHub →
app auto-update sendiri di semua HP (sw.js). Tanpa
internet tetap jalan dari cache.

SELAMAT PAKAI! — Miapos v2.6
