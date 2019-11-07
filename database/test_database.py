from sqlalchemy import Column, DateTime, String, Integer, ForeignKey, func
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


Base = declarative_base()


class Users(Base):
    __tablename__ = "users"
    id = Column(Integer, primery_key=True)
    name = Column(String)
    phone = Column(String)
    instagram = Column(String)



engine = create_engine('sqlite:///testUsers.sqlite')
session = sessionmaker()
session.configure(bind=engine)
Base.metadata.create_all(engine)
