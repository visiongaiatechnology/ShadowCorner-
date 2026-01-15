import ctypes
import time
import sys
import os
import winreg
from ctypes import wintypes

# --- KONFIGURATION (FINAL STABLE) ---
CORNER_SIZE = 5         
POLL_INTERVAL = 0.02    
AUTOSTART_KEY = "ShadowCorner"
# Eindeutige Identität für Windows Task Manager & Taskbar
APP_ID = "Shadow.Corps.HotCorner.v1" 

# --- WINAPI INIT ---
user32 = ctypes.windll.user32
kernel32 = ctypes.windll.kernel32
shell32 = ctypes.windll.shell32

# 1. High-DPI Awareness (Präzision)
try:
    ctypes.windll.shcore.SetProcessDpiAwareness(1) 
except Exception:
    try:
        user32.SetProcessDPIAware()
    except Exception:
        pass

# 2. IDENTITÄTS-SIGNATUR (FIX FÜR TASK MANAGER ICON)
# Zwingt Windows, den Prozess als App mit diesem Icon zu erkennen
try:
    shell32.SetCurrentProcessExplicitAppUserModelID(APP_ID)
except Exception:
    pass

# Tasten-Konstanten
VK_LWIN = 0x5B
VK_TAB  = 0x09
KEYEVENTF_KEYUP = 0x0002

class POINT(ctypes.Structure):
    _fields_ = [("x", ctypes.c_long), ("y", ctypes.c_long)]

# --- OPERATIVE FUNKTIONEN ---

def press_keys():
    """Feuert Win+Tab. Timing auf 50ms verlangsamt für Zuverlässigkeit."""
    user32.keybd_event(VK_LWIN, 0, 0, 0)
    time.sleep(0.05) 
    user32.keybd_event(VK_TAB, 0, 0, 0)
    time.sleep(0.05)
    user32.keybd_event(VK_TAB, 0, KEYEVENTF_KEYUP, 0)
    time.sleep(0.05)
    user32.keybd_event(VK_LWIN, 0, KEYEVENTF_KEYUP, 0)

def get_mouse_pos():
    pt = POINT()
    user32.GetCursorPos(ctypes.byref(pt))
    return pt.x, pt.y

def neutralize_hostiles():
    """Scannt Registry und Autostart-Ordner nach Altlasten."""
    targets = ["hotcorner", "hot corners", "hotcornerswin"]
    key_path = r"Software\Microsoft\Windows\CurrentVersion\Run"
    hostiles_found = []

    # Phase 1: Registry
    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_path, 0, winreg.KEY_ALL_ACCESS)
        i = 0
        while True:
            try:
                name, value, _ = winreg.EnumValue(key, i)
                if any(t in name.lower() or t in value.lower() for t in targets):
                    hostiles_found.append(name)
                i += 1
            except OSError:
                break 
        for target in hostiles_found:
            try: winreg.DeleteValue(key, target)
            except: pass
        winreg.CloseKey(key)
    except: pass 

    # Phase 2: Startup Folder
    try:
        startup_path = os.path.join(os.getenv('APPDATA'), r'Microsoft\Windows\Start Menu\Programs\Startup')
        if os.path.exists(startup_path):
            for file in os.listdir(startup_path):
                if any(t in file.lower() for t in targets):
                    try: os.remove(os.path.join(startup_path, file))
                    except: pass
    except: pass

def ensure_persistence():
    exe_path = os.path.abspath(sys.argv[0])
    if not exe_path.endswith(".exe"): return 
    key_path = r"Software\Microsoft\Windows\CurrentVersion\Run"
    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_path, 0, winreg.KEY_ALL_ACCESS)
        try:
            val, _ = winreg.QueryValueEx(key, AUTOSTART_KEY)
            if val != exe_path: raise FileNotFoundError
        except FileNotFoundError:
            winreg.SetValueEx(key, AUTOSTART_KEY, 0, winreg.REG_SZ, exe_path)
        winreg.CloseKey(key)
    except: pass

# --- HAUPTSCHLEIFE ---

def main():
    if getattr(sys, 'frozen', False):
        neutralize_hostiles() 
        ensure_persistence()  

    armed = True 
    time.sleep(1.0) 

    while True:
        x, y = get_mouse_pos()

        if x <= CORNER_SIZE and y <= CORNER_SIZE:
            if armed:
                press_keys() 
                armed = False 
                time.sleep(0.5) 
        else:
            if x > 50 or y > 50: 
                armed = True
                
        time.sleep(POLL_INTERVAL)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(0)