class Product:
    """Класс для представления продуктов"""
    # Атрибуты класса Product

    name: str          # название
    description: str   # описание
    price: float       # цена
    quantity: str      # количество в наличии

    def __init__(self, name, description, price, quantity):
        """Метод для инициализации экземпляра класса. Задаем значения атрибутам экземпляра."""
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
