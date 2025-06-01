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

def view_menu_items():
    items = session.query(MenuItem).all()
    if items:
        table = [[i.id, i.name, i.category, i.price] for i in items]
        print(tabulate(table, headers=["ID", "Name", "Category", "Price"]))
    else:
        print("📭 No menu items found.")

def delete_menu_item():
    try:
        item_id = int(input("Enter item ID to delete: "))
    except ValueError:
        print("❌ Invalid ID.")
        return

    item = session.query(MenuItem).get(item_id)
    if item:
        session.delete(item)
        session.commit()
        print(f"🗑️ Menu item '{item.name}' deleted.")
    else:
        print("❌ Item not found.")