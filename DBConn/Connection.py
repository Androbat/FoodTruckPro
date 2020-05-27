import sqlite3
import sqlalchemy as db

class DB_Conn():
    def __init__(self, *args, **kwargs):
        URL = 'sqlite:///FT_DB.sqlite'
        self.make_conn(URL)
    
    def make_conn(self,url):
        self.engine = db.create_engine(url, echo=True)
    
    def get_engine(self):
        return self.engine
