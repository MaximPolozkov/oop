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

