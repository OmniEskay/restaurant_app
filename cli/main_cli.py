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

def add_order():
    customer = input("Enter customer name: ")
    view_menu_items()
    try:
        item_id = int(input("Enter menu item ID to order: "))
    except ValueError:
        print("❌ Invalid ID.")
        return

    item = session.query(MenuItem).get(item_id)
    if not item:
        print("❌ Menu item not found.")
        return

    order = Order(customer_name=customer, menu_item=item)
    session.add(order)
    session.commit()
    print(f"✅ Order placed for {customer}: {item.name}")

def view_orders():
    orders = session.query(Order).all()
    if orders:
        table = [[o.id, o.customer_name, o.menu_item.name, o.menu_item.price] for o in orders]
        print(tabulate(table, headers=["Order ID", "Customer", "Item", "Price"]))
    else:
        print("📭 No orders found.")

def delete_order():
    try:
        order_id = int(input("Enter order ID to delete: "))
    except ValueError:
        print("❌ Invalid ID.")
        return

    order = session.query(Order).get(order_id)
    if order:
        session.delete(order)
        session.commit()
        print(f"🗑️ Order #{order_id} deleted.")
    else:
        print("❌ Order not found.")

def run_cli():
    while True:
        print("\n📋 Restaurant CLI")
        print("1. Add Menu Item")
        print("2. View Menu Items")
        print("3. Delete Menu Item")
        print("4. Add Order")
        print("5. View Orders")
        print("6. Delete Order")
        print("7. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            add_menu_item()
        elif choice == "2":
            view_menu_items()
        elif choice == "3":
            delete_menu_item()
        elif choice == "4":
            add_order()
        elif choice == "5":
            view_orders()
        elif choice == "6":
            delete_order()
        elif choice == "7":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice.")