class Product:
    """Класс предоставляющий товар"""

    def __init__(self, name, description, price, quantity):
        """Инициализируем объект товаров"""
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
