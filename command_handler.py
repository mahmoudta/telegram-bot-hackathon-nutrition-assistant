from functions import *


def handle_start(command, user_info):
    respond = "there should be no<arg> for start, try again"
    arg = command.split()
    if len(arg) == 1:
        respond = func_start(command)

    return respond


def handle_check(command, user_info):
    respond = "there should be  <sentence> for check, try again"
    arg = command.split()
    if len(arg) > 1:
        respond = func_check(command)
    return respond


def handle_init(command, user_info):
    respond = "there should be  <sentence> for check, try again"
    arg = command.split()
    print(len(arg))
    if len(arg) == 6:
        respond = func_init(command, user_info)
    return respond


def handle_help(command, user_info):
    respond = "there should be no <arg> for help, try again"
    arg = command.split()
    if len(arg) == 1:
        respond = func_help(command)

    return respond


def handle_get_calories(command, user_info):
    target_calories = func_get_calories(user_info)["target_calories"]
    result = f"Your daily intake of calories should be {target_calories} calories per day"
    return result


direct_commands = {'/start': handle_start,
                   '/help': handle_help,
                   '/check': handle_check,
                   '/insert': handle_init,
                   '/calories': handle_get_calories
                   }


def parse_message(message, user_info):
    try:
        message_command = message.split()[0]

        if message_command in direct_commands:
            tosendback = direct_commands[message_command](message, user_info)
        else:
            tosendback = "wrong command try again"


    except:
        print("exception provoked from command_handler.parse_message ")

    return tosendback
