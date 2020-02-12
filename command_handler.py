from functions import *
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
    print(len(arg))
    if len(arg) == 6:
        respond = func_init(command, user_info)
    return respond


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
    result = f"Your BMI is {bmi:.2f} and you are {bmi_status}"
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
    return f"{t.__str__()}\n Remaining calories are <i>{target_calories - calories}</i> \n"
