import requests
import bot_testing
from telegram import ReplyKeyboardRemove, ReplyKeyboardMarkup

# base urls
TOKEN = '1040555856:AAEeMTa4pUEa_ERPYtf8dhMCisGaqVXG_18'
NGROK_URL = 'https://325c06ce.ngrok.io'
BASE_TELEGRAM_URL = 'https://api.telegram.org/bot{}'.format(TOKEN)
LOCAL_WEBHOOK_ENDPOINT = '{}/message'.format(NGROK_URL)

# url to init connection (no arg needed)
TELEGRAM_INIT_WEBHOOK_URL = BASE_TELEGRAM_URL + '/setWebhook?url={}'.format(LOCAL_WEBHOOK_ENDPOINT)

# url to send to user need (the chat id from ['message']['chat']['id'] , message to send back)
TELEGRAM_SEND_MESSAGE_URL = BASE_TELEGRAM_URL + '/sendMessage?chat_id={}&text={}&parse_mode=HTML'

TELEGRAM_SEND_BOTTON_URL = TELEGRAM_SEND_MESSAGE_URL + '&reply_markup={}'

# connect to bot
requests.get(TELEGRAM_INIT_WEBHOOK_URL)


def send_message_to_user(chat_data, tosendback):
    chat_id = chat_data['message']['chat']['id']
    res = requests.get(TELEGRAM_SEND_MESSAGE_URL.format(chat_id, tosendback))
    return res


def build_menu(buttons, n_cols, header_buttons=None, footer_buttons=None):
    menu = [buttons[i:i + n_cols] for i in range(0, len(buttons), n_cols)]
    if header_buttons:
        menu.insert(0, header_buttons)
    if footer_buttons:
        menu.append(footer_buttons)
    return menu


def add_botton(chatid, custom_keyboard, title):
    try:
        print("chatid")
        print(chatid)

        reply_markup = ReplyKeyboardMarkup(custom_keyboard)
        res = requests.get(TELEGRAM_SEND_BOTTON_URL.format(chatid, title, reply_markup.to_json()))
    except:
        print("exception provoked from connect_to_bot.add_gender_botton")


def removepreviusmarkup(chatid):
    reply_markup = ReplyKeyboardRemove()
    res = requests.get(TELEGRAM_SEND_BOTTON_URL.format(chatid, "---", reply_markup.to_json()))
