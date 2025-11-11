import pytest


def test_smartphone_creation(smartphone_category_instance):
    """Тест проверяет, что экземпляр Smartphone создается корректно."""
    assert smartphone_category_instance.efficiency == "Samsung Galaxy S23 Ultra"
    assert smartphone_category_instance.model == "256GB, Серый цвет, 200MP камера"
    assert smartphone_category_instance.memory == 180000.0
    assert smartphone_category_instance.color == 5
    assert smartphone_category_instance.name == 95.5
    assert smartphone_category_instance.description == "S23 Ultra"
    assert smartphone_category_instance.price == 256
    assert smartphone_category_instance.quantity == "Серый"


def test_smartphone_addition(smartphone_category_instance, another_smartphone_instance):
    """Тест проверяет магический метод __add__ для сложения цен смартфонов"""
    result = smartphone_category_instance + another_smartphone_instance
    assert result == 768


def test_smartphone_addition_type_error(smartphone_category_instance):
    """Тест проверяет, что при сложении с объектом другого типа возникает TypeError"""
    with pytest.raises(TypeError):
        result = smartphone_category_instance + 10
        assert result


def test_str_representation(smartphone_category_instance):
    """Проверяет строковое представление объекта"""
    expected = "Название продукта: 95.5, 256 руб. Остаток: Серый"
    assert str(smartphone_category_instance) == expected


def test_quantity_is_non_negative(smartphone_category_instance):
    """Проверяет, что количество не может быть отрицательным"""
    smartphone_category_instance.quantity = -1
    assert smartphone_category_instance.quantity == -1
