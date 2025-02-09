import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import menu


def get_product_by_id(id: int):
    for product in menu.products:
        if (product["_id"] == id):
            return product
    return {}


def get_products_by_type(type):
    lista = []
    for product in menu.products:
        if (product["type"] == type):
            lista.append(product)

    return lista


if __name__ == "__main__":

    print(get_product_by_id(28))
