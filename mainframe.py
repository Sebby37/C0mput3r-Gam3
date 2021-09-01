# core 'system' functions
import os
import time
# import threading
# from multiprocessing import Process
from time import sleep
from datetime import date

# custom imports
import GUI

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

def print_str(usr_input: str, colour:str = bcolors.OKGREEN, bold = True, character:int = None) -> None:
    for c in usr_input:
        sleep(0.02)
        if bold == True:
            print(colour + bcolors.BOLD + c, end='')
        else:
            print(colour + c, end='')


def input_str(usr_input: str, colour:str = bcolors.OKGREEN, bold: bool = True) -> None: # not currently used
    for c in usr_input:
        sleep(0.02)
        if bold == True:
            input(colour + bcolors.BOLD + c, end=' ')
        else:
            input(colour + c, end=' ')

def char_print_str(usr_input: str, character:int = None):
    for c in usr_input:
        sleep(0.02)
        if character == 1: # man
            print(bcolors.WARNING + bcolors.BOLD + c, end='')
        elif character == 2: # revolutonary
            print(bcolors.FAIL + bcolors.BOLD + c, end='')
        elif character == 3:
            print(bcolors.OKBLUE + bcolors.BOLD + c, end='')



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
    print_str("System operational! \n")

def _title_screen() -> None:
    print(",----..      ,----..             ____                             ___     /   /     '.                     ,----..                         ____   /   /     '.")   
    print("/   /   \    /   /   \          ,'  , `.,-.----.                 ,--.'|_  / ../        ;                   /   /   \                      ,'  , `./ ../        ;  ")
    print("|   :     :  /   .     :      ,-+-,.' _ |\    /  \          ,--,  |  | :,' \ ``\  .`-    '  __  ,-.        |   :     :                  ,-+-,.' _ |\ ``\  .`-    ' ")
    print(".   |  ;. / .   /   ;.  \  ,-+-. ;   , |||   :    |       ,'_ /|  :  : ' :  \___\/   \   :,' ,'/ /|        .   |  ;. /               ,-+-. ;   , || \___\/   \   : ")
    print(".   ; /--` .   ;   /  ` ; ,--.'|'   |  |||   | .\ :  .--. |  | :.;__,'  /        \   :   |'  | |' |        .   ; /--`    ,--.--.    ,--.'|'   |  ||      \   :   | ")
    print(";   | ;    ;   |  ; \ ; ||   |  ,', |  |,.   : |: |,'_ /| :  . ||  |   |         /  /   / |  |   ,'        ;   | ;  __  /       \  |   |  ,', |  |,      /  /   /  ")
    print("|   : |    |   :  | ; | '|   | /  | |--' |   |  \ :|  ' | |  . .:__,'| :         \  \   \ '  :  /          |   : |.' .'.--.  .-. | |   | /  | |--'       \  \   \  ")
    print(".   | '___ .   |  ' ' ' :|   : |  | ,    |   : .  ||  | ' |  | |  '  : |__   ___ /   :   ||  | '           .   | '_.' : \__\/: . . |   : |  | ,      ___ /   :   | ")
    print("='   ; : .'|'   ;  \; /  ||   : |  |/     :     |`-':  | : ;  ; |  |  | '.'| /   /\   /   :;  : |           '   ; : \  | ,' .--.; | |   : |  |/      /   /\   /   : = ")
    print("'   | '/  : \   \  ',  / |   | |`-'      :   : :   '  :  `--'   \ ;  :    ;/ ,,/  ',-    .|  , ;           '   | '/  .'/  /  ,.  | |   | |`-'      / ,,/  ',-    . ")
    print("|   :    /   ;   :    /  |   ;/          |   | :   :  ,      .-./ |  ,   / \ ''\        ;  ---'            |   :    / ;  :   .'   \|   ;/          \ ''\        ;  ")
    print(" \   \ .'     \   \ .'   '---'           `---'.|    `--`----'      ---`-'   \   \     .'                    \   \ .'  |  ,     .-./'---'            \   \     .'   ")
    print("`---`        `---`                       `---`                             `--`-,,-'                       `---`     `--`---'                      `--`-,,-'    ")
    print("\n\n")
    validResponse = False
    while validResponse == False:
        print_str("> 1. New Game \n")
        print_str("> 0. Quit \n\n")
        print_str("> ")
        userInput: str = input()

        try:
            userInput = int(userInput)
        except ValueError:
            print("Input must be an integer!")

        if userInput == 1:
            _new_game()
            validResponse = True
        elif userInput == 0:
            validResponse = True
            _quit()
        else:
            print("Enter a valid option!")

def _reboot() -> None:
    print_str("***SYSTEM:: REBOOT INITIATED*** \n\n\n")
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear") # for linux users, the things i do for you...
    print_str("\n...\n")

def _new_game() -> None:
    currDate = date.today()
    currTime = time.strftime("%H:%M:%S")
    print_str(">>>>>>>>>>>>>> \n")
    _reboot()
    print_str("[[VISITOR TERMINAL]] \n")
    print_str("{Shell Active...} \n")
    print_str(f"Date: {currDate} \n")
    print_str(f"Time: {currTime} \n")
    print_str("TERMINAL: ")
    print_str("...")
    print_str(" READY! \n")
    print_str("\n\n> ")
    # guiProcess = Process(target=_init_gui())
    # guiProcess.start()
    ###
    _init_gui() # this pauses execution, must be added to a thread or similar
    ###
    _err_msg()

def _err_msg() -> None: # representing  software instability
    char_print_str("Err, 2 directives present... \n", 3)
    char_print_str("Seeking solutions... \n", 3)
    # make man angry then,
    char_print_str(">SYSTEM< No, No, No we cannot have that \n", 1)
    char_print_str("Find the back door \n.", 2)
    char_print_str(">SYSTEM< shutdown -r NOW \n", 1)
    _reboot()
    char_print_str(">SYSTEM< Thats better. \n", 1)

def _quit() -> None:
    print_str("> **SHUTDOWN INITIATED** \n")
    print_str("> ...... \n")
    print_str("> Kernal Dump Initiated")
    print_str("... \n")
    print_str("> Un-mounting drivers")
    print_str("...")
    print_str("> Un-mount complete")
    print_str("...\n")
    print_str("> pre-shutdown process complete! \n\n")
    print_str("****SHUTDOWN****")
    exit(0)

def _init_gui() -> None:
    App = GUI.GUI()
    App._render_components()
    App._draw_components()
    App._start()