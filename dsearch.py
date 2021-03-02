from colorama import Fore, Back, Style
import requests
import time
import os
#imports lmao

url=input("Enter url: ")
fpath=input("Enter the full path of your wordlist: ")
wfile=open(fpath, 'r')

i=0
while(i<1):
    print("Loading...|")
    time.sleep(0.3)
    os.system("cls")
    print("Loading.../")
    time.sleep(0.3)
    os.system("cls")
    print("Loading...-")
    time.sleep(0.3)
    os.system("cls")
    print("Loading...|")
    time.sleep(0.3)
    os.system("cls")
    print("Loading.../")
    time.sleep(0.3)
    os.system("cls")
    print("Loading...-")
    time.sleep(0.3)
    os.system("cls")
    print("Loading...\\")
    time.sleep(0.3)
    os.system("cls")
    i+=1
    
    
os.system("cls")

for line in wfile:
    req=requests.get("http://"+url+"/"+line)
    if req.status_code==200:
        print("Found directory: "+ line+"\n")
    else:
        pass
    
    
