import pytest


def test_lawngrass_init(grass_2):
    assert grass_2.name == "Газонная трава 2"
    assert grass_2.description == "Выносливая трава"
    assert grass_2.price == 450.0
    assert grass_2.quantity == 15
    assert grass_2.country == "США"
    assert grass_2.germination_period == "5 дней"
    assert grass_2.color == "Темно-зеленый"


def test_lawngrass_add(grass_1, grass_2):
    glass_sum = grass_1 + grass_2
    assert glass_sum == 16750.0


def test_lawngrass_add_error(smartphone_1, grass_2):

    with pytest.raises(TypeError):
        smartphone_1 + grass_2
