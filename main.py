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
    # x = load_data_from_json("./products.json")
    # print(x)
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    print(product1.name)
    print(product1.description)
    print(product1.price)
    print(product1.quantity)

    print(product2.name)
    print(product2.description)
    print(product2.price)
    print(product2.quantity)

    print(product3.name)
    print(product3.description)
    print(product3.price)
    print(product3.quantity)

    category1 = Category("Смартфоны",
                         "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
                         [product1, product2, product3])

    print(category1.name == "Смартфоны")
    print(category1.description)
    print(len(category1.product_list))
    print(category1.add_category)
    print(category1.product_list)

    product4 = Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7)
    category2 = Category("Телевизоры",
                         "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
                         [product4])

    print(category2.name)
    print(category2.description)
    print(len(category2.product_list))
    print(category2.products)

    print(Category.add_category)
    print(Category.product_list)
