@echo off
cd /d "%~dp0"
python stop.py
timeout /t 2 /nobreak >nul
