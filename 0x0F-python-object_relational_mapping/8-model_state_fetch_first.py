#!/usr/bin/python3
"""
A module containing a function that prints the
first state in the database
"""
from model_state import State, Base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


def show_first_state(username, password, db):
    """
    A function that prints the first state
    """

    engine = create_engine(
            f'mysql+mysqldb://{username}:{password}@localhost/{db}'
            )
    Session = sessionmaker()
    Session.configure(bind=engine)

    sess = Session()
    obj = sess.query(State).order_by(State.id).first()
    if obj:
        print(f'{obj.id}: {obj.name}')
    else:
        print('Nothing')


if __name__ == '__main__':
    import sys

    if len(sys.argv) >= 4:
        username = sys.argv[1]
        password = sys.argv[2]
        db = sys.argv[3]
        show_first_state(username, password, db)
