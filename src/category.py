class Category:
    """Класс, предоставляющий категории товаров"""
    total_categories = 0
    total_products = 0

    def __init__(self, name, description, products=None):
        """Инициализируем объект категории"""
        self.name = name
        self.description = description
        self.products = products if products is not None else []

        Category.total_categories += 1
        Category.total_products += len(self.products)
