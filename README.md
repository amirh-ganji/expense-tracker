# 💰 Expense Tracker

A simple command-line expense tracking application written in Python. Easily add, view, filter, and save your daily expenses.

## ✨ Features

- Add expenses with description, amount, category, and date
- View all recorded expenses
- Calculate total expenses
- Filter expenses by **category** or **date**
- Save expenses to a CSV file
- Load expenses from a previously saved CSV file

## 📁 Project Structure

```
expense-tracker/
├── main.py        # Entry point and menu interface
├── expense.py     # Expense and ExpenseTracker classes
├── expense.csv    # Auto-generated data file (created on save)
└── README.md      # Project documentation
```

## 🚀 Getting Started

### Prerequisites

- Python 3.x

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/YOUR_USERNAME/expense-tracker.git
   cd expense-tracker
   ```

2. Run the application:
   ```bash
   python main.py
   ```

## 🖥️ Usage

When you run the app, you'll see a menu like this:

```
--- Expense Tracker ---

1. Add Expense
2. Show All Expenses
3. Calculate Total Expense
4. Filter by Category
5. Filter by Date
6. Save to File
7. Load from File
8. Exit
```

### Example

```
Enter description: Coffee
Enter amount: 3.5
Enter category: Food
Enter date (e.g. 2025-08-07): 2025-08-07
```

Expenses are automatically saved to `expense.csv` when you exit.

## 💾 Data Storage

Expenses are stored in a local CSV file (`expense.csv`) with the following columns:

| description | amount | category | date |
|-------------|--------|----------|------|
| Coffee | 3.5 | Food | 2025-08-07 |

## 🤝 Contributing

Pull requests are welcome! Feel free to open an issue for suggestions or bug reports.

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
