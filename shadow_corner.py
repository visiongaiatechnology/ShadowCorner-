import ctypes
import time
import sys
import os
import winreg
from ctypes import wintypes

# --- KONFIGURATION ---
CORNER_SIZE = 5         
POLL_INTERVAL = 0.02    
AUTOSTART_KEY = "ShadowCorner"
APP_ID = "Shadow.Corps.HotCorner.v2" 

# --- WINAPI INIT ---
user32 = ctypes.windll.user32
kernel32 = ctypes.windll.kernel32
shell32 = ctypes.windll.shell32

# High-DPI Awareness
try:
    ctypes.windll.shcore.SetProcessDpiAwareness(1) 
except Exception:
    try: user32.SetProcessDPIAware()
    except: pass

# App ID setzen
try: shell32.SetCurrentProcessExplicitAppUserModelID(APP_ID)
except: pass

# --- STRUKTUREN ---
class RECT(ctypes.Structure):
    _fields_ = [("left", ctypes.c_long), ("top", ctypes.c_long),
                ("right", ctypes.c_long), ("bottom", ctypes.c_long)]

class POINT(ctypes.Structure):
    _fields_ = [("x", ctypes.c_long), ("y", ctypes.c_long)]

# Konstanten
VK_LWIN = 0x5B
VK_TAB  = 0x09
KEYEVENTF_KEYUP = 0x0002
SM_CXSCREEN = 0
SM_CYSCREEN = 1

# --- OPERATIVE INTELLIGENZ (FULLSCREEN GUARD) ---

def is_fullscreen_app_active():
    """
    Prüft, ob das aktive Fenster eine Vollbildanwendung ist (Game, F11 Browser).
    Rückgabe: True (Sensor deaktivieren), False (Sensor aktiv).
    """
    try:
        # 1. Handle des aktiven Fensters holen
        hwnd = user32.GetForegroundWindow()
        if not hwnd: return False

        # 2. Auflösung des Primärmonitors holen
        scr_w = user32.GetSystemMetrics(SM_CXSCREEN)
        scr_h = user32.GetSystemMetrics(SM_CYSCREEN)

        # 3. Geometrie des Fensters holen
        rect = RECT()
        user32.GetWindowRect(hwnd, ctypes.byref(rect))
        
        win_w = rect.right - rect.left
        win_h = rect.bottom - rect.top

        # 4. Namen der Fensterklasse holen (um Desktop/Shell auszuschließen)
        class_name = ctypes.create_unicode_buffer(256)
        user32.GetClassNameW(hwnd, class_name, 256)
        cls = class_name.value

        # Ausnahmen: Desktop (WorkerW, Progman) und Taskleiste (Shell_TrayWnd) 
        # sollen NICHT als Fullscreen-Blocker gelten.
        if cls in ["WorkerW", "Progman", "Shell_TrayWnd"]:
            return False

        # 5. Logik: Wenn Fenstergröße >= Bildschirmgröße -> Vollbild erkannt
        if win_w >= scr_w and win_h >= scr_h:
            return True # Es ist ein Game oder F11 Browser

    except Exception:
        pass
    
    return False

# --- INPUT LOGIK ---

def press_keys():
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
    # ... (Gleiche Routine wie zuvor) ...
    targets = ["hotcorner", "hot corners", "hotcornerswin"]
    key_path = r"Software\Microsoft\Windows\CurrentVersion\Run"
    
    # Registry Cleanup
    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_path, 0, winreg.KEY_ALL_ACCESS)
        hostiles = []
        i = 0
        while True:
            try:
                n, v, _ = winreg.EnumValue(key, i)
                if any(t in n.lower() or t in v.lower() for t in targets): hostiles.append(n)
                i += 1
            except: break
        for h in hostiles:
            try: winreg.DeleteValue(key, h)
            except: pass
        winreg.CloseKey(key)
    except: pass

    # Startup Folder Cleanup
    try:
        sp = os.path.join(os.getenv('APPDATA'), r'Microsoft\Windows\Start Menu\Programs\Startup')
        if os.path.exists(sp):
            for f in os.listdir(sp):
                if any(t in f.lower() for t in targets):
                    try: os.remove(os.path.join(sp, f))
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

# --- MAIN LOOP ---

def main():
    if getattr(sys, 'frozen', False):
        neutralize_hostiles() 
        ensure_persistence()  

    armed = True 
    time.sleep(1.0) 

    while True:
        # INTELLIGENZ-CHECK VOR DEM MAUS-CHECK
        # Wenn wir im Game sind, sparen wir uns den Rest
        if is_fullscreen_app_active():
            time.sleep(1.0) # Schlafen, um CPU zu sparen während gezockt wird
            continue # Nächster Loop-Durchlauf, keine Maus-Prüfung

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