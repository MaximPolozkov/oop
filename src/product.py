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
