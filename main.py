import json

from category import Category
from product import Product


def load_data_from_json(filename):
    """Функция подгрузи данных по категориям и товарам из файла JSON"""
    categories = []
    products_filter = []
    category_filter = []
    with open(filename, 'r', encoding='utf-8') as file:
        reader_json = json.load(file)
        categories.append(reader_json)

    for x in categories[0]:
        name = x["name"]
        description = x["description"]
        z = x["products"]
        for i in z:
            name = i['name']
            description = i['description']
            price = i['price']
            quantity = i['quantity']

            product = Product(name, description, price, quantity)
            products_filter.append(product)

        category = Category(name, description, products_filter)
        category_filter.append(category)

    return category_filter


if __name__ == "__main__":
    try:
        product_invalid = Product("Бракованный товар", "Неверное количество", 1000.0, 0)
    except ValueError as e:
        print(
            "Возникла ошибка ValueError прерывающая работу программы при попытке добавить продукт с нулевым количеством")
    else:
        print("Не возникла ошибка ValueError при попытке добавить продукт с нулевым количеством")

    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    category1 = Category("Смартфоны", "Категория смартфонов", [product1, product2, product3])

    print(category1.middle_price())

    category_empty = Category("Пустая категория", "Категория без продуктов", [])
    print(category_empty.middle_price())

