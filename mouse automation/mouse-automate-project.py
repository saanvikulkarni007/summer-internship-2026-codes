import pyautogui
import subprocess
import sys
import time

# ── 1. Get screen resolution ──────────────────────────────────────────────────
width, height = pyautogui.size()
print(f"Screen resolution: {width} x {height}")

# ── 2. Close all open windows ─────────────────────────────────────────────────
platform = sys.platform

if platform == "win32":
    # Windows: use taskkill or keyboard shortcut cascade
    import ctypes
    # Show desktop (minimize all windows)
    ctypes.windll.user32.keybd_event(0x5B, 0, 0, 0)   # Win key down
    ctypes.windll.user32.keybd_event(0x44, 0, 0, 0)   # D key down
    ctypes.windll.user32.keybd_event(0x44, 0, 2, 0)   # D key up
    ctypes.windll.user32.keybd_event(0x5B, 0, 2, 0)   # Win key up
    print("All windows minimized (Win + D)")

elif platform == "darwin":
    # macOS: use AppleScript to close all windows
    script = '''
    tell application "System Events"
        set allProcesses to every process where background only is false
        repeat with proc in allProcesses
            try
                tell proc
                    click menu item "Close" of menu "File" of menu bar 1
                end tell
            end try
        end repeat
    end tell
    '''
    subprocess.run(["osascript", "-e", script])
    print("Attempted to close all windows (macOS AppleScript)")

elif platform.startswith("linux"):
    # Linux (X11): use wmctrl to close all windows
    try:
        result = subprocess.run(["wmctrl", "-l"], capture_output=True, text=True)
        window_ids = [line.split()[0] for line in result.stdout.strip().split("\n") if line]
        for wid in window_ids:
            subprocess.run(["wmctrl", "-ic", wid])
        print(f"Closed {len(window_ids)} windows via wmctrl")
    except FileNotFoundError:
        # Fallback: minimize all with xdotool
        subprocess.run(["xdotool", "key", "super+d"])
        print("Minimized all windows via xdotool (super+d)")

print("Done.")