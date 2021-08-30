# core 'system' functions

from time import sleep

def printStr(string, delay = 0.02, newline = False):
    for c in string:
        sleep(delay)
        print(c, end='')
    if newline:
        print("")
