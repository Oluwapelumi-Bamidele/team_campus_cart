'''Main Script'''

from inventory import (
    calc_price,
    display_low_stock_report,
    display_sorted_catalog,
    update_stock,
)
from cart import add_item, calculate_subtotal, stream_receipt_lines
from logger import log_transaction


# Mock initial database/inventory setup for the campus store
def initialize_inventory():
    return {
        "101": {"name": "Notebook", "price": 2.50, "stock": 15},
        "102": {"name": "Campus Hoodie", "price": 25.00, "stock": 4},
        "103": {"name": "Scientific Calculator", "price": 15.00, "stock": 8},
        "104": {"name": "Ballpoint Pens (10-pack)", "price": 4.75, "stock": 40},
        "105": {"name": "Highlighter Set", "price": 6.25, "stock": 22},
        "106": {"name": "Backpack", "price": 32.99, "stock": 6},
        "107": {"name": "USB Flash Drive 64GB", "price": 11.50, "stock": 18},
        "108": {"name": "Water Bottle", "price": 9.99, "stock": 12},
        "109": {"name": "Desk Lamp", "price": 19.95, "stock": 3},
        "110": {"name": "Sticky Notes", "price": 1.99, "stock": 55},
        "111": {"name": "Graph Paper Pad", "price": 3.25, "stock": 9},
        "112": {"name": "Campus T-Shirt", "price": 14.00, "stock": 25},
        "113": {"name": "Laptop Sleeve", "price": 17.50, "stock": 7},
        "114": {"name": "Stapler", "price": 7.80, "stock": 14},
        "115": {"name": "Ruler Set", "price": 2.10, "stock": 30},
        }

@log_transaction
def checkout_order(cart):
    """Processes the final checkout, wrapped with the @log_transaction decorator."""
    subtotal = calculate_subtotal(cart)
    # Applying order-level discount calculation logic
    final_total = calc_price(subtotal, order_total=subtotal)
    return f"Total Items: {len(cart)} | Final Amount (with tax/discounts): ${final_total:.2f}"


def main():
    inventory = initialize_inventory()
    cart = []

    print("=" * 60)
    print("      WELCOME TO CAMPUS CART - STUDENT STORE SYSTEM      ")
    print("=" * 60)

    while True:
        print("\n--- Main Menu ---")
        print("1. View Product Catalog (Sorted by Price)")
        print("2. Search / Check Low Stock Items")
        print("3. Add Item to Cart")
        print("4. View Cart & Stream Receipt")
        print("5. Checkout & Complete Order")
        print("6. Exit Application")

        choice = input("\nEnter your choice (1-6): ").strip()

        if choice == "1":
            print("\nHow would you like to sort the catalog?")
            print("1. Low to High Price")
            print("2. High to Low Price")
            sort_choice = input("Select sorting option (1-2): ").strip()
            ascending = True if sort_choice != "2" else False
            display_sorted_catalog(inventory, ascending=ascending)

        elif choice == "2":
            try:
                limit = int(input("Enter stock threshold limit (e.g., items below): "))
                if limit > 0:
                    display_low_stock_report(inventory, limit)
                else:
                    print("\n[Error] Please enter a valid number greater than 0 (zero) for the stock limit.")
            except ValueError:
                print("\n[Error] Please enter a valid number for the stock limit.")

        elif choice == "3":
            display_sorted_catalog(inventory, ascending=True)
            item_id = input("\nEnter the Item ID you want to add to your cart: ").strip()

            if item_id in inventory:
                item_data = inventory[item_id]
                if item_data["stock"] > 0:
                    # Ask for quantity or add 1
                    add_item(cart, item_data["name"], item_data["price"])
                    # Deduct from inventory stock using modular update_stock function
                    success, result = update_stock(inventory, item_id, -1)
                    if success:
                        print(f"\n[Success] Added '{item_data['name']}' to your cart! (Stock left: {result})")
                else:
                    print(f"\n[Sorry] '{item_data['name']}' is currently out of stock!")
            else:
                print("\n[Error] Invalid Item ID. Please check the catalog.")

        elif choice == "4":
            print("\n--- Current Cart Receipt Stream ---")
            if not cart:
                print("Your cart is currently empty.")
            else:
                # Utilizing the generator function to stream receipt lines sequentially
                for line in stream_receipt_lines(cart):
                    print(f"  > {line}")

        elif choice == "5":
            if not cart:
                print("\n[Notice] Your cart is empty. Add items before checking out!")
            else:
                print("\n--- Processing Checkout ---")
                for line in stream_receipt_lines(cart):
                    print(f"  > {line}")

                confirm = input("\nDo you want to proceed with payment? (y/n): ").strip().lower()
                if confirm == "y":
                    # Trigger checkout wrapped in the @log_transaction decorator
                    checkout_order(cart)
                    cart.clear()  # Empty cart after successful purchase
                else:
                    print("\nCheckout cancelled.")

        elif choice == "6":
            print("\nThank you for using Campus Cart! Good luck")
            break
        else:
            print("\n[Error] Invalid selection. Please choose an option between 1 and 6.")


if __name__ == "__main__":
    main()
