import pytest


def test_smartphone_init(smartphone_2):
    assert smartphone_2.name == "Iphone 15"
    assert smartphone_2.description == "512GB, Gray space"
    assert smartphone_2.price == 210000.0
    assert smartphone_2.quantity == 8
    assert smartphone_2.efficiency == 98.2
    assert smartphone_2.model == "15"
    assert smartphone_2.memory == 512
    assert smartphone_2.color == "Gray space"


def test_smartphone_add(smartphone_1, smartphone_2):
    smartphone_sum = smartphone_1 + smartphone_2
    assert smartphone_sum == 2114000.0


def test_smartphone_add_error(smartphone_1, grass_2):

    with pytest.raises(TypeError):
        smartphone_1 + 1.5
