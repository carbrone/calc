import time
import mss
import keyboard
import pyautogui as py
import numpy as np

color = (165, 165, 165)

py.displayMousePosition()


def findfish():
    fesh = py.locateOnScreen("thefishy.png", confidence=0.8)
    if fesh is not None:
        print("found")
        x, y = py.center(fesh)
        print(x, y)
        return x, y
    else:
        print("not found")
        return False

def goon():
    fihtime = py.prompt("how many clicks")

    time.sleep(2)
    
    regon = (608, 140, 710, 721)
    picture = py.screenshot(region=regon)
    picture.save("test.png")

    for i in range(int(fihtime)):
        thing = findfish()

        if thing:
            x, y = thing
            py.moveTo(x, y)
            py.click()
            print("fish at " + str(x) + "x " + str(y) + "y")
        else:
            print("fish not found")

        time.sleep(0.25)
    
goon()
