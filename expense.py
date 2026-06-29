import csv

class Expense:
    def __init__(self, description, amount, category, date):
        self.description = description
        self.amount = amount
        self.category = category
        self.date = date

class ExpenseTracker:
    def __init__(self):
        self.expense_list = []


    def add_expense(self, description, amount, category, date):
        expense = Expense(description, amount, category, date)
        self.expense_list.append(expense)


    def show_all_expense(self):
        for i, item in enumerate(self.expense_list):
            print(f"{i}. {item.description} {item.amount} {item.category} {item.date}")

    def calculate_expense(self):
        res = 0
        for item in self.expense_list:
            res += item.amount
        print(res)


    def filter_expense(self, choise):

        if choise == 1: # category
            data = input("Enter category to filter: ")
            category_list = list(filter(lambda item : item.category.lower() == data.lower(), self.expense_list))
            for i, item in enumerate(category_list):
                print(f"{i}. {item.description} {item.amount} {item.category} {item.date}")

        elif choise == 2: # date
            data = input("Enter date to filter (e.g. 2022-01-01): ")
            date_list = list(filter(lambda item : item.date == data, self.expense_list))
            for i, item in enumerate(date_list):
                print(f"{i}. {item.description} {item.amount} {item.category} {item.date}")


    def file_save(self, filename="expense.csv"):
        with open(filename, 'w', newline="") as file:
            write = csv.writer(file)
            write.writerow(['description', 'amount', 'category', 'date'])
            for item in self.expense_list:
                write.writerow([item.description, item.amount, item.category, item.date])


    def load_file(self, filename="expense.csv"):
        with open(filename, 'r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                expense = Expense(
                    description=row['description'],
                    amount=float(row["amount"]),
                    category=row["category"],
                    date=row["date"]
                )
                self.expense_list.append(expense)
            
