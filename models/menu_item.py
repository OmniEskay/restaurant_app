from sqlalchemy import Column, Integer, String, Float
from models import Base

class MenuItem(Base):
    __tablename__ = 'menu_items'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    category = Column(String, nullable=False)
    price = Column(Float, nullable=False)

    def __repr__(self):
        return f"<MenuItem(id={self.id}, name='{self.name}', category='{self.category}', price={self.price})>"

    @property
    def is_valid(self):
        return self.price > 0
