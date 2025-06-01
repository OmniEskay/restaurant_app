from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base
from models.menu_item import MenuItem
from models.order import Order

engine = create_engine("sqlite:///restaurant.db")
Session = sessionmaker(bind=engine)
session = Session()

def init_db():
    Base.metadata.create_all(engine)
