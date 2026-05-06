import pytesseract
from PIL import ImageGrab
import time
import keyboard

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


SCORE_REGION = (239, 485, 545, 585)

import easyocr
from PIL import ImageGrab

reader = easyocr.Reader(['en'])


def getscore():
    img = ImageGrab.grab(bbox=SCORE_REGION)
    img.save("score.png")
    result = reader.readtext("score.png", detail=0)
    print(result)
    text = result[0] if result else None
    
    try:
        current, total = text.split("/")
        return int(current.strip()), int(total.strip())
    except:
        return None, None
    
keyboard.wait("z")
getscore()