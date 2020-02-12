import datetime
import edamam_api
import Dao
import pretty_message
import calories_calculator



def func_start(command):
    return "received command " + command[1:]

def func_cunsumed(command, user_info):
    try:
        sentence = " ".join(command.split()[1:])
        nutrition = edamam_api.get_nutritions(sentence)


        food_id = Dao.get_or_insert_food(nutrition["name"],nutrition["weight"],nutrition["calories"],nutrition["protein"],nutrition["total_fat"],nutrition["carbs"],nutrition["water"])

        now=datetime.date.today()
        now=now.strftime('%Y-%m-%d')

        results=Dao.insert_or_increment_food_user(user_info['id'],food_id,now,1)
        if results:
            toreturn = pretty_message.check_pretty(nutrition)
        else:
            toreturn="failed to add food"
    except:
        print("exception provoked from functhion.func_check")

    return toreturn

def func_init(command, user_info):
    var_list = command.split()[1:]
    age = var_list[0]
    height = var_list[1]
    weight = var_list[2]
    gender = var_list[3]
    if gender == "M":
        gender_bool = True
    elif gender == "F":
        gender_bool = False

    exercise = var_list[4]

    insert_result = Dao.insert_user(user_info['id'], user_info['username'], age, height, weight, gender_bool)
    if insert_result:

        target_calories = calories_calculator.calculate_daily_calories(height, weight, age, gender, exercise)
        target_result = Dao.insert_user_target(user_info['id'], 0, target_calories, 0, 0)
    else:
        toreturn = "init failed"
    return toreturn


def func_check(command):
    try:
        sentence = " ".join(command.split()[1:])
        toreturn = edamam_api.get_nutritions(sentence)
        toreturn = pretty_message.check_pretty(toreturn)
    except:
        print("exception provoked from functhion.func_check")

    return toreturn


def func_help(command):
    return 'commands list :\n ' \
           '/start  to initi details.\n ' \
           '/check  to check nutrethion in food.\n ' \
           '/help - to get to this* command list. \n '
