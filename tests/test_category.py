import pytest

from src.category import Category, Order
from src.product import Product


def test_init_1(category_1):
    assert category_1.name == "Смартфоны"
    assert category_1.description == "Смартфоны, как средство для получения дополнительных функций для удобства жизни"
    assert category_1.products == ["Samsung Galaxy S23 Ultra", "Iphone 15", "Xiaomi Redmi Note 11"]
    assert category_1.product_count == 3
    assert category_1.category_count == 1
    assert len(category_1.products) == 3


def test_add_product(all_products):
    product4 = Product("QLED", "Фоновая подсветка", 12, 7)
    all_products.add_product(product4)
    assert Category.product_count == 5


def test_str_for_categories(all_products):
    products = all_products
    assert str(products) == "Смартфоны, количество продуктов: 5 шт."


def test_str_for_categories_many(category_many):
    products = category_many
    assert str(products) == "Смартфоны, количество продуктов: 27 шт."


def test_category_iterator(category_iterator):
    iter(category_iterator)
    assert category_iterator.index == 0
    assert next(category_iterator).name == "Samsung"

    with pytest.raises(StopIteration):
        next(category_iterator)


def test_category_iterator_many(category_iterator_many):
    iter(category_iterator_many)
    assert category_iterator_many.index == 0
    assert next(category_iterator_many).name == "Samsung Galaxy S23 Ultra"
    assert next(category_iterator_many).name == "Iphone 15"
    assert next(category_iterator_many).name == "Xiaomi Redmi Note 11"

    with pytest.raises(StopIteration):
        next(category_iterator_many)


def test_add_product_error(all_products):

    with pytest.raises(TypeError):
        all_products.add_product(1) == 1


def test_category_abc(capsys):
    product_1 = Product("tomato", "red tomato from Azerbaijan", 150, 10)
    order = Order(product_1, 20)

    message = capsys.readouterr()
    assert message.out.strip() == "Product(tomato, red tomato from Azerbaijan, 150, 10)"
    assert repr(order) == "tomato, 150 руб. Остаток: 10 шт.: куплено 20шт. на сумму 3000 рублей"


def test_middle_price(category_many, category_without_products):
    assert category_many.middle_price() == 140333.33
    assert category_without_products.middle_price() == 0


def test_custom_exception(capsys, category_many):
    assert len(category_many.products) == 3


def test_custom_exception_2(capsys, category_many):
    with pytest.raises(ValueError) as excinfo:
        product_add = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 0)
        category_many.products = product_add
        assert str(excinfo.value) == "Товар с нулевым количеством не может быть добавлен"
