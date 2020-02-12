import requests
import bot_testing

# base urls
TOKEN = '1040555856:AAEeMTa4pUEa_ERPYtf8dhMCisGaqVXG_18'
NGROK_URL='https://da4d3727.ngrok.io'
BASE_TELEGRAM_URL='https://api.telegram.org/bot{}'.format(TOKEN)
LOCAL_WEBHOOK_ENDPOINT='{}/message'.format(NGROK_URL)

#url to init connection (no arg needed)
TELEGRAM_INIT_WEBHOOK_URL =BASE_TELEGRAM_URL+'/setWebhook?url={}'.format(LOCAL_WEBHOOK_ENDPOINT)

#url to send to user need (the chat id from ['message']['chat']['id'] , message to send back)
TELEGRAM_SEND_MESSAGE_URL=BASE_TELEGRAM_URL+'/sendMessage?chat_id={}&text={}'

#connect to bot
requests.get(TELEGRAM_INIT_WEBHOOK_URL)


def send_back_to_user(chat_data,tosendback):
    chat_id = chat_data['message']['chat']['id']
    res = requests.get(TELEGRAM_SEND_MESSAGE_URL.format(chat_id, tosendback))
    bot_testing.print_server_respond(res)
    return res