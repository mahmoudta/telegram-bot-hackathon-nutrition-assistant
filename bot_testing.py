

def print_message_info(chatinfo,message):
    try:
        print("from print_message_info")
        print("message: " + message)
        print("from " + "id: "+str(chatinfo['id'])+" username: "+chatinfo['username'])

    except:
        print("exception provoked from bot_testing.print_message_info ")


def print_server_respond(res):
    print(res)