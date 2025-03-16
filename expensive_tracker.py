import json
import os
from datetime import datetime

# File to store expenses
EXPENSE_FILE = 'expenses.json'

# Predefined categories
CATEGORIES = ['food', 'transport', 'entertainment', 'utilities', 'others']


def load_expenses():
    if os.path.exists(EXPENSE_FILE):
        with open(EXPENSE_FILE, 'r') as file:
            return json.load(file)
    return []


def save_expenses(expenses):
    with open(EXPENSE_FILE, 'w') as file:
        json.dump(expenses, file, indent=4)


def add_expense(expenses):
    try:
        date_str = input("Enter date (YYYY-MM-DD): ")
        # Validate date format
        datetime.strptime(date_str, "%Y-%m-%d")

        amount = float(input("Enter amount: "))
        print("Select a category from:", ', '.join(CATEGORIES))
        category = input("Enter category: ").lower()

        if category not in CATEGORIES:
            print("Invalid category. Adding to 'others'.")
            category = 'others'

        description = input("Enter description: ")

        expense = {
            "date": date_str,
            "amount": amount,
            "category": category,
            "description": description
        }

        expenses.append(expense)
        save_expenses(expenses)
        print("Expense added successfully!")

    except ValueError as ve:
        print("Invalid input. Please try again.", ve)


def view_expenses(expenses):
    if not expenses:
        print("No expenses found.")
        return

    for idx, exp in enumerate(expenses, start=1):
        print(f"{idx}. Date: {exp['date']}, Amount: {exp['amount']}, Category: {exp['category']}, Description: {exp['description']}")


def view_expenses_by_category(expenses):
    category = input("Enter category to view: ").lower()
    filtered = [exp for exp in expenses if exp['category'] == category]

    if not filtered:
        print(f"No expenses found in category '{category}'.")
        return

    for idx, exp in enumerate(filtered, start=1):
        print(f"{idx}. Date: {exp['date']}, Amount: {exp['amount']}, Description: {exp['description']}")


def monthly_summary(expenses):
    month = input("Enter month in format YYYY-MM: ")
    filtered = [exp for exp in expenses if exp['date'].startswith(month)]

    if not filtered:
        print(f"No expenses found for {month}.")
        return

    total = sum(exp['amount'] for exp in filtered)
    print(f"Total expenses for {month}: {total}")

    category_totals = {}
    for exp in filtered:
        category_totals[exp['category']] = category_totals.get(exp['category'], 0) + exp['amount']

    print("Category-wise breakdown:")
    for cat, amt in category_totals.items():
        print(f"{cat}: {amt}")


def main():
    expenses = load_expenses()

    while True:
        print("\n====== Expense Tracker ======")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. View Expenses by Category")
        print("4. View Monthly Summary")
        print("5. Exit")

        choice = input("Select an option: ")

        if choice == '1':
            add_expense(expenses)
        elif choice == '2':
            view_expenses(expenses)
        elif choice == '3':
            view_expenses_by_category(expenses)
        elif choice == '4':
            monthly_summary(expenses)
        elif choice == '5':
            print("Exiting Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid option. Please select from the menu.")


if __name__ == "__main__":
    main()