#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
==============================================
  MIAPOS SERVER — Python + C++ Engine (Termux)
==============================================
Jalankan file ini di Termux untuk menjadikan
Miapos sebagai aplikasi lokal di HP kamu.

Di dalamnya sudah tersisip:
  • Python  -> server lokal + API + auto-backup data
  • C++     -> native analytics engine (engine/miapos_engine)
               untuk menghitung tren & prediksi penjualan

Cara pakai:
  python main.py            -> server jalan + buka browser
  python main.py --port 9000-> pakai port lain
  python main.py --no-open  -> jangan buka browser otomatis
  python main.py --lan      -> tampilkan alamat IP lokal
  python main.py --help     -> bantuan
"""

import argparse
import glob
import json
import os
import socket
import subprocess
import sys
import time
import webbrowser
from datetime import datetime
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer

# ---------- Konfigurasi ----------
DEFAULT_PORT = 8080
HTML_FILE = "index.html"  # fallback ke miapos.html kalau index tidak ada
BACKUP_DIR = "backup"
ENGINE_SRC = os.path.join("engine", "miapos_engine.cpp")
ENGINE_BIN = os.path.join("engine", "miapos_engine")
MAX_BACKUPS = 30          # simpan maksimal 30 backup terakhir
MAX_BODY = 15 * 1024 * 1024  # batas ukuran request 15 MB
SYNC_DIR = "sync"         # v2.14: folder data sinkron antar HP (per akun)

# Warna terminal (ANSI)
class C:
    GREEN = "\033[92m"
    CYAN = "\033[96m"
    YELLOW = "\033[93m"
    DIM = "\033[90m"
    BOLD = "\033[1m"
    END = "\033[0m"


def find_free_port(start):
    """Cari port yang masih kosong mulai dari `start`."""
    port = start
    while port < start + 50:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            try:
                s.bind(("127.0.0.1", port))
                return port
            except OSError:
                port += 1
    raise RuntimeError("Tidak ada port kosong ditemukan.")


def get_lan_ips():
    """Ambil alamat IP lokal (WiFi/hotspot) supaya bisa dibuka dari device lain."""
    ips = set()
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.connect(("8.8.8.8", 80))
            ips.add(s.getsockname()[0])
    except OSError:
        pass
    try:
        for info in socket.getaddrinfo(socket.gethostname(), None):
            ip = info[4][0]
            if "." in ip and not ip.startswith("127."):
                ips.add(ip)
    except OSError:
        pass
    return sorted(ips)


def open_browser(url):
    """Buka URL: coba termux-open-url / termux-open dulu, lalu fallback webbrowser."""
    for cmd in (["termux-open-url", url], ["termux-open", url]):
        try:
            subprocess.Popen(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            return "termux-open"
        except FileNotFoundError:
            continue
    try:
        webbrowser.open(url)
        return "webbrowser"
    except Exception:
        return None


# ============================================================
#  C++ NATIVE ENGINE — deteksi, kompilasi ulang, dan eksekusi
# ============================================================

def try_compile_engine():
    """Coba compile ulang engine C++ kalau source ada tapi binary belum ada."""
    if os.path.exists(ENGINE_BIN):
        return True, "binary sudah ada"
    if not os.path.exists(ENGINE_SRC):
        return False, "source tidak ada"
    for compiler in ("g++", "clang++"):
        if not _which(compiler):
            continue
        try:
            r = subprocess.run(
                [compiler, "-std=c++17", "-O2", "-o", ENGINE_BIN, ENGINE_SRC],
                capture_output=True, timeout=60,
            )
            if r.returncode == 0:
                return True, f"dicompile ulang dengan {compiler}"
        except Exception:
            continue
    return False, "compiler C++ tidak ditemukan (jalankan: pkg install clang)"


def _which(name):
    from shutil import which
    return which(name)


def cpp_engine_available():
    return os.path.exists(ENGINE_BIN) and os.access(ENGINE_BIN, os.X_OK)


def run_cpp_stats(lines):
    """Jalankan binary C++: input baris 'ts amount', output 'total|days|...|trend'."""
    payload = "".join(f"{ts} {amt}\n" for ts, amt in lines)
    r = subprocess.run(
        [os.path.abspath(ENGINE_BIN)],
        input=payload.encode(), capture_output=True, timeout=10,
    )
    if r.returncode != 0:
        raise RuntimeError(r.stderr.decode(errors="replace")[:200])
    out = r.stdout.decode().strip()
    parts = out.split("|")
    if len(parts) != 9:
        raise RuntimeError("output engine tidak valid")
    names = ["total", "days", "avg", "growthPct", "movAvg7",
             "bestTs", "bestAmount", "forecast", "trend"]
    vals = [float(p) for p in parts[:8]] + [parts[8]]
    return dict(zip(names, vals))


def python_stats_fallback(lines):
    """Versi murni Python — dipakai kalau binary C++ tidak tersedia."""
    days = [(float(ts), float(amt)) for ts, amt in lines]
    n = len(days)
    if n == 0:
        return {"total": 0, "days": 0, "avg": 0, "growthPct": 0, "movAvg7": 0,
                "bestTs": 0, "bestAmount": 0, "forecast": 0, "trend": "KOSONG"}
    total = sum(a for _, a in days)
    avg = total / n
    last7 = [a for _, a in days[-7:]]
    last7_avg = sum(last7) / len(last7)
    prev = [a for _, a in days[-14:-7]]
    prev7_avg = (sum(prev) / len(prev)) if prev else 0.0
    growth = ((last7_avg - prev7_avg) / prev7_avg * 100.0) if prev7_avg > 0 else 0.0
    best_ts, best_amt = max(days, key=lambda x: x[1])
    forecast = max(0.0, 0.7 * last7_avg + 0.3 * avg)
    trend = "NAIK" if growth > 5 else ("TURUN" if growth < -5 else "STABIL")
    return {"total": total, "days": n, "avg": avg, "growthPct": growth,
            "movAvg7": last7_avg, "bestTs": best_ts, "bestAmount": best_amt,
            "forecast": forecast, "trend": trend}


def save_backup(data):
    """Simpan JSON data aplikasi ke folder backup/ dengan nama ber-stempel waktu."""
    os.makedirs(BACKUP_DIR, exist_ok=True)
    stamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    path = os.path.join(BACKUP_DIR, f"miapos-backup-{stamp}.json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False)
    # buang backup paling lama kalau sudah melebihi batas
    olds = sorted(glob.glob(os.path.join(BACKUP_DIR, "miapos-backup-*.json")))
    while len(olds) > MAX_BACKUPS:
        os.remove(olds.pop(0))
    return path


def list_backups():
    os.makedirs(BACKUP_DIR, exist_ok=True)
    out = []
    for p in sorted(glob.glob(os.path.join(BACKUP_DIR, "miapos-backup-*.json")), reverse=True):
        st = os.stat(p)
        out.append({
            "file": os.path.basename(p),
            "size": st.st_size,
            "time": datetime.fromtimestamp(st.st_mtime).strftime("%d %b %Y %H:%M"),
        })
    return out


# ---------- v2.14: SINKRON OTOMATIS ANTAR HP (per akun) ----------
def sync_file(acc):
    """acc (no. HP) -> path file sync/acc-<noHP>.json. None kalau tak valid."""
    digits = "".join(ch for ch in str(acc or "") if ch.isdigit())[:20]
    if len(digits) < 8:
        return None
    os.makedirs(SYNC_DIR, exist_ok=True)
    return os.path.join(SYNC_DIR, f"acc-{digits}.json")


def sync_sha(path):
    """Token revisi sederhana dari mtime+size — untuk deteksi 'unchanged'."""
    st = os.stat(path)
    return f"{st.st_mtime_ns:x}-{st.st_size:x}"


def load_sync(acc):
    path = sync_file(acc)
    if not path or not os.path.exists(path):
        return None, None
    with open(path, encoding="utf-8") as f:
        return json.load(f), sync_sha(path)


def save_sync(acc, payload):
    path = sync_file(acc)
    if not path:
        raise ValueError("nomor akun tidak valid")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False)
    return sync_sha(path)


class MiaposHandler(SimpleHTTPRequestHandler):
    """Handler HTTP: file statis + API lokal (backup & analytics)."""

    server_version = "MiaposServer/2.14"

    # ---------- helper JSON ----------
    def _json(self, obj, code=200):
        body = json.dumps(obj).encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(body)

    def _read_json(self):
        length = int(self.headers.get("Content-Length") or 0)
        if length <= 0 or length > MAX_BODY:
            raise ValueError("ukuran request tidak valid")
        raw = self.rfile.read(length)
        return json.loads(raw.decode("utf-8"))

    # ---------- v2.14: sinkron antar HP (GET = tarik) ----------
    def _query(self):
        from urllib.parse import parse_qs
        try:
            q = self.path.split("?", 1)[1] if "?" in self.path else ""
            return {k: v[0] for k, v in parse_qs(q).items()}
        except Exception:
            return {}

    def _api_sync_get(self):
        q = self._query()
        data, sha = load_sync(q.get("acc", ""))
        if data is None:
            self._json({"ok": False, "error": "AKUN_BELUM_ADA_DI_CLOUD"}, 404)
            return
        if q.get("rev") and q["rev"] == sha:
            self._json({"ok": True, "unchanged": True, "sha": sha})
            return
        self._json({"ok": True, "data": data, "sha": sha,
                    "updatedAt": (data or {}).get("updatedAt", "")})

    def _api_sync_put(self):
        q = self._query()
        body = self._read_json()
        if not isinstance(body, dict) or not body.get("store") or not isinstance(body.get("acc"), dict):
            self._json({"ok": False, "error": "DATA_TIDAK_VALID"}, 400)
            return
        import time as _t
        payload = {
            "v": 2,
            "acc": body["acc"],
            "store": body["store"],
            "deviceId": str(body.get("deviceId", ""))[:40],
            "updatedAt": datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z",
        }
        sha = save_sync(q.get("acc", ""), payload)
        self._json({"ok": True, "sha": sha, "updatedAt": payload["updatedAt"]})

    def _api_sync_delete(self):
        q = self._query()
        path = sync_file(q.get("acc", ""))
        if path and os.path.exists(path):
            os.remove(path)
        self._json({"ok": True, "deleted": True})

    # ---------- GET ----------
    def do_GET(self):
        path = self.path.split("?")[0]
        if path == "/api/ping":
            cpp = cpp_engine_available()
            self._json({
                "ok": True, "app": "miapos", "server": "python",
                "version": "2.14", "cppEngine": cpp, "sync": True,
                "time": datetime.now().strftime("%H:%M:%S"),
            })
            return
        if path == "/api/backups":
            try:
                self._json({"ok": True, "backups": list_backups()})
            except Exception as e:
                self._json({"ok": False, "error": str(e)}, 500)
            return
        if path == "/api/sync":
            try:
                self._api_sync_get()
            except Exception as e:
                self._json({"ok": False, "error": str(e)}, 500)
            return
        super().do_GET()

    # ---------- PUT (v2.14: sinkron antar HP = kirim) ----------
    def do_PUT(self):
        path = self.path.split("?")[0]
        try:
            if path == "/api/sync":
                self._api_sync_put()
                return
            self._json({"ok": False, "error": "endpoint tidak dikenal"}, 404)
        except (ValueError, json.JSONDecodeError) as e:
            self._json({"ok": False, "error": f"JSON tidak valid: {e}"}, 400)
        except Exception as e:
            self._json({"ok": False, "error": str(e)}, 500)

    # ---------- DELETE (v2.14: hapus data sinkron akun) ----------
    def do_DELETE(self):
        path = self.path.split("?")[0]
        try:
            if path == "/api/sync":
                self._api_sync_delete()
                return
            self._json({"ok": False, "error": "endpoint tidak dikenal"}, 404)
        except Exception as e:
            self._json({"ok": False, "error": str(e)}, 500)

    # ---------- POST ----------
    def do_POST(self):
        path = self.path.split("?")[0]
        try:
            if path == "/api/backup":
                data = self._read_json()
                path_saved = save_backup(data)
                print(f"{C.DIM}[miapos]{C.END} 💾 backup tersimpan: {path_saved}")
                self._json({"ok": True, "file": os.path.basename(path_saved),
                            "total": len(list_backups())})
                return
            if path == "/api/stats":
                body = self._read_json()
                daily = body.get("daily") or []
                lines = [(int(d.get("ts", 0)), float(d.get("amount", 0))) for d in daily]
                t0 = time.time()
                use_cpp = cpp_engine_available()
                try:
                    stats = run_cpp_stats(lines) if use_cpp else python_stats_fallback(lines)
                    engine = "cpp" if use_cpp else "python"
                except Exception:
                    stats = python_stats_fallback(lines)
                    engine = "python-fallback"
                stats["engine"] = engine
                stats["computeMs"] = round((time.time() - t0) * 1000, 2)
                self._json({"ok": True, "stats": stats})
                return
            self._json({"ok": False, "error": "endpoint tidak dikenal"}, 404)
        except (ValueError, json.JSONDecodeError) as e:
            self._json({"ok": False, "error": f"JSON tidak valid: {e}"}, 400)
        except Exception as e:
            self._json({"ok": False, "error": str(e)}, 500)

    # ---------- file statis ----------
    def end_headers(self):
        if self.path.endswith(".html") or self.path == "/":
            self.send_header("Cache-Control", "no-cache, no-store, must-revalidate")
            self.send_header("Pragma", "no-cache")
            self.send_header("Expires", "0")
        super().end_headers()

    def log_message(self, fmt, *args):
        # Log ringkas & berwarna
        sys.stdout.write(f"{C.DIM}[miapos]{C.END} {fmt % args}\n")


def main():
    parser = argparse.ArgumentParser(description="Miapos Server untuk Termux")
    parser.add_argument("--port", type=int, default=DEFAULT_PORT, help="Port server (default 8080)")
    parser.add_argument("--no-open", action="store_true", help="Jangan buka browser otomatis")
    parser.add_argument("--lan", action="store_true", help="Tampilkan alamat IP LAN juga")
    args = parser.parse_args()

    # Pastikan file aplikasi ada di sebelah file ini (utamakan index.html)
    global HTML_FILE
    base_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(base_dir)
    if not os.path.exists(HTML_FILE) and os.path.exists("miapos.html"):
        HTML_FILE = "miapos.html"
    if not os.path.exists(HTML_FILE):
        print(f"{C.YELLOW}⚠ index.html / miapos.html tidak ditemukan di folder ini!{C.END}")
        print(f"{C.DIM}  Taruh main.py satu folder dengan index.html.{C.END}")
        sys.exit(1)

    # Cek / compile C++ engine
    ok, note = try_compile_engine()
    cpp_ready = ok and cpp_engine_available()

    port = find_free_port(args.port)
    url = f"http://localhost:{port}/{HTML_FILE}"

    server = ThreadingHTTPServer(("0.0.0.0", port), MiaposHandler)
    server.daemon_threads = True

    print()
    print(f"{C.BOLD}  ╔══════════════════════════════════════════╗{C.END}")
    print(f"{C.BOLD}  ║   🍴  M I A P O S  ·  S E R V E R        ║{C.END}")
    print(f"{C.BOLD}  ╚══════════════════════════════════════════╝{C.END}")
    print()
    print(f"  {C.GREEN}● Server berjalan!{C.END}")
    print(f"  {C.CYAN}➜ Aplikasi:{C.END} {C.BOLD}{url}{C.END}")
    if args.lan:
        for ip in get_lan_ips():
            print(f"  {C.CYAN}➜ Perangkat lain (WiFi sama):{C.END} http://{ip}:{port}/{HTML_FILE}")
    print()
    print(f"  {C.BOLD}Mesin terpasang:{C.END}")
    print(f"  {C.GREEN}● Python{C.END}  v{sys.version.split()[0]} — server + API + auto-backup")
    if cpp_ready:
        print(f"  {C.GREEN}● C++ Engine{C.END} — AKTIF (native analytics) {C.DIM}[{note}]{C.END}")
    else:
        print(f"  {C.YELLOW}● C++ Engine{C.END} — tidak aktif, pakai fallback Python {C.DIM}[{note}]{C.END}")
    print()
    print(f"  {C.DIM}Tips: buka link di Chrome lalu pilih 'Tambahkan ke'{C.END}")
    print(f"  {C.DIM}'Layar utama' supaya jadi aplikasi fullscreen.{C.END}")
    print(f"  {C.DIM}Tekan Ctrl+C untuk berhenti.{C.END}")
    print()

    if not args.no_open:
        how = open_browser(url)
        if how:
            print(f"  {C.DIM}Browser dibuka via {how}...{C.END}")
        else:
            print(f"  {C.YELLOW}Tidak bisa buka browser otomatis. Buka manual: {url}{C.END}")

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print()
        print(f"  {C.YELLOW}Server dihentikan. Sampai jumpa! 👋{C.END}")
        server.server_close()


if __name__ == "__main__":
    main()
