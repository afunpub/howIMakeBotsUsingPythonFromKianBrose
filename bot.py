#play magic piano tiles from agame.com
from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api,win32con

#title 1 X:  833 Y:  954 RGB: (  0,  0,  0) title 2 X: 1013 Y:  978 RGB:
#( 78,  81, 115) title 3 X: 1173 Y:  994 RGB: ( 77,  80, 116) title 4 X:
#1365 Y: 1006 RGB: ( 82,  84, 116)

class Get():
    wait=False

    def doThis(self,e):
        self.wait= not self.wait
        
def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.01) #This pauses the script for 0.01 seconds
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

a=Get()
keyboard.on_press_key("q",a.doThis)

#while keyboard.is_pressed('q')==False:
while 1:
    if a.wait:
        try:
            if pyautogui.pixel(833,929)[0] == 0:
                click(833,954)
            if pyautogui.pixel(1013,953)[0] == 0:
                click(1013,978)
            if pyautogui.pixel(1173,969)[0] == 0:
                click(1173,994)
            if pyautogui.pixel(1365,981)[0] == 0:
                click(1365,1006)
        except WindowsError:
            print("You got a WindowsError")
