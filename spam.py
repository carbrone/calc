#me spam 

import time
import pyautogui
import keyboard

#this makes it stop when press x main thingie ma bober
def stopppp():
    global stop
    stop = True
    print("stopping")

keyboard.add_hotkey("x", stopppp)

#just spams one text at a time and counts for how many 
def regularspam():
    global stop
    stop = False
    text = pyautogui.prompt("what thing")
    print(text)
    times = (pyautogui.prompt("how many times (put 0 for forever)"))
    print(times)

    if times != int:
        while not times.isdigit():
            print("thats not a number")
            times = (pyautogui.prompt("how many times (put 0 for forever)"))

    times = int(times)
    time.sleep(5)

    if times == 0:
        i = 0
        while stop == False: #its like the one at the bottom but since its a for loop it uses stop == false instead of if stop
            i+=1
            pyautogui.typewrite(text + str(i + 1))
            pyautogui.press("enter")
            time.sleep(0.75)
        print("is stop")
        
        

    else:
        for i in range(times):
            if stop: #when stop = True (x is pressed) it will stop
                print("is stop 2")
                break
            pyautogui.typewrite(text + " " + str(i + 1))
            pyautogui.press("enter")
            time.sleep(0.75)
            

#ts is basically the same thing but it adds more text each time like a staircase

def staircasespam():
    global stop
    stop = False
    text = pyautogui.prompt("what thing")
    print(text)
    times = (pyautogui.prompt("how many times (put 0 for forever)"))
    print(times)

    if times != int:
        while not times.isdigit():
            print("thats not a number")
            times = (pyautogui.prompt("how many times (put 0 for forever)"))

    times = int(times)
    time.sleep(5)

    for i in range(times):
        if stop: 
            print("is stop stiar")
            break
        pyautogui.typewrite(text * (i + 1))
        pyautogui.press("enter")
        time.sleep(0.75)

staircasespam()
#regularspam()