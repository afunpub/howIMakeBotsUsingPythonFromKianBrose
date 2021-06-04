# aimbooster.com
from pyautogui import *
import pyautogui
import keyboard
import time
import random
import win32api,win32con

time.sleep(2)

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

class Get():
    wait=False

    def doThis(self,e):
        self.wait=not self.wait

# color of center:(255, 219, 195)
def fun01():
    pic=pyautogui.screenshot(region=(464,756,1200,840))
    width,heigh=pic.size
    for x in range(0,width,5):
        for y in range(0,heigh,5):
            r,g,b=pic.getpixel((x,y))
            if b==195:
                click(x+464,y+756)
                time.sleep(0.05)
                break

a=Get()
keyboard.on_press_key('q',a.doThis)
while 1:
    if a.wait:
        fun01()