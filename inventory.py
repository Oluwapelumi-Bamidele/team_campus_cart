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
    
def sort_catalog_by_price(inventory, ascending=True):
    #uses a Lambda function and sorted to arrange the product by price"
    sorted_items = sorted(inventory.items(), key=lambda item: item[1]["price"], reverse=not ascending)
    return dict(sorted_items)

def display_sorted_catalog(inventory, ascending=True):
    #Sorts the inventory by price and prints it as a clean table.
    sorted_items = sort_catalog_by_price(inventory, ascending=ascending)
    
    direction = "Ascending (Low to High)" if ascending else "Descending (High to Low)"
    print(f"\n--- Product Catalog ({direction}) ---\n")
    print(f"{'ID':<7} | {'Item Name':<27} | {'Price':<16} | {'Stock':<15}")
    print("-" * 52)
    
    for item_id, data in sorted_items.items():
        name = data["name"]
        price = f"${data['price']:.2f}"
        stock = data["stock"]
        print(f"{item_id:<7} | {name:<27} | {price:<16} | {stock:<15}")
    
    print("-" * 52)
    
# Local independent verification script block
if __name__ == "__main__":
    campus_inventory = {
        "101": {"name": "Notebook", "price": 2.50, "stock": 15},
        "102": {"name": "Campus Hoodie", "price": 25.00, "stock": 4},
        "103": {"name": "Scientific Calculator", "price": 15.00, "stock": 8}
    }
    
    print("--- Testing Inventory Module ---\n")
    print(f"Stock for item 101: {check_stock(campus_inventory, '101')}\n")
    
    # Test price quote where it triggers 10% discount when order total exceed $20
    quote = calc_price(25.00, order_total=25.00)
    print(f"Price quote for $25 item (with order total > $20 discount): ${quote}\n")
    
    #Test update_stock where it check for stock availablity and return a message
    success, message = update_stock(campus_inventory, '102', -5)
    print(f"Stock Update Test: Success = {success}, Result = {message}\n")
    
    #Test fiter_low_stock where filter out items that is below a certain limit
    low_stock = filter_low_stock(campus_inventory, limit=10)
    print(f"Low Stock Items (<10): {low_stock}\n")
    
    # This single line handles the filtering and prints the professional table automatically!
    display_low_stock_report(campus_inventory, limit=10)
    print("\n")
    
    #Test sort_catalog_price where price is sorted in ascending order of its price
    sorted_catalog = sort_catalog_by_price(campus_inventory, ascending=True)
    print(f"Sorted Catalog by Price: {sorted_catalog}\n")
    
    # This single line dispaly price in ascending order of its price
    display_sorted_catalog(campus_inventory, ascending=True)
    print("\n")
    
    # This single line dispaly price in descending order of its price
    display_sorted_catalog(campus_inventory, ascending=False)
    