import os
import pyautogui
import time
try:
    pass_file = open('pas.txt', "r")
except:
    print("Password file not opened")
    quit()
for password in pass_file:
    password = password.replace("\n","")
    print(password)

    pyautogui.write(password, interval=0.1)
    pyautogui.press('enter')
    time.sleep(1)