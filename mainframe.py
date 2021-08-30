# core 'system' functions

from time import sleep

def printStr(string):
    for c in string:
        sleep(0.02)
        print(c, end='')