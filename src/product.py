class Product:
    """Класс предоставляющий товар"""

    def __init__(self, name, description, price, quantity):
        """Инициализируем объект товаров"""
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @property
    def price(self):
        """Геттер для приватного атрибута __price"""
        return self.__price

    @price.setter
    def price(self, new_price):
        """Сеттер для приватного атрибута __price с подтверждением понижения."""
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return

        if new_price < self.__price:
            confirmation = input(f"Цена понижается с {self.__price} до {new_price}. Подтвердить изменения? (y/n)")
            if confirmation.lower() == 'y':
                self.__price = new_price
                print("Цена успешно понижена.")
            else:
                print("Действия отменено. Цена осталась прежней.")
        else:
            self.__price = new_price

    @classmethod
    def new_product(cls, product_data, existing_products=None):
        """Создает новый объект класса Product, проверяя наличие похожего товара"""
        name = product_data.get('name')
        description = product_data.get('description')
        price = product_data.get('price')
        quantity = product_data.get('quantity')

        if not all([name, description, price, quantity is not None]):
            raise ValueError("Необходимо передать все поля для создания продукта")

        if existing_products:
            for product in existing_products:
                if product.name == name:
                    product.quantity += quantity
                    product.price = max(product.price, price)
                    return product

        return cls(name, description, price, quantity)

    def __str__(self):
        """Магический метод для строкового отображения"""
        return f'Название продукта: {self.name}, {self.__price} руб. Остаток: {self.quantity}'

    def __add__(self, other):
        """Магический метод дл я вывода продукции"""
        if not isinstance(other, Product):
            raise TypeError(f'Ожидался Product, а получен {type(other).__name__}')
        return self.price * other.quantity + other.price * other.quantity


if __name__ == "__main__":
    result1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    print(result1)
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("iPhone 14 Pro", "256GB, Space Black", 190000.0, 3)
    print(product1 + product2)
