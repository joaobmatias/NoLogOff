import pyautogui

## from PyQt4 import *


pyautogui.FAILSAFE = True
pyautogui.PAUSE = 10




# function move mouse
def moveMouse():
    while True:
        pyautogui.moveRel(100, 0, duration=0.25)
        pyautogui.moveRel(0, 100, duration=0.25)
        pyautogui.moveRel(-100, 0, duration=0.25)
        pyautogui.moveRel(0, -100, duration=0.25)

# function close program
def closeProg():
        KeyboardInterrupt
        print('\nProgram stopped. Thank you for using')


try:
    moveMouse()
    print('Mouse moving automatically activated')
    print('Press Ctrl-C to quit.')

except:
    closeProg()