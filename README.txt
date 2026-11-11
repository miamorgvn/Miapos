================================================
  MIAPOS v2.27 — DIALOG UBAH METODE
     PEMBAYARAN DISEMAININ KAYA LAYAR BAYAR
     PERTAMA KALI (ADA INPUT UANG DITERIMA +
     TOMBOL CEPAT + KEMBALIAN) &
     DETAIL PESANAN LUNAS TINGGAL 1 TOMBOL
     (UBAH PESANAN DIHAPUS)
     (di bawah: pesanan batal gak lagi
     dihitung "Belum Bayar" + pesanan batal
     bisa dibuka lagi + biaya tambahan jadi
     item + pesanan udh done bisa dibatalkan +
     backup cloud tanpa password + keranjang
     rapi + catatan nota + tambahan
     ditandain + tombol biaya ikut tema + teks
     cuaca santai + laporan urut antrian +
     antrian auto-reset + back navigasi HP +
     sinkron antar HP + 2 bahasa + 4 tema)
================================================

APA YANG BARU DI v2.27 (dialog ubah metode kaya layar bayar)
------------------------------------------------------------
1. DIALOG "UBAH METODE PEMBAYARAN" DIROMBAK
   - SEKARANG KAYA LAYAR BAYAR PERTAMA
   KALI:
   • Kemarin dialognya cuma pilih Tunai/
     QRIS/Transfer terus Simpan. Sekarang
     tampilannya PERSIS kaya dialog
     "Pembayaran" waktu kasir nerima bayar
     pertama kali (yang ada pilihan uangnya
     itu loh).
   • Kalau pilih TUNAI: ada kolom "Uang
     Diterima" + 4 tombol cepat (Uang Pas,
     50.000, 100.000, 150.000) + baris
     "Kembalian" yang kehitung sendiri.
     Contoh: total 77.000, diisi 100.000 ->
     kembalian 23.000.
   • Kalau uangnya kurang dari total,
     tombolnya mati & tulisannya "Uang
     tidak cukup" - gak bisa salah simpan.
   • Pilih QRIS -> tampil gambar QRIS resto;
     pilih Transfer -> tampil info transfer.
     Sama kaya layar bayar pertama kali.
   • Uang diterima & kembalian yang diisi
     ikut TERSIMPAN di pesanan - catatan
     tunainya bener, struk yang dicetak
     berikutnya kecetak sesuai itu.
2. DETAIL PESANAN LUNAS TINGGAL 1 TOMBOL:
   • Pilihan "Ubah Pesanan" di pesanan yang
     udah dibayar DIHAPUS ("ubah jadi cmn
     metode pembayaran aja, ubah pesanannya
     diilangin"). Di detail pesanan lunas
     sekarang cuma ada tombol "Ubah Metode
     Pembayaran" - langsung kebuka, gak
     perlu lewat menu panah ke atas lagi.
   • Pesanan BELUM bayar tetap kaya biasa
     (gak dapet tombol ini) - cukup
     Batalkan Pesanan + Bayar Sekarang.
   • Pesanan batal tetap bisa dibuka lagi
     lewat tombol hijau "Ubah Pesanan"
     (fitur v2.25) - gak berubah.
   • Tombol merah "Batalkan Pesanan" tetap
     ada buat semua pesanan.
3. PERBAIKAN LAMA TETAP JALAN:
   • Pesanan batal gak lagi dihitung di chip
     "Belum Bayar" (fix v2.26).
   • Biaya tambahan tetap berbentuk item
     (qty + catatan + hapus, v2.24).
4. VERSI NAIK:
   • App v2.27 (footer sidebar + kartu
     Pengaturan) · cache sw.js miapos-v2.27-r1 ·
     server main.py v2.27 · package.json
     2.27.0.
   • Ingat aturannya: tiap update versi SELALU
     naik.

================================================
  CATATAN v2.26 (rilis sebelumnya) — PESANAN
     LUNAS BISA DIUBAH: TOMBOL "UBAH" (PANAH
     KE ATAS) BERISI UBAH PESANAN & UBAH
     METODE PEMBAYARAN
================================================

APA YANG BARU DI v2.26 (pesanan lunas bisa diubah — tombol panah ke atas)
------------------------------------------------------------
1. TOMBOL "UBAH" (PANAH KE ATAS) DI PESANAN
   YANG UDH DIBAYAR:
   • Pesanan yang udah done (sudah bayar)
     sekarang punya tombol "Ubah" dengan
     panah ke atas - polanya persis kaya
     tombol "Cetak Dapur" yang menu-nya buka
     ke atas. Dipencet -> muncul menu gelap
     ke atas berisi 2 pilihan. Tujuannya
     biar detail pesanan gak penuhin tombol.
   • Isinya: "Ubah Pesanan" & "Ubah Metode
     Pembayaran".
   • Tombol merah "Batalkan Pesanan" tetap
     ada - buat pesanan lunas maupun yang
     belum bayar.
   • Pesanan yang BELUM bayar gak dapet
     menu ini - tampilannya masih kaya
     biasa (Tambah Biaya Tambahan, Cetak
     Struk/Dapur, Batalkan Pesanan, Bayar
     Sekarang). Pesanan batal tetap pakai
     tombol hijau "Ubah Pesanan" yang lama.
   • Di Riwayat/Laporan (tanggal lampau),
     menu Ubah cuma berisi Ubah Metode
     Pembayaran - isi pesanan tanggal lampau
     memang buat dilihat aja.
2. UBAH METODE PEMBAYARAN (GANTI CARA BAYAR
   TANPA BATALKAN):
   • Ini buat keluhan kemarin: pelanggan
     konfirmasi QRIS pas udah "done", eh
     ternyata dia bayar tunai. Sekarang gak
     perlu batal-bikin-lagi: buka detail
     pesanannya -> Ubah -> Ubah Metode
     Pembayaran -> pilih Tunai/QRIS/Transfer
     -> Simpan. Beres.
   • Pesanan tetap tercatat SUDAH BAYAR &
     omzet gak berubah - jumlahnya sama,
     cuma metodenya yang keganti.
   • Struk kasir yang dicetak berikutnya
     otomatis pakai metode yang baru.
3. UBAH PESANAN DI PESANAN YANG UDH DIBAYAR:
   • Pilihan "Ubah Pesanan" di pesanan lunas
     kerjanya kaya di pesanan batal: SEMUA
     detail dimuat ke keranjang (menu + qty,
     biaya tambahan, pelanggan, meja,
     catatan, diskon) -> ubah yang perlu ->
     bayar lagi.
   • Pesanan lunas yang aslinya OTOMATIS
     dibatalkan dulu (badge Dibatalkan, gak
     dihitung omzet, bahan baku balik ke
     stok) - biar omzet gak kehitung DOBEL.
     Notifikasinya juga nyebutin ini.
4. PESANAN BATAL GAK LAGI DIHITUNG "BELUM
   BAYAR" (FIX):
   • Bug kemarin: di daftar Pesanan, pesanan
     yang udah dibatal masih kehitung di
     chip "Belum Bayar (1)" & di tulisan
     "1 belum bayar" di atas - padahal
     badgenya udah Dibatalkan.
   • Sekarang pesanan batal cuma tampil di
     "Semua Status"; filter Belum Bayar &
     Sudah Bayar plus hitungannya udah bener.
5. VERSI NAIK:
   • App v2.26 (footer sidebar + kartu
     Pengaturan) · cache sw.js miapos-v2.26-r1 ·
     server main.py v2.26 · package.json
     2.26.0.
   • Ingat aturannya: tiap update versi SELALU
     naik.

================================================
  CATATAN v2.25 (rilis sebelumnya) — PESANAN
     YANG DIBATALKAN BISA DIBUKA LAGI
     (UBAH PESANAN) — GA PERLU BIKIN DARI NOL
================================================

APA YANG BARU DI v2.25 (pesanan batal bisa diubah lagi)
------------------------------------------------------------
1. PESANAN YANG UDH DIBATALKAN BISA DIBUKA
   LAGI — TOMBOL "UBAH PESANAN":
   • Ini nyambung sama fitur kemarin (pesanan
     done bisa dibatalin). Kemarin kasirnya
     batalkan pesanan QRIS terus bikin lagi
     dari nol buat bayar tunai — capek, menu
     satu-satunya harus diketik ulang.
   • Sekarang: buka pesanan yang dibatalkan
     (yang ada badge merah "Dibatalkan") ->
     di bawah ada tombol hijau "Ubah
     Pesanan" -> SEMUA detailnya langsung
     masuk keranjang: menu + qty, biaya
     tambahan (qty & catatannya juga), nama
     pelanggan, tempat/meja, catatan dapur,
     sampai diskon.
   • Tinggal ubah yang perlu doang (misal
     pembayarannya ganti tunai) -> bayar
     seperti biasa. Gak perlu ngetik ulang
     dari awal.
   • Pesanan yang dibayar ulang jadi
     pesanan sendiri (nomor baru) — catatan
     yang lama tetap ada sebagai
     "Dibatalkan" & tetap gak dihitung
     omzet, jadi angka laporan tetap jujur
     (omzet kehitung sekali doang).
   • Cuma muncul di menu PESANAN hari ini —
     riwayat tanggal lampau di Laporan cuma
     buat dilihat, bukan diubah.
2. KONFIRMASI BATAL MAKIN JELAS:
   • Teks konfirmasi "Batalkan Pesanan"
     sekarang ngeingetin: pesanan yang
     dibatal MASIH BISA dibuka lagi lewat
     tombol Ubah Pesanan — jadi gak takut
     salah pencet, kebalik lagi mah gampang.
3. DETAIL PESANAN BATAL = BACA SAJA:
   • Di pesanan yang udah dibatal, tombol
     "+ Tambah Pesanan" & "+ Tambah Biaya
     Tambahan" disembunyiin — mau ubah isi
     pesanannya lewat tombol Ubah Pesanan
     aja, biar alurnya satu & gak nutupin
     catatan batal.
4. VERSI NAIK:
   • App v2.25 (footer sidebar + kartu
     Pengaturan) · cache sw.js miapos-v2.25-r1 ·
     server main.py v2.25 · package.json
     2.25.0.
   • Ingat aturannya: tiap update versi SELALU
     naik.

================================================
  CATATAN v2.24 (rilis sebelumnya) — BIAYA
     TAMBAHAN JADI ITEM (QTY + CATATAN +
     HAPUS) · PESANAN YANG UDH DONE BISA
     DIBATALKAN
================================================

APA YANG BARU DI v2.24 (biaya kaya menu + batalkan pesanan)
------------------------------------------------------------
1. BIAYA TAMBAHAN SEKARANG KAYA MENU:
   • Di keranjang & di detail pesanan, tiap
     biaya tambahan jadi KARTU ITEM sendiri:
     ada QTY (+/-), kolom CATATAN, tombol
     hapus, dan subtotal per baris - persis
     kaya kartu menu di keranjang.
   • "Jumlah Biaya" sekarang artinya HARGA
     SATUAN. Total biayanya = satuan x qty.
     Contoh: Packing Rp2.800 x 3 = Rp8.400.
   • Catatan per biaya juga bisa - ikut
     tercetak di struk kasir (di bawah
     baris biayanya).
   • Di struk kasir, kalau qty lebih dari 1,
     barisnya jadi "Biaya: 3x Packing".
   • Biaya lama yang belum punya qty tetap
     dihitung qty 1 - gak ada angka yang
     berubah sendiri.
2. PESANAN YANG UDH DONE (SUDAH BAYAR) BISA
   DIBATALKAN:
   • Ini buat keluhan kemarin: pelanggan
     konfirmasi QRIS, ternyata transaksinya
     gagal, dia mau ganti tunai. Dulu
     pesanan udah kecatat bayar QRIS &
     masuk omzet - bingung mau apain.
   • Sekarang: buka detail pesanannya ->
     tombol merah "Batalkan Pesanan" ->
     konfirmasi dulu (biar gak kepencet) ->
     beres. Terus bikin pesanan baru, bayar
     tunai. Cuma beda 2x klik.
   • Pesanan yang dibatalkan dikasih badge
     merah "Dibatalkan" di daftar pesanan,
     detail, & riwayat - catatannya tetap
     ada, gak dihapus.
   • Omzet & SEMUA laporan (dashboard,
     laporan menu, laporan pembayaran,
     riwayat pesanan, Owner Zone, export
     Excel) otomatis TIDAK menghitung
     pesanan batal - angka tetap jujur.
   • Bahan baku yang kepotong waktu pesanan
     dibuat OTOMATIS BALIK ke stok, tercatat
     di Riwayat Pergerakan Stok dengan
     alasan "Pembatalan Pesanan" (+ angka).
   • Meja yang nempel di pesanan batal juga
     langsung lepas.
3. VERSI NAIK:
   • App v2.24 (footer sidebar + kartu
     Pengaturan) · cache sw.js miapos-v2.24-r1 ·
     server main.py v2.24 · package.json
     2.24.0.
   • Ingat aturannya: tiap update versi SELALU
     naik.

================================================
  CATATAN v2.23 (rilis sebelumnya) — BACKUP
     CLOUD TANPA PASSWORD (CUKUP LOGIN AKUN)
     · JAWABAN SOAL ENGINE C++ · CORDOVA ·
     PESANAN "HILANG"
================================================

APA YANG BARU DI v2.23 (backup bebas password)
------------------------------------------------------------
1. BACKUP CLOUD TANPA PASSWORD:
   • Dulu buat nyalain backup otomatis ke GitHub
     harus isi "password backup" (BACKUP_KEY)
     di Pengaturan — ribet.
   • Sekarang cukup LOGIN AKUN (no. HP + kata
     sandi seperti biasa): backup otomatis jalan
     sendiri (maks. 1x per 2 jam kalau data
     berubah), tombol "Backup Sekarang" &
     "Pulihkan" juga langsung jalan TANPA isi
     password apa pun.
   • Password backup (BACKUP_KEY di Vercel)
     jadi OPSIONAL — cuma dipakai kalau belum
     login / mau pakai kunci sendiri. Yang udah
     pernah nge-key tetap jalan kayak biasa.
2. UPDATE APP GAK PERLU LOGOUT — INGAT INI:
   • Timpa file repo → push → tunggu deploy →
     buka app: akun TETAP ke-login, data TETAP
     ada. Gak perlu keluar-masuk akun lagi,
     gak perlu sinkron ulang.
   • Asal domain/URL-nya SAMA. Kalau pindah ke
     domain baru, ya login sekali lagi — data
     akun otomatis keunduh dari cloud.
3. PESANAN KEMARIN "HILANG"? ENGGA — DIARSIP:
   • Tiap ganti hari, pesanan hari sebelumnya
     otomatis pindah ke arsip biar daftar
     pesanan bersih cuma nampilin hari ini.
   • Cek lagi di: LAPORAN → tab "Riwayat
     Pesanan" → pilih tanggalnya. Omzet &
     Laporan Pembayaran tetap ngitung semuanya.
4. SOAL MAIN.PY + ENGINE C++ (jawaban):
   • Dua-duanya GAK aktif sendiri & GAK wajib.
     App web (index.html di Vercel) jalan
     sendiri — sinkron antar HP pakai api/
     sync.js yang aktif OTOMATIS begitu deploy
     ke Vercel (butuh env GITHUB_TOKEN sekali
     setel di Vercel).
   • main.py = server OPSIONAL buat PC/Termux
     (backup lokal + analytics) — baru jalan
     kalau lu jalanin sendiri (python main.py
     atau install.sh). Engine C++ ikut
     dicompile sama main.py, bukan buat web.
5. MAU JADI APLIKASI ANDROID (CORDOVA)?
   • BISA — index.html DOANG cukup. App-nya
     100% offline & tombol back HP udah jalan
     (sama kaya sekarang).
   • Tips: arahkan WebView ke URL Vercel lu
     (bukan file index.html lokal) biar sinkron
     & backup cloud tetap jalan di dalam APK.
     Kalau index.html dibuka lokal di WebView,
     app tetap jalan penuh tapi sinkron antar
     HP mati (API /api/* gak ada di situ).
6. VERSI NAIK:
   • App v2.23 (footer sidebar + kartu
     Pengaturan) · cache sw.js miapos-v2.23-r1 ·
     server main.py v2.23 · package.json
     2.23.0.
   • Ingat aturannya: tiap update versi SELALU
     naik.

================================================
  CATATAN v2.22 (rilis sebelumnya) — TOMBOL
     "+ TAMBAH MENU" DI KERANJANG DIHAPUS
     (NYEMPIL) · BIAYA TAMBAHAN TETAP
================================================

APA YANG BARU DI v2.22 (keranjang dirapikan)
------------------------------------------------------------
1. TOMBOL "+ TAMBAH MENU" DI KERANJANG DIHAPUS:
   • Di v2.21 tombol "+ Tambah Menu" nyempil di
     keranjang, persis di bawah pilihan Dine In /
     Bawa Pulang — malah bikin sesak.
   • Sekarang DIHAPUS total, di HP (mobile) &
     desktop sama-sama bersih.
   • Nambah menu tetap gampang: tutup keranjang →
     ketuk menunya di layar Tambah Pesanan → qty
     otomatis gabung ke keranjang. Jadi gak perlu
     tombol dobel.
2. TOMBOL "TAMBAH BIAYA TAMBAHAN" TETAP DI SITU:
   • Masih PERSIS di bawah pilihan Dine In / Bawa
     Pulang, sekarang full-width (lebih rapi).
   • Formnya tetap sama: Nama Biaya + Jumlah Biaya
     → Simpan. Daftar biayanya tampil di atas
     Subtotal, bisa dihapus lagi, langsung masuk
     Total, dan ikut ke pesanan + struk kasir.
3. VERSI NAIK:
   • App v2.22 (footer sidebar + kartu
     Pengaturan) · cache sw.js miapos-v2.22-r1 ·
     server main.py v2.22 · package.json
     2.22.0.
   • Ingat aturannya: tiap update versi SELALU
     naik.

================================================
  CATATAN v2.21 (rilis sebelumnya) — KERANJANG ·
     CATATAN NOTA DI DETAIL · TAMBAHAN DIGABUNG
     TETAP DITANDAIN
================================================

APA YANG BARU DI v2.21 (keranjang · catatan nota · pelacakan tambahan)
------------------------------------------------------------
1. KERANJANG: TOMBOL "+ TAMBAH MENU" DITARO
   DI BAWAH PILIHAN DINE IN / BAWA PULANG:
   (v2.22: tombol ini DIHAPUS lagi — nyempil.
     Lihat APA YANG BARU DI v2.22 di atas.)
   • Dulu buat nambah menu, keranjang harus
     ditutup dulu baru balik ke daftar menu.
   • Sekarang di keranjang, PERSIS di bawah
     pilihan Dine In / Bawa Pulang, ada tombol
     "+ Tambah Menu" di tengah. Ketuk → muncul
     daftar menu (tampilannya sama kaya layar
     Tambah Pesanan) → ketuk menunya → langsung
     masuk keranjang tanpa nutup apa-apa.
     Jumlah yang udah ada di keranjang tampil
     di bawah tombol +.
2. KERANJANG: TOMBOL "TAMBAH BIAYA TAMBAHAN":
   • Dulu biaya tambahan (ongkir, packing,
     dll) cuma bisa diisi dari detail pesanan
     — setelah pesanan jadi.
   • Sekarang tombolnya ada juga DI KERANJANG,
     persis di bawah pilihan Dine In / Bawa Pulang
     (v2.22: tombol + Tambah Menu dihapus, tombol
     biaya jadi full-width). Formnya sama: Nama
     Biaya + Jumlah Biaya →
     Simpan. Daftar biayanya tampil di atas
     Subtotal, bisa dihapus lagi, dan langsung
     masuk Total. Begitu pesanan dibayar/
     disimpan/dicetak, biayanya ikut ke
     pesanan & tercetak di struk kasir.
3. DETAIL PESANAN: TOMBOL "CATATAN NOTA":
   • Dulu catatan di header nota cuma bisa
     diisi waktu bikin pesanan baru.
   • Sekarang di detail pesanan ada tombol
     "Catatan Nota" (di bawah daftar item).
     Ketuk → tulis "Bungkus" / "Bawa Pulang"
     dsb → Simpan. Catatannya masuk ke HEADER
     nota dapur pas dicetak, dan langsung
     tampil di info pesanan.
4. MENU SAMA YANG DITAMBAH LAGI: GABUNG,
   TAPI DITANDAIN "TAMBAHAN +N":
   • Dulu menu yang sama yang ditambahin
     lewat sheet Tambah Pesanan digabung ke
     baris yang sama, tapi tanda Tambahan-nya
     hilang — jadi gak ikut kecetak di nota
     tambahan.
   • Sekarang qty tetap gabung, TAPI
     tambahannya dicatat di aplikasi:
     - Badge "Tambahan +N" tampil di baris
       itu (N = porsi yang ditambahin).
     - Tombol + di detail pesanan juga dihitung
       tambahan (tombol − ngurangin lagi).
     - "Cetak Tambahan" mencetak CUMA porsi
       yang ditambahin (bukan satu baris
       penuh) — dan tambahan yang sudah pernah
       kecetak gak diulang lagi.
   • Daftar Pesanan ikut nandain: kartu
     pesanan yang pernah ditambahin menu
     tampil catatan "🏷️ Ada Tambahan".
5. VERSI NAIK:
   • App v2.21 (footer sidebar + kartu
     Pengaturan) · cache sw.js miapos-v2.21-r1 ·
     server main.py v2.21 · package.json
     2.21.0.
   • Ingat aturannya: tiap update versi SELALU
     naik.

================================================
  CATATAN v2.20 (rilis sebelumnya) — TOMBOL
     BIAYA IKUT TEMA · TEKS CUACA SANTAI ·
     LAPORAN URUT ANTRIAN · ANTRIAN AUTO-RESET
================================================

APA YANG BARU DI v2.20 (tema · teks cuaca · laporan · antrian)
------------------------------------------------------------
1. TOMBOL BIAYA TAMBAHAN IKUT WARNA TEMA:
   • Dulu tombol "Tambah Biaya Tambahan" selalu
     merah di tema apa pun.
   • Sekarang warnanya ikut tema yang dipilih
     (Emerald = hijau, Royal = oranye, Pink =
     pink, Charcoal = neon) — sama kaya tombol
     lain, konsisten.
2. TEKS RANDOM KARTU CUACA DITULIS ULANG:
   • Dulu kaya poster motivasi ("Hari ini sudah
     hebat, saatnya rehat") — terlalu baku,
     kaku, dan cringe.
   • Sekarang kaya teman ngobrol santai di
     kasir: "Udah makan belum? Kasir juga butuh
     makan", "Antriannya panjang? Berarti
     masakannya emang enak", dll. Tetap tanpa
     istilah teknis/data/server.
3. TEKS CUACA GANTI TIAP 5 MENIT:
   • Dulu teksnya bisa ganti setiap pindah
     layar.
   • Sekarang teksnya DIKUNCI 5 MENIT — pindah
     layar, tutup-buka app, ganti tab: tetap
     sama. Setelah 5 menit ganti sendiri, dan
     gak ngulang kalimat yang sama berturut-
     turut. Pas periode berganti (pagi→siang→
     sore→malam) teksnya ikut pindah pool.
4. LAPORAN PEMBAYARAN URUT NO. ANTRIAN:
   • Daftar transaksi lunas dulu diurut dari
     waktu bayar (terbaru di atas); sekarang
     diurut dari NO. ANTRIAN kecil → besar
     (1, 2, 3, ...) biar enak dicek. Kalau
     nomornya sama/kosong, baru pakai waktu
     bayar. Kartu tanggal tetap berfungsi.
5. NO. ANTRIAN AUTO-RESET GANTI HARI:
   • Dulu counter antrian cuma reset manual
     (Pengaturan → Reset Antrian) — kalau
     lupa, besoknya lanjut nomor kemarin.
   • Sekarang begitu tanggal berganti (jam 12
     malam waktu HP), pesanan pertama otomatis
     dapat No. 1 lagi. Reset manual tetap ada.
   • Tampilan "No. Antrian Berikutnya" di
     Pengaturan juga sadar-tanggal: pas hari
     baru yang belum ada pesanan, tampil 1
     (dengan keterangan "Ganti hari otomatis
     mulai dari 1").
6. FILE NOTIF YANG TERSISA DIHAPUS PERMANEN:
   • Sejak v2.10 fitur notifikasi dicabut, tapi
     file panduan & API-nya masih tertinggal di
     repo (PANDUAN-NOTIF.txt, api/push-*.js,
     api/_pushlib.js) — padahal gak kepakai
     lagi.
   • v2.20: semuanya DIHAPUS dari repo. App
     memang gak bisa push notif (fiturnya sudah
     diangkat sejak v2.10), jadi tinggalan-nya
     dibuang biar repo bersih.
7. VERSI NAIK:
   • App v2.20 (footer sidebar + kartu
     Pengaturan) · cache sw.js miapos-v2.20-r1 ·
     server main.py v2.20 · package.json
     2.20.0.
   • Ingat aturannya: tiap update versi SELALU
     naik.

================================================
  CATATAN v2.19 (rilis sebelumnya) — BIAYA
     TAMBAHAN · FIX MENU DOBEL · BACK NAVIGASI HP
================================================

APA YANG BARU DI v2.19 (biaya tambahan + fix menu dobel + back HP)
------------------------------------------------------------
1. TOMBOL TAMBAH BIAYA TAMBAHAN (detail pesanan):
   • Di detail pesanan (layar yang menampilkan menu-menu
     pesanan pelanggan) sekarang ada tombol merah
     "Tambah Biaya Tambahan" di bawah kartu Total.
   • Dipencet → muncul form: Nama Biaya + Jumlah Biaya
     → Simpan (sesuai contoh layout dari owner).
   • Biaya ini di luar menu (contoh: ongkos kirim,
     packing) — ikut menghitung Total tagihan,
     tampil sebagai baris "Biaya: <nama>" di struk
     kasir, dan bisa dihapus lagi selama pesanan
     belum dibayar.
   • Dialog bayar & laporan otomatis ikut total baru.
2. FIX: MENU YANG SAMA GAK KEPISAH LAGI:
   • Dulu di sheet tambah item, menu yang sama dipencet
     2x malah bikin baris sendiri di bawahnya.
   • Sekarang digabung: qty bertambah (2x, 3x, ...)
     di baris yang sama.
3. TOMBOL "TAMBAH MENU" JADI "TAMBAH PESANAN":
   • Tombol di detail pesanan + judul sheet-nya ganti
     jadi "Tambah Pesanan". (Yang di Kelola Menu tetap
     "Tambah Menu" karena fungsinya bikin menu baru.)
   • Di bawah tombol + sekarang tampil jumlah item
     menu itu yang sudah ada di pesanan (contoh: 2x).
4. PRATINJAU NOTA: TAB NOTA DAPUR-TAMBAHAN:
   • Pengaturan → Pratinjau Nota kini punya 3 tab:
     Nota Kasir · Nota Dapur · Nota Dapur-Tambahan.
5. TOMBOL BACK NAVIGASI HP SEKARANG JALAN DI APP:
   • Lagi di detail pesanan (menu-menu pesanan
     pelanggan) → klik back → balik ke daftar pesanan
     hari itu.
   • Lagi di daftar pesanan → klik back → ke Dashboard.
   • Di Dashboard: back pertama muncul pengingat
     "Tekan sekali lagi untuk keluar aplikasi",
     back kedua (dalam 2,5 detik) keluar aplikasi.
   • Back saat dialog bayar terbuka = batalkan dialog.
6. BAHASA BAKU:
   • Sesuai aturan owner, semua teks baru tetap
     menggunakan bahasa Indonesia baku.
7. VERSI NAIK:
   • App v2.19 (footer sidebar + kartu Pengaturan) ·
     cache sw.js miapos-v2.19-r1 · server api/sync.js
     & main.py v2.19.
   • Ingat aturannya: tiap update versi SELALU naik.

================================================
  CATATAN v2.18 (rilis sebelumnya) — NO. ANTRIAN
     KASIH JEDA 1 BARIS
================================================

APA YANG BARU DI v2.18 (No. Antrian gak nempel lagi)
------------------------------------------------------------
1. JEDA SATU BARIS SEBELUM NO. ANTRIAN:
   • Dulu "No. Antrian: 24" nempel persis di bawah
     daftar menu/catatan item — keliatan sesak.
   • Sekarang dikasih SATU baris kosong dulu,
     jadi daftar menu ... (jeda) ... No. Antrian.
     Lebih lega dan matanya langsung ke angka.
   • Berlaku untuk nota dapur & nota dapur
     tambahan. Nota kasir tidak berubah.
2. SISANYA SAMA DENGAN v2.17: judul DAPUR tetap
   tinggi dobel (lonjong) sama kaya No. Antrian,
   garis pembatas cukup satu di bawah header.
3. BAHASA BAKU:
   • Sesuai aturan owner, semua teks baru tetap
     menggunakan bahasa Indonesia baku.
4. VERSI NAIK:
   • App v2.18 (footer sidebar + kartu
     Pengaturan) · cache sw.js miapos-v2.18-r1 ·
     server api/sync.js & main.py v2.18.
   • Ingat aturannya: tiap update versi SELALU
     naik.

================================================
  CATATAN v2.17 (rilis sebelumnya) — JUDUL DAPUR
     SEBESAR NO. ANTRIAN
================================================

APA YANG BARU DI v2.17 (judul DAPUR sebesar No. Antrian)
------------------------------------------------------------
1. JUDUL "DAPUR" DICETAK TINGGI DOBEL (LONJONG):
   • Dulu tulisan DAPUR di kepala nota dapur
     ukurannya sama kaya tulisan biasa — cuma
     No. Antrian yang besar/lonjong.
   • Sekarang DAPUR dicetak dengan mode
     Double-Height (ESC ! 0x10) — tinggi dobel,
     lonjong ke bawah, SAMA PERSIS kaya No.
     Antrian di bawahnya. Nota dapur langsung
     kelihatan headernya dari jauh.
   • Berlaku juga untuk nota "DAPUR - TAMBAHAN".
   • Nota kasir tidak berubah (tetap font normal).
2. INFO: GARIS BAWAH SEBELUM NO. ANTRIAN SUDAH
   DIHAPUS SEJAK v2.16:
   • Permintaan owner: garis pembatas di bawah
     daftar menu cukup diilangin, jadi daftar
     menu langsung ketemu No. Antrian.
   • Kalau di nota cetakan masih muncul dua
     garis ('=' di bawah daftar menu), artinya
     app di HP masih versi lama — buka app
     sampai penuh saat online supaya service
     worker mengambil versi terbaru, lalu cek
     tulisan versi di Pengaturan (harus v2.17).
3. BAHASA BAKU:
   • Sesuai aturan owner, semua teks baru tetap
     menggunakan bahasa Indonesia baku.
4. VERSI NAIK:
   • App v2.17 (footer sidebar + kartu
     Pengaturan) · cache sw.js miapos-v2.17-r1 ·
     server api/sync.js & main.py v2.17.
   • Ingat aturannya: tiap update versi SELALU
     naik.

================================================
  CATATAN v2.16 (rilis sebelumnya) — NOTA CUKUP 1
     GARIS '=' · POPUP HASIL CETAK · ANGKA LAPORAN
================================================

APA YANG BARU DI v2.16 (nota rapih + popup cetak + angka muat)
------------------------------------------------------------
1. GARIS '====' DI NOTA CUKUP SATU (HEMAT KERTAS):
   • Dulu nota kasir & nota dapur masing-masing
     punya DUA garis '=' (bawah header + sebelum
     footer) — keliatan dobel & makan tempat.
   • Sekarang cukup SATU garis di bawah header;
     bagian bawah langsung No. Antrian (dapur) /
     ucapan terima kasih (kasir).
   • Berlaku untuk semua nota: kasir, dapur, dan
     nota tambahan. Pratinjau Nota di Pengaturan
     ikut menampilkan bentuk barunya.
2. POPUP HASIL CETAK — BERHASIL/GAGAL SELALU TERTERA:
   • Dulu cetak sukses itu SENYAP — kasir harus
     bolak-balik ngecek printer sendiri.
   • Sekarang setiap cetak muncul POPUP:
     - HIJAU "Nota Berhasil Dicetak" + nama
       printernya.
     - MERAH "Nota Gagal Dicetak" + alasannya,
       plus tombol "Salin Teks Nota" buat dicetak
       manual.
   • Jalan untuk SEMUA tombol cetak: Cetak Dapur,
     Cetak Struk, dan tombol cetak di layar
     Pembayaran Berhasil.
3. ANGKA LAPORAN OTOMATIS MENYESUAIKAN LEBAR KARTU:
   • Dulu omzet yang panjang kepotong jadi
     "Rp4.081.00…" di kartu Laporan Menu.
   • Sekarang angka otomatis mengecil sampai muat
     penuh — berlaku di Laporan Menu, Laporan
     Pembayaran, dan kartu statistik dashboard.
4. BAHASA MAKIN BAKU:
   • Seluruh teks aplikasi dirapikan ke bahasa
     Indonesia baku: sapaan dashboard, tips
     laporan, pesan scan QR, Owner Zone, dan
     pesan-pesan lainnya. Sesuai aturan owner:
     setiap update, bahasa wajib baku.
5. VERSI NAIK:
   • App v2.16 (footer sidebar + kartu Pengaturan)
     · cache sw.js miapos-v2.16-r1 · server
     api/sync.js & main.py v2.16.
   • Ingat aturannya: tiap update versi SELALU naik.

================================================
  CATATAN v2.15 (rilis sebelumnya) — FIX SINKRON:
     CUKUP KATA SANDI AKUN · STATUS SINKRON JUJUR
================================================

APA YANG BARU DI v2.15 (fix: menu gak masuk ke HP lain)
------------------------------------------------------------
KEJADIAN: menu yang diinput di HP pertama (ikon + di
  tengah → Tambah Menu) gak muncul di HP kedua walau
  akunnya sama.
SEBABNYA (ketemu & dibenerin):
  1) SINKRON DULU WAJIB PASSWORD BACKUP CLOUD — dan
     kalau di salah satu HP password itu belum diisi,
     kirim/tarik data DIBATALIN DALAM SENYAP (gak ada
     pesan apa-apa). Jadi menu lu gak pernah naik ke
     cloud → HP kedua gak dapat apa-apa.
  2) Kalau app dibuka dari GitHub Pages / hosting
     statis (bukan Vercel / Termux), sinkron memang
     gak bisa jalan — juga dulu gak ada pemberitahuan
     yang jelas.
1. SINKRON SEKARANG CUKUP KATA SANDI AKUN (TANPA SETUP):
   • Server (api/sync.js & main.py) sekarang menerima
     KATA SANDI AKUN yang lu ketik waktu login — jadi
     HP lain tinggal MASUK dengan akun yang sama,
     data langsung ngalir. GAK PERLU setel password
     Backup Cloud dulu buat sinkron (jalur password
     backup lama tetap jalan buat yang mau pakai).
   • Login di HP kedua juga sekarang bawa password
     akunnya — kalau password salah, MUNCUL PESAN
     "Kata sandi salah", bukan diam-diam gagal.
2. STATUS SINKRON YANG JUJUR (kartu akun, Pengaturan):
   • Hijau = AKTIF + kunci pakai apa (kata sandi akun
     / password backup) + jam kirim & tarik terakhir.
   • Kuning = sebabnya ditulis + solusinya (belum
     login, server belum ada / belum diupdate).
   • Merah = password salah → disuruh login ulang.
   • Tombol SINKRON SEKARANG sekarang selalu bisa
     nyoba ulang (dulu gagal diam kalau server belum
     terdeteksi).
3. AUTO-UP: begitu password backup diisi di Pengaturan,
   data akun langsung dinaikkan ke cloud otomatis
   (dulu nunggu perubahan data berikutnya).
4. CARA PASTIKAN MENU LU MASUK (urutan cek):
   ① UPDATE DEPLOYMENT: timpa semua file repo dengan
     isi zip ini (index.html + sw.js + api/ + main.py
     + semuanya) → push → tunggu deploy beres.
   ② DI KEDUA HP: buka app-nya sampe kebuka penuh
     (biar service worker ambil v2.15) — cek footer
     bawah / kartu Pengaturan harus tulis v2.15.
   ③ HP 1: Pengaturan → Akun → masuk akun lu →
     tunggu status sinkron HIJAU (kunci: kata sandi
     akun) + ada jam "kirim terakhir".
   ④ HP 2: keluar dulu (kalau udah keburu masuk
     pakai cara lama), terus MASUK LAGI dengan nomor
     HP + kata sandi akun yang sama → data menu
     langsung keunduh.
   ⑤ Kalau status kuning tulis "butuh server" → app
     lu bukan dari Vercel/Termux. Pindah ke alamat
     Vercel (atau jalanin python main.py).
5. VERSI NAIK:
   • App v2.15 · cache sw.js miapos-v2.15-r1 ·
     server api/sync.js & main.py v2.15.
   • Ingat aturannya: tiap update versi SELALU naik.

================================================
  CATATAN v2.14 (rilis sebelumnya) — SINKRON OTOMATIS
     ANTAR HP VIA AKUN · LAPORAN PEMBAYARAN + KALENDER
================================================

APA YANG BARU DI v2.14 (sinkron otomatis akun + laporan pembayaran)
------------------------------------------------------------
1. SINKRON OTOMATIS ANTAR HP — GAK PERLU INPUT/SCAN ULANG:
   • Dulu: HP lain mau dipakai jualan? Harus scan QR
     akun / tempel kode manual dulu, capek sendiri.
   • Sekarang: cukup LOGIN ke akun yang sama di HP
     baru → SEMUA DATA LANGSUNG MASUK SENDIRI — menu,
     pesanan, omzet, stok, laporan, pengaturan.
     Gak perlu scan apa-apa. 🎉
   • DUA ARAH & BERJALAN TERUS: HP A nambah menu →
     HP B otomatis ke-update beberapa detik kemudian
     (saat online). Internet mati? Tetap jalan normal,
     begitu online datanya ketrimbalan sendiri.
   • PENGHAPUSAN JUGA IKUT: menu/pesanan yang dihapus
     di HP A gak bakal bangkit lagi di HP B
     (pencatatan hapus / tombstone).
   • CARA PAKAI:
     1. HP utama: isi Kata Sandi Backup Cloud di
        Pengaturan → Backup Cloud & Mesin Lokal
        (ini kunci sinkronnya — jangan lupa!).
     2. HP lain: Pengaturan → Akun → masuk dengan
        nomor HP + kata sandi akun yang sama.
     3. Selesai — data masuk sendiri, statusnya bisa
        dilihat di kartu akun: "Sinkron otomatis
        AKTIF" + waktu sinkron terakhir.
   • BUTUH SERVER: deploy di Vercel (file api/sync.js
     udah disediakan) atau jalanin main.py di Termux/
     komputer. Data akun disimpan satu file JSON per
     akun di folder sync/ repo — kuncinya kata sandi,
     bukan siapa-siapa bisa baca.
   • Tetap ada mode lama buat kondisi offline: QR Akun
     & Kode Data Lengkap gak diilangin.
2. LAPORAN PEMBAYARAN (DI PENGATURAN):
   • Pengaturan → LAPORAN PEMBAYARAN — lihat hari
     ini orang bayar pakai apa aja: Tunai / QRIS /
     Transfer, ada total per metode + daftar per
     transaksi (jam, meja, jumlah, metode).
   • Cocok buat jam tutup: cocokin uang fisik di
     kasir sama catatan app.
3. BISA LIHAT HARI-HARI SEBELUMNYA (KALENDER DI ATAS):
   • Sama persis kaya Laporan Menu: panah mundur/
     maju + ketuk tanggalnya buka kalender + tombol
     cepat Hari Ini / Kemarin.
   • Pesanan lama yang terarsip tetap kehitung.
4. VERSI NAIK:
   • Versi app jadi v2.14 (footer bawah + kartu
     Pengaturan). Cache sw.js jadi miapos-v2.14-r1.
   • Server ikut nambah: api/sync.js (Vercel) &
     main.py v2.14 (Termux) — dua-duanya harus di-
     update barengan biar sinkron jalan.
   • Ingat aturannya: tiap update versi SELALU naik.

================================================
  CATATAN v2.13 (rilis sebelumnya) — AKUN ANTAR HP ·
     CATATAN PER MENU · 2 BAHASA · 4 TEMA
================================================
1. CATATAN BUAT DAPUR BISA DIISI PER MENU:
   • Dulu catatan dapur cuma 1 buat seluruh pesanan
     (yang di bagian bawah keranjang). Sekarang DI
     BAWAH TIAP MENU yang udah masuk keranjang ada
     kolom catatan sendiri — contoh: "pedas, tanpa
     es" cuma buat Mie Ayam-nya doang.
   • Catatannya ikut kecetak di NOTA DAPUR (baris
     "cat: ..." di bawah nama menunya).
   • Ada di keranjang desktop & drawer keranjang HP.
   • PESANAN YANG UDH MASUK PUN BISA: buka detail
     pesanan → tiap menu ada kolom catatan (ikon
     pensil editor catatan lama tetap ada).
2. NOTA CETAKAN GAK KAPITAL-KAPITAL AMAT LAGI:
   • Dulu nota dapur nyetak nama menu HURUF KAPITAL
     SEMUA (contoh: 2 NASI GORENG SPESIAL) — makan
     tempat & susah dibaca. Sekarang huruf normal
     persis kaya nama di daftar menu (2 Nasi Goreng
     Spesial).
   • Berlaku untuk SEMUA nota: nota dapur & struk
     kasir sama-sama huruf normal. Hemat kertas 😄
3. TOMBOL CETAK DI LAYAR "SUDAH BAYAR" JADI 2:
   • Kejadian belinya: pembeli habis pesen langsung
     bayar. Dulu pas udah bayar cuma ada 1 tombol
     cetak struk (buat kasir). Sekarang jadi 2:
     - CETAK DAPUR → nota dapur langsung kecetak,
       dapur bisa mulai masak.
     - STRUK KASIR → bukti bayar buat pembeli.
4. BAHASA BAKU + TOMBOL 2 BAHASA (Indonesia/English):
   • Tulisan di aplikasi dirapikan pake bahasa baku
     (contoh: "cth:" jadi "contoh:", "Belum pilih
     meja" jadi "Meja belum dipilih", "item kecetak"
     jadi "item tercetak", dsb).
   • Pengaturan → Aplikasi → BAHASA: pilih Indonesia
     atau English — tersimpan otomatis. Fitur utama
     (kasir, pesanan, pembayaran, pengaturan) ikut
     keganti bahasanya; layar panduan dalam tetap
     Indonesia.
5. TEMA WARNA: ROYAL ORANGE DIPERBAIKI + PINK & PUTIH:
   • Bug: tema "Royal & Orange" ternyata warna
     utamanya BIRU (masa iya biru namanya orange 😅).
     Udah dibenerin — sekarang beneran ORANYE, dari
     header sampai tombol bayar.
   • Tema BARU: "Pink & Putih" — aksen pink di atas
     latar terang.
   • Total jadi 4 tema: Emerald & Slate, Royal &
     Orange, Pink & Putih, Charcoal Dark.
6. AKUN & QR ANTAR HP (DASAR SINKRON — DILENGKAP DI v2.14):
   • Sekarang ada AKUN: Pengaturan → bagian AKUN
     (paling atas). Daftar dulu: nama lengkap, no.
     handphone, nama usaha, alamat, kata sandi —
     bentuk form-nya kaya layar "Ubah Akun" yang
     kamu tunjukin di pict.
   • TIAP HP YANG MASUK AKUN YANG SAMA, SEMUA DATA
     IKUT: menu, pesanan, omzet, stok, laporan.
     Caranya ada 2 tombol di header kartu akun:
     - TAMPILKAN QR AKUN → muncul QR berisi akun
       (+ data usaha kalau muat). Di HP lain tinggal
       PINDAI QR AKUN → muncul popup info akun
       (nama, no HP, nama usaha, alamat lengkap) →
       "Masuk dengan Akun Ini" → semua data langsung
       ke-load di HP itu. Sekali scan, beres.
     - Kalau datanya kebesaran buat QR (pesanan
       sudah banyak), QR tetap jalan buat akunnya,
       dan muncul "Kode Data Lengkap" — salin kodenya,
       kirim lewat WhatsApp ke HP lain, tempel di
       menu Pindai QR Akun → masuk, data ikut semua.
   • Belum ada akun di HP itu? Tinggal daftar di
     situ (tab Daftar), atau pakai QR dari HP utama.
   • Salah akun? Ada tombol KELUAR (log out) — data
     akun tetap tersimpan aman, masuk lagi langsung
     ke-load lagi. Bisa juga UBAH AKUN (ganti nama,
     nomor, kata sandi).
   • Data disimpan PER AKUN di tiap HP + snapshot
     otomatis, jadi aman walau ganti-ganti akun.
   • Catatan jujur: sinkronnya lewat QR/kode (100%
     offline, tanpa server). Bukan real-time antar
     HP — tapi sekali pindah, datanya utuh semua.
     (UPDATE v2.14: kini udah ada sinkron otomatis
     real-time via server — baca catatan v2.14 di
     paling atas!)
     Kalau nanti mau real-time via cloud, tinggal
     bilang, butuh server sendiri.
7. VERSI NAIK:
   • Versi app jadi v2.13 (sidebar + kartu bawah
     Pengaturan). Cache sw.js jadi miapos-v2.13-r1.
   • Ingat aturannya: tiap update versi SELALU naik.

================================================
  CATATAN v2.12 (rilis sebelumnya) — RESET DATA PAKAI
     KONFIRMASI 5 DETIK + README.md BARU
================================================

APA YANG BARU DI v2.12 (reset anti ke pencet + README GitHub)
------------------------------------------------------------
1. RESET DATA SEKARANG WAJIB KONFIRMASI + JEDA 5 DETIK:
   • Kejadian dulu: tombol Reset Data di Pengaturan
     DIPENCET GAK SENGAJA pas naruh HP → semua menu
     yang udah diinput ilang seketika. Sakit hati 😭
   • Sekarang: klik Reset Data → muncul popup
     "Yakin Reset Data?" — ada peringatan jelas:
     semua menu/pesanan/stok balik ke data awal &
     GAK BISA DIKEMBALIKAN.
   • Tombol merah "Ya, Reset Data" TERKUNCI 5 DETIK
     (tampil "Tunggu 5 detik…" terus menghitung
     mundur). Abis 5 detik baru bisa diklik. Jadi
     kalau gak sengaja kepencet, masih sempat nekankan
     BATAL — datamu aman.
   • Tombol Batal selalu aktif — nutup tanpa ngapa-
     ngapain.
   • Bonus: ikon reset (panah muter) di Topbar versi
     desktop/web — yang tadinya LANGSUNG ngereset
     tanpa tanya — sekarang pakai popup & jeda yang
     sama. Gak ada lagi jalur reset langsung.
   • Tombol merah "Hapus Semua Data Lokal" emang udah
     ada dialog konfirmasi bawaan dari dulu — tetap.
2. README.md BARU BUAT HALAMAN GITHUB:
   • Halaman depan repo sekarang ada README.md yang
     rapih & enak dibaca: ada emoji, badge versi,
     penjelasan fitur per seksi, cara pakai, struktur
     file, teknologi & riwayat versi singkat.
   • README.txt tetap ada — jadi catatan lengkap
     per versi (file ini).
3. VERSI NAIK:
   • Versi app jadi v2.12 (sidebar + kartu bawah
     Pengaturan). Cache sw.js jadi miapos-v2.12-r1.
   • Ingat aturannya: tiap update versi SELALU naik.

================================================
  CATATAN v2.11 (rilis sebelumnya)
================================================

APA YANG BARU DI v2.11 (fix tulisan bawah kepotong)
------------------------------------------------------------
1. FIX TULISAN BAWAH KEPOTONG:
   • Keluhannya: di layar Pengaturan, tulisan versi
     "Miapos F&B Suite v2.x · Python + C++ Engine" di
     kartu paling bawah KEPOTONG — ada yang ketutupan
     navigation bar bawah (Home/Pesanan/+/Lapor/Set).
   • Penyebabnya (ADA 2):
     1) Layar (main) pakai min-height:100% — jadi tinggi
        layarnya 100% LAYAR + numpuk di bawah header.
        Akibatnya ~100px bagian bawah layar NEMBUS ke
        luar batas app yang tersembunyi (overflow
        hidden) — bagian itu GAK BISA kegulung, alias
        hilang selamanya di balik navbar.
     2) Ruang gulung bawah cuma 96px — lebih kecil dari
        tinggi navbar di HP yang punya garis gestur/
        safe-area gedhe.
   • Perbaikannya:
     1) min-height layar dicabut (min-h-0) di SEMUA 13
        layar — sekarang tinggi layar pas sampai dasar
        HP, gak ada lagi bagian yang nembus & hilang.
     2) Ruang bawah tiap layar digedein 96px → 160px
        biar aman juga di HP yang navbar-nya tinggi.
     Sekarang digulung sampai habis → kartu paling
     bawah KELIHATAN SEMUA, gak ada lagi yang kepotong.
2. VERSI NAIK TERUS:
   • Dari v2.11 ini, SETIAP update berikutnya versi
     selalu nambah: v2.12, v2.13, dst. Nama cache di
     sw.js juga ganti tiap rilis (miapos-v2.11-r1)
     biar PWA lama otomatis ke-refresh ke versi baru.

================================================
  CATATAN v2.10 (rilis sebelumnya)
================================================

APA YANG BARU DI v2.10 (scan barcode + laporan menu + QRIS + cetak tambahan)
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
4. FITUR NOTIFIKASI DICABUT TOTAL (revisi v2.10):
   • Semua yang berbau notif DIHAPUS dari app: popup izin,
     banner dashboard, saklar & tombol tes, seksi notif di
     Owner Zone, push server + cron, sampai file api/push-*.
     Alasannya simpel: permintaan owner — "hapus aja deh".
   • Akibatnya app jalan BERSIH: buka app gak ada popup
     izin nanya-nanya, gak ada banner, kasir fokus jualan.
   • File yang ikut dihapus dari zip: PANDUAN-NOTIF.txt,
     api/push-subscribe.js, api/push-send.js, api/_pushlib.js.
     vercel.json & package.json dikosongin (cron + web-push
     ikut dicabut). Kalau di repo masih ada sisa file itu,
     hapus manual biar bersih.
5. FIX BUG LAYAR PUTIH:
   • Stok & Bahan → tab Produk kadang blank putih (data
     lama/backup tanpa varian) — sudah dibaliki lapis
     normalisasi otomatis. Gak blank lagi.
6. OWNER ZONE MAKIN RAPIH:
   • Isinya sekarang SEKSI GULUNG: QRIS / Keamanan — klik
     baru layarnya kebuka, gak numpuk
     panjang ke bawah. (Setelan teks kartu cuaca DIHAPUS —
     teksnya sekarang diatur app sendiri.)
   • Kartu cuaca NAIK ke paling atas Dashboard (di atas
     4 kotak ringkasan) — sesuai permintaan.
7. TEKS KARTU CUACA RANDOM (BARU — permintaan owner):
   • Salam di kartu cuaca sekarang RANDOM: "Selamat malam,
     Trinda!" diikuti kalimat santai yang ganti sendiri —
     tiap app dibuka beda + diacak ulang tiap 5 menit
     (10 kalimat per waktu: pagi/siang/sore/malam).
   • Isinya dikontrol app: kalimat kenyamanan buat kasir
     (semangat, jam makan, rehat) — TANPA kata teknis kaya
     "data aman semua" yang bikin kasir bingung.
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
13. FIX KARTU CUACA NYASAR WAKTU (revisi v2.10):
   • Bug: pas MALEM gambarnya masih matahari ☀️ + salam
     masih "Selamat siang". Penyebab: emoji cuaca gak
     kenal siang/malem, dan pas HP diemin/dibungkus
     app-nya Android ngebekuin timer — jam gak dihitung
     ulang pas app dibuka lagi.
   • Fix: emoji cuaca ikut jam — malem hari langit cerah
     tampil BULAN 🌙 (hujan/kabut tetap). Salam dihitung
     ulang tiap menit + tiap app dibuka lagi, jadi gak
     nyasar lagi. Kalimat random juga ikut ganti pool
     (malem gak muncul kalimat "makan siang" lagi).
14. WIDGET JAM LIVE DI KARTU CUACA (baru):
   • Di dalam kartu cuaca ada jam berdetik: HH:MM:SS
     (angka besar) + tanggal kecil di bawahnya + ikon
     siang/malem.
   • Warnanya ikut suasana: siang gradasi jingga,
     malem gradasi indigo gelap. Tetap di kartu cuaca,
     posisi kartu tetap paling atas (di atas 4 kotak).
15. LAPORAN MENU PUNYA TANGGALAN (baru):
   • Di atas laporan ada navigator tanggal: panah kiri/
     kanan buat geser hari, ketuk label buat buka
     kalender, plus tombol cepat "Hari Ini" & "Kemarin".
   • Buat intip KEMARIN kejual apa aja — buat nyiapin
     stok besok (dapur gak perlu nanya "ayam/bebek
     kejual berapa" satu-satu lagi).
   • Pesanan yang udah masuk arsip tetap kebaca, jadi
     tanggal berapa pun masih ada laporannya.
16. KATEGORI "DESSERT" JADI "SAMBAL" (revisi v2.10):
   • Kategori bawaan Dessert diganti Sambal 🌶️ — menu
     yang tadinya di Dessert otomatis ikut pindah
     (label aja yang ganti, datanya aman).
17. KATEGORI SEKARANG BISA DIHAPUS SEMUA (revisi):
   • Dulu cuma kategori buatan sendiri yang bisa
     dihapus. Sekarang kategori bawaan juga (Minuman,
     Sambal, Camilan) — buat koreksi salah input.
   • Semua menu di kategori yang dihapus otomatis
     pindah ke Makanan. Kategori Makanan sendiri gak
     bisa dihapus (dia jangkarnya).
18. SCAN QR DIGEDEIN + QR MENU AUTO-ISI (revisi):
   • Kotak scan digedein & dibikin PERSEGI — pas buat
     QR (QR bukan kode unik produk, butuh kotak gede
   biar kebaca semua).
   • QR menu format MIAPOS|Nama|Harga|Kategori →
     sekali scan menu LANGSUNG masuk lengkap +
     kesortir di kategorinya, tanpa ngetik. Kategori
     belum ada? Otomatis dibikinin.
   • Kamera dibikin kotak (1:1) biar QR gede muat.
19. PANDUAN-SCAN.txt (BARU — ada di dalam zip):
   • Panduan lengkap cara input menu yang BANYAK
     lewat QR: format QR, cara bikin QR massal dari
     Google Sheets (gratis, 1 formula), tips print,
     cara scan, plus aturan bikin/hapus kategori.
20. IMPORT QR MASSAL — 1 QR BERISI BANYAK MENU (revisi 2):
   • Menu lu 50-100-an? Gak perlu scan satu-satu
     lagi. Bikin SATU QR yang isinya daftar semua
     menu → scan sekali → SEMUA masuk sekaligus +
     kesortir kategori otomatis.
   • Format yang kebaca: multi-baris MIAPOS (1 menu
     tiap baris), tabel/CSV (koma/;/|/tab), atau
     JSON. Harga lentur: 27000 / 27.000 / 27,000 /
     Rp27.000 / 27rb semua kebaca bener.
   • Datanya kepanjangan buat 1 QR (±2.900 huruf)?
     Pecah 2-3 QR → scan berurutan → otomatis
     NGGABUNG, terakhir tinggal tekan IMPORT SEMUA.
   • Panel preview ungu: daftar menu yang kebaca,
     duplikat ditandai ⚠️ & ditolak, kategori baru
     dibikinin otomatis (lengkap sama emoji).
   • Gak bisa scan? Ada fallback TEMPES TEKS di
     layar scan — tempel daftar menunya, hasilnya
     persis sama.
   • Panduan lengkapnya: PANDUAN-SCAN.txt BAGIAN 6.

APA YANG BARU DI v2.9 (notif jadwal buka/tutup + Owner Zone + checklist 6/6)
------------------------------------------------------------
   (CATATAN v2.10 revisi: seluruh fitur notifikasi dari
    v2.9 SUDAH DIHAPUS — lihat seksi 4 di atas. Sisanya —
    Owner Zone, tema, backup cloud — tetap jalan normal.)
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
   (CATATAN v2.10 revisi: notifikasi salam pagi ikut dicabut;
    kartu cuaca tetap ada + teks salamnya sekarang random.)
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

SELAMAT PAKAI! — Miapos v2.15
