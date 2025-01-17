from src.category import Category
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
