from datetime import datetime

def validate_date(date_str):
    """Validates a date string against a specified format."""
    try:
        datetime.strptime(date_str,"%Y-%m-%d")
        return True
    except ValueError:
        print("Invalid date format. Please enter the date as YYYY-MM-DD.")
        return False

def validate_amount(amount_str):
    try:
        amount = float(amount_str)
        if amount <= 0:
            print("$ can't be negative.")
            return False
        return True
    except ValueError:
        print("Invalid input. Please enter an valid amount")
        return False
    
def validate_category(category_str,allowed_categories):
    if category_str.lower() in [category.lower() for category in allowed_categories]:
        return True
    else:
        print(f"Invalid category. Please choose from: {','.join(allowed_categories)}.")
        return False