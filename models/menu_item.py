from sqlalchemy import Column, Integer, String, Float
from db.setup import session
from models import Base
from tabulate import tabulate

class MenuItem(Base):
    __tablename__ = 'menu_items'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    category = Column(String)
    price = Column(Float)

    def __repr__(self):
        return f"<MenuItem(name='{self.name}', category='{self.category}', price={self.price})>"

    @classmethod
    def add(cls):
        name = input("Enter item name: ")
        category = input("Enter category: ")
        try:
            price = float(input("Enter price: "))
            item = cls(name=name, category=category, price=price)
            session.add(item)
            session.commit()
            print("Item added.")
        except ValueError:
            print("Invalid price.")

    @classmethod
    def view_all(cls):
        items = session.query(cls).all()
        print(tabulate([[i.id, i.name, i.category, i.price] for i in items], headers=["ID", "Name", "Category", "Price"]))

    @classmethod
    def edit(cls):
        id = input("Enter item ID to edit: ")
        item = session.query(cls).get(id)
        if item:
            item.name = input(f"Enter new name [{item.name}]: ") or item.name
            item.category = input(f"Enter new category [{item.category}]: ") or item.category
            try:
                new_price = input(f"Enter new price [{item.price}]: ")
                if new_price:
                    item.price = float(new_price)
                session.commit()
                print("Item updated.")
            except ValueError:
                print("Invalid price.")
        else:
            print("Item not found.")

    @classmethod
    def delete(cls):
        id = input("Enter item ID to delete: ")
        item = session.query(cls).get(id)
        if item:
            session.delete(item)
            session.commit()
            print("Item deleted.")
        else:
            print("Item not found.")

    @classmethod
    def search(cls):
        term = input("Search by name or category: ").lower()
        results = session.query(cls).filter((cls.name.ilike(f"%{term}%")) | (cls.category.ilike(f"%{term}%"))).all()
        if results:
            print(tabulate([[i.id, i.name, i.category, i.price] for i in results], headers=["ID", "Name", "Category", "Price"]))
        else:
            print("No items found.")