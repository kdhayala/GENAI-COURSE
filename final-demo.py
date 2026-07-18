import time
import pyautogui

pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0.5

# Open Run dialog
pyautogui.hotkey('win', 'r')
time.sleep(1)

# Launch Chrome
pyautogui.write('chrome')
pyautogui.press('enter')

# Wait for Chrome to open
time.sleep(5)

# Focus the address bar
pyautogui.hotkey('ctrl', 'l', interval=0.1)

# Type the URL
pyautogui.typewrite('https://www.accuweather.com/en/in/chennai/206671/hourly-weather-forecast/206671', interval=0.50)
time.sleep(1)
time.sleep(1)
pyautogui.press('enter')

print("Take a screenshot of the weather forecast page in 5 seconds...")

time.sleep(5)
pyautogui.hotkey('ctrl', 'a', interval=0.1) # Select all content
time.sleep(1)
pyautogui.hotkey('ctrl', 'c', interval=0.1) # Copy content to clipboard
time.sleep(1)

print("Screenshot taken and content copied to clipboard.")

# Open Notepad directly instead of using unsupported shortcuts
pyautogui.hotkey('win', 'r')
time.sleep(1)
pyautogui.write('notepad')
time.sleep(1)
pyautogui.press('enter')
time.sleep(2)
pyautogui.hotkey('ctrl', 'v')
