#!/usr/bin/python3

""" A python script that connects to a DB and populates it with data"""

from sqlalchemy import  create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DECIMAL
from sqlalchemy.dialects.mysql import CHAR
from sqlalchemy.orm import sessionmaker
from uuid import uuid4
from sys import argv



Base = declarative_base()

# echo is a shortcut setting up SQLAlchemy logging (python's 'logging module')
# it (echo) generates all SQL output. Set it to False, for less output
# sqlite dialect interprets to the pythons sqlite3 module.
engine = create_engine(f'mysql+mysqlconnector://{argv[1]}:{argv[2]}@localhost/ALX_prodev', echo=True)

# return value of create_engine is an Engine instance


# connection successful
# Database ALX_prodev is present



class User(Base):
    """ Base users class """
    __tablename__ = 'user_data'

    # During actual class constructor, Declarative replaces Column with
    # python accessors know as descriptors. Process is know as instrumentation.
    # instrumentation makes it possible to refer to tabless in SQL context.
    user_id = Column(CHAR(36), primary_key=True, default=lambda: str(uuid4()), index=True)
    name = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False)
    age = Column(DECIMAL(10, 2), nullable= False)

    def __repr__(self):
        return f"<User(user_id='{self.user_id}', name='{self.name}', email='{self.email}', age='{self.age}')>"
    
def connect_db():
    """ Connects to the mysql server """
    Session = sessionmaker(bind=engine)

    # Whenever there is need for a converstation. a Session is instantiated
    # session = Session()

def create_database(connection):
    """ Creates a database ALX_prodev if it does not exist """
    pass

def create_table(connection):
    """ Creates a table user_data if it does not exist,
        with required fields
    """
    pass

def insert_data(connection, data):
    """ insert data in the database if it does not exist """
    pass
  
# Table user_data created successfully
# Inspect the table attribute(schema)
print(User.__table__)