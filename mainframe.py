# Core 'system' functions
import os
import tkinter as tk
from time import sleep

# Prints a string one character at a time with a specific interval
def printStr(input, interval = 0.02, newline = False):
    for c in input:
        sleep(interval)
        print(c, end='')
    if newline:
        print("")

# Just the introduction
def initBios():
    printStr("......... \n")
    printStr("Oracle Terminal ")
    printStr("-> ")
    printStr("Boot sequence initiated! \n")
    printStr("Booting signal GREEN")
    printStr("." * 3)
    print()
    printStr("[")
    for i in range(30):
        printStr("=")
    printStr("=>] \n")
    printStr("Reboot requested... \n")
    reboot()

    printStr("System reboot successful. \n Welcome user. \n")

def reboot():
    printStr("***SYSTEM:: REBOOT INITIATED*** \n\n\n")
    if os.name == "nt":
        os.system('cls')
    else:
        os.system('clear') # for linux users

    printStr("\n...")
