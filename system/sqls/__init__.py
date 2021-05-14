from Config import Variable
import os
import logging
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker



def start() -> scoped_session:
    engine = create_engine(Variable.DATABASE_URL)
    BASE.metadata.bind = engine
    BASE.metadata.create_all(engine)
    return scoped_session(sessionmaker(bind=engine, autoflush=False))


try:
    BASE = declarative_base()
    SESSION = start()
except AttributeError as e:
    logging.error(e)