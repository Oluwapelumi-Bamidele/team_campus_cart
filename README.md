# Campus Cart – Student Store System

A command-line point-of-sale and inventory application for a campus store. Students can browse a product catalog, check low-stock items, build a shopping cart, and check out with automatic discounts and tax. Administrators can restock, adjust, add, and delete products.

## Features

- **Two role interfaces** – a User / Student interface and an Administrator interface
- **Product catalog** – view all 10 products sorted by price (low to high or high to low)
- **Low-stock report** – list items whose stock is below a threshold you choose
- **Shopping cart** – add items by ID; inventory is deducted automatically
- **Cart editing** – remove some or all of an item, or clear the cart; stock is returned to inventory
- **Receipt streaming** – cart contents are printed line by line using a generator
- **Checkout** – applies a 10% discount on orders over $20, then 7.5% tax
- **Transaction logging** – a decorator tracks and reports the number of completed transactions
- **Admin tools** – restock items, directly modify stock, add new products, and delete products

## Project Structure

```
campus-cart/
├── main.py        # Entry point: inventory setup, user/admin menus, checkout
├── inventory.py   # Stock management, pricing, filtering, sorting, reports
├── cart.py        # Cart operations and receipt generation
└── logger.py      # @log_transaction decorator
```

| File           | Responsibility                                                                                                                                                                                        |
| -------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `main.py`      | Initializes the mock inventory, runs the role selection, user and admin menu loops, and defines the decorated `checkout_order` function                                                               |
| `inventory.py` | `check_stock`, `update_stock`, `verify_and_add_stock`, `add_new_item`, `delete_item`, `calc_price`, `filter_low_stock`, `display_low_stock_report`, `sort_catalog_by_price`, `display_sorted_catalog` |
| `cart.py`      | `add_item`, `remove_item`, `calculate_subtotal`, `stream_receipt_lines` (generator)                                                                                                                   |
| `logger.py`    | `log_transaction` decorator using a closure to count transactions                                                                                                                                     |

## Requirements

- Python 3.6 or newer
- No third-party packages (standard library only)

## Getting Started

1. Place `main.py`, `inventory.py`, `cart.py`, and `logger.py` in the same folder.
2. Run the application:

```bash
python main.py
```

## Usage

**Role Selection**

```
1. User / Student Interface
2. Administrator Interface
3. Exit System
```

**User Menu**

```
1. View Product Catalog
2. Search / Check Low Stock Items
3. Add Item to Cart
4. Remove Item from Cart
5. View Cart & Stream Receipt
6. Clear Cart
7. Checkout & Complete Order
8. Switch Role / Return to Main Landing
```

**Administrator Menu**

```
1. View Full Catalog (Includes Stock & Unit Codes)
2. Check Stock Below Threshold Limit
3. Restock Item
4. Directly Modify Item Stock (Add/Remove)
5. Add Brand New Product to Catalog
6. Delete Item from Catalog
7. Return to Role Selection / Main Interface
8. Exit Application Entirely
```

**Typical workflow**

1. Choose `1` at the role screen to enter the User interface.
2. Choose `1` to browse the catalog and pick a sort order.
3. Choose `3`, then enter an Item ID (e.g. `101`) and a quantity to add it to your cart. Repeat for more items.
4. Choose `5` to review your cart and receipt preview.
5. Choose `7`, review the final receipt, and confirm with `y` to pay.
6. Choose `8` to return to role selection, then `3` to exit.

## Pricing Rules

Defined in `calc_price` in `inventory.py`:

- **Discount:** 10% off when the order total exceeds $20
- **Tax:** 7.5% applied after the discount

Example: a $25.00 order → $22.50 after discount → **$24.19** with tax.

## Sample Inventory

| ID  | Item                     | Price  | Stock |
| --- | ------------------------ | ------ | ----- |
| 101 | Notebook                 | $2.50  | 15    |
| 102 | Campus Hoodie            | $25.00 | 4     |
| 103 | Scientific Calculator    | $15.00 | 8     |
| 104 | Ballpoint Pens (10-pack) | $4.75  | 40    |
| 105 | Highlighter Set          | $6.25  | 22    |
| 106 | Backpack                 | $32.99 | 6     |
| 107 | USB Flash Drive 64GB     | $11.50 | 18    |
| 108 | Water Bottle             | $9.99  | 12    |
| 109 | Desk Lamp                | $19.95 | 3     |
| 110 | Sticky Notes             | $1.99  | 55    |

Inventory lives in memory and resets each time the program starts.

## Python Concepts Demonstrated

- **Modular design** – logic split across separate modules
- **Lambda functions** – used for filtering low stock and sorting by price
- **Generators** – `stream_receipt_lines` yields receipt lines one at a time
- **Decorators and closures** – `@log_transaction` tracks transaction counts without global variables
- **Dictionary and list comprehensions** – used in filtering and subtotal calculation
- **Input validation** – menu choices, stock thresholds, quantities, and item IDs are checked

## Testing Modules Individually

`inventory.py`, `cart.py`, and `logger.py` each include an `if __name__ == "__main__":` block for quick standalone checks:

```bash
python inventory.py
python cart.py
python logger.py
```

## PROJECT MEMBERS

- Oluwapelumi Bamidele | [Github Profile](https://github.com/Oluwapelumi-Bamidele)
- Oluwatomisin Tomoloju | [Github Profile](https://github.com/tomisintom)
