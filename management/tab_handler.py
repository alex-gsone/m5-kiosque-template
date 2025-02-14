from menu import products

def calculate_tab(table:list):
    total = 0
    for product in table:
        for item in products:
            if( product["_id"] == item["_id"] ):
                total = total + product["amount"]*item["price"]
    consumoMesa = {"subtotal": round(total, 2)}           
    return consumoMesa