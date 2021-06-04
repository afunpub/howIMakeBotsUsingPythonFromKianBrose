from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api,win32con

#r'C:\Users\afunp\Downloads\howIMakeBotsUsingPythonFromKianBrose'

while 1:
    if pyautogui.locateOnScreen('stickman.png',region=(460,470,430,490),grayscale=True,confidence=0.8)!=None:
        print("I can see it")
        time.sleep(0.5)
    else:
        print("I am unable to see it")
        time.sleep(0.5)
