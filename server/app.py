#!/usr/bin/env python3
"""
miamotion app server
====================
Serve the dashboard on localhost + keep the API safe (server-side).

Endpoints:
  GET  /                 -> dashboard (index.html)
  GET  /<file>           -> static files (css/js/icons/manifest/...)
  POST /api/activate     -> activation API:
        - api_mode = "proxy": forward the request to upstream_api_url
          (your existing serverless API). Keys stay on the server.
        - api_mode = "local": run server/api_handler.py (fully offline)
  GET  /api/stats        -> live execution statistics (used by the dashboard chart)
  POST /api/stats/reset  -> clear statistics
  GET  /api/version      -> current version + repo info (used by auto-update watcher)

Auto-update: a background thread calls server/updater.py every
`update_interval_sec` seconds (default 300 = 5 minutes).
"""

import json
import sys
import threading
import time
from datetime import datetime
from pathlib import Path

from flask import Flask, jsonify, request, send_from_directory

ROOT = Path(__file__).resolve().parent.parent
SRV = Path(__file__).resolve().parent
sys.path.insert(0, str(SRV))

import updater  # noqa: E402

CONFIG_PATH = ROOT / "config" / "config.json"
EXAMPLE_PATH = ROOT / "config" / "config.example.json"
DATA_DIR = SRV / "data"
STATS_PATH = DATA_DIR / "stats.json"
LOCK = threading.Lock()

DEFAULTS = {
    "port": 8080,
    "host": "0.0.0.0",
    "api_mode": "proxy",
    "upstream_api_url": "",
    "upstream_api_key": "",
    "repo": "",
    "branch": "main",
    "github_token": "",
    "update_interval_sec": 300,
    "auto_open_browser": False,
}


def load_config() -> dict:
    """Read config/config.json; auto-create it from the example on first run."""
    if not CONFIG_PATH.exists():
        try:
            CONFIG_PATH.parent.mkdir(parents=True, exist_ok=True)
            if EXAMPLE_PATH.exists():
                CONFIG_PATH.write_text(EXAMPLE_PATH.read_text(encoding="utf-8"), encoding="utf-8")
            else:
                CONFIG_PATH.write_text(json.dumps(DEFAULTS, indent=2), encoding="utf-8")
            print("[config] created config/config.json from example - edit it!", flush=True)
        except Exception as e:  # noqa: BLE001
            print(f"[config] WARNING: could not create config: {e}", flush=True)

    cfg = dict(DEFAULTS)
    try:
        raw = json.loads(CONFIG_PATH.read_text(encoding="utf-8"))
        cfg.update({k: v for k, v in raw.items() if not str(k).startswith("_")})
    except Exception as e:  # noqa: BLE001
        print(f"[config] WARNING: bad config.json ({e}) - using defaults", flush=True)
    return cfg


CFG = load_config()


# ---------------------------------------------------------------- stats
def ensure_stats() -> None:
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    if not STATS_PATH.exists():
        save_stats(blank_stats())


def blank_stats() -> dict:
    return {"days": {}, "totals": {"s": 0, "f": 0, "sent": 0}, "recent": []}


def load_stats() -> dict:
    try:
        st = json.loads(STATS_PATH.read_text(encoding="utf-8"))
        if "totals" not in st:
            raise ValueError("no totals")
        st.setdefault("days", {})
        st.setdefault("recent", [])
        return st
    except Exception:  # noqa: BLE001
        return blank_stats()


def save_stats(st: dict) -> None:
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    STATS_PATH.write_text(json.dumps(st, indent=1), encoding="utf-8")


def mask_email(e: str) -> str:
    if not e or "@" not in e:
        return (e or "")[:12]
    u, _, d = e.partition("@")
    return f"{(u or '*')[0]}***@{d}"


def record(ev: str, payload: dict) -> None:
    """ev = 'sent' | 'success' | 'fail'"""
    with LOCK:
        st = load_stats()
        day = datetime.now().strftime("%Y-%m-%d")
        d = st["days"].setdefault(day, {"s": 0, "f": 0, "sent": 0})
        if ev == "sent":
            d["sent"] += 1
            st["totals"]["sent"] += 1
        elif ev == "success":
            d["s"] += 1
            st["totals"]["s"] += 1
        else:
            d["f"] += 1
            st["totals"]["f"] += 1
        st["recent"].insert(0, {
            "t": datetime.now().isoformat(timespec="seconds"),
            "ev": ev,
            "platform": payload.get("platform", ""),
            "email": mask_email(payload.get("email", "")),
        })
        st["recent"] = st["recent"][:50]
        save_stats(st)


# ---------------------------------------------------------------- app
app = Flask(__name__, static_folder=None)


@app.get("/")
def index():
    return send_from_directory(str(ROOT), "index.html")


@app.get("/<path:p>")
def static_files(p):
    return send_from_directory(str(ROOT), p)


@app.post("/api/activate")
def activate():
    payload = request.get_json(silent=True) or {}
    step = payload.get("step")

    if CFG.get("api_mode") == "proxy":
        url = (CFG.get("upstream_api_url") or "").strip()
        if not url or "your-app.vercel.app" in url:  # placeholder from example config
            return jsonify({
                "success": False,
                "error": "API not configured yet. Edit config/config.json -> set upstream_api_url "
                         "to your real API URL (or set api_mode='local' and implement "
                         "server/api_handler.py). See PANDUAN.md section 6."
            }), 503
        import requests as rq
        headers = {"Content-Type": "application/json",
                   "User-Agent": "miamotion-app/2.0"}
        key = (CFG.get("upstream_api_key") or "").strip()
        if key:
            headers["x-api-key"] = key  # stays server-side, never reaches the browser
        try:
            resp = rq.post(url, json=payload, headers=headers, timeout=60)
        except Exception as e:  # noqa: BLE001
            record("fail", payload)
            return jsonify({"success": False, "error": f"Upstream unreachable: {e}"}), 502
        try:
            out = resp.json()
        except Exception:  # noqa: BLE001
            out = {"success": False, "error": f"Upstream returned HTTP {resp.status_code}"}
        ok = bool(out.get("success"))
        if step == "send":
            record("sent" if ok else "fail", payload)
        elif step == "verify":
            record("success" if ok else "fail", payload)
        return jsonify(out), resp.status_code

    # ---- local mode: run server/api_handler.py ----
    try:
        import api_handler  # noqa: E402
        result = api_handler.handle(payload)
        if not isinstance(result, dict):
            result = {"success": False, "error": "api_handler must return a dict"}
    except Exception as e:  # noqa: BLE001
        result = {"success": False, "error": f"api_handler error: {e}"}
    ok = bool(result.get("success"))
    if step == "send":
        record("sent" if ok else "fail", payload)
    elif step == "verify":
        record("success" if ok else "fail", payload)
    return jsonify(result)


@app.get("/api/stats")
def stats():
    with LOCK:
        st = load_stats()
    return jsonify({
        "ok": True,
        "stats": st,
        "updated_at": datetime.now().isoformat(timespec="seconds"),
    })


@app.post("/api/stats/reset")
def stats_reset():
    with LOCK:
        save_stats(blank_stats())
    return jsonify({"ok": True})


@app.get("/api/version")
def version():
    out = {
        "version": None,
        "repo": CFG.get("repo") or "",
        "interval": CFG.get("update_interval_sec"),
        "last_check": None,
    }
    vj = ROOT / "version.json"
    if vj.exists():
        try:
            out["version"] = json.loads(vj.read_text(encoding="utf-8")).get("version")
        except Exception:  # noqa: BLE001
            pass
    lu = DATA_DIR / "last_update.json"
    if lu.exists():
        try:
            out["last_check"] = json.loads(lu.read_text(encoding="utf-8")).get("time")
        except Exception:  # noqa: BLE001
            pass
    return jsonify(out)


# ---------------------------------------------------------------- background
def update_loop() -> None:
    interval = int(CFG.get("update_interval_sec") or 0)
    if interval <= 0:
        print("[update] auto-update disabled (update_interval_sec = 0)", flush=True)
        return
    while True:
        time.sleep(interval)
        try:
            updater.update_once(CFG, log=lambda m: print(f"[update] {m}", flush=True))
        except Exception as e:  # noqa: BLE001
            print(f"[update] error: {e}", flush=True)


def open_browser() -> None:
    time.sleep(1.2)
    try:
        import webbrowser
        webbrowser.open(f"http://127.0.0.1:{CFG.get('port')}")
    except Exception:  # noqa: BLE001
        pass


def main() -> None:
    ensure_stats()
    threading.Thread(target=update_loop, daemon=True).start()
    if CFG.get("auto_open_browser"):
        threading.Thread(target=open_browser, daemon=True).start()

    port = int(CFG.get("port") or 8080)
    host = CFG.get("host") or "0.0.0.0"
    bar = "=" * 46
    print(f"""
{bar}
  miamotion app  -  v2.0.0
{bar}
  Dashboard : http://localhost:{port}
  LAN       : http://0.0.0.0:{port}  (device lain di WiFi yang sama)
  API mode  : {CFG.get('api_mode')}
  Auto-upd  : {'ON (every ' + str(int(CFG.get('update_interval_sec') or 300) // 60) + ' min)' if int(CFG.get('update_interval_sec') or 0) > 0 else 'OFF'}
  Repo      : {CFG.get('repo') or '(not set - auto-update inactive)'}
{bar}
  Ctrl+C untuk stop
{bar}""", flush=True)
    app.run(host=host, port=port, debug=False, threaded=True)


if __name__ == "__main__":
    main()
