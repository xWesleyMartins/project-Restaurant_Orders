import pytest
from src.models.ingredient import Ingredient
from src.models.dish import Dish  # noqa: F401, E261, E501


# Req 2
def test_dish():
    dish_name = "Churrasco"
    dish_price = 109.9
    dish_test = Dish(dish_name, dish_price)
    dish_hash = hash("Dish('{}', R${:.2f})".format(dish_name, dish_price))

    assert dish_test == Dish(dish_name, dish_price)
    assert dish_test.name == dish_name
    assert hash(dish_test) == dish_hash
    assert not dish_test.get_restrictions()

    assert repr(dish_test) == "Dish('Churrasco', R$109.90)"

    with pytest.raises(
        ValueError, match="Dish price must be greater then zero."
    ):
        Dish("carne", 0)

    ingredient_barbecue = Ingredient("Barbecue")
    dish_test.add_ingredient_dependency(ingredient_barbecue, 1)

    assert dish_test.recipe == {ingredient_barbecue: 1}
    assert {ingredient.name for ingredient in dish_test.get_ingredients()} == {
        "Barbecue"
    }
