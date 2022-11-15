import os
import pyautogui
import time
import hashlib
input_hash = input("Enter hash of victim: ")
try:
    pass_file = open('pas.txt', "r")
except:
    print("Password file not opened")
    quit()
for password in pass_file:
    password = password.replace("\n","")
    print(password)
    enc = password.encode('utf-8')
    #in loc de md5 pun hash fol de catre victima
    digest = hashlib.md5(enc.strip()).hexdigest()
    print("password" + " " + digest)
    if input_hash == digest:
        print("password found")
        print("password is " + " " + password)
        break
    