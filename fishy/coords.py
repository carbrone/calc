import pyautogui as py
import time
import keyboard
import ctypes
ctypes.windll.shcore.SetProcessDpiAwareness(2)
#for i in range(4):
 #   keyboard.wait("z")
  #  x, y = py.position()
   # print(x, y)

topX = 724 
topY = 288
width = 188
length = 140
time.sleep(5)
py.screenshot(r"C:\Users\carso\OneDrive\Documents\GitHub\calc\fishy\fishytest.png", region=(topX, topY, width, length))
print("done")