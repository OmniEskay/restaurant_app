from models.menu_item import MenuItem
from models.order import Order
from db.setup import session
from tabulate import tabulate

def run_cli():
    while True:
        print("\n\U0001F4CB Restaurant CLI")
        print("1. Add Menu Item")
        print("2. View Menu Items")
        print("3. Edit Menu Item")
        print("4. Delete Menu Item")
        print("5. Add Order")
        print("6. View Orders")
        print("7. Edit Order")
        print("8. Delete Order")
        print("9. Search Menu Items")
        print("10. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            MenuItem.add()
        elif choice == "2":
            MenuItem.view_all()
        elif choice == "3":
            MenuItem.edit()
        elif choice == "4":
            MenuItem.delete()
        elif choice == "5":
            Order.add()
        elif choice == "6":
            Order.view_all()
        elif choice == "7":
            Order.edit()
        elif choice == "8":
            Order.delete()
        elif choice == "9":
            MenuItem.search()
        elif choice == "10":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")