from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from db.setup import session
from models import Base
from tabulate import tabulate
from models.menu_item import MenuItem 

order_items = Table(
    'order_items', Base.metadata,
    Column('order_id', Integer, ForeignKey('orders.id')),
    Column('menu_item_id', Integer, ForeignKey('menu_items.id'))
)

class Order(Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True)
    customer_name = Column(String)
    items = relationship("MenuItem", secondary=order_items, backref="orders")

    def __repr__(self):
        return f"<Order(customer_name='{self.customer_name}')>"

    @classmethod
    def add(cls):
        name = input("Enter customer name: ")
        ids = input("Enter menu item IDs (comma separated): ")
        try:
            item_ids = [int(i.strip()) for i in ids.split(",")]
            menu_items = session.query(MenuItem).filter(MenuItem.id.in_(item_ids)).all()
            order = cls(customer_name=name, items=menu_items)
            session.add(order)
            session.commit()
            print("Order added.")
        except ValueError:
            print("Invalid item IDs.")

    @classmethod
    def view_all(cls):
        orders = session.query(cls).all()
        for order in orders:
            item_names = ", ".join(item.name for item in order.items)
            print(f"Order #{order.id} - {order.customer_name} - Items: {item_names}")

    @classmethod
    def edit(cls):
        id = input("Enter order ID to edit: ")
        order = session.query(cls).get(id)
        if order:
            name = input(f"Enter new name [{order.customer_name}]: ") or order.customer_name
            ids = input("Enter new item IDs (comma separated): ")
            try:
                item_ids = [int(i.strip()) for i in ids.split(",")]
                menu_items = session.query(MenuItem).filter(MenuItem.id.in_(item_ids)).all()
                order.customer_name = name
                order.items = menu_items
                session.commit()
                print("Order updated.")
            except ValueError:
                print("Invalid item IDs.")
        else:
            print("Order not found.")

    @classmethod
    def delete(cls):
        id = input("Enter order ID to delete: ")
        order = session.query(cls).get(id)
        if order:
            session.delete(order)
            session.commit()
            print("Order deleted.")
        else:
            print("Order not found.")