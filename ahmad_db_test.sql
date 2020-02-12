use sql_testing;

-- INSERT INTO user values (1, "ahmad", 24, 175, 75, 1);
-- INSERT INTO user values (2, "wasseem", 26, 185, 65, 1);


-- DELETE FROM food_user;
-- INSERT INTO food VALUES("apple", 182, 94, 0, 25, 25, 155);
-- INSERT INTO food VALUES("banana", 116, 102, 1, 0, 26, 86);


-- insert into food(name,weight,calories,protein,fat,carbs,water)
--  values('banana',1,10,0.5,0.4,10,20);

-- insert into food(name,weight,calories,protein,fat,carbs,water)
--  values('apple',115, 102, 1.2 ,0.3 ,26.4 ,86);

-- INSERT INTO food_user VALUES (1, 2, curdate(),1);
-- INSERT INTO food_user VALUES (1, 3, curdate(),1);

-- DELETE from food_user 
-- INSERT INTO food_user VALUES (1, 2, STR_TO_DATE("2020-2-5 6:55",'%Y-%m-%d %h:%i'),1);


SELECT * from food_user
JOIN food 
on food_id = food.id
where date_now BETWEEN "2020-2-5 00:00:00" AND "2020-2-12 23:59:59";



-- SELECT * FROM user;
-- SELECT * FROM food;
-- SELECT * FROM food_user;


-- ALTER TABLE food_user
-- MODIFY date_now DATETIME;


-- where date_now BETWEEN STR_TO_DATE("2020-2-5 00:00:00","%Y-%m-%d %h:%i:%s") AND STR_TO_DATE("2020-2-12 23:59:59","%Y-%m-%d %h:%i:%s");
