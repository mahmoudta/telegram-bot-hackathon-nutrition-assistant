import math


def start(command):
    return "received command " + command[1:]


def check(command):
    return "received command " + command[1:] + "with values" + ""


def help(command):
    return 'commands list :\n ' \
           '/start  to initi details.\n ' \
           '/check  to check nutrethion in food.\n ' \
           '/help - to get to this* command list. \n '
