def compute(recipe: dict, pantry: dict) -> int:
    counters = []
    for ingredient, quantity in recipe.items():
        if ingredient in pantry:
            counters.append(
                int(pantry[ingredient]/quantity)
            )
        else:
            counters.append(0)
    return min(counters)


recipe1 = {"eggs": 2, "flour": 200, "milk": 100}
pantry1 = {"eggs": 12, "flour": 1000, "milk": 250, "apple": 2, "sugar": 850}

print(compute(recipe1, pantry1))