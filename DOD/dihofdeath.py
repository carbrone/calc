import time
from PIL import Image
import keyboard
import pytesseract as pt
import cv2
import pyautogui as auto
import threading
import sys
auto.FAILSAFE = True

print_lock = threading.Lock()
stop_event = threading.Event()

#silly varibels#
coords=""
Thelace=""  
wego = "we no head to"
zekiller = "no kaller"

# mouse pos yes me#

def mousepos():
    global coords
    while not stop_event.is_set():
        x, y = auto.position()
        coords = f"X: {x:5d}  Y: {y:5d}"
        time.sleep(0.05)

#ocr for the top location of the screen#

def look():
    global Thelace
    while not stop_event.is_set():
        Place = auto.screenshot(region = (625, 37, 600, 37))
        Thelace = pt.image_to_string(Place).replace("\n", "").strip()
        time.sleep(0.5)

#says which map we are going to#

def whichmap():
    global wego
    while not stop_event.is_set():
        if "Baseplate" in Thelace:
            wego = "we go baseplate"
        elif "Backyard" in Thelace:
            wego = "we go backyard"
        elif "Temple" in Thelace:
            wego = "we go tempil"
        elif "HQ" in Thelace:
            wego = "we go  hatchoo"
        elif "Tundra" in Thelace:
            wego = "we go toondra"
        elif "Glasshouses" in Thelace:
            wego = "we go glasshouses"
        elif "Teapot" in Thelace:
            wego = "we cecus"
        else:
            wego = "we no head to"
        time.sleep(0.5)
    
def tskiller():
    global zekiller
    while not stop_event.is_set():
        killer = auto.screenshot(region = (700, 920, 500, 200))
        killer.save("killer.png")
        ouikiller = pt.image_to_string(killer).replace("\n", "").strip()
        time.sleep(0.5)
        if "pineapple7987" in ouikiller:
            zekiller = "Its meee"
        else:
            zekiller = "ts not a killer"


mouse = threading.Thread(target=mousepos)
location = threading.Thread(target=look)
igo = threading.Thread(target=whichmap)
askiller = threading.Thread(target=tskiller)

mouse.start()
location.start()
igo.start()
askiller.start()

print(zekiller)
sys.stdout.write("hello\n")
while True:
    print(f" ze coords  {coords} | za ocr {Thelace} | za map {wego} | oui killer {zekiller} ", end="\r", flush=True)
    time.sleep(0.05)

    if keyboard.is_pressed("z"):
        stop_event.set()
        print("oki i stop")
        sys.exit()
        break


mouse.join()
location.join()
print('stop')
