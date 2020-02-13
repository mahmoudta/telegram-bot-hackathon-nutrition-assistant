# NutriBot

Project name is `Diet tracker` it allows `someone who wants to maintain or reach his goal wait` to `monitor his daily consumption and alert him regarding his left calories`.

![Template GIF](https://media.giphy.com/media/H8E1H1H63TDjsPutZY/giphy.gif)

<!-- Additional line of information text about what the project does. Your introduction should be around 2 or 3 sentences. Don't go overboard, people won't read it. -->

## Prerequisites

Before you begin, ensure you have met the following requirements:
<!--- These are just example requirements. Add, duplicate or remove as required --->
* You have installed `Python 3.6+`
* You have installed `MySQL 5.5+`

## Dependencies
```
requests==2.22.0
flask==1.1.1
python-telegram-bot==12.4.2
prettytable==0.7.2
pymysql==0.9.3
```

## Installing NutriBot

To find NutriBot search in Telegram:
```
@nutrition_assistantBot
```

## Using NutriBot

To use NutriBot, follow these steps:

```
/insert <age> <height> <weight>.
/check <sentence>
/consume <sentence>
/todaycal
/todayprot
```


## The Math
1. Calorie Calculator uses the `Revised Harris-Benedict Equation` to approximate the daily required calories.
The equation works on 3 levels of excercise intensity.
2. BMI Calculator assumes 2.2g of protein per Kg of weight.

## External API
```
https://developer.edamam.com
```



## Contributors

* [@AhmadMinwer](https://github.com/AhmadMinwer) 📖
* [@WasseemB](https://github.com/WasseemB) 🐛
* [@MahmoudTa](https://github.com/MahmoudTa) 🐛