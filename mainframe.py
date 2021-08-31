# core 'system' functions
import os
from time import sleep

class bcolors: # for printing color to termial
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'



def print_str(input: str) -> str:
    for c in input:
        sleep(0.02)
        print(bcolors.OKGREEN, c, end='')
    return input

# just the introduction
def _init_bios() -> None:
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
    _reboot()

    print_str("System reboot successful. \n Welcome user. \n")

def _reboot() -> None:
    print_str("***SYSTEM:: REBOOT INITIATED*** \n\n\n")
    if os.name == "nt":
        os.system('cls')
    else:
        os.system('clear') # for linux users

    print_str("\n...")

