❖ SHADOW CORNER

ADVANCED WINDOW MANAGEMENT INTERFACE

DESIGNED & ENGINEERED BY KDY // SPACIATMAN

📜 MISSION PARAMETER

ShadowCorner ist eine aggressive, minimalistische System-Erweiterung für Microsoft Windows. Sie portiert die "Hot Corner" Funktionalität (bekannt aus MacOS und Linux Gnome) in die Windows-Umgebung.

Das Ziel: Maximale Übersicht mit einer einzigen Geste.
Bewegen Sie die Maus in die obere linke Bildschirmecke, um sofort die Task-Ansicht (Win+Tab) auszulösen.

⚡ CORE ARCHITECTURE

Im Gegensatz zu bloated Software-Lösungen arbeitet ShadowCorner direkt am Systemkern:

Zero Bloat: Weniger als 10MB RAM Nutzung.

Direct WinAPI Access: Nutzt ctypes und user32.dll für direkte Hardware-Abfragen.

Ultra-Low Latency: 20ms Polling-Rate für sofortige Reaktion ohne CPU-Last.

Hostile Neutralization: Erkennt und eliminiert automatisch konkurrierende oder veraltete HotCorner-Prozesse beim Start.

Persistent State: Integrierter Autostart-Mechanismus in der Registry.

🛠️ INSTALLATION & DEPLOYMENT

OPTION A: PRE-COMPILED BINARY (EMPFOHLEN)

Laden Sie die signierte Executable direkt herunter. Keine Installation notwendig, Portable Mode.

Download der shadowCorner.zip.

Entpacken an einen beliebigen Ort (z.B. C:\Tools\ShadowCorner).

shadowCorner.exe ausführen.

Fertig. Das System ist nun "Armed".

SHA-256 Verifikation für ShadowCorner.zip:

65f95a108ce6587d627f49808562a3486151e4412e560a20c47134185434dd2c


OPTION B: BUILD FROM SOURCE

Für Entwickler, die dem Code misstrauen oder ihn modifizieren wollen.

Voraussetzungen:

Python 3.10+

Pip

Build Sequenz:

# 1. Repository klonen
git clone [https://github.com/visiongaiatechnology/ShadowCorner-.git](https://github.com/visiongaiatechnology/ShadowCorner-.git)
cd ShadowCorner-

# 2. Abhängigkeiten installieren
pip install pillow pyinstaller

# 3. Icon schmieden & Kompilieren
# Führt forge_icon.py und PyInstaller aus
build_shadow.bat


Das fertige Artefakt befindet sich anschließend im Ordner dist/.

🧠 LOGIC FLOW

Die Kernlogik (shadow_corner.py) basiert auf einer Endlosschleife mit minimalem Sleep-Timer, um die CPU zu schonen, aber maximale Reaktivität zu gewährleisten.

# Auszug aus dem Neural Core
def main():
    if getattr(sys, 'frozen', False):
        neutralize_hostiles() # Clean Environment
        ensure_persistence()  # Registry Hook

    armed = True 
    # ... Event Loop ...


⚖️ LIZENZ & CREDITS

Dieses Projekt ist unter der GPLv3 Lizenz veröffentlicht. Open Source ist die einzige Wahrheit.

PROJECT ARCHITECT:

KDY // SPACIATMAN

VisionGaia Technology © 2026
