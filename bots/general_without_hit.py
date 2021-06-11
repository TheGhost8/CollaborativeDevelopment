"""First and Second player moves a square."""

import pyautogui
import time

time.sleep(2)

for i in range(6):
    pyautogui.press("up")
    pyautogui.press("d")
    time.sleep(1)
    pyautogui.press("right")
    pyautogui.press("s")
    time.sleep(2)
    pyautogui.press("down")
    pyautogui.press("a")
    time.sleep(1)
    pyautogui.press("left")
    pyautogui.press("w")
    time.sleep(2)

pyautogui.press("esc")
