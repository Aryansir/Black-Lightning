from . import *

from sqlalchemy import *

class bot_Sql(BASE):
    __tablename__ = "bot_Sql"
    id =  Column(Integer, primary_key=True)


bot_Sql.__table__.create(checkfirst=True)


def add_user(id):
    user =  bot_Sql(id=id)
    SESSION.add(user)
    SESSION.commit()
    SESSION.close()

def get_ids():
    i = ""
    for user in bot_Sql.__table__.columns.keys():
      i += "🐱‍👤" + "\n" + user  
    return i