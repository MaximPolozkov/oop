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
    x = load_data_from_json("./products.json")
    print(x)
