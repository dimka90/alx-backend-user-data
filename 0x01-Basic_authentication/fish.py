from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
engine = create_engine('sqlite:///sales.db', echo = True)
Base = declarative_base()

class Customer(Base):
    __tablename__ = "customers"
    id = Column(Integer, primary_key = True)
    name = Column(String)

Base.metadata.create_all(engine)
