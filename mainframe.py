# core 'system' functions
import os
from time import sleep

def printStr(input: str) -> str:
    for c in input:
        sleep(0.02)
        print(c, end='')
    return input

# just the introduction
def initBios() -> None:
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

def reboot() -> None:
    printStr("***SYSTEM:: REBOOT INITIATED*** \n\n\n")
    if os.name == "nt":
        os.system('cls')
    else:
        os.system('clear') # for linux users

    printStr("\n...")
