# Copyright (C) 2021 KeinShin@Github.



from . import *
from sqlalchemy import Column, String, Integer, text
# from sqlalchemy.orm import selectinload


class pm_sql(BASE):
    __tablename__ = "pm_sql"
    name = Column(String)
    id =  Column(Integer, primary_key=True)
    turns =  Column(Integer, primary_key=True)


pm_sql.__table__.create(checkfirst=True)

class get_id:
    def __init__(self, id):
      self.id = SESSION.query.get(id)



def approve_(id, name: str = None):
    if id:
      user =  pm_sql(id=id, turn=0)
      SESSION.add(user)
      SESSION.commit()
      SESSION.close()

    elif name:
      user =  pm_sql(name=name, turn=0)
      SESSION.add(user)
      SESSION.commit()
      SESSION.close()

def get_approve():
    i = ""
    for user in pm_sql.__table__.columns.keys():
      i += "\n" + user  
    return i

def dispprove(id = False, name: str = None):
    if id:
     name =  SESSION.query.get(id)
     SESSION.delete(name)
     SESSION.close()

    elif name:
     name =  SESSION.query.get(name)


     SESSION.delete(name)
     SESSION.close()

    
def get_user(id):
  
  return SESSION.query.get(id)


def his_turn(id):
    
    SESSION.query().\
        filter(pm_sql.id   == id).\
        update({pm_sql.turns: (pm_sql.turns +1)})
    SESSION.commit()


   
