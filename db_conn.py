import sqlalchemy as db
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

# To use the ORM, we need to create a session maker
from sqlalchemy.orm import sessionmaker

from DBConn.Connection import DB_Conn
conn = DB_Conn()
engine = conn.get_engine()

# To create tables, we need to use to use the next object
Session = sessionmaker(bind=engine)
Base = declarative_base()












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



