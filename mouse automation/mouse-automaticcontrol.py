import pyautogui
import time

# Get screen resolution
width, height = pyautogui.size()
print(f"Screen resolution: {width} x {height}")

# Move mouse to center of screen
pyautogui.moveTo(width/2, height/2, duration=1)
print("Mouse moved to center")

# Move mouse to all 4 corners
pyautogui.moveTo(0, 0, duration=0.5)           # top left
pyautogui.moveTo(width, 0, duration=0.5)        # top right
pyautogui.moveTo(width, height, duration=0.5)   # bottom right
pyautogui.moveTo(0, height, duration=0.5)       # bottom left

# Close all windows using keyboard shortcut
pyautogui.hotkey('win', 'd')
print("All windows minimized")