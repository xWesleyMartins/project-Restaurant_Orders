from src.models.dish import Dish
import csv
from src.models.ingredient import Ingredient


class MenuData:
    def __init__(self, source_path: str) -> None:
        self.items = self.read_csv(source_path)
        self.dishes = self.create_recipes()

    def read_csv(self, path: str):
        with open(path, "r") as csv_file:
            menu = list(csv.DictReader(csv_file))
            return menu

    def create_recipes(self):
        menu = {}

        for item in self.items:
            dish_name = item["dish"]
            dish_price = float(item["price"])
            ingredient_name = item["ingredient"]
            recipe_amount = int(item["recipe_amount"])

            dish = menu.setdefault(dish_name, Dish(dish_name, dish_price))
            ingredient = Ingredient(ingredient_name)

            dish.add_ingredient_dependency(ingredient, recipe_amount)

        return set(menu.values())
