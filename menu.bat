@echo off
color 0A
echo.
echo ========================================
echo    ANTICROISSANTERIA - ULTRA RAPIDE
echo ========================================
echo.
echo [!] VERSION OPTIMISEE
echo     Verrouillage en moins de 40ms
echo     AVANT que le message soit envoye !
echo.
echo ========================================
echo.
echo Choisissez une action :
echo.
echo [1] Lancer le programme (mode normal)
echo [2] Lancer en mode invisible
echo [3] Installer au demarrage Windows
echo [4] Tester la performance
echo [5] Voir les statistiques
echo [6] Quitter
echo.
echo ========================================
echo.

set /p choix="Votre choix (1-6) : "

if "%choix%"=="1" goto normal
if "%choix%"=="2" goto invisible
if "%choix%"=="3" goto install
if "%choix%"=="4" goto test
if "%choix%"=="5" goto stats
if "%choix%"=="6" goto fin

:normal
echo.
echo [*] Lancement du programme en mode normal...
echo [*] Appuyez sur Echap pour arreter
echo.
python main.py
goto fin

:invisible
echo.
echo [*] Lancement en mode invisible...
echo [*] Le programme tourne en arriere-plan
echo [*] Aucune fenetre visible
echo.
start "" wscript.exe lancer_invisible.vbs
echo [OK] Programme lance en arriere-plan !
timeout /t 3
goto fin

:install
echo.
echo [*] Installation au demarrage automatique...
echo.
python install_startup.py
timeout /t 5
goto fin

:test
echo.
echo [*] Test de performance...
echo [!] Option 2 ou 3 recommandee (sans verrouillage)
echo.
python test_performance.py
timeout /t 3
goto fin

:stats
echo.
echo [*] Statistiques d'utilisation...
echo.
python -c "from logger import print_stats; print_stats()"
echo.
echo [*] Photos capturees :
dir /B captures 2>nul || echo    Aucune photo pour le moment
echo.
pause
goto fin

:fin
echo.
echo [*] Au revoir !
timeout /t 2
exit
