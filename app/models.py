from sqlalchemy import Column, Integer, Date
from .db import Base

class Item(Base):
    __tablename__ = "egg_items"

    id = Column(Integer, primary_key=True, index=True)
    bad_count = Column(Integer, index=True)
    good_count = Column(Integer, index=True)
    date = Column(Date, index=True)
