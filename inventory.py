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