#!/usr/bin/python3
"""
A class definition of a State and an instance of
Base = declarative_base()
"""
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

"""
engine = create_engine('mysql+mysqldb://py_alch:jossy@' +
                       'localhost:3306/test_alchemy')
"""
Base = declarative_base()


class State(Base):
    """
    A class State that inherits from Base
    """
    __tablename__ = 'states'

    id = Column('id', Integer, primary_key=True)
    name = Column('name', String(128), nullable=False)


#  Base.metadata.create_all(engine)
