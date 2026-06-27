import webbrowser
import subprocess
import threading
import time
import os
import pyautogui
import pygetwindow as gw

pyautogui.FAILSAFE = True

def open_browser():
    webbrowser.open("https://www.google.com")

def draw_line(x1, y1, x2, y2, speed=0.4):
    pyautogui.moveTo(x1, y1)
    pyautogui.mouseDown()
    pyautogui.moveTo(x2, y2, duration=speed)
    pyautogui.mouseUp()
    time.sleep(0.2)

def open_paint_and_draw():
    # ── OPEN PAINT via Windows Store URI ──────────────────────────
    print("Opening Paint...")
    os.system("start ms-paint:")
    time.sleep(6)

    # ── FIND AND FOCUS PAINT WINDOW ───────────────────────────────
    paint_win = None
    for title in gw.getAllTitles():
        if 'Paint' in title:
            print(f"Found window: {title}")
            paint_win = gw.getWindowsWithTitle(title)[0]
            break

    if paint_win:
        paint_win.maximize()
        time.sleep(1)
        paint_win.activate()
        time.sleep(1)
    else:
        print("Could not find Paint window. Trying to click center...")
        pyautogui.click(960, 540)
        time.sleep(1)

    # Click canvas to make sure Paint is active and focused
    pyautogui.click(700, 500)
    time.sleep(0.5)

    # ── LINE ──────────────────────────────────────────────────────
    print("Drawing Line...")
    draw_line(300, 300, 700, 300)
    time.sleep(0.5)

    # ── RECTANGLE ─────────────────────────────────────────────────
    print("Drawing Rectangle...")
    draw_line(500, 200, 800, 200)   # Top
    draw_line(800, 200, 800, 420)   # Right
    draw_line(800, 420, 500, 420)   # Bottom
    draw_line(500, 420, 500, 200)   # Left
    time.sleep(0.5)

    # ── SAVE ──────────────────────────────────────────────────────
    print("Saving file...")
    pyautogui.hotkey('ctrl', 's')
    time.sleep(2)
    pyautogui.typewrite('shapes_drawing3', interval=0.1)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.press('enter')
    print("File saved as shapes_drawing3!")

# ── RUN BOTH THREADS ──────────────────────────────────────────────
browser_thread = threading.Thread(target=open_browser)
paint_thread   = threading.Thread(target=open_paint_and_draw)

browser_thread.start()
paint_thread.start()

browser_thread.join()
paint_thread.join()

print("✅ All done!")