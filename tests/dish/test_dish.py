from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient
import pytest


# Req 2
def test_dish():
    dish1 = Dish("pizza", 50.0)
    dish2 = Dish("hamburguer", 5.0)
    assert dish1.name == "pizza"
    assert dish1.price == 50.0
    assert repr(dish1) == "Dish('pizza', R$50.00)"
    assert (dish1 == dish1) is True
    assert hash(dish1) == hash(dish1)
    assert hash(dish1) != hash(dish2)
    with pytest.raises(TypeError) as error:
        Dish("pizza", "50.0")
    assert str(error.value) == "Dish price must be float."
    with pytest.raises(ValueError) as error:
        Dish("pizza", -50.0)
    assert str(error.value) == "Dish price must be greater then zero."
    ingredient1 = Ingredient("farinha")
    dish1.add_ingredient_dependency(ingredient1, 1)
    assert dish1.recipe.get(ingredient1) == 1
    assert len(dish1.get_restrictions()) == 1
    assert dish1.get_ingredients() == {ingredient1}
