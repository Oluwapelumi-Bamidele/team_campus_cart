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

