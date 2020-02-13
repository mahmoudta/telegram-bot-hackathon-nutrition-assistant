def check_pretty(json):
    name = json["name"]
    calories = json["calories"]
    total_fat = json["total_fat"]
    carbs = json["carbs"]
    protein = json["protein"]
    water = json["water"]
    weight = json["weight"]
    sugar = json["sugar"]
    return f"{name} has  {weight} weight\n {calories} calories,\n {total_fat:.3f} fats,\n" \
           f" {carbs:.3f} carbs,\n {protein:.3f} proteins,\n {water:.3f} water \n {sugar:.3f} sugar \n"
