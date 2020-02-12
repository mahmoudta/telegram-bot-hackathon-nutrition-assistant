from functions import *


def handle_start(command,user_info):
    respond = "there should be no<arg> for start, try again"
    arg = command.split()
    if len(arg) == 1:
        respond = func_start(command)

    return respond


def handle_check(command,user_info):
    respond = "there should be  <sentence> for check, try again"
    arg = command.split()
    if len(arg) > 1:
        respond = func_check(command)
    return respond

def handle_init(command,user_info):
    respond = "there should be  <sentence> for check, try again"
    arg = command.split()
    if len(arg) == 4:
        respond = func_init(command,user_info)
    return respond



def handle_help(command,user_info):
    respond = "there should be no <arg> for help, try again"
    arg = command.split()
    if len(arg) == 1:
        respond = func_help(command)

    return respond


direct_commands = {'/start': handle_start,
                   '/help': handle_help,
                   '/check': handle_check,
                   }


def parse_message(message,user_info):
    try:
        message_command = message.split()[0]

        if message_command in direct_commands:
            tosendback = direct_commands[message_command](message,user_info)
        else:
            tosendback = "wrong command try again"


    except:
        print("exception provoked from command_handler.parse_message ")

    return tosendback
