import pyautogui as py
import pyperclip  as pyp

# 这个插件是用来快速打开知网的
a = py.locateCenterOnScreen("image copy.png",confidence=0.8)
py.moveTo(a)
py.click(clicks=2)
py.sleep(0.3)
pyp.copy("https://www.cnki.net/")
py.hotkey("ctrl","v")
py.press("enter")
