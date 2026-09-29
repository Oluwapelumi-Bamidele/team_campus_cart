"""
Inventory Engine Module

This module provides tools for managing product inventory levels, calculating discounted pricing,
filtering stock levels, and displaying formatted terminal reports.
"""

def check_stock(inventory, item_id):
    #return the quantity of an item number
    if item_id in inventory:
        return inventory[item_id]["stock"]
    return 0

def update_stock(inventory, item_id, qty_change):
    #update the stock availability of an item
    #return a Boolean statement and a new stock qty or message
    if item_id in inventory:
        current_stock = inventory[item_id]["stock"]
        new_stock = current_stock + qty_change
        if new_stock >= 0:
            inventory[item_id]["stock"] = new_stock
            return True, inventory[item_id]["stock"]
        return False, "Error: Your demand is higher than the quantity available"
    return False, "Errror: Item ID not found"

def calc_price(base_price, tax_rate=0.075, order_total=0.0):
    #calculate the final price (including tax and conditional discount)
    #apllies 10% discount if overall order exceeds $20
    discount = 0.10 if order_total > 20 else 0.0
    
    discounted_price = base_price * (1 - discount)
    final_price = discounted_price * (1 + tax_rate)
    return round(final_price, 2)

def filter_low_stock(inventory, limit):
    #Uses a lambda function to filter items below a specified stock limit
    is_low_stock = lambda data: data["stock"] < limit
    return {item_id : data for item_id, data in inventory.items() if is_low_stock(data)}

def display_low_stock_report(inventory, limit):
    #Takes the inventory and limit, filters low stock, and prints as a table.
    low_stock_items = filter_low_stock(inventory, limit)
    
    if not low_stock_items:
        print("\n--- Low Stock Alert Report ---")
        print("Status: All items are currently well-stocked!")
        return

    print("\n--- Low Stock Alert Report ---\n")
    print(f"{'Item ID':<4} | {'Item Name':<27} | {'Price':<16} | {'Stock Remaining':<15}")
    print("-" * 75)
    
    for item_id, data in low_stock_items.items():
        name = data["name"]
        price = f"${data['price']:.2f}"
        stock = data["stock"]
        print(f"{item_id:<7} | {name:<27} | {price:<16} | {stock:<15}")
    
    print("-" * 75)