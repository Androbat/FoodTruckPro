#run python app.py to populate the database

from main import session
from models import User

u1 = User(name="Anabel", 
            lastname="Ferreira",
            type=1)

u2 = User(name="Bob", 
            lastname="Ferreira",
            type=1)

u3 = User(name="Bil", 
            lastname="Ferreira",
            type=1)

u4 = User(name="Cristhian", 
                lastname="Ferreira",
                type=1)

session.add(u1)
session.add(u2)
session.add(u3)

session.commit()

print(u1,u2,u3)