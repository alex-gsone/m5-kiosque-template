import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import menu
from menu import products

def get_product_by_id(id: int):
    try:
        if not isinstance(id, int):
            raise TypeError 
        for product in menu.products:
            if (product["_id"] == id):
                return product
        return {}
    except TypeError:
        return ("Product ID must be an integer")

def get_products_by_type(type):
    lista = []
    try:
        if not isinstance(type, str):
            raise TypeError
        for product in menu.products:
            if (product["type"] == type):
                lista.append(product)
        return lista
    except TypeError:
        return ("product type must be a str")

def add_product(menu, **new_product):
    id = 0
    for product in menu:
        if (product["_id"] > id):
            id = product["_id"]
    #new_product = {"_id": 1+id, **new_product}
    new_product["_id"] = 1+id
    menu.append(new_product)
    return new_product

def menu_report():
    contagemTotal = len(products)
    somaTotal = 0
    for product in products:
        somaTotal += product["price"]

    media = somaTotal/contagemTotal
    print(f"\n Products Count: {contagemTotal}"
                f" - Average Price: {media:.2f} - Most Common Type: <tipo_mais_comum>")