from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session

from vakaavto.app import app


Base = declarative_base()

engine = create_engine(app.config['DATABASE_URI'], pool_recycle=600)

Session = sessionmaker(bind=engine)
session = scoped_session(lambda: Session(autoflush=False, expire_on_commit=False))


def remove_session(*args):
    session.rollback()
    session.remove()
