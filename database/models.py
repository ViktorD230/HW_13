from sqlalchemy import Column, Integer, String, Date, func
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import DateTime

Base = declarative_base()

#create model
class Contact(Base):
    __tablename__ = "contacts"
    id = Column(Integer, primary_key=True)
    first_name = Column(String(25), nullable=True)
    last_name = Column(String(25), nullable=True)
    email = Column(String(30), nullable=False, unique=True)
    phone = Column(String(13), nullable=False)
    date_birthday = Column(Date, nullable=False)
    user_id = Column('user_id', ForeignKey('users.id', ondelete='CASCADE'), default=None)
    user = relationship('User', backref="notes")


#create model for table users
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String(16))
    email = Column(String(100), nullable=False, unique=True)
    password = Column(String(10), nullable=False)
    created_at = Column('crated_at', DateTime, default=func.now())
    refresh_token = Column(String(255), nullable=True)