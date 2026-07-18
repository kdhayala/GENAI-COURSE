import time
import pyautogui

pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0.5

print("Moving the mouse to different positions...")
pyautogui.moveTo(100, 100, duration=1)
time.sleep(0.5)
pyautogui.click(100, 100)
time.sleep(0.5)

pyautogui.moveTo(200, 200, duration=1)
time.sleep(0.5)
pyautogui.rightClick(200, 200)
time.sleep(0.5)

pyautogui.moveTo(300, 300, duration=1)
time.sleep(0.5)
pyautogui.middleClick(300, 300)
time.sleep(0.5)

pyautogui.moveTo(400, 400, duration=1)
time.sleep(0.5)
pyautogui.doubleClick(400, 400)

print("Mouse automation completed.")