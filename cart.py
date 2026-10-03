"""
Cart Engine Module

This module provides tools for managing carts, adding to cart, removing from cart, checking out cart
"""
# cart.py

def add_item(cart, name, price):
    """Manages selection by adding a new item to the cart list."""
    cart.append({"name": name, "price": price})
    return cart

def calculate_subtotal(cart):
    """Calculates the subtotal of items in the cart[cite: 1, 5]."""
    return sum(item["price"] for item in cart)

def stream_receipt_lines(cart):
    """Generator function to stream receipt lines sequentially[cite: 1, 5]."""
    for item in cart:
        yield f"{item['name']} - ${item['price']}"
    yield f"Subtotal: ${calculate_subtotal(cart)}"

if __name__ == "__main__":
    # Local verification block
    sample_cart = []
    add_item(sample_cart, "Apple", 2.0)
    add_item(sample_cart, "Bread", 3.5)
    
    for line in stream_receipt_lines(sample_cart):
        print(line)