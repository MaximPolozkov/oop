from category import Category


def test_category_initialization(sample_category):
    """Проверяет корректность инициализации объекта Category."""
    assert sample_category.name == "Смартфоны"
    assert sample_category.description == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    assert sample_category.get_products() == []


def test_category_counts(sample_product, sample_category):
    """Проверяет подсчет количества продуктов и категорий."""
    assert Category.total_categories == 0
    assert Category.total_products == 0
    Category.add_category()
    assert Category.total_categories == 1

    assert Category("Телевизоры", "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником", [sample_product])
    Category.add_category()
    assert Category.total_categories == 2
    assert Category.total_products == 0


def test_adding_products_to_category(sample_category, sample_product):
    """Проверяет добавление товаров в категорию."""
    sample_category.add_products(sample_product)
    assert len(sample_category.get_products()) == 1
    assert Category.total_products == sample_product.quantity
