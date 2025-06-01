from db.setup import session
from models.menu_item import MenuItem
from models.order import Order
from tabulate import tabulate

def add_menu_item():
    name = input("Enter item name: ")
    category = input("Enter category: ")
    try:
        price = float(input("Enter price: "))
    except ValueError:
        print("❌ Invalid price.")
        return

    item = MenuItem(name=name, category=category, price=price)
    if not item.is_valid:
        print("❌ Price must be greater than 0.")
        return

    session.add(item)
    session.commit()
    print(f"✅ '{name}' added to menu.")