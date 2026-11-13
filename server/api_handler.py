"""
LOCAL API MODE  -  server/api_handler.py
========================================
Dipakai jika config/config.json -> "api_mode": "local".
Logika aktivasi dijalankan penuh di device ini (100% offline, tanpa serverless).

>>> Jangan commit key/secret apa pun ke repo. Simpan di config/config.json
>>> (file itu di-.gitignore) atau environment variable.

handle(payload) menerima payload dari dashboard:
    { "step": "send",   "email": "...", "platform": "Android" }
    { "step": "verify", "email": "...", "link": "https://..." }

dan HARUS mengembalikan dict:
    { "success": true/false, "data": {...opsional...}, "error": "..." }
"""

import json
import os
from pathlib import Path

CONFIG_PATH = Path(__file__).resolve().parent.parent / "config" / "config.json"


def _cfg(key: str, default: str = "") -> str:
    """Baca satu nilai dari config/config.json (file lokal, tidak ikut ke GitHub)."""
    try:
        data = json.loads(CONFIG_PATH.read_text(encoding="utf-8"))
        return str(data.get(key, default) or default)
    except Exception:  # noqa: BLE001
        return os.environ.get(key.upper(), default)


# ---------------------------------------------------------------------
# CONTOH STRUKTUR (ganti dengan logika API kamu yang asli).
# response dari kedua step harus bentuknya sama dengan yang diharapkan
# dashboard: { "success": bool, "data": { "order_id": "...", "message": "..." } }
#
# import requests
#
# def handle(payload):
#     step = payload.get("step")
#     if step == "send":
#         r = requests.post(
#             _cfg("MY_PROVIDER_URL"),
#             headers={"Authorization": "Bearer " + _cfg("MY_PROVIDER_KEY")},
#             json={"email": payload["email"], "platform": payload.get("platform")},
#             timeout=45,
#         )
#         j = r.json()
#         return {"success": True, "data": {"order_id": j["order_id"], "message": "Check your inbox"}}
#
#     if step == "verify":
#         link = payload.get("link", "")
#         # panggil endpoint verifikasi provider kamu di sini, contoh:
#         r = requests.post(_cfg("MY_VERIFY_URL"), json={"link": link}, timeout=45,
#                           headers={"Authorization": "Bearer " + _cfg("MY_PROVIDER_KEY")})
#         if r.ok:
#             return {"success": True, "data": {"message": "Account active"}}
#         return {"success": False, "error": "Provider rejected the link"}
#
#     return {"success": False, "error": "unknown step"}
# ---------------------------------------------------------------------


def handle(payload: dict) -> dict:
    step = payload.get("step")

    if step == "send":
        # TODO: ganti dengan logika pengiriman verifikasi kamu.
        return {
            "success": False,
            "error": "api_handler.py belum diisi. Buka server/api_handler.py dan tempel "
                     "logika API kamu (lihat PANDUAN.md bagian 'API Tetap Aman'). "
                     "Atau set api_mode='proxy' di config/config.json untuk memakai "
                     "API serverless kamu yang sekarang.",
        }

    if step == "verify":
        return {
            "success": False,
            "error": "api_handler.py belum diisi (lihat komentar di file ini).",
        }

    return {"success": False, "error": "unknown step"}
