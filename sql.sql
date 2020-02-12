use sql_testing;


drop table if exists food_user;
drop table if exists target_goals;
drop table if exists food;
drop table if exists user;


CREATE TABLE User (
  id INT PRIMARY KEY,
  name VARCHAR(30),
  age INT,
  height INT,
  weight INT,
  gender boolean
);



-- insert into user(id,name,age,height,weight,gender) where

CREATE TABLE food (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(40),
  weight INT,
  calories INT,
  protein FLOAT,
  fat FLOAT,
  carbs FLOAT,
  water FLOAT
);

CREATE TABLE food_user (
  user_id INT,
  food_id INT,
  date_now DATE,
  amount INT,
  FOREIGN KEY (user_id) REFERENCES User(id),
  FOREIGN KEY (food_id) REFERENCES food(id),
  UNIQUE KEY(user_id,food_id,date_now)
);
CREATE TABLE target_goals (
  user_id INT,
  target_weight INT,
  target_calories INT,
  target_protein FLOAT,
  target_fat FLOAT,
  FOREIGN KEY (user_id) REFERENCES User(id),
  UNIQUE KEY(user_id)
);