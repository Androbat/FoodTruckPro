import sqlalchemy as db
from sqlalchemy.ext.declarative import declarative_base
from models import Base, User
# To use the ORM, we need to create a session maker
from sqlalchemy.orm import sessionmaker
URL = 'sqlite:///db.sqlite3'
engine = db.create_engine(URL,echo=True)
# To create tables, we need to use to use the next object
Session = sessionmaker(bind=engine)
session = Session()
Base.metadata.create_all(engine)











# import sqlite3
# import sqlalchemy as db

# # To use the ORM, we need to create a session maker
# from sqlalchemy.orm import sessionmaker
# # To create tables, we need to use to use the next object
# from sqlalchemy.ext.declarative import declarative_base

# from sqlalchemy import Column, Integer, String


# engine = db.create_engine('sqlite:///FT_DB.sqlite', echo=True)
# con = engine.connect()
# Session = sessionmaker(bind=engine)
# Base = declarative_base()



