import json
import sqlite3
from datetime import datetime
from data_validation import validate_date, validate_amount, validate_category
DATA_FILE = "transactions.json"

allowed_categories = ["Food","Rent","Entertainment","Transportion","Other"]

def add_transaction():

    while True:
        date = input("Enter the date (YYYY-MM-DD): ")
        if validate_date(date):
            break
   
    description = input("Enter trans description: ")
    
    while True:    
        category = input(f"Enter category ({','.join(allowed_categories)}): ")
        if validate_category(category,allowed_categories):
            break

    while True: 
        amount_str = input("Enter the amount: ")
        if validate_amount(amount_str):
            amount = float(amount_str)
            break

    transaction = {
        "date" : date,
        "description" : description,
        "category" : category,
        "amount" : amount
    }
    try:
        with open(DATA_FILE, "r") as file:
            transactions = json.load(file)
    except FileNotFoundError:
        transactions = []

    transactions.append(transaction)

    with open(DATA_FILE, "w") as file:
        json.dump(transactions, file, indent=4)
        print("Success. Transaction added.")

def view_transactions():
    try:
        with open(DATA_FILE, "r") as file:
            transactions = json.load(file)

    except FileNotFoundError:
        print("No transactions found.")
        return
    print("\nTransactions:")
    for transaction in transactions:
        print(f"{transaction['date']} - {transaction['description']} - {transaction['category']} -- ${transaction['amount']}")
