# miamotion App v2.0.0 🚀

Dashboard aktivasi dengan **live stats** (bar chart 7 hari + donut success rate + feed real-time), desain **neon cyber**, plus:

- 🐍 **Server Python** — serve dashboard, proxy API (key aman server-side), catat stats
- ⚙️ **Launcher C++** — `g++ -O2 -std=c++17 -o launch launcher.cpp && ./launch`
- 🔄 **Auto-update** — push ke GitHub → semua device update sendiri tiap 5 menit
- 📱 **Termux / PWA** — jadi aplikasi Android via localhost
- 🔒 **API tetap aman** — mode `proxy` (serverless kamu) atau `local` (`server/api_handler.py`)

## Quick Start

```bash
pip install -r server/requirements.txt
bash run.sh          # Windows: run.bat
# buka http://localhost:8080
```

Setup auto-update: edit `config/config.json` → `"repo": "USERNAME/NAMA-REPO"`

**Panduan lengkap (GitHub, Termux, keamanan API, troubleshooting): 👉 [PANDUAN.md](PANDUAN.md)**
