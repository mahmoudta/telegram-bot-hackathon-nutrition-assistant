import requests
import bot_testing

TOKEN = '1008102529:AAEUP_EsZdSN1D47Pa5hA1OPKi03bPIGeos'
google_url='https://da4d3727.ngrok.io'
TELEGRAM_INIT_WEBHOOK_URL = 'https://api.telegram.org/bot{}/setWebhook?url={}/message'.format(TOKEN,google_url)
requests.get(TELEGRAM_INIT_WEBHOOK_URL)


def send_back_to_user(chat_data,tosendback):
    chat_id = chat_data['message']['chat']['id']
    res = requests.get("https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}"
                       .format(TOKEN, chat_id, tosendback))
    bot_testing.print_server_respond(res)
    return res
