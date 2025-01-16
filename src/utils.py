import json
from pathlib import Path
from typing import Any

from src.category import Category
from src.product import Product
from src.settings import BASE_DIR

json_filename = Path(BASE_DIR, "data", "products.json")


def read_json_data(path: str) -> dict:
    with open(json_filename, "r", encoding="UTF-8") as file:
        data = json.load(file)
    return data


# data = read_json_data(json_filename)
# print(data)
# print(type(data))


def create_category_from_json(data: list) -> list[Any]:
    category_list = []
    for category in data:
        products = []
        for product in category.get("products"):
            products.append(Product(**product))
        category["products"] = products
        category_list.append(Category(**category))

    return category_list


if __name__ == "__main__":
    raw_data = read_json_data("../data/data.json")

    # print(raw_data)
    category_data = create_category_from_json(raw_data)
    print(category_data[0].name)
    print(category_data[0].products)
    # print(len(category_data))
    # print(type(category_data))
    # print(category_data)
    # print(category_data[1].name)
    # print(category_data[1].products)
