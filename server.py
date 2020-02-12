from flask import Flask, Response, request

from connect_to_bot import *

import bot_testing
import command_handler

app = Flask(__name__)


@app.route('/sanity')
def sanity(): return "Server is running"


@app.route('/message', methods=["POST"])
def handle_message():
    try:
        chat_data = request.get_json()

        user_info=chat_data['message']['chat']
        message = chat_data['message']['text']

        bot_testing.print_message_info(user_info, message)

        tosendback = command_handler.parse_message(message,user_info)

        send_message_to_user(chat_data, tosendback)
    except:
        print("exception provoked from server.handle_message")

    return Response("success")


if __name__ == '__main__':
    app.run(port=5000)
