import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import menu


def get_product_by_id(id: int):
    i = 1
    for product in menu.products:
        if (product["_id"] == id):
            print(product)
            break
        elif (i == len(menu.products)):
            emptyDict = {}
            print(emptyDict)
        i = i+1


def get_products_by_type(type):

    lista = []
    for product in menu.products:
        if (product["type"] == type):
            lista.append(product)

    return lista


if __name__ == "__main__":

    print(get_products_by_type('drink'))
