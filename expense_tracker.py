import csv

# File to store expenses
FILE_NAME = "expenses.csv"

def load_expenses():
    expenses = []
    try:
        with open(FILE_NAME, mode="r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                expenses.append(row)
    except FileNotFoundError:
        pass  # If the file doesn't exist, start with an empty list
    return expenses

def save_expenses(expenses):
    with open(FILE_NAME, mode="w", newline="") as file:
        fieldnames = ["Date", "Category", "Description", "Amount"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(expenses)

def add_expense(expenses):
    date = input("Enter the date (YYYY-MM-DD): ")
    category = input("Enter the category (e.g., Food, Transport, etc.): ")
    description = input("Enter a brief description: ")
    try:
        amount = float(input("Enter the amount: "))
        expenses.append({"Date": date, "Category": category, "Description": description, "Amount": f"{amount:.2f}"})
        print("Expense added successfully!")
    except ValueError:
        print("Invalid amount. Expense not added.")

def view_expenses(expenses):
    if not expenses:
        print("No expenses recorded.")
    else:
        print("\n--- Expense List ---")
        for i, expense in enumerate(expenses, start=1):
            print(f"{i}. {expense['Date']} | {expense['Category']} | {expense['Description']} | ₹{expense['Amount']}")
        print("---------------------")

def summary_by_category(expenses):
    if not expenses:
        print("No expenses to summarize.")
    else:
        category_totals = {}
        for expense in expenses:
            category = expense["Category"]
            amount = float(expense["Amount"])
            category_totals[category] = category_totals.get(category, 0) + amount
        print("\n--- Expense Summary by Category ---")
        for category, total in category_totals.items():
            print(f"{category}: ₹{total:.2f}")
        print("-----------------------------------")

def main():
    expenses = load_expenses()
    while True:
        print("\n--- Expense Tracker Menu ---")
        print("1. View Expenses")
        print("2. Add Expense")
        print("3. Summary by Category")
        print("4. Exit")
        choice = input("Choose an option (1-4): ")
        if choice == "1":
            view_expenses(expenses)
        elif choice == "2":
            add_expense(expenses)
            save_expenses(expenses)
        elif choice == "3":
            summary_by_category(expenses)
        elif choice == "4":
            print("Exiting Expense Tracker. Stay financially savvy!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
