#!/usr/bin/env python3
"""
miamotion auto-updater
======================
Keeps this app in sync with your GitHub repo, so you can just
`git push` once and every device updates itself.

Two strategies (automatic):
  1. GIT  - if this folder is a git clone (has .git):
        git fetch  ->  git reset --hard  (local changes are discarded,
        but config/ and server/data/ are ignored/untracked so they survive)
  2. ZIP  - otherwise: download the repo zipball from GitHub and copy it
        over this folder, EXCEPT protected files:
          - config/config.json   (your secrets/settings)
          - server/data/         (your stats)
          - .env

Usage:
  python3 server/updater.py --once     # single check (used at app start)
  python3 server/updater.py            # loop, uses update_interval_sec
"""

import argparse
import json
import shutil
import subprocess
import tempfile
import time
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = Path(__file__).resolve().parent / "data"

# files/dirs that are NEVER overwritten by an update
PROTECT_FILES = {"config/config.json", ".env", "server/data/stats.json", "server/data/last_update.json"}
PROTECT_DIRS = {".git", "server/data"}
JUNK_NAMES = {"__pycache__"}


def _now() -> str:
    return time.strftime("%Y-%m-%dT%H:%M:%S")


def _log_default(m: str) -> None:
    print(f"[update] {m}", flush=True)


def _write_last(result: dict) -> None:
    try:
        DATA_DIR.mkdir(parents=True, exist_ok=True)
        (DATA_DIR / "last_update.json").write_text(json.dumps(result, indent=1), encoding="utf-8")
    except Exception:  # noqa: BLE001
        pass


def _read_version() -> str | None:
    try:
        return json.loads((ROOT / "version.json").read_text(encoding="utf-8")).get("version")
    except Exception:  # noqa: BLE001
        return None


def _git_out(args: list, timeout: int = 120) -> subprocess.CompletedProcess:
    return subprocess.run(args, cwd=str(ROOT), capture_output=True, text=True, timeout=timeout)


def _git_update(repo: str, branch: str, token: str, log) -> dict:
    before = _git_out(["git", "rev-parse", "HEAD"]).stdout.strip()

    if token and repo.count("/") == 1 and not repo.endswith(".git"):
        fetch_url = f"https://x-access-token:{token}@github.com/{repo}.git"
    else:
        fetch_url = "origin"

    r = _git_out(["git", "fetch", "--quiet", fetch_url, branch])
    if r.returncode != 0:
        raise RuntimeError("git fetch failed: " + (r.stderr or "").strip()[:200])

    after = _git_out(["git", "rev-parse", "FETCH_HEAD"]).stdout.strip()
    if not after:
        raise RuntimeError("could not read FETCH_HEAD")

    if before == after:
        log("already up to date")
        return {"changed": False}

    rr = _git_out(["git", "reset", "--hard", "FETCH_HEAD"])
    if rr.returncode != 0:
        raise RuntimeError("git reset failed: " + (rr.stderr or "").strip()[:200])
    log(f"updated  {before[:7]} -> {after[:7]}")
    return {"changed": True, "sha": after}


def _copy_tree(src: Path, dst: Path) -> None:
    for p in src.iterdir():
        rel = p.relative_to(src).as_posix()
        if p.is_dir():
            if p.name in JUNK_NAMES or rel in PROTECT_DIRS or rel == ".git":
                continue
            _copy_tree(p, dst / p.name)
        else:
            if rel in PROTECT_FILES or rel.endswith(".pyc") or "__pycache__" in rel:
                continue
            target = dst / p.name
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(p, target)


def _zip_update(repo: str, branch: str, token: str, log) -> dict:
    import requests

    if repo.count("/") == 1 and not repo.startswith("http"):
        api = f"https://api.github.com/repos/{repo}/zipball/{branch}"
    elif repo.startswith("http"):
        api = f"{repo.rstrip('/')}/archive/{branch}.zip"
    else:
        raise RuntimeError("repo must look like 'username/repo-name'")

    headers = {"User-Agent": "miamotion-updater"}
    if token:
        headers["Authorization"] = f"Bearer {token}"

    before = _read_version()
    with tempfile.TemporaryDirectory() as td:
        tdp = Path(td)
        zpath = tdp / "repo.zip"
        with requests.get(api, headers=headers, stream=True, timeout=120) as r:
            r.raise_for_status()
            with open(zpath, "wb") as f:
                for chunk in r.iter_content(65536):
                    f.write(chunk)
        xdir = tdp / "x"
        xdir.mkdir()
        with zipfile.ZipFile(zpath) as z:
            z.extractall(xdir)
        entries = list(xdir.iterdir())
        src = entries[0] if len(entries) == 1 else xdir  # zipball has one top folder
        _copy_tree(src, ROOT)

    after = _read_version()
    changed = before != after
    log("zip updated" if changed else "zip: no version change")
    return {"changed": changed}


def update_once(cfg: dict, log=_log_default) -> dict:
    repo = (cfg.get("repo") or "").strip()
    branch = (cfg.get("branch") or "main").strip()
    token = (cfg.get("github_token") or "").strip()

    result = {"time": _now(), "changed": False, "method": None, "error": None}
    if not repo:
        log("repo not set - auto-update skipped (set 'repo' in config/config.json)")
        _write_last(result)
        return result

    try:
        if (ROOT / ".git").exists() and shutil.which("git"):
            result["method"] = "git"
            result.update(_git_update(repo, branch, token, log))
        else:
            result["method"] = "zip"
            result.update(_zip_update(repo, branch, token, log))
    except Exception as e:  # noqa: BLE001
        result["error"] = str(e)
        log(f"error: {e}")

    _write_last(result)
    return result


def main() -> None:
    ap = argparse.ArgumentParser(description="miamotion auto-updater")
    ap.add_argument("--once", action="store_true", help="single check then exit")
    args = ap.parse_args()

    cfg: dict = {}
    cp = ROOT / "config" / "config.json"
    if cp.exists():
        try:
            cfg = {k: v for k, v in json.loads(cp.read_text(encoding="utf-8")).items()
                   if not str(k).startswith("_")}
        except Exception:  # noqa: BLE001
            pass

    if args.once:
        update_once(cfg)
        return

    interval = int(cfg.get("update_interval_sec") or 300)
    if interval <= 0:
        _log_default("disabled (update_interval_sec = 0)")
        return
    while True:
        update_once(cfg)
        time.sleep(interval)


if __name__ == "__main__":
    main()
