❖ SHADOW CORNER v2.0

Minimalist. Invisible. Tactical.
Developed by Vision Gaia Technology (2026)

📜 MISSION PARAMETER

Shadow Corner ist eine aggressive, minimalistische System-Erweiterung für Microsoft Windows. Sie portiert die "Hot Corner" Funktionalität (bekannt aus MacOS und Linux Gnome) in die Windows-Umgebung – ohne den Ballast herkömmlicher Tools.

Das Ziel: Maximale Übersicht mit einer einzigen Geste.
Bewegen Sie die Maus in die obere linke Bildschirmecke, um sofort die Task-Ansicht (Win+Tab) auszulösen.

Status: STABLE / PRODUCTION READY
Architect: KDY // SPACIATMAN

⚡ CORE ARCHITECTURE (v2.0)

Im Gegensatz zu "bloated" Software-Lösungen arbeitet Shadow Corner direkt am Systemkern:

🛡️ Smart Guard (NEU in v2.0):

Das System verfügt über eine integrierte IFF-Erkennung (Friend or Foe).

Erkennt automatisch Vollbildanwendungen (Games wie CS2/Valorant oder YouTube im F11-Modus).

Effekt: Der Sensor wird temporär deaktiviert, um versehentliche "Tab-Outs" während Gefechten zu verhindern.

👻 Ghost Mode:

Läuft komplett unsichtbar im Hintergrund. Kein Tray-Icon, das die Taskleiste verstopft.

Ressourcenverbrauch: < 10 MB RAM. CPU-Last im Idle: 0.0%.

⚔️ Hostile Neutralization:

Erkennt und eliminiert beim Start automatisch konkurrierende oder veraltete Prozesse (z.B. "HotCornersWin"), um Konflikte zu vermeiden.

💎 Stealth Identity:

Maskiert sich im Task-Manager mit korrekten Metadaten und dem "Tactical Corner" Icon.

🛠️ INSTALLATION & DEPLOYMENT

OPTION A: PRE-COMPILED BINARY (EMPFOHLEN)

Keine Installation notwendig. Portable Mode.

Laden Sie die neueste ShadowCorner.exe unter Releases herunter.

Führen Sie die Datei einmalig aus.

Fertig. Das System ist nun "Armed" und hat sich selbstständig in den Autostart eingetragen.

📦 ARTIFACT VERIFICATION

Vertrauen ist gut, Kontrolle ist besser. Überprüfen Sie die Integrität Ihrer Downloads.

👉 OFFICIAL HASH CHECKER

OPTION B: BUILD FROM SOURCE

Für Agenten, die dem Code misstrauen oder ihn modifizieren wollen.

Voraussetzungen:

Python 3.13+

Pip

Build Sequenz:

Repository klonen:

git clone [https://github.com/visiongaiatechnology/ShadowCorner-.git](https://github.com/visiongaiatechnology/ShadowCorner-.git)
cd ShadowCorner-


Abhängigkeiten installieren:

pip install pillow pyinstaller


Kompilieren (One-Click):
Starten Sie die build_shadow.bat.
Das fertige Artefakt (Exe) befindet sich anschließend im Ordner dist/.

🧠 LOGIC FLOW

Die Kernlogik (shadow_corner.py) basiert auf einer Endlosschleife mit adaptivem Polling (20ms), um die CPU zu schonen, aber maximale Reaktivität zu gewährleisten.

Auszug aus dem Neural Core:

def main():
    if getattr(sys, 'frozen', False):
        neutralize_hostiles() # Clean Environment
        ensure_persistence()  # Registry Hook

    armed = True 
    # ... Event Loop mit Smart Guard Check ...


⚖️ LIZENZ & CREDITS

Dieses Projekt ist Open Source.
Lizenziert unter GPLv3
Developed by Vision Gaia Technology.

Project Architect: KDY // SPACIATMAN

Copyright: © 2026 Vision Gaia Technology

License: Shadow Protocol (Open Source)