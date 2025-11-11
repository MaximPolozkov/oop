import pytest
from product import Product


@pytest.fixture
def sample_product():
    return Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 10)


def test_product_initialization():
    """Проверяет корректность инициализации объекта Product."""
    product = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    assert product.name == "Samsung Galaxy S23 Ultra"
    assert product.description == "256GB, Серый цвет, 200MP камера"
    assert product.price == 180000.0
    assert product.quantity == 5


def test_price_setter_positive():
    """Проверка установки положительной цены."""
    product = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product.price = 200000.0
    assert product.price == 200000.0


def test_new_product_creation():
    """Проверка создания нового товара через classmethod"""
    product_data = {"name": "Sony T766", "description": "128GB", "price": 110000.0, "quantity": 15}
    product = Product.new_product(product_data)
    assert product.name == "Sony T766"
    assert product.price == 110000.0
    assert product.quantity == 15


def test_new_product_dublicate(sample_product):
    """Проверка обработки дубликата товара"""
    product_data = {"name": "Samsung Galaxy S23 Ultra", "description": "256GB, Серый цвет, 200MP камера, цвет черный", "price": 200000.0, "quantity": 5}
    existing_products = [sample_product]
    updated_product = Product.new_product(product_data, existing_products)
    assert updated_product.quantity == 15
    assert updated_product.price == 200000.0


def test_product_str_method(sample_product):
    """Проверяет корректность работы метода __str__."""
    assert str(sample_product) == f"Название продукта: {sample_product.name}, {sample_product.price} руб. Остаток: {sample_product.quantity}" # Добавил проверку str


def test_product_add_method(sample_product):
    """Проверяет корректность работы метода __add__."""
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("iPhone 14 Pro", "256GB, Space Black", 190000.0, 3)
    assert product1 + product2


def test_product_add_type_error(sample_product):
    """Проверяет, что метод __add__ вызывает TypeError, если складывать с не Product."""
    with pytest.raises(TypeError):
        sample_product + "string"


def test_product_initialization_zero_quantity():
    """Проверяет, что при инициализации товара с нулевым количеством выбрасывается исключение ValueError."""
    with pytest.raises(ValueError) as excinfo:
        Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 0)
    assert "Товар с нулевым количеством не может быть добавлен" in str(excinfo.value)


def test_product_initialization_positive_quantity():
    """Проверяет, что при инициализации товара с положительным колличеством, товар создается корректно"""
    product = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
    assert product.quantity == 14





