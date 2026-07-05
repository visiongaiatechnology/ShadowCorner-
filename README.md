<div align="center">

```
 ███████╗██╗  ██╗ █████╗ ██████╗  ██████╗ ██╗    ██╗
 ██╔════╝██║  ██║██╔══██╗██╔══██╗██╔═══██╗██║    ██║
 ███████╗███████║███████║██║  ██║██║   ██║██║ █╗ ██║
 ╚════██║██╔══██║██╔══██║██║  ██║██║   ██║██║███╗██║
 ███████║██║  ██║██║  ██║██████╔╝╚██████╔╝╚███╔███╔╝
 ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝  ╚═════╝  ╚══╝╚══╝
```

# ❖ ShadowCorner
### Hot Corner for Windows — Minimalist. Invisible. Tactical.

[![License](https://img.shields.io/badge/License-GPLv3-green?style=for-the-badge)](LICENSE)
[![Version](https://img.shields.io/badge/Version-3.0.0-brightgreen?style=for-the-badge)](#)
[![Status](https://img.shields.io/badge/Status-DIAMANT_VGT_SUPREME-purple?style=for-the-badge)](#)
[![Platform](https://img.shields.io/badge/Platform-Windows_10%2F11-0078D4?style=for-the-badge&logo=windows)](https://microsoft.com/windows)
[![Python](https://img.shields.io/badge/Python-3.13+-3776AB?style=for-the-badge&logo=python)](https://python.org)
[![Architecture](https://img.shields.io/badge/Architecture-Domain--Driven-blue?style=for-the-badge)](#)
[![CPU Idle](https://img.shields.io/badge/CPU_Idle-0.00%25-brightgreen?style=for-the-badge)](#)
[![RAM](https://img.shields.io/badge/RAM-%3C_10_MB-brightgreen?style=for-the-badge)](#)
[![VGT](https://img.shields.io/badge/VGT-VisionGaia_Technology-red?style=for-the-badge)](https://visiongaiatechnology.de)
[![Donate](https://img.shields.io/badge/Donate-PayPal-00457C?style=for-the-badge&logo=paypal)](https://www.paypal.com/paypalme/dergoldenelotus)

**GHOST MODE ACTIVE · EVENT-DRIVEN · ZERO POLLING · ZERO TRAY**

</div>

---

## ⚠️ DISCLAIMER: EXPERIMENTAL R&D PROJECT

This project is a **Proof of Concept (PoC)** and part of ongoing research and development at VisionGaia Technology. It is **not** a certified or production-ready product.

**Use at your own risk.** The software may contain security vulnerabilities, bugs, or unexpected behavior.

Found a vulnerability or have an improvement? **Open an issue or contact us.**

---

## 🔍 What is ShadowCorner?

ShadowCorner ports the Hot Corner paradigm — known from macOS and Linux GNOME — into Windows. Move your mouse to the **top-left corner** of your screen and Task View fires instantly.

Every existing Windows Hot Corner tool is either abandoned, resource-heavy, or breaks during fullscreen applications — triggering accidental tab-outs in the middle of a game.

| Standard Solutions | ShadowCorner v3.0 |
|---|---|
| ❌ Tray icons, settings panels, bloat | ✅ Ghost Mode — completely invisible |
| ❌ Triggers during fullscreen / games | ✅ Smart Guard — native API query, auto-disables |
| ❌ Conflicts with competing processes | ✅ Hostile Neutralization on startup |
| ❌ High RAM / CPU footprint | ✅ < 10 MB RAM · 0.00% CPU idle |
| ❌ Polling loop — constant CPU baseline | ✅ Event-driven — WH_MOUSE_LL hook, zero polling |
| ❌ Generic, unverified binaries | ✅ Signed identity + official hash checker |
| ❌ Breaks on multi-monitor setups | ✅ Full multi-monitor support |
| ❌ DPI scaling errors | ✅ Per-Monitor DPI Awareness Level 2 |

---

## ⚡ Architecture — v3.0 DIAMANT VGT SUPREME

V3.0 is not an incremental update. The entire system was rebuilt from a procedural polling script into a **domain-driven, event-driven, enterprise-grade utility**.

```
┌─────────────────────────────────────────────────────────┐
│                    OPERATOR INPUT                        │
│              Mouse Movement (top-left corner)           │
├─────────────────────────────────────────────────────────┤
│           WH_MOUSE_LL LOW-LEVEL HOOK (Domain 1)         │
│   Windows event callback — fires only on mouse move     │
│   GetMessageW native Win32 message pump (kernel-space)  │
├─────────────────────────────────────────────────────────┤
│         HIGH-PERFORMANCE SPATIAL RAM CACHE (Domain 2)   │
│   O(1) bounds lookup — WinAPI calls reduced by >99%     │
│   Handles 1,000–8,000 Hz gaming mouse polling rates     │
├─────────────────────────────────────────────────────────┤
│           SMART GUARD — FULLSCREEN IFF (Domain 3)       │
│   SHQueryUserNotificationState — native API query       │
│   Auto-disables in games, F11 browser, presentations   │
├─────────────────────────────────────────────────────────┤
│         SENDINPUT KEYBOARD SIMULATION (Domain 4)        │
│   Atomic Win + Tab — modern, AV-compliant, glitch-free  │
├─────────────────────────────────────────────────────────┤
│              STEALTH IDENTITY (Domain 5)                 │
│   Task Manager: Vision Gaia Technology metadata         │
├─────────────────────────────────────────────────────────┤
│          HOSTILE NEUTRALIZATION (Domain 6)               │
│   Conflicting processes terminated on startup           │
└─────────────────────────────────────────────────────────┘
```

---

## 🏛️ Domain-Driven Architecture (V3.0)

V3.0 introduces strict domain separation — the entire system is organized into logically isolated, self-contained domains (Domain 0 through Domain 6).

| Domain | Responsibility |
|---|---|
| **Domain 0** | Configuration & constants |
| **Domain 1** | WH_MOUSE_LL hook + Win32 message pump |
| **Domain 2** | Spatial RAM cache (O(1) bounds lookup) |
| **Domain 3** | Smart Guard — fullscreen IFF detection |
| **Domain 4** | SendInput keyboard simulation |
| **Domain 5** | Stealth identity & process metadata |
| **Domain 6** | Hostile neutralization on startup |

**Enterprise Exception Hierarchy:**
```
VGTException (base)
├── WinAPIException    → OS-level WinAPI interaction failures
└── EnvironmentException → Environment / system state failures
```

Structured, crash-safe error handling for all critical OS interactions.

---

## 🛡️ Core Features

### 👻 Ghost Mode
Runs completely invisible. No system tray icon. No window. No presence. Pure behavior.

```
RAM Usage  : < 10 MB
CPU (Idle) : 0.00%  ← exact, event-driven, kernel-resident
Tray Icon  : NONE
Window     : NONE
```

### 🛡️ Smart Guard — Fullscreen IFF

V1.0 attempted to detect fullscreen games by geometrically comparing the active window size against screen resolution — unreliable with borderless windowed mode and multi-monitor setups.

V3.0 queries the Windows subsystem directly:

```python
SHQueryUserNotificationState()
```

If any application holds exclusive fullscreen access (games, presentations, F11 browser), the sensor disables itself. Re-enables the moment you exit. No false positives. No accidental tab-outs.

### ⚔️ Hostile Neutralization

On startup, ShadowCorner detects and terminates conflicting or outdated processes (e.g. `HotCornersWin`) to prevent behavioral conflicts — automatically and silently.

### 💎 Stealth Identity

Registers itself in Task Manager with correct metadata under **Vision Gaia Technology**. No anonymous or suspicious process entries.

---

## 📊 Evolution — V1.0 → V3.0

| Feature / Metric | V1.0 (Original) | V3.0 (DIAMANT VGT SUPREME) |
|---|---|---|
| **CPU at Idle** | Constant (polling every 20ms) | Exactly 0.00% (event-driven) |
| **Execution Model** | `while True` polling loop | WH_MOUSE_LL hook + Win32 message pump |
| **Multi-Monitor** | Primary monitor only | Full multi-monitor via `MonitorFromPoint` |
| **DPI Scaling** | Broken above 100% | Per-Monitor DPI Awareness Level 2 |
| **Keyboard Sim** | Deprecated `keybd_event` | Atomic `SendInput` |
| **Fullscreen Detection** | Geometric guessing (unreliable) | `SHQueryUserNotificationState` (native API) |
| **Code Architecture** | Procedural script, loose helpers | Domain-Driven Architecture (Domain 0–6) |
| **Error Handling** | No type checks — crash risk | `VGTException` hierarchy + strict prototyping |
| **WinAPI Safety** | No `argtypes`/`restype` — pointer truncation risk | Full 64-bit pointer declaration on all APIs |
| **GC Safety** | Hook callback GC'd mid-run (sporadic crashes) | Callback pinned as class attribute — GC-proof |
| **RAM Cache** | None — WinAPI calls on every mouse event | O(1) spatial RAM cache — >99% WinAPI reduction |

---

## 📜 Changelog

### V3.0.0 — DIAMANT VGT SUPREME *(Current)*

#### Architecture & Design

- **Domain-Driven Architecture:** strict separation into Domain 0–6 — configuration, hook engine, spatial cache, Smart Guard, input simulation, identity, hostile neutralization
- **Enterprise Exception Hierarchy:** `VGTException` base class with `WinAPIException` and `EnvironmentException` subclasses for structured, crash-safe OS interaction error handling

#### Performance & Memory

- **WH_MOUSE_LL Low-Level Mouse Hook:** complete elimination of the CPU-intensive polling loop (`while True` + `time.sleep`). The tool is now purely event-driven — Windows notifies the application via callback only when the mouse actually moves
- **Native Win32 Message Pump (GetMessageW):** when the mouse is idle, the application consumes exactly 0.00% CPU and blocks efficiently in kernel-space until the OS sends a new event
- **High-Performance Spatial RAM Cache:** gaming mice send polling rates of 1,000–8,000 Hz. To avoid thousands of costly WinAPI context switches per second (`MonitorFromPoint`, `GetMonitorInfoW`), an O(1) RAM cache is implemented — WinAPI calls reduced by over 99%

#### Stability & System Safety

- **64-bit Pointer Protection (Strict Prototyping):** all WinAPI interfaces from `user32.dll`, `kernel32.dll` and `shell32.dll` now have explicit `.argtypes` and `.restype` declarations — eliminates memory access violation risk from pointer truncation on 64-bit systems
- **Garbage Collection Protection:** the `ctypes` callback wrapper (`HOOKPROC`) is now permanently held as a class instance attribute — prevents Python's garbage collector from silently disposing the low-level hook during operation (previously caused sporadic, hard-to-debug crashes)

---

### V2.0.0 — Multi-Monitor & Modern Input

#### Geometry & Hardware Detection

- **True Multi-Monitor Support:** moved away from fixed primary monitor coordinates (`SM_CXSCREEN` / `SM_CYSCREEN`). The system now dynamically determines via `MonitorFromPoint` which monitor the mouse is on and calculates the top-left corner of the active monitor
- **DPI Awareness Level 2:** upgraded to Per-Monitor DPI Awareness (`SetProcessDpiAwareness(2)`) — prevents Windows scaling settings (e.g. 150% on 4K monitors) from distorting coordinates

#### Input Simulation

- **SendInput Modernization:** replaced the deprecated `keybd_event` (marked deprecated since Windows 2000) with the modern, atomic `SendInput` API. The key sequence (Win + Tab) is now delivered as a single atomic package to the OS — significantly improves AV recognition rates and eliminates keyboard glitch effects

#### Smart Guard (Fullscreen Protection)

- **Shell State Guard:** replaced geometric window detection with `SHQueryUserNotificationState`. The system now directly queries the Windows subsystem for exclusive fullscreen access (games, presentations, F11 browser) — orders of magnitude faster and more reliable than manual window size comparisons

---

### V1.0.0 — Original *(archived)*

Polling-based implementation. `while True` loop every 20ms — constant CPU baseline load even when idle. Primary monitor only. Deprecated `keybd_event`. No DPI awareness. No type declarations (memory violation risk). Geometric fullscreen detection — unreliable with borderless windowed mode.

---

## 📦 System Specs

```
TRIGGER         TOP-LEFT HOT CORNER
ACTION          WIN + TAB (Task View)
EXECUTION       EVENT-DRIVEN — WH_MOUSE_LL (no polling)
CPU_IDLE        0.00% (kernel-resident message pump)
RAM             < 10 MB
FULLSCREEN_IFF  SHQueryUserNotificationState (native API)
MULTI_MONITOR   MonitorFromPoint — all monitors
DPI_AWARENESS   Per-Monitor Level 2
KEYBOARD_SIM    SendInput (atomic, AV-compliant)
PROCESS_GUARD   HOSTILE NEUTRALIZATION ON BOOT
AUTOSTART       ENABLED ON FIRST RUN
VISIBILITY      GHOST MODE (NO TRAY · NO WINDOW)
ARCHITECTURE    DOMAIN-DRIVEN (0–6)
EXCEPTION_MODEL VGTException hierarchy
LICENSE         GPLv3
```

---

## 🚀 Installation

### Option A — Pre-Compiled Binary (Recommended)

No installation required. Fully portable.

1. Download the latest `ShadowCorner.exe` from [**Releases**](../../releases)
2. Run it
3. **Done.** Autostart is active immediately.

### 🔐 Artifact Verification

Always verify the integrity of your download before execution.

[![Hash Checker](https://img.shields.io/badge/Verify-Official_Hash_Checker-orange?style=for-the-badge)](https://visiongaia.de/hashchecker/)

### Option B — Build from Source

**Requirements:** Python 3.13+, pip

```bash
# Clone the repository
git clone https://github.com/visiongaiatechnology/ShadowCorner-.git

# Install dependencies
pip install pillow pyinstaller

# Build
build_shadow.bat
```

---

## 👁️ Proof of Stealth

### Low Footprint (< 10 MB)
![Performance](./assets/proof_performance.png)

### Corporate Identity
![Identity](./assets/proof_identity.png)

---

## 🔗 VGT Ecosystem

| Tool | Type | Purpose |
|---|---|---|
| ❖ **ShadowCorner** | **Desktop Utility** | Hot corner for Windows — you are here |
| 🧠 **VGT AETHEL** | **Sovereign AI Kernel** | Local AI agent runtime with operator governance |
| 🖥️ **[VGT WP-Desk](https://github.com/visiongaiatechnology/vgtdesk)** | **OS-Layer / UX** | Hardened WordPress operator workspace |
| ⚡ **[VGT Auto-Punisher](https://github.com/visiongaiatechnology/vgt-auto-punisher)** | **IDS** | L4+L7 Hybrid IDS |
| ⚔️ **[VGT Sentinel](https://github.com/visiongaiatechnology/sentinelcom)** | **WAF / IDS** | Zero-Trust WordPress WAF |
| 🌐 **[GaiaCom](https://github.com/visiongaiatechnology/GaiaCom)** | **Communication** | Post-quantum federated E2EE platform |

---

## ☕ Support the Project

ShadowCorner is free. If it improves your daily workflow:

[![Donate via PayPal](https://img.shields.io/badge/Donate-PayPal-00457C?style=for-the-badge&logo=paypal)](https://www.paypal.com/paypalme/dergoldenelotus)

| Method | Address |
|---|---|
| **PayPal** | [paypal.me/dergoldenelotus](https://www.paypal.com/paypalme/dergoldenelotus) |
| **Bitcoin** | `bc1q3ue5gq822tddmkdrek79adlkm36fatat3lz0dm` |
| **ETH / USDT (ERC-20)** | `0xD37DEfb09e07bD775EaaE9ccDaFE3a5b2348Fe85` |

---

## 🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first.

Licensed under **GPLv3** — open source, auditable, free.

---

## 🏢 Built by VisionGaia Technology

[![VGT](https://img.shields.io/badge/VGT-VisionGaia_Technology-red?style=for-the-badge)](https://visiongaiatechnology.de)

VisionGaia Technology builds enterprise-grade security and AI tooling — engineered to the DIAMANT VGT SUPREME standard.

**Project Architect:** KDY // SPACIATMAN
**Copyright:** © 2026 Vision Gaia Technology

> *"The best interface is the one you never see."*

---

<div align="center">

**VISIONGAIATECHNOLOGY – WE ARCHITECT THE FUTURE OF SECURITY.**

[![VGT](https://img.shields.io/badge/VisionGaia-Technology-red?style=for-the-badge)](https://visiongaiatechnology.de)

*ShadowCorner v3.0.0 — DIAMANT VGT SUPREME // Domain-Driven Architecture // WH_MOUSE_LL Event Hook // O(1) Spatial RAM Cache // SHQueryUserNotificationState Fullscreen Guard // SendInput Atomic Simulation // Per-Monitor DPI Level 2 // Full Multi-Monitor // VGTException Hierarchy // Ghost Mode // GPLv3*

</div>
