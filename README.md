# Campus Cart – Student Store System

A command-line point-of-sale and inventory application for a campus store. Browse a product catalog, check low-stock items, build a shopping cart, and check out with automatic discounts and tax.

## Features

- **Product catalog** – view all 15 products sorted by price (low to high or high to low)
- **Low-stock report** – list items whose stock is below a threshold you choose
- **Shopping cart** – add items by ID; inventory is deducted automatically
- **Receipt streaming** – cart contents are printed line by line using a generator
- **Checkout** – applies a 10% discount on orders over $20, then 7.5% tax
- **Transaction logging** – a decorator tracks and reports the number of completed transactions

## Project Structure

```
campus-cart/
├── main.py        # Entry point: inventory setup, menu loop, checkout
├── inventory.py   # Stock management, pricing, filtering, sorting, reports
├── cart.py        # Cart operations and receipt generation
└── logger.py      # @log_transaction decorator
```

| File           | Responsibility                                                                                                                                 |
| -------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| `main.py`      | Initializes the mock inventory, runs the interactive menu, and defines the decorated `checkout_order` function                                 |
| `inventory.py` | `check_stock`, `update_stock`, `calc_price`, `filter_low_stock`, `display_low_stock_report`, `sort_catalog_by_price`, `display_sorted_catalog` |
| `cart.py`      | `add_item`, `calculate_subtotal`, `stream_receipt_lines` (generator)                                                                           |
| `logger.py`    | `log_transaction` decorator using a closure to count transactions                                                                              |

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

```
--- Main Menu ---
1. View Product Catalog (Sorted by Price)
2. Search / Check Low Stock Items
3. Add Item to Cart
4. View Cart & Stream Receipt
5. Checkout & Complete Order
6. Exit Application
```

**Typical workflow**

1. Choose `1` to browse the catalog and pick a sort order.
2. Choose `3`, then enter an Item ID (e.g. `101`) to add it to your cart. Repeat for more items.
3. Choose `4` to review your cart.
4. Choose `5`, review the receipt, and confirm with `y` to pay.
5. Choose `6` to exit.

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
| 111 | Graph Paper Pad          | $3.25  | 9     |
| 112 | Campus T-Shirt           | $14.00 | 25    |
| 113 | Laptop Sleeve            | $17.50 | 7     |
| 114 | Stapler                  | $7.80  | 14    |
| 115 | Ruler Set                | $2.10  | 30    |

Inventory lives in memory and resets each time the program starts.

## Python Concepts Demonstrated

- **Modular design** – logic split across separate modules
- **Lambda functions** – used for filtering low stock and sorting by price
- **Generators** – `stream_receipt_lines` yields receipt lines one at a time
- **Decorators and closures** – `@log_transaction` tracks transaction counts without global variables
- **Dictionary and list comprehensions** – used in filtering and subtotal calculation
- **Input validation** – menu choices, stock thresholds, and item IDs are checked

## Testing Modules Individually

`inventory.py`, `cart.py`, and `logger.py` each include an `if __name__ == "__main__":` block for quick standalone checks:

## PROJECT MEMBERS

- Oluwapelumi Bamidele | [Github Profile](https://github.com/Oluwapelumi-Bamidele)
- Oluwatomisin Tomoloju | [Github Profile](https://github.com/tomisintom)
