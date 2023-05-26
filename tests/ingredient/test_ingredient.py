from src.models.ingredient import (
    Ingredient,
    Restriction,
)  # noqa: F401, E261, E501


# Req 1
def test_ingredient():
    ingredient_margarina = Ingredient("margarina")
    ingredient_margarina2 = Ingredient("margarina")
    ingredient_cafe = Ingredient("cafe")
    ingredient_farinha = Ingredient("farinha")

    assert hash(ingredient_margarina) == hash(ingredient_margarina2)
    assert hash(ingredient_cafe) != hash(ingredient_margarina)
    assert ingredient_margarina.__eq__(ingredient_margarina) is True
    assert ingredient_margarina.__eq__(ingredient_cafe) is False
    assert ingredient_margarina.name == "margarina"
    assert repr(ingredient_margarina) == "Ingredient('margarina')"

    GLUTEN_RESTRICTION = {Restriction.GLUTEN}
    assert ingredient_farinha.restrictions == GLUTEN_RESTRICTION
