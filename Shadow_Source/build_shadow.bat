@echo off
echo [SHADOW] Starte Kompilierungsequenz...

:: Icon generieren (falls gelöscht)
python forge_icon.py

:: Alten Build bereinigen
rmdir /s /q build
rmdir /s /q dist

:: Kompilieren (Clean, OneFile, NoConsole, Icon)
pyinstaller --noconsole --onefile --clean --icon=shadow.ico --name shadowCorner shadow_corner.py

echo.
echo [SHADOW] Mission Complete.
echo Die Waffe liegt im Ordner "dist".
pause