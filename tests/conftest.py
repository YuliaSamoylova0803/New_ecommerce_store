import pytest

from src.category import Category
from src.product import Product


@pytest.fixture
def product_1():
    return Product(
        name="Samsung Galaxy S23 Ultra", description="256GB, Серый цвет, 200MP камера", price=180000.0, quantity=5
    )


@pytest.fixture
def product_2():
    return Product(name="Iphone 15", description="512GB, Gray space", price=210000.0, quantity=8)


@pytest.fixture
def product_3():
    return Product(name="Xiaomi Redmi Note 11", description="1024GB, Синий", price=31000.0, quantity=14)


@pytest.fixture
def product_4():
    return Product(name='55" QLED 4K', description="Фоновая подсветка", price=123000.0, quantity=7)


@pytest.fixture
def category_1():
    return Category(
        name="Смартфоны",
        description="Смартфоны, как средство для получения дополнительных функций для удобства жизни",
        products=["Samsung Galaxy S23 Ultra", "Iphone 15", "Xiaomi Redmi Note 11"],
    )


@pytest.fixture
def data_test():
    return [
        {
            "name": "Смартфоны",
            "description": "Смартфоны, как средство для получения дополнительных функций для удобства жизни",
            "products": [
                {
                    "name": "Samsung Galaxy C23 Ultra",
                    "description": "256GB, Серый цвет, 200MP камера",
                    "price": 180000.0,
                    "quantity": 5,
                },
                {"name": "Iphone 15", "description": "512GB, Gray space", "price": 210000.0, "quantity": 8},
                {"name": "Xiaomi Redmi Note 11", "description": "1024GB, Синий", "price": 31000.0, "quantity": 14},
            ],
        },
        {
            "name": "Телевизоры",
            "description": "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом",
            "products": [
                {"name": '55" QLED 4K', "description": "Фоновая подсветка", "price": 123000.0, "quantity": 7}
            ],
        },
    ]


@pytest.fixture
def dict_test():
    return {"name": "Iphone 15", "description": "512GB, Gray space", "price": 210000.0, "quantity": 8}


@pytest.fixture
def new_price():
    return 125000


@pytest.fixture
def all_products():
    product1 = Product("Samsung", "Серый цвет", 18, 5)

    category1 = Category("Смартфоны", "Смартфоны, как средство", [product1])
    return category1


@pytest.fixture
def product_new_product():
    return Product("Iphone 15", "512GB, Gray space", 120000.0, 8)
