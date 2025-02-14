from management.product_handler import add_product
from management.tab_handler import calculate_tab

from menu import products


if __name__ == "__main__":
    # Seus prints de teste aqui
    table_1 = [{"_id": 1, "amount": 5}, {"_id": 19, "amount": 5}]
    table_2 = [
        {"_id": 10, "amount": 3},
        {"_id": 20, "amount": 2},
        {"_id": 21, "amount": 5},
    ]

    print(calculate_tab(table_1))
    print(calculate_tab(table_2))
