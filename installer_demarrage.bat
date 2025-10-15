@echo off
echo ================================================
echo Installation AntiCroisenteria au demarrage
echo ================================================
echo.

cd /d "%~dp0"

REM Lancer le script d'installation
python install_startup.py

echo.
pause
