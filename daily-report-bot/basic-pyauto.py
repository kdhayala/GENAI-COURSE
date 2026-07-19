import pyautogui
import pyperclip
import time
from datetime import datetime

# -----------------------------
# Configuration
# -----------------------------
pyautogui.FAILSAFE = True
pyautogui.PAUSE = 1

today = datetime.now()
date_time = today.strftime("%Y-%m-%d %H:%M:%S")
date_only = today.strftime("%Y-%m-%d")

filename = f"daily_report_{date_only}.xlsx"
comment = "Good day for outdoor activities"

# -----------------------------
# Open Chrome
# -----------------------------
pyautogui.hotkey("win", "r")
time.sleep(1)

pyautogui.write("chrome")
pyautogui.press("enter")

time.sleep(5)

# -----------------------------
# Open Website
# -----------------------------
pyautogui.hotkey("ctrl", "l")
pyautogui.write("https://www.weather.com", interval=0.03)
pyautogui.press("enter")

time.sleep(8)

# -----------------------------
# Copy page title (example)
# -----------------------------
pyautogui.hotkey("ctrl", "l")
time.sleep(1)

pyautogui.hotkey("ctrl", "c")

time.sleep(1)

website = pyperclip.paste()

# -----------------------------
# Open Excel
# -----------------------------
pyautogui.hotkey("win", "r")

time.sleep(1)

pyautogui.write("excel")

pyautogui.press("enter")

time.sleep(8)

# -----------------------------
# New Workbook
# -----------------------------
pyautogui.hotkey("ctrl", "n")
time.sleep(2)

# -----------------------------
# Write Data
# -----------------------------
pyautogui.write(date_time)

pyautogui.press("tab")

pyautogui.write(website)

pyautogui.press("tab")

pyautogui.write(comment)

# -----------------------------
# Save Workbook
# -----------------------------
pyautogui.hotkey("ctrl", "shift", "s")

time.sleep(3)

pyautogui.write(filename)

time.sleep(1)

pyautogui.press("enter")

time.sleep(5)

# -----------------------------
# Screenshot
# -----------------------------
pyautogui.screenshot(f"daily_report_{date_only}.png")

print("Automation completed successfully!")
