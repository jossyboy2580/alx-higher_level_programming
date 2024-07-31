#!/usr/bin/python3
"""
A module with a function to insert a state into the
model State
"""
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


def add_state(username, password, db):
    """
    Adding a new state to the database has never been easier
    """
    engine = create_engine(
            f'mysql+mysqldb://{username}:{password}@localhost/{db}'
            )
    Session = sessionmaker(bind=engine)
    ss = Session()
    new = State()
    new.name = 'Louisiana'
    ss.add(new)
    ss.commit()
    print(f'{new.id}')


if __name__ == '__main__':
    import sys

    if len(sys.argv) >= 4:
        username = sys.argv[1]
        password = sys.argv[2]
        db = sys.argv[3]

        add_state(username, password, db)
