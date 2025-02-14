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


def add_product(menu, **new_product):
    id = 0
    for product in menu:
        if (product["_id"] > id):
            id = product["_id"]
    #new_product = {"_id": 1+id, **new_product}
    new_product["_id"] = 1+id
    menu.append(new_product)
    return new_product
