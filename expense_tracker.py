import csv
import os

FILENAME = "expenses.csv"

def add_expense():
    date = input("Enter date (DD-MM-YYYY): ")
    category = input("Enter category (Food/Travel/Shopping/etc): ")
    amount = float(input("Enter amount: "))

    with open(FILENAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount])

    print("Expense added successfully!\n")


def view_expenses():
    if not os.path.exists(FILENAME):
        print("No expenses recorded yet.\n")
        return

    total = 0
    with open(FILENAME, "r") as file:
        reader = csv.reader(file)
        print("\nDate | Category | Amount")
        print("-" * 30)
        for row in reader:
            print(f"{row[0]} | {row[1]} | {row[2]}")
            total += float(row[2])

    print("-" * 30)
    print(f"Total Spending: {total}\n")


def main():
    while True:
        print("===== Smart Expense Tracker =====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.\n")


if __name__ == "__main__":
    main()