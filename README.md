# 🍽️ Restaurant Menu & Orders CLI App

A Python command-line application that helps manage a restaurant's menu and customer orders using SQLAlchemy and a local SQLite database. The app features a friendly CLI interface to perform CRUD operations on menu items and orders.

---

## 🧠 Features

- Add, view, and delete **Menu Items**
- Add, view, and delete **Orders**
- See all orders with associated menu items
- View all menu items with prices and categories
- Input validation with helpful feedback
- All data stored in a persistent SQLite database

---

## 🏗️ Project Structure

```
restaurant_app/
├── cli/
│   └── main_cli.py          # CLI menus and logic
│
├── db/
│   └── setup.py             # SQLAlchemy engine and session setup
│
├── models/
│   ├── __init__.py          # SQLAlchemy Base definition
│   ├── menu_item.py         # MenuItem model
│   └── order.py             # Order model with relationship
│
├── main.py                  # Application entry point
├── Pipfile                  # Project dependencies
├── README.md                # This file
└── .gitignore               # Git ignored files
```

---

## 🚀 Getting Started

### 🔧 Prerequisites

- Python 3.10+
- Pipenv (install with `pip install pipenv`)

### 📦 Install Dependencies

```bash
pipenv install
```

### ▶️ Run the Application

```bash
pipenv run python main.py
```

You will see a CLI menu like:

```
📋 Restaurant CLI
1. Add Menu Item
2. View Menu Items
3. Delete Menu Item
4. Add Order
5. View Orders
6. Delete Order
7. Exit
```

---

## 🗄️ Technologies Used

- **Python 3.10+**
- **SQLAlchemy** – ORM for Python
- **SQLite** – Lightweight relational database
- **Tabulate** – CLI table formatting

---

## 📌 Minimum Viable Product (MVP)

1. Create and list menu items
2. Add and list customer orders
3. Delete menu items and orders
4. Validate user input with meaningful error messages
5. Keep user in the CLI loop until they choose to exit


---

## 👨‍🍳 Author

Created by Kitolo Samuel. Contributions welcome!