from src.models.ingredient import Ingredient, Restriction


def test_ingredient():
    ingredient1 = Ingredient("farinha")
    ingredient2 = Ingredient("queijo mussarela")

    assert ingredient1.name == "farinha"
    assert ingredient2.name == "queijo mussarela"

    assert ingredient1.restrictions == {Restriction.GLUTEN}
    assert ingredient2.restrictions == {
        Restriction.LACTOSE,
        Restriction.ANIMAL_DERIVED,
    }
    assert ingredient1.__hash__() == hash("farinha")
    assert ingredient2.__hash__() == hash("queijo mussarela")
    assert ingredient1.__hash__() != ingredient2.__hash__()
    assert (ingredient1 == ingredient2) is False
    assert (ingredient1 != ingredient2) is True
    assert (ingredient1 == ingredient1) is True

    assert repr(ingredient1) == "Ingredient('farinha')"
