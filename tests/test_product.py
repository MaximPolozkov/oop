def test_product_initialization(sample_product):
    """Проверяет корректность инициализации объекта Product."""
    assert sample_product.name == "Samsung Galaxy S23 Ultra", "256GB"
    assert sample_product.description == "256GB, Серый цвет, 200MP камера"
    assert sample_product.price == 180000.0
    assert sample_product.quantity == 5
