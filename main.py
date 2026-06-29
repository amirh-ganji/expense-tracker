from expense import ExpenseTracker

def main():
    tracker = ExpenseTracker()

    while True:
        print("\n--- Expense Tracker ---")
        print("\n1. Add Expense")
        print("2. Show All Expenses")
        print("3. Calculate Total Expense")
        print("4. Filter by Category")
        print("5. Filter by Date")
        print("6. Save to File")
        print("7. Load from File")
        print("8. Exit")

        choice = input("\nEnter the number of the option you want to select: ")

        if choice == "1":
            description = input("Enter description: ")
            amount = float(input("Enter amount: "))
            category = input("Enter category: ")
            date = input("Enter date (e.g. 2025-08-07): ")
            tracker.add_expense(description, amount, category, date)

        elif choice == "2":
            tracker.show_all_expense()

        elif choice == "3":
            tracker.calculate_expense()

        elif choice == "4":
            tracker.filter_expense(1)

        elif choice == "5":
            tracker.filter_expense(2)

        elif choice == "6":
            tracker.file_save()
            print("Expenses saved successfully.")

        elif choice == "7":
            tracker.load_file()
            print("Expenses loaded successfully.")

        elif choice == "8":
            tracker.file_save()
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please try again.")


if __name__ == ('__main__'):
    main()