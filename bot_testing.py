

def print_message_info(chat_data):
    print("message:")
    print(chat_data['message']['text'])
    print("from:")
    print(chat_data['message']['chat'])

def print_server_respond(res):
    print(res)