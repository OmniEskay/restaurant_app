from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from models import Base

class Order(Base):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True)
    customer_name = Column(String, nullable=False)
    menu_item_id = Column(Integer, ForeignKey('menu_items.id'))
    menu_item = relationship("MenuItem", backref="orders")
