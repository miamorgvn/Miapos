#!/data/data/com.termux/files/usr/bin/bash
# ============================================
#  MIAPOS — Installer (cukup dijalankan SEKALI)
# ============================================
echo ""
echo "  ╔══════════════════════════════════════╗"
echo "  ║   🍴  MIAPOS INSTALLER (Termux)      ║"
echo "  ╚══════════════════════════════════════╝"
echo ""

# 1. Install Python (wajib)
echo "[1/3] Memasang Python..."
if command -v python >/dev/null 2>&1; then
    echo "  ✔ Python sudah terpasang: $(python --version 2>&1)"
else
    pkg install -y python || { echo "  ✘ Gagal install python. Cek koneksi internet."; exit 1; }
fi

# 2. Install compiler C++ (opsional — untuk native engine)
echo "[2/3] Menyiapkan C++ Engine (opsional)..."
COMPILER=""
if command -v clang++ >/dev/null 2>&1; then COMPILER="clang++";
elif command -v g++ >/dev/null 2>&1; then COMPILER="g++";
elif pkg install -y clang >/dev/null 2>&1 && command -v clang++ >/dev/null 2>&1; then COMPILER="clang++";
else echo "  ⚠ Tidak bisa install clang — app tetap jalan (analytics pakai mode Python)."; fi

if [ -n "$COMPILER" ] && [ -f engine/miapos_engine.cpp ]; then
    echo "  → Compile engine C++ dengan $COMPILER..."
    if $COMPILER -std=c++17 -O2 -o engine/miapos_engine engine/miapos_engine.cpp 2>/dev/null; then
        echo "  ✔ C++ Native Engine AKTIF (engine/miapos_engine)"
    else
        echo "  ⚠ Compile gagal — app tetap jalan (analytics pakai mode Python)."
    fi
else
    echo "  ⚠ Source engine tidak ditemukan — dilewati."
fi

# 3. Merapikan izin file
echo "[3/3] Merapikan izin file..."
chmod +x "$(dirname "$0")/main.py" 2>/dev/null
chmod +x "$(dirname "$0")/start.sh" 2>/dev/null
[ -f engine/miapos_engine ] && chmod +x engine/miapos_engine 2>/dev/null

echo ""
echo "  ✔ SELESAI! Cara menjalankan aplikasi:"
echo ""
echo "      cd $(dirname "$0")"
echo "      python main.py"
echo ""
echo "  Atau klik file start.sh lewat Termux:Widget."
echo ""
