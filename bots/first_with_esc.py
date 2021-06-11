"""First player moves a square."""

import pyautogui
import time

time.sleep(2)

for i in range(8):
    pyautogui.press("d")
    time.sleep(1)
    pyautogui.press("s")
    time.sleep(1)
    pyautogui.press("a")
    time.sleep(1)
    pyautogui.press("w")
    time.sleep(1)

pyautogui.press("esc")
