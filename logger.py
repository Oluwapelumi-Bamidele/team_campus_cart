"""
A logger module that uses decorator function to add logging to any transaction function
"""

def log_transaction(func):
    # Dictionary to keep track of the total number of transactions processed
    analytics = {"total_transactions": 0}
    
    # Inner wrapper function that runs in place of the original function
    def wrapper(*args, **kwargs):
        # Increment the transaction counter by 1
        analytics["total_transactions"] += 1
        print("\nProcessing your payment...")
        
        # Execute the original function and store its return value
        result = func(*args, **kwargs)
        
        # Display the result and updated transaction count
        print(f"Details: {result}")
        print(f"Transaction completed successfully! (Total logged transactions: {analytics['total_transactions']})")
        
        # Return the original function's output
        return result
        
    return wrapper


# Run test code only when this file is executed directly
if __name__ == "__main__":
    print("--- Running Log Transaction Tests ---")

    # Sample transaction function wrapped with @log_transaction
    @log_transaction
    def process_checkout(cart_total, item_count):
        """Simulates processing a checkout for testing."""
        return f"Items: {item_count} | Total Amount: ${cart_total:.2f}"

    # Test 1: First transaction
    process_checkout(45.50, 3)

    # Test 2: Second transaction to confirm the counter increments
    process_checkout(120.00, 5)