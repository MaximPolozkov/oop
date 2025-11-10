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
    assert Category.total_products == 1


def test_products_info_property(sample_category, sample_product):
    """Проверяет корректность работы свойства products_info."""
    sample_category.add_products(sample_product)
    info = sample_category.products_info
    assert len(info) == 1
    assert info[0] == f"{sample_product.name}, {sample_product.price} руб. Остаток: {sample_product.quantity} шт."


def test_product_list_property(sample_category, sample_product):
    """Проверяет корректность работы свойства product_list."""
    sample_category.add_products(sample_product)
    product_list = sample_category.product_list
    assert len(product_list) == 1
    assert product_list[0] is sample_product  # Проверяем, что это тот же самый объект, а не копия


def test_category_str_method(sample_category, sample_product):
    """Проверяет корректность работы метода __str__."""
    sample_category.add_products(sample_product)
    assert str(sample_category) == f"{sample_category.name}, количество товаров, {sample_product.quantity} шт"
