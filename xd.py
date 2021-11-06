from selenium import webdriver;
import time;
import os;
import pyautogui;
import requests;
from pynput.keyboard import Key, Controller
keyboard = Controller()
def Title():
    print("Welcome to ohusq's Multi tool!")
    print("1 = Discord DM Spammer")
    print("2 = Pinger [WIP]")
    print("3 = Chrome Tab Macro")
Title()
def Start():
    OptionSelect = input("Option: ")

    if OptionSelect == "1":
        print()
        req = requests.Session()
        cookiefilefolder = os.path.dirname(__file__)
        cookiefile = (cookiefilefolder + "\cookies.txt")
        cookie = open(cookiefile).read().splitlines()
        validcount = 0
        invalidcount = 0

        if len(cookie) > 0:
            print(str(len(cookie)) + " Cookie(s) Found")
            print(" ")
            pathnameforvalid = os.path.join(os.path.dirname(__file__), "validcookies.txt")
            newfileforvalid = open(pathnameforvalid, "w")
            newfileforvalid.truncate(0)
            pathnameforinvalid = os.path.join(os.path.dirname(__file__), "invalidcookies.txt")
            newfileforinvalid = open(pathnameforinvalid, "w")
            newfileforinvalid.truncate(0)
            for line in cookie:
                check = req.get('https://api.roblox.com/currency/balance', cookies={'.ROBLOSECURITY': str(line)})
                if check.status_code == 200:
                    newfileforvalid.write(str(line) + "\n")
                    validcount += 1
                else:
                    newfileforinvalid.write(str(line) + "\n")
                    invalidcount += 1
            print("Valid Cookie(s): " + str(validcount) + "\nInvalid Cookie(s):" + str(invalidcount))
        else:
            print("No cookies found.")


    if OptionSelect == "2":
        IpInput = input("IP: ")
        print('#' * 20)
        print('Request Timed Out = Website Down')
        os.system('ping -l 1 ' + IpInput)
        print('#' * 20)

    if OptionSelect == "3":
        print('Press Tab to auto switch tabs!')
        while keyboard.pressed(Key.tab):
            with keyboard.pressed(Key.ctrl):
                keyboard.press(Key.tab)
                keyboard.release(Key.tab)
            print("Tab Pressed")
            

while True: # Goes back to Start()
    Start()