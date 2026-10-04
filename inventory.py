"""
Inventory Engine Module

Provides tools for managing product inventory levels, calculating pricing,
filtering stock levels, displaying reports, and administrative management.
"""

def check_stock(inventory, item_id):
    # Return stock count if item exists; otherwise return 0
    if item_id in inventory:
        return inventory[item_id]["stock"]
    return 0

def update_stock(inventory, item_id, qty_change):
    # Check if item exists in inventory dictionary
    if item_id in inventory:
        current_stock = inventory[item_id]["stock"]
        new_stock = current_stock + qty_change
        
        # Ensure stock does not drop below zero
        if new_stock >= 0:
            inventory[item_id]["stock"] = new_stock
            return True, inventory[item_id]["stock"]
        return False, "Error: Requested quantity exceeds available stock."
    return False, "Error: Item ID not found."

def verify_and_add_stock(inventory, item_id, add_qty):
    # Check if item exists before restocking
    if item_id not in inventory:
        return False, "Error: Item ID not found in inventory."
    
    # Increase stock count by the added quantity
    inventory[item_id]["stock"] += add_qty
    return True, f"Successfully added {add_qty} units! New stock: {inventory[item_id]['stock']}"

def add_new_item(inventory, item_id, name, price, stock):
    # Check to prevent duplicate item IDs
    if item_id in inventory:
        return False, "Error: An item with this ID already exists."
    
    # Add new product entry to inventory dictionary
    inventory[item_id] = {
        "name": name,
        "price": price,
        "stock": stock,
    }
    return True, f"Successfully added '{name}' (ID: {item_id}) to inventory!"

def delete_item(inventory, item_id):
    # Remove item from inventory if present
    if item_id in inventory:
        removed_item = inventory.pop(item_id)
        return True, f"Successfully removed '{removed_item['name']}' from inventory."
    return False, "Error: Item ID not found."

def calc_price(base_price, tax_rate=0.075, order_total=0.0):
    # Apply 10% discount if order total exceeds $20
    discount = 0.10 if order_total > 20 else 0.0
    discounted_price = base_price * (1 - discount)
    
    # Calculate tax and round to two decimal places
    final_price = discounted_price * (1 + tax_rate)
    return round(final_price, 2)

def filter_low_stock(inventory, limit):
    # Lambda function to check if item stock is below threshold limit
    is_low_stock = lambda data: data["stock"] < limit
    return {item_id: data for item_id, data in inventory.items() if is_low_stock(data)}

def display_low_stock_report(inventory, limit):
    # Retrieve items below specified limit
    low_stock_items = filter_low_stock(inventory, limit)
    
    # Show status message if all items meet threshold
    if not low_stock_items:
        print("\n--- Low Stock Alert Report ---")
        print("Status: All items are currently well-stocked!")
        return

    # Print formatted table header
    print("\n--- Low Stock Alert Report ---\n")
    print(f"{'Item ID':<8} | {'Item Name':<25} | {'Price':<10} | {'Stock Remaining':<15}")
    print("-" * 68)
    
    # Print formatted rows for low stock items
    for item_id, data in low_stock_items.items():
        name = data["name"]
        price = f"${data['price']:.2f}"
        stock = data["stock"]
        print(f"{item_id:<8} | {name:<25} | {price:<10} | {stock:<15}")
    print("-" * 68)

def sort_catalog_by_price(inventory, ascending=True):
    # Sort items dictionary by price field in ascending or descending order
    sorted_items = sorted(inventory.items(), key=lambda item: item[1]["price"], reverse=not ascending)
    return dict(sorted_items)

def display_sorted_catalog(inventory, ascending=True):
    # Sort inventory by price and set title direction
    sorted_items = sort_catalog_by_price(inventory, ascending=ascending)
    direction = "Ascending (Low to High)" if ascending else "Descending (High to Low)"
    
    # Display formatted table header and items
    print(f"\n--- Product Catalog ({direction}) ---\n")
    print(f"{'ID':<6} | {'Item Name':<25} | {'Price':<10} | {'Stock':<8}")
    print("-" * 55)
    for item_id, data in sorted_items.items():
        print(f"{item_id:<6} | {data['name']:<25} | ${data['price']:<9.2f} | {data['stock']:<8}")
    print("-" * 55)


# Run test code only when this file is executed directly
if __name__ == "__main__":
    print("--- Running Inventory Engine Tests ---")

    # Sample inventory setup
    test_inventory = {
        "101": {"name": "Notebook", "price": 2.50, "stock": 15},
        "102": {"name": "Campus Hoodie", "price": 25.00, "stock": 3},
        "103": {"name": "Sticky Notes", "price": 1.99, "stock": 50},
    }

    # 1. Test check_stock
    print(f"\nChecking stock for Item '101': {check_stock(test_inventory, '101')} units")

    # 2. Test update_stock
    print("\nDeducting 5 units from Item '101':")
    success, result = update_stock(test_inventory, "101", -5)
    print(f"  Result: Success={success}, New Stock={result}")

    # 3. Test verify_and_add_stock
    print("\nRestocking 10 units to Item '102':")
    success, msg = verify_and_add_stock(test_inventory, "102", 10)
    print(f"  Result: {msg}")

    # 4. Test add_new_item
    print("\nAdding new item 'Desk Lamp' (ID: 104):")
    success, msg = add_new_item(test_inventory, "104", "Desk Lamp", 19.95, 8)
    print(f"  Result: {msg}")

    # 5. Test calc_price
    price_under_20 = calc_price(15.00, order_total=15.00)
    price_over_20 = calc_price(25.00, order_total=25.00)
    print(f"\nPrice calculation test:")
    print(f"  $15.00 Order (No Discount + 7.5% Tax): ${price_under_20}")
    print(f"  $25.00 Order (10% Discount + 7.5% Tax): ${price_over_20}")

    # 6. Test low stock report
    print("\nTesting Low Stock Report (Threshold: 11):")
    display_low_stock_report(test_inventory, limit=11)

    # 7. Test display sorted catalog
    print("\nTesting Sorted Catalog (Low-to-High Price):")
    display_sorted_catalog(test_inventory, ascending=True)

    # 8. Test delete_item
    print("\nDeleting Item '103':")
    success, msg = delete_item(test_inventory, "103")
    print(f"  Result: {msg}")
