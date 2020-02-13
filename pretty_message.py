def check_pretty(json):
    name = json["name"]
    calories = json["calories"]
    total_fat = json["total_fat"]
    carbs = json["carbs"]
    protein = json["protein"]
    water = json["water"]
    weight = json["weight"]
    if int(calories) > 300:
        return f"Seriously?? Take care of yourself!!!\n" \
               f"A {name} weighs {weight:.2f} gm\n{calories} calories\n{total_fat:.3f} fats\n" \
               f"{carbs:.3f} carbs\n{protein:.3f}proteins\n{water:.3f} water\n" \
               f"Take care of yourself more!!"
    elif int(protein) > 9:
        return f"Good protein intake!\n" \
               f"A {name} weighs {weight:.2f} gm\n{calories} calories\n{total_fat:.3f} fats\n" \
               f"{carbs:.3f} carbs\n{protein:.3f}proteins\n{water:.3f} water\n" \
               f"Keep going!"
    else:
        return f"Good choice!\n" \
               f"A {name} weighs {weight:.2f} gm\n{calories} calories\n{total_fat:.3f} fats\n" \
               f"{carbs:.3f} carbs\n{protein:.3f}proteins\n{water:.3f} water\n"
        # return f"{name} has {weight:.2f} weight\n {calories} calories,\n {total_fat:.3f} fats,\n" \
        #        f" {carbs:.3f} carbs,\n {protein:.3f} proteins,\n {water:.3f} water \n"
