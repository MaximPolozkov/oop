import pytest

from category import Category
from product import Product
from smartphone import Smartphone
from lawn_grass import LawnGrass

@pytest.fixture
def sample_product():
    """Фикстура для создания экземпляра Product."""
    return Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)


@pytest.fixture
def sample_category():
    """Фикстура для создания экземпляра Category."""
    return Category("Смартфоны", "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни")


@pytest.fixture
def smartphone_category_instance():
    """Фикстура для создания экземпляра Smartphone"""
    return Smartphone("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5,
                         "S23 Ultra", 256, "Серый")


@pytest.fixture
def another_smartphone_instance():
    """Фикстура для создания второго экземпляра Smartphone"""
    return Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")


@pytest.fixture
def lawn_grass_instance():
    """Создаем экземпляр LawnGrass для тестов"""
    return LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")


@pytest.fixture
def another_lawn_grass_instance():
    """Создаем второй экземпляр LawnGrass для тестов"""
    return LawnGrass("Газонная трава 2", "Выносливая трава", 450.0, 15, "США", "5 дней", "Темно-зеленый")

