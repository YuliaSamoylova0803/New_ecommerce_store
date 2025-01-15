from itertools import product


class Product:
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


    @classmethod
    def new_product(cls, dict_with_params: dict):
        """Метод, который принимает параметры в виде словаря, а возвращает объект класса """
        name = dict_with_params.get("name")
        description = dict_with_params.get("description")
        price = dict_with_params.get("price")
        quantity = dict_with_params.get("quantity")

        return cls(name, description, price, quantity)


    @property
    def price(self):
        return self.__price


    @price.setter
    def price(self, new_price: float):
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return
        self.__price = new_price


if __name__ == "__main__":
    new_product = Product.new_product(
        {"name": "Samsung Galaxy S23 Ultra", "description": "256GB, Серый цвет, 200MP камера", "price": 180000.0,
         "quantity": 5})
    print(new_product.name)
    print(new_product.description)
    print(new_product.price)
    print(new_product.quantity)

    new_product.price = 800
    print(new_product.price)

    new_product.price = -100
    print(new_product.price)
    new_product.price = 0
    print(new_product.price)


