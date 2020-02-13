from functions import *
import connect_to_bot

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


def handle_consume(command, user_info):
    respond = "there should be  <sentence> for consume, try again"
    arg = command.split()
    print(len(arg))
    if len(arg) > 1:
        respond = func_cunsumed(command, user_info)
    return respond


def handle_init(command, user_info):
    respond = "there should be  <age> <height> <weight> <gender> <low|medium|high> for init, try again"
    arg = command.split()
    if len(arg) == 6:
        respond = func_init(command, user_info)
    return respond

def handle_atractive_insert(command, user_info):
    respond = "there should be  <age> <height> <weight> for insert, try again"
    arg = command.split()
    if len(arg) == 4:
        respond = func_atractive_insert(command, user_info)

        custom_keyboard = [['F', 'M']]
        title = "chose gender - male or female"
        connect_to_bot.add_botton(user_info['id'], custom_keyboard,title)
    return respond

def handle_gender_botton(chatid):

    connect_to_bot.removepreviusmarkup(chatid)
    custom_keyboard = [['low', 'medium', 'high']]
    title= "chose daily exersise intencity - low or medium or high"
    connect_to_bot.add_botton(chatid,custom_keyboard,title)


def handle_exercise_botton(chatid):

    connect_to_bot.removepreviusmarkup(chatid)


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
