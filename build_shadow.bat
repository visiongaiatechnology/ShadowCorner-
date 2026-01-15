@echo off
echo [SHADOW] Starte Kompilierungsequenz v2.0...

:: 1. Icon generieren (falls gelöscht)
python forge_icon.py

:: 2. Alten Build bereinigen
if exist build rmdir /s /q build
if exist dist rmdir /s /q dist

:: 3. Kompilieren (MIT Version Info)
:: Der Parameter --version-file=version_info.txt ist entscheidend!
pyinstaller --noconsole --onefile --clean --icon=shadow.ico --version-file=version_info.txt --name ShadowCorner shadow_corner.py

echo.
echo [SHADOW] Mission Complete.
echo Die Waffe liegt im Ordner "dist".
pause