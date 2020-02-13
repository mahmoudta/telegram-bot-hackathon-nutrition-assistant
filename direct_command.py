import command_handler

direct_commands = {'/start': command_handler.handle_start,
                   '/help': command_handler.handle_help,
                   '/check': command_handler.handle_check,
                   '/insert': command_handler.handle_init,
                   '/calories': command_handler.handle_get_calories,
                   '/cool_insert': command_handler.handle_atractive_insert,
                   '/consume': command_handler.handle_consume,
                   '/bmi': command_handler.handle_bmi,
                   '/ate': command_handler.handle_user_food,
                   '/todaycal': command_handler.handle_today_calories,
                   '/todayprot': command_handler.handle_today_protein,
                   '/today': command_handler.handle_all_info
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

button_commands={
    'M':command_handler.handle_gender_botton,
    'F':command_handler.handle_gender_botton,
    'low':command_handler.handle_exercise_botton,
    'medium':command_handler.handle_exercise_botton,
    'high':command_handler.handle_exercise_botton,
}

def button_parser(chat_data):
    try:

        text = chat_data['message']['text']

        if text in button_commands:
            tosendback = button_commands[text](chat_data['message']['from']['id'])
        else:
            tosendback = "unaccepted input"


    except:
        print("exception provoked from command_handler.button_parser ")

    return tosendback

