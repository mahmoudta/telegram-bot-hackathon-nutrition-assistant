from functions import *


def handle_start(command):
    respond = "there should be no<arg> for start, try again"
    arg = command.split()
    if len(arg) == 1:
        respond = start(command)

    return respond

def handle_check(command):
    respond = "there should be two <arg> for check, try again"
    arg = command.split()
    if len(arg) == 3:
        respond = check(command)

    return respond


def handle_help(command):
    respond = "there should be no <arg> for help, try again"
    arg = command.split()
    if len(arg) == 1:
        respond = help(command)

    return respond


direct_commands = {'/start': handle_start,
                 '/help': handle_help,
                 '/check': handle_check,
                 }


def parse_message(message):

    try:
        message_command = message.split()[0]

        if message_command in direct_commands:
            tosendback = direct_commands[message_command](message)
        else:
            tosendback = "wrong command try again"


    except:
        print("exception provoked from command_handler.parse_message ")

    return tosendback