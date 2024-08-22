import csv
from src.models.dish import Dish
from src.models.ingredient import Ingredient


class MenuData:
    def __init__(self, source_path):
        self.dishes = set()
        self._load_data(source_path)

    def _load_data(self, source_path):
        with open(source_path, mode="r", newline="", encoding="utf-8") as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                dish_name, price, ingredient_name, quantity = row
                price = float(price)
                quantity = int(quantity)
                dish = next(
                    (d for d in self.dishes if d.name == dish_name), None
                )
                if dish is None:
                    dish = Dish(dish_name, price)
                    self.dishes.add(dish)
                ingredient = next(
                    (
                        i
                        for i in dish.get_ingredients()
                        if i.name == ingredient_name
                    ),
                    None,
                )
                if ingredient is None:
                    ingredient = Ingredient(ingredient_name)

                dish.add_ingredient_dependency(ingredient, quantity)
