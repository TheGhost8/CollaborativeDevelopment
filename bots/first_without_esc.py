"""First player moves a rectangle."""

import pyautogui
import time

time.sleep(2)

for i in range(18):
    pyautogui.press("d")
    time.sleep(1)
    pyautogui.press("s")
    time.sleep(2)
    pyautogui.press("a")
    time.sleep(1)
    pyautogui.press("w")
    time.sleep(2)
