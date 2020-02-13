from flask import Flask, Response, request

from connect_to_bot import *

import bot_testing
import direct_command

app = Flask(__name__)


@app.route('/sanity')
def sanity(): return "Server is running"


@app.route('/message', methods=["POST"])
def handle_message():
    try:
        chat_data = request.get_json()
        print(chat_data)
        tosendback = " "

        if  'entities' in chat_data['message']:
            user_info = chat_data['message']['chat']
            message = chat_data['message']['text']
            bot_testing.print_message_info(user_info, message)
            tosendback = direct_command.parse_message(message, user_info)
        else:
            direct_command.button_parser(chat_data)

        send_message_to_user(chat_data, tosendback)

    except :
        print("exception provoked from server.handle_message")

    return Response("success")


if __name__ == '__main__':
    app.run(port=5000)
