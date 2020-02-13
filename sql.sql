use sql_testing;


-- drop table if exists food_user;
-- drop table if exists target_goals;
-- drop table if exists food;
-- drop table if exists user;


-- CREATE TABLE User (
--   id INT PRIMARY KEY,
--   name VARCHAR(30),
--   age INT,
--   height INT,
--   weight INT,
--   gender boolean
-- );



-- -- insert into user(id,name,age,height,weight,gender) where

-- CREATE TABLE food (
--   id INT AUTO_INCREMENT PRIMARY KEY,
--   name VARCHAR(40),
--   weight INT,
--   calories INT,
--   protein FLOAT,
--   fat FLOAT,
--   carbs FLOAT,
--   water FLOAT
-- );

-- CREATE TABLE food_user (
--   user_id INT,
--   food_id INT,
--   date_now DATE,
--   amount INT,
--   FOREIGN KEY (user_id) REFERENCES User(id),
--   FOREIGN KEY (food_id) REFERENCES food(id),
--   UNIQUE KEY(user_id,food_id)
-- );
-- CREATE TABLE target_goals (
--   user_id INT,
--   target_weight INT,
--   target_calories INT,
--   target_protein FLOAT,
--   target_fat FLOAT,
--   FOREIGN KEY (user_id) REFERENCES User(id),
--   UNIQUE KEY(user_id)
-- );

-- insert into food(name,weight,calories,protein,fat,carbs,water)
--  values('banana',1,10,0.5,0.4,10,20);


-- insert into

-- select * from food;

-- select * from food_user;

-- select * from
--  user, target_goals where user.id = target_goals.user_id;

-- select * from target_goals;
-- select * from food;
-- ALTER TABLE food_user
-- MODIFY date_now DATETIME;

-- select * from food_user;
-- SELECT food_user.user_id, sum(calories), sum(protein), sum(fat), sum(carbs), sum(water) from food_user
-- JOIN food
-- on food_id = food.id
-- where food_user.user_id=22770211 and date_now BETWEEN "2020-2-12 00:00:00" AND "2020-2-12 23:59:59";

-- INSERT INTO food_user VALUES (22770211, 1, curdate(),1);
-- INSERT INTO food_user VALUES (22770211, 2, curdate(),1);

-- INSERT INTO food_user VALUES (22770211, 1, STR_TO_DATE("2020-2-12 6:55",'%Y-%m-%d %h:%i'),1);
-- INSERT INTO food_user VALUES (22770211, 2, STR_TO_DATE("2020-2-12 6:55",'%Y-%m-%d %h:%i'),1);

-- UPDATE target_goals SET target_protein = 120;
-- select * from target_goals;