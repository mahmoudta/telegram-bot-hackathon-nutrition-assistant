from functions import *
import connect_to_bot
from prettytable import PrettyTable


def handle_start(command, user_info):
    respond = "there should be no<arg> for start, try again"
    arg = command.split()
    if len(arg) == 1:
        respond = func_start(command)
    return respond


def handle_check(command, user_info):
    respond = "there should be  <sentence> for check, try again"
    arg = command.split()
    if len(arg) > 1:
        respond = func_check(command)
    return respond


def handle_consume(command, user_info):
    respond = "there should be  <sentence> for consume, try again"
    arg = command.split()
    print(len(arg))
    if len(arg) > 1:
        respond = func_cunsumed(command, user_info)
    return respond


def handle_init(command, user_info):
    respond = "there should be  <age> <height> <weight> <gender> <low|medium|high> for init, try again"
    arg = command.split()
    if len(arg) == 6:
        respond = func_init(command, user_info)
    return respond


def handle_atractive_insert(command, user_info):
    respond = "there should be  <age> <height> <weight> for insert command, try again"
    arg = command.split()
    if len(arg) == 4:
        respond = func_atractive_insert(command, user_info)

        custom_keyboard = [['F'], ['M']]
        title = "chose gender - male or female"
        connect_to_bot.add_botton(user_info['id'], custom_keyboard, title)
    return respond


def handle_gender_botton(chatid, text):
    gender_bool = gender_str_to_bool(text)
    Dao.update_half_user_gender(chatid, gender_bool)
    connect_to_bot.removepreviusmarkup(chatid)
    custom_keyboard = [[['low'], ['medium'], ['high']]]
    title = "chose daily exercise intensity - low or medium or high"
    connect_to_bot.add_botton(chatid, custom_keyboard, title)


def handle_exercise_botton(chatid, text):
    connect_to_bot.removepreviusmarkup(chatid)
    user_data = Dao.get_user_data(chatid)
    height = user_data["height"]
    weight = user_data["weight"]
    age = user_data["age"]
    gender_type = gender_bool_to_str(user_data["gender"])

    target_calories = calories_calculator.calculate_daily_calories(int(height), int(weight), int(age), gender_type,
                                                                   text)
    target_protein = calories_calculator.calculate_protein_intake(int(weight))

    target_result = Dao.insert_user_target(chatid, 0, target_calories, target_protein, 0)


def handle_help(command, user_info):
    respond = "there should be no <arg> for help, try again"
    arg = command.split()
    if len(arg) == 1:
        respond = func_help(command)
    return respond


def handle_get_calories(command, user_info):
    target_calories = func_get_calories(user_info)["target_calories"]
    result = f"Your daily intake of calories should be {target_calories} calories per day"
    return result


def handle_bmi(command, user_info):
    total_result = func_get_bmi(user_info)
    height = total_result["height"]
    weight = total_result["weight"]
    bmi = calories_calculator.calculate_bmi(weight, height)
    bmi_status = calories_calculator.get_adults_bmi_status(bmi)
    response = ""
    if bmi < 18.5:
        response = "C'mon you need to eat more!"
    elif bmi > 30:
        response = "You are heavy!\nEat and less and become healthy"
    else:
        response = "Good job! Keep up the good effort"
    result = f"Your BMI is {bmi:.2f} and you are {bmi_status}!\n{response}"
    return result


def handle_user_food(command, user_info):
    total_result = func_get_user_food(user_info)
    ate_today = "\n".join(total_result)
    print(ate_today)
    return ate_today


def handle_today_calories(command, user_info):
    calories = func_today_calories(user_info)
    target_calories = func_get_calories(user_info)["target_calories"]
    return f"You ate {calories} of your {target_calories} calories => <i><b>{calories / target_calories * 100:.2f}%</b></i> "


def handle_today_protein(command, user_info):
    target_protein = func_get_target_protein(user_info)["target_protein"]
    protein = func_today_protein(user_info)
    return f"You ate {protein:.2f} of {target_protein} gram of protein => <i><b>{protein / target_protein * 100:.2f}%</b></i> "


def get_percentage_calories(user_info):
    calories = func_today_calories(user_info)
    target_calories = func_get_calories(user_info)["target_calories"]
    calories_percentage = "{0:.2f}".format(calories / target_calories * 100)
    return calories_percentage


def handle_all_info(command, user_info):
    calories = func_today_calories(user_info)
    target_calories = func_get_calories(user_info)["target_calories"]
    protein = func_today_protein(user_info)
    target_protein = func_get_target_protein(user_info)["target_protein"]
    protein_nice = "{0:.2f}".format(protein)

    protein_percentage = "{0:.2f}".format(protein / target_protein * 100)
    calories_percentage = "{0:.2f}".format(calories / target_calories * 100)

    t = PrettyTable(['Type', 'Consumed', 'Target', "   %   "])
    t.add_row(['Calories', calories, target_calories, calories_percentage + "%"])
    t.add_row(['Protein', protein_nice, target_protein, protein_percentage + "%"])
    extra_info = ""
    if float(calories_percentage) > 100:
        extra_info = "You are over your limit!\nThink of burning some calories!\nMaybe go for a run?\n"
    elif float(calories_percentage) > 75:
        extra_info = "You are near your limit!\nThink carefully when eating!\nUse /check before consuming your food\n"
    elif float(protein_percentage) > 60:
        extra_info = "You are near your protein goal!\nGood job!\n"

    if target_calories < calories:
        extra_extra_info = f"Surplass of <i>{calories - target_calories} calories</i>"
    else:
        extra_extra_info = f"Remaining calories of <i>{calories - target_calories}</i>"

    return f"{extra_info}{t.__str__()}\n{extra_extra_info} \n"
