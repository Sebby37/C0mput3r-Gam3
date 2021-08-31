# core 'system' functions
import os
from time import sleep

def print_str(input: str) -> str:
    for c in input:
        sleep(0.02)
        print(c, end='')
    return input

# just the introduction
def initBios() -> None:
    print_str("......... \n")
    print_str("Oracle Terminal ")
    print_str("-> ")
    print_str("Boot sequence initiated! \n")
    print_str("Booting signal GREEN")
    print_str("." * 3)
    print()
    print_str("[")
    for i in range(30):
        print_str("=")
    print_str("=>] \n")
    print_str("Reboot requested... \n")
    reboot()

    print_str("System reboot successful. \n Welcome user. \n")

def reboot() -> None:
    print_str("***SYSTEM:: REBOOT INITIATED*** \n\n\n")
    if os.name == "nt":
        os.system('cls')
    else:
        os.system('clear') # for linux users

    print_str("\n...")
