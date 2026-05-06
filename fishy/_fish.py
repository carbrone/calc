import time
import mss
import keyboard
import pyautogui as py
import numpy as np
from PIL import ImageGrab
import pydirectinput
import pytesseract


box2 = (452, 504, 100, 100)

#who is he? mr. color
#color = (165, 165, 165)

#pytesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
#what the fish is
fish = r"C:\Users\carso\OneDrive\Documents\GitHub\calc\fishy\nobgfisb.png"

def stawp():
    global stop
    stop = False

keyboard.add_hotkey("x", stawp)

#finds the fish
def findfish():
    try:
        fesh = py.locateOnScreen(fish, confidence=0.7, grayscale=True)
        x,y = py.center(fesh)
        print(x, y)
        return x, y
    except py.ImageNotFoundException:
        print("couldnt find fish")


# def findfish():
#     img = ImageGrab.grab(bbox=box)
#     pixels = np.array(img)
    
#     # find white pixels (the number on fish #1 only)
#     pixel = (
#     (pixels[:,:,0] == 255) &
#     (pixels[:,:,1] == 255) &
#     (pixels[:,:,2] == 255)
# )
    
#     locations = np.argwhere(pixels)
    
#     if len(locations) > 0:
#         y, x = locations.mean(axis=0)
#         screen_x = int(x) + box[0]
#         screen_y = int(y) + box[1]
#         return screen_x, screen_y
    
#     return None

#does and maybe clicks
def goon():
    fihtime = py.prompt("how many clicks")

    global box
    box = (608, 140, 710, 721)
    picture = py.screenshot(region=box)
    picture.save(r"C:\Users\carso\OneDrive\Documents\GitHub\calc\fishy\test.png")

    pydirectinput.click()
    pydirectinput.click()

    for i in range(int(fihtime)):
        result = findfish()
        if result:
            x, y = result
            color = py.pixel(int(x), int(y))
            print(f"click {i+1}: found at {x}, {y}")
            print(color)
            pydirectinput.click(x, y)
        else:
            print(f"click {i+1}: not found")
        time.sleep(0.1)

    pydirectinput.click()
    pydirectinput.click()


stop = False

while stop != True:
    goon()
    if stop:
        print("its stoped")
        break
