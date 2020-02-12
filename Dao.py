import pymysql
import datetime

connection = pymysql.connect(
    host="localhost",
    user="root",
    password="toor2005",
    db="sql_testing",
    charset="utf8",
    cursorclass=pymysql.cursors.DictCursor
)


def get_all_food():
    food_list = list()
    try:
        with connection.cursor() as cursor:
            query = 'select * from food'
            cursor.execute(query)
            res = cursor.fetchall()
            for row in res:
                food_list.append(
                    (row["id"], row["name"], row["weight"], row["calories"], row["fat"], row["carbs"], row["water"]))
            return food_list
    except Exception as e:
        print("get_all_food")
        print(e)


def get_or_insert_food(food_name, weight, calories, protein, fat, carbs, water):
    query = f"select id from food where food.name ='{food_name}'"
    try:
        with connection.cursor() as cursor:
            cursor.execute(query)
            result = cursor.fetchone()
            if result:
                return result["id"]
            else:
                return insert_food(food_name, weight, calories, protein, fat, carbs, water)
            # if result == None
    except Exception as e:
        print("get_or_insert_name")
        print(e)


def insert_food(food_name, weight, calories, protein, fat, carbs, water):
    try:
        with connection.cursor() as cursor:
            query = 'INSERT into food(name, weight,calories,protein,fat,carbs,water) values (%s,%s,%s,%s,%s,%s,%s)'
            cursor.execute(query, args=[food_name, weight, calories, protein, fat, carbs, water])
            # connection.commit()
            return cursor.lastrowid
    except Exception as e:
        print("insert_owner")
        print(e)
        return e


# --   id INT PRIMARY KEY,
# --   name VARCHAR(30),
# --   age INT,
# --   height INT,
# --   weight INT,
# --   gender boolean
def insert_user(id, name, age, height, weight, gender):
    try:
        with connection.cursor() as cursor:
            query = 'INSERT into User(id,name,age,height,weight,gender) values (%s,%s,%s,%s,%s,%s)'
            cursor.execute(query, args=[id, name, age, height, weight, gender])
            connection.commit()
            return True
    except Exception as e:
        return False
        print("insert_user")
        print(e)
        return e


def insert_half_user(id, name, age, height, weight):
    try:
        with connection.cursor() as cursor:
            query = 'INSERT into User(id,name,age,height,weight) values (%s,%s,%s,%s,%s)'
            cursor.execute(query, args=[id, name, age, height, weight])
            connection.commit()
            return True
    except Exception as e:
        return False
        print("insert_half_user")
        print(e)
        return e


def update_half_user_gender(id, gender):
    try:
        with connection.cursor() as cursor:
            q = f"UPDATE User SET gender = {gender} where User.id = {id}"
            cursor.execute(q)
            connection.commit()
            return True
    except Exception as e:
        return False
        print("update_half_user_gender")
        print(e)
        return e


# --   user_id INT,
# --   target_weight INT,
# --   target_calories INT,
# --   target_protein FLOAT,
# --   target_fat FLOAT,
def insert_user_target(user_id, target_weight, target_calories, target_protein, target_fat):
    try:
        with connection.cursor() as cursor:
            query = 'INSERT into target_goals(user_id, target_weight, target_calories, target_protein, target_fat) ' \
                    'values (%s,%s,%s,%s,%s)'
            cursor.execute(query, args=[user_id, target_weight, target_calories, target_protein, target_fat])
            connection.commit()
    except Exception as e:
        print("insert_user_target")
        print(e)
        return e


# -- CREATE TABLE food_user (
# --   user_id INT,
# --   food_id INT,
# --   date_now DATE,
# --   amount INT,
# --   FOREIGN KEY (user_id) REFERENCES User(id),
# --   FOREIGN KEY (food_id) REFERENCES food(id),
# --   UNIQUE KEY(user_id,food_id,date_now)
# -- );


def insert_or_increment_food_user(user_id, food_id, date_now, amount):
    try:
        with connection.cursor() as cursor:
            query = 'INSERT into food_user(user_id, food_id, date_now, amount) values (%s,%s,%s,%s)'
            cursor.execute(query, args=[user_id, food_id, date_now, amount])
            connection.commit()
            return True
    except Exception as e:
        print("insert_or_increment_food_user")
        return False
        print(e)
        return e


def get_calories_for_user(user_id):
    query = f"select target_goals.target_calories from user, target_goals where user.id = target_goals.user_id and " \
            f"user.id = {user_id} "
    try:
        with connection.cursor() as cursor:
            cursor.execute(query)
            result = cursor.fetchone()
            return result
            # if result == None
    except Exception as e:
        print("get_or_insert_name")
        print(e)


def get_bmi(user_id):
    query = f"select height,weight from user where user.id = {user_id} "
    try:
        with connection.cursor() as cursor:
            cursor.execute(query)
            result = cursor.fetchone()
            return result
            # if result == None
    except Exception as e:
        print("get_or_insert_name")
        print(e)


def get_all_user_food(user_id):
    query = f"select f.name from food as f, food_user as fu, User as u where" \
            f" f.id = fu.food_id and fu.user_id = u.id and u.id =  {user_id} "
    try:
        with connection.cursor() as cursor:
            cursor.execute(query)
            result = cursor.fetchall()
            result_list = list()
            for i in result:
                result_list.append(i["name"])
            return result_list
            # if result == None
    except Exception as e:
        print("get_or_insert_name")
        print(e)


def get_target_protein(user_id):
    query = f"select target_goals.target_protein from user, target_goals where user.id = target_goals.user_id and " \
            f"user.id = {user_id} "
    try:
        with connection.cursor() as cursor:
            cursor.execute(query)
            result = cursor.fetchone()
            return result
            # if result == None
    except Exception as e:
        print("get_or_insert_name")
        print(e)


def get_today_food_progress(user_id):
    today_date = datetime.date.today()
    formated_today_date = today_date.strftime('%Y-%m-%d')
    # 2020-2-10
    query = f'''SELECT 
    sum(calories), 
    sum(protein), 
    sum(fat), 
    sum(carbs), 
    sum(water) 
    FROM food_user 
    JOIN food on food_id = food.id 
    where food_user.user_id={user_id} and date_now BETWEEN "{formated_today_date} 00:00:00" AND "{formated_today_date} 23:59:59"'''

    with connection.cursor() as cursor:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
