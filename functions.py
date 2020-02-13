import datetime
import edamam_api
import Dao
import pretty_message
import calories_calculator


def func_start(command):
    return func_help(command)


def func_cunsumed(command, user_info):
    try:
        sentence = " ".join(command.split()[1:])
        nutrition = edamam_api.get_nutritions(sentence)
        if not nutrition:
            return "Wrong spelling or undefined unit"

        # food_id = Dao.get_or_insert_food(nutrition["name"], nutrition["weight"], nutrition["calories"],
        #                                  nutrition["protein"], nutrition["total_fat"], nutrition["carbs"],
        #                                  nutrition["water"])

        food_id = Dao.get_or_insert_food(nutrition["name"],nutrition["weight"],nutrition["calories"],nutrition["protein"],nutrition["total_fat"],nutrition["carbs"],nutrition["water"], nutrition['sugar'])

        now=datetime.date.today()
        now=now.strftime('%Y-%m-%d')

        results = Dao.insert_or_increment_food_user(user_info['id'], food_id, now, 1)
        if results:
            toreturn = pretty_message.check_pretty(nutrition)
        else:
            toreturn = "failed to add food"
    except:
        print("exception provoked from functhion.func_cunsumed")

    return toreturn


def gender_str_to_bool(str_gender):
    if str_gender == "M":
        return True
    elif str_gender == "F":
        return False


def gender_bool_to_str(gender):
    if gender:
        return "M"
    else:
        return "F"

def func_init(command, user_info):
    var_list = command.split()[1:]
    age = var_list[0]
    height = var_list[1]
    weight = var_list[2]
    gender = var_list[3]
    gender_bool=gender_str_to_bool(gender)
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
        target_protein = calories_calculator.calculate_protein_intake(int(weight))
        target_result = Dao.insert_user_target(user_info['id'], 0, target_calories, target_protein, 0)
        response = "You got inserted"
    else:
        response = "There was an issue"
    return response


def func_atractive_insert(command, user_info):
    var_list = command.split()[1:]
    age = var_list[0]
    height = var_list[1]
    weight = var_list[2]
    insert_result = Dao.insert_half_user(user_info['id'], user_info['username'], age, height, weight)
    if insert_result:

        response = " "
    else:
        response = "failed to insert"
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


def func_get_bmi(user_info):
    try:
        return Dao.get_bmi(user_info["id"])
    except:
        print("exception provoked from function.func_get_calories")


def func_today_calories(user_info):
    try:
        data_list = Dao.get_today_food_progress(user_info["id"])
        print(data_list)
        result = data_list[0]["sum(calories)"]
    except IndexError:
        result = "You ate nothing"

    return result


def func_today_protein(user_info):
    try:
        data_list = Dao.get_today_food_progress(user_info["id"])
        print(data_list)
        result = data_list[0]["sum(protein)"]
    except IndexError:
        result = "You ate nothing"

    return result


def func_get_user_food(user_info):
    try:
        return Dao.get_all_user_food(user_info["id"])
    except:
        print("exception provoked from function.func_get_user_food")


def func_get_target_protein(user_info):
    try:
        return Dao.get_target_protein(user_info["id"])
    except:
        print("exception provoked from function.func_get_target_protein")


def func_help(command):
    return "commands list :\n" \
           "/insert insert you info in order with space between them as age height weight " \
           "after that you will be asked about the gender and the daily exercise intercity\n" \
           "/check to check nutrition in food\n" \
           "/calories, get remaining calories and your current daily calories" \
           "/consume report a food consumption to us \n" \
           "/bmi return your bmi report\n" \
           "/ate return the food you ate\n"\
           "/todaycal return your calories for today\n" \
           "/todayprot return your protein for today\n" \
           "/today return a table with everything\n" \
           "/help - get this command list"


