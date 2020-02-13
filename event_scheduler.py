import sched, time
import Dao
import requests
from connect_to_bot import TELEGRAM_SEND_MESSAGE_URL
from command_handler import handle_all_info, get_percentage_calories, handle_get_calories, handle_today_protein
import time
import random

s = sched.scheduler(time.time, time.sleep)

random_data = ["Been a while since last time\n Below is a summary of your daily report\n",
               "Did you enter your last meal?\n Use /consume to add it\n",
               "Check your food for fats before eating them using /check\n",
               "Have you passed your target calories??\n"
               "Is your protein intake enough for today??\n"]


def do_something(sc):
    chat_ids = Dao.get_all_user_id()
    if chat_ids:
        for id in chat_ids:
            user_info = {"id": id}
            random_int = random.randrange(0, len(random_data))
            if random_int == 0:
                res = requests.get(TELEGRAM_SEND_MESSAGE_URL.format(id, random_data[0]))
                res = requests.get(TELEGRAM_SEND_MESSAGE_URL.format(id, handle_all_info("", user_info)))
            elif random_int == 1:
                res = requests.get(TELEGRAM_SEND_MESSAGE_URL.format(id, random_data[1]))
            elif random_int == 2:
                res = requests.get(TELEGRAM_SEND_MESSAGE_URL.format(id, random_data[2]))
            elif random_int == 3:
                res = requests.get(TELEGRAM_SEND_MESSAGE_URL.format(id, random_data[3]))
                res = requests.get(TELEGRAM_SEND_MESSAGE_URL.format(id, handle_get_calories(" ", user_info)))
            elif random_int == 4:
                res = requests.get(TELEGRAM_SEND_MESSAGE_URL.format(id, random_data[4]))
                res = requests.get(TELEGRAM_SEND_MESSAGE_URL.format(id, handle_today_protein(" ",user_info)))

            # res = requests.get(TELEGRAM_SEND_MESSAGE_URL.format(id, "Been a while since last time"))
            # res = requests.get(TELEGRAM_SEND_MESSAGE_URL.format(id, "Below is your summary so far"))
            # res = requests.get(TELEGRAM_SEND_MESSAGE_URL.format(id, handle_all_info("", user_info)))

    s.enter(10, 1, do_something, (sc,))


s.enter(10, 1, do_something, (s,))
s.run()
