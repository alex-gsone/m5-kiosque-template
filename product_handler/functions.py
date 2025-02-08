import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import menu


def get_product_by_id(id: int):
    for product in menu.products:
        if (product["_id"] == id):
            print(product)
            break
        else:
            print("k")
            print(len(menu.products))


def get_products_by_type(string: type):
    pass


if __name__ == "__main__":

    get_product_by_id(2)
