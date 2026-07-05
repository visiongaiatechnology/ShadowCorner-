# STATUS: DIAMANT VGT SUPREME

import ctypes
import time
import sys
import os
import winreg
from ctypes import wintypes

# ==============================================================================
# DOMÄNE 0: ARCHITEKTONISCHE AUSNAHME-HIERARCHIE
# ==============================================================================
class VGTException(Exception):
    """Basis-Exception für das VisionGaia Architektur-System."""
    pass

class WinAPIException(VGTException):
    """Tritt bei unzulässigen Rückgabewerten der Windows-API auf."""
    pass

class EnvironmentException(VGTException):
    """Tritt bei Fehlern im OS-Umfeld oder Rechtenormen auf."""
    pass

# ==============================================================================
# DOMÄNE 1: SUBSYSTEM FÜR CONFIG & GEOMETRIE
# ==============================================================================
class VGTConfig:
    CORNER_SIZE: int = 5
    HYSTERESIS_THRESHOLD: int = 60
    COOLDOWN_DELAY: float = 0.6
    AUTOSTART_KEY: str = "ShadowCorner"
    APP_ID: str = "Shadow.Corps.HotCorner.v3"
    WH_MOUSE_LL: int = 14
    WM_MOUSEMOVE: int = 0x0200
    INPUT_KEYBOARD: int = 1
    KEYEVENTF_KEYUP: int = 0x0002
    VK_LWIN: int = 0x5B
    VK_TAB: int = 0x09
    MONITOR_DEFAULTTONEAREST: int = 0x00000002

# ==============================================================================
# DOMÄNE 2: NATIVE TYP-DEFINITIONEN & WINAPI PROTOTYPEN
# ==============================================================================
user32 = ctypes.windll.user32
kernel32 = ctypes.windll.kernel32
shell32 = ctypes.windll.shell32

class RECT(ctypes.Structure):
    _fields_ = [
        ("left", ctypes.c_long),
        ("top", ctypes.c_long),
        ("right", ctypes.c_long),
        ("bottom", ctypes.c_long)
    ]

class POINT(ctypes.Structure):
    _fields_ = [
        ("x", ctypes.c_long),
        ("y", ctypes.c_long)
    ]

class MONITORINFO(ctypes.Structure):
    _fields_ = [
        ("cbSize", wintypes.DWORD),
        ("rcMonitor", RECT),
        ("rcWork", RECT),
        ("dwFlags", wintypes.DWORD)
    ]

class KEYBDINPUT(ctypes.Structure):
    _fields_ = [
        ("wVk", wintypes.WORD),
        ("wScan", wintypes.WORD),
        ("dwFlags", wintypes.DWORD),
        ("time", wintypes.DWORD),
        ("dwExtraInfo", ctypes.POINTER(ctypes.c_ulong))
    ]

class HARDWAREINPUT(ctypes.Structure):
    _fields_ = [
        ("uMsg", wintypes.DWORD),
        ("wParamL", wintypes.WORD),
        ("wParamH", wintypes.WORD)
    ]

class MOUSEINPUT(ctypes.Structure):
    _fields_ = [
        ("dx", ctypes.c_long),
        ("dy", ctypes.c_long),
        ("mouseData", wintypes.DWORD),
        ("dwFlags", wintypes.DWORD),
        ("time", wintypes.DWORD),
        ("dwExtraInfo", ctypes.POINTER(ctypes.c_ulong))
    ]

class INPUT_UNION(ctypes.Union):
    _fields_ = [
        ("mi", MOUSEINPUT),
        ("ki", KEYBDINPUT),
        ("hi", HARDWAREINPUT)
    ]

class INPUT(ctypes.Structure):
    _fields_ = [
        ("type", wintypes.DWORD),
        ("u", INPUT_UNION)
    ]

class MSLLHOOKSTRUCT(ctypes.Structure):
    _fields_ = [
        ("pt", POINT),
        ("mouseData", wintypes.DWORD),
        ("flags", wintypes.DWORD),
        ("time", wintypes.DWORD),
        ("dwExtraInfo", ctypes.POINTER(ctypes.c_ulong))
    ]

HOOKPROC = ctypes.WINFUNCTYPE(ctypes.c_longlong, ctypes.c_int, wintypes.WPARAM, wintypes.LPARAM)

# Explizite Prototypisierung zur Verhinderung von 64-Bit-Pointer-Kürzungen
kernel32.GetModuleHandleW.argtypes = [wintypes.LPCWSTR]
kernel32.GetModuleHandleW.restype = wintypes.HMODULE

kernel32.GetLastError.argtypes = []
kernel32.GetLastError.restype = wintypes.DWORD

user32.SetWindowsHookExW.argtypes = [ctypes.c_int, HOOKPROC, wintypes.HINSTANCE, wintypes.DWORD]
user32.SetWindowsHookExW.restype = wintypes.HHOOK

user32.UnhookWindowsHookEx.argtypes = [wintypes.HHOOK]
user32.UnhookWindowsHookEx.restype = wintypes.BOOL

user32.CallNextHookEx.argtypes = [wintypes.HHOOK, ctypes.c_int, wintypes.WPARAM, wintypes.LPARAM]
user32.CallNextHookEx.restype = ctypes.c_longlong

user32.GetMessageW.argtypes = [ctypes.POINTER(wintypes.MSG), wintypes.HWND, wintypes.UINT, wintypes.UINT]
user32.GetMessageW.restype = wintypes.BOOL

user32.TranslateMessage.argtypes = [ctypes.POINTER(wintypes.MSG)]
user32.TranslateMessage.restype = wintypes.BOOL

user32.DispatchMessageW.argtypes = [ctypes.POINTER(wintypes.MSG)]
user32.DispatchMessageW.restype = ctypes.c_longlong

user32.MonitorFromPoint.argtypes = [POINT, wintypes.DWORD]
user32.MonitorFromPoint.restype = wintypes.HMONITOR

user32.GetMonitorInfoW.argtypes = [wintypes.HMONITOR, ctypes.POINTER(MONITORINFO)]
user32.GetMonitorInfoW.restype = wintypes.BOOL

user32.SendInput.argtypes = [wintypes.UINT, ctypes.POINTER(INPUT), ctypes.c_int]
user32.SendInput.restype = wintypes.UINT

shell32.SHQueryUserNotificationState.argtypes = [ctypes.POINTER(ctypes.c_int)]
shell32.SHQueryUserNotificationState.restype = ctypes.c_long

try:
    ctypes.windll.shcore.SetProcessDpiAwareness(2)
except Exception:
    try:
        user32.SetProcessDPIAware()
    except Exception:
        pass

try:
    shell32.SetCurrentProcessExplicitAppUserModelID(VGTConfig.APP_ID)
except Exception:
    pass

# ==============================================================================
# DOMÄNE 3: SYSTEM-UMFELDS-GUARD (FULLSCREEN & STATE VALIDATION)
# ==============================================================================
class VGTSystemGuard:
    @staticmethod
    def is_fullscreen_active() -> bool:
        state = ctypes.c_int(0)
        hr = shell32.SHQueryUserNotificationState(ctypes.byref(state))
        if hr == 0:
            if state.value in (2, 3, 4):
                return True
        return False

# ==============================================================================
# DOMÄNE 4: INPUT INJECTION ARCHITEKTUR
# ==============================================================================
class VGTInputEngine:
    @staticmethod
    def _create_key_input(vk: int, flags: int) -> INPUT:
        extra = ctypes.c_ulong(0)
        ki = KEYBDINPUT(
            wVk=vk,
            wScan=0,
            dwFlags=flags,
            time=0,
            dwExtraInfo=ctypes.pointer(extra)
        )
        return INPUT(type=VGTConfig.INPUT_KEYBOARD, u=INPUT_UNION(ki=ki))

    @classmethod
    def inject_task_view(cls) -> None:
        inputs = (INPUT * 4)()
        inputs[0] = cls._create_key_input(VGTConfig.VK_LWIN, 0)
        inputs[1] = cls._create_key_input(VGTConfig.VK_TAB, 0)
        inputs[2] = cls._create_key_input(VGTConfig.VK_TAB, VGTConfig.KEYEVENTF_KEYUP)
        inputs[3] = cls._create_key_input(VGTConfig.VK_LWIN, VGTConfig.KEYEVENTF_KEYUP)
        
        result = user32.SendInput(4, inputs, ctypes.sizeof(INPUT))
        if result != 4:
            raise WinAPIException("SendInput-Sequenz unvollständig ausgeführt.")

# ==============================================================================
# DOMÄNE 5: KERNEL RECOVERY & HARDENING (CLEANUP & AUTOSTART)
# ==============================================================================
class VGTLifecycleManager:
    @staticmethod
    def neutralize_hostiles() -> None:
        targets = ["hotcorner", "hot corners", "hotcornerswin"]
        key_path = r"Software\Microsoft\Windows\CurrentVersion\Run"
        try:
            key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_path, 0, winreg.KEY_ALL_ACCESS)
            hostiles = []
            i = 0
            while True:
                try:
                    name, val, _ = winreg.EnumValue(key, i)
                    if any(t in name.lower() or t in val.lower() for t in targets):
                        if VGTConfig.AUTOSTART_KEY.lower() not in name.lower():
                            hostiles.append(name)
                    i += 1
                except OSError:
                    break
            for h in hostiles:
                try:
                    winreg.DeleteValue(key, h)
                except OSError:
                    pass
            winreg.CloseKey(key)
        except Exception as e:
            error_log(f"[SEC] Registry-Bereinigung fehlgeschlagen: {str(e)}")

    @staticmethod
    def ensure_persistence() -> None:
        exe_path = os.path.abspath(sys.argv[0])
        if not exe_path.lower().endswith(".exe"):
            return
        key_path = r"Software\Microsoft\Windows\CurrentVersion\Run"
        try:
            key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_path, 0, winreg.KEY_ALL_ACCESS)
            try:
                val, _ = winreg.QueryValueEx(key, VGTConfig.AUTOSTART_KEY)
                if val != exe_path:
                    raise FileNotFoundError
            except FileNotFoundError:
                winreg.SetValueEx(key, VGTConfig.AUTOSTART_KEY, 0, winreg.REG_SZ, exe_path)
            winreg.CloseKey(key)
        except Exception as e:
            error_log(f"[STORAGE] Autostart-Persistenz fehlgeschlagen: {str(e)}")

def error_log(message: str) -> None:
    print(message, file=sys.stderr)

# ==============================================================================
# DOMÄNE 6: CORE EXECUTION ENGINE (EREIGNISGESTEUERTE HOOK-SCHLEIFE WITH CACHE)
# ==============================================================================
class VGTShadowEngine:
    def __init__(self) -> None:
        self._hook: wintypes.HHOOK = None
        self._armed: bool = True
        self._last_trigger_time: float = 0.0
        self._hook_wrapper = HOOKPROC(self._mouse_hook_callback)

        self._cached_left: int = 0
        self._cached_top: int = 0
        self._cached_right: int = 0
        self._cached_bottom: int = 0
        self._cache_valid: bool = False

    def _mouse_hook_callback(self, nCode: int, wParam: wintypes.WPARAM, lParam: wintypes.LPARAM) -> ctypes.c_longlong:
        if nCode >= 0 and wParam == VGTConfig.WM_MOUSEMOVE:
            try:
                data = ctypes.cast(lParam, ctypes.POINTER(MSLLHOOKSTRUCT)).contents
                x, y = data.pt.x, data.pt.y

                if self._cache_valid and (self._cached_left <= x < self._cached_right) and (self._cached_top <= y < self._cached_bottom):
                    target_x = self._cached_left
                    target_y = self._cached_top
                else:
                    pt = POINT(x, y)
                    h_monitor = user32.MonitorFromPoint(pt, VGTConfig.MONITOR_DEFAULTTONEAREST)
                    if h_monitor:
                        mi = MONITORINFO()
                        mi.cbSize = ctypes.sizeof(MONITORINFO)
                        if user32.GetMonitorInfoW(h_monitor, ctypes.byref(mi)):
                            self._cached_left = mi.rcMonitor.left
                            self._cached_top = mi.rcMonitor.top
                            self._cached_right = mi.rcMonitor.right
                            self._cached_bottom = mi.rcMonitor.bottom
                            self._cache_valid = True
                            
                            target_x = self._cached_left
                            target_y = self._cached_top
                        else:
                            return user32.CallNextHookEx(self._hook, nCode, wParam, lParam)
                    else:
                        return user32.CallNextHookEx(self._hook, nCode, wParam, lParam)

                in_corner = (x <= target_x + VGTConfig.CORNER_SIZE) and (y <= target_y + VGTConfig.CORNER_SIZE)
                current_time = time.time()

                if in_corner:
                    if self._armed and (current_time - self._last_trigger_time >= VGTConfig.COOLDOWN_DELAY):
                        if not VGTSystemGuard.is_fullscreen_active():
                            VGTInputEngine.inject_task_view()
                            self._last_trigger_time = current_time
                            self._armed = False
                else:
                    if (x > target_x + VGTConfig.HYSTERESIS_THRESHOLD) or (y > target_y + VGTConfig.HYSTERESIS_THRESHOLD):
                        self._armed = True

            except Exception as e:
                error_log(f"[FATAL] Fehler im Hook-Callback: {str(e)}")

        return user32.CallNextHookEx(self._hook, nCode, wParam, lParam)

    def start(self) -> None:
        if getattr(sys, 'frozen', False):
            VGTLifecycleManager.neutralize_hostiles()
            VGTLifecycleManager.ensure_persistence()

        # Typensicheres Auflösen des HMODULE über das nun korrekte 64-Bit-Prototyping
        h_module = kernel32.GetModuleHandleW(None)

        self._hook = user32.SetWindowsHookExW(
            VGTConfig.WH_MOUSE_LL,
            self._hook_wrapper,
            h_module,
            0
        )

        if not self._hook:
            error_code = kernel32.GetLastError()
            raise WinAPIException(f"Low-Level Windows Mouse Hook konnte nicht instanziiert werden. System-Fehlercode: {error_code} (0x{error_code:X})")

        try:
            msg = wintypes.MSG()
            while user32.GetMessageW(ctypes.byref(msg), None, 0, 0) != 0:
                user32.TranslateMessage(ctypes.byref(msg))
                user32.DispatchMessageW(ctypes.byref(msg))
        finally:
            if self._hook:
                user32.UnhookWindowsHookEx(self._hook)

# ==============================================================================
# ENTRY POINT
# ==============================================================================
if __name__ == "__main__":
    try:
        engine = VGTShadowEngine()
        engine.start()
    except KeyboardInterrupt:
        sys.exit(0)
    except VGTException as e:
        error_log(f"[CRITICAL] System-Absturz verhindert: {str(e)}")
        sys.exit(1)
