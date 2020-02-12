import requests
from config import edamam_app_id, edamam_app_key
from config import edamam_food_text_analysis_api_url as api_url


# formated_api_url = api_url.format(edamam_app_id,edamam_app_key)
# res = requests.get(formated_api_url)
# json_res = res.json()
# total_cal = json_res['totalNutrientsKCal']['ENERC_KCAL']

def get_nutrition_json(item):
    formated_api_url = api_url.format(edamam_app_id, edamam_app_key, item)
    res = requests.get(formated_api_url)
    json_nutrition = res.json()
    json_nutrition['name'] = item
    if json_nutrition['totalWeight'] == 0:
        return None
    else:
        return json_nutrition


def get_name(json_nutrition):
    return json_nutrition['name']


def get_total_cal(json_nutrition):
    return json_nutrition['calories']


def get_total_fat(json_nutrition):
    return json_nutrition['totalNutrients']['FAT']['quantity']


def get_carbs(json_nutrition):
    return json_nutrition['totalNutrients']['CHOCDF']['quantity']


def get_protein(json_nutrition):
    return json_nutrition['totalNutrients']['PROCNT']['quantity']


# the unhealthy fat
def get_saturated_fat(json_nutrition):
    try:
        return json_nutrition['totalNutrients']['FASAT']['quantity']
    except KeyError:
        return 0


# the healthy fat
def get_unsaturated_fat(json_nutrition):
    return get_total_fat(json_nutrition) - get_saturated_fat(json_nutrition)


def get_sugars(json_nutrition):
    return json_nutrition['totalNutrients']['SUGAR']['quantity']


def get_water(json_nutrition):
    return json_nutrition['totalNutrients']['WATER']['quantity']


def get_labels(json_nutrition):
    return json_nutrition['healthLabels']


def get_weight(json_nutrition):
    return json_nutrition['totalWeight']


def get_nutritions(food_text):
    nutrition_json = get_nutrition_json(food_text)
    nutritions = {
        'name': get_name(nutrition_json),
        'calories': get_total_cal(nutrition_json),
        'total_fat': get_total_fat(nutrition_json),
        'saturated_fat': get_saturated_fat(nutrition_json),
        'unsaturated_fat': get_unsaturated_fat(nutrition_json),
        'carbs': get_carbs(nutrition_json),
        'protein': get_protein(nutrition_json),
        'sugars': get_sugars(nutrition_json),
        'water': get_water(nutrition_json),
        'weight': get_weight(nutrition_json),
        'labels': get_labels(nutrition_json)
    }
    return nutritions


if __name__ == "__main__":
    nutritions = get_nutrition_json('apple')
    print('name: ', nutritions['name'])
    print('calories: ', get_total_cal(nutritions))
    print('total fat: ', get_total_fat(nutritions))
    print('saturated fat: ', get_saturated_fat(nutritions))
    print('unsaturated fat: ', get_unsaturated_fat(nutritions))
    print('carbs: ', get_carbs(nutritions))
    print('protein: ', get_protein(nutritions))
    print('sugars: ', get_sugars(nutritions))
    print('water: ', get_water(nutritions))
    print('weight: ', get_weight(nutritions))
    print('labels: ', get_labels(nutritions))
    print(get_nutritions('3 apple'))
