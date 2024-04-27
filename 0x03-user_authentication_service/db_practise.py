from sqlalchemy import create_engine
from sqlalchemy.orm.session import Session
engine = create_engine("sqlite:///a.db", echo=False)

session = Session(bind=engine)