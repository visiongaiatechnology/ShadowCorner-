Shadow Corner - Operations Log

Status: Active

Classification: Open Source Tooling

Identity: Minimalist Hot Corner Daemon (Python Native)

Ein radikal reduzierter, ressourcen-effizienter Ersatz für "HotCornersWin".

Fokus: Zero-Bloat, maximale Performance, "Ghost Mode" Operation.

[v2.0.0] - "Smart Guard" (Current Build)

Major Release

Feature: Fullscreen Guard (Smart Sensor)

Der Sensor erkennt jetzt automatisch Vollbildanwendungen (Spiele, YouTube im F11-Modus).

IFF-Logik: Unterscheidet zwischen "Maximiertem Fenster" (Arbeitsmodus -> Sensor AN) und "Exklusivem Vollbild" (Gaming/Media -> Sensor AUS).

Verhindert tödliche "Tab-Outs" in CS2, Valorant oder CoD bei schnellen Mausbewegungen ("Flicks").

Core: Update auf Kernel v2.0.

Meta: Integration von Windows-Versions-Metadaten (Task-Manager zeigt jetzt korrekte Version und Firmenname "Shadow Corps").

[v1.5.0] - "Identity"

Visuals: Custom Icon

Implementierung der "Tactical Corner" Insignie (Rote Ecke auf Schwarz).

Integration in Taskleiste und Task-Manager via AppUserModelID.

Tooling: forge_icon.py erstellt Assets (ICO & PNG) dynamisch.

[v1.4.0] - "Ghost Mode"

Feature: Hostile Takeover

Automatischer Scan und Entfernung von Konkurrenz-Software ("HotCornersWin") aus Registry und Autostart-Ordnern beim Start.

Stealth: Optimierung für konsolenlosen Betrieb.

Persistence: Robuste Registry-Injektion (HKCU\...\Run).

[v1.3.0] - "Protocol Breach"

Core: Input Protocol Change

Wechsel von SendInput (Hardware Scan Codes) auf Legacy API keybd_event.

Tactical Advantage: Umgehung von Sicherheitsfiltern in Windows 11, die synthetische Eingaben blockierten.

Timing-Anpassung auf 50ms für maximale Zuverlässigkeit bei minimaler Latenz.

[v1.0.0 - v1.2.0] - "Prototype Phase"

v1.2: Experimente mit Hardware Scan Codes (Vom OS blockiert).

v1.1: High-Frequency Polling (Instabil).

v1.0: Initialer Proof of Concept mit ctypes.