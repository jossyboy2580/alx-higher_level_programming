#!/usr/bin/python3
"""
Get a paticular state
"""
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def get_a_state(username, password, db, state):
    """
    A function that gets a paticular state from the database
    """
    engine = create_engine(
            f'mysql+mysqldb://{username}:{password}@localhost/{db}'
            )
    Session = sessionmaker(bind=engine)
    ss = Session()
    res = ss.query(State).filter(State.name == state).first()
    if not res:
        print('Not found')
    else:
        print(f'{res.id}')


if __name__ == '__main__':
    import sys

    if len(sys.argv) >= 5:
        username = sys.argv[1]
        password = sys.argv[2]
        db = sys.argv[3]
        state = sys.argv[4]
        get_a_state(username, password, db, state)
