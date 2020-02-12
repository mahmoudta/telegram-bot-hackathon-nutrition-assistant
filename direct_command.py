import command_handler

direct_commands = {'/start': command_handler.handle_start,
                   '/help': command_handler.handle_help,
                   '/check': command_handler.handle_check,
                   '/insert': command_handler.handle_init,
                   '/calories': command_handler.handle_get_calories,
                   '/consume': command_handler.handle_consume,
                   '/bmi': command_handler.handle_bmi,
                   '/today':command_handler.handle_user_food
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
