from product import Product


class Category:
    """Класс, предоставляющий категории товаров"""
    total_categories = 0
    total_products = 0

    def __init__(self, name, description, products=None):
        """Инициализируем объект категории"""
        self.name = name
        self.description = description
        self.__products = products if products is not None else []

    def add_products(self, product):
        if isinstance(product, Product):
            self.__products.append(product)
            Category.total_products += product.quantity
        else:
            raise ValueError("Можно добовлять только объект класса Product")

    def get_products(self):
        return self.__products.copy()

    @classmethod
    def add_category(cls):
        Category.total_categories += 1

    @property
    def products_info(self):
        """Возвращает информацию о продуктах в формате строк."""
        products_strings = []
        for product in self.__products:
            products_strings.append(f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.")
        return products_strings


# Category.total_categories += 1
# Category.total_products += len(__products)
