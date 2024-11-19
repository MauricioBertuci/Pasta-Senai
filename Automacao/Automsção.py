#Assistir video no youtube
import time
import pyautogui as auto

auto.hotkey("win", "tab")
time.sleep(1)
auto.moveTo(x=111, y=56)
auto.click()
time.sleep(1)
auto.click(x=292, y=95)
time.sleep(2)

auto.press("win")
time.sleep(1)
auto.write("Google", interval= 0.25)
time.sleep(2)
auto.press("enter")
time.sleep(2)

auto.write('youtube.com', interval= 0.25)
auto.press("backspace")
auto.press("enter")
time.sleep(2)

auto.moveTo(x=848, y=170)
auto.click()

auto.write("video de pessoas dormindo",interval= 0.25)
auto.click()
auto.press("enter")
time.sleep(1)
auto.moveTo(x=815, y=349)
auto.click()





