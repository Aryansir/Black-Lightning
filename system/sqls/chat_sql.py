 # Copyright (C) 2021 KeinShin@Github.



from system.sqls import BASE, SESSION
from sqlalchemy import Column, String, Integer, text


class chat(BASE):
    __tablename__ = "chat"
    name = Column(String)
    channel = Column(String)
    user = Column(String)


chat.__table__.create(checkfirst=True)



def add_chat(name, channel):
    name =  chat(name=name, channel=channel)
    SESSION.add(name)
    SESSION.commit()



    SESSION.close()




def add_user(name):
    name =  chat(user=name, channel=name)
    SESSION.add(name)
    SESSION.commit()
    SESSION.close()
    

def get_chat(name):
      
  return SESSION.query.get(channel=name)

def chats(exsis=False):
    chaat = []
    for i in chat.__table__.columns.keys():
       chaat.append(i)
    if exsis and chaat.count == 0:
        return "no chats"
    else:

        return chaat  


def get_channel(name):
      
  return SESSION.query.get(name)


def exists(name = None, user=False):
    if user:
     k = SESSION.query(
    SESSION.query(chat).filter_by(user=user).exists()
).scalar()
    else:
     k = SESSION.query(
    SESSION.query(chat).filter_by(name=name).exists()
).scalar()
    return k
