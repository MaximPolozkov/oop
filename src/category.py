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

    def add_products(self, production):
        if isinstance(production, Product):
            self.__products.append(production)
            Category.total_products += production.quantity
        else:
            raise ValueError("Можно добавлять только объект класса Product")

    def get_products(self):
        """Возвращаем копию списка продуктов"""
        return self.__products.copy()

    @classmethod
    def add_category(cls):
        """Увеличиваем счетчик категорий на 1"""
        Category.total_categories += 1

    @property
    def products_info(self):
        """Возвращает информацию о продуктах в формате строк."""
        products_strings = []
        for product in self.__products:
            products_strings.append(f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.")
        return products_strings

    @property
    def product_list(self):
        """Геттер, чтобы посчитать количество товаров в категории"""
        return self.__products

    def __str__(self):
        """Магический метод для вывода в строке общего количества категорий"""
        count = 0
        for productions in self.__products:
            count += productions.quantity
        return f"{self.name}, количество товаров, {count} шт"


if __name__ == "__main__":
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3]
    )

    products = category1.product_list
    print(products)


    #print(category1.get_products())
    product4 = Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7)
    category1.add_products(product4)

    products = category1.product_list

    print(products)
    print(product3)

    print(category1.add_category())
    print(category1.total_categories)

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
# Category.total_categories += 1
# Category.total_products += len(__products)
