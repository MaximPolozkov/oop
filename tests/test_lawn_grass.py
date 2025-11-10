import pytest


def test_lawn_grass_creation(lawn_grass_instance):
    """Проверяем создание экземпляра LawnGrass."""
    assert lawn_grass_instance.country == "Газонная трава"
    assert lawn_grass_instance.germination_period == "Элитная трава для газона"
    assert lawn_grass_instance.color == 500.0
    assert lawn_grass_instance.name == 20
    assert lawn_grass_instance.description == "Россия"
    assert lawn_grass_instance.price == "7 дней"
    assert lawn_grass_instance.quantity == "Зеленый"


def test_lawn_grass_addition(lawn_grass_instance, another_lawn_grass_instance):
    """Проверяем сложение цен двух экземпляров LawnGrass."""
    result = lawn_grass_instance + another_lawn_grass_instance
    assert result == "7 дней5 дней"


def test_lawn_grass_addition_type_error(lawn_grass_instance):
    """Проверяем, что при сложении с другим типом возникает TypeError."""
    with pytest.raises(TypeError):
        result = lawn_grass_instance + 10
        assert result
