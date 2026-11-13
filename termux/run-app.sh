#!/data/data/com.termux/files/usr/bin/bash
# miamotion app - launcher khusus Termux (dipakai Termux:Widget / Termux:Boot)
# Copy file ini ke ~/.shortcuts/ (Widget) atau ~/.termux/boot/ (autostart)

DIR="$(cd "$(dirname "$0")" && pwd)"
# kalau dijalankan dari ~/.shortcuts atau ~/.termux/boot, arahkan ke folder app:
if [ ! -f "$DIR/server/app.py" ]; then
  DIR="$HOME/miamotion-app"
fi
cd "$DIR" || exit 1

# biar layar tetap nyala / server tetap hidup saat app di background
command -v termux-wake-lock >/dev/null 2>&1 && termux-wake-lock

PY="$(command -v python3 || command -v python)"
"$PY" server/updater.py --once
exec "$PY" server/app.py
