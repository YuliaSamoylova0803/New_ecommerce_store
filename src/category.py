from abc import ABC, abstractmethod

from src.product import Product


class Abstract(ABC):

    @abstractmethod
    def __repr__(self):
        pass


class Order(Abstract):

    def __init__(self, product, purchased_product):
        self.product = product
        self.purchased_product = purchased_product
        self.total_cost = self.purchased_product * int(product.price)

    def __repr__(self):
        return f"{self.product}: куплено {self.purchased_product}шт. на сумму {self.total_cost} рублей"


class Category(Abstract):
    """Класс для представления продуктов"""

    # Атрибуты класса Category

    name: str
    description: str
    products: list
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products=None):
        """Метод для инициализации экземпляра класса. Задаем значения атрибутам экземпляра."""
        self.name = name
        self.description = description
        self.__products = products if products else []
        Category.category_count += 1
        Category.product_count += len(self.products) if products else 0

    def __repr__(self):
        return f"{self.__class__.__name__} - {self.name}, {self.description}, продукты в наличие: {self.__products}"

    def __str__(self):
        total_products = 0
        for product in self.__products:
            total_products += product.quantity
        return f"{self.name}, количество продуктов: {total_products} шт."

    def add_product(self, new_product):
        if isinstance(new_product, Product):

            self.__products.append(new_product)
            Category.product_count += 1
        else:
            raise TypeError

    @property
    def products(self):
        product_str = ""
        for product in self.__products:
            product_str += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
        return product_str

    @property
    def products(self) -> list:
        return self.__products


# if __name__ == "__main__":
#     product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
#     ord_1 = Order(product2, 10)
#     print(ord_1)
#
#     product_1 = Product("tomato", "red tomato from Azerbaijan", 150, 10)
#     order = Order(product_1, 20)
#     print(order)
# message = capsys.readouterr()
# assert message.out.strip().split("\n")[-1] == "Product('tomato', 'red tomato from Azerbaijan', 150, 10)"
# assert repr(order) == "tomato, куплено - 20 штук, итоговая стоимость - 3000 рублей""Samsung Galaxy S23 Ultra"
#     product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
#     product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
#     product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
#
#     category1 = Category(
#         "Смартфоны",
#         "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
#         [product1, product2, product3]
#     )
#     cat_2 = Category(
#         name="Смартфоны",
#         description="Смартфоны, как средство для получения дополнительных функций для удобства жизни",
#         products=["Samsung Galaxy S23 Ultra", "Iphone 15", "Xiaomi Redmi Note 11"],
#     )
#     print(cat_2)
#     # print(category1.products)
#     # product4 = Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7)
#     # category1.add_product(product4)
#     # print(category1.products)
#     # print(category1.product_count)
#     # product_1 = Product("tomato", "red tomato from Azerbaijan", 150, 10)
#     # category_1 = Category("products", "products for salad", [])
#     # category_1.add_product(product_1)
#     print(category1)
