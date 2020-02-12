from flask import Flask, Response, request
from connect_to_bot import *

import bot_testing
import command_handler

app = Flask(__name__)

@app.route('/sanity')
def sanity():return "Server is running"

@app.route('/message', methods=["POST"])
def handle_message():
    try:
        chat_data=request.get_json()

        message = chat_data['message']['text']

        bot_testing.print_message_info(chat_data)

        tosendback =command_handler.message_parser(message)

        send_back_to_user(chat_data,tosendback)

    except:
        print("eception provoked")

    return Response("success")

if __name__ == '__main__':
    app.run(port=5000)
