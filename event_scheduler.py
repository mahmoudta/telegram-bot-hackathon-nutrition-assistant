import sched, time
import Dao
import requests
from connect_to_bot import TELEGRAM_SEND_MESSAGE_URL
from command_handler import handle_all_info, get_percentage_calories
import time

s = sched.scheduler(time.time, time.sleep)


def do_something(sc):
    chat_ids = Dao.get_all_user_id()
    if chat_ids:
        for id in chat_ids:
            res = requests.get(TELEGRAM_SEND_MESSAGE_URL.format(id, "Been a while since last time"))
            res = requests.get(TELEGRAM_SEND_MESSAGE_URL.format(id, "Below is your summary so far"))
            user_info = {"id": id}
            res = requests.get(TELEGRAM_SEND_MESSAGE_URL.format(id, handle_all_info("", user_info)))
            # calories_percentage = get_percentage_calories(user_info)
            #
            # pre = "Daily Calories "
            # progress_bar = "█" * int(int(calories_percentage) / 100 * 10)
            # progress_left = " " * int((100 - int(calories_percentage)) / 100 * 10)
            # post = "|"
            # total = f"{pre}{progress_bar}{progress_left}{post} %"
            # res = requests.get(TELEGRAM_SEND_MESSAGE_URL.format(id, total))

    # print("hello it is me")
    # do your stuff
    s.enter(10, 1, do_something, (sc,))


s.enter(10, 1, do_something, (s,))
s.run()
