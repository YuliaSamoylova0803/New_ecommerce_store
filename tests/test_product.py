from unittest.mock import patch

from src.product import Product


def test_init_1(product_1):
    assert product_1.name == "Samsung Galaxy S23 Ultra"
    assert product_1.description == "256GB, Серый цвет, 200MP камера"
    assert product_1.price == 180000.0
    assert product_1.quantity == 5


def test_init_2(product_2):
    assert product_2.name == "Iphone 15"
    assert product_2.description == "512GB, Gray space"
    assert product_2.price == 210000.0
    assert product_2.quantity == 8


def test_init_3(product_3):
    assert product_3.name == "Xiaomi Redmi Note 11"
    assert product_3.description == "1024GB, Синий"
    assert product_3.price == 31000.0
    assert product_3.quantity == 14


def test_init_4(product_4):
    assert product_4.name == '55" QLED 4K'
    assert product_4.description == "Фоновая подсветка"
    assert product_4.price == 123000.0
    assert product_4.quantity == 7


def test_new_product_method(dict_test):
    assert str(Product.new_product(dict_test)) == "Iphone 15, 210000.0 руб. Остаток: 8 шт."


def test_str_method(product_3):
    product1 = product_3
    assert str(product1) == "Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт."


@patch("src.product.input")
def test_product_price_setter(mock_input):
    mock_input.return_value = "Цена понижается с 180000.0 по 800. Подтверждаете? (y/n)"


def test_product_str(product_3):
    assert str(product_3) == "Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт."


def test_product_add1(product_2, product_3):
    assert product_2 + product_3 == 2114000.0
