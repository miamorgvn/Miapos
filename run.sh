#!/usr/bin/env bash
# miamotion app - run di Linux / macOS / Termux
# usage: bash run.sh
cd "$(dirname "$0")" || exit 1
PY="$(command -v python3 || command -v python)"
if [ -z "$PY" ]; then
  echo "[x] Python tidak ditemukan. Termux: pkg install python"
  exit 1
fi
"$PY" server/updater.py --once
exec "$PY" server/app.py
