def log_transaction(func):
    """Decorator (@log_transaction) for runtime execution audits and analytics summaries."""
    # Track analytics securely using a closure without global variables
    analytics = {"total_transactions": 0}
    
