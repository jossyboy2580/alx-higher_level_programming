#!/usr/bin/python3
"""
A module that connects to a database and lists all
the states present
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State, Base


def show_states(usrname, passwd, db):
    """
    A function to show all states in a
    database
    """

    engine = create_engine(
             f"mysql+mysqldb://{usrname}:{passwd}@localhost/{db}"
             )

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    sess = Session()

    for row in sess.query(State).order_by(State.id).all():
        print(f'{row.id}: {row.name}')


if __name__ == '__main__':
    import sys

    if len(sys.argv) >= 4:
        username = sys.argv[1]
        password = sys.argv[2]
        db = sys.argv[3]
        show_states(username, password, db)
