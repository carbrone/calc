import time
import mss
import keyboard
import pyautogui as py
import numpy as np

color = (165, 165, 165)

fish = r"C:\Users\carso\OneDrive\Documents\GitHub\calc\fishy\nobgfisb.png"

def findfish():
    try:
        fesh = py.locateOnScreen(fish, confidence=0.8)
        x,y = py.center(fesh)
        print(x, y)
        return x, y
    except py.ImageNotFoundException:
        print("couldnt find fish")







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
