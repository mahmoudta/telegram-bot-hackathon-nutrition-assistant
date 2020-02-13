
from articles import data as articles

def normal_protein_need_per_day(weight, exercise_amount):
    exercise_amount_list ={
        'low': 0.8,
        'medium': 1.4,
        'high': 2.0
    }
    return weight * exercise_amount_list[exercise_amount]


def normal_carbs_need_per_day(weight, exercise_amount):
    exercise_amount_list ={
        'low': 7.7,
        'medium': 8.8,
        'high': 9.9
    }
    return weight * exercise_amount_list[exercise_amount] 

def get_normal_fat_need_per_day(total_calories_per_day):
    return (total_calories_per_day * 0.27)/9

def get_protein_consumption_lable(weight, exercise_amount, actual_protein_consumption_per_day):
    normal_protein_consumption = normal_protein_need_per_day(weight, exercise_amount)
    max_normal_protein_consumption = (normal_protein_consumption + normal_protein_consumption* 0.2 ) 
    min_normal_protein_consumption = (normal_protein_consumption - normal_protein_consumption* 0.2 ) 
    if actual_protein_consumption_per_day > max_normal_protein_consumption:
        return 'high_protein'
    if actual_protein_consumption_per_day < min_normal_protein_consumption:
        return 'low_protein'
    else: 'normal_protein'


def get_carbs_consumption_lable(weight, exercise_amount, actual_carbs_consumption_per_day):
    normal_carbs_consumption = normal_carbs_need_per_day(weight, exercise_amount)
    max_normal_carbs_consumption = (normal_carbs_consumption + normal_carbs_consumption* 0.2 ) 
    min_normal_carbs_consumption = (normal_carbs_consumption - normal_carbs_consumption* 0.2 ) 
    if actual_carbs_consumption_per_day > max_normal_carbs_consumption:
        return 'high_carbs'
    if actual_carbs_consumption_per_day < min_normal_carbs_consumption:
        return 'low_carbs'
    else: 'normal_carbs'

def get_fat_consumption_lable(total_calories_per_day, actual_fat_consumption_per_day):
    normal_fat_consumption = get_normal_fat_need_per_day(total_calories_per_day)
    max_normal_fat_consumption = (normal_fat_consumption + normal_fat_consumption* 0.2 ) 
    min_normal_fat_consumption = (normal_fat_consumption - normal_fat_consumption* 0.2 ) 
    if actual_fat_consumption_per_day > max_normal_fat_consumption:
        return 'high_fat'
    if actual_fat_consumption_per_day < min_normal_fat_consumption:
        return 'low_fat'
    else: return 'normal_fat'


def get_match_articles(user_lables):
    user_lables.append('all')
    
    matched_articles = []
    flag_found = False

    for article in articles:
        flag_found = False
        for lable in article['labels']:
            for user_lable in user_lables:
                if user_lable == lable:
                    matched_articles.append(article)
                    flag_found = True
                    break
            if flag_found:
                break
    
    return matched_articles



if __name__ == "__main__":
    print(get_match_articles(['low_protein']))

