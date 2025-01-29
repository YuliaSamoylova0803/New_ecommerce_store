from abc import ABC, abstractmethod


class BaseProduct(ABC):

    @abstractmethod
    def __add__(self, other):
        pass


class ProductMixin:

    def __init__(self):
        print(repr(self))

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name}, {self.description}, {self.price}, {self.quantity})"


class Product(BaseProduct, ProductMixin):
    """Класс для представления продуктов"""

    # Атрибуты класса Product

    name: str  # название
    description: str  # описание
    price: float  # цена
    quantity: str  # количество в наличии

    def __init__(self, name, description, price, quantity):
        """Метод для инициализации экземпляра класса. Задаем значения атрибутам экземпляра."""

        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        super().__init__()

    def __str__(self):
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if type(other) is self.__class__:
            return self.__price * self.quantity + other.__price * other.quantity
        raise TypeError

    @classmethod
    def new_product(cls, dict_with_params: dict):
        """Метод, который принимает параметры в виде словаря, а возвращает объект класса"""
        name = dict_with_params.get("name")
        description = dict_with_params.get("description")
        price = dict_with_params.get("price")
        quantity = dict_with_params.get("quantity")

        return cls(name, description, price, quantity)

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        elif new_price < self.__price:
            answer = input(f"Цена понижается с {self.__price} по {new_price}. Подтверждаете? (y/n)")
            if answer == "y":
                self.__price = new_price
        else:
            self.__price = new_price


# if __name__ == "__main__":
#
#
#     new_product = Product.new_product(
#         {"name": "Samsung Galaxy S23 Ultra", "description": "256GB, Серый цвет, 200MP камера", "price": 180000.0,
#          "quantity": 5})
#     print(new_product.name)
#     print(new_product.description)
#     print(new_product.price)
#     print(new_product.quantity)
#
#     new_product.price = 800
#     print(new_product.price)
