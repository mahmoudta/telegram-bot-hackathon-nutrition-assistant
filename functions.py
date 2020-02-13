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


        food_id = Dao.get_or_insert_food(nutrition["name"],nutrition["weight"],nutrition["calories"],nutrition["protein"],nutrition["total_fat"],nutrition["carbs"],nutrition["water"], nutrition['sugar'])

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
    # def calculate_daily_calories(height, weight, age, gender, exercise):
    if insert_result:
        target_calories = calories_calculator.calculate_daily_calories(int(height), int(weight), int(age), gender,
                                                                       exercise)
        print(target_calories)
        target_result = Dao.insert_user_target(user_info['id'], 0, target_calories, 0, 0)
        print(target_calories)
        print(target_result)
        response = "You got inserted"
    else:
        response = "There was an issue"
    return response


def func_check(command):
    try:
        sentence = " ".join(command.split()[1:])
        toreturn = edamam_api.get_nutritions(sentence)
        toreturn = pretty_message.check_pretty(toreturn)
    except:
        print("exception provoked from functhion.func_check")

    return toreturn


def func_get_calories(user_info):
    try:
        return Dao.get_calories_for_user(user_info["id"])
    except:
        print("exception provoked from function.func_get_calories")


def func_help(command):
    return 'commands list :\n ' \
           '/start  to initi details.\n ' \
           '/insert insert your data as followd <age> <height> <weight> <gender> <exercise> gender exercise should be (M|F) exercise should be (low|medium|high).\n ' \
           '/check  to check nutrethion in food.\n ' \
           '/calories  get you recommended remainig calories for the day.\n ' \
           '/consume  inform us of a consumed food to update.\n ' \
           '/bmi  inform us of a consumed food .\n ' \
           '/help - to get to this* command list. \n '