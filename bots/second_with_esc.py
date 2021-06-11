"""Second player moves a square."""

import pyautogui
import time

time.sleep(2)

for i in range(8):
    pyautogui.press("up")
    time.sleep(1)
    pyautogui.press("right")
    time.sleep(1)
    pyautogui.press("down")
    time.sleep(1)
    pyautogui.press("left")
    time.sleep(1)
pyautogui.press("esc")
