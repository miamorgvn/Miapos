================================================
  MIAPOS v2.10 — SCAN BARCODE + LAPORAN MENU + QRIS
     + NOTIF WALAU APP DITUTUP + OWNER ZONE + CUACA
     + BACKUP CLOUD + 3 TEMA + SIAP PLAY STORE
================================================

APA YANG BARU DI v2.10 (scan barcode + laporan menu + QRIS + push server)
------------------------------------------------------------
1. SCAN BARCODE BUAT INPUT MENU:
   • Pengaturan → Kelola Menu → tombol SCAN (ikon barcode)
     di SAMPING tombol +.
   • Scan barcode/QR pakai kamera → tinggal isi nama + harga
     → menu langsung masuk daftar. Lanjut scan lagi-lagi,
     sekali sesi bisa masuk BANYAK menu sekaligus.
   • 100% OFFLINE — pakai BarcodeDetector bawaan Chrome
     Android, tanpa library internet.
   • Menu yang dibikin lewat scan langsung nyimpen barcodenya
     — scan ulang nanti dikenali (gak dobel).
   • Browser gak dukung kamera? Ada input kode manual.
2. LAPORAN MENU (MENGGANTIKAN LAYAR DAPUR/KDS):
   • Menu "Dapur (KDS)" diganti "Laporan Menu" — kelihatan
     hari ini kejual APA aja, BANYAKNYA berapa, per item per
     qty, langsung keSORTIR dari yang paling banyak terjual
     (+ omzet per menu + medali 3 besar).
   • Gak perlu geser-geser riwayat pesanan satu-satu lagi.
3. QRIS RESTO:
   • Owner Zone → seksi "QRIS Resto" → upload gambar QRIS
     (screenshot QRIS dari bank/e-wallet).
   • Otomatis muncul di layar pembayaran saat kasir pilih
     metode QRIS — customer tinggal scan.
4. NOTIF WALAU APP DITUTUP (PUSH SERVER):
   • Server Miapos ngirim notif buka (08.00 WIB) & tutup
     (21.00 WIB) langsung ke HP walau app-nya ditutup total
     — kayak notif WA. Yang jalan di HP cuma sistem
     notifikasi Android-nya (bukan app), baterai aman.
   • Butuh deploy: api/push-subscribe.js + api/push-send.js +
     vercel.json + package.json (sudah ada di zip ini) —
     langkahnya di PANDUAN-NOTIF.txt.
5. FIX BUG LAYAR PUTIH:
   • Stok & Bahan → tab Produk kadang blank putih (data
     lama/backup tanpa varian) — sudah dibaliki lapis
     normalisasi otomatis. Gak blank lagi.
6. OWNER ZONE MAKIN RAPIH:
   • Isinya sekarang SEKSI GULUNG: Notifikasi / Kartu Cuaca /
     Push Server / QRIS / Keamanan — klik baru layarnya
     kebuka, gak numpuk panjang ke bawah.
   • Teks kartu cuaca bisa diatur owner (kosong = salam
     otomatis yang ikut jam & nama kasir).
   • Kartu cuaca NAIK ke paling atas Dashboard (di atas
     4 kotak ringkasan) — sesuai permintaan.
7. IZIN NOTIFIKASI MAKIN GAMPANG:
   • Tombol Tes Notifikasi sekarang sekaligus minta izin
     (gak perlu nyari baris lain dulu).
   • Kalau izin diblokir, app kasih tahu langkah buka blokir
     di setelan HP. Detail: PANDUAN-NOTIF.txt.
8. SHEET "TAMBAH MENU" DI DETAIL PESANAN:
   • Buka pesanan (menu Pesanan) → "+ Tambah Menu" → muncul
     KOTAK BAWAH (drag-handle) yang tampilannya sama persis
     kaya layar Tambah Pesanan: search + chip kategori +
     daftar menu dengan tombol + hijau.
   • Menu yang ditambahin belakangan dikasih label "Tambahan"
     DI APLIKASI aja — di nota cetakan GAK ada tulisan
     tambahan (nota tetap bersih), sesuai permintaan.
9. CETAK DAPUR & CETAK TAMBAHAN (menu buka ke ATAS):
   • Di detail pesanan, tombol Cetak Dapur sekarang ada
     tanda panah ke ATAS — diklik muncul menu gelap ke atas:
     - CETAK DAPUR → semua item kecetak (nota dapur biasa).
     - CETAK TAMBAHAN → cuma menu yang ditambahin belakangan
       aja yang kecetak (kepala nota: "DAPUR - TAMBAHAN",
       nama menu tetap polos tanpa label tambahan).
   • Setelah cetak (dapur/tambahan), daftar "yang belum
     kecetak" direset — item tambahan berikutnya yang
     kecetak pas Cetak Tambahan selanjutnya.
   • Nota tambahan pakai printer DAPUR yang sama (gak perlu
     set printer baru).
10. SCAN QR/BARCODE DARI GAMBAR GALERI:
   • Layar scan sekarang ada tombol "Galeri" di samping KIRI
     kamera. Klik → pilih gambar/screenshot dari galeri HP →
     kodenya kebaca sama kaya scan kamera.
   • Berguna buat QR/barcode yang cuma punya bentuk
     screenshot-nya.
11. KATEGORI BISA DIBUAT & DIHAPUS (input menu manual):
   • Form Tambah/Edit Menu → grid kategori ada tile
     "+ Kategori" (garis putus-putus) → bikin kategori sendiri
     (nama + pilih ikon emoji).
   • Kategori buatan sendiri punya tombol x merah buat hapus
     — semua menu di dalamnya otomatis pindah ke Makanan
     (gak ada menu yang hilang).
   • Kategori baru langsung muncul di semua tempat: chip
     layar Tambah Pesanan, sheet Tambah Menu, scan barcode,
     Kelola Menu & grafik dashboard.
12. FIX BUG RpNaN:
   • Total pesanan kadang nampil "RpNaN" (screenshot owner
     31 Okt). Penyebabnya ketemu: tombol "Bayar Nanti" ikut
     ngirim event klik sebagai diskon. Udah dibenerin
     (diskon aneh otomatis dianggap 0) + semua tampilan
     total sekarang kebal NaN.

APA YANG BARU DI v2.9 (notif jadwal buka/tutup + Owner Zone + checklist 6/6)
------------------------------------------------------------
1. CHECKLIST SERVICE WORKER PWABUILDER — 6/6 LOLOS:
   • Sebelumnya 3 lolos (Has SW, Has Logic, Offline).
   • Sekarang tambar 3 yang kurang, kodenya beneran ada:
     - PUSH NOTIFICATIONS → handler 'push' di sw.js
     - BACKGROUND SYNC → handler 'sync' + pendaftaran
     - PERIODIC SYNC → handler 'periodicsync' + pendaftaran
   • Re-analyze URL di PWABuilder → skor kartu Service
     Worker jadi 6/6 (tambar +3).
2. NOTIFIKASI JADWAL BUKA & TUTUP RESTO:
   • Jam 08.00 (buka) → notif: "morgvn: Selamat pagi,
     saatnya memulai kembali bisnis yaaa! ..."
   • Jam 21.00 (tutup) → notif: "morgvn: Sudah jam 9 malam,
     waktunya tutup. Capek kan? ..." + GETAR PENDEK
     (bentar aja, gak lama).
   • Maks 1x per hari per jenis — gak nyerang terus.
   • Dikejar juga kalau app dibuka telat (masih dalam
     1 jam dari jadwal).
3. OWNER ZONE (FITUR KHUSUS OWNER, PAKAI PASSWORD):
   • Pengaturan → "Owner Zone 🔒" → isi password.
     Password default: morgvn — GANTI dari dalam
     (bagian Keamanan) biar cuma lu yang tahu.
   • Bisa diatur: jam buka, jam tutup, teks notif buka,
     teks notif tutup, nama pengirim (morgvn), saklar
     getar notif tutup, ganti password, + tombol
     Tes Notif Buka / Tes Notif Tutup.
   • Ada pratinjau isi notif sebelum disimpan.
   • Data tersimpan di HP tempat app jalan — bukan di
     Vercel; app-nya sendiri tetap dihosting Vercel.
4. SALAM DI DASHBOARD MAKIN PINTAR:
   • Tetap di bawah 4 kotak, ikut KASIR AKTIF (ganti
     kasir → nama ikut ganti) & ikut JAM (pagi/siang/
     sore/malam) — sekarang dicek tiap menit, jadi
     salamnya ganti sendiri walau app dibuka lama.
5. LABEL VERSI: "Miapos F&B Suite v2.9".

APA YANG BARU DI v2.8 (kartu cuaca + notifikasi salam pagi)
------------------------------------------------------------
1. KARTU CUACA DI DASHBOARD:
   • Suhu hari ini + kelembapan + gambar cuaca: matahari
     ☀️ cerah, awan mendung ☁️, gerimis 🌦️, hujan 🌧️,
     badai petir ⛈️ — otomatis sesuai kondisi nyata
     (data Open-Meteo, gratis, tanpa daftar apa pun).
   • Sekalian nampilin salam sesuai jam: "Selamat pagi,
     Chelsa! Saatnya buka lapak..." (pagi/siang/sore/malam).
   • Posisi pas: di bawah 4 kotak ringkasan, di atas grafik
     tren omzet — ukuran compak, gak makan tempat.
   • Butuh internet SESKALI (refresh ±30 menit). Offline?
     Kartu tetap nampilin data terakhir, app tetap jalan.
2. NOTIFIKASI SALAM PAGI (seperti yang diminta):
   • Tiap pagi (04.00–10.00, maks 1x sehari) app kirim
     notifikasi: "☀️ Selamat pagi, [nama]! Saatnya buka
     lapak — semangat memulai kembali bisnis hari ini! 💪"
   • Muncul di bilah notifikasi HP (beneran kayak notif WA).
   • Aktifinnya gampang: banner di Dashboard → IZINKAN.
     Bisa dimatiin di Pengaturan → "Notifikasi Salam Pagi".
     Ada tombol "Kirim Notifikasi Tes" buat mastiin jalan.
   • Notif diketuk → app Miapos langsung kebuka.
3. PANDUAN GITHUB DIRAPIKAN (PANDUAN-GITHUB.txt):
   • Tabel "FILE APA SAJA YANG HARUS DIPUSH" + penjelasan
     folder api/ (mesin backup cloud — WAJIB dipush) dan
     bagian "GAK PERLU UNINSTALL-UNINSTALL LAGI".
4. FILE BARU: CHECKLIST-UPDATE.txt — checklist semua fitur
   + langkah push langkah demi langkah.
5. LABEL VERSI: "Miapos F&B Suite v2.8".

APA YANG BARU DI v2.7 (backup cloud otomatis — tanpa Termux)
------------------------------------------------------------
1. BACKUP CLOUD OTOMATIS — DATA NYANGKUT DI GITHUB:
   • App yang dibuka lewat URL Vercel otomatis kirim
     snapshot data ke folder backups/ di repo GitHub —
     TANPA Termux, TANPA jaga server, TANPA nguras batre.
   • Sopan: maksimal 1x per 2 jam & hanya kalau data
     beneran berubah. Tiap backup = 1 commit di repo.
   • Rotasi otomatis: cukup 7 backup terakhir disimpan.
2. PULIHKAN DATA DARI HP MANA PUN:
   • Pengaturan → "Backup Cloud & Mesin Lokal" → daftar
     backup → ketuk "Pulihkan" → data diganti dari backup
     (selalu ada konfirmasi dulu). Ganti HP / HP hilang?
     Buka app → isi password → Pulihkan — beres.
3. LAYAR "MESIN LOKAL" JADI "BACKUP CLOUD & MESIN LOKAL":
   • Status jelas lewat badge: CLOUD AKTIF / ISI PASSWORD
     / PASSWORD SALAH / TERMUX AKTIF / STANDALONE.
   • Dibuka sebagai file HTML? Tetap tenang: SEMUA fitur
     jalan 100% offline & data aman di HP — pesan kuning
     yang dulu bikin panik sudah diganti yang menenangkan.
4. KEAMANAN:
   • Backup dijaga password (BACKUP_KEY di Vercel, diisi
     sekali di app). Salah password = ditolak server.
   • Termux tetap kompatibel (main.py tidak berubah) —
     backup mode Termux juga bisa dipulihkan dari app.
5. LABEL VERSI: "Miapos F&B Suite v2.7".
   SETUP SEKALI ±10 MENIT: ikuti PANDUAN-BACKUP-CLOUD.txt
   (bikin token GitHub → 2 env di Vercel → isi password
   di app). Sebelum setup, semua fitur tetap jalan normal.
   (Sejak v2.8: folder api/ WAJIB dipush ke repo — tanpa
   dia, backup cloud memang tidak jalan.)

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

SELAMAT PAKAI! — Miapos v2.10
