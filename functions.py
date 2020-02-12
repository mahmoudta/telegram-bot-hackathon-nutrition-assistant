import math

def start(command):
    return "received command "+command[1:]

def help(command):
    return 'commands list :\n ' \
                     '/start  to initi details.\n ' \
                     '/help - to get to this* command list. \n ' \
