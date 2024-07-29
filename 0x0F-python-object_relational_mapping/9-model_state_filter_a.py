#!/usr/bin/python3
"""
A module containing a function that shows
all states with the letter 'a'
"""
from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def all_states_with_a(username, password, db):
    """
    This module displays all states with the letter a
    """
    Session = sessionmaker()
    engine = create_engine(
            f'mysql+mysqldb://{username}:{password}@localhost/{db}'
            )
    Session.configure(bind=engine)
    ss = Session()

    for row in ss.query(State).filter(State.name.like('%a%')).all():
        print(f'{row.id}: {row.name}')


if __name__ == '__main__':
    import sys

    if len(sys.argv) >= 4:
        username = sys.argv[1]
        password = sys.argv[2]
        db = sys.argv[3]
        all_states_with_a(username, password, db)
