import pytest

from category import Category
from product import Product


@pytest.fixture
def sample_product():
    """Фикстура для создания экземпляра Product."""
    return Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)


@pytest.fixture
def sample_category():
    """Фикстура для создания экземпляра Category."""
    return Category("Смартфоны", "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни")
