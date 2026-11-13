@echo off
title miamotion app
cd /d "%~dp0"
where python >nul 2>nul
if errorlevel 1 (
  echo [x] Python tidak ditemukan. Install dari https://python.org dan centang "Add to PATH".
  pause
  exit /b 1
)
python server\updater.py --once
python server\app.py
pause
