from functions import *


def handle_start(command):
    respond = "no <arg> for start, try again"
    arg = command.split()
    if len(arg) == 1:
        respond = start(command)

    return respond


def handle_help(command):
    respond = "no <arg> for help, try again"
    arg = command.split()
    if len(arg) == 1:
        respond = help(command)

    return respond


direct_commands = {'/start': handle_start,
                 '/help': handle_help,
                 }


def message_parser(message):
    message_command = message.split()[0]

    if message_command in direct_commands:
        tosendback = direct_commands[message_command](message)
    else:
        tosendback = "wrong command try again"

    return tosendback