from math import sqrt


def calculate_daily_calories(height, weight, age, gender, exercise):
    ''' height: 'cm'\n weight: 'kg'\n age: 'year'\n gender:['M', 'F']'''

    exercise_lifestyle = {
        'low': 1.25,
        'medium': 1.575,
        'high': 1.85
    }

    if gender == 'M':
        return (13.397 * weight + 4.799 * height - 5.677 * age + 88.362) * exercise_lifestyle[exercise]
    elif gender == 'F':
        return (9.247 * weight + 3.098 * height - 4.330 * age + 447.593) * exercise_lifestyle[exercise]
    else:
        return None


def calculate_bmi(weight, height):
    ''' weight(kg)\n height(cm)\n '''
    return weight / (height * height) * (10000)


def get_adults_bmi_status(bmi):
    if bmi < 16:
        return 'Severe Thinness'
    elif bmi < 17:
        return 'Moderate Thinness'
    elif bmi < 18.5:
        return 'Mild Thinness'
    elif bmi < 25:
        return 'Normal'
    elif bmi < 30:
        return 'Overweight'
    elif bmi < 35:
        return 'Obese Class I'
    elif bmi < 40:
        return 'Obese Class II'
    else:
        return 'Obese Class III'


def get_expected_calories_during_duration(current_weight, target_weight, duration, height, age, gender, exercise):
    weight_difference = target_weight - current_weight
    calorie_difference = weight_difference * 2.20462 * 3500
    calorie_difference_per_day = calorie_difference / duration
    normal_calories_per_day = calculate_daily_calories(height, current_weight, age, gender, exercise)
    target_calories_per_day = normal_calories_per_day + calorie_difference_per_day

    if target_calories_per_day > 1500:
        return target_calories_per_day
    else:
        return "unreasonable"


if __name__ == "__main__":
    print(calculate_daily_calories(185, 80, 24, 'M', 'low'))
    bmi = calculate_bmi(80, 185)
    print(get_adults_bmi_status(bmi))
    print(get_expected_calories_during_duration(75, 70, 50, 175, 25, 'M', 'low'))
