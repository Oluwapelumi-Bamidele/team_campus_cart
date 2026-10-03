'''The Logger Module'''

def log_transaction(func):
    """Decorator (@log_transaction) for runtime execution audits and analytics summaries."""
    # Track analytics securely using a closure without global variables
    analytics = {"total_transactions": 0}
    
    def wrapper(*args, **kwargs):
        analytics["total_transactions"] += 1
        print("\nProcessing your payment...")
        
        # Execute the original function and get its result
        result = func(*args, **kwargs)
        
        # Display the actual result to the user
        print(f"Details: {result}")
        print(f"Transaction completed successfully! (Total processed so far: {analytics['total_transactions']})")
        
        return result
        
    return wrapper

# Local verification block
if __name__ == "__main__":
    @log_transaction
    def make_payment(amount):
        return f"Paid {amount}"

    make_payment(5000)
    make_payment(2000)