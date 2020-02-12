import Dao
import datetime

# --   user_id INT,
# --   target_weight INT,
# --   target_calories INT,
# --   target_protein FLOAT,
# --   target_fat FLOAT,

mock_food = {"name": "an apple", "weight": 182, "calories": 94, "total_fat": 0.3094, "carbs": 25.13, "water": 155,
             "protein": 0.4732}
mock_user = {"id": 123, "name": "Mahmoud", "age": 24, "height": 170, "weight": 100, "gender": True}
mock_target = {"id": 123, "target_weight": 90, "target_calories": 2700, "target_protein": 200, "target_fat": 50}
if __name__ == "__main__":
    # food_list = Dao.get_all_food()
    # print(food_list)

    result_insert_food_id = Dao.get_or_insert_food(mock_food["name"], mock_food["weight"], mock_food["calories"],
                                                   mock_food["protein"], mock_food["total_fat"], mock_food["carbs"],
                                                   mock_food["water"])
    print(result_insert_food_id)

    result_insert_user = Dao.insert_user(mock_user["id"], mock_user["name"], mock_user["age"], mock_user["height"],
                                         mock_user["weight"], mock_user["gender"])
    print(result_insert_user)

    # def insert_user_target(user_id, target_weight, target_calories, target_protein, target_fat):
    result_user_target = Dao.insert_user_target(mock_target["id"], mock_target["target_weight"],
                                                mock_target["target_calories"],
                                                mock_target["target_protein"], mock_target["target_fat"])
    print(result_user_target)

    now = datetime.date.today()
    now = now.strftime('%Y-%m-%d')

    result_insert_or_incr = Dao.insert_or_increment_food_user(mock_user["id"], result_insert_food_id, now, 1)
    print(result_insert_or_incr)
