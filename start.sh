#!/data/data/com.termux/files/usr/bin/bash
# ============================================
#  MIAPOS — Launcher 1-Klik (Termux:Widget)
# ============================================
# Salin file ini ke ~/.shortcuts/ supaya bisa
# dijalankan langsung dari layar utama HP
# lewat aplikasi Termux:Widget.
# ============================================
cd "$(dirname "$0")" || exit 1

# Jaga CPU tetap nyala saat aplikasi dipakai (opsional)
command -v termux-wake-lock >/dev/null 2>&1 && termux-wake-lock

python main.py

command -v termux-wake-unlock >/dev/null 2>&1 && termux-wake-unlock
